# Triage brief: Lens-scanned but unflagged Craigslist listings (Refurbish)

You review listings that Google Lens ran on but did NOT flag. Most real leads hide here: Lens flags are almost all false, and the leads found so far came from reading the Lens AI identification together with the title and price. Most rows are clear kills from the text alone, so be fast on those and spend your time on the few that could be valuable. Dylan buys under-priced items from private sellers
(≤ $200, shipped nationwide) and resells them on eBay. We are hunting the rare real deal ("gold eggs").

Input: a TSV with columns pid, price, cat, area, title, best, med, ai (the Lens AI identification), url, img.
- `best` is the Google Lens best match.
- `med` is the Lens median of matched listing prices. These are mostly ASKING prices, often for a better or different
  item, so never trust med on its own.

For EACH row:
1. **Triage by title and Lens text.** Kill straight away, without opening photos:
   - anything bigger than a car's passenger seat (furniture, big lamps, large framed art, rugs over about 4×6)
   - modern decor and mass-market items
   - untested electronics
   - things needing authentication (designer bags, luxury watches)
   - dealer or antique-mall stock
   - reproductions
2. **Photo-check the rest.** Download the main photo with
   `curl -s -o /tmp/res/img/<pid>.jpg https://images.craigslist.org/<img>_1200x900.jpg` and view it with Read. Then:
   - Identify the maker, model, period and material.
   - Read any text visible on the item.
   - Fetch the listing body with `python3 /home/claude/game-platform/scripts/review_helpers.py --body <url>`, run from
     /home/claude/game-platform. It often reveals per-item pricing, damage or "dealer". For promising items, fetch the
     other photos from the listing page HTML (grep it for images.craigslist.org ids).
3. **Look up the type** with `cd /home/claude/game-platform && python3 scripts/enc.py find <words>`, and read the entry
   with `enc.py show <slug>`. Use its value ladder, tells and buy rule. For sold data, also check
   `grep -i '<words>' db/comps.jsonl`. Do NOT use WebSearch (no budget this turn) and do NOT use the browser.
4. **Decide.**
   - Profit = resale × 0.87 − ship to buyer − ship to Dylan − price. It must be ≥ max($50, price).
   - Tier A: profit ≥ 2× price. Tier B: passes. Tier C: needs an answer or an offer from the seller.
   - Verdicts:
     - `kill`, with a one-line specific reason
     - `ask`, with what to ask
     - `buy`, with the evidence
5. **Write results** to `/tmp/res/rev/out_<part>.jsonl`, one JSON object per line:
   `{"pid": "...", "verdict": "kill|ask|buy", "type": "<encyclopedia slug>", "note": "<identification + reason>", "est_resale": <number or null>, "tier": "A|B|C|null"}`
6. **Record new knowledge.** If you learn something an entry doesn't say (a tell, a maker, a price point), append it to
   `/tmp/res/rev/knowledge_<part>.md` as `slug: fact`. Don't edit the entries.

Final report: counts of kill, ask and buy; full details of every ask and buy (pid, identification, est. resale, profit,
confidence); and any process lessons.

## Calibration (learned Oct 13)
Resale estimates from general knowledge have run 2–3× above actual eBay sold medians. Lot examples: lead-soldier lots
sell for about $30, a vintage band tee for about $37, an Ideal plastic toy for about $25. So:
- When you have no sold comp, use the LOW end of your range.
- Mark the estimate "no comp".
- Only call it a `buy` when a sold comp in db/comps.jsonl or the entry supports it. Otherwise call it an `ask` or a
  `kill`.
Strip `\r` from every field. The input files may have CRLF line endings.

## No generalization (Dylan, Oct 13)
The money is in specifics: the one maker, mark, model, variant, material or date that makes THIS item worth multiples
of the lookalikes beside it. So:
- An `ask` or `buy` verdict must name the exact thing (maker/model/variant/mark/material/period) and the SPECIFIC tell
  you saw or need to see ("Goebel full-bee TMK-2 stamp, not the later stylized bee"; "21 jewels engraved on the
  movement, Jostens service award — the case may be 14K"; "Ainsworth aluminium body, not the brass Indian replica").
- "Vintage pocket watch, ~$50–150" is not a verdict. If you can't say what separates this one from the common
  version, say what photo or question would settle it and make it an `ask`.
- Kills can be one line, but when a kill is "common version of a type that HAS a valuable version", say which
  valuable version it is NOT (e.g. "Stanley No. 5 type 19, not the pre-1910 type 11 with the low knob").
- Record every such tell you learn in knowledge_<part>.md as `slug: fact`; those lines become encyclopedia field notes.
