# Lens worker (the part that runs in Dylan's Chrome)

Google blocks Lens from servers/headless browsers ("unusual traffic"), so photo identification has to run in a real,
signed-in browser. That is the only piece not in the cloud.

## Current method: Tampermonkey userscript `scripts/refurbish-lens.user.js` (v1.0, Oct 12 2026)

- Control page: **https://www.google.com/robots.txt?refurb** (status, Start/Stop, token box, log).
- Start marks that one tab as the worker (sessionStorage). The tab then *navigates itself*:
  `lens.google.com/uploadbyurl?url=<photo>` → Google redirects to `www.google.com/search?…udm=26` → the script waits
  for "Visual matches" (≤22 s), parses, saves the result to Tampermonkey storage, waits 2.5–4 s, goes to the next.
- **Memory:** every listing is a new top-level page, so the previous page is freed completely. (The older in-page
  iframe loop leaked ~20 MB per item and had to stop at ~90 items.)
- **Durability:** result saved after every item; uploaded every 25 to `db/inbox/` with the GitHub token; the push
  triggers the cloud workflow, which ingests them within minutes. If the browser crashes, nothing saved is lost.
- **Queue:** when empty it fetches `q/current/queue.txt`; if nothing new it idles on the control page and checks every
  20 min. Already-done pids are skipped (local DONE set, plus the cloud never re-queues a lensed listing).
- **Rate limits:** a `/sorry/` page = blocked → wait 3 min. 7 blocks in an hour → pause 1 hour. 2-minute break every
  200 items. Throughput ≈ 10–12 items/minute.
- Only the worker tab is affected; Dylan's own Google/Lens use in other tabs is ignored.

### Setup (Dylan, once per computer)
1. Chrome Web Store → Tampermonkey → Add. `chrome://extensions` → Tampermonkey → Details → **Allow User Scripts** on.
2. Open the raw URL of `scripts/refurbish-lens.user.js` → Install. (Updates come from the same URL automatically.)
3. github.com/settings/personal-access-tokens/new → only `game-platform` → Contents: Read and write → copy.
4. Open the control page, paste the token, Save token, **Start in this tab**. Leave the tab open (background is fine).

Claude must never type the token itself — Dylan pastes it.

### Checking it from a Claude session
- With Chrome tools: read the control page text (`get_page_text` on the robots.txt?refurb tab). Do not press Start in a
  second tab (two workers double the rate and risk a Google block).
- Without Chrome: `STATUS.md` → lens count and newest `lensworker-*` run; `git log --oneline -5 -- db/inbox` on the branch.
- No token? Results pile up in the browser. Export: open `…/robots.txt?refurb&dump`, `get_page_text`, copy between
  EXPORT_START/END into a file, `python3 scripts/cloud_cycle.py --no-harvest` after putting it in `db/inbox/`, then
  open `…/robots.txt?refurb&clearbuf=<count>` to drop the exported ones.

### Real memory check (macOS)
`performance.memory` in the page is cached/bucketed and NOT reliable. Measure Chrome's real usage on the Mac with the
osascript tool: `do shell script "ps -axo rss,command | grep 'Chrome Helper (Renderer)' | grep -v grep | awk '{s+=$1} END {print s/1024 \" MB\"}'"`.
Baseline Oct 12: 18 renderers, 1.6 GB total, 49% of 8 GB free.

## Fallback: `scripts/lens_gentle.js` (v7) pasted by a Claude session
Same parsing and flag rule, runs in a hidden iframe on a robots.txt tab, needs a Claude session to paste/restart it and
to reload the tab every ~40 items (leak). Use only if Tampermonkey is unavailable. Start/resume lines are at the bottom
of the file.

## Flag rule (both workers)
`med` = median price of matches on second-hand/collector sites (eBay, Etsy, Chairish, 1stDibs, WorthPoint,
LiveAuctioneers, Invaluable, Reverb, Discogs, …; Craigslist and retail ignored). Flag if **any**:
ratio med/price ≥ 2.5 with ≥2 priced matches and med ≥ $60 · a collector/auction site matched and med is missing or
≥ $80 · the AI overview states a value ≥ $100. Expect ~35–45% flagged; the photo review is the real filter.
