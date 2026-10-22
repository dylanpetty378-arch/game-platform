# Low-usage mode — the default Refurbish loop since Oct 21 2026

Dylan is conserving Claude usage. This loop keeps a real eye on real photos, with the encyclopedia, while moving every
step that doesn't need judgement onto free compute. It replaces review-cycle.md §0b for normal runs; the old loop
(8 Opus agents on 120-cell sheets every 3 h) is kept there for reference only.

## Where the usage went before (Oct 13–16 numbers)
- 8 scheduled Opus sessions a day, each spawning 8–12 Opus eye agents over 40–50 sheets of *everything* (~5,500
  eBay thumbnails per run). Every agent re-carries a full context; every tool call re-sends the conversation.
- Result: ~170,000 photos looked at, 0 shippable confirmed eggs, a handful of leads. Yield per token was the problem,
  not effort.

## The loop now
| Step | Who | Cost |
|---|---|---|
| eBay pool (ending ≤26 h + newly listed ≤26 h, casual sellers, ≤3 bids, ≤$200) | GitHub Actions `eye-shortlist`, 08:47 UTC daily (backup 09:29) | free |
| ShopGoodwill lots ending ≤26 h, egg categories | same workflow | free |
| Text drops: repro/new/cards/ACEO/OOAK/AI art, over money rule, title already names a maker (makers.json) | `scripts/shortlist.py` | free |
| CLIP image score + match against all 663 encyclopedia types, weighted by each type's top-tier value | `scripts/shortlist.py` + `research/enc_digest.json` | free |
| Keep best ~1,000, fetch all photos + description for each | same | free |
| Eye: 48-photo sheets at 220 px, each with notes (price, bids, title, matched types) and those types' money tells | 2–3 **Sonnet** agents | small |
| Deep review of flags: full photo panels + sold-comp web research | the main session (Opus) | the only expensive step, ≤ ~8 items |
| **Outcomes**: every sold ShopGoodwill lot (~5k/day, photo + final price) → db/outcomes/sgw; last shortlist joined to its finals → db/outcomes/shortlist.jsonl | `scripts/outcomes.py` in the same workflow | free |
| **Similar sold**: CLIP look-alikes among sold lots → median/p75 picker price per shortlisted row (store in actions cache) | `scripts/knn.py` | free |
| **Read the marks**: CLIP picks each row's mark/label/signature photos, Tesseract reads them → maker or metal not in the title | `scripts/ocr.py` | free |
| **Melt floor**: weight × purity × spot (research/spot.json) at refiner payout; rows that clear the money rule always go in | `scripts/melt.py` | free |
| **Misses**: SGW lots that sold ≥ $100 with titles that don't say why → research/pools/misses/<date>.md | `outcomes.py misses` | free |

The shortlist already skips anything shown before (research/pools/shown.json, 12 days), so nothing is screened twice.

## Running it ("get going", or the daily scheduled task)
1. `git pull`; `python3 scripts/lock.py take "<chat>" 2` (stop if BUSY); commit + push the lock.
2. `python3 scripts/lowuse.py prep` → prints run name, sheet count and agent batches. If the shortlist is older than
   ~30 h the workflow failed — run anyway and say so.
3. Spawn the eye agents **in one message**, `model: "sonnet"`, one per batch. Prompt each with: read
   research/LOWUSE_EYE_BRIEF.md and /tmp/eye/<run>/top-tells.md; for each sheet N in its batch read
   /tmp/eye/<run>/sheet_NN.md then the image sheet_NN.jpg; write flags to /tmp/eye/<run>/flags_<a>.tsv.
4. `cat /tmp/eye/<run>/flags_*.tsv > /tmp/eye/<run>/flags.tsv && python3 scripts/lowuse.py panels <run> /tmp/eye/<run>/flags.tsv`
5. Deep review in the main session: read flagged.md, view each panel, then sold comps (WebSearch; prefer auction
   archives and sold listings, never asking prices). Kill fast: stop researching an item the moment it fails.
   Rules: research/EBAY_DEEP_BRIEF.md / GOLDEN_DEEP_BRIEF.md (value_low = conservative sold value; max bid leaves
   profit ≥ max($50, price) after 13% fees and shipping).
6. Write verdicts (`sheet\tcell\tegg|lead|kill\tvalue_low\tmax_bid\tnote`) and `python3 scripts/lowuse.py log <run> <tsv>`.
   EGG → scripts/build_report.py PDF and send it to Dylan with max bid, end time, evidence, what to check.
7. Append one short block to docs/improvements.md (counts, flags, verdicts), commit db/ docs/ research/, push,
   `lock.py release`, push. Reply in 3–5 lines.

**Budget:** main session ≈ 20–25 tool calls; no fan-outs beyond the eye agents; no browser; no Opus agents.

## Who this is for (Dylan, Oct 22 2026)
Full-time job, two kids, no warehouse: few items, each worth real money. The money rule stays (profit ≥ $50 under
$50; profit ≥ the price above $50) but it is a floor — surface fewer, stronger leads, never a bulk/volume flow.

## Weekly (Sundays, or when research/pools/misses/REVIEWED is > 7 days old) — learn from the market
1. `python3 scripts/lowuse.py misses 7` → sheets of the week's top misses (sold high, title silent). One Sonnet agent
   (or the main session) answers per cell: what is it, and what in the photo showed it? Write the answers to
   research/pools/misses/review-<date>.md.
2. Repeat answers become encyclopedia tells / new types (research/new-type-candidates.md) — the eye learns what bidders saw.
3. Check the category breakdown (the misses report's lead lines): if $100+ sales concentrate in categories the harvest
   skips, widen `sgw.FIRST` (Oct 22: 66% of $100+ sales were outside it → jewelry by type + instruments added).
4. Update research/spot.json (gold, silver per troy oz; the workflow warns after 10 days).
5. Look at db/outcomes/shortlist.jsonl: did high-score rows sell high? Re-fit the score weights in shortlist.py `main()`
   once a few weeks are in. Touch the date in research/pools/misses/REVIEWED.

## Deep review of the new lead types
- **Melt leads:** weight must be shown on a scale or stated in grams by the seller; the mark must be legible in a photo;
  no plating/filled marks; seller feedback ≥ 20 for gold. Max bid = the MELT line's max bid (already the money rule).
- **Photo-mark leads:** confirm the mark in the full-size photo before any comp research; then comps for that maker.

## Tuning knobs
- `shortlist.py --n` (photos per day, default 1,000). More photos = more eye cost, linearly.
- Score weights in shortlist.py `main()` (egg, type value, title vagueness). Re-fit once verdicts accumulate in
  research/pools/lowuse-log.jsonl: compare flagged/lead rows' `score` components against the rest.
- Facebook Marketplace has no API; Dylan pastes links or screenshots into a chat and the same deep review applies.
