# Refurbish — START HERE

**Read this first, every session.** It is the whole project in one page; the other docs go deeper.
Branch `refurbish` of github.com/dylanpetty378-arch/game-platform (public repo — never commit personal details:
no names of family, emails, phone numbers, home address. Seller relay emails/phones go in chat, not here).

## 1. What the project is

Dylan runs a resale side-project: **information arbitrage**. Find items listed cheaply by sellers who don't know what
they have (no brand/maker/model in the listing), identify them from the photos, prove the value with sold comps,
buy, and resell with the right name on it. Profits go toward buying a truck.

**Buy rule (never change without Dylan):** price ≤ $200 and expected profit ≥ max($50, price) after ~13% selling
fees and shipping both ways. Nationwide — anything anywhere is fair game; we ask the seller to ship and pay for it.
**Out:** repairs, untested/broken electronics, small engines, anything needing authentication (designer bags, signed
sports items, unverifiable precious metal). Furniture only if profit ≥ $750 (Honda Civic, no storage).
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
 queue the best 800 new listings per cycle               (no memory build-up), parse matches + AI overview,
 ingest Lens results from db/inbox/  ◄──────────────     save result, every 25 → upload to db/inbox/ (GitHub token)
 rebuild queue + STATUS.md + status.json                 pauses itself if Google rate-limits
                         │
                         ▼
             db/ (the database, JSONL in git)  ◄──── any Claude session: photo review, sold comps,
             STATUS.md (what's waiting)               decisions, encyclopedia, PDF for Dylan
```

Why each piece exists and what was rejected: `docs/decisions.md`. Everything learned the hard way: `docs/improvements.md`.

## 3. Where things are

| Thing | Location (raw URL base: `https://raw.githubusercontent.com/dylanpetty378-arch/game-platform/refurbish/`) |
|---|---|
| Current status — what's waiting, finds, counts | `STATUS.md`, `status.json` |
| Database tables | `db/*.jsonl`, `db/<table>/YYYY-MM.jsonl` — schema in `docs/database.md` |
| Lens queue the Chrome worker reads | `q/current/queue.txt` (+ `meta.json`) |
| Cloud worker | `scripts/cloud_cycle.py` (+ `harvest_cl.py`, `scoring.py`), run by `.github/workflows/refurbish-cycle.yml` on **main** |
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

Then:
1. **Is the cloud worker healthy?** `STATUS.md` timestamp should be < 5 h old. If not: repo → Actions → refurbish-cycle
   (or `gh api repos/dylanpetty378-arch/game-platform/actions/runs`). Fix, re-run, log in `docs/improvements.md`.
2. **Is the Chrome worker running?** STATUS shows Lens results arriving (`lens` count rising; `lensworker-*` runs).
   If not, and Chrome tools are available: open `https://www.google.com/robots.txt?refurb` and read the panel.
3. **Work the flagged list** (`python3 scripts/db.py worklist flagged` or STATUS.md) with `docs/review-procedure.md`.
   Log every step as an event (`db.py event <pid> photo_review --status kill --note "…" --type <slug>`).
4. **Finds → PDF for Dylan** (`scripts/legacy/build_run12.py` style; format in `docs/history/report-format.md`),
   drafted seller messages in the PDF/reply, nothing sent without his OK.
5. **Write down what you learned**: encyclopedia entries for every item type researched, improvements/lessons in
   `docs/improvements.md`, run summary `db.py run <id> --data '{…}'`. Commit + push (`git pull --rebase` first —
   the cloud bot commits too).

## 5. Standing instruction from Dylan

Keep finding better ways to do this and update these docs. When choosing between approaches, research and pick
the most comprehensive one; record the reasoning in `docs/decisions.md`. Free/no-limit options over paid ones.
