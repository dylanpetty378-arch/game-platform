# Improvements log + backlog

Dylan's standing instruction: keep finding better ways and update the docs. Log what changed (with evidence) at
the top of the log; keep the backlog ranked. Measure everything against the funnel numbers in the database
(`db.py sql` — flagged rate, Stage-2 keep rate, finds per 1,000 Lens items).

## Backlog (ranked)

1. **eBay Browse API `search_by_image`** — Dylan applied for an eBay developer account (under review, Oct 12). Once he
   shares the App ID/Cert ID (store as GitHub Actions secrets, never in files): run image search for every queued
   listing *in the cloud workflow* — returns priced eBay matches, 5,000 calls/day free. Removes the browser
   dependency for Stage 1 and the Google rate-limit risk; Lens becomes the second opinion. Biggest single upgrade.
2. **Parser quality** — `best` often picks an AI-overview line ("Key Features", "Material: …") instead of a match
   title; ~5% of reads are empty ("Results are personalized"). Store raw match rows (`rows`, now saved by the
   userscript) and re-score offline; tune the flag rule on labelled outcomes (Stage-2 keep/kill events).
3. **Category-match false flags** — rugs, roll-top desks, generic lamps, Lego bulk, dollhouses flag on category medians.
   Add a per-type "category inflation" dampener learned from kills (type → typical med/real ratio).
4. **More sources into the same queue** — FB Marketplace (browser-only; Dylan's account — feeds captured before, see
   history/shipped-sweep-methods.md), OfferUp, estate-sale photo sets (estatesales.net API), ShopGoodwill (API works
   from the container), HiBid. Each needs a harvester that emits the same listing shape with a `source` field.
5. **Liveness checks** — cloud cycle re-checks flagged/find listings and writes `expired` events when deleted.
6. **Specialist exact lookups** — ISBN/UPC → BookScouter/PriceCharting; records → Discogs; Lego set numbers →
   BrickLink. Deterministic value for those categories.
7. **Stage-2 automation** — a cloud job can't see images with judgment, but a Claude session can batch-review
   flagged listings with 1200px photos; consider splitting the flagged list into daily review packets (one PDF/sheet).

## Log

### 2026-10-12 (evening) — the always-on system
- Moved the whole project into the `refurbish` branch of game-platform: docs, encyclopedia, history, scripts, data.
- Database introduced (`db/`, `scripts/db.py`) — every harvest, queued listing, Lens result, stage change, comp.
- Cloud worker: `cloud_cycle.py` + GitHub Actions every 4 h (approved by Dylan). Harvests 6 h of Craigslist
  nationwide, selects the best 800 unseen by seller-ignorance score, rebuilds the queue, ingests Lens uploads, writes
  STATUS.md.
- Lens worker rewritten as a Tampermonkey userscript (fresh page per item → no memory build-up; saves after each
  item; uploads every 25). The iframe loop (v7) is now the fallback.
- Run 14 (in-page loop, before the switch): harvest 262,059 listings (48 h, 29 categories, 413 areas) → 3,000 queued →
  93 through Lens, 38 flagged (41%), 0 blocks, 7 stalls, 2 stale-frame reads, 3 empty reads. Stopped by memory guard.
- Lessons: performance.memory is cached — measure real memory with ps via osascript; Lens result pages land on
  `www.google.com/search?…udm=26`; a stalled iframe can return the previous item's text (now detected and retried).
