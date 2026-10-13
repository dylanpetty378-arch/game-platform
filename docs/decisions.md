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
