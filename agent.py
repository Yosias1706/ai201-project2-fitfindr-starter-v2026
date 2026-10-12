"""
The FitFindr planning loop.

This is the file that makes FitFindr an agent rather than a script. It decides
which tool to run next based on what the last one returned.

If your loop calls all three tools no matter what comes back, you have a list
of function calls. A loop looks at the last result before it picks the next
step. **That branch is the graded part of this unit.**

Build and test your three tools in `tools.py` first. Then come here.

    python agent.py          runs both example paths below
"""

import re

import config
import trace
from tools import search_listings, suggest_outfit, create_fit_card
from generate import ModelUnavailable
from mcp_client import MCPError


# ── session state ─────────────────────────────────────────────────────────────

def new_session(query: str, wardrobe: dict) -> dict:
    """
    A fresh session for one user interaction.

    The session is the single source of truth for a run. Every tool result goes
    in here, and the next tool reads it back out.

    You could pass values straight from one call to the next. It would work,
    and you would not be able to test it — you can't print a variable you have
    already overwritten. Going through the session is what makes the state
    visible, and unit 4 has you write a criterion about exactly that.

    Add fields if you need them.
    """
    return {
        "query": query,              # what the user typed
        "parsed": {},                # description / size / max_price you pulled out of it
        "search_results": [],        # everything search_listings returned
        "selected_item": None,       # the one you chose — goes into suggest_outfit
        "wardrobe": wardrobe,        # the user's wardrobe
        "outfit_suggestion": None,   # what suggest_outfit returned
        "fit_card": None,            # what create_fit_card returned
        "error": None,               # set when the run ended early
    }


# ── planning loop ─────────────────────────────────────────────────────────────

def run_agent(query: str, wardrobe: dict) -> dict:
    """
    Run the loop once and return the finished session.

    Args:
        query:    what the user asked for, in plain language
                  (e.g. "vintage graphic tee under $30, size M").
        wardrobe: a wardrobe dict — get_example_wardrobe() or
                  get_empty_wardrobe() from utils/data_loader.py.

    Returns:
        The session dict. **Check session["error"] first** — if it isn't None,
        the run ended early and the later fields will still be None.

    ─────────────────────────────────────────────────────────────────────────
    TODO — build this, following the branch rule you wrote in Milestone 2.

      1. Start a session with new_session().

      2. Count the times round the loop, and call trace.check_iterations(count)
         on each one before you go again. It raises when the count passes
         MAX_ITERATIONS in config.py — see trace.py.

      3. Parse the query into a description, a size, and a max_price. Regex,
         string splitting, or asking the model are all fine — say which you
         chose in your README. Put the result in session["parsed"].

      4. Call search_listings() with what you parsed.
         Put the results in session["search_results"].

         ⚠️ THIS IS THE BRANCH. If nothing came back:
              - put a message in session["error"] saying what the user could
                change — "No results" is not that message
              - return the session
              - do NOT call suggest_outfit with nothing

      5. Choose an item — the first result is fine. Put it in
         session["selected_item"].

      6. Call suggest_outfit() with the selected item and the wardrobe.
         Put the result in session["outfit_suggestion"].

      7. Call create_fit_card() with the outfit and the item.
         Put the result in session["fit_card"].

      8. Return the session.

    ─────────────────────────────────────────────────────────────────────────
    IN UNIT 4 you come back and add two things:

      • Trace calls. One per step. `trace.step("search_listings", inputs=...,
        returned=...)` — see trace.py. Your README needs the output.

      • A handler for ModelUnavailable, so a bad key produces a message rather
        than a stack trace. The import is already at the top of this file.
    """
    session = new_session(query, wardrobe)
    session["parsed"] = parse_query(query)
    trace.step("parse_query", inputs=query, returned=session["parsed"])

    count = 0
    next_step = "search"
    try:
        while next_step != "done":
            count += 1
            trace.check_iterations(count)

            if next_step == "search":
                from mcp_client import call_tool
                parsed = session["parsed"]
                args = {
                    "description": parsed["description"],
                    "size": parsed["size"],
                    "max_price": parsed["max_price"],
                }
                session["search_results"] = call_tool("search_listings", args) or []
                # The branch: nothing found means stop here, before any model call.
                if not session["search_results"]:
                    session["error"] = _no_results_message(parsed)
                    trace.step("search_listings (via MCP)", inputs=args,
                               returned=session["search_results"],
                               note="branch: empty, stopping before suggest_outfit")
                    next_step = "done"
                else:
                    session["selected_item"] = session["search_results"][0]
                    trace.step("search_listings (via MCP)", inputs=args,
                               returned=session["search_results"],
                               note="branch: results found, selecting the first")
                    next_step = "suggest"

            elif next_step == "suggest":
                item = session["selected_item"]
                wardrobe_items = (session["wardrobe"] or {}).get("items") or []
                session["outfit_suggestion"] = suggest_outfit(item, session["wardrobe"])
                trace.step("suggest_outfit",
                           inputs={"item": item, "wardrobe_items": len(wardrobe_items)},
                           returned=session["outfit_suggestion"],
                           note="" if wardrobe_items else "empty wardrobe: general styling advice")
                next_step = "fit_card"

            elif next_step == "fit_card":
                session["fit_card"] = create_fit_card(
                    session["outfit_suggestion"], session["selected_item"]
                )
                trace.step("create_fit_card",
                           inputs={"outfit": session["outfit_suggestion"],
                                   "item": session["selected_item"]},
                           returned=session["fit_card"])
                next_step = "done"
    except ModelUnavailable as exc:
        session["error"] = (
            f"The model couldn't be reached, so FitFindr stopped before finishing. "
            f"{exc} Fix that and ask again."
        )
        trace.step("model unavailable", returned=str(exc), note="stopping")
    except MCPError as exc:
        session["error"] = (
            f"The search tool couldn't be reached, so nothing was searched. {exc}"
        )
        trace.step("search_listings (via MCP)", returned=str(exc), note="MCP failed, stopping")

    return session


# ── query parsing (regex) ─────────────────────────────────────────────────────

_PRICE = re.compile(
    r"(?:under|below|less than|max|up to|<)\s*\$?\s*(\d+(?:\.\d+)?)|\$(\d+(?:\.\d+)?)",
    re.I,
)
_SIZE = re.compile(r"\bsize\s+((?:US\s*)?[A-Za-z0-9.]+(?:/[A-Za-z0-9.]+)?(?:\s+L\d+)?)", re.I)
_FILLER = re.compile(
    r"\b(?:i'?m|i am|looking for|i want|i need|find me|show me|something|some|please)\b",
    re.I,
)


def parse_query(query: str) -> dict:
    """
    Pull a description, a size and a max_price out of plain language.

    "vintage graphic tee under $30, size M"
        → {"description": "vintage graphic tee", "size": "M", "max_price": 30.0}
    """
    text = query or ""

    max_price = None
    price = _PRICE.search(text)
    if price:
        max_price = float(price.group(1) or price.group(2))
        text = text[:price.start()] + " " + text[price.end():]

    size = None
    size_match = _SIZE.search(text)
    if size_match:
        size = size_match.group(1).strip()
        text = text[:size_match.start()] + " " + text[size_match.end():]

    text = _FILLER.sub(" ", text)
    description = " ".join(re.sub(r"[^\w'$-]+", " ", text).split())

    return {"description": description, "size": size, "max_price": max_price}


def _no_results_message(parsed: dict) -> str:
    """Say what the user could change, using the filters they actually set."""
    asked = f"'{parsed['description']}'" if parsed["description"] else "your search"
    if parsed["size"]:
        asked += f" in size {parsed['size']}"
    if parsed["max_price"] is not None:
        asked += f" under ${parsed['max_price']:.0f}"

    tips = []
    if parsed["max_price"] is not None:
        tips.append("raise the price limit")
    if parsed["size"]:
        tips.append("drop the size or try a neighbouring one")
    tips.append("use broader words, like 'dress' instead of 'ballgown'"
                if parsed["description"] else "describe the item, like 'denim jacket'")

    if len(tips) > 1:
        tips[-1] = "or " + tips[-1]
    return f"Nothing matched {asked}. Try to {', '.join(tips)}."


# ── running it directly ───────────────────────────────────────────────────────

def _show(session: dict) -> None:
    if session["error"]:
        print(f"  stopped: {session['error']}")
        print(f"  fit_card is {session['fit_card']!r} — it should still be None here")
        return

    item = session["selected_item"] or {}
    print(f"  found:    {item.get('title')} — ${item.get('price')} on {item.get('platform')}")
    print(f"  outfit:   {session['outfit_suggestion']}")
    print(f"  fit card: {session['fit_card']}")


if __name__ == "__main__":
    from utils.data_loader import get_example_wardrobe

    print("=== A query the data can match ===")
    _show(run_agent(
        query="looking for a vintage graphic tee under $30",
        wardrobe=get_example_wardrobe(),
    ))

    print("\n=== A query it can't ===")
    _show(run_agent(
        query="designer ballgown size XXS under $5",
        wardrobe=get_example_wardrobe(),
    ))

    print(
        "\nThe second one should stop before the fit card. If both paths look "
        "the same,\nthe branch isn't doing anything yet."
    )
