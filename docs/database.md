# The database

Plain files in git: `db/` on the `refurbish` branch. One JSON object per line, **append-only** (never edit or delete a
line; corrections are new lines). `scripts/db.py` reads them all into SQLite (`/tmp/refurb.sqlite`) for queries.

## Tables

| Table | File | One row per | Key fields |
|---|---|---|---|
| `harvests` | `db/harvests.jsonl` | harvest/sweep of a site | harvest_id, source, hours, cats, n_listings, n_new, n_selected, by_cat, failed_requests |
| `searches` | `db/searches.jsonl` | any individual query typed anywhere (eBay sold search, web search, site search) | site, query, purpose, results, run |
| `listings` | `db/listings/YYYY-MM.jsonl` | listing the pipeline touched (first sighting) | pid, source, title, price, area, region, cat, imgs, url, posted (epoch), score |
| `lens` | `db/lens/YYYY-MM.jsonl` | Google Lens result — **every one**, flagged or not | pid, run, best, med, n, ratio, collect, sources, ai, ai_value, flag |
| `events` | `db/events/YYYY-MM.jsonl` | stage change of a listing | pid, stage, status, type, note, run, by, data |
| `comps` | `db/comps.jsonl` | sold-comparables lookup | type (encyclopedia slug), query, source, prices[], median, n, pid |
| `item_types` | `db/item_types.jsonl` | encyclopedia entry | slug, name, volume, aliases |
| `runs` | `db/runs.jsonl` | run summary | run + free-form numbers |
| inbox | `db/inbox/*.json` | upload from the Chrome worker, waiting for the cloud cycle to ingest | (deleted after ingest) |

Not stored: the full raw harvest (~260 K listings / 48 h, ~100 MB). Only listings selected into the queue are kept;
counts per category are kept in `harvests`. Reason in `docs/decisions.md`.

## Stages (a listing's current stage = its latest event)

`harvested → queued → lensed | flagged → photo_review → identified → comps → decided → contacted → bought → listed → sold`
(+ `expired` when the listing is gone). Use `--status` for the outcome at that stage:

| stage | status values | note / data |
|---|---|---|
| photo_review | `keep` / `kill` | why (one line); `--type` = encyclopedia slug of what it is |
| identified | `sure` / `likely` / `need_mark` | maker/model/pattern; what photo would settle it |
| comps | `pass` / `fail` / `close` | median, n, net profit math in `--data` |
| decided | `find` / `ask` / `pass` | tier A/B/C, profit; `ask` = need seller info first |
| contacted | `sent` / `replied` / `no_reply` | channel (never the seller's contact details in this public repo) |
| bought / listed / sold | — | prices, platform, dates in `--data` |

## Commands

```
python3 scripts/db.py stats
python3 scripts/db.py worklist flagged
python3 scripts/db.py show 7966413399
python3 scripts/db.py event 7966413399 photo_review --status kill --type waste-basket --note "modern cedar bin, not antique"
python3 scripts/db.py comp --type carved-santo --query "carved santo gilt" --source ebay_sold --prices 1450,399,365,300 --pid 79…
python3 scripts/db.py search --site ebay_sold --query "Louis XV gilt bronze chenets" --purpose comps --results 14
python3 scripts/db.py sql "SELECT area, COUNT(*) FROM listing_status WHERE stage='flagged' GROUP BY 1 ORDER BY 2 DESC"
python3 scripts/db.py seen > seen.txt
```
`listing_status` is a SQL view: every listing with its latest stage/status.

## Rules
- Always `git pull --rebase origin refurbish` before committing; the cloud bot commits every few hours.
- Log as you go (each kill, each comp search) — not at the end. The log is what makes the next session faster and
  what lets us measure which methods actually find things.
- Never write personal data here (public repo).
