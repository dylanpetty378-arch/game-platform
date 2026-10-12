# Refurbish — Project Charter

*Established September 13, 2026*

## The thesis

We are not in the repair business. We are in the **information arbitrage** business.

The money is made in the gap between what an item sells for when the seller
doesn't know what it is, and what it sells for when the buyer is told exactly
what it is. A dresser listed as "wood dresser $60" and the same dresser listed
as "Lane Acclaim Mid-Century Walnut Dovetail Dresser, 1962" are the same object.
The spread between those two prices, minus cleaning, fees, and time, is the
entire business.

Three things create that spread, in order of how much they're worth:

1. **Identification** — the maker, line, pattern, era, or model the seller never named.
2. **Presentation** — cleaning, staging, photography, and copy that make the claim credible.
3. **Routing** — listing on the platform where that category actually clears at a premium.

We do all three. We do not do repair.

## Scope

**In:** Furniture and wood. Clothing. Toys. Housewares, pottery, glass, and
china. Collectibles. Electronics and audio **that already work**. Anything that
fits in the corner of the garage and needs nothing more than cleaning, polishing,
hardware, and staging.

**Out — hard boundaries, no exceptions without a deliberate decision to change this document:**

- Anything broken. No non-working electronics.
- Small engines, motors, anything mechanical needing service.
- Anything requiring refinishing beyond clean/polish/wax, rewiring, reupholstery, or parts sourcing.
- Anything that does not fit in the designated garage corner.
- Anything where the value depends on authentication we can't perform (high-end handbags, fine art, precious gems, signed sports memorabilia).

The boundary is deliberate. The moment an item needs *work* instead of *cleaning*,
the margin stops being information and starts being labor — and labor is the one
input we have least of.

## Roles

| Who | Owns |
|---|---|
| **Dylan** | Sourcing, in-store scouting, online listing sweeps, acquisition decisions, listing and selling, the numbers. |
| **Claude** | Identification, comp research, valuation, go/no-go math, listing titles and copy, maintaining the data collections. |
| **the partner** | Cleaning, staging, photography. The presentation half of the spread. |

the partner's time is the binding constraint on throughput, not Dylan's and not
Claude's. Every go/no-go decision is priced against it. See
`pricing-and-decision-rules.md`.

## The pipeline

```
SCOUT  →  TRIAGE  →  ACQUIRE  →  CLEAN & STAGE  →  LIST  →  SELL  →  LOG
```

1. **Scout** — Dylan finds candidates: photos in stores, online listing sweeps, pasted Facebook Marketplace posts.
2. **Triage** — Claude IDs what's identifiable, flags what needs a second photo, prices it, returns a verdict per item. Fast and compressed. See `triage-playbooks.md`.
3. **Acquire** — Dylan buys only what clears the max-bid rule. Everything evaluated gets logged, bought or not.
4. **Clean & stage** — the partner. Cleaning only. If it needs more, it was a bad buy; record why.
5. **List** — brand-forward title, the maker's mark as a hero photo, routed to the right platform.
6. **Sell** — price discipline, scheduled markdowns, hard liquidation date.
7. **Log** — actual numbers go into the item log. Non-negotiable; it's what makes the next decision better.

## Decision rules (summary)

Full math in `pricing-and-decision-rules.md`.

- **Never bid above the confidence-tiered max bid.** Confirmed ID buys at 40% of net proceeds, probable at 25%, speculative at 15%.
- **Floor:** projected net profit under $25 is a pass regardless of percentage.
- **Time:** projected profit under $40 per combined hands-on hour is a pass.
- **WIP limit:** the garage corner. When it's full, nothing new comes in until something ships. A full corner is a signal to sell, not to expand.
- **Aging:** reprice at 30 days, reprice again at 60, liquidate at 90. Dead inventory is a cash flow problem, not a patience problem.

## What we measure

The scoreboard, in priority order:

1. **Profit per hands-on hour** — the real constraint.
2. **Go-decision hit rate** — of items bought, what fraction cleared the projected profit.
3. **Median days to sell** — the cash cycle.
4. **Capital turns per quarter** — how hard the same dollar works.
5. **Pass calibration** — of items we declined, how many later sold high. This is the only metric that tells us what we're *missing*, and it's the one most resellers never track.

## What compounds

Five datasets, defined in `data-collections.md`. The brand reference is the moat:
every identification we make once gets written down so it's instant the next
time. After a hundred items, the triage step stops being research and starts
being recall.

## Companion documents

- `identification-routing.md` — looks like X → look it up here. Where the marks hide, by category.
- `triage-playbooks.md` — the three bulk operating modes and their input/output formats.
- `pricing-and-decision-rules.md` — fee tables, comp methodology, condition grading, max-bid math.
- `standing-searches.md` — repeatable hunting queries built on seller-doesn't-know language.
- `data-collections.md` — the six datasets, field-level schemas, review cadence.

**Refurbish Field Kit** — the phone tool for in-store use: max-bid calculator with
the floor checks built in, mark locations by category, and one-tap sold-comp links.
https://claude.ai/code/artifact/4cc646c7-4f98-4b34-a8a9-c97c041bb4bb
