# Decisions — what was chosen, what was rejected, and why

Newest first. When you change an approach, add an entry here with the evidence.

## 2026-10-12 — Database: append-only JSONL in this git branch (+ SQLite on demand)
Considered: (a) SQLite file in git, (b) hosted DB (Firebase/Supabase/Turso), (c) Google Sheet via Apps Script,
(d) JSONL in git.
- (a) binary file: two sessions writing = unmergeable conflicts; no history per row.
- (b) best for live writes from the browser, but needs an account and a secret; a secret can't live in a public repo
  and Claude can't create accounts. Every Claude surface reaches GitHub; not all reach a custom DB.
- (c) workable sink for the browser, but another account dependency and awkward to query.
- (d) **chosen**: readable from anywhere by URL, writable by any session with the repo, merges cleanly with git's
  `merge=union` driver (.gitattributes — plain append-only lines DO conflict without it; learned on the first cloud run),
  full history in git, free, no limits that matter. SQLite built on demand gives real SQL. Mutable state is events.
- Not stored: the full raw harvest (~260 K listings per 48 h ≈ 100 MB/run would bloat git by GBs/year). Only queued
  listings + per-category counts. Revisit if price-history-of-everything becomes a goal (then: compressed monthly
  Parquet in a release asset, not git).

## 2026-10-12 — Always-on cloud worker: GitHub Actions on the public game-platform repo
Considered: GitHub Actions; Dylan's Mac (launchd/cron); paid VPS/cloud functions; claude.ai scheduled tasks.
- Actions: free on public repos with no minute cap (docs.github.com "About billing for GitHub Actions"); 6 h job
  limit (a cycle takes ~15 min); scheduled workflows run only from the default branch (so the yml is on `main`) and
  are disabled after 60 days without repo activity (the bot's own commits keep it active). **Chosen.**
- Mac: free but only while the laptop is awake; Craigslist harvest doesn't need the Mac.
- Paid hosting: rejected — Dylan wants free/no-limit.
- Scheduled Claude tasks: Dylan said they haven't worked well for him; also burns usage.
- Craigslist sapi from Actions IPs: verify on the first runs (it worked from the Anthropic container).

## 2026-10-12 — Lens runs in Dylan's Chrome via a Tampermonkey userscript, one fresh page per item
- Google blocks Lens from headless/datacenter browsers (tested Oct 12; "unusual traffic"), so it must be a real browser.
- The first loop (hidden iframe on a google.com/robots.txt tab, pasted by Claude) leaked memory: ~2 GB JS heap after
  ~90 items, stopped by its own watchdog, and needed Claude to restart it. Dylan: "the memory cannot be an issue —
  this truly needs to run in the background."
- **Chosen:** the worker tab navigates itself to each Lens result as a new page (the browser frees the old page
  entirely); a userscript survives the navigations, saves after every item, uploads every 25. No Claude needed.
- Rejected: reloading the iframe tab periodically (still needs something to re-inject code after reload → the
  userscript anyway); a custom Chrome extension (more setup for Dylan, same result); performance.memory as the
  guard (it's cached/bucketed — measured 1,969 MB before and after a full navigation; real Chrome total was 1.6 GB).

## 2026-10-12 — Public repo for project data (owner's call)
The safety layer refused committing project data into the public game-platform repo; Dylan overrode it ("you could
post into the public repo before, so you can do so now"). Mitigation: nothing personal goes in — no family names,
emails, phone numbers, addresses, seller contact details, household items. History docs were copied with those
redacted. The raw.githubusercontent URLs are public but unadvertised ("hidden" by obscurity only).

## Earlier
See `docs/history/valuation-method.md` (why Lens-first beat thumbnail review: 22/30 identified vs coarse type only),
`docs/history/site-access-methods.md` (which sites work from where), `docs/history/sweep-log.md` (every run).

## 2026-10-12 (night) — size rule, deep research, one working chat
- Dylan: only items that fit in a passenger seat (a little bigger at most); anything bigger is a waste of time. Hard
  exclusion in scoring (`BULKY` minus `SMALL` exemptions such as doll trunk, hand mirror, bench vise), filtered out of
  existing queues, extra CLIP negatives for furniture-like photos.
- Dylan: spend more time on each item that passes the size rule — research the type (makers, marks, finishes,
  quality, nuances, sold prices) and write it into the encyclopedia, including for items we pass on. Research every item
  already scanned too. For anything bought/sold, keep a full item dossier (docs/items/) he can quote to buyers.
- Dylan: no separate scheduled Claude sessions changing code (they could overwrite each other). One working chat does
  all iterations; the 6-hourly scheduled review task was deleted. The cloud workflow + Lens worker keep running.

## 2026-10-13 — No device dependency
Dylan: the system must run on any device and without his laptop open. Decision:
- The cloud is the backbone: GitHub Actions for harvest and API comps, one Claude cloud scheduled task for review,
  and git for the database.
- His Chrome (Lens, Terapeak) becomes an optional accelerator.
- Sold data without a browser: the eBay developer APIs. The Browse API (active listings) is available to every free
  developer account. The Marketplace Insights API (sold, 90 days) needs eBay's approval, which Dylan applies for.
  Scraping eBay from the cloud was rejected because of bot checks and ToS.
- Dylan approved an automated job on his eBay account. Done through the official API, it needs no laptop at all.
- Triage without Lens: `review_helpers.py --unlensed`. Measured on Oct 13: Lens flags gave 0 keepers; reading the
  listings found the leads.
- The send_later check-in chain is retired. It was bound to the Mac, so it stalled when the Mac was closed.

## 2026-10-13 — Lens's role, and why Refurbish doesn't live in Vectus
- **Lens's role (Dylan's framing):** Lens is the identifier. It turns a photo into a description of what the item
  really is. Claude takes that description, researches what the public sells it for, and compares that with what the
  seller says and asks. The gap is the deal. Lens was never meant to price anything. What failed was our use of Lens's
  match-price ratio as a filter. The Lens AI identification text stays a core input to triage. Where no browser is
  available, Claude identifies from the photo itself (`--unlensed`), which fills the same role.
- **Only Claude sleuths.** It may run only while Claude is active, but it must start from any device: any chat via
  docs/device-free.md, or the cloud scheduled task.
- **Vectus checked.** It is Dylan's tabletop RPG platform: a Postgres (Neon) database with game tables (identity,
  campaigns, records, characters, assets), on Fly.io, auto-deployed on every push to main, with strict corpus and
  vocabulary rules. It has no harvesting, comps or resale code, and adding resale tables would break its own rules
  and risk the live playtest. Refurbish stays in game-platform/refurbish: git JSONL plus SQLite on demand, free, and
  already running. The eBay keys go in game-platform's Actions secrets.

## 2026-10-13 — No generalization
Dylan: "no generalization about items. They are each unique. We need to know specific brands and specific ways that
items are more valuable than items that are similar to them. That's where the money is going to come from." Applied:
- Triage verdicts (ask/buy) must name the exact maker/model/variant/mark and the specific tell; a type-level price
  range is not a verdict (research/TRIAGE_BRIEF.md).
- Every encyclopedia entry gets `### Golden-egg tells`: the specific variants worth multiples, with the multiple and
  how to see it in a photo (briefs + encyclopedia/README.md). `enc.py lint` flags entries without it.

## 2026-10-13 — Two restrictions loosened (Dylan)
- Electronics the seller says are tested/working are allowed, but only when profit ≥ 3× price. Untested stays out.
- A $200–$500 price tier is allowed, but only when profit ≥ 10× price. The harvest now pulls up to $500.
