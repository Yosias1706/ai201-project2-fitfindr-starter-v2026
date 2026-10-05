"""
The three FitFindr tools.

Each one is a standalone function you can call and test on its own, before any
of them are wired into the loop. Build and test them one at a time — three
untested tools joined by a loop is one problem that looks like six, because you
can't tell which layer is lying to you.

    search_listings(description, size, max_price)  → list[dict]
    suggest_outfit(new_item, wardrobe)             → str
    create_fit_card(outfit, new_item)              → str

All three are stubs right now. They run and they do nothing — that's the
starting position and it's deliberate.

⚠️ Before you write any of them, fill in the **Tool Inventory** section of your
README (Milestone 2). Four lines per tool: what it does, each input with its
type, exactly what it returns, and what it returns when it has nothing to give.
That last line is what your loop branches on. "Returns a list" earns nothing —
the description has to say what is *in* the list.
"""

import re
import config  # noqa: F401 — you'll use this in search_listings
from generate import generate
from utils.data_loader import load_listings


# ── Tool 1: search_listings ───────────────────────────────────────────────────

_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "from", "has", "he", "in", "is", "it", "its", "of", "on", "that", "the", "to", "was", "in", "with", "without" }

def _keywords(text:str) -> set[str]:
    """Lowercase words worth matching on, stopwords removed"""
    words = re.findall(r"[a-z0-9']+", (text or "").lower())
    return  {w for w in words if w not in _STOPWORDS and len(w) > 1}
def _size_tokens(size: str) -> set[str]:
    """Whole size tokens, so "M" matches "S/M" but "S" never matches "US 9"."""
    cleaned = re.sub(r"\([^)]*\)", "", size or "")
    parts = re.split(r"[/\s]+", cleaned.upper())
    return {p for p in parts if p}

def _size_matches(wanted: str, listing_size: str) -> bool:
    if not wanted:
        return True
    if (listing_size or "").upper().startswith("ONE SIZE"):
        return True
    return bool(_size_tokens(wanted) & _size_tokens(listing_size))

def _score(words: set[str], listing: dict) -> int:
    """Keyword overlap. Title and style tags count double; description once."""
    strong = _keywords(" ".join([
        listing.get("title", ""),
        " ".join(listing.get("style_tags") or []),
        listing.get("category", ""),
        " ".join(listing.get("colors") or []),
        listing.get("brand") or "",
    ]))
    weak = _keywords(listing.get("description", ""))
    return 2 * len(words & strong) + len(words & weak)



def search_listings(
    description: str,
    size: str | None = None,
    max_price: float | None = None,
) -> list[dict]:
    """
    Search the listings data for items matching a description, and optionally a
    size and a price ceiling.

    This is the tool that doesn't call the model, which makes it the easiest one
    to test and the one to move onto MCP in unit 4.

    Args:
        description: keywords describing what the user wants
                     (e.g. "vintage graphic tee").
        size:        a size string to filter by, or None to skip size filtering.
                     Match case-insensitively — "M" should match "S/M".

                     ⚠️ Read the sizes in the data before you reach for a plain
                     substring test. `"s" in "us 9"` is True, and so is
                     `"l" in "xl"`. A filter that returns shoes when someone
                     asked for a small top reads like a broken search, and it
                     will quietly cost you in unit 4 when you test criterion 1.
                     What counts as a size match is part of your spec — decide
                     it and write it into your Tool Inventory.
        max_price:   maximum price, inclusive, or None to skip price filtering.

    Returns:
        A list of matching listing dicts, best match first.
        **Returns an empty list when nothing matches — an empty list, not None,
        and not an exception.** Your loop branches on this.

    Each listing dict has these fields:
        id, title, description, category, style_tags (list), size,
        condition, price (float), colors (list), brand (str or None), platform

    Note that `brand` is None for most listings. That is deliberate and
    realistic — thrift listings often have no brand. If something you write
    assumes a brand is always there, you will find out in unit 4.

    TODO:
        1. Load every listing with load_listings().
        2. Filter by max_price and by size, when each is provided.
        3. Score what's left by keyword overlap with `description`.
        4. Drop anything scoring zero.
        5. Sort by score, highest first, and return the listing dicts —
           at most config.SEARCH_RESULT_LIMIT of them.

    Test it from a terminal before you move on:
        python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"
    """
    words = _keywords(description)
    if not words:
        return []

    scored = []
    for listing in load_listings():
        if max_price is not None and listing["price"] > max_price:
            continue
        if not _size_matches(size, listing["size"]):
            continue
        score = _score(words, listing)
        if score > 0:
            scored.append((score, listing))

    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [listing for _, listing in scored[:config.SEARCH_RESULT_LIMIT]]


# ── Tool 2: suggest_outfit ────────────────────────────────────────────────────

def suggest_outfit(new_item: dict, wardrobe: dict) -> str:
    """
    Given a thrifted item and the user's wardrobe, suggest one or two outfits.

    This one calls the model, through `generate()`. You don't need to think
    about rate limits — the adapter handles pacing for you.

    Args:
        new_item: a listing dict — the item the user is considering.
        wardrobe: a wardrobe dict with an 'items' key holding a list of items.
                  **It may be empty.** Handle that.

    Returns:
        A non-empty string with outfit suggestions.
        With an empty wardrobe, return general styling advice rather than
        raising or returning "". Unit 4 has you trigger the empty wardrobe on
        purpose, so decide now what it should do.

    TODO:
        1. Check whether wardrobe['items'] is empty.
        2. If it is, ask the model for general styling ideas for this item.
        3. If it isn't, format the wardrobe items into the prompt and ask for
           specific combinations naming pieces the user already owns.
        4. Return the model's response.

    Test it from a terminal before you move on:
        python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"
    """
    item = _describe_item(new_item)
    items = (wardrobe or {}).get("items") or []

    if not items:
        prompt = (
            f"Someone is thinking about buying this thrifted item:\n{item}\n\n"
            "They haven't saved any of their wardrobe yet. Give general styling "
            "advice: one or two outfits built around this item, naming the kinds "
            "of pieces that would go with it. Keep it under 120 words."
        )
    else:
        owned = "\n".join(
            f"- {w.get('name')} ({', '.join(w.get('colors') or [])})" for w in items
        )
        prompt = (
            f"Someone is thinking about buying this thrifted item:\n{item}\n\n"
            f"Here is what they already own:\n{owned}\n\n"
            "Suggest one or two outfits that pair the new item with specific "
            "pieces from their wardrobe, naming those pieces. Keep it under 120 words."
        )

    response = generate(prompt, system="You are a practical thrift stylist.")
    return response.strip() or f"Style the {new_item.get('title', 'item')} with simple basics in neutral colors."


# ── Tool 3: create_fit_card ───────────────────────────────────────────────────

def create_fit_card(outfit: str, new_item: dict) -> str:
    """
    Write a short caption someone would actually post about the find.

    This calls the model too.

    Args:
        outfit:   the outfit suggestion string from suggest_outfit().
        new_item: the listing dict for the item.

    Returns:
        A two-to-four sentence caption.
        If `outfit` is empty or whitespace, return a descriptive message rather
        than raising.

    The caption should read like a real post rather than a product description,
    mention the item and its price and platform once each, and be specific about
    the vibe.

    It should also come out **differently for different inputs**. If you run
    this three times on the same item and get three word-for-word identical
    strings, it's one of two things, and both are near the top of `config.py`:

        • CACHE_ENABLED — the adapter handed back an answer it already had
        • TEMPERATURE   — at 0.0 the model gives the same words every time

    TODO:
        1. Guard against an empty or whitespace-only `outfit`.
        2. Build a prompt with the item details and the outfit.
        3. Call generate() and return the response.

    Test it from a terminal before you move on:
        python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"
    """
    if not outfit or not outfit.strip():
        return "No outfit suggestion to build a fit card from — run suggest_outfit first."

    prompt = (
        f"The find:\n{_describe_item(new_item)}\n\n"
        f"How it'll be styled:\n{outfit}\n\n"
        "Write a caption someone would actually post about this thrift find. "
        "Two to four sentences. Mention the item, its price (as $ and a number) "
        "and the platform once each, and be specific about the vibe. "
        "Return only the caption."
    )
    return generate(prompt, system="You write short, casual social media captions.").strip()


def _describe_item(item: dict) -> str:
    """The listing fields the model needs, skipping brand when there isn't one."""
    lines = [
        f"Title: {item.get('title')}",
        f"Category: {item.get('category')}",
        f"Size: {item.get('size')}",
        f"Condition: {item.get('condition')}",
        f"Colors: {', '.join(item.get('colors') or [])}",
        f"Style: {', '.join(item.get('style_tags') or [])}",
        f"Price: ${item.get('price', 0):.0f}",
        f"Platform: {item.get('platform')}",
    ]
    if item.get("brand"):
        lines.insert(1, f"Brand: {item['brand']}")
    return "\n".join(lines)
