# Lens pipeline runbook — find mis-priced listings anywhere in the US from their photos

**Who this is for:** any Claude session (any model size) that opens the Refurbish project and is asked to "run a sweep", "find golden geese", "find things sellers don't know the value of", or anything similar. Follow it top to bottom. Every step says exactly what to run, what you should see, and what to do if you don't see it. Do not improvise a different method unless Dylan asks — the alternatives were tested (see `claude/valuation-method.md`) and this one won.

**What it does in one sentence:** pull every cheap owner listing in the country → have Google Lens identify each photo → keep the ones where the match prices are far above the asking price → check sold prices → apply Dylan's rule → print a PDF.

**Dylan's rule (never change it):** buy price ≤ $200; expected profit after ~13% selling fees and shipping both ways must be ≥ the larger of $50 and the buy price. No repairs, no untested electronics, nothing that needs authentication (designer bags, signed sports items, precious-metal content you can't verify). Never search by brand name — the point is to find things the *seller* didn't identify. Contact sellers only through the site's own reply method; any email goes from [owner personal Gmail]; never send a message without Dylan's explicit OK for that specific message.

---

## 0. Before you start — the pieces

| Piece | Where | What it is |
|---|---|---|
| `cl_nat.py` | `claude/cl_nat.py` in the project; copy to `/home/claude/sweep/` | Harvests every Craigslist post with photos from 413 US areas via the sapi JSON API. Needs `areas.json` next to it (download from `https://reference.craigslist.org/Areas` as JSON if missing). |
| `lens_prep.py` | `claude/lens_prep.py` | Scores the harvest for "seller probably doesn't know what this is", keeps the top N, writes the queue strings. |
| `lens_gentle.js` | `claude/lens_gentle.js` | The code that runs inside Dylan's Chrome and drives Google Lens. Paste it with the Chrome `javascript_tool`. |
| `lens_export.py` | `claude/lens_export.py` | Joins the flagged results back to the listings, prints the Stage-2 worklist, builds photo sheets. |
| `st.py` | `claude/st.py` | Helpers (`sheet()` builds contact sheets; needs `pip install pillow --break-system-packages`). |
| `lookup.py` | `claude/lookup.py` | Prints a listing's title/price/area/URL/body from a list file. |
| Encyclopedia | `encyclopedia/*.md` in the project | What we already know about each item type. Read the matching entry during Stage 2; write a new one for every type you research. |
| Report builder | `claude/build_run12.py` + `claude/report-format.md` | Makes the printable PDF with QR codes. |

Chrome: Dylan's Chrome must be open with the Claude extension (the `mcp__claude-in-chrome__*` tools). Load them once: `ToolSearch` → `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__get_page_text`. If those tools are absent, Chrome is not connected: tell Dylan "I need Chrome open with the Claude extension to run Lens" and stop at Step 2.

Why Chrome and not the container: Google blocks Lens from datacenters/headless browsers ("unusual traffic"). It only works from a real signed-in browser. This was tested; don't retry it from the container.

---

## 1. Harvest (container, ~10 minutes)

```
mkdir -p /home/claude/sweep && cd /home/claude/sweep
python3 cl_nat.py ata,cba,clt,ele,emd,hab,hsh,jwa,mus,pha,spo,sys,tls,tag,vga,bik,bop,boo,clo,mob,mpo,rvs,wan,for,hsd,gms,art,fua,atq 24
```
- First argument = Craigslist category codes (`ata` antiques, `cba` collectibles, `clt` clothing, `ele` electronics, `jwa` jewelry, `mus` instruments, `pha` photo/video, `spo` sporting, `tls` tools, `vga` video gaming, `art`, `fua` furniture, `atq`… — this list is the standard set; use it as-is).
- Second argument = hours back (24 for a daily run).
- Output: `cl_nat_<timestamp>.json`, a list of records `{pid, posted, price, title, imgs:[imageId,…], slug, uuid, area, region, cat}`. Expect ~80,000 records for 24 h. If you get under 20,000, the API is down or `areas.json` is missing — check the printed progress.
- Listing URL = `https://www.craigslist.org/view/d/<slug>/<uuid>`. Photo URL = `https://images.craigslist.org/<imageId>_600x450.jpg` (or `_1200x900.jpg` for full size).

## 2. Prioritise and build the queue (container, 1 minute)

```
python3 lens_prep.py cl_nat_<timestamp>.json 2000 lens_ledger.json
```
- Keeps the 2,000 listings most likely to be mis-described. The scoring is in the file; in words: short generic titles, "estate / grandma's / moving / box of / old / not sure" language, price $10–100 and 3+ photos score up; model numbers and reseller words (authentic, rare, mint, NIB, retails, OBO, lot of 12) score down; junk categories (firewood, tires, mattresses, pets, services, "wanted", "free") are dropped.
- `lens_ledger.json` remembers which pids have already been through Lens so a repeat run on the next day's harvest skips them. Always pass it.
- Outputs `lens_pri.json` (full records, in queue order) and `pri0.txt`, `pri1.txt` (queue strings of up to 1,000 items each, format `imageId,price;imageId,price;…`).
- Want more than 2,000? Raise the number. Lens throughput is ~600–700 items/hour per tab, so 2,000 ≈ 3 hours.

## 3. Start the Lens loop in Chrome (5 minutes of setup, then it runs alone)

1. `tabs_context_mcp` → `tabs_create_mcp` → `navigate` the new tab to `https://www.google.com/robots.txt`. (A plain, nearly empty google.com page. Lens results are google.com, so a same-origin hidden iframe on this page can be read. Don't use the Google homepage — it froze under load.)
2. `Read` `lens_gentle.js` (local copy of `claude/lens_gentle.js`) and paste its entire contents as the `text` of one `javascript_tool` call on that tab. Expected result: `gentle v5 ready mem=<number>`.
3. `Read` `pri0.txt` and run, in the same tab:
   ```
   pushQ("<paste the whole pri0.txt string here>"); newFrame(); runLoop().catch(e=>{STATS.stopped='crash '+e}); 'queued '+QUEUE.length
   ```
   Expected result: `queued 9xx`.
4. Tell Dylan: "Lens pass started on N listings in the robots.txt tab; it runs by itself; he can close that tab any time to stop it." The page shows a live status line at the bottom.

**What the loop does (so you can explain or debug it):** one hidden iframe loads `https://lens.google.com/uploadbyurl?url=<photo>` for each listing; it waits (event-driven, not timers — hidden tabs throttle timers) until the page text contains "Visual matches", reads the page text, parses the match rows (source site, title, price) and the AI-overview sentence, then moves to the next item after a 2.5 s pause. The iframe is recreated every 25 items or after any 30 s stall. It stops by itself at 2,000 items, if the renderer heap passes `MEMLIM` (2,200 MB), or after 7 "unusual traffic" blocks (each block waits 3 minutes first).

**Flag rule (what counts as interesting):** `med` = median price of matches from secondhand/collectible sites (eBay, Etsy, Mercari, Poshmark, Chairish, 1stDibs, WorthPoint, LiveAuctioneers, Invaluable, Proxibid, HiBid, Reverb, Discogs, BrickLink…), ignoring Craigslist and retail stores. An item is flagged if **any** of:
- `med ÷ asking price ≥ 2.5` with at least 2 priced matches and `med ≥ $60`, or
- a collectible-channel site (WorthPoint / LiveAuctioneers / Invaluable / 1stDibs / Chairish / auction houses) matched and `med` is missing or ≥ $80, or
- the AI overview contains a value sentence ("sells for / worth / valued …") with a figure ≥ $100.
Expect 25–40% of prioritised listings to flag. That is fine — Stage 2 is cheap and the point of Stage 1 is recall.

## 4. Monitor (every 10–15 minutes; don't poll faster)

Run on the tab:
```
JSON.stringify({done:STATS.done,flag:STATS.flag,blocked:STATS.blocked,errs:STATS.errs,stalls:STATS.stalls,stopped:STATS.stopped,q:QUEUE.length,mem:memMB()})
```
- `done` should rise ~10/minute. If it hasn't moved in 10 minutes and `stopped` is empty: `RUNNING=false; newFrame();` wait 5 s, then `runLoop().catch(e=>{STATS.stopped='crash '+e})`. If `stopped` starts with `crash`, read the error, fix the script, re-paste it (state in the page survives a re-paste; it does not survive a reload).
- `stopped:"memory …"` → the google.com renderer is heavy (Dylan's Gmail/Drive tabs share it; a fresh reload showed 800 MB with nothing running). Reload the tab, re-paste `lens_gentle.js`, set `MEMLIM=3000`, push the remaining queue (see "resuming" below).
- `stopped:"blocked"` → Google is rate-limiting. Stop for an hour. Next run, add `await sleep(5000)` (edit the `2500` at the end of `runLoop` to `5000`).
- `stopped:"cap"` or `"queue empty"` → finished; go to Step 5.
- Never run two loops at once, never open a second Lens tab, and never remove the 2.5 s pause: the first version (no pause, new iframe per item) froze Dylan's whole PC and he had to force-quit Chrome.

**Resuming after a reload:** everything lives in the page, so a reload loses it. Export first (Step 5) whenever you can. To resume, re-paste the script, set `STATS.idx = <number already done>` so indices stay aligned with `lens_pri.json`, and `pushQ()` the remaining part of the queue string (split `pri0.txt` on `;` and join from the right position).

## 5. Export the results (2 tool calls)

Tool results are truncated at ~1,000 characters, so don't return JSON directly. Instead render it into the page and read the page:
```
let d=document.getElementById('exp')||document.createElement('pre'); d.id='exp'; d.textContent='EXPORT_START\n'+JSON.stringify(FLAGGED)+'\nEXPORT_END'; document.body.prepend(d); 'ok '+d.textContent.length
```
then `get_page_text` on the tab and copy everything between `EXPORT_START` and `EXPORT_END` into `/home/claude/sweep/run<N>/flagged.json` (use the `Write` tool; it's plain JSON). Each entry: `{i, img, price, ratio, med, n, c, best, ai, av, s}` — `i` = position in `lens_pri.json`, `img` = first photo id, `best` = best match title, `s` = match sources, `av` = AI value sentence, `c` = 1 if a collectible channel matched.

Do this at the end, and also every ~500 items (a Chrome crash loses anything not exported).

## 6. Stage 2 — look at the flagged ones properly (container + your eyes)

```
python3 lens_export.py run<N>/flagged.json lens_pri.json       # worklist + stage2.json
python3 lens_export.py --photos stage2.json run<N>/sheets      # one 3×2 photo sheet per listing
```
For **each** flagged listing, in worklist order (highest ratio first):
1. `Read` its photo sheet. Look at the actual object, not the Lens title.
2. Decide what it is. Use the Lens `best` title as a hint, not a verdict — Lens often matches the *category* (any oak rocker, any silver tea set), which gives wildly high `med` values. Write down brand/maker/model/pattern if you can see it; if a mark or label would settle it, note "ask seller for photo of mark".
3. Open the project encyclopedia entry for that item type (`encyclopedia/index.md` → volume file). If one exists, use its tells and sold ranges. If not, you will write one in Step 8.
4. Kill it now if it is: furniture or anything that can't ship for under ~$60 unless the spread is enormous; broken/untested electronics; needs authentication; a reseller's listing (title already has the model, "retails for", lot pricing).
5. Keep a short list of survivors with the exact search string you'd use for sold comps (e.g. `Temple Stuart maple rocker`, not `rocking chair`).

Typical survival rate: 1 in 4 flagged listings reaches Stage 3; 1 in 15–25 flagged listings becomes a real find.

## 7. Stage 3 — sold prices and Dylan's rule (Chrome, ebay.com tab)

Use eBay sold listings (Terapeak via Seller Hub if Dylan's eBay is signed in, otherwise `ebay.com/sch/i.html?_nkw=<search>&LH_Sold=1&LH_Complete=1`). For each survivor:
1. Search the exact name. Exclude parts/"for parts"/lots that don't match. Note the median of the last 10–20 sold prices and whether they sold with shipping charged.
2. `net = median_sold × 0.87 − shipping_to_buyer − shipping_from_seller_to_Dylan`. Use $15 for small items, $30 for medium, $60+ for large/fragile when estimating shipping; ask the seller for a shipping quote in the message if size is unclear.
3. `profit = net − asking_price`. Passes if `profit ≥ max(50, asking_price)`. Tier: **A** profit ≥ 2× price; **B** passes the rule; **C** close (within 20%) — list as "ask for mark/condition photo first".
4. Record the comps in `data/comps.csv` (columns as in that file) — this is what calibrates future runs.

## 8. Write it down (encyclopedia + logs) — do not skip

- For every item type you researched in Stage 2/3 (pass or fail), add or update an entry in the encyclopedia volume for its first letter, following `encyclopedia/README.md` (tells, what sells, sold ranges, "seen in sweeps" line). Add a row to `encyclopedia/index.md`. This is what makes the next run faster and better; it is never used to filter listings out.
- Append the run to `claude/sweep-log.md`: date, harvest size, queued, Lens done, flagged, Stage-2 survivors, finds, blocks/stalls, anything that broke and how you fixed it.
- Push `lens_ledger.json` content forward (it lives in the container; copy the pid list into `data/seen-pids.csv` if you want it to survive the session).

## 9. Deliver

Build the printable PDF with `build_run12.py` as the template (one page per find: photo, title, price, location, what it is, sold comps, profit math, tier, QR code to the listing, a drafted message to the seller). Send it with `SendUserFile`. Then list the finds in the reply in one line each with the next action (e.g. "Hoyt bow $40 — needs reply via Craigslist email relay, draft ready, say OK to send").

Messages to sellers: draft them in the PDF/reply; **send nothing** until Dylan says yes to that message. Craigslist reply addresses need Chrome (`craigslist.org/reply/<area>/<cat>/<pid>` from a logged-in tab); the container gets 404.

---

## Troubleshooting index

| Symptom | Cause | Fix |
|---|---|---|
| `javascript_tool` returns `[BLOCKED: Cookie/query string data]` | the extension refuses to return text that looks like a URL query/cookie | return counts/fields, not raw function source or full URLs |
| Tool result ends in `[TRUNCATED]` | ~1,000-char limit on results | render into a `<pre>` and use `get_page_text` (Step 5) |
| "Chrome extension disconnected" | service worker restarted | wait 5 s, `tabs_context_mcp`, retry once |
| Lens page says "unusual traffic" | rate limit / not a real browser | real Chrome only; slow down; stop for an hour |
| `done` frozen, `stopped` empty | iframe navigation stalled | `newFrame(); RUNNING=false;` then `runLoop()` |
| Everything is flagged with huge ratios | Lens matched the category, not the item | that's expected; Stage 2 photo review is the filter |
| `cl_nat.py` returns few posts | `areas.json` missing or sapi down | re-download Areas JSON; retry later |
| Dylan's PC freezes | too many iframes / no pause | never change the gentle-mode settings; one tab only |
| Loop stops after exactly 1 item, `stopped` empty, `errs` 0 | a helper named like a reserved `window` property (`status`, `name`, `top`, `parent`, `length`…) was overwritten by the browser and threw outside the try/catch | never define `window.status`/`window.name`/etc.; keep `runLoop().catch(...)` so the crash shows up in `STATS.stopped` |
| Memory shows ~800 MB on a fresh tab | `performance.memory` is per renderer process; Dylan's other google.com tabs (Gmail, Drive) share it | that's the baseline, not a leak; `MEMLIM` 2200 is fine |

## Numbers to expect (Run 13, Oct 12 2026)
Harvest 81,854 → 72,105 after junk filter → 2,000 prioritised → Lens ~10/min → 38% flagged → Stage 2 keeps ~25% of those → ~4–8 real finds per 1,000 Lens items.
