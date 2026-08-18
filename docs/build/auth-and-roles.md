# Auth and roles

## Authentication: magic links, nothing else

No passwords exist anywhere in the system — not stored, not hashed, not reset. Dylan's call, and it also removes an entire class of breach.

**The flow:**

1. `POST /auth/request-link { email }` — always responds 200 identically whether the account exists (no enumeration). If the email matches an **invited or existing** user, a login token is created: 32 random bytes, stored **hashed** (SHA-256) in `login_tokens`, 15-minute expiry, single-use.
2. Email via Resend: "Your Vectus sign-in link" → `https://…/auth/complete?token=…`.
3. `GET /auth/complete` — verifies hash, expiry, unused; marks used; creates a **session**: 32 random bytes, stored hashed in `sessions`, 30-day sliding expiry, bound to a user agent string for display (not enforcement).
4. The client stores the session token and sends it as `Authorization: Bearer …` on HTTP and in the WS hello. Per `../architecture.md` §16's note, auth is token-in-header, never cookie-only — which also keeps the future mobile-wrapper path open.
5. `/settings` lists active sessions; any can be revoked; revocation is immediate (sessions are checked per-request against the DB — at playtest scale a per-request lookup is nothing, and it makes revocation truthful).

**Invite-only.** During the playtest, `POST /auth/request-link` only issues tokens for emails present in `invites` (created by super-admin at `/admin`) or already in `users`. The landing page's "request an invite" writes to an `invite_requests` table for Dylan to review. Open signup is a Phase 7 switch, not a code change.

**Rate limits:** 5 link requests per email per hour, 20 per IP per hour, enforced in the server (a `rate_limits` table; no vendor).

## The role model

Two layers, deliberately small:

**Account-level** — `users.role`:

| Role | Who | Grants |
|---|---|---|
| `user` | everyone | The app |
| `super_admin` | Dylan (and only Dylan, seeded by migration against his email) | Everything: `/admin`, bulk inject, tuning defaults, invites, any campaign read access, base-content authoring. Super-admin actions still flow through the same pipelines as everyone else's — the access is wider, the doors are the same |

**Campaign-level** — `campaign_members.role`:

| Role | Grants |
|---|---|
| `gm` | The GM screen, campaign asset authoring, scene/turn control, Proposals, campaign tunable overrides, inviting members. A campaign can have multiple GMs |
| `player` | The table, their characters, declaring attempts and reactions on what they control |
| `observer` | Read-only presence at the table (a playtester watching) |

**Authorization is one function**: `can(actor, action, resource)` in `/server/authz.ts`, exhaustive-switched over a closed action union, called at every HTTP handler and WS command. No scattered checks — one file, testable as a table.

## The playtest transparency rule (law 1, enforced in authz)

During the playtest era there is **no information hiding between campaign members**: every member — player, GM, observer — reads the full campaign state, every Entity, every Threshold, every log. The `delivery` field exists in the Record shape but is not enforced as a filter (that is Phase 3's job). Concretely: the read-side authz check for campaign data is *membership, nothing finer*. This is a deliberate, documented simplification with one flag (`transparency_mode: 'full'` — a tunable, locked `full` for the beta, same pattern as `bar_visibility`), so release-mode secrecy later is a change of enforcement, not of shape.

**Between campaigns, isolation is real**: members of campaign A read nothing of campaign B. Playtest transparency is within the table, not across the site.

## Provenance — who did a thing

Every Record already carries `actor: { kind: user | system | agent, id }` (`../architecture.md` §10.3). The site enforces:

- Human actions → `kind: "user"` with the user id.
- Engine-driven consequences (Listeners, Decider defaults, timers) → `kind: "system"`.
- **Claude-drafted content injected by Dylan → `kind: "agent"`** with a label naming the session; the publish action itself also records Dylan as the approving super-admin. Nothing an agent drafts reaches players without a human publish click — this is the site-side enforcement of the no-AI-content rule's *audit trail* (the rule itself governs what may be drafted at all: mechanics and data yes; player-facing prose and art, never).
