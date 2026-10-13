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

### 2026-10-12 (night) — first cloud run, coverage fix, worker live
- **Lens worker (userscript) running in Dylan's Chrome**: ~5 listings/min, 0 Google blocks in the first 90, 42% flagged.
  First token was rejected (HTTP 401) — results buffered in the browser until a valid token is saved. Userscript 1.1
  backs off uploads for 5 min after a failure; 1.2 switches to a newer cloud queue every 40 items.
- **Cloud run 1** (Actions): harvest worked from GitHub's servers — 97,189 listings / 6 h, 800 queued — but the commit
  failed: my push and the bot's both appended to `db/events/2026-10.jsonl` → git conflict. "Append-only merges cleanly"
  was wrong. Fix: `.gitattributes` `merge=union` for db/*.jsonl, bot pulls with `-X theirs` for generated files, retries.
- **Harvest was badly truncated**: sapi returns at most the newest 360 per query; with a 150-mile radius SF antiques had
  5,159 matches and we got 6 h of them. Now: each site's own listings (no radius → no overlap between neighbouring
  sites) + adaptive price-band splitting whenever a query is capped before the window ends. Test: 5 metros × 3 cats ×
  24 h → 7,380 listings, 24 splits, 0 still capped.
- `mus` is not a valid sapi category (HTTP 400 for every area = the 413 failed requests). Owner instruments = `msa`.
- Queue order now rotates across areas within each score tier (the first 200 of run 14 were all SF/Seattle).
- STATUS.md is the live dashboard: github.com renders it with listing photos (finds table + flagged table).
  Link: https://github.com/dylanpetty378-arch/game-platform/blob/refurbish/STATUS.md
- eBay is not signed in on the new Mac → Terapeak unavailable; comps fell back to web search. Dylan to sign in.
- Run-14 Stage 2 (in-page loop's 93): 38 flagged → 37 killed by photo, 1 find: SF all-silver squash blossom necklace
  $75 (73.5 g, cast naja, est. profit $110–260).

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
