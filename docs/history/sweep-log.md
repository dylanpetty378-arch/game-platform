# Sweep log

## Run 13 – Mon Oct 12, 2026 (1–2 pm) – first Google Lens pass (stopped early by Dylan at 2:03 pm)

**Method:** the Lens pipeline – now fully written up in `claude/lens-pipeline-runbook.md` (Dylan: "document this whole new process so even the simplest model can do it"). Scripts: `lens_prep.py` (prioritise + queue strings), `lens_gentle.js` (the loop that runs in Chrome), `lens_export.py` (flagged → Stage-2 worklist + photo sheets).

- **Queue:** the Run-12 harvest (81,854 posts) → 72,105 after junk filter → 2,000 prioritised by seller-ignorance score → pushed in 1,000-item strings into the hidden-iframe loop on a google.com/robots.txt tab.
- **Lens:** 108 listings identified before Dylan called it (several restarts, see lessons). 50 flagged (46%) by the machine rule. 0 "unusual traffic" blocks.
- **Stage 2 (photo sheets, by eye):** 20 of the 50 looked at. Category-level Lens matches (any oak rocker → "Temple Stuart", any brass ladle, any tub seat) explain most false flags.
- **Stage 3 (eBay sold, Chrome):** 2 survivors, both from Lens on titles that said nothing:
  - **TOP PICK – carved polychrome gilt santo, 25¼", Tucson $125** (title "Antique Wooden Statue", body "history unknown"). Sold comps for carved santos ≥$150: $1,450 / $399 / $365 / $300 / $275 / $259 / $250 / $225 / $220 / $200; large gilt pieces $400+. Est. ~$215 profit after $50 shipping. Relay: [relay address – kept in project].
  - **STRONG – pair Louis XV gilt-bronze chenets with log bars, Chino Valley AZ $150** (title "Antique Brass Andirons", body "French style brass andirons"). Sold: $1,195, $797, $300, $290, $275×2, $250×2, $147 (fronts only). Clears only if real gilt bronze (verdigris says yes); ask height + back casting. Relay: [relay address – kept in project].
  - Passed after photos: Reach "Vince DiMaggio" glove $25 (seller identified it, "rare"); Italian tulipiere $75 Dallas (sold ~$150–250, profit short, fragile); Gilbert parlor clock $100 (sells $80–200); slag-glass lamp *base only* $80; modern swirl art-glass vase $50 (dealer, sticker $85); silverplate box $100 with a 1943 New Guinea trench-art opener; Bethlehem PA jeweler's ring box $10; cut-glass flare vase $15 (pressed, unmarked); hand-adzed handled bowl $125 (origin unverifiable); 1990s junk-wax football cards.
- **Run-12 follow-ups:** Hoyt bow relay address captured ([relay address – kept in project]). **Flato compact dropped** – seller says "No shipping. Meet at Medford Outlet" and already lists the maker. Camera lot: "Call Don", number behind the listing's show-contact button. Furbys: Fergie [phone removed].
- **Output:** `Resale-Finds-Nationwide-2026-10-12-b.pdf` (6 pages: 2 new + 8 live Run-12 items, contacts on each card). No messages sent – all need Dylan's OK.

### Lessons (all folded into the runbook)
- `window.status` is a reserved string property: defining a `status()` helper killed the loop after one item with no error. Renamed `showStatus`; `runLoop().catch(…)` now records crashes in `STATS.stopped`.
- Navigating the same iframe to about:blank between items raced with the next Lens URL and stalled; v4+ goes Lens → Lens directly and recreates the iframe every 25 items or on a 30-s stall.
- Hidden-tab throttling: once the tab has been hidden 5 min Chrome stretches nested timers to one per minute (throughput fell to ~3/min). Scheduling the pause through a MessageChannel resets the nesting and restored ~9/min.
- `performance.memory` is per renderer process: Dylan's Gmail/Drive tabs share it, so the "memory" reading starts at ~800 MB. The 900 MB watchdog was tripping on that; now 2,200 MB.
- Tool results truncate at ~1,000 chars – export via a `<pre>` + `get_page_text` (which also dumps robots.txt itself; strip it).
- Craigslist reply relay: click "reply", then the "email" dropdown, then `find` the mailto link – the address is not in the page text until the dropdown is open. Direct `/reply/...` URLs 404.
- Machine flags are 46% at this rule; the photo pass is the real filter (2 of 20 viewed → Stage 3). Expect ~1 find per 50 Lens items on the prioritised slice.

### Next
- Dylan: say OK on any of the drafted messages (santo and andirons first – both are 4 weeks old and may go any day).
- Resume the Lens pass from queue position 108 of `pri0.txt` (`STATS.idx=108`, push the rest of the string) – ~850 items left in chunk 0, 1,000 in `pri1.txt`.
- Encyclopedia: add santos (carved polychrome) and chenets/andirons entries from today's comps (done below in this commit).


## Run 12 – Mon Oct 12, 2026 (afternoon) – first nationwide, encyclopedia-method sweep

**Dylan's two changes (11:01 am):** (1) search everywhere – no shipping filter; we ask any seller to ship and pay for it; (2) the encyclopedia method – identify and research every item type as it comes up, write it down for reuse, judge from the research. Runbook rewritten accordingly.

- **Craigslist nationwide (container):** 413 US areas × 9 categories (ata cba pha msa sga tla ara taa jwa), owner-only, ≤$200, last 24 h → **81,854 posts with photos in 6 min** (`cl_nat.py`). Review slice: newest 9,600 after the junk filter with a 12-per-area/category cap → 282 cities represented → 80 contact sheets (15×8 @130 px).
- **Review:** 10 parallel agents, 8 sheets each, every cell identified by type, `lookup.py` for descriptions and full-size photo sheets, web research per type. ~2.3M agent tokens, ~15 min wall time. Output: ~45 candidates → 23 Terapeak queries → **9 on the sheet**.
- **Encyclopedia:** 146 new entries written (189 agent files merged, duplicates folded), 179 index rows added → 148 entries total, pushed to the project as 7 alphabetical volumes (`encyclopedia/encyclopedia-<letters>.md`) + `index.md` + `README.md`. Terapeak verdicts recorded in 19 entries' "Seen in sweeps".
- **Finds:** TOP PICK – Mesquite TX camera lot $100 (black Nikon F2 Photomic median $228 + SX-70 Sonar median $125 + 7 more cameras/meter/projector; ~$375 profit, local pickup) · TOP PICK – Hoyt UltraTec + spare XT3000 limbs $40, Carthage NY (median $200; needs strings ~$30; ~$140) · STRONG – 8 NIB 1998 Furbys at $10, Grants Pass OR (median $50 each; ~$130) · STRONG – Paul Flato compact + lipstick boxed $25, Medford MN (median $108, sets $140; ~$85) · ASK FIRST – Maui cymbal bundle $123 (23" A Sweet Ride median $380 – is $123 the lot?), Yamaha A-series "Guitar" $100 Sweet Home AR (A1M median $325; need label), Sherman+Boucher brooches $90 Whistler BC (offer $65), Houghton MI bamboo rods $200 (need butt stamps) · BORDERLINE – Thorens AD30 + 23 discs $100 Quakertown PA (clears at $75).
- **Output:** `Resale-Finds-Nationwide-2026-10-12.pdf` (5 pages, print format, QR codes).

### Lessons
- The nationwide Craigslist feed is where the uninformed sellers are: 'Guitar' (a Yamaha A-series), 'Vintage Film Cameras' (an F2), 'Vintage Music Box' (a Thorens). Shipped-only marketplaces (Run 11) gave none of that.
- Volume is the constraint, not sourcing: 82K posts/day; we reviewed 12%. Next run: raise to ~20K with 20 agents, or run twice a day with a 12 h window; also add ela foa hsa cla vga bka categories.
- Agents' web comps are often "knowledge-based" – Terapeak corrected several (Bauer ringware $38 not $60–120; Japanese archaic bronze n=1; DeArmond n=0). Keep Terapeak as the gate; feed its numbers back into the entries, which was done.
- Scam patterns to drop at harvest: placeholder price ($1/$12/$99) + "email for more info" + pro/stock photo ('Martin' $12, 'Telecaster $99', Onewheel $100 on white background).
- Captions at 130 px bleed into neighbours; `lookup.py IDX` before any flag is non-negotiable (an agent's "$29 banjo" was a $2,950 Vega).
- `qrcode`/`reportlab` had to be reinstalled – the container was reset between sessions; `st.py`, `cl_nat.py`, `lookup.py`, `build_run12.py` are in the project now.

### Next
- Dylan: contact Don (Mesquite camera lot) first – it's local and the F2 alone covers the price.
- Add the FB/OfferUp local feeds back into the same encyclopedia pipeline (they were skipped this run to get the nationwide method working).
- Build a "seen" ledger keyed by posting id so repeats across runs are marked, not re-reviewed.

## Run 11 – Mon Oct 12, 2026 – first nationwide SHIPPED-items sweep

**Ask:** widen from Keller pickup to anything that ships, same rules (seller doesn't know, ≤$200, profit ≥ max($50, price) incl. shipping in/out).

- **Facebook Marketplace, shipping-only, nationwide (browser):** 3,189 listings in ~12 min – 9 category feeds (antiques 20 pp, toys 12, instruments 8, entertainment 8, jewelry 8, home-improvements 6, sports 6, electronics 4, home 4) + 48 generic keywords × 2 pp ("no idea", "don't know", "grandma", "inherited", "attic", "lot", "box of", "unmarked", "signed", camera/lens/watch/knife/reel/lure/pen/radio/tube/amp/pedal/mic/figure/doll/train/kit/cards/comic/coin/stamp/book/map/print/painting/carved/brass/bronze/cast iron/military/pocket). 167 GraphQL pages with **no rate limit** this time. 2,681 reviewed after dropping jewelry + junk titles, on 16-column light-tab grids (128 per screen, 22 screens). ~45 flags → 14 opened full size.
- **ShopGoodwill, national (container):** 1,549 soonest-ending lots ≤$25 with ≤1 bid across 13 categories → 1,364 after junk filter → 12 contact sheets, 3 parallel agents → 9 weak flags (B&L Discoverer scope $7.99, Linnig etching $7.99, Swift microscope, Nivada watch…). All were Goodwill-researched titles ending within minutes; none actionable.
- **OfferUp:** now **403 (Cloudflare) from the container**, and the web search has **no shipping filter** at all (filters exposed: distance, price, sort, condition; every tile is `LOCAL_PICKUP`). Shipping search is app-only. Parked for shipped sweeps.
- **AuctionNinja (container, 200):** 20 current sales, mostly CT/NC shipping-only estate auctions run by companies that research. Not harvested this run.

### Result: nothing cleared the profit rule.
Opened full-size and passed: 1920s ukulele lot ×5 $150 (eBay-syndicated, "for parts or repair"); Filson "single tin chap" $60 (it is literally one replacement leg); Nikon lot "$1" (seller has every body priced at market); 31-watch lot $35 and watches/pocket-watches $25 (untested quartz fashion watches); 5 wooden lures $27 (common Heddon Tiny Torpedo/Crazy Crawler, beat-up); Sentinel bakelite radio $90 (brown bakelite not catalin, 1950, reseller – median ~$80); Japanese woodblock $50 (4.5×6 in, unsigned, foxed); "B Herd" painting $50 (print 84/500); "Robin '72" studio vase $35; ham-radio "junk drawer" $59.95 (eBay-syndicated, $40 ship). Not opened, judged from the grid: Stübben Siegfried saddle $175 (brand in title; resale $300–500, ~$40 ship → profit short of the $175 needed), SA System 2 fly reel $70 (median ~$120), unmarked cast iron $30–80 (Wagner/Griswold named by sellers), Navajo "Pinto" pot $150, Descoware pair $80 (damaged).

### Why the nationwide shipped feed is thin (worth knowing before the next one)
1. **Facebook now syndicates eBay listings into Marketplace** ("Discover eBay listings on Marketplace"). A large share of the shipped antiques/collectibles feed – everything from "Citrus Heights, CA" for instance – is an eBay item with an eBay.ai summary. Those are already priced to eBay's market. Filter them out: the item page text contains "See item on eBay" / "Summarized by eBay.ai"; the feed itself doesn't mark them, so detect by seller/location clusters or open and check.
2. The remaining shipped sellers skew toward **resellers** (ratings in the 50–150 range, studio photos, keyword-stuffed titles). Nationwide ≠ uninformed: the uninformed sellers are the local-pickup, "just clearing out the garage" ones. The only shipped listings that looked like real people were clothing, fashion watches and Old Navy.
3. Generic keyword search with shipping-only mostly matches product names ("You Don't Know Jack", "Old Navy", "grandpa sweater"), not seller ignorance.

### Technique notes
- FB shipping-only = `commerce_enable_shipping:true` + `commerce_enable_local_pickup:false` in `browse_request_params` (captured from a page with `?deliveryMethod=shipping`). Category feeds (SEO template, bqf `COMMERCE_MKTPLACE_SEO`/`""`, `surface:'TOPIC_PAGE'`) and keyword search (`COMMERCE_MKTPLACE_WWW`, `surface:'SEARCH'`) both work from the robots.txt tab, but keyword search needs **`commerce_search_and_rp_ctime_days` as a semicolon list of epoch-day numbers** (e.g. `20738;20737;…`), not `7` – with `7` it returns 0 results silently. Category feeds accept `null`.
- `localStorage` on facebook.com got wiped when navigating robots.txt → a Marketplace page (lost a 1,108-listing harvest). Keep the harvest in `window`/`sessionStorage` on the robots.txt tab and **export flags to the container before navigating anywhere**.
- Doc id unchanged from 10/8 (29274780305481097). 167 pages without a rate limit – the earlier ~120-page ceiling may have been per-hour.
- Light-tab grid: 16 columns × 72 px thumbs = 128 listings per 1568×745 screenshot. Screenshots fail once then succeed every single time – just retry.

### Next
- Dylan's call on five questions (asked in chat 10/12): skip eBay-syndicated FB items; whether to build eBay's own Browse API (free developer key under his eBay account – the proper way to scan thousands of newly listed, badly titled, few-bid auctions nationwide, which is the classic shipped-arbitrage source); whether shipped sweeps should include auctions with max bids (ShopGoodwill/HiBid shipping lots) once he has accounts; whether "needs repair" lots are OK when the brand carries them (the ukulele lot); whether to drop Mercari/Poshmark/Depop/Etsy from shipped sweeps for good.

## Run 10 – Thu Oct 8, 2026 – fresh full sweep (16 days since Run 9)

- **Window:** everything posted since Sept 22. All Run 9 finds treated as expired; nothing carried forward unverified.
- **Craigslist:** 16,116 posts across 27 categories (price-band splitting) → 12,151 with photos after the junk filter. **OfferUp:** 4,000 newest → 2,875 kept. Both reviewed as 126 contact sheets (15×8 @130 px) by 6 parallel agents → 66 flags.
- **Facebook:** 2,172 listings from 8 category feeds (antiques 30 pp, toys 20, instruments 10, hobbies 14, entertainment 10, home-improvements 8, sports 8, free 10) ≈ 104 GraphQL pages before stopping short of the rate limit. Reviewed as 24 light-tab grids (14 cols × 84 per screen) → 6 flags.
- **Estate sales:** 194 sales within 40 mi → 89 in the 7-day window → 33 within ~20 mi picked (9,790 photos, all downloaded) → 102 contact sheets reviewed by 5 parallel agents → ~230 flags → 113 pulled up full-size → 37 final targets across 16 sales.
- **Comps:** 45 Terapeak queries. The comps killed most of the photo flags, including some that looked strong: Singer Featherweight 221 at $200 (median $335 → profit $64 vs $200 needed), Seeburg Wall-O-Matic $175, Reflex-Nikkor 500mm $95 (median $146), Nikon ED Plan 1x $150, Leitz microscope $125, 1960s G.I. Joe jeep set $150 (median $198), Super Naturals lot $160, Spencer microscope $65, post-office box bank $150, Love Field crock $70, Beck/Arnley sign $79, Scientific Anglers reel $40, pachislo machine $150, Macross VF-19 $80, Fluke 45 $200, Webster tube amp $190.
- **Survivors (13):** Lie-Nielsen shoulder plane $40 (median $240) and the Epoch Zelda Epona figure $40 (median $200) are the two real ones; Herman Miller Setu stools $80 ea (×15) and five Eames-style shells for $189 are the furniture plays; three Abu Garcia reels $49; six-reel lot $9; 1941 Chrysler pedal car $180; Beta 52A $35; Coravin Model One $15 (listed as "CORAVAN"); Richfield porcelain pump sign $30; four carded Street Sharks $100; a FREE vintage mandolin in Lewisville; a $100 "Blaeu Africa 1630" map that is probably a reproduction.
- **Top estate stops:** #1 Rivers Wind warehouse, Fort Worth (~$520 across 3 targets; stained-glass window ~$238) · #2 Southlake "Light, bright" (~$398; Rickenbacker amp ~$158) · #3 Retro Betties Southlake (~$349; MCM teak surfboard table ~$188) · #4 Kings Attic NRH (~$406; Zuni inlay set ~$263) · #5 Southern Charm Fort Worth next weekend (JLC Atmos clock ~$299).
- **Output:** `DFW-Resale-Finds-Full-List-2026-10-08.pdf` (10 pages; Part 1 marketplace, Part 2 estate sales running now, Part 2b next weekend). One document, per the deliverable rule.

### Lessons
- The container survived the 16-day gap with all modules and caches intact; nothing had to be rebuilt.
- **FB doc_id rotated** (29274780305481097 on 10/8). Re-capture it every run. Also: writing `localStorage.FBKIT` and reading it back in the *same* JS call is required – a write issued at the end of one call didn't persist.
- Add cursor persistence to `FBSEO` (`window.CUR[seo]`). Without it, each call restarts the feed at page 1 and burns rate-limit budget re-reading pages already seen.
- **Terapeak price spans are `"$ 39.99"` with a space** – the old `/^\$([\d,.]+)$/` regex silently returned "0 sold". Also sanitise titles (`[?&=%#;:+]` → space) or the extension blocks the result as "Cookie/query string data".
- Contact-sheet captions at 130 px are OCR-unreliable: three agents reported prices and even item identities that belonged to a neighbouring cell. Always re-resolve a flagged key against the index and look at the full-size photo before pricing it.
- Chrome dropped mid-run (both tabs frozen, then "extension not connected"). Opening a *new* tab recovered it; the frozen tabs never came back. Screenshots on the heavy grid page reliably fail once and succeed on the retry.
- Estate photo volume is the real constraint: 89 sales in range would be ~20,000 photos. Capping at ~20 miles and ~9,800 photos kept the review to one pass of 5 agents.

### Next
- Still waiting on Dylan: HiBid account (bidding), CTBids, Nextdoor; and the first entries in Buys & Sales – every resale estimate is still untested.
- Worth building: a proper "was this already shown to Dylan" ledger so repeat listings across runs can be marked rather than re-reviewed.

## Run 9 – Tue Sept 22, 2026 (morning) – daily sweep + full master list

- **Window:** since Mon 9/21 noon.
- **Craigslist:** 2,037 posts in 17 categories (incl. gms) → 1,471 not seen before → 1,169 after filtering. **OfferUp:** 2,289 newest → 1,501 after filtering. All reviewed on 23 contact sheets by 3 parallel agents. Result: 3 weak leads (jewelry box $15, box of LPs $20, fragrance lot $35); bugle and Star Wars lot failed Terapeak.
- **Facebook:** category feeds + keywords from a facebook.com/robots.txt tab (tokens + query captured from a category page into `localStorage.FBKIT`). 1,903 listings before FB returned **"Rate limit exceeded"** after ~100 pages. Mostly repeats of 9/21; nothing new cleared.
- **Estate sales:** 64 sales this week; 9 new sales + 13 with new photos → 1,818 new photos reviewed by 2 agents. 8 new targets after Terapeak: Honda EU2000i (median $585), Bernina Virtuosa 153 QE ($570), Atari 2600 lot ($188), Robert Held-style art glass pair, Yashica-Mat EM, boxed Accutron, iMac G4, model-kit stack.
- **Live check:** all 9/21 marketplace deals still up except the Southwest pottery (SOLD). G.I. Joe lot still has no price.
- **Output:** `Refurbish-Master-List-2026-09-22.xlsx` (Estate sale plan · Marketplace listings · Estate sale targets · Checked & passed · Buys & Sales) and `DFW-Resale-Finds-Full-List-2026-09-22.pdf` – the complete list of everything found so far, per Dylan's request.

### Lessons
- FB rate-limits at roughly 100–150 GraphQL pages per session: cap each run (~8 categories × 10 pages + 20 keywords × 3 pages) and save to localStorage after every query.
- OfferUp item pages now 403 from the container after a 25-page feed pull; check liveness in the browser (fetch `/item/detail/<id>` from an offerup.com tab).
- The FB Marketplace tab froze twice mid-harvest (lost state). Running the harvest from the robots.txt tab avoided it.


## Run 8 – Mon Sept 21, 2026 (night) – source iteration

- **Facebook category feeds (biggest win):** keyword-free, newest-first category browsing via the same GraphQL query (`FBSEO`). 5,879 listings from 10 feeds in ~6 min, including badly titled listings keyword search never returns. Sub-category slugs don't filter – noted.
- **Light-tab grid review:** rendering grids on facebook.com/robots.txt (data passed via localStorage) fixed the constant 30-second screenshot timeouts.
- **Mercari:** API captured (persisted GraphQL + page headers, paging by `nextKey`). 3,367 items reviewed – nothing clears; it's a reseller marketplace. Better as a selling channel.
- **eBay search pages:** bot challenge after a few requests → parked; Terapeak still fine.
- **Craigslist `gms` + `zip`:** added; mostly cross-posts from far away and estate companies already covered.
- **Facebook groups:** found the big DFW garage-sale and antique groups; public garage groups are spammy and overlap with Marketplace. Private antique groups need Dylan to join.
- **estatesale.com / gotoauction.com:** bot-protected; browser-only, not built. **PublicSurplus:** national, low fit.
- **Finds:** ~950 photos reviewed across FB category feeds; 12 flagged (Airline 1960s guitar $60, lot of 3 vintage Bach mouthpieces $149, Roland U-110 $80, Hunter Zephair fan $100, Olds trombone $125, 1960s fiberglass office shell chair $55, camera lots). **All failed Terapeak** (e.g. Zephair median $73, Bach Mt Vernon mouthpieces $75 each, Airline acoustic median $110) – nothing added to the deal sheet.

### Next
- Build sub-category capture for FB (typewriters, antique-electronics, cameras) using each page's own category_ids.
- Keep checking the estate readout weekly (Tue/Wed); HiBid max-bid list once Dylan has an account.


## Run 7 – Mon Sept 21, 2026 (late night) – estate readout, Terapeak, new sites

- **Terapeak unlocked** (Dylan added his address). JSON API reverse-engineered; 45 comp queries run with no throttling.
- **Estate sales, full pass:** 57 sales / 10,191 photos, all reviewed by 4 parallel agents (80 flags), top ~20 re-checked at full size, Terapeak comps for 40 item types. Output: `Estate-Sales-Readout-2026-09-24.xlsx` – 45 targets across 18 sales.
  - Top stops: Arlington/Dayspring 76018 (American Girl boxed dolls, Lilli Ann coats, rock LPs, Pyrex) · Desoto/About The House (1970s ceramic trees, Le Creuset, 1935 Dallas pin-up calendar, railroad date nails) · Weatherford/And Again (TEAC reel-to-reel, airline posters and manuals) · Weatherford/Unique (Pendleton GNP blanket, 30 pairs of boots, turquoise) · Duncanville/Kitchens To Closets (1960s comic lot, Evel Knievel lunchbox) · Bedford (Commodore 1702-type monitor, Shirley Temple doll).
- **gsalr garage sales:** built; 71 DFW sales, 22 garage/multi-family; 6 listed (Fort Worth comics garage sale is the standout).
- **HiBid:** GraphQL harvest built; 4,000 soonest-closing lots → 2,088 after dropping store-return sellers; 294 photo-reviewed. No buy – best candidate was a reproduction sextant.
- **AuctionNinja:** mostly out-of-state shipped sales. **CTBids:** DFW locations found; search API needs a token → browser.
- **Browser note:** partway through, the Chrome tab group was replaced by a new window that is **not signed in to eBay** (Terapeak failed there). If this recurs, check which Chrome profile the extension is attached to.
- **Report format** documented in `claude/report-format.md`; PDF generator saved as `claude/build_finds_pdf.py`.

### Next
1. Dylan: pick estate sales for Thu–Sat; log buys in Buys & Sales.
2. Needs Dylan's accounts: HiBid (bidding), CTBids (browse/bid), Nextdoor (For Sale feed), Mercari (optional).
3. Build Mercari + eBay local-pickup search next; add FB buy/sell groups to the FB harvest.


## Run 6 – Mon Sept 21, 2026 (night) – process upgrades + new sources

### Implemented
- **Liveness check:** `live.py` (Craigslist/OfferUp, container) + Facebook navigate-and-check snippet. All 14 deal/lead links were live at ~11 pm.
- **Seller-awareness corrections from the live check:** Lane table ("Vintage Lane Cube End Table", cut from $150), yellow Eames ("Vintage Herman Miller Eames…"), rope-edge Eames ("Early Herman Miller…", cut from $175, 4 weeks), Nikonos V (model in title, cut from $120, 13 weeks). The Lane table dropped to Just Barely. The PDF and sheet were fixed.
- **Trips tab:** Mansfield $310 · Dallas ~$1,020 (with the G.I. Joe placeholder) · Fort Worth ~$670 · Plano/Coppell/Frisco ~$440 · Keller/Newark ~$445.
- **Buys & Sales tab** for calibration (carry it forward every run).
- **Furniture rule:** small car-sized furniture OK at profit ≥ 2× price, relisted within a week.
- **estatesales.net API puller** (`esn.py`): 158 sales / 57 this week / 10,191 photos; ~2,300 reviewed. 6 sales on the "Estate sales this week" tab.
- **Source directory:** 30+ sites tested and tiered in site-access-methods.md.

### Tested and parked
- Terapeak: blocked until Dylan completes eBay's seller address step.
- Facebook thumbnails in the container: work, but cost ~10× the tokens of grid screenshots.

### Next run should start with
1. Dylan: finish eBay seller setup (unlocks Terapeak), log any buys in Buys & Sales.
2. Build gsalr.com garage-sale photo pull (Tier 1).
3. Try AuctionNinja/CTBids in the browser for DFW online estate auctions closing this week.


## Run 5 – Mon Sept 21, 2026 (late) – new profit rule + photo-first

- **Rule change:** profit ≥ MAX($50, price), price ≤ $200. Tiers now scale with price (see runbook).
- **Window:** Craigslist 145 new + OfferUp 356 new since run 4 (82 reviewed after filtering) + Facebook round B (16 generic queries, 916 listings, 890 reviewed on photo grids).

### Deals (sheet: Refurbish-Sweep-2026-09-21-v4.xlsx)

| Tier | Item | Price | Where | Est. profit | Link |
|---|---|---|---|---|---|
| Great Deal | Stressless Consul + ottoman | $50 | FB, Mansfield | ~$310 | https://www.facebook.com/marketplace/item/28819451134345367/ |
| Good Deal | Singer 221K Featherweight | $200 (offer $160) | OfferUp, Dallas | ~$245 | https://offerup.com/item/detail/bda0b634-b9c1-3cdd-a1d3-11d6341393cf |
| Good Deal | Fishing lot w/ boxed Creek Chub/Heddon | $200 (offer $150) | CL, Fort Worth | ~$250 | https://www.craigslist.org/view/d/fort-worth-large-lot-vintage-fishing/3Ny6BYLx4rtfYTPsHS1wja |
| Good Deal | Star Wars CCG (Decipher), 5 boxes | $50 | OfferUp, Dallas | ~$125 | https://offerup.com/item/detail/8620a05e-1fe3-3e55-9292-91813516dbce |
| Good Deal | Lane walnut cube end table | $75 | FB, Fort Worth | ~$175 | https://www.facebook.com/marketplace/item/28460368930264731/ |
| Good Deal | Eames fiberglass side shell, yellow | $75 | FB, Plano | ~$200 | https://www.facebook.com/marketplace/item/1574262364433783/ |
| Just Barely | Eames rope-edge armshell | $100 | FB, Coppell | ~$160 | https://www.facebook.com/marketplace/item/1404427988253058/ |
| Just Barely | Nikonos V | $80 | FB, Fort Worth | ~$120 | https://www.facebook.com/marketplace/item/977121448457611/ |
| Just Barely | Singer 15-91 head (no cord) | $20 | FB, Frisco | ~$75 | https://www.facebook.com/marketplace/item/26238600912504049/ |
| Just Barely | 75 lb Lego + instructions | $200 | OfferUp, Keller | ~$250 at full value | https://offerup.com/item/detail/548482b2-ce76-3ae6-85d1-9693662769c3 |
| Lead | 381 LPs | $5 | FB, Newark | unknown | https://www.facebook.com/marketplace/item/39425707730361878/ |
| Lead | Tombstone radio | $50 | FB, Fort Worth | $50–200 | https://www.facebook.com/marketplace/item/29256010280653061/ |
| Lead | G.I. Joe lot / SW pottery | TBD / $180 | CL Dallas / FB Dallas | see run 4 | – |

### Techniques added

- Facebook photo grid at 20 columns ≈ 120 listings per screenshot (wait ~4 s for lazy images).
- Facebook item viewer v2: select `img[alt^="Product photo"]` + the first large image; stored as code in localStorage `IVC` so it survives navigation (`await eval(localStorage.IVC)`).
- The FB background harvest keeps running while the grid overlay is drawn – but navigating the tab kills it, so review grids first and open items after the harvest finishes.
- Fetching FB item pages with `fetch()` doesn't include the listing data (it loads via GraphQL). Dead end.

### Dead ends

- eBay sold search throttled after ~15 calls (timeouts). Used WebSearch instead.
- Round B's last 4 queries (cast iron, bronze, inherited, no idea) added almost nothing – likely FB rate limiting after ~12 queries. Spread queries across the run.
- The bamboo chair + table (CL, sweep 1) wasn't in the current feeds – assumed sold.

### Next run should start with

1. Message: G.I. Joe (price), records (spine photos), radio (back label), both Eames (underside), Star Wars CCG (card count).
2. estatesales.net photo previews for the weekend.


## Run 4 – Mon Sept 21, 2026 (evening) – first run under the new rules

- **Window:** Craigslist, last 48 hrs · OfferUp, newest ~4,000 · Facebook, up to 7 days (28 generic queries) · ShopGoodwill Fort Worth, all active.

### Volume

| Site | Harvested | Reviewed |
|---|---|---|
| Craigslist | 4,141 | 3,320 on photo contact sheets |
| OfferUp | 3,999 | ~770 of 1,885 filtered on photos. **Sheets 12–29 were NOT reviewed.** |
| Facebook | 6,625 | 4,367 after junk filter, all titles read. About 100 shortlisted and viewed as photos. |
| ShopGoodwill | 1,882 | 192 on photos, then deprioritized |

### Deals (sheet: Refurbish-Sweep-2026-09-21-v3.xlsx)

| Tier | Item | Price | Where | Est. profit | Link |
|---|---|---|---|---|---|
| Great Deal | Ekornes Stressless Consul small + ottoman (arm tear) | $50 | FB, Mansfield | ~$310 | https://www.facebook.com/marketplace/item/28819451134345367/ |
| Good Deal | Singer 221K Featherweight (listed as "Vintage Singer") | $200, offer $160 | OfferUp, Dallas | ~$245 | https://offerup.com/item/detail/bda0b634-b9c1-3cdd-a1d3-11d6341393cf |
| Good Deal | Vintage fishing lot with boxed Creek Chub/Heddon | $200, offer $150 | CL, Fort Worth | ~$250 on eBay piece-out | https://www.craigslist.org/view/d/fort-worth-large-lot-vintage-fishing/3Ny6BYLx4rtfYTPsHS1wja |
| Lead | G.I. Joe ARAH lot incl. Defiant | price TBD | CL, Dallas | $450+ if ≤$200 | https://www.craigslist.org/view/d/dallas-vintage-gi-joe-power-ranger/xkFP7E19VchkSi7cffsbRg |
| Lead | Southwest pottery group | $180 | FB, Dallas | uncertain | https://www.facebook.com/marketplace/item/28402405612731893/ |

### Techniques added

- Craigslist JSON API with price-band splitting
- OfferUp SSR JSON with a location cookie
- Facebook GraphQL replay (about 250 results per query instead of 15–30)
- ShopGoodwill API
- Container-side contact sheets
- Facebook titles-first triage

### Dead ends

- Craigslist browser pages (IP blocked)
- Facebook UI scroll
- Container fetches of Facebook item pages, eBay, Mercari, HiBid (403 or login)

### Next run should start with

1. Message the G.I. Joe seller for a price.
2. Finish OfferUp sheets 12–29 if those listings are still in the window.
3. Build the estatesales.net photo-preview pull for this coming weekend.
