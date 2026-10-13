# Redo brief: listings killed without a real identification (Dylan, Oct 13: "redo the ones that were left out")

These Lens-read listings were killed earlier with either (a) a maker/model named by Lens that the seller's title does
NOT mention (`mismatch` column — the arbitrage signal), or (b) a kill note with no specific reason (`why` = weak).
Columns: pid, price, area, title, best (Lens best match), med (Lens asking-price median), ai (Lens identification),
url, img (main photo id), mismatch, old_kill (the earlier note), why.

For EVERY row — no exceptions, no title-only kills:
1. Fetch the listing body: `cd /home/claude/game-platform && python3 scripts/review_helpers.py --body <url>`. If the
   listing is gone (`live: false`), verdict `kill` with note "expired".
2. Download the main photo (`https://images.craigslist.org/<img>_600x450.jpg`) and look at it. For anything with a
   maker/model/mark question, pull the listing page HTML and fetch ALL its photos (grep images.craigslist.org ids).
3. **Identify it specifically** — maker, model/pattern/variant, material, period — from the photos, the body and the
   Lens text. Use `python3 scripts/enc.py find <words>` and `enc.py show <slug>` (read the Golden-egg tells and the
   value ladder). Use `grep -i '<words>' db/comps.jsonl` for sold data. No WebSearch.
4. Verdict:
   - `buy` only with a sold comp (comps.jsonl or the entry's dated comps) showing profit = median×0.87 − 2×ship − price
     ≥ max($50, price). Tier A if ≥ 2×price.
   - `ask` when the item is plausibly the valuable variant and ONE photo/question would settle it (mark, stamp, case
     back, label, signature) — say exactly what to ask. Also `ask` when you cannot identify it and it is ≤ $40.
   - `bundle` when profit is $30–50 and the type is one Dylan could buy several of (see BUNDLE lane below).
   - `kill` ONLY with a specific reason: the common-variant tell you saw, a sold comp with no margin, or size /
     untested electronics / dealer / per-item pricing / repro. Write the identification anyway.
5. Write `/tmp/res/redo/out_<part>.jsonl`, one object per row:
   `{"pid","verdict","type","note","est_resale","tier","identified": "<maker/model/variant or 'unidentified: needs <x>'>"}`
   and `/tmp/res/redo/knowledge_<part>.md` with `slug: fact` lines for every tell learned.

BUNDLE lane (Dylan, Oct 13): small certain profits ($30–50) are worth it only in bundles of the same category, so
listing, photographing and shipping are shared. Mark such items `bundle` with the type slug; the system groups them.

Final report (under 250 words): counts; every buy/ask/bundle with pid, identification, evidence, confidence; and
what the earlier kills got wrong most often.
