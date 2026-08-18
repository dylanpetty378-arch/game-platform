# The engine — the pure `/ruleset` package

*Tier 1. The game itself, as a TypeScript package with no I/O, no framework imports, no vendor types, no wall clock, no `Math.random`, no floats. The client imports it for optimistic prediction and the explainer's live widgets; the server imports it as the authority. This document also closes the four pre-code specs `../phase-map.md` requires: canonical serialization + hashing, the PRNG, the integer policy, and (in `api-and-protocol.md`) the WS reconnect protocol.*

## Package layout

```
/ruleset
  /substrate
    ids.ts            branded id types (EntityId, RecordSeq, Moment, …)
    entity.ts         the eight universal fields; Category bundles
    verbs.ts          the seven Verb payload shapes (closed union, exhaustive)
    moments.ts        the nine Moment kinds; every reference carries a round
    proposal.ts       Proposals, Deciders, defaults, timers-as-data
    listener.ts       the 7 condition forms; once/while; and/or/not
    fold.ts           THE FOLD — see contract below
    lattice.ts        the 41 slots, five regions, as data
    apportion.ts      trunc_div + integer apportionment (port of phase-0-checks.py)
    canonical.ts      canonical JSON + state hash (spec below)
    prng.ts           the keyed counter PRNG (spec below)
  /editions/e1
    dimensions.ts     the 14 non-attempt Dimensions (from dictionary L22)
    channels.ts       the 88 Channels — GENERATED from game-platform docs/channels.py; do not hand-edit
    tracks.ts         the 14 Tracks with bands (L5)
    attempt.ts        7 Domains / 15 attempt Dimensions (L29); Attempt Point resolution
    resolution.ts     the R-region pipeline, slot by slot; returns the full expansion
    shaping.ts        Bonus Points → Baseline, points only
    guards.ts         named flat → universal flat (redistribute) → cancellation → proportional
    scale.ts          R-750 conversion; parts carry their own Scale
    economy.ts        doubloons; cost = { cost, timing, cap }
    landing.ts        the landing spec: push the Track the Dimension names; contributor
                      breakdown, sort key; sum/highest/each Threshold reads
    listeners.ts      evaluation order: class → (layer, component_id, listener_id,
                      target_entity_id, source_record_id); depth 32; halt-and-Record
  /sockets
    place.ts          minimal occupant: named zones, here/near/far
    resolution.ts     minimal occupant: dice expression evaluator + published distribution
  index.ts            the public surface, and nothing else
```

## The Fold contract

```ts
fold(records: Record[], config: FoldConfig): CampaignState
// Pure. Deterministic. Same records + same config → identical state, byte-identical hash.
// FoldConfig = { edition, componentVersions, tunables } — tunables come in as explicit
// inputs; the engine NEVER reads a database or a clock.
step(state: CampaignState, record: Record, config): CampaignState   // fold = records.reduce(step)
expand(records, config, seq): ResolutionExpansion   // every slot of one resolution, derived not stored
hash(state): string                                  // canonical hash, spec below
```

State is immutable-by-convention (readonly types; no in-place mutation — enforced by lint). `step` throws only `EngineHalt` (cascade limit, integer overflow) — which the server converts into a halt Record, per the settled halt-and-write-a-Record rule.

## Canonical serialization + state hash *(pre-code spec #1, now law)*

- Canonical JSON per **RFC 8785 (JCS)**: object keys sorted by UTF-16 code units, no insignificant whitespace, numbers in JCS form — trivially satisfied because **every number in engine state is an integer**.
- `hash(state)` = lowercase hex **SHA-256** of the JCS bytes of the state with map-like collections represented as sorted arrays of `[key, value]` pairs (never relying on JS object insertion order).
- Postgres `jsonb` does not preserve key order — irrelevant by construction, because hashing always re-canonicalizes; nothing ever hashes stored bytes.
- The determinism harness (`/tools`) folds fixture ledgers and compares hashes across Node versions and against golden files in CI.

## The PRNG *(pre-code spec #2, now law)*

Keyed, counter-based, stateless — so any roll is reproducible from its coordinates and no fold order can drift it:

```
seed   = campaign.rng_seed (32 random bytes fixed at campaign creation, stored in campaigns)
draw(seed, recordSeq, purpose, counter) =
  SHA-256(seed ‖ u64be(recordSeq) ‖ utf8(purpose) ‖ u32be(counter)) → first 8 bytes → u64
```

Dice values come from `draw` via **rejection sampling** (reject u64 ≥ ⌊2⁶⁴/n⌋·n, increment counter, redraw) so every die is exactly uniform. The dice expression evaluator (Resolution occupant) parses `NdM(+NdM…)` from the `attempt_roll` tunable, draws each die with `purpose = "attempt:die:<i>"`, and **records the rolled values into the Resolution Record's payload** — refolds never re-roll; the PRNG exists for the first execution and for what-if.

## The integer policy *(pre-code spec #3, now law)*

All engine arithmetic is on JS `number` integers with a CI-asserted working bound of |x| ≤ 2⁴⁵ (safe-integer headroom for any intermediate product). No `BigInt` in the hot path — magnitudes at Scale extremes stay within bounds because Scale conversion divides before anything multiplies. Division exists only as `truncDiv` (toward zero — ported with its phase-0 test cases). Floats are banned by an eslint rule (`no-restricted-syntax` on non-integer literals in `/ruleset`, plus a runtime `assertInt` at every public entry in dev builds). Overflow → `EngineHalt` → halt Record, same discipline as the cascade limit.

## Fixtures — the arithmetic is already proven; keep it proven

`game-platform/docs/phase-0-checks.py` is the source of golden truth. M1 ports every check into vitest fixtures (`/tools/fixtures/*.json` + runners): apportionment sweeps, no-Alabama-paradox, truncate-vs-floor on negatives, Guard redistribution, capacity clamps, the three rounding sites, Scale crossings, shaping order. **Never regenerate a fixture to make a test pass** — a fixture changes only when a Part 12 decision changed the arithmetic, and the commit says which. `channels.ts` is generated by a build step from the canonical `channels.py` data (checked-in generated file + a CI check that regeneration is clean), keeping one source of truth for the 88.

## What the engine explicitly does not know

Users, campaigns-as-rows, HTTP, the database, tunable *storage* (it receives resolved values), the current time (Moments are game-time; `created_at` is the server's business), and anything about React. CI enforces this with a dependency-cruiser rule: `/ruleset` imports nothing outside itself.
