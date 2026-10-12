# Pricing and Decision Rules

Everything in this document exists to answer one question at the moment it
matters: **what is the most I can pay for this and still make it worth doing?**

---

## 1. Platform fees

Fees verified September 2026. **Re-verify quarterly** — platforms change these
without much notice and a stale fee table quietly destroys margin. Log
verification dates in `fees.csv`.

| Platform | Seller fee | Fixed | Notes |
|---|---|---|---|
| **eBay** | ~13.6% standard (varies by category) | $0.30 if order ≤$10, $0.40 if >$10 | Fee is charged on item + shipping + handling + tax, not just item price. 250 free listings/month, then $0.35 each. Confirm the category rate — some differ materially. |
| **Mercari** | 10% flat | none | Payment processing folded into the 10%. No listing fee. |
| **Poshmark** | $2.95 flat under $15; **20%** at $15+ | none | Simple but expensive. The 20% is the highest of any channel here. |
| **Facebook Marketplace** | 10% on shipped orders; **0% on local pickup** | none | Local pickup is free. This is the single most important fee fact in the table. |
| **Etsy** | 6.5% transaction + 3% + $0.25 payment processing | $0.20/listing | Offsite Ads add 12–15% when they trigger; newer sellers can opt out. |
| **Depop** | Verify before first use | — | Fee structure has changed repeatedly; don't assume. |

### The routing consequence

**Furniture sells locally on Facebook.** Zero fees, zero shipping, zero damage
risk. A $400 dresser sold locally nets $400; the same dresser on eBay nets maybe
$345 before you've even solved the problem of shipping a dresser. Furniture goes
local unless there's a compelling reason otherwise.

**Small, light, brand-driven items go to eBay.** The fee is high but the buyer
pool is the only one that searches by model number, and model number is where our
margin lives.

**Clothing** splits: eBay when the brand is the story and the buyer will search
for it; Poshmark and Depop when the look is the story. Watch the Poshmark 20%.

**Collectibles and electronics: eBay,** essentially always.

---

## 2. Comp methodology

Comps are the input to everything downstream, so the discipline here is
non-negotiable.

**Rules:**

1. **Sold prices only.** Asking prices are what sellers wish; sold prices are what buyers did. Use `LH_Sold=1&LH_Complete=1`.
2. **Last 90 days.** Older comps get a haircut or get dropped. Markets move.
3. **Minimum three comps** for a "confirmed" valuation. One comp is an anecdote.
4. **Median, not mean.** One collector overpaying once shouldn't set our expectation.
5. **Drop the top and bottom 10%** when you have enough comps to do so.
6. **Match condition honestly.** A comp for a mint example is not a comp for yours.
7. **Check what the comp included.** A sold "lot of 6" is not a comp for your single piece.

**Record every comp you pull** in `comps.csv` with the date. Comps decay, and a
dated record lets us see how fast a given category is moving.

---

## 3. Condition grading

One consistent scale, applied to the comp median.

| Grade | Definition | Multiplier |
|---|---|---|
| **A — Mint** | Unused, tags attached, or indistinguishable from new | 1.00× |
| **B — Excellent** | Cleans up to near-new. No visible flaws at photo distance | 0.85× |
| **C — Good** | Honest wear, photographs fine, nothing structurally wrong | 0.65× |
| **D — Fair** | Flaws that will show in photos and must be disclosed | 0.40× |
| **F — Damaged** | Chips, holes, cracks, non-working | **Out of scope.** Don't buy it. |

Grade **before** buying, and grade pessimistically. The most common failure mode
in this business is grading an item B in the store and discovering it's a C under
good light at home.

---

## 4. Net proceeds

What actually lands in the account:

```
Net proceeds = (Expected sale price × (1 − fee rate))
             − fixed fees
             − shipping cost (if we pay it)
             − supplies (cleaning, packing materials, hardware)
```

Expected sale price = **comp median × condition multiplier.**

Everyone who loses money at this loses it by skipping the second and third lines.
Shipping a 40-pound item eats $40 of a $90 sale.

---

## 5. The max bid rule

Max bid is a **percentage of net proceeds, scaled by how confident we are in the
identification.** Confidence is the thing being priced — this is an information
business, so uncertainty about the information is the central risk.

| Confidence | Definition | Max bid |
|---|---|---|
| **HIGH** | Mark read clearly and unambiguously. 3+ sold comps within 90 days. | **40% of net proceeds** |
| **MEDIUM** | Strong indicators but no confirmed mark, *or* only 1–2 comps, *or* comps older than 90 days. | **25% of net proceeds** |
| **LOW** | Attractive and plausible but unverified. A bet. | **15% of net proceeds**, and never more than $40 absolute. |

### The three hard floors

A bid must clear the percentage rule **and all three of these**:

1. **Profit floor.** Projected net profit below **$25** is a pass, regardless of percentage. Small wins don't pay for the handling.
2. **Time floor.** Projected profit below **$40 per combined hands-on hour** (Dylan's + the partner's, sourcing through shipping) is a pass. the partner's time is the scarce input; price it.
3. **Space.** If the garage corner is full, the answer is no. A full corner means sell something, not buy something.

### Worked example

A dresser at an estate sale. Label inside the drawer reads Broyhill Brasilia.

```
Comp median (sold, last 90 days, 4 comps)     $720
Condition: B — Excellent                     × 0.85
Expected sale price                           $612

Sell local on Facebook Marketplace, 0% fee      −$0
Shipping: local pickup                          −$0
Supplies: cleaner, wax, new drawer pulls       −$25
Net proceeds                                   $587

Confidence: HIGH (mark read, 4 comps)
Max bid = 40% × $587 =                         $235

Profit at max bid:      $587 − $235 = $352     ✓ clears $25 floor
Hands-on time estimate: 3.5 hrs → $100/hr      ✓ clears $40/hr floor
Space:                  corner has room        ✓
```

**Verdict: GRAB, up to $235.**

Now the same dresser with no label found, identified only by the drawer-front
pattern:

```
Confidence: MEDIUM
Max bid = 25% × $587 = $147
```

Same object. The $88 difference is the price of not having read the mark — which
is exactly why the CHECK verdict and the thirty-second walk to flip something over
is the highest-return action in the whole pipeline.

---

## 6. Selling discipline

**Listing price:** start at the comp median for your condition grade, not above.
Overpricing costs holding time, and holding time is the hidden expense.

**Markdown schedule:**

| Day | Action |
|---|---|
| 0 | List at comp median × condition multiplier |
| 30 | Reprice −15%. Re-shoot if the photos are the problem. |
| 60 | Reprice −25% from original. Consider a different platform. |
| 90 | **Liquidate.** Local, bundled, donated — gone. |

The 90-day rule is not a suggestion. Dead inventory ties up cash and, worse, ties
up the corner of the garage that the next good buy needs. Take the loss, record
it in the item log, and learn from it.

**Walk-away floor:** set it when you list, write it down, and honor it. It's
cost + fees + $10. Below that you're working for free.

---

## 7. The listing itself — where presentation earns its share

The spread isn't captured until the listing makes the claim credible.

**Title formula** — front-load what people search:

```
Brand + Line/Pattern + Item + Era/Style + Material + Size + Condition
```

> *Broyhill Brasilia Mid Century Modern Walnut 9-Drawer Dresser 1960s Excellent*

Not: *Nice wood dresser*.

**Photos:**

1. Hero shot, staged, clean background, good natural light
2. **The mark itself, in focus, filling the frame** — this is the proof, and it converts skeptics
3. Full front, sides, back
4. Detail shots: hardware, joinery, any distinctive feature
5. **Every flaw, honestly.** Disclosed flaws build trust; discovered flaws cause returns.

**Description:** name the maker, the line, the years produced, the designer if
known, the materials, exact measurements, and the condition in plain terms. The
research we did *is* the product — put it in the listing.

the partner's staging is doing real economic work here, not decoration. The same item,
shot on a clean styled surface with good light versus on a garage floor, is
routinely a 30–50% price difference. Stage the background once and reuse it.
