# The build order — milestones M0 → M9

*A dependency order, like every sequence in this project. Each milestone has acceptance criteria; a milestone is done when they all pass, and not before. `PROGRESS.md` at the repo root records where things stand — every session updates it. Estimated shape, not schedule: no dates, per the phase-map's rule.*

## M0 · The scaffold
Create the private `vectus` repo: pnpm workspaces (`/ruleset /server /client /shared /tools /ops`), TypeScript strict + project references, eslint (with the no-float and no-wall-clock rules), vitest, `compose.yaml` (Postgres 17), the migration runner + migration 001, CI running typecheck/test/lint, `CLAUDE.md` from `claude-md-template.md`, `PROGRESS.md`, README pinning the game-platform docs commit.
**Done when:** CI is green on a hello-world of each package; `pnpm dev` serves a page; `pnpm migrate` applies 001 locally.

## M1 · The engine core, proven
`/ruleset` per `engine-spec.md`: substrate types, apportionment, canonical hashing, PRNG, dimensions/channels(generated)/tracks/attempt data, the resolution pipeline for the slots the beta exercises, shaping, guards, scale, landing, economy; the fixture harness porting **every** `phase-0-checks.py` case; the determinism suite (fold twice, hash-compare; golden files).
**Done when:** all ported fixtures green; `hash(fold(fixtureLedger))` matches goldens; dependency-cruiser proves `/ruleset` imports nothing.

## M2 · Ledger + server spine
Migrations 002–003; the event store module (append with optimistic seq, read streams); fold-on-read with the per-room cache; `/healthz`; auth end-to-end (magic links via Resend, sessions, invites, rate limits); the `can()` authz table.
**Done when:** a script creates a campaign, appends 1,000 records concurrently without a gap or dupe, folds identically to the engine fixtures; login works from a real inbox.

## M3 · The wire
`api-and-protocol.md` in full: HTTP routes for campaigns/members/state/records/expansion; the WS server (hello/subscribe/command/records/reply), reconnect-resume, idempotency, optimistic-prediction support in the client runtime.
**Done when:** two browsers at one table see each other's commands < 500ms; kill one mid-session, reconnect, state identical (hash check in dev overlay); replayed command with same idempotency key appends once.

## M4 · The table (play, visible)
`/c/:id/play` + `/c/:id/gm` per `site-map.md`: full-state display (law 1), the attempt interface (Attempt Point buttons, declaration-order join, cap-disable), resolution expansion open-by-default, the event-log rail, doubloon bar, GM declarations with the downside-bar counter, Ordered-time entry (Q3.3 rule + manual), Proposals with Decider defaults. Tunables live (migration 006, `/tuning`, per-campaign overrides, changes logged) — dice expression swap mid-session works. Playtest event batching (migration 007, `POST /events`) wired into every play surface.
**Done when:** `../beta-spec.md`'s developer-page list is fully satisfied and a scripted two-player scene (the lock, an attack, a reaction, a Repin, a Proposal default firing) runs clean end-to-end; every beta-spec measurement query returns rows.

## M5 · Characters and sheets
Migration 004; `/characters/new` as the `creation_flow`-driven shell; the sheet component rendering person/ship/faction from Category bundles (the kind-agnosticism test, on screen); derived values expandable to sources.
**Done when:** the three sheets render from three Entities; a person made via a seeded minimal creation_flow can play M4's scripted scene.

## M6 · The authoring studio + inject
Migration 005; `authoring-pipeline.md` in full: schema-driven forms for all kinds, live compilation preview, the expressibility validator with misfit classification, publish with approval, the library; `/admin/inject` bulk door + `pnpm asset-schema` bundle; state inspector + log browser + notes; what-if stub.
**Done when:** a GM creates a creature + ability + threshold_set in the studio and uses them the same session; a JSON batch with one good asset, one `misfit:additive`, one `misfit:structural` and one agent-prose violation produces exactly the right four outcomes.

## M7 · The explainer
`rules-explainer.md` in full, plus the public landing page and about/no-AI pages per `site-map.md`.
**Done when:** its acceptance checklist passes, logged out, on a phone.

## M8 · Async play
The Dispatch: a per-player digest of what changed / what's waiting / what you can do (new `dispatches` table: id, campaign_id, user_id, generated_at, body jsonb, seen_at); standing orders authored per character (Standing Order parameters are already authorable); Proposal timers firing defaults on a scheduled sweep; email nudge via Resend. This is the six-week play-by-post test's machinery — the business bet, in the same build.
**Done when:** a two-player async campaign advances a full scene over three days with each player logging in twice; nothing ever waits forever (timer sweep proven by test).

## M9 · Hardening for strangers
Sentry wired; backup cron to R2 verified by a restore drill; export/import round-trip byte-identical (the determinism harness's first cross-machine run — Phase 3's opening move); load sanity (20 concurrent sockets, one campaign, p95 command < 300ms); a pass of `design:accessibility-review` basics (contrast on Void, keyboard play); invite flow polished.
**Done when:** Dylan invites the first stranger group with a straight face.

---

**Standing rules across all milestones:** vocabulary from `dictionary.md` exactly, including identifiers · every non-trivial unit specs first in `/spec` · fixtures never regenerate to pass · every session ends green, `PROGRESS.md` updated, pushed · findings that smell structural stop the line and get written up against the corpus, not worked around.
