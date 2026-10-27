# Photo in → answer out (Oct 27 2026)

Dylan sends pictures: things he sees in a store, a Facebook post, an estate-sale photo, something in the garage. Any
chat follows this so his own photos get the same treatment as the sweeps, and the work lands in the database.

## Procedure (per item, in this order — stop the moment it fails)
1. **Look before you read.** Zoom on every photo for marks (base, back, clasp, inside a lid, labels, edition fractions,
   hallmarks, model plates), construction (hand vs mould, solid vs plated wear-through), material (weight cues, grain,
   patina), and size cues (a hand, a coin, floor tiles). Write down what is *seen*, not what the title/Dylan called it.
2. **Name the specific thing.** Maker · model/pattern · material · period · variant. Use the encyclopedia first:
   `python3 scripts/enc.py find <words>` then `enc.py show <slug>` — read its **Golden-egg tells** and **real vs copy**
   lines. The CLIP type match is a hint; the eye on the object wins. If no entry fits, say so (and it becomes a
   new-type candidate in research/new-type-candidates.md).
3. **Metal first.** If the photo or seller gives a weight and a purity: `python3 -c "import sys;sys.path.insert(0,
   'scripts');import melt;print(melt.floor('<title + description + marks>', <price>))"` — the floor at refiner payout
   and the max bid. Count only the metal (stones, pearls, beads, cord and clasps come out of the weight).
4. **Value from SOLD comps, never asking.** eBay sold (Terapeak in db/comps.jsonl where we have it), LiveAuctioneers,
   Heritage, WorthPoint summaries. Match the **condition band** and the **exact variant**. Agent guesses run 2–3× above
   eBay sold medians: `value_low` is the conservative sold figure for this condition, with a URL.
5. **Money rule.** max bid = min(value_low − 50, value_low / 2) after ~13% fees and shipping both ways; profit ≥ $50
   under $50, ≥ the price above. $200–500 only if profit ≥ 10× price. Size: fits a Civic trunk or back seat. No repairs,
   no authentication-dependent items, untested electronics only if profit ≥ 3× price. Never-show: Funko, trading cards,
   furniture/big appliances, instruments/audio.
6. **Real-or-fake check** in one line: the single tell that separates the money version from the copy, and whether the
   photo shows it or Dylan must check it in person (and exactly where to look).
7. **Verdict card** (what Dylan reads on his phone):
   - **What it is** (one line) · **Verdict** egg / lead / pass · **Pay up to $X** · **Sells for $Y–Z** (sold comps, links)
   - **Why it's worth more than it looks** (the tell) · **Check before paying** (one or two things) · **Resale plan**
     (eBay shipped vs FB local, title to use, what to photograph)
8. **Log it.** `python3 scripts/db.py event <pid> rubric --data '{…}'` with the item rubric (docs/rubric.md), or
   `scripts/lowuse.py log` for sweep verdicts; `enc.py seen <slug> "<line>"` for anything the type's entry should learn.
   A bought item starts a dossier (docs/item-dossiers.md).

## What to answer when the photo isn't enough
Say exactly which photo would settle it (the base, the clasp stamp, the back of the frame, the inside of the lid) and
what the two answers would mean in dollars — never "take it to an appraiser".

## Speed
Repeat types are fast: the entry's Golden-egg tells + Quick ID checklist are the whole first pass. New types get the
full research and their entry written (`enc.py add`) so the next one is fast.
