# Golden-egg deep review — ShopGoodwill flags

A picker flagged these auctions from thumbnails as possible **golden eggs**: worth $1,000+ resale (or ≥10× the
realistic hammer price) without the listing recognising it. Dylan: "$100 profit isn't a golden egg." Be ruthless —
most flags will be decor, reproductions or prints. But a real one is the whole point, so look properly.

For each row:
1. `cd /home/claude/game-platform && python3 scripts/sgw.py detail <itemId>` — description, bids, weight, photo URLs.
2. Download EVERY photo (`curl -s -o /tmp/res/gold/img/<id>_<n>.jpg <url>`) and view each with Read. Look for:
   signatures, foundry marks, hallmarks (14K/18K/750, maker marks), canvas/stretcher age, printer's dots (= print),
   giclée texture, labels on the back, movement/dial details, edition numbers, period construction, damage.
3. Identify the specific thing (artist / maker / model / period / material). Say what separates it from the common or
   reproduction version, and which of those this one is.
4. Value it with evidence: WebSearch for auction or sold records of THAT artist/maker/model (LiveAuctioneers,
   invaluable, eBay sold, Heritage). Cite at least one source URL for any egg. Use the low end.
5. Realistic hammer price on ShopGoodwill: current bid now, but obvious names get bid up — estimate what it will end at.
6. Verdict:
   - `egg`: specific identification + evidence of $1,000+ value + reason other bidders will miss it. Include max bid.
   - `lead`: real and profitable (profit ≥ max($50, cost) after 13% fees and shipping) but not an egg. Include max bid.
   - `ask`: could be an egg, but one detail decides (e.g. signature legibility) — say exactly what.
   - `kill`: one specific line (print, repro, plated, modern, decor, damage, already titled and bid up).

Write one JSON per row to the output file you were given:
`{"pid":"sgw<id>","verdict":"egg|lead|ask|kill","what":"…","evidence":"… with URL","value_low":n,"hammer_est":n,"max_bid":n,"ends":"…","note":"…"}`
Append after each row. Final reply: counts, then every egg/lead/ask in full.
