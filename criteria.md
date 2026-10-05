# Acceptance criteria — FitFindr

Five criteria that say what "working" means for this agent, written in unit 3
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"The agent handles errors"* is an opinion.
*"When search returns nothing, the agent stops before calling the second tool,
in 5 of 5 tries"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter one. A reason that says something about your tools, your loop, or the
data earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

**Two are written for you. You write three.**

---

## 1. A matching query completes all three tools

Given a query that matches at least one listing, the agent completes all three
tool calls and returns a fit card — in at least 4 of 5 tries.

**Why this target:**
<!-- Why 4 of 5 and not 5 of 5? Something about your search, probably —
     "my search is a plain keyword match and some phrasings will miss" is a
     real answer. -->

`search_listings` is a plain keyword-overlap score with stopwords removed — no
stemming or synonyms — so a phrasing like "tees" vs "tee" or "t-shirt" vs
"graphic tee" can score zero even when a matching listing exists, and the regex
parser can mis-pull a size or price out of the query. Two of the three tools
also call the model, so one of five tries can fail on a model hiccup. 5 of 5
would pretend the keyword match and regex parsing never miss; anything below
4 of 5 would mean the happy path is genuinely broken.

---

## 2. An impossible query stops before the second tool

Given a query that matches no listings, the agent stops before calling
`suggest_outfit` and returns a message naming what to change — 5 of 5 tries.

**Why this target:**
<!-- Why is 5 of 5 reasonable here when criterion 1 isn't? What's different
     about this path? -->

This path never touches the model. `search_listings` is deterministic — the
same parsed query against the same `listings` data returns the same empty list
every time — and the branch in `agent.py::run_agent` is a single `if not
results` check. There's no randomness anywhere on this path, so a single
failure means the branch or the price/size filter is wrong, not unlucky.

---

## 3. The item search found is the item every later tool received

Given a matching query, the `id` of `session["selected_item"]` equals the `id`
of `session["search_results"][0]`, equals the `id` of the `new_item` that
`suggest_outfit` and `create_fit_card` actually received (as logged by
`trace.step`), and the `outfit` string `create_fit_card` received is exactly
`session["outfit_suggestion"]` — all four checks hold in 5 of 5 tries.

**Why this target:**
Nothing on this path is random: the hand-off is just reads and writes on the
session dict, so if the loop is wired right it is right every time and 5 of 5
is the only honest target. It isn't free, though — it's easy to pass a
different variable than the one stored (a stale `results[0]` from an earlier
line, or the outfit text before it was saved), and that bug would look like a
bad outfit or a wrong caption rather than a state problem. Comparing `id`s at
each hand-off is what makes it countable instead of a judgment call.

---

## 4. The fit card is a postable caption with the real details

Given a matching query, the fit card is 2–4 sentences (counted by splitting on
`.`, `!`, `?`), under 400 characters, contains the selected item's price as
`$` + its whole-dollar amount (e.g. `$24` for 24.0), and names its `platform`
(case-insensitive) — all four true in at least 4 of 5 tries.

**Why this target:**
`create_fit_card`'s docstring asks for exactly this: two to four sentences,
price and platform mentioned, reading like a post rather than a product
description. At TEMPERATURE 0.9 the model will sometimes run long, drop the
price, or write "24 bucks" instead of `$24`, and emoji or "..." can throw off
the sentence count, so 5 of 5 isn't realistic for model output. But the prompt
hands it the price and platform directly, so missing them more than once in
five means the prompt isn't doing its job.

---

## 5. A matching query finishes in under 10 seconds

Given a matching query, `run_agent` returns a completed session (fit card set,
no error) in under 10 seconds of wall-clock time, measured with
`time.perf_counter()` around the call — in at least 4 of 5 tries.

**Why this target:**
`search_listings` is local and runs in well under a second, so the time is
almost all the two `generate()` calls (`suggest_outfit` and
`create_fit_card`); on `gemini-3.5-flash-lite` each is normally a few seconds,
so a typical run should land around 3–6 seconds and 10 leaves room for normal
latency. It isn't 5 of 5 because `config.py` caps us at 15 requests per
minute: five back-to-back tries is 10 model calls, and one rate-limit pause or
a retry in `generate.py` can add tens of seconds to a single try. More than one
slow try, though, would mean the prompts are too long or the loop is making
calls it doesn't need.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 4 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 4. Something about the fit card

         The fit card is different every time.

         **Why this target:** ...

         > **Revised in unit 4:** For 5 different items, the 5 fit cards share
         > no opening sentence.
         >
         > **Why revised:** "different" wasn't checkable — two cards that
         > differed by one word still counted. The new version is something I
         > can actually score.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said the empty search stops it 5 of 5 times, but I got 3 of 5,
            so 3 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
