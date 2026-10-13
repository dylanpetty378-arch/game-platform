# Research brief — resale encyclopedia entries

You are writing entries for a resale encyclopedia. It is used by a reseller (Dylan) who buys under-priced items from
private sellers (Craigslist, ≤ $200, nationwide, shipped) and resells them, mostly on eBay. The encyclopedia is
permanent, reusable knowledge. He will also quote it to his own buyers, so it must be accurate, specific and complete.
Take the time to do it properly: depth beats speed.

## Your input
A batch file listing ~8 item types (`## <slug>`). Each type has real listings we scanned: price, title, photo URL,
Google Lens best match, Lens AI text, and our verdict.

## For EACH type in your batch
1. **Look at the photos** of the example listings. Download each with
   `curl -s -o /tmp/res/img/<pid>.jpg <photo url>` (mkdir -p first) and view them with the Read tool. Identify exactly
   what each one is: maker, model, period, material, and any marks visible.
2. **Research the type** from your own knowledge (THIS RUN HAS NO WEB SEARCH BUDGET — do not call WebSearch; WebFetch only on URLs you already know are relevant, e.g. maker history pages). Mark knowledge-based numbers "(general knowledge, verify)" and set rubric "confidence": "low" unless the batch file or /home/claude/game-platform/db/comps.jsonl (grep it for your type: Terapeak sold data) gives real sold data.
   completed listings as they appear in search results, WorthPoint, LiveAuctioneers, Invaluable or auction-house
   results, Replacements.com, collector clubs and price guides. Also use maker histories, mark guides and collector
   sites for identification. Note the URL of every source you rely on. If you can't find sold data, say so and label
   numbers as estimates.
3. **Write the entry** to `/tmp/res/enc/<slug>.md` in EXACTLY the template below. Every section is required; write
   "unknown" rather than leaving one out. Cover:
   - every important maker, brand or line, with marks and dates
   - finishes and materials, and how to tell quality from cheap production and old from new
   - common damage and repairs
   - fakes and reproductions
   - a value ladder of sold prices by tier
   - at least 3 dated comps with sources where they can be found
   - market speed
   - what sellers miss
   - shipping
   - what to tell buyers
   - a buy rule under Dylan's profit rule
   - the full rubric JSON
4. **Judge each example listing** against what you learned. At the end of the entry's "Seen in sweeps", add one line per
   example: `- 2026-10-13 – craigslist – "<title>" – $<price> – <verdict: pass / possible buy / ask seller> – <why, with the
   identification and estimated resale>`.
   **If any example is a real possible buy** (estimated resale × 0.87 − ~$15–25 shipping each way − price ≥ max($50,
   price), and it fits a car's passenger seat), say so prominently in your final report, with pid, identification,
   evidence and confidence. Those are what we're hunting.

## Dylan's rules (use them in the buy rule)
- Price ≤ $200. Profit = sold median × 0.87 − shipping to buyer − shipping to Dylan − price. Pass unless profit ≥ max($50,
  price). Tier A: profit ≥ 2× price.
- Size: the item must fit in a car's passenger seat. Anything bigger is not worth his time.
- No repairs, no untested electronics, no items that need professional authentication (designer bags, high-end
  watches, etc. — say so in the buy rule).
- Never shop by brand name. The edge is owners who don't know what they have, so explain the visual tells that identify
  the valuable versions from photos.

## Template (copy exactly; replace the <…> parts)
````
# <Type name> (<main makers/brands>)
Updated: 2026-10-13 · Sources: <list every source with URL>
Slug: <slug> · Aliases: <other names sellers use in titles>
Summary: <one line: tiers with $ ranges>
Buy rule (short): <one line>

## What it is / how to recognise it in a photo
## Makers, brands and variants
## Materials, finishes and quality tells
## Condition, damage and repairs
## Fakes, reproductions and reissues
## Value ladder (sold prices, not asking)
| Tier | Examples | Typical sold price | Notes |
|---|---|---|---|
## Comps (sold, dated)
## Market
## What sellers usually miss
## Shipping / handling
## Selling it (for the buyer-facing listing)
## Buy rule
## Rubric
```json
{"size_class": "pocket|shoebox|carry-on|passenger-seat|bigger", "weight_lb": 0, "shape": "flat|round|tall|irregular|set-of-many",
 "fragility": 1, "transit_damage_risk": 1, "hidden_defect_risk": 1, "testability": 1, "repro_risk": 1, "id_difficulty": 1,
 "rarity": 1, "sold_per_month": 0, "sell_through": "0%", "days_to_sell": 0, "price_p25_p50_p75": [0, 0, 0], "price_spread": 0,
 "condition_sensitivity": 1, "seasonality": "", "best_platform": "", "fees_pct": 13, "ship_cost_to_buyer": 0,
 "undervalue_frequency": 1, "bust_probability": "0%", "expected_profit_typical": 0, "confidence": "high|medium|low"}
```
(1–5 scales: 1 = low/good for us … 5 = high/bad for us; undervalue_frequency: 5 = owners often under-price it.
sold_per_month = eBay US sold listings per month, order of magnitude. price_spread = p75 ÷ p25. bust_probability = chance a
typical purchase ends up a loss or not worth the time.)
## Seen in sweeps
````

## Final report (your last message)
Keep it short:
- the slugs written
- **POSSIBLE BUYS** (pid, what it is, est. resale, est. profit, confidence, evidence), or "none"
- anything surprising worth adding to our process

Do not contact anyone and do not buy anything. Write only to /tmp/res/enc/ and /tmp/res/img/.
