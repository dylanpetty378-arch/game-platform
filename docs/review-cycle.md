# Review cycle: what the working Claude chat does, over and over

Dylan (Oct 12 2026): one working chat does all the iterations. No separate scheduled Claude sessions change code, because
they could overwrite each other. The cloud workflow and the Lens worker run by themselves; the chat reviews, researches,
improves and documents. When you think you're out of things to do, check every step again.

Take longer per item and research deeply. Everything learned goes into the encyclopedia and the database.

## 0. Setup (any new chat)
- `add_repo dylanpetty378-arch/game-platform` (push), then
  `git clone --depth 200 -b refurbish https://github.com/dylanpetty378-arch/game-platform && cd game-platform`.
- `git config user.email noreply@anthropic.com && git config user.name Claude`. Read `docs/START-HERE.md`.

## 1. Health check: every step of the machine
`python3 scripts/health.py` prints PASS/WARN/FAIL with numbers for:
- workflow runs
- harvest age and failures
- queue age and size
- Lens freshness, read quality and worker version
- flag rate
- JSONL integrity
- inbox
- review backlog

Fix FAILs first: change the code, push, then run
`gh api -X POST repos/dylanpetty378-arch/game-platform/actions/workflows/refurbish-cycle.yml/dispatches -f ref=main -f 'inputs[no_harvest]=true'`
and log the fix in `docs/improvements.md`. For the Chrome worker, read the control page
`https://www.google.com/robots.txt?refurb` in a non-worker tab. Never navigate or close the worker tab, and never press
Start in a second tab.

## 2. Triage the flagged list
Run `python3 scripts/review_helpers.py --flagged`.
- **Kill at once** (event `photo_review/kill`, a one-line reason, `type` slug) for:
  - anything bigger than a car's passenger seat (size rule, no exceptions)
  - policy-banned items: offensive imagery, ivory
  - untested or broken electronics
  - items that need authentication: designer bags, luxury watches
  - obvious reproductions
  - antique-mall dealer stock
- **Treat Lens medians as asking prices, not sales.** A median above 5× the asking price usually means a wrong or
  category-level match. Judge by the photo.
- Everything else gets photo review.

## 3. Photo review, listing body, item rubric
- Make photo sheets: `python3 scripts/review_helpers.py --shortlist pid,pid,…` then
  `python3 scripts/lens_export.py --photos shortlist.json sheets/`. Read each one.
- Fetch the listing body with `review_helpers.py --body <url>`. It often changes the verdict: per-item pricing, damage
  mentions, "local cash only".
- Read any text visible on the item, such as "21 Jewels" or "14K". Wrong subject names in a title ("Napoleon" for an
  Incroyable) are leads.
- Score the item rubric (docs/rubric.md). Store it as an event with `stage=rubric` and the fields in `data`.

## 4. Research the type deeply (for passes too)
- Run `python3 scripts/enc.py find <words>`.
  - If an entry exists: apply it, then add the sighting with `enc.py seen <slug> "<line>"`.
  - If there's no entry, or the item is a variant the entry doesn't cover: research it fully and write or extend the
    entry. Use the template in docs/encyclopedia/README.md, including the rubric JSON, then run `enc.py add <file>`.
- For many types at once, use research agents with `research/BRIEF.md` (one agent per 8 types, 6 in parallel).
- **Sold prices:** use Terapeak in Chrome on an ebay.com/sh/research tab.
  - Get the TPR/COMP helper from `scripts/review_helpers.py --terapeak-js`. For bulk runs, use the in-page loop in
    `research/terapeak-bulk.md`.
  - The container can't reach eBay sold pages, and WorthPoint is paywalled. WebSearch is capped at 200 calls per chat
    turn, shared by all agents in the turn, so save searches for identification and use Terapeak for prices.
- Log every query with `db.py search` and every comp with `db.py comp`.

## 5. Decide
- Apply the rule: profit = median × 0.87 − ship to buyer − ship to Dylan − price. It passes if profit ≥ max(50, price).
- Tier A: profit ≥ 2× price. Tier B: passes. Tier C: needs an answer or an offer.
- Record the event `decided` with data {price, est_resale, profit, tier}.
- For A/B: start the item dossier (docs/item-dossiers.md). Build the printable report with `scripts/build_report.py`,
  using a spec in /tmp so seller contacts never go in the repo. Send it to Dylan.
- For asks: draft the seller message. Never send anything without Dylan's OK on that specific message.

## 6. Learn and improve
- Run `enc.py index && enc.py sync`.
- Put anything that would make this faster or better in `docs/improvements.md`, and make small safe fixes now.
- Commit `db/ docs/ scripts/ research/` only. Never commit `q/`, `STATUS.md` or `status.json`; the bot owns them.
- Run `git pull --rebase -X theirs`, push, then dispatch the workflow with no_harvest.
- Then go back to step 1.
