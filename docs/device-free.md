# Running with no particular device (Oct 13 2026)

Dylan: "This should run on any device. I should only have to tell you to get going." So nothing essential may
depend on one laptop being open.

## What runs where

| Piece | Where it runs | Needs a device? | If the device is off |
|---|---|---|---|
| Harvest Craigslist (413 areas), score, CLIP re-rank, queue, STATUS | GitHub Actions `refurbish-cycle` | No | — |
| eBay comps (`scripts/ebay_api.py`, official API) | GitHub Actions, once Dylan adds the `EBAY_CLIENT_ID` / `EBAY_CLIENT_SECRET` secrets | No | — |
| Review cycle: triage, research, encyclopedia, decisions, PDFs | Claude cloud scheduled task "Refurbish review cycle" (fresh cloud session every 3 h) or any chat | No | — |
| Database (db/*.jsonl), docs, encyclopedia | git, `refurbish` branch, plus copies in the claude.ai Refurbish project | No | — |
| Google Lens reads (Tampermonkey worker) | Dylan's Chrome | **Yes** — a bonus, not required | Triage uses `review_helpers.py --unlensed` (title + photo + body read by Claude). Lens flags produced 0 keepers; the leads came from reading. |
| Terapeak sold prices | Any Chrome with the Claude extension, signed in to eBay | **Yes** — a bonus | Sold data comes from (1) 1,400+ stored comps in the encyclopedia, (2) the Marketplace Insights API if eBay approves it, (3) active asks from the Browse API as a ceiling. A lead verified only by active asks is marked "needs sold check" in the PDF. |

## "Get going" — what any new chat does (any device, claude.ai or Claude Code)
1. Attach the repo: `add_repo dylanpetty378-arch/game-platform` (push), then clone `-b refurbish`. Read `docs/START-HERE.md`.
2. `python3 scripts/lock.py status`. If Dylan is in this chat, `take "<chat id>" 3 --force`, commit and push
   `ops/lock.json`. The scheduled runner backs off while a live lock belongs to someone else.
3. Follow `docs/review-cycle.md`. Use Chrome tools only if they're present (Terapeak, Lens). Otherwise use the
   device-free paths above.
4. Before stopping: release the lock, commit, push, and refresh the project volumes (`enc.py volumes`).

With no repo tooling (a plain chat), read STATUS.md and START-HERE.md via WebFetch from raw.githubusercontent.com
and work from those. Then hand Dylan the `db.py event …` lines to log next time.

## The scheduled runner
One recurring Claude cloud task runs the review cycle every 3 h, with no device bound. It is the ONLY scheduled
Claude job for this project, so scheduled sessions never overlap. It takes the lock at start, skips writing if
someone else holds a live lock, and releases the lock at the end.
