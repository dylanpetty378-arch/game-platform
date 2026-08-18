# Stack and hosting

*The technology tiers and the reasoning are settled in `../architecture.md` §10 — this document is the operational restatement plus the vendor picks at the budget Dylan set (~$25/month for the playtest era). Every vendor here is **Tier 2: replaceable in one to two weeks.** The test of every choice below is that leaving it is a fortnight, not a rewrite.*

## The stack (decided; do not relitigate)

| Layer | Choice | Tier |
|---|---|---|
| Language | **TypeScript, strict mode**, everywhere — client, server, ruleset. Discriminated unions, exhaustive switches, branded types for every ID | 1 |
| Rules | **The pure `/ruleset` package** — no I/O, no framework imports, no vendor types, no `Date.now`, no `Math.random`, no floats | 1 |
| Storage | **PostgreSQL**, hand-rolled event store (~400 lines owned outright). One database. No ORM — the `postgres` (porsager) driver and hand-written SQL | 1 (semantics) / 2 (host) |
| Realtime | **Plain WebSockets** (`ws` on the server), owned message protocol (`api-and-protocol.md`) | 1 (protocol) / 2 (host) |
| Client | **React 19 SPA on Vite.** NOT Next.js, NOT React Server Components | 1 (React as client lib) |
| Validation | **zod** at every boundary (HTTP bodies, WS payloads, asset payloads, tunables). Types inferred from schemas, one source of truth in `/shared` | 2 |
| Styling | Plain CSS with design tokens from `../brand-identity.md` (CSS custom properties: `--void #080D11`, `--paper #F3F2EE`, `--graphite #21242A`, `--steel #39414B`, `--signal #22D3EE`). No Tailwind, no CSS-in-JS runtime — fewer moving parts, and the beta is deliberately plain | 2 |
| Monorepo tooling | **pnpm workspaces** + TypeScript project references. No Nx/Turbo — three packages don't need an orchestrator | 3-avoidance |
| Tests | **vitest** everywhere; the determinism fixtures are ordinary vitest suites in `/tools` | 2 |

**Explicitly not used** (Tier 3, per §10.1): meta-frameworks, magic ORMs (Prisma/Drizzle), managed realtime (Pusher/Ably), backend-as-a-service (Supabase-as-platform, Firebase), sync engines, GraphQL/tRPC (a hand-typed HTTP+WS surface is smaller than the machinery).

## The vendors, at ~$25/month

| Concern | Pick | Cost | Why, and the exit |
|---|---|---|---|
| App server (API + WS + serves the SPA) | **Fly.io**, one `shared-cpu-1x` machine (512MB–1GB), always-on | ~$5–8/mo | One Node process holds the rooms in memory exactly as §10.4 prescribes; no cold starts (WS hates them); `fly.toml` in repo. Exit: any Docker host — the app is one container |
| Postgres | **Neon** Launch plan | $19/mo | Real Postgres, point-in-time restore, branching (dev branches per feature are genuinely useful for schema work). Exit: `pg_dump` to any Postgres — the schema is plain SQL |
| Transactional email (magic links) | **Resend** free tier | $0 (3k/mo) | One `POST /emails` call. Exit: any SMTP/API provider behind the 30-line `mailer.ts` |
| Offsite backups | **Cloudflare R2** free tier | ~$0 | Nightly `pg_dump` from a Fly scheduled machine, uploaded to R2, 30-day retention. Neon's PITR is the first line; R2 is the "vendor died" line |
| DNS/domain | Cloudflare registrar | ~$10/yr | Domain waits on Vectus clearance; until then the Fly `*.fly.dev` URL is fine for playtesters |
| CI | **GitHub Actions** (private repo free minutes) | $0 | Runs typecheck, tests, determinism fixtures, and the docs lint on every push; deploy on main via `flyctl` |
| Errors/observability | **Sentry** free tier + Fly logs | $0 | Structured `pino` logs; Sentry for client+server exceptions. No metrics stack yet — the playtest event log *is* the analytics |

**Total: ≈ $25–28/month.** The single most load-bearing property: the app is one Docker container plus one Postgres URL plus one email API key. That whole footprint moves anywhere in an afternoon.

## Environments

- **`dev`** — local: `pnpm dev` runs Vite + the server with a local Postgres (Docker `postgres:17` via `compose.yaml`) or a Neon dev branch. Seed script creates Dylan (super-admin), one demo campaign, the reference content.
- **`prod`** — the Fly app + Neon main. **There is no staging in the playtest era** — the playtest *is* staging; a `deploy_freeze` tunable lets Dylan pause deploys mid-session. Staging appears at Phase 5.
- Config via environment variables only, validated at boot by a zod schema in `/server/env.ts` — the process refuses to start on a missing var. Secrets live in Fly secrets and GitHub Actions secrets; never in the repo.

## Migrations

Plain SQL files in `/server/migrations/NNN_name.sql`, applied in order by a ~60-line runner (`pnpm migrate`) that records applied filenames in a `schema_migrations` table, wraps each file in a transaction, and refuses to run out of order. No down-migrations — forward-only, matching the append-only temperament of the whole system. Destructive changes require a new column/table + backfill + later drop, each its own migration.

## CI pipeline (GitHub Actions)

1. `pnpm install --frozen-lockfile`
2. `pnpm typecheck` (all packages, project references)
3. `pnpm test` (vitest, includes the determinism fixtures and golden files)
4. `pnpm lint` (eslint with the no-float and no-wall-clock rules from `claude-md-template.md`)
5. On `main` only: build the container, `flyctl deploy`, then run `pnpm smoke` against prod (login-page 200, WS connect, `/healthz` reports DB + migrations current).

A red step blocks deploy. The determinism fixtures failing is treated exactly like the docs lint in `game-platform`: **fix the code, never the fixture** — fixtures change only when a Part 12 decision changed the arithmetic.

## Backups and the export promise

Nightly `pg_dump --format=custom` to R2. Additionally — because Q5.2 ("can the game be played without your server") is answered structurally by the append-only Ledger — **the per-campaign export endpoint ships in the playtest era** (`api-and-protocol.md`): any campaign's complete Record history as canonical JSON, byte-stable, re-importable. The export is a user feature, a backup, and the obsolescence answer in one.
