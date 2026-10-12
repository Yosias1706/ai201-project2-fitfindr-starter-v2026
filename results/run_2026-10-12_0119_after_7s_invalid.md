# Run log — after

- Produced by: `run_eval.py::main`
- Loop: `agent.py::run_agent` · tools: `tools.py`
- Tries per scenario: 5, caching off
- Temperature: 0.9
- When: 2026-10-12 01:19

Paste the table below into your README. Fill in the Criterion and
Target columns from `criteria.md`, then mark each try PASS or FAIL
from the output underneath and count them for the Verdict.

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1. matching query completes |  |   |   |   |   |   |  |
| 2. impossible query stops early |  |   |   |   |   |   |  |
| empty wardrobe _(diagnostic — not one of your five)_ |  |   |   |   |   |   |  |
| 3. selected item is the item passed on |  |   |   |   |   |   |  |
| 4. fit card is a postable caption |  |   |   |   |   |   |  |
| 5. matching query finishes under 10s |  |   |   |   |   |   |  |

> The Try and Verdict columns are blank on purpose. Whether a try
> passed depends on the criterion you wrote, so it's yours to decide.
> Count the passes, then read that count against your target: a row
> targeting 4 of 5 with three PASS cells is MISSED (3/5).

---

## What actually happened

Real output, as text. Paste the relevant parts into your README —
the rubric asks for output, not a description of it.

### matching query completes

- Query: `vintage graphic tee under $30`
- Wardrobe: example

**Try 1**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
- search_results: 10

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Y2K Baby Tee — Butterfly Print, Vintage Band Tee — Faded Grey … +7 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 2**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
- search_results: 10

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Y2K Baby Tee — Butterfly Print, Vintage Band Tee — Faded Grey … +7 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 3**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
- search_results: 10

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Y2K Baby Tee — Butterfly Print, Vintage Band Tee — Faded Grey … +7 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 4**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
- search_results: 10

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Y2K Baby Tee — Butterfly Print, Vintage Band Tee — Faded Grey … +7 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 5**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
- search_results: 10

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Y2K Baby Tee — Butterfly Print, Vintage Band Tee — Faded Grey … +7 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

### impossible query stops early

- Query: `designer ballgown size XXS under $5`
- Wardrobe: example

**Try 1**

- stopped early: yes — Nothing matched 'designer ballgown' in size XXS under $5. Try to raise the price limit, drop the size or try a neighbouring one, or use broader words, like 'dress' instead of 'ballgown'.
- selected_item: (none)
- search_results: 0

Trace:

```
[1] parse_query
      in:  designer ballgown size XXS under $5
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: [] (empty)
      →    branch: empty, stopping before suggest_outfit
```

**Try 2**

- stopped early: yes — Nothing matched 'designer ballgown' in size XXS under $5. Try to raise the price limit, drop the size or try a neighbouring one, or use broader words, like 'dress' instead of 'ballgown'.
- selected_item: (none)
- search_results: 0

Trace:

```
[1] parse_query
      in:  designer ballgown size XXS under $5
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: [] (empty)
      →    branch: empty, stopping before suggest_outfit
```

**Try 3**

- stopped early: yes — Nothing matched 'designer ballgown' in size XXS under $5. Try to raise the price limit, drop the size or try a neighbouring one, or use broader words, like 'dress' instead of 'ballgown'.
- selected_item: (none)
- search_results: 0

Trace:

```
[1] parse_query
      in:  designer ballgown size XXS under $5
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: [] (empty)
      →    branch: empty, stopping before suggest_outfit
```

**Try 4**

- stopped early: yes — Nothing matched 'designer ballgown' in size XXS under $5. Try to raise the price limit, drop the size or try a neighbouring one, or use broader words, like 'dress' instead of 'ballgown'.
- selected_item: (none)
- search_results: 0

Trace:

```
[1] parse_query
      in:  designer ballgown size XXS under $5
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: [] (empty)
      →    branch: empty, stopping before suggest_outfit
```

**Try 5**

- stopped early: yes — Nothing matched 'designer ballgown' in size XXS under $5. Try to raise the price limit, drop the size or try a neighbouring one, or use broader words, like 'dress' instead of 'ballgown'.
- selected_item: (none)
- search_results: 0

Trace:

```
[1] parse_query
      in:  designer ballgown size XXS under $5
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: [] (empty)
      →    branch: empty, stopping before suggest_outfit
```

### empty wardrobe

- Query: `denim jacket under $50`
- Wardrobe: empty

**Try 1**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, 90s Track Jacket — Navy/White Stripe, High-Waisted Denim Shorts — Cutoff … +4 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 2**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, 90s Track Jacket — Navy/White Stripe, High-Waisted Denim Shorts — Cutoff … +4 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 3**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, 90s Track Jacket — Navy/White Stripe, High-Waisted Denim Shorts — Cutoff … +4 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 4**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, 90s Track Jacket — Navy/White Stripe, High-Waisted Denim Shorts — Cutoff … +4 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 5**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, 90s Track Jacket — Navy/White Stripe, High-Waisted Denim Shorts — Cutoff … +4 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

### selected item is the item passed on

- Query: `90s track jacket in size M`
- Wardrobe: example

**Try 1**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: 90s Track Jacket — Navy/White Stripe ($45.0, poshmark)
- search_results: 5

Trace:

```
[1] parse_query
      in:  90s track jacket in size M
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 5 items: 90s Track Jacket — Navy/White Stripe, 90s Leather Bomber — Black, 90s Silk Slip Dress — Floral, Midi Length … +2 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 2**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: 90s Track Jacket — Navy/White Stripe ($45.0, poshmark)
- search_results: 5

Trace:

```
[1] parse_query
      in:  90s track jacket in size M
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 5 items: 90s Track Jacket — Navy/White Stripe, 90s Leather Bomber — Black, 90s Silk Slip Dress — Floral, Midi Length … +2 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 3**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: 90s Track Jacket — Navy/White Stripe ($45.0, poshmark)
- search_results: 5

Trace:

```
[1] parse_query
      in:  90s track jacket in size M
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 5 items: 90s Track Jacket — Navy/White Stripe, 90s Leather Bomber — Black, 90s Silk Slip Dress — Floral, Midi Length … +2 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 4**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: 90s Track Jacket — Navy/White Stripe ($45.0, poshmark)
- search_results: 5

Trace:

```
[1] parse_query
      in:  90s track jacket in size M
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 5 items: 90s Track Jacket — Navy/White Stripe, 90s Leather Bomber — Black, 90s Silk Slip Dress — Floral, Midi Length … +2 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 5**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: 90s Track Jacket — Navy/White Stripe ($45.0, poshmark)
- search_results: 5

Trace:

```
[1] parse_query
      in:  90s track jacket in size M
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 5 items: 90s Track Jacket — Navy/White Stripe, 90s Leather Bomber — Black, 90s Silk Slip Dress — Floral, Midi Length … +2 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

### fit card is a postable caption

- Query: `vintage graphic tee under $30`
- Wardrobe: example

**Try 1**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
- search_results: 10

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Y2K Baby Tee — Butterfly Print, Vintage Band Tee — Faded Grey … +7 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 2**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
- search_results: 10

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Y2K Baby Tee — Butterfly Print, Vintage Band Tee — Faded Grey … +7 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 3**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
- search_results: 10

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Y2K Baby Tee — Butterfly Print, Vintage Band Tee — Faded Grey … +7 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 4**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
- search_results: 10

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Y2K Baby Tee — Butterfly Print, Vintage Band Tee — Faded Grey … +7 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 5**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
- search_results: 10

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Y2K Baby Tee — Butterfly Print, Vintage Band Tee — Faded Grey … +7 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

### matching query finishes under 10s

- Query: `denim jacket under $50`
- Wardrobe: example

**Try 1**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, 90s Track Jacket — Navy/White Stripe, High-Waisted Denim Shorts — Cutoff … +4 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 2**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, 90s Track Jacket — Navy/White Stripe, High-Waisted Denim Shorts — Cutoff … +4 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 3**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, 90s Track Jacket — Navy/White Stripe, High-Waisted Denim Shorts — Cutoff … +4 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 4**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, 90s Track Jacket — Navy/White Stripe, High-Waisted Denim Shorts — Cutoff … +4 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```

**Try 5**

- stopped early: yes — The model couldn't be reached, so FitFindr stopped before finishing. Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s is too short. Minimum allowed deadline is 10s.', 'status': 'INVALID_ARGUMENT'}} Fix that and ask again.
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
[2] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, 90s Track Jacket — Navy/White Stripe, High-Waisted Denim Shorts — Cutoff … +4 more
      →    branch: results found, selecting the first
[3] model unavailable
      out: Couldn't reach the model: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Manually set deadline 7s i…
      →    stopping
```
