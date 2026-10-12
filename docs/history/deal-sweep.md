# Deal Sweep — Online Listing Arbitrage

*Started September 21, 2026*

## What this is

Claude sweeps the selling platforms for listings where the seller has under-described or under-priced an item, identifies what it actually is (brand, maker, model, line) from the title, description, and photos, checks sold comps, and reports only the ones that clear the bar.

## The bar (Dylan's thresholds)

An item is a hit only if **both** are true:

1. **Resale value ≥ $50** (realistic sale price, condition-adjusted, from sold comps).
2. **Spread ≥ $25**, meaning expected net proceeds minus the all-in buy cost.
   - All-in buy cost = asking price + shipping to 76078/Keller (for shipped items) + tax where applicable.
   - Net proceeds = sale price − platform fees − outbound shipping − supplies.

The project's max-bid rules in `pricing-and-decision-rules.md` still apply on top of this. A hit can clear the $50/$25 bar and still come with a lower recommended offer.

## Pickup vs. shipped

- **Local pickup:** North Fort Worth area only (Keller, Watauga, Haltom City, NRH, Saginaw, Haslet, Roanoke, Colleyville, Southlake, Lake Worth, and Fort Worth proper). Anything farther gets flagged with the distance.
- **Shipped:** anywhere, with the shipping cost counted in the buy price.

## Platforms and how access works

| Platform | Access | Notes |
|---|---|---|
| eBay | Chrome (Browser 1), logged in | Bulk-fetching triggers a CAPTCHA. Keep it to about one search every few seconds. Sold comps come from `LH_Sold=1&LH_Complete=1`. |
| Facebook Marketplace | Chrome, logged in | Use `facebook.com/marketplace/fortworth/search/?query=...&exact=false`. Past the first ~50 results, the results fill with furniture-store spam. |
| Craigslist | Chrome | Fort Worth subarea: `craigslist.org/search/subarea/ftw?cat=sss&query=...&sort=date`. Best local yield in the pilot. |
| OfferUp | Chrome | Works logged out, defaults to Fort Worth. |
| Mercari | Chrome | Works. Search results render under `[data-testid=ItemContainer]`. |

## Sweep procedure

1. Pull newest listings for the standing-search terms (see `standing-searches.md`) on each platform.
2. Screen by title for anything identifiable, under-described, or priced like the seller didn't research it.
3. Look at the photos for the shortlist: marks, labels, hardware, construction.
4. Pull sold comps (eBay sold for shippables; local asking prices as a secondary signal for furniture).
5. Apply the $50 / $25 bar, then the max-bid rules.
6. Report only hits and near-misses worth watching. Everything evaluated gets a one-line verdict.

---

## Pilot sweep — Sept 21, 2026

Roughly 1,800 eBay, 720 Craigslist, and 340 Marketplace listings screened, plus access tests on OfferUp and Mercari.

### Hits

**Thomasville Chippendale block-front lowboy / vanity: Craigslist, Colleyville, $100 OBO.**
The "Thomasville" stamp is visible inside a drawer. It has the carved shell, cabriole legs, and brass bat-wing pulls, and measures 34×18×32 in. The seller listed it as just "vintage wooden dresser." Local Thomasville case pieces ask $300–$1,800, and one eBay sold comp for a Thomasville Queen Anne cherry lowboy went for $450 (Aug 2026). Realistic local sale: $275–$350. Net at $275 is about $175 profit. Confidence is MEDIUM because the comps are mostly asking prices. **Offer $70, walk at $100.**
https://www.craigslist.org/view/d/colleyville-thomasville-vintage-wooden/96jsjSnuAXkTDDkJTseExE

**Cerwin-Vega VS-120 floor speakers (pair): Craigslist, Fort Worth, $140 OBO.**
The seller says they work, but the woofer foam surrounds are deteriorating, and they say "need gone ASAP." Local asking prices for the same model are $275 (Springtown, reduced from $350) and $450 (FW). The parts market is strong: on eBay, a pair of VS-120 woofers sold for $300, midranges for $65–$80 each, and crossovers for $38–$75 each. Realistic local sale as a pair: about $225–$275. The rule max bid is about $56–$90. **Offer $90. Pass above $110.**
https://www.craigslist.org/view/d/fort-worth-cerwin-vega-vs-vintage/1r8VExdtLkXTFNz5yFEU1j

### Time-sensitive freebie

**Vintage walnut kneehole desk: Facebook, Keller, FREE, at the curb.**
It's at the corner of Wall Price Keller Rd and W Conchos Circle ([zip]), and trash pickup is Monday, Sept 21. The top is painted or damaged, so it needs refinishing, which is outside the charter. It could still sell as-is as a "project desk" for $50–$80 locally. Grab it only if you're passing by.

### Checked and passed

| Item | Where | Ask (landed) | Why pass |
|---|---|---|---|
| "Levi's Big E Type 3" trucker jacket | eBay | $37.52 | Photos show a small-e red tab and an orange paper patch, so it's a 1970s–80s 70506, not Big E. Resale is about $50–$75, spread about $12. The seller mislabeled it. |
| Dorothy Thorpe silver-band highballs (6) | eBay | $65.70 | Sold comps for sets of 6–8 are $30–$75. No spread. |
| Dansk staved teak bowl 10" | eBay | $69.95 | 10-inch comps are $59–$116. Net after fees and shipping is about even. |
| Stanley thermos pair | FB, Haltom City | $25 | Common 1-quart model at $15–$45 each. Spread under $25. |
| Solid teak 3-pc bedroom set | CL, Fort Worth | $275 | Contemporary import teak (ring pulls), not Danish MCM. No brand, so LOW confidence. Watch only. |
| Industrial drafting stool | CL, Fort Worth | $10 | Needs reupholstery (outside the charter). |
| "Old Americana" chest | CL, N. Beach & Tarrant Pkwy | $40 | 1980s pine veneer, no maker. |

### Lessons from the pilot

- **Craigslist beat eBay** for real spreads. eBay sellers are mostly resellers who already researched their items. Craigslist and Marketplace sellers are households.
- **Seller-doesn't-know phrases on eBay return mostly junk** under $30. Misspelling searches mostly return correctly spelled listings because eBay autocorrects them.
- **Comps corrected the gut calls every time.** Dorothy Thorpe, Dansk, and the Levi's all looked like wins by title and were not.

---

## Sweep 2 — Sept 21, 2026 (photo-ID method)

**Method that worked best:** pull large batches of by-owner listings with generic titles (Craigslist Fort Worth + Mid-Cities by category with `purveyor=owner`, and Facebook generic searches like "vintage chair", "bar cart", "fiberglass chair"). Lay out the first photos as contact sheets (60 per screen) and flag anything recognizable. Open only the flagged listings, then price them from eBay sold comps plus current DFW asking prices.

**Volume:** ~1,800 Craigslist listings and ~640 Marketplace listings screened. Results are in `Refurbish-Deal-Sheet-2026-09-21.xlsx` (10 items at $100+ projected profit, $2,260 combined at the recommended offers).

**Photo-ID hits (seller didn't name what it is):** Thomasville block-front lowboy, faux-bamboo brass bar cart, Chinese Chippendale bamboo chair, MCM hutch, rope-edge Eames shell.
**Brand named but badly underpriced:** GF Davis Allen desk ($75), Steelcase tanker ($55), Sherrill wingbacks ($40 each), Henredon octagonal table, Cerwin-Vega VS-120.

**Platform notes:**
- A new Facebook account returns only ~15 results per search, and results after the first ~50 are furniture-store spam. Many narrow searches work better than a few broad ones.
- Craigslist OR searches need quoted phrases: `%22card catalog%22|%22flat file%22`.
- Craigslist nearby results can pull in Austin/Houston listings, so filter by location.
- eBay: pace sold-comp lookups a few seconds apart, or its human check comes back.

**Categories that produced:** MCM/Regency furniture, office/industrial steel (tanker, GF), designer chairs (Eames, Cesca, Sherrill), faux-bamboo and brass.
**Categories that didn't:** thermoses, barware, small glass, and eBay "seller-doesn't-know" phrases.

## Sweep 3 — Sept 21, 2026 (car-fit / shippable, $150+ spread, one $500+)
Constraint: no truck. Items must ship (cost included) or fit in a car around North Fort Worth.
Result: 7 items with a $150+ spread at the resale midpoint, not the 10 Dylan asked for. Only one reaches $500, and only at the top of its sold range (Arturia MatrixBrute, $900 in Dallas; eBay sold $1,095–1,473). Deliverable: Refurbish-Car-Fit-Deals-2026-09-21.xlsx (Deals + Leads & passes).
Deals: MatrixBrute ($900 Dallas), Alpha Juno-2 ($400 Richardson resale shop, 30% off offered), Eames yellow side chair ($75 Plano), Eames rope-edge armshell ($100 Coppell), Nikonos V + 35mm ($80, QT on Basswood Blvd 76131), bamboo chair + table (sweep 1 carry-over), antique camera lot with Minox B ($150 FW).
Best open lead: Denton 7-camera lot (1431299715712814). FB related searches suggest a Pentax 645N; the seller prices on request.
Lessons:
- DFW Marketplace is efficient for named music gear, reel-to-reels, Aerons, Festool, Leica and watch lots. Spreads come from generic titles and lots, not from brand-name searches.
- Juno-106s listed at ~$1,000 usually need voice chips (a repair, so out of scope).
- FB related-search chips on a listing page leak model names that aren't in the title (for example 'pentax 645n'). Use them for photo-ID.
- Craigslist blocked the session after heavy fetches. Keep CL fetches sparse and spaced out.
- New harvester: GRAB snippet in sessionStorage. Navigate to the search URL, then run eval(GRAB)('label'). It scrolls 4x and collects about 15–25 items per query (new-account cap).
