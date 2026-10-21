# Refurbish — START HERE

**Read this first, every session.** It is the whole project in one page; the other docs go deeper.

> **Low-usage mode is the default since Oct 21 2026 (Dylan is conserving Claude usage): follow `docs/low-usage.md`.**
> Free GitHub Actions build a ~1,000-photo shortlist daily (text filters + CLIP + encyclopedia type match); 2–3 Sonnet
> eye agents screen it with the matched encyclopedia money tells; the main session deep-reviews only the flags.
> No Opus eye agents, no browser sweeps, no 3-hourly runs.
Branch `refurbish` of github.com/dylanpetty378-arch/game-platform (public repo — never commit personal details:
no names of family, emails, phone numbers, home address. Seller relay emails/phones go in chat, not here).

## 1. What the project is

Dylan runs a resale side-project: **information arbitrage**. Find items listed cheaply by sellers who don't know what
they have (no brand/maker/model in the listing), identify them from the photos, prove the value with sold comps,
buy, and resell with the right name on it. Profits go toward buying a truck.

**Buy rule (never change without Dylan):** price ≤ $200 and expected profit ≥ max($50, price) after ~13% selling
fees and shipping both ways. **$200–$500 tier (Dylan, Oct 13 2026): allowed only if profit ≥ 10× price.** Nationwide — anything anywhere is fair game; we ask the seller to ship and pay for it.
**Out:** repairs, untested/broken electronics (electronics the *seller says are tested/working* are allowed only if profit ≥ 3× price — Dylan, Oct 13 2026), small engines, anything needing authentication (designer bags, signed
sports items, unverifiable precious metal). **Size rule (Oct 12 2026): only items that fit in a car's passenger seat (a little bigger at most).** Anything bigger is
not worth the time — excluded at harvest (`scoring.is_bulky`, -99) and killed on sight in review. Within that limit, spend
MORE time per item: deep research, full encyclopedia entries. (Replaces the older "furniture only if profit ≥ $750".)
**No generalization (Oct 13):** every verdict and every entry names the specific brand, mark, model or variant
that makes one item worth multiples of its lookalikes, and how to see it in a photo. Type-level ranges are not answers.
**Never search by brand name** — the point is finding what the *seller* didn't identify.
**Contact sellers only through the site's own method** (Craigslist reply relay, FB/OfferUp messaging); email only
from Dylan's personal Gmail (never his work account); **send nothing without Dylan's OK for that exact message.**
**Prefers:** decisive recommendations, concise output, printed PDFs for finds (he works from paper).

## 2. How the machine works (Oct 2026 architecture)

```
 GitHub Actions (cloud, free, every 4 h)                 Dylan's Chrome (Tampermonkey userscript, background tab)
 ─────────────────────────────────────                   ──────────────────────────────────────────────────────
 harvest Craigslist, 413 US areas, 29 categories  ──►    reads q/current/queue.txt
 score each title for "seller doesn't know"              for each listing: open Google Lens on photo 1 as a FRESH page
 CLIP image model re-ranks the top 12,000 by photo       (no memory build-up), parse matches + AI overview,
 queue the best 800 new listings per cycle
 ingest Lens results from db/inbox/  ◄──────────────     save result, every 25 → upload to db/inbox/ (GitHub token)
 rebuild queue + STATUS.md + status.json                 pauses itself if Google rate-limits
                         │
                         ▼
             db/ (the database, JSONL in git)  ◄──── any Claude session: photo review, sold comps,
             STATUS.md (what's waiting)               decisions, encyclopedia, PDF for Dylan
```

Why each piece exists and what was rejected: `docs/decisions.md`. Everything learned the hard way: `docs/improvements.md`.

### Runs with no particular device
Everything essential runs in the cloud: GitHub Actions, a Claude scheduled task, and the eBay API. Dylan's Chrome
(the Lens worker and Terapeak) is a bonus that's used when present. Details, plus the "get going" steps for any
new chat: **`docs/device-free.md`**. One working Claude at a time, enforced by `scripts/lock.py`.

## 3. Where things are

| Thing | Location (raw URL base: `https://raw.githubusercontent.com/dylanpetty378-arch/game-platform/refurbish/`) |
|---|---|
| Current status — what's waiting, finds, counts | `STATUS.md` (with photos: https://github.com/dylanpetty378-arch/game-platform/blob/refurbish/STATUS.md), `status.json` |
| Database tables | `db/*.jsonl`, `db/<table>/YYYY-MM.jsonl` — schema in `docs/database.md` |
| Lens queue the Chrome worker reads | `q/current/queue.txt` (+ `meta.json`) |
| Cloud worker | `scripts/cloud_cycle.py` (+ `harvest_cl.py`, `scoring.py`, `clip_rank.py`), run by `.github/workflows/refurbish-cycle.yml` on **main** |
| Chrome worker | `scripts/refurbish-lens.user.js` (Tampermonkey) — doc `docs/lens-worker.md` |
| Fallback Chrome loop (Claude pastes it) | `scripts/lens_gentle.js` v7 |
| Database tool | `scripts/db.py` |
| Stage 2/3 procedure (photo review, comps, decide) | `docs/review-procedure.md` |
| Item-type knowledge ("resell encyclopedia") | `docs/encyclopedia/` (index.md first) |
| History: every earlier method, runbook, sweep log | `docs/history/` |
| Legacy scripts / data (PDF builders, older sweeps) | `scripts/legacy/`, `data/legacy/` |

## 4. Starting a session — do this, in order

**A. With repo access (Claude Code / cloud session with GitHub):**
```
git clone --depth 50 -b refurbish https://github.com/dylanpetty378-arch/game-platform refurbish && cd refurbish
python3 scripts/db.py stats          # where everything is
cat STATUS.md | head -80             # what's waiting
```
**B. Without the repo (plain claude.ai chat):** WebFetch `…/refurbish/STATUS.md` and `…/refurbish/docs/START-HERE.md`
(raw URLs above). You can review flagged listings and research comps; record your conclusions in the chat and, if
nothing can write to the repo, give Dylan the exact `db.py event …` lines so the next repo session logs them.

Then follow **`docs/review-cycle.md`** — the exact run: `python3 scripts/health.py` (PASS/WARN/FAIL for every step:
workflow, harvest, queue, Lens worker freshness + read quality, database integrity, review backlog) → triage the
flagged list (`scripts/review_helpers.py --flagged`) → photo review + listing bodies (`--body <url>`) → sold comps
(Terapeak JS via `--terapeak-js`, else web) → events/comps/encyclopedia → commit `db/ docs/ scripts/` only (never
`q/`, `STATUS.md`, `status.json` — the bot owns them) → dispatch the workflow with no_harvest → Tier A/B finds go to
Dylan as a PDF (`scripts/build_report.py`, seller contacts only in the spec in /tmp).

**Scheduled:** ONE Claude cloud scheduled task, "Refurbish review cycle", runs this every 3 h with no device bound.
It respects `scripts/lock.py`. A chat that has Chrome and a signed-in eBay account should re-check keepers on
Terapeak. With no Chrome, use `ebay_api.py` comps plus the stored comps. See docs/device-free.md.

**History / logs on request:** everything is in `db/` — `python3 scripts/db.py sql "SELECT …"` (tables harvests,
searches, listings, lens, events, comps, item_types, runs; view listing_status = latest stage per listing), plus `git
log` of the branch (every cycle and every worker upload is a commit).

## 5. Standing instruction from Dylan

Keep finding better ways to do this and update these docs. When choosing between approaches, research and pick
the most comprehensive one; record the reasoning in `docs/decisions.md`. Free/no-limit options over paid ones.
