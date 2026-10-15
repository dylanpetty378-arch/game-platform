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
5. ~~Liveness checks~~ — done Oct 13 (cloud_cycle.liveness, every cycle).
6. **Specialist exact lookups** — ISBN/UPC → BookScouter/PriceCharting; records → Discogs; Lego set numbers →
   BrickLink. Deterministic value for those categories.
7. **Stage-2 automation** — a cloud job can't see images with judgment, but a Claude session can batch-review
   flagged listings with 1200px photos; consider splitting the flagged list into daily review packets (one PDF/sheet).

## Log

### 2026-10-13 (17:00–17:40) — unlensed pool drained; tells in 128 entries
- FIX: 95 size-kills had titles the bulky filter passed (tricycles, bikes, sleds, floor lamps, coolers, computers,
  amplifiers, street signs, churns, 5-gal crocks). `scoring.py` gained those words plus a HEAVY list that wins even
  when a small word (sign, lamp, radio) is in the title. Guitar amps and radios stay allowed.
- Last 851 never-Lensed rows: 4 agents, 851 kills, 0 asks. Three pools in a row now show the same shape: the
  never-Lensed queue is ~75% furniture/decor by title and the rest dies on weight or retail pricing. So the harvest
  ranking is letting too much furniture through — `is_bulky` should learn from these kills (next improvement).
- Golden-egg tells now in 128 entries. This batch's standouts: Ping Anser "Redwood City, Cal."; B.F. Meek & Sons
  head plate; Griswold #13 slant-logo; Russell & Erwin Standing Elk knob; Buddy L 27" trucks; Handel 6xxx shade
  signature; Dunhill Rollagas struck 750; WWII black-crackle Zippo tells; Enid Collins pre-1972 "ec".

### 2026-10-13 (16:00–17:00) — unlensed triage, 4 new entries, tells to 80 entries
- Unlensed pool (never read by Lens): 900 rows, 4 agents → 895 kills, 4 asks, 1 buy. The buy: a Fender silverface
  Champ (AA764 spec, c.1975–81) listed as "Vintage fender amplifier" at $50 in Delaware; seller says it works; sells
  $350–550 → Tier A, but it is a tube amp (Dylan's electronics rule — his call) and needs a sold check.
- Zap Comix #1 at $50 was re-opened from kill to ask after the new underground-comix entry: a 35¢ copy with
  "Printed by Don Donahue" on the back cover is the ~5,000-run 2nd printing ($500–900), without it the 100k Print
  Mint 3rd ($40–70). Lesson: comics verdicts need back-cover/indicia photos; printing decides everything.
- New entries: watt-pottery, underground-comix, wood-cased-telephones, vintage-ray-ban-sunglasses (asking-price
  based, confidence low — Terapeak pass needed).
- Golden-egg tells now in 80 entries (527 to go). Standouts: Stanley No. 1 (no cast number, no lateral lever)
  $1,200–1,800; Van Briggle 1902 incised = $11k; Kamaka Gold Label ~20× a Makala; Hamm's Scene-O-Rama motion sign.
- Unlensed-pool lesson (3 agents agree): ~80–95% die on title alone, the rest on the body; the plausible types fail
  on weight/shipping, not identification. A weight filter before photo work would save most of the time.

### 2026-10-13 (15:20–16:00) — triage round 6 under the no-generalization rule; golden-egg tells begin
- Triage: 1,773 rows (1,030 lensed + 743 flagged), 8 agents, every verdict naming the specific variant. 1,760 kills,
  13 asks, 0 buys. Best asks: Lionel postwar lot $50 with a 6520 searchlight car whose generator is ORANGE (scarce
  vs maroon/grey) → Tier A if they run; Kalo Shop hand-wrought sterling bracelet in the 222 S. Michigan box at $199
  (offer $120); Watt Pottery #16 pitcher in the scarce Tulip pattern at $20; a Campagnolo Nuovo Record crank at $90
  (offer $60); a 14k-stamped ring at "make offer"; a possible 1930s Dunhill Unique in a $65 lighter lot.
- The specific tells that decided kills are now field notes (56 added): Zap Comix #1 25¢ Plymell vs 35¢ Apex; Ping
  Zing 85020 vs 85029 Scottsdale; Dubl Duck Goldedge vs Special No.1; Shirley Temple 1972 vinyl vs 1930s composition;
  Lens "best" was wrong on nearly every photo-checked flagged row.
- Golden-egg tells: 48 entries (the most-seen non-dead types) now have `### Golden-egg tells`, the specific variants
  worth multiples and how to see them in a photo (e.g. Illinois Bunn Special "23 Jewel 60 Hour" dial; Hummel "/X"
  jumbo suffix; Trifari jelly belly; Red Wing cobalt butterfly; Accutron Spaceview). 559 entries still need the
  section (`enc.py lint --tells`); next batches go in order of sightings.
- New-entry candidates from this round: Watt Pottery, underground comix, Stromberg-Carlson wood deco phones,
  vintage Ray-Ban B&L (16 lines in research/new-type-candidates.md).
- Standing idea (agent): types that only fail on the $50 floor at $20–65 asks (Watt, Czech Deco glass, Toshikane)
  are worth a ≤$15–20 standing search.

### 2026-10-13 (14:00–15:10) — the website, and eBay comps from the cloud
- **Refurbish website** is live at a hidden path on the Vectus site (URL in the claude.ai project; `spec/refurbish.md` in
  the Vectus repo). Own Postgres database beside the game's, own code, no shared tables. Pages: dashboard, leads,
  listings search, item file (photos, Lens, history, comps, entries, notes, tracking), encyclopedia, Lens control,
  bought/sold ledger, printable report. JSON twins under `<base>/api/*.json`.
- Sync: reads `db/manifest.json` (scripts/manifest.py, run by the workflow before every commit) and raw files — no
  GitHub API, which is rate-limited per IP on Fly. First sync stalled on the API and on a single 15k-row insert;
  fixed with the manifest and 500-row chunks. Full sync from empty ≈ 2 min; incremental every 10 min.
- **eBay keys work.** First cloud run: 194 queries, 187 with results. The Browse token works; the Marketplace
  Insights (sold) token is refused, so these are ACTIVE asking prices (source `ebay-active`), a ceiling only. Dylan
  can apply for the Insights scope at developer.ebay.com; until then every lead still needs a sold comp.
- Harvest at 13:35 UTC succeeded end-to-end with the type_model fix and the manifest step.

### 2026-10-13 (12:00–12:40) — triage round 5, 48 more entries deepened, field notes
- Triage: 347 rows (208 lensed + 139 flagged), 4 agents. 343 kills, 4 asks, 0 buys.
  - Postcards: 65 cards for $35; needs the card count and the number of RPPCs.
  - Snap-on/Blackhawk tool tote: $50, pickup only.
  - Violin bow: $75; needs a maker stamp.
  - 3 USN officer cap badges: $10; ask whether they are sterling.
  None clears the rule without the seller's answer.
- Recurring lesson: multi-item posts price each piece in the body, so the title price is the cheapest piece. Read the
  body before the photo. Dealer tells now recorded in the original-art field notes.
- Deepened entries: 48 more (96 in total). Corrections:
  - Real Ainsworth Bruntons are aluminium; brass ones are usually Indian replicas. Our open Brunton lead is aluminium,
    so it is fine.
  - The Shure "Elvis" mic is the 55S.
  - The Pioneer RT-707 takes 7" reels only.
  - Post-1963 Buescher Aristocrat saxophones are Selmer-era student horns.
  - Yamaha green-label guitars are 1966–67 Japan-only.
  - Heywood-Wakefield "Amber" is the post-1992 finish.
  - Delta Electric ran 1913–78.
  - Nikon AI-S is identified by the bayonet notch.
- New `## Field notes (learned in triage)` section added: 14 facts filed. 22 facts for types with no entry went to
  research/new-type-candidates.md (brass instruments, reloading dies, tennis rackets, industrial gauges, soapstone foo
  dogs…).

### 2026-10-13 (11:55) — FIX: harvest runs failed at push
- The 11:31 harvest built `research/type_model.json` but the commit step only staged `db q STATUS.md status.json`.
  The unstaged file broke `git pull --rebase`, so the whole harvest was lost. Health showed a FAIL (0/5 runs ok;
  the rest were pending push runs cancelled by newer pushes, which is normal).
- Fix: the commit step now also stages `research/type_model.json`, on both main and refurbish. Lesson: any file a
  cycle step writes must be in the `git add` list.

### 2026-10-13 (10:30–11:00) — 48 entries deepened (research/DEEPEN_BRIEF.md)
- The 48 most-seen non-dead types with thin entries (<7 KB) were rewritten by 6 research agents (≤30 web searches
  each). Each now has deeper maker/marks/finish detail, a **Quick ID checklist** and a **What to tell the buyer** paragraph.
  Every earlier fact, comp and sweep line is kept, with no invented comps.
- Errors fixed along the way:
  - Ivory Pyralin is DuPont's.
  - Emerson's 4th model digit is the blade count.
  - The vintage Barbie body mark is "Barbie T.M.".
  - Royal Doulton HN2000 dates to the late 1940s, and the © year is the design year.
  - Smith-Miller is postwar.
  - TNF Steep Tech dates from 1991.
  - The red-white-blue ILGWU label is 1974–95.
  - Valje was founded by Tom Flores in LA.
  - Josef Originals' Japan production began in 1959.
  - Revere Ware is copper-clad stainless steel.
- Flagged, not changed:
  - Shawnee Corn King/Queen colours need checking against the Mangus guide.
  - Several Terapeak lines are contaminated by parts or accessories: Gibson J-45, Martin D-18, KEF LS3/5A, and new LED
    signs in beer neon. Re-query these with exclusions.
- Batch the rest the same way: next are the types ranked 49–156 by sightings.

### 2026-10-13 (10:00) — quick-reject for types that can never pass
- `type_model.py build` now marks a type **dead** when its rubric p75 × 0.87 − 2 × ship_cost_to_buyer < $20, meaning a
  single item can't clear the rule even at a good price. 208 of 605 rubric'd types are dead: Avon bottles, dinnerware,
  prints, advertising tins, carnival glass and the like.
- `adjustment()` gives dead types an extra −1.5 when the classifier is confident, unless the title signals multiples:
  lot, collection, set of N, N pcs, a count, plurals such as figurines/heads/albums/tools, assorted, misc.
- Calibrated against the 40 open leads. A −3 penalty without the plural exemption demoted 9 of them (Bossons heads,
  Hummel figurines, LP albums…). The final version mildly demotes 4 single items and spares every lot. Of the last
  20k harvested listings, ~1.4k were in dead types.
- health.py now also reports encyclopedia comp coverage (459/607 with Terapeak), open leads (40) and the text-triage
  backlog.

### 2026-10-13 (09:30) — round 4 + calibration lesson
- Triage round 4 (917 listings): 1 "buy" + 8 asks from agents; Terapeak re-check killed 4 of them — **agent
  general-knowledge resale estimates ran ~2–3× higher than Terapeak sold medians** (lead soldiers $120 est vs ~$30/lot
  sold; Reebok $120 vs $29; Ideal toy $110 vs $25; Garcia tee $120 vs $37). Rule: no lead goes to Dylan without a
  Terapeak (or dated sold) comp; agent estimates are only for triage ordering.
- CSV splits written with Python's csv module use CRLF → agents' curl URLs broke; write with lineterminator='\n'.
- Policy filter: butterfly knives/balisong, Nazi militaria added (eBay-prohibited).

### 2026-10-13 (07:10) — Terapeak wave 2 and the eBay bot check
- 1,100 queries were generated from every entry's Collectible and Top tiers. The first 369 ran (341 comps, 172 entries
  got top-tier sold data). Then eBay served its "Pardon Our Interruption" bot-check page, so the rest returned nothing.
  The loop now has to stop on a run of zero-result queries or that page title, and stay under about 300 queries per
  session (research/terapeak-bulk.md). Indices 369–1099 are still to run.
- Triage round 3: 250 listings, 2 weak asks. Policy filter now also covers bear claws, eagle feathers and sea turtle.

### 2026-10-13 (06:30) — the encyclopedia now steers the harvest
- `scripts/type_model.py`: a naive-Bayes title→type classifier, trained on about 2,500 labelled titles (review
  events, research/types.tsv and entry names). It is rebuilt every harvest cycle. `scoring.score()` adds the predicted
  type's value × confidence. Value = clamp(expected_profit_typical/25, ±3) + 0.5 × (undervalue_frequency − 3), taken
  from the entry's rubric. Examples: pocket watches +0.96, straight razors +1.35, Hummel +1.0, decorator lamps −0.85,
  antique bottles −0.68. Cost is about 1 ms per title.
- Category learning now uses review outcomes (asks and finds) instead of Lens medians. Jewelry +1.1, art −1.1 (mostly
  prints), furniture −1.3.
- CLIP gets positive prompts for the lead patterns: collections laid out, open pocket-watch backs, razors, surveying
  instruments, chalkware heads, maker marks, and silver jewelry.
- 23 new entries for types first seen in triage, 607 in total.
- Backlog idea from the research agents: a quick-reject rule. If a type's median × 0.87 − round-trip shipping is under
  $50, the type can never pass at any price, so demote it hard. That is partly covered by the type value, since
  expected_profit_typical is negative for those types.

### 2026-10-13 (05:00–06:30) — triage everything, Terapeak at scale, cron fix
- Text-triage of ALL 678 Lens-scanned-but-unflagged listings (4 agents) + 206 flagged: flagged → 0 buys; unflagged →
  1 find (Ainsworth Brunton transit $35, Terapeak median $99–150) and several asks. Total open leads now ~30; PDF of the
  7 best sent to Dylan (`Refurbish-New-Leads-2026-10-13.pdf`). Review-cycle now triages all scanned listings.
- Scoring: collections/lots + full-bee/Goebel + jewelled/hunter watches are lead patterns (boost); "lot of N" no longer
  penalised.
- Terapeak: 469 identification queries in one sequential loop (Web-Worker-paced) → 370 comps; 265 encyclopedia
  entries got dated sold comps. Method in research/terapeak-bulk.md.
- **The 4-hourly cron had never fired** (no `schedule` runs in Actions history). Fixes on main AND the refurbish copy
  (push runs use the branch's copy): separate concurrency groups for push vs harvest, and push runs now harvest when the
  last harvest is > 4.5 h old (the Lens worker pushes every ~4 min, so harvests can no longer stall). First fallback
  harvest started 05:31 UTC.

### 2026-10-13 (04:00–06:00) — deep research, rubric, encyclopedia restructure
- Dylan: passenger-seat size rule (hard exclusion), deep research on every scanned item, rubric of key facts per type and
  per item, full dossiers for anything bought/sold, one working chat (scheduled review task deleted).
- Encyclopedia moved to one file per type (`docs/encyclopedia/entries/`, `scripts/enc.py`); duplicate sections merged;
  48 new researched entries (wave 1 of 417 types found in the 960 scanned listings); all 168 older entries upgraded
  to the full template with machine-readable rubric (`enc.py lint` = 0). 216 entries total, synced to `item_types`.
- Research findings that changed the process:
  * Non-flagged listings hide the real leads: the best lead of the night (a "quartz" Jostens watch whose dial reads
    21 Jewels — possible 14K, Tier A) was never flagged by Lens. Type research over ALL scanned items finds them.
  * Lens medians are asking prices / category matches; > 5× asking price usually means a wrong match.
  * Read text on the item (dial, base, labels) — it contradicts titles. Wrong names in titles ("Napoleon") are leads.
  * Same photo posted twice → deduped in the queue now. Offensive-imagery / ivory items → excluded (eBay bans).
  * Empty Lens reads ("Results are personalized") ran at 28% on the v1 worker at night → auto re-queued at ingest
    (max 2 tries); 113 backfilled.
  * Sold data: container can't reach eBay sold pages; WorthPoint paywalled; WebSearch is capped at 200 calls per chat
    turn shared by all agents. Terapeak in Chrome works but bot protection (Radware) blocked it after ~160 queries with
    3 parallel loops — run it sequentially, ≥ 2–3 s apart. 161 Terapeak queries imported to `comps`.
  * Metals moved: silver ~$60.7/oz, gold ~$4,144/oz (Oct 2026) — entries pegged to older spot (silver-certificates,
    scarab bracelets, wristwatch gold cases) need re-pegging; any small gold-tone piece with karat marks → ask for the mark.
- Proposed (blocked by the safety classifier, needs Dylan's decision): let the Lens worker also run one Terapeak query
  per Lens page from his browser and upload the comps — fully automatic sold data with no Claude tokens.
- Known encyclopedia clean-ups: merge/alias overlapping entries (film-cameras ↔ film-slr-cameras, hohner-harmonicas ↔
  hohner-chromatic-harmonicas, snap-on-tools ↔ snap-on-vintage-toolboxes, the three reel entries, duck ↔ fish decoys,
  tube-radios ↔ bakelite-and-mid-century-radios); 120+ entries are confidence "low" until a Terapeak pass.

### 2026-10-13 (03:10) — review 41 flagged, what the labels say
- Reviewed all 41 flagged (v1 reads): 0 keeps. Notables killed with reasons: modern cloisonné and Rose Medallion,
  Elgin GF hunter and Swiss Bijou watches at near-market asks, amateur-painted Limoges, unsigned cobalt salt-glaze jug
  (heavy shipping), Gulf brass dallah, decorative byobu screens, an antique-mall dealer's watch case.
- 432 listings now have a photo-review label (18 keeps). Lens price features do NOT separate keeps from kills (keep
  rate ~1–3% in every n × ratio bucket) — the flag rule is only a coarse gate; the leverage is in what gets queued.
- Furniture/bulky words (desk, table, chair, cabinet, mirror, trunk, chest, dresser, rocking…) = 120+ kills, 0 keeps →
  `scoring.BULKY` −4 title penalty (table lamp/clock exempt). Frees Lens capacity for small shippable items.
- Too few positives (18) for a learned ranker yet; revisit at ~60 keeps.

### 2026-10-13 (night) — the machine checks itself
- `scripts/health.py`: one command, PASS/WARN/FAIL for every step (workflow runs, harvest age/failures, queue age/size,
  Lens freshness, read quality of the last 200 — priced ≥80%, empty ≤5%, worker version mix — flag rate, JSONL
  integrity, inbox drained, flagged backlog). First run: all PASS; last 200 reads still v1 (92% priced, 5% empty, AI 32%).
- `scripts/review_helpers.py`: flagged worklist (TSV with Lens fields), listing body/liveness fetch, shortlist export,
  Terapeak helper JS.
- `docs/review-cycle.md` + Claude scheduled task "Refurbish review cycle" (every 6 h, cloud): Stage 2/3 now runs
  without anyone opening a chat. Messages Dylan only for Tier A/B finds or breakage.
- Liveness in every cloud cycle (`cloud_cycle.liveness`): open leads (flagged, keepers, finds) re-fetched; HTTP 404/410
  or a deletion notice → `expired` event, so dead listings drop off STATUS and out of review. First run: 47 checked, 0 dead.
- Gotcha: raw.githubusercontent.com caches a branch file ~5 min; a local `origin/<branch>` ref can be stale — check
  with `git fetch` + `merge-base --is-ancestor` before concluding a push failed.

### 2026-10-13 (early) — first top-10 report from the database
- ~830 listings through Lens (worker v1.3 on the CLIP-ranked queue since 02:27 UTC), 360 flagged → all triaged; 40
  photo-reviewed in full; Terapeak sold comps for ~25 item types (eBay now signed in on the Mac); listing bodies pulled
  for every candidate (they changed 5 verdicts: per-item pricing, local-only, "stops running").
- Funnel: flagged → photo keep ≈ 1 in 12; keep → passes the rule ≈ 1 in 4. Lens-flag yield on the OLD title-only queue
  was mostly furniture; the CLIP-ranked queue's flags were visibly better (portraits, Islamic bronze, Limoges, guitars).
- Earlier-run finds (camera lot, santo, chenets, Hoyt, Furbys, Thorens, cymbals) were liveness-checked and added to
  the DB as `decided` events so the database holds every live lead.
- `scripts/build_report.py` builds the printable report from a spec (seller contacts stay in the spec, not the repo).
- Lesson: always read the listing body before comps — Lens + photos can't see "$20 each", "local cash only", or
  "runs for a bit then stops".

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
- **True volume is ~400 K listings/day** (cloud run 2: 143,076 in 8 h, 291 price splits, 0 capped, 0 failures). Lens
  capacity is ~5–7 K/day, so prioritisation is now the main lever. Added category priors (antiques/collectibles/jewelry/
  art/cameras/instruments up; furniture/RVs/boats/wanted down) plus a LEARNED per-category adjustment computed from
  Lens outcomes every cycle (strong-signal share vs average, shrunk until ~150 results). Next: learn from Stage-2 keep/
  kill and finds instead of Lens medians (which are inflated by category matches), then a title/image model.
- **CLIP image pre-ranking** (`scripts/clip_rank.py`, open_clip ViT-B-32, free on the Actions CPU): the best 12,000 title
  candidates per cycle get a photo score ("looks collectible" prompts vs junk prompts); combined = title + 0.6 × clip.
  Test on 400 random listings: top = Roseville bowl, original paintings, Inuit print, enamel art; bottom = CPAP part,
  file cabinets, bikes, barbells. 13.5 img/s on 2 threads. Embeddings are not stored yet (size); a learned ranker on
  embeddings + our outcomes is the next step (recompute from photo URLs while listings are live).
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

## 2026-10-13 — Why yield looked like it fell, and the eye-first test
- **Diagnosis (7,800 reviewed listings, 109 leads):** the title score that picks 800 of 30–140k fresh listings per
  harvest does not predict leads. Lead rate ≈1.4% in every score fifth, every category, price band and title keyword;
  CLIP fifths the same; Lens-read 1.2% vs not 1.7%. Early runs looked richer because "leads" then were agent guesses
  (2–3× high); with sold comps required, Run 12 was ~1 find per 1,000, the same as now.
- **Redo of open leads under the current process:** 30 dropped (no sold comp, comp shows no margin, repair, authentication),
  3 re-based on Terapeak (Bell 500-TX helmets ask, cobalt stoneware ask, Chinese silk panels Tier A ask).
- **Eye-first test (scripts/eye_screen.py, run eye-20261013-1904):** 116,850 listings (12 h, 17 categories) → 91,277
  after size/junk filters → random 12,000 as 100 contact sheets → 261 flagged by 8 agents (2.2%) → deep review:
  11 asks, 0 buys. Per deep review: 4.2% asks vs ~1.4% for the score-picked 800 (≈3× efficiency). Per listing seen:
  about the same yield. Eye flags misread ~1 in 7 thumbnails; the body text killed most fast.
- **Conclusion:** neither title nor thumbnail finds golden eggs at a useful rate; the base rate on Craigslist ≤$500 is
  ~1 sold-comp-confirmed find per 1,000 listings. The eye screen is kept as the selector because it is 3× cheaper per
  lead. Knowledge from the review: research/eye-knowledge-20261013.md.

## 2026-10-13 (late) — ShopGoodwill golden-egg scan
- scripts/sgw.py: public buyer API (no login) → 49,266 auctions ending within 36 h in egg-dense categories → 13,383
  in pool → 112 contact sheets → 77 flags (GOLDEN_EYE_BRIEF) → full-photo review with web evidence (GOLDEN_DEEP_BRIEF):
  **0 eggs, 1 marginal lead** (hand-painted Soviet copy of Kramskoi listed as a print, max bid $35).
- Why: Goodwill staff and its bidders catch the obvious; what's left at low bids is reproductions, prints, plated
  watches, souvenir "Native"/"Asian" decor. Real pieces that showed up (A.R. Valentien Rookwood 1885, 1959 Mourlot Miró,
  6.9 g 14K) were already bid toward value or damaged.
- Lesson: on photo-rich, expert-watched marketplaces the photo is the same for every bidder, so eggs there are
  rarer than on Craigslist. Golden eggs need either an information edge (marks only in photo 2+, which pros also
  open) or a *competition* edge: venues with few bidders and bad photos (small regional auctions, estate sales).

## 2026-10-13 (evening) — DFW estate-sale galleries (scripts/esn.py)
- 85 sales this week, 12,913 photos → 108 sheets (ESTATE_EYE_BRIEF) → 153 flags → full-size + auction records
  (ESTATE_DEEP_BRIEF): **1 egg-grade** (hand-signed 1968 Warhol/Viva poster, Dallas — needs authentication, Dylan's
  rule normally excludes; flagged for his call), **13 leads**, four of which are $1,500+ if the on-site check goes right
  (two Disneyland Art Corner Sleeping Beauty cels, Grande Baroque flatware if sterling, the Warhol). PDF to Dylan.
- Best yield of the day per photo reviewed: estate sales have no bidders and companies only caption ~10% of photos.
- Bug fixed: ~25% of estate flags pointed at the wrong photo — cell labels under thumbnails were read as the next
  row's. Labels now sit in a yellow tag inside the top-left of each cell (eye_screen.py).

## 2026-10-13 (late afternoon) — eBay casual-seller auctions (scripts/ebay_eggs.py + ebay-eggs workflow)
- Browse API from Actions (api.ebay.com is blocked from Claude's container): auctions ending ≤24 h, ≤$200, ≤3 bids,
  seller feedback ≤150, in Art/Antiques/Pottery & Glass/Jewelry & Watches/Cameras/Collectibles/Instruments/Militaria
  → 15,904 (12,783 without sports cards) → 107 sheets → 67 flags → full listing + every photo (detail mode) →
  **0 eggs, 2 thin leads** (Wally Shoop bronze ended first; Qing-type lotus jar max $175).
- Day total: ~170,000 listings/photos screened across Craigslist, ShopGoodwill, DFW estate sales, HiBid (sample) and
  eBay → 1 egg-grade item (needs authentication), 0 shippable confirmed golden eggs. A true egg (≥$1,000 unrecognised,
  shippable, ≤$500) is on the order of 1 per 100k+ listings online. The pipeline now covers enough volume to see
  ~50k/day if run continuously; that is the realistic way to find them.

## 2026-10-14 00:15 — scheduled runner (cloud, no device)
- health.py FAIL: lens empty reads 20% (priced 78%). Saved rows carry best="Results are personalized", n=0, no AI —
  measure() saw prices the parser did not, so v2.0.0's empty guard let them through. **lens-worker.js 2.0.1** also
  retries a *parsed*-empty page once, then leaves it in the queue. Loader picks it up within 10 min. Also: cloud ingest
  dropped the worker's `q` block, so health always reported version "v1"; ingest now keeps `q` — next health run
  shows the real worker version and wait/why stats.
- Text triage: 504 lensed + 812 flagged = 1,316 rows (8 agents). 0 buys, 30 asks (all Tier C, mostly "show the mark /
  karat stamp"), 1,286 kills. Logged as events run `review-20261014-0015`. Two asks have real sold comps behind the
  upside: Frankart nude lamp (Terapeak median $200, n=50) and a 1917 Elgin hunter if solid 14K (median $570, n=49).
- Skipped `--unlensed 300`: TRIAGE_BRIEF Rethink rule 1 says the unlensed pool goes to the Lens worker, and the worker
  was live (newest read 0.0 h). The scheduled-task prompt still lists it — Dylan to settle which wins.
- Agents' phone numbers leaked into two triage notes; scrubbed before commit. Brief should say "no phone/email in note".
- Encyclopedia: 48 thin entries deepened (Quick ID, Golden-egg tells, buyer copy; several factual fixes — Nerf/Kenner
  dates, Yashica T4 f/3.5, Homco "Denim Days", Stanley thermos history, Boat and Tote 1944/1965). 14 new entries
  (vintage-comic-books, japanese-tetsubin, class-rings, liddle-kiddles, schramberg-smf-pottery, mechanical-stopwatches,
  chinese-silk-embroidery, vintage-star-wars-figures, mexican-silver, chinese-export-silver, military-insignia,
  antique-tennis-rackets, railroad-spittoons, advertising-china). russian-porcelain and antique-scissors overlap
  existing entries → research/merge-pending/ for a merge, not added. 58 triage field notes into 43 entries; 27 to
  new-type-candidates (several are aliases of existing slugs, e.g. costume-jewelry → costume-jewelry-lots).
- To fix: stopwatches-and-timers ladder ($90–160 for plain Minerva timers) looks ~3× high (Catawiki €30 sale).
- Idea: triage agents should get an alias map (slug → existing slug) so they stop inventing near-duplicate slugs.

## 2026-10-14 03:15 — scheduled runner (cloud, no device)
- health.py: 3 FAILs, none cloud-fixable. Lens quality (64% priced, 34% empty) is measured on the last 200 rows, which
  all predate lens-worker 2.0.1 (worker idle since 00:29Z; Dylan's Chrome closed). Re-judge after the worker runs 2.0.1.
  Queue 444 < 500 only because the worker consumed it; next cloud cycle rebuilds 800.
- **ebay-eggs schedule never fired** (cron `41 */6` on main; only 2 manual runs since it was added Oct 13 20:04 —
  GitHub often skips crons on newly added workflows until the next push to the default branch). Dispatched run 3
  manually at 03:25Z. If it still doesn't fire by itself, a push to main (any commit touching the yml) re-registers it.
- Text triage: 22 lensed + 38 flagged + 300 unlensed = 360 rows (4 agents). 0 buys, 17 asks (all Tier C, no sold comp
  clears the bar), 343 kills. Run `review-20261014-0315`. Unlensed pool triaged this time because the worker was idle
  (prompt asks for it; TRIAGE_BRIEF rule 1 assumes a live worker) — unlensed yielded 14 asks from 300, all Tier C.
- Best asks: 9-doll lot $25 with probable Alexander-kins (sold median $40/doll), bracelet lot $15 with possible 14K
  charms, signed numbered screenprint $25 (artist unnamed by seller — mismatch signal), Hampden hunter $40 if solid 14K.
- Encyclopedia: 48 thin entries deepened (several factual fixes: Blue Mountain 1953, Nemadji 1920–2002, Franklin Mint
  history/"Sterling Plus", F&E = Hedman, Masudaya Gang of Five, Betjemann stamp location, ES Keramik = Emons & Söhne,
  tennis-ball can dates, Byers' Choice clay faces). 7 new: vintage-football-helmets, nancy-ann-storybook-dolls,
  chocolate-molds, industrial-pressure-gauges, eye-wash-cups, western-hats, farm-implement-wrenches. 31 field notes into
  entries, 11 to new-type-candidates.
- Ideas: (1) review_helpers should skip pids already in an entry's "Seen in sweeps" (SMF pitcher triaged twice);
  (2) flagged TSV has 15 columns vs 10 for lensed — unify; (3) alias `industrial-gauges` → `industrial-pressure-gauges`
  in comps; (4) jewelry < $25 with no karat/maker word could be pre-killed (≈40% of the unlensed pool, 0 leads);
  (5) pickup-only asks need a rule (kill, or ask to ship?) — Dylan to decide.
- eBay egg loop (03:34Z pool, 16,026 auctions): screened only the 3,598 ending after 20:15Z (the rest overlapped the
  Oct 13 20:14 pool, already screened) → 30 sheets, 3 eye agents → 38 flags → detail mode (run 4) → 3 deep agents:
  **0 eggs, 0 leads**. Paintings/prints were 25 of 38 flags and all were reprints, hobby art or book plates — the eye
  brief over-flags "aged" paintings on eBay; the description settled every one. Closest: Pfretzschner 301 student violin
  (needs sold check, ~$140 max bid). Idea: `sheetpool` should drop auctions already in the previous pool automatically.

## 2026-10-15 — review cycle back on; eBay pool + Craigslist asks
- The scheduled "Refurbish review cycle" had been disabled since Oct 14 03:53Z; re-enabled with a golden-egg-first prompt
  (eBay every run; ShopGoodwill 00:14/12:14; Craigslist 12:14; DFW estate sales Tue 12:14; daily one-line status).
- eBay pool 12:09Z: 12,664 new auctions → 106 sheets → 60 flags → full listings → 0 eggs, 5 leads (Hiroshige I Vertical
  Tokaido Numazu — original only if the 1855 seals show; Pfretzschner bow; late-Qing censer; papillon vase; a scroll that
  ended). `ebay_eggs.py sheetpool` now skips auctions already screened (research/pools/ebay-screened.json);
  `ebay_eggs.py flags <run>` writes the flagged file.
- Terapeak on the 11 open Craigslist asks: 2 kept (Smith-Miller + Thimble Drome lot ≈ $900 if originals; surf scoter decoy
  median $270), 9 dropped.
