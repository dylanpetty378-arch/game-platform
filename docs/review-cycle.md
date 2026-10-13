# Review cycle — what a scheduled (unattended) Claude session does every run

This is the Stage-2/3 step that needs judgment (looking at photos, pricing). The cloud workflow and the Lens worker do
everything else. A scheduled task runs this every 6 hours; any Claude session can run it by hand ("run the Refurbish
review cycle"). Follow it exactly; log everything; message Dylan only about real finds or real breakage.

## 0. Setup (2 min)
- Repo: `add_repo` dylanpetty378-arch/game-platform (push), then
  `git clone --depth 200 -b refurbish https://github.com/dylanpetty378-arch/game-platform /home/claude/refurbish && cd /home/claude/refurbish`
- `pip install --break-system-packages -q qrcode pillow reportlab` if missing. Read `docs/START-HERE.md` (rules) once.

## 1. Health check (each step of the machine) — fix before reviewing
Run `python3 scripts/health.py` (prints a pass/fail table and writes nothing). It checks:
1. Cloud workflow: last runs succeeded; last harvest < 6 h old; failed requests < 5%; 0 "still capped".
2. Queue: `q/current/meta.json` < 6 h old; ≥ 500 pending.
3. Lens worker: newest `lens` row < 2 h old (Dylan's Chrome may be closed overnight — then just note it);
   read quality of the last 200 rows (share with priced matches ≥ 80%, empty ≤ 5%, `q.v` = current WORKER_VERSION).
4. Database: no unparseable lines; inbox empty after the last cycle.
If something fails, fix it (code in `scripts/`), push, re-run the workflow (`gh api -X POST
repos/dylanpetty378-arch/game-platform/actions/workflows/refurbish-cycle.yml/dispatches -f ref=main -f
'inputs[no_harvest]=true'`), log the fix in `docs/improvements.md`. If it needs Dylan (Chrome closed for > 24 h, token
expired = upload HTTP 401 in the worker log), send ONE short message saying exactly what to do.

## 2. Triage everything newly flagged
`python3 scripts/db.py worklist flagged` (or the SQL in `scripts/review_helpers.py --flagged`). For each:
- Read title, price, area, Lens `best`, `med`, `ratio`, `ai`, `ai_value`.
- Kill at once (event `photo_review/kill`, one-line reason, `--type` slug): furniture (unless the profit could be
  ≥ $750), bulky/fragile low-value, untested/broken electronics, needs authentication, obvious reproductions, Lens
  category matches with nothing specific in the photos.
- Shortlist the rest (usually 5–15%).

## 3. Photo review the shortlist
`python3 scripts/lens_export.py --photos shortlist.json sheets/` → Read each sheet. Also fetch each listing's body
(`python3 scripts/review_helpers.py --body <url>`): it often changes the verdict (per-item pricing, "local cash only",
"runs then stops"). Identify the maker/model/type; read the encyclopedia entry; kill or keep with events.

## 4. Sold comps (Terapeak) for keepers
If Claude in Chrome is available and eBay is signed in: open `https://www.ebay.com/sh/research`, paste the TPR/COMP
helper from `docs/history/site-access-methods.md` (also in `scripts/review_helpers.py --terapeak-js`), run all queries
in one call, render to the page, read with get_page_text. Otherwise use web search for sold prices (mark comps
`source=web`, lower confidence). Log `db.py comp` and `db.py search` for every query.
Apply the rule: profit = median × 0.87 − ship to buyer − ship to Dylan − price; pass if profit ≥ max(50, price).
Tier A ≥ 2× price, B passes, C needs an answer/offer. Event `decided` with `data` {price, est_resale, profit, tier}.

## 5. Learn
- Encyclopedia entry for every new type (docs/encyclopedia, README format); `db.py itemtype`.
- Anything that would have made this faster/better → `docs/improvements.md`; small safe fixes → do them now.

## 6. Report
- Commit + push data/doc changes only (`db/`, `docs/`, `scripts/`) — never `q/`, `STATUS.md`, `status.json` (the bot
  owns generated files); then dispatch the workflow with no_harvest so STATUS.md updates.
- If there are new Tier A/B finds: build the printable report (`scripts/build_report.py`, spec in /tmp — seller
  contacts never in the repo), send it to Dylan (SendUserFile) with one line per find. No finds → no message.
- Never contact sellers. Never buy. Drafted messages only.
