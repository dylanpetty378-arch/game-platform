# Site map — every surface of the Vectus website

*Who sees what, and what each page does. Routes are the SPA's client routes; `(public)` needs no login. Visual language: `../brand-identity.md` — Void background, Paper text, Signal accents, Space Grotesk display / Inter body, the play-register vocabulary only on player-facing surfaces. During the playtest era every page carries the **PLAYTEST ribbon**: a thin Signal-colored banner stating "Playtest build — every number can change, everything is visible, everything is logged."*

## Public (no login)

| Route | Page | What it does |
|---|---|---|
| `/` | **Landing** | The brand board made real: the mark, "Your Story. Your World. Your Way.", the essence statement, the eight steps as a horizontal strip, the no-AI statement linked in the footer, and one CTA: *Request an invite* (playtest era — accounts are invite-only) |
| `/learn/*` | **How Vectus Works** | The rules explainer — the whole system, nitty-gritty and all, with live widgets running the real engine. Fully specced in `rules-explainer.md`. This is the biggest public surface and it is public *on purpose* |
| `/about` | About + no-AI statement | The published statement from `../brand-drafts.md`, dated; who is building this and why |
| `/legal/*` | Terms, privacy | Plain-language; the privacy page states exactly what the playtest logs record (everything) and why |
| `/login` | **Login** | One email field → "check your email" → magic link completes. No passwords exist anywhere |

## App (logged in)

| Route | Page | Who | What it does |
|---|---|---|---|
| `/home` | **Dashboard** | all | Your campaigns, your characters, pending Dispatches ("what's waiting on you"), invites |
| `/campaigns/new` | Create campaign | any user | Name, Setting, Active Set (edition + Component versions — pre-filled with the only ones that exist), invite players by email |
| `/c/:id` | **Campaign hub** | members | Roster, characters, session scheduler, campaign log (the Chronicle's ancestor), campaign settings, export button |
| `/c/:id/play` | **The table** | members | The live play surface: scene state, every Entity's full state (law 1 — Tracks with bands, Capacities, Tags, links, pending vectors, all visible to everyone in the playtest), the attempt interface (Attempt Point buttons per Dimension, GM-named Domain highlighted, declaration-order joining, cap-disabled buttons), the event log rail (color-coded, per the brand's UI mock), the doubloon budget bar, and the **resolution expansion** — every resolution opens to all its slots, by default |
| `/c/:id/gm` | **GM screen** | gm | Everything on the table *plus*: declare Entities/vectors/Thresholds mid-session (Threshold form always offers the downside bar and counts omissions — the A1 instrument), scene and turn management (enter/leave Ordered time, per Q3.3's rule plus manual initiation), Proposal management (Deciders, timers, defaults), and the campaign's asset library |
| `/characters/new` | **Character creation** | all | The guided flow. **The rules of character creation do not exist yet** — this page is built as a shell over the authoring pipeline: it composes a Creature-category Entity from published assets (features, equipment, abilities) with Attempt Points and Tracks per the settled model, and its steps are driven by a `creation_flow` asset so Dylan + Claude can design creation in chat and inject it as content, not code |
| `/characters/:id` | **Character sheet** | owner + campaign | The person sheet (ship and faction sheets are the same component with a different Category bundle — the kind-agnosticism test made UI). Everything visible; every derived number expandable to its sources |
| `/library` | **Asset library** | all | Browse published assets: features, equipment, abilities, creatures, Thresholds, Settings, Adventures. Filter by kind, Setting, author. Every asset shows its full engine compilation (law 1) |
| `/studio/*` | **The authoring studio** | gm + super-admin | Create and edit assets — fully specced in `authoring-pipeline.md`. Draft → validate → publish, with the expressibility check inline |
| `/settings` | Account | all | Email, display name, sessions/devices, data export, delete account |

## Developer & playtest surfaces (every logged-in user in the playtest era; role-gated later)

| Route | Page | What it does |
|---|---|---|
| `/c/:id/inspect` | **State inspector** | Any Entity, any Moment: fold-to-Moment and look around (time travel, read-only) |
| `/c/:id/logs` | **Log browser** | The Ledger and the playtest event log, searchable — by Entity, Moment, Verb, actor, Record type |
| `/tuning` | **Tuning console** | The tunables registry from `../beta-spec.md`, live: current values, per-campaign overrides, change any of them, full change history. Every value marked `PLAYTEST` |
| `/c/:id/whatif` | What-if *(Phase 3 completes it; a stub exists from M6)* | Re-resolve a past resolution with one input changed; never writes |
| `/notes` | Notes | Notes anchored to Records/Entities/slots, kinds: bug · balance · confusion · idea |

## Super-admin (Dylan only)

| Route | Page | What it does |
|---|---|---|
| `/admin` | **Admin home** | Invites (create/revoke), users, campaigns overview, deploy freeze, feature flags |
| `/admin/inject` | **Bulk inject** | Paste or upload Claude-drafted asset JSON; it runs the *identical* validation pipeline a GM's form submission runs (`authoring-pipeline.md` — this is the load-bearing rule), shows the expressibility report per asset, then publishes in bulk with `actor.kind = "agent"` provenance |
| `/admin/analysis` | **Measurements** | The saved queries from `database.md`: A9 decision time, A11 GM Threshold time, A1 downside-bar omission rate, Q3.5 arrivals-per-Moment, tuning history vs session notes |

## Explicitly not in the playtest build

Payments and tiers (Phase 8) · marketplace (Phase 8) · hidden-information play and `delivery` filtering (Phase 3+) · mobile apps (the SPA is responsive; wrappers are Phase 7 per `../architecture.md` §15) · public signup without an invite (open beta is Phase 7) · forums/social (Discord fills this for the playtest).
