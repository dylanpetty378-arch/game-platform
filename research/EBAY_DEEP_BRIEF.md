# eBay golden-egg deep review

Rows (JSON) are eBay auctions from casual sellers (feedback ≤150), ≤3 bids, either newly listed (any end date) or ending within 24 h, flagged from
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

## Lessons added Oct 15 2026 (Marie jar 377556654389)
1. **Value by condition band, not by name.** First find comps in the SAME condition. Signed San Ildefonso
   blackware: very good $2,600–5,400, scuffed $1,000–1,850, slip loss or repairs $250–1,150. That is a 70–90% drop.
   The first pass valued a flaking jar at the clean price and called it an egg. `value_low` must come from the
   condition-matched band, and the evidence must cite at least one comp in that band.
2. **Signed pieces: compare the signature, don't just read it.** Download 3–5 authenticated examples of the same
   signature era (dealer sold pages, auction lot photos) and put them side by side with the listing's base photo.
   Check the letterforms, how the mark was made (fired-in vs scratched after), and whether design and era agree.
   Save the comparison image to /tmp and send it with any egg.
3. **Check the seller's other listings.** Add the id to research/pools/ebay-seller-req.json and run detail mode.
   It shows whether this is an estate or garage clear-out (good) or a reseller who knows the category (bad), and it
   may turn up a second find.
4. Put the auction end in Dylan's time (Central) and the hours left on the first line of the report.
