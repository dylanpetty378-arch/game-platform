# eBay golden-egg deep review

Rows (JSON) are eBay auctions from casual sellers (feedback ≤150), ≤3 bids, ending within 24 h, flagged from
thumbnails as possible golden eggs ($1,000+ value the listing doesn't recognise). Each row has `detail` = the seller's
description, every photo URL, current bid, shipping, location.

For each row: download EVERY photo (`curl -s -o /tmp/res/eb/img/<id>_<n>.jpg <url>`; swap the size suffix to
`s-l1600` for full size) and view it. Read the description. Identify the specific maker/artist/model/period/material
and what separates it from the common/reproduction version. Value it with WebSearch evidence (auction records, eBay
sold, Heritage, LiveAuctioneers) — cite a URL for any egg or lead. Estimate the realistic final price: eBay auctions
get sniped in the last seconds, so an obvious name ends near value; a mis-titled one may not.
Verdict:
- `egg`: $1,000+ low-end value, specific ID with evidence, and a reason the title/photos hide it. Give max bid.
- `lead`: profit ≥ max($50, cost) after 13% fees and shipping, but not an egg. Give max bid.
- `kill`: one specific line.
Remember: no authentication-dependent items (signed sports, designer bags), no untested electronics.
Write JSON per row (append) to your output file:
`{"id":"…","verdict":"egg|lead|kill","what":"…","evidence":"… URL","value_low":n,"max_bid":n,"ends":"…","url":"…","note":"…"}`
Final reply: counts, then every egg/lead in full.
