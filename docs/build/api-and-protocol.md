# The API and the wire protocol

*Hand-typed HTTP + one owned WebSocket protocol. No GraphQL, no tRPC — the surface is small enough to own. Every request body and every WS payload is zod-validated against schemas in `/shared`, which both client and server import, so the types cannot drift. All routes return `{ ok: true, data }` or `{ ok: false, error: { code, message } }` with a closed error-code union.*

## HTTP surface

Auth: `Authorization: Bearer <session token>` on everything except `(public)`.

| Method + path | Who | Does |
|---|---|---|
| `POST /auth/request-link` | public | Magic link flow (`auth-and-roles.md`) |
| `GET  /auth/complete` | public | Token → session |
| `POST /auth/logout` · `GET /auth/sessions` · `DELETE /auth/sessions/:id` | user | Session management |
| `GET  /me` | user | Profile, role, memberships, pending Dispatch count |
| `POST /campaigns` · `GET /campaigns` · `GET /campaigns/:id` · `PATCH /campaigns/:id` | user / member / gm | CRUD-lite; PATCH is name/archive/active-set only |
| `POST /campaigns/:id/members` · `DELETE …/members/:uid` | gm | Invite by email (creates `invites` row if needed), remove |
| `GET  /campaigns/:id/state?at_seq=` | member | The folded state (optionally at a past seq — time travel) |
| `GET  /campaigns/:id/records?from=&to=&filters…` | member | Ledger reads for the log browser |
| `GET  /campaigns/:id/records/:seq/expansion` | member | The full slot-by-slot resolution expansion |
| `GET  /campaigns/:id/export` | member | The complete canonical-JSON Ledger export (streamed) — byte-stable, re-importable |
| `POST /campaigns/:id/import` | super_admin | Re-import an export into a fresh campaign (test/fork tool) |
| `POST /characters` · `GET /characters/:id` · list | owner/member | Sheet metadata; creation drives WS commands for the Ledger side |
| `GET  /assets?kind=&scope=&…` · `GET /assets/:id` | user | Library browsing (published versions; drafts visible to their authors/scope) |
| `POST /assets` · `POST /assets/:id/versions` · `POST /assets/:id/versions/:v/validate` · `…/publish` · `…/retire` | gm / super_admin | The authoring pipeline (`authoring-pipeline.md`) |
| `POST /admin/inject` | super_admin | Bulk asset JSON → same validate/publish pipeline, per-item report |
| `GET/PUT /tunables` · `GET/PUT /campaigns/:id/tunables` · `GET /tunables/history` | user reads; gm writes overrides; super_admin writes defaults | Law 2 |
| `POST /events` | user | Batched playtest UI events (law 3) — fire-and-forget, ≤50/batch |
| `POST /notes` · `GET /notes?anchor…` · `PATCH /notes/:id` | user | Anchored notes |
| `GET  /admin/*` (invites, users, analysis queries) | super_admin | Admin surfaces |
| `GET  /healthz` | public | DB reachable, migrations current, version hash |

Explainer content is static (built into the SPA); no API.

## The WebSocket protocol *(pre-code spec #4, now law)*

One WS connection per client, multiplexing all of that client's campaigns. Envelope, both directions:

```ts
{ v: 1, id: string, type: string, payload: unknown }
// id: client-generated ulid on client→server messages; echoed on replies.
```

**Client → server**

| type | payload | semantics |
|---|---|---|
| `hello` | `{ token, resume: { campaignId, lastSeq }[] }` | Authenticates the socket; requests resume per campaign |
| `subscribe` | `{ campaignId }` | Join a room (authz: membership) |
| `command` | `{ campaignId, expectedSeq, idempotencyKey, intent }` | The only way game state changes. `intent` is a closed union (`declare_attempt`, `allocate`, `join_attempt`, `declare_threshold`, `place_vector`, `decide`, `enter_ordered_time`, `gm_create_entity`, …) — the server validates against authz + the fold, converts to Record(s), appends at `expectedSeq+1` |
| `ping` | `{}` | Heartbeat (client every 25s; server closes at 60s silence) |

**Server → client**

| type | payload | semantics |
|---|---|---|
| `welcome` | `{ userId, resumed: {campaignId, fromSeq}[] }` | Post-hello |
| `records` | `{ campaignId, records: Record[] }` | The stream — in seq order, gapless. **This is the only state-bearing message**; clients fold locally with the same engine package |
| `presence` | `{ campaignId, online: userId[] }` | Who's at the table |
| `reply` | `{ id, ok, error?, seq? }` | Command outcome; `seq` = the appended Record's seq |
| `error` | `{ id?, code, message }` | Protocol errors; `code ∈ {unauthorized, bad_message, conflict, halted, rate_limited}` |

**Reconnect/resync** — the whole spec, and it is small because the per-campaign `seq` is gapless: on reconnect the client sends `hello.resume` with the last seq it folded per campaign; the server replies with every record after it (chunked ≥1000), then live-streams. A client with no local state sends `lastSeq: 0` and receives the full ledger (or calls the HTTP state endpoint for a fast first paint, then subscribes from that seq). There is no other sync path, no snapshot negotiation, no vector clocks — gapless seq is the entire algorithm.

**Optimistic prediction** — the client may apply a command's expected Records locally (same engine, `step`) tagged provisional; the authoritative `records` stream overwrites on arrival; a `reply` with `conflict` (someone else appended first) drops provisional state and the client refolds from the stream. This is §10.5/§10.6's "the two good ideas from local-first, taken free."

**Idempotency** — the server keeps `(campaignId, idempotencyKey) → seq` for 24h; a retried command returns the original reply instead of double-appending. Keys are ulids minted per user action, surviving reconnects.

**Ordering guarantees** — per campaign: total order by seq, exactly the append order. Across campaigns: none, by design.
