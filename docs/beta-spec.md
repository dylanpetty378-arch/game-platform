# The Beta — the developer playtest build

*Written August 2026, when Phase 2 changed from paper to software. This is the spec for the first thing ever built: a website where the game is played by the people making it. `phase-map.md` says why the phase exists; this document says what the build is.*

**Why the paper phase died:** nobody can run the vector arithmetic by hand and still have a great time. A paper trial would test a simplification of the pipeline, and its findings would not transfer. So the trial happens where the game actually lives — and the build's whole personality follows from who it is for: **the developers of the game.** Dylan, and the playtesters working with him. Not customers. Not strangers. Nothing about it is a product.

---

## The three laws

Everything in this document is one of these three, worked out.

**1 · Everything is visible.** Nothing hidden in the slightest. Every bar, every pending vector, every slot of every resolution, the state of every Track on every Entity, the tuning values currently in force. This build is more transparent about what it is doing and tracking than anything — that is its reason to exist. Hidden information is a *release-mode* feature (the near-miss reveal is the leading candidate, per Q4.2), designed later, against this build's logs.

**2 · Everything provisional is a hard-labeled PLAYTEST tunable, changeable on the fly.** A developer changes the dice mid-session and the very next attempt uses them. Every tunable is visibly marked `PLAYTEST` in the interface wherever its value appears, so nobody — including a future session of Claude — mistakes a knob for a decision.

**3 · Every log lands in the database.** The Ledger is already append-only history; the beta logs everything *around* it too — button presses, allocation timings, tuning changes, session boundaries — because the balance and comprehension questions get answered by analysis, not recollection.

---

## Three kinds of value, permanently distinct

| Kind | Examples | Can the console change it? |
|---|---|---|
| **Frozen Substrate** | the Verb shape · the 41 slots · the three rounding sites · cascade depth 32 · integer apportionment · determinism rules | **Never.** Not a dial, not in the beta, not ever. If play makes one of these look wrong, that is a *structural finding* — stop and say so, per CLAUDE.md |
| **Settled Ruleset lists** | the 14 Dimensions · the 88 Channels · the 14 Tracks and their bands · the attempt Domains | Not from the console. Changing these is content work with its own additive-only discipline — though the beta may *display* proposals |
| **PLAYTEST tunables** | everything in the registry below | **Yes — mid-session, logged, labeled** |

The line matters because the beta will make twiddling cheap, and the one thing cheap twiddling must never touch is the part that can never be revised.

## The tunables registry

Seed set, August 2026. The registry is additive: any developer may add a tunable, and every tunable must be registered here, labeled in the UI, and logged on change. Defaults are Dylan's calls.

| Tunable | Default | Form | Notes |
|---|---|---|---|
| `attempt_roll` | **d100, rolled as two d10s** | any dice expression | d20 is the named alternate. The console accepts arbitrary expressions (`3d6`, `2d10`, `d20`, `4dF`…) because comparing feels is the point. This is a stand-in for the Resolution occupant's final formula, which still must publish its distribution when it is chosen |
| `attempt_points` | **5** | integer ≥ 1 | Scales with the character eventually — start near 3, grow to as many as the character can use; the curve belongs to character creation. Per-character override supported |
| `turn_allowance` | **20** doubloons | integer ≥ 1 | Scales with level and character eventually. Per-character override supported |
| `price_ladder` | basic action 8 · reaction 5 · interrupt 8 · big swing 15 | integers | First guesses against the 20-doubloon turn; exists to be wrong. Every authored cost in beta content references a ladder entry so retuning is one change |
| `bar_visibility` | **full** | full · near-miss-reveal · hidden | **Locked to `full` for the beta** (law 1). The other modes exist in the enum so release-mode candidates can be trialed deliberately, late, as an experiment — never by accident |
| `participation_order` | declaration | — | Settled (Q3.7), surfaced here so the loose-time nimbleness tiebreak can be watched |
| `reserve_on_declaration` | **on** | on · off | The Q3.6 double-spend answer, provisional: a spend from a shared Track is held at declaration |
| `specialisation_bonus` | 3 | integer | Bonus Points a Specialisation grants in scope |
| `enhancement_default` | 100% | percentage | The Enhancement Capacity a thing has when content declares none |
| `participation_default` | 2 | integer | The Participation Capacity when content declares none |

## The developer playtest page

What a session actually looks at. Deliberately ugly — a developer tool should look like one; attachment to this interface is a bug.

- **The three character sheets** — person, ship, faction. The Phase 1 debt, discharged where it is naturally due, and still the kind-agnosticism test: the values all three need are the Capacity set, and the ones only a person needs reveal whether the Substrate is honest.
- **The attempt interface.** Attempt Point buttons per Dimension; the GM names the Domain (or a Dimension, which is harder); at least one point must land inside it. Contributors join in declaration order — **when a capped stat fills, its button disables**; the other stats of the party-sized roll stay open. Outside Ordered time, simultaneous declarations break by nimbleness (the MOVEMENT Dimensions), then the stable key.
- **The resolution expansion, open by default.** Every resolution showing every slot: the roll, the apportionment, each modifier and its source, the clamp, Scale conversion, each Guard's bite, cancellation, landing, each Track pushed and its band before and after. *Why was it 17* should never take ten seconds here, because the answer is already on screen.
- **The GM panel.** Declare Entities, Thresholds and vectors mid-session. The Threshold form always offers the downside-bar field — and **counts every Threshold shipped without one**, because that omission rate is the A1 all-in answer being tested.
- **The tuning console.** The registry above, live. Every change writes who, what, old → new, when, and against which session.
- **The log browser.** The Ledger and the event log, searchable, in the same page.

## The logging spec

Two stores, one database:

- **The Ledger** — the game itself, exactly per the architecture: append-only Records, per-Campaign, server-folded. The beta writes nothing to a Record payload that the release engine would not (and PII never — rule 10).
- **The playtest event log** — everything around the game: UI events (button presses with timestamps, allocation started/committed), tuning changes, session boundaries, participant identities, free-text notes anchored to a Record or a slot. Separate tables, joinable to the Ledger by Record id, and explicitly *not* part of folded state — throwing the event log away must never change a fold.

**The measurements the logs must support from day one** — these are the phase's actual questions:

| Measurement | Answers |
|---|---|
| time from attempt-opened to allocation-committed | A9 — is splitting attention a decision or homework |
| time from Threshold-form-opened to declared | A11 — can a GM invent bars in the ten seconds a table will wait |
| Thresholds declared without a downside bar | A1 — does the all-in answer hold with real GMs |
| arrivals-per-Moment per creature | Q3.5 — whether turn position skews defensive load, which Dylan disputes; the data decides |
| tuning-change history vs session feel notes | Q2.10, Q3.1, L28 — what the dice, point and allowance numbers should actually be |
| every resolution's full expansion, retained | balance work, and the L6 closing procedure's raw material |

## What the beta pulls forward from the Spike

*(The implementation blueprint for all of this — and for the full website around it — is `build/`, starting at `build/README.md`. This document stays the behavioral spec; `build/` is the how.)*

The engine core, because the beta cannot exist without it: the Ledger (append-only, per-Campaign, the settled Postgres shape), **server-side folding from the first commit** (clients render; the server is authoritative — Q3.4's non-deferrable half), the uniform Verb shape, Moments and the timing machinery, Deciders with defaults, the resolution pipeline for the slots play actually exercises (the 41-slot numbering reserved in full, occupied as needed), and minimal Place and Resolution occupants. CLAUDE.md's working rules apply in full — spec first, strict TypeScript, no floats, the three rounding sites, golden fixtures seeded from `phase-0-checks.py`.

**What stays in Phase 3:** the cross-machine determinism harness, export/import round-tripping, time travel, what-if, the state inspector's full form, `delivery` and real hidden information, and the four pre-code specs made law. The beta may take on one server what Phase 3 must then prove everywhere.

## What the beta is not

Not the product. Not pretty — the Vectus identity (`brand-identity.md`) deliberately does not apply here; the first branded surface is the public one. Not hidden-information play. Not the Resolution occupant's final formula. Not multi-campaign scale, not accounts hardening, not mobile. Every one of those has a phase, and it is not this one.

## The gate

Unchanged from the phase it replaced: **a group asks to play again without being asked.** The async play-by-post trial runs in this same build — it is the business bet, and a spreadsheet cannot track the layers.
