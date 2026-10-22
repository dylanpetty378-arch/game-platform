# Facebook Marketplace — Refurbish Watcher (Oct 22 2026)

Dylan finds great deals on Facebook but can only see a couple dozen of the thousands of new local posts a day. The
Refurbish Watcher Chrome extension reads Marketplace's category feeds — every listing in a category, newest first,
within 50 miles of Keller — and saves them to this repo. Free compute scores them. A Claude chat reviews them when
Dylan asks. No alerts, no Claude usage while sweeping.

**Dylan's decision (Oct 22 2026):** go ahead with the token-replay design, accepting Facebook's terms-of-service risk
and a small chance of the account being restricted. Keep it human-paced: ≤ 120 feed pages per sweep (Facebook
rate-limits around 100–150), pauses between pages, sweeps started by Dylan (or an optional repeat ≥ 2 h).

## How it works
1. **Extension** (tools/fb-extension, on Dylan's home computer): opens a Marketplace category page in a background tab,
   reads Facebook's own search query + session tokens from it (method from the Sept/Oct 2026 browser sweeps —
   project doc claude/site-access-methods.md), moves the tab to facebook.com/robots.txt, then replays the query one
   page at a time per category feed: local pickup only, ≤ 50 mi of Keller, ≤ $400, newest first. A feed stops when a
   whole page is listings it already saved. New listings → `db/fb/inbox/<time>.json` on branch `refurbish`.
   Stored per listing: id, title, price, city/state, photo URL, category. **Never seller names or profiles.**
2. **fb-score workflow** (GitHub Actions, free, on every inbox push): `scripts/fb.py score` → text filters (junk,
   > $400, > 60 mi), CLIP collector look + encyclopedia type/value, similar-sold (kNN over SGW sold lots), melt floor,
   distance band from Keller → `db/fb/scored/<date>.jsonl`.
3. **Review** (a Claude chat, when Dylan says "review the facebook posts"): below.

## Setup (once, on the home computer — Dylan)
1. **GitHub token:** github.com → Settings → Developer settings → Personal access tokens → Fine-grained → Generate.
   Repository access: *Only select repositories* → `game-platform`. Permissions: **Contents: Read and write**. Expiry:
   up to a year. Copy it. (It stays inside the extension on that computer; don't paste it anywhere else.)
2. **Install:** unzip `refurbish-watcher.zip` → Chrome → `chrome://extensions` → turn on **Developer mode** →
   **Load unpacked** → pick the unzipped folder. Pin the extension (puzzle icon → pin).
3. Be logged in to Facebook in that Chrome profile.
4. Click the extension → Settings → paste the token → Save. Defaults: 50 mi, $400, 120 pages, feeds antiques,
   jewelry, instruments, hobbies, free, toys, entertainment, sports, home-improvements.
5. **Start sweep.** The status box shows pages / seen / new / saved. A first sweep takes ~5 minutes.
   Optional: "Repeat every N h" (minimum 2) keeps sweeping while Chrome stays open.

**If it says "No Marketplace query found":** open facebook.com/marketplace once by hand, make sure you're logged in, try
again. Facebook changes its pages occasionally — send the exact status message to a Claude chat to fix the extension.

## Review procedure (Claude chat — "review the facebook posts")
Low-usage rules apply (docs/low-usage.md): ≈ 20 tool calls, Sonnet eye agents only, deep review ≤ ~8 items.
1. Clone/pull `refurbish`; `python3 scripts/lock.py take "<chat>" 2`; `pip install -q --break-system-packages pillow`.
2. `python3 scripts/fb.py stats` then `python3 scripts/fb.py prep` → run name `fb-<ts>`, sheets of the best ≤ 480
   unreviewed listings (title carries `[city Nmi]`; > 30 mi is marked "needs notice").
3. Eye: one Sonnet agent per batch, same prompt as docs/low-usage.md step 3, plus: "These are Facebook Marketplace
   local-pickup listings near Keller TX — read the Facebook section of the brief."
4. `cat flags_*.tsv > flags.tsv && python3 scripts/lowuse.py panels <run> flags.tsv` (one photo per Facebook listing;
   Dylan opens the link for more).
5. Deep review (sold comps by WebSearch). Facebook prices are fixed and usually negotiable: give a **max offer**, not a
   max bid; profit rule as everywhere (≥ $50 under $50, ≥ the price above $50) after ~13% fees + shipping if resold
   on eBay, or no fees if resold locally.
6. `python3 scripts/lowuse.py log <run> verdicts.tsv`, then `python3 scripts/fb.py done <run>`.
7. Reply to Dylan: each lead with price, max offer, city + miles, link, what to ask/check in person. Never message
   sellers. Commit db/ docs/ research/, push, release the lock.
