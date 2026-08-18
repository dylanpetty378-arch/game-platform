# The database

*One PostgreSQL database. The `records` event store is the heart and comes verbatim from `../architecture.md` §10.3; everything else here is the site around it. Conventions: `uuid` PKs via `gen_random_uuid()` except where a natural key exists; `timestamptz` everywhere; `jsonb` payloads always validated by a zod schema in `/shared` before insert — the DB trusts the app layer, the app layer trusts nothing. All DDL below is the actual migration content, in order.*

## Migration 001 — identity and access

```sql
create table users (
  id           uuid primary key default gen_random_uuid(),
  email        text not null unique,          -- lowercased at the boundary
  display_name text not null default '',
  role         text not null default 'user' check (role in ('user','super_admin')),
  created_at   timestamptz not null default now()
);

create table invites (
  email       text primary key,
  invited_by  uuid not null references users(id),
  note        text not null default '',
  created_at  timestamptz not null default now()
);

create table invite_requests (
  email      text primary key,
  message    text not null default '',
  created_at timestamptz not null default now(),
  handled    boolean not null default false
);

create table login_tokens (
  token_hash  bytea primary key,              -- sha256 of the raw token
  user_email  text not null,
  expires_at  timestamptz not null,
  used_at     timestamptz
);

create table sessions (
  token_hash  bytea primary key,
  user_id     uuid not null references users(id) on delete cascade,
  user_agent  text not null default '',
  created_at  timestamptz not null default now(),
  last_seen   timestamptz not null default now(),
  expires_at  timestamptz not null
);
create index on sessions (user_id);

create table rate_limits (
  bucket     text not null,                   -- e.g. 'link:email:x@y.z' or 'link:ip:1.2.3.4'
  window_start timestamptz not null,
  count      int not null default 0,
  primary key (bucket, window_start)
);
```

## Migration 002 — campaigns and membership

```sql
create table campaigns (
  id          uuid primary key default gen_random_uuid(),
  name        text not null,
  setting_id  uuid,                           -- references assets(id); nullable until Settings exist
  active_set  jsonb not null,                 -- { edition: 1, components: { "<name>": "<version>" } }
  created_by  uuid not null references users(id),
  created_at  timestamptz not null default now(),
  archived_at timestamptz
);

create table campaign_members (
  campaign_id uuid not null references campaigns(id) on delete cascade,
  user_id     uuid not null references users(id) on delete cascade,
  role        text not null check (role in ('gm','player','observer')),
  joined_at   timestamptz not null default now(),
  primary key (campaign_id, user_id)
);
create index on campaign_members (user_id);
```

## Migration 003 — the event store (verbatim shape from `../architecture.md` §10.3)

```sql
create table records (
  campaign_id      uuid    not null,
  seq              bigint  not null,          -- gapless per campaign; the PK does the concurrency work
  type             text    not null,
  version          int     not null,
  payload          jsonb   not null,
  actor            jsonb   not null,          -- { kind: 'user'|'system'|'agent', id, label? }
  causation_id     uuid,
  correlation_id   uuid,
  moment           text    not null,
  tick             int     not null,
  delivery         jsonb,                     -- present in shape; unenforced in playtest (auth-and-roles.md)
  edition          int     not null,
  component_version text   not null,
  tx_id            xid8    not null default pg_current_xact_id(),
  created_at       timestamptz not null default now(),
  primary key (campaign_id, seq)
) partition by hash (campaign_id);
-- 8 hash partitions records_p0..p7 created in the same migration.
```

Append is `insert … values (:campaign, :expected_seq, …)` — a unique-violation means a concurrent writer won; the server refetches and retries the command against the new head (or rejects, per command semantics). **Fold on read** (`../architecture.md` §10.3): the server folds a campaign's records through the pure ruleset Fold to answer state queries, with an in-memory per-room cache of `(seq, folded_state)` so live play folds incrementally — cache, not projection; losing it costs a refold, never correctness. No async projection daemon, ever, until measurement demands an inline (same-transaction) projection.

**Record `type` namespace** (closed union in `/shared/records.ts`): the seven Verbs (`verb.push`, `verb.set`, `verb.place`, `verb.repin`, `verb.link`, `verb.create`, `verb.decide`), plus `resolution` (the full attempt result — inputs stored; the slot-by-slot expansion is *derived* by the engine, never stored), plus lifecycle types (`campaign.configured`, `scene.opened`, `ordered_time.entered`, `proposal.opened`, …). Adding a type is additive; changing one bumps its `version` with an upcaster in `/ruleset`.

## Migration 004 — characters (the sheet's metadata; the character itself is an Entity in the Ledger)

```sql
create table characters (
  id           uuid primary key default gen_random_uuid(),
  campaign_id  uuid not null references campaigns(id) on delete cascade,
  entity_id    bigint not null,               -- the in-Ledger Entity id
  owner_id     uuid references users(id),     -- null for GM-run creatures
  name         text not null,                 -- display convenience; the Ledger holds truth
  kind         text not null default 'person' check (kind in ('person','ship','faction','creature')),
  created_at   timestamptz not null default now(),
  unique (campaign_id, entity_id)
);
```

## Migration 005 — the asset pipeline (`authoring-pipeline.md` is the behavior spec)

```sql
create table assets (
  id          uuid primary key default gen_random_uuid(),
  kind        text not null,                  -- closed union: see authoring-pipeline.md §Kinds
  scope       text not null check (scope in ('base','setting','campaign')),
  campaign_id uuid references campaigns(id) on delete cascade,  -- required iff scope='campaign'
  setting_id  uuid,                           -- required iff scope='setting'
  name        text not null,
  slug        text not null,
  created_by  uuid not null references users(id),
  created_at  timestamptz not null default now(),
  scope_key   text generated always as (coalesce(campaign_id::text, setting_id::text, 'base')) stored,
  constraint scope_shape check (
    (scope = 'campaign' and campaign_id is not null) or
    (scope = 'setting'  and setting_id  is not null) or
    (scope = 'base'     and campaign_id is null and setting_id is null)
  )
);
create unique index assets_slug_unique on assets (kind, scope, scope_key, slug);

create table asset_versions (
  asset_id    uuid not null references assets(id) on delete cascade,
  version     int  not null,
  status      text not null check (status in ('draft','validated','published','retired')),
  payload     jsonb not null,                 -- the authored content, per-kind zod schema
  compiled    jsonb,                          -- expressibility output: engine terms it compiles to
  validation  jsonb,                          -- full expressibility report incl. misfit classification
  authored_by jsonb not null,                 -- { kind:'user'|'agent', id, label? } — agent = Claude draft
  approved_by uuid references users(id),      -- required to reach 'published'
  created_at  timestamptz not null default now(),
  primary key (asset_id, version)
);
create index on asset_versions (status);
```

Published versions are immutable — a change is a new version. A campaign's Active Set pins asset versions the way it pins Component versions, so a later edit never rewrites a running game.

## Migration 006 — tunables (the registry from `../beta-spec.md`, made storage)

```sql
create table tunable_defaults (
  key        text primary key,                -- 'attempt_roll', 'attempt_points', ...
  value      jsonb not null,
  updated_by uuid not null references users(id),
  updated_at timestamptz not null default now()
);

create table tunable_overrides (
  campaign_id uuid not null references campaigns(id) on delete cascade,
  key         text not null,
  value       jsonb not null,
  updated_by  uuid not null references users(id),
  updated_at  timestamptz not null default now(),
  primary key (campaign_id, key)
);

create table tunable_changes (                -- append-only audit; law 2's memory
  id          uuid primary key default gen_random_uuid(),
  campaign_id uuid,                            -- null = default changed
  key         text not null,
  old_value   jsonb,
  new_value   jsonb not null,
  changed_by  uuid not null references users(id),
  changed_at  timestamptz not null default now()
);
```

Resolution order: campaign override → default → the registry's hard-coded seed (in `/shared/tunables.ts`, which also carries each key's zod schema and PLAYTEST label text). **The engine never reads these tables** — the server resolves tunables and passes them as explicit fold/resolve inputs, recorded into the triggering Record's payload so history refolds identically forever even after a knob moves.

## Migration 007 — the playtest event log (law 3) and notes

```sql
create table playtest_events (
  id          bigint generated always as identity primary key,
  campaign_id uuid,
  user_id     uuid,
  session_key uuid,                            -- groups one sitting
  type        text not null,                   -- 'ui.attempt_opened','ui.allocation_committed','ui.button_pressed',
                                               -- 'ui.threshold_form_opened','ui.threshold_declared','tuning.changed',
                                               -- 'session.started','session.ended','page.viewed', ...
  record_ref  bigint,                          -- records.seq it relates to, if any
  payload     jsonb not null default '{}',
  at          timestamptz not null default now()
);
create index on playtest_events (campaign_id, at);
create index on playtest_events (type, at);

create table notes (
  id         uuid primary key default gen_random_uuid(),
  author_id  uuid not null references users(id),
  kind       text not null check (kind in ('bug','balance','confusion','idea')),
  body       text not null,
  anchor     jsonb not null,                   -- { campaign_id?, record_seq?, entity_id?, slot?, asset_id?, route? }
  created_at timestamptz not null default now(),
  resolved_at timestamptz
);
```

Explicitly **not** part of folded state: deleting every `playtest_events` row must never change a fold — CI asserts the engine package has no import path to any of this.

## Measurements — the saved queries `/admin/analysis` ships with

- **A9** — decision time: per attempt, `allocation_committed.at − attempt_opened.at`, distribution over time and per player.
- **A11** — GM Threshold authoring time: `threshold_declared.at − threshold_form_opened.at`.
- **A1** — downside-bar omission: share of `threshold_declared` events whose payload lacks a downside bar, per GM, trend.
- **Q3.5** — arrivals-per-Moment per creature: from `records` where type `resolution`/`verb.push`, grouped by target entity and moment; joined against initiative position to test Dylan's no-skew claim.
- **Tuning vs feel** — `tunable_changes` timeline overlaid with `notes` (kind `balance`/`confusion`) in the same sessions.

## What is deliberately absent

Snapshots, async projections, read replicas, a second datastore, soft-delete flags on everything (append-only where it matters, real deletes where it doesn't — accounts honor deletion by anonymizing `users` and leaving Records' actor ids dangling-by-design), and any table the playtest era has no reader for. Dispatches (the async play digest) get their table when M8 builds them — schema sketched in `build-order.md`, not created before its milestone.
