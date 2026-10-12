# How to value any item from a photo – method notes (Oct 12, 2026)

Dylan's challenge: "if you're looking for how valuable something is based on a picture, any item in the world, what is the best method?" and "in the whole country you found 9 things? No." This file records what was tested, with numbers, and the pipeline that follows from it.

## Why the Run 12 funnel found 9 in 9,600 (0.09%)

Identification was done by a language model reading 130-px thumbnails on contact sheets. At that size the marks, labels and model numbers that carry value are invisible, so the review really matched silhouettes plus titles. Recall was low; the 9 were the items whose value happened to be visible in shape alone (an F2, a Furby box).

## What was tested (random samples from the same 9,600, Oct 12)

| Method | Identifies brand/model | Found a clear the funnel missed | Cost / throughput | Verdict |
|---|---|---|---|---|
| LLM on 130-px contact sheets (Run 12) | ~coarse type only | baseline (0.09%) | ~250 tokens/item | too weak as the first pass |
| **Google Lens on the listing's first photo** (uploadbyurl, in Dylan's signed-in Chrome) | **22 of 30 (73%)** to brand/model; 6 of 30 added facts the title lacked (Touraine flow blue, Andrea by Sadek, Fire Chief decanter, Nixon 51-30, Martha Stewart punches, Hammond vs "Conn") | yes: Nixon 51-30 at $50 (sells $100–230); Martha Stewart punch lot $20 (~10 × $22) | 2.8–4.6 s/item from a hidden tab, 0 blocks in 58 items → ~780/hour/tab | **the first pass** |
| OCR (tesseract) on 1200-px photos | readable text on 16 of 30, useful on ~3 (boxes, printed matter) | no | free | only as a supplement; Lens already OCRs |
| Headless Chromium (container or Dylan's PC) → Lens | blocked ("unusual traffic") from both | – | – | dead: Google wants a real signed-in browser |
| curl → Lens | 200 but results are rendered by JS | – | – | dead |
| Terapeak (eBay sold) on the identified name | n/a | converts identification into a real spread; corrected 5 agent estimates today | ~3 s/query, no throttling at 40–60/run | **the valuation gate** |

Hit rate on random listings with Lens-first: 1–2 real clears per 60 = roughly 2–3%. On 82,000 Craigslist posts a day that is on the order of 1,500–2,500 candidates/day, versus 9.

## The pipeline (replaces "photo-first" and the thumbnail review)

1. **Harvest** (container, done): every listing with photos from every source – Craigslist 413 areas (`cl_nat.py`), FB/OfferUp local feeds, estate-sale photo sets. Keep id, price, title, area, image ids.
2. **Stage 1 – identify by machine, every listing** (Dylan's Chrome, background): Google Lens on photo #1 via a hidden iframe on a `google.com/robots.txt` tab, event-driven (iframe `load` + MutationObserver – timers are throttled in hidden tabs; this isn't). Store per listing: AI-mode sentence, visual-match rows (source, title, price). Exclude matches that are the listing itself (craigslist.org). ~780/hour/tab; several tabs/windows multiply it. Google's tolerance beyond ~100/hour is the open risk – measure; if it blocks, slow down or rotate windows.
3. **Stage 1 scoring (machine):** parse match prices from eBay/Etsy/Reverb/Chairish/WorthPoint/1stDibs/auction rows → median asking band; score = band ÷ listing price; plus flags: collectible-channel matches (WorthPoint, LiveAuctioneers, Invaluable), AI-mode "sells for / value" sentence, seller-ignorance signals (generic title, no brand token, estate/grandma/moving language, round low price).
4. **Stage 2 – LLM on the top ~10%:** read the Lens text + full-size photos (`lookup.py --photos`), confirm what it is, note condition and the marks to ask for. This is where the encyclopedia entries get written and used.
5. **Stage 3 – Terapeak sold comps** on the identified name (min price set, parts excluded) → profit after 13% fees and shipping both ways → Dylan's rule (≥ max($50, price)) → tier.
6. **Learn:** every Stage 2/3 result goes into the encyclopedia entry for that type (tells, sold medians, "seen in sweeps") and into a per-item ledger so repeats are recognised and estimates get calibrated against real buys.

## What a second identification engine would add
- **eBay Browse API `search_by_image`** (free developer key under Dylan's eBay account, 5,000 calls/day default): returns similar *eBay listings with prices* straight from the container, no browser. Same job as Lens with a priced catalogue; doubles throughput and removes the Google-tolerance risk. Needs Dylan to create the keyset (developer.ebay.com, ~5 min).
- **Google Cloud Vision web detection** (official, ~$3.50 per 1,000 images): best-guess labels + matching web pages; a legitimate, scalable Lens-lite if Lens tolerance turns out to be the bottleneck. Needs a Google Cloud billing account.
- Specialist lookups where photo→value is deterministic: ISBN/barcodes → BookScouter/PriceCharting, Discogs for records, BrickLink for Lego set numbers. Cheap and exact; worth wiring in for those categories.

## Things learned today that matter for the next run
- Lens visual matches often include Dylan's own listing (Craigslist) – drop it before scoring.
- The AI-mode paragraph arrives 1–5 s after the visual matches; the matches alone identify the product, so don't wait for it.
- Hidden-tab timer throttling stalled a setTimeout loop at 2 items/160 s; the event-driven loop did 28 in 130 s.
- A heavy Google homepage tab froze under repeated iframes; the robots.txt tab did not.
- Scam pattern on Craigslist: placeholder price + "email for info" + stock photo. Drop at harvest.
