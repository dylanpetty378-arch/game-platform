# The rubric — key facts tracked for every item type and every item

Dylan (Oct 12 2026): "have a rubric of key information tracked for each thing … shape of item, how often they're sold,
how quickly they're sold, how much the price can vary, the seller's reliability, the item's rarity, the item's fragility,
the possibility of it being broken, the chances that the item will be a waste of money … all things like that."

There are two levels. Everything is stored in the database, so it can be queried and averaged:
- **Type rubric**: one per encyclopedia entry. It covers what is true of the type in general: market, physical traits,
  and risks. It lives in the entry's `## Rubric` section AND in `db/item_types.jsonl` (`rubric` field), written with
  `scripts/enc.py`.
- **Item rubric**: one per listing that reaches photo review or later. It covers what is true of this specific listing:
  the seller, condition, completeness and price. It is stored as an event with `stage=rubric` and the fields in `data`,
  written with `db.py event … --data`.

Scales: 1 = low/good-for-us … 5 = high/bad-for-us unless stated. `?` = unknown (say so; never guess silently).

## Type rubric fields

| Field | Meaning / how to measure | Scale or unit |
|---|---|---|
| `size_class` | pocket · shoebox · carry-on · passenger-seat · bigger (bigger = excluded by the size rule) | enum |
| `weight_lb` | typical shipped weight incl. packing | lb |
| `shape` | flat / round / tall / irregular / set-of-many — drives packing and box cost | enum |
| `fragility` | 1 metal/textile … 5 thin porcelain, glass, lamp shades | 1–5 |
| `transit_damage_risk` | chance it arrives damaged even if packed well | 1–5 |
| `hidden_defect_risk` | cracks, repairs, hairlines, not working, missing parts that photos don't show | 1–5 |
| `testability` | can a non-expert verify it works/is right before paying? 1 = obvious from photos, 5 = needs a specialist | 1–5 |
| `repro_risk` | reproductions, fakes, later re-issues, married parts | 1–5 |
| `id_difficulty` | how much expertise it takes to tell the valuable version from the common one | 1–5 |
| `rarity` | 1 common everywhere … 5 rarely seen | 1–5 |
| `sold_per_month` | eBay US sold listings per month for the type (Terapeak / sold search), order of magnitude | count |
| `sell_through` | sold ÷ (sold + active) on eBay | % |
| `days_to_sell` | typical days from listing to sale at a fair price | days |
| `price_p25_p50_p75` | sold-price quartiles for the sellable tier | $ |
| `price_spread` | p75 ÷ p25 — how much price varies by condition/variant | ratio |
| `condition_sensitivity` | how fast value falls with wear/damage | 1–5 |
| `seasonality` | peak months, if any | text |
| `best_platform` | where it sells best (eBay, Etsy, Reverb, Chairish, local, auction) | text |
| `fees_pct` | platform fees for that venue | % |
| `ship_cost_to_buyer` | typical outbound shipping | $ |
| `undervalue_frequency` | how often owners list it far under value (our edge) | 1–5 (5 = often) |
| `bust_probability` | chance a typical purchase ends up a loss or not worth the time (unsellable, damaged, fake, slow) | % |
| `expected_profit_typical` | at a typical owner asking price, after fees + shipping both ways | $ |
| `confidence` | how solid the numbers are: high (Terapeak/sold data) · medium (web sold listings) · low (estimates) | enum |

## Item rubric fields (per listing)

| Field | Meaning | Scale |
|---|---|---|
| `seller_reliability` | 1 detailed honest listing, many clear photos, measurements, flaws shown … 5 one blurry photo, vague, evasive, "as is" | 1–5 |
| `seller_type` | owner-estate / owner-casual / picker / dealer-reseller (dealers price at retail — usually pass) | enum |
| `photo_quality` | can marks, condition and size be judged from the photos? | 1–5 (1 = yes) |
| `marks_visible` | maker's mark / signature / hallmark / model plate seen in photos | yes/no/n.a. |
| `condition_seen` | mint / excellent / good / fair / poor / unknown | enum |
| `completeness` | complete / missing parts / unknown | enum |
| `works` | tested working / seller says works / untested / not working / n.a. | enum |
| `provenance` | anything that adds value (estate, original owner, receipts, box, papers) | text |
| `identification` | what exactly it is (maker, model, period, material) | text |
| `id_confidence` | high / medium / low | enum |
| `est_resale` | expected sold price, this condition | $ |
| `est_profit` | Dylan's rule: resale × 0.87 − ship to buyer − ship to Dylan − price | $ |
| `bust_probability` | type bust probability adjusted for this listing | % |
| `size_ok` | fits a passenger seat | yes/no |
| `questions_for_seller` | what to ask before paying | text |
| `verdict` | kill / keep / ask / decided-A/B/C | enum |

## How to use it
- Photo review: score the item rubric for every listing that survives triage; keep only if est_profit passes the rule and
  bust_probability ≤ ~25% (or the upside clearly pays for the risk).
- Encyclopedia research: every new or extended entry fills the type rubric; `scripts/enc.py` syncs it into the database.
- Buying/selling: the item dossier (docs/items/) carries the item rubric plus everything needed to describe the piece to
  a buyer (see docs/item-dossiers.md).
- Learning: as outcomes arrive (sold price, days to sell, damage, returns), update the type rubric — measured numbers
  replace estimates and `confidence` goes up.
