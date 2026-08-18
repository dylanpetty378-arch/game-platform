# Template: the `CLAUDE.md` for the `vectus` code repository

*Copy everything below the line into the new repo's root `CLAUDE.md` at M0. It extends — never replaces — the design corpus's working rules: `game-platform/docs` remains the source of truth for what the game IS; this file governs how code gets written.*

---

# CLAUDE.md — working rules for the Vectus codebase

**What this is:** the website and engine for Vectus, the tabletop RPG that is its own platform. The design lives in the `game-platform` repo (public), pinned at the commit named in README.md. The build blueprint is `game-platform/docs/build/` — read its README first, then `build-order.md`, then come back here. `PROGRESS.md` says where the build stands; keep it true.

## The rules that are law

1. **Vocabulary is law.** Every term from `dictionary.md`, used exactly, in identifiers too: it is `attemptPoints`, `doubloons`, `Track`, `Moment`, `Repin` — never `actionPoints`, `gold`, `stat`, `tick2`, `reschedule`. A concept that needs a word the dictionary lacks is a finding — write it up, don't coin silently.
2. **Two registers.** Engine/server code speaks the engine register. Player-facing strings speak the play register (`brand-identity.md`: the eight steps, vector, magnitude, chance). Never mix them in one surface.
3. **`/ruleset` is pure. Absolutely.** No I/O, no imports outside itself, no `Date.now`, no `Math.random`, no floats, no `try/catch`-and-continue. The dependency-cruiser rule enforcing this is CI law; if a task seems to need to break it, the task is misdrawn — stop and re-read `engine-spec.md`.
4. **No floats anywhere in game arithmetic.** Integers, `truncDiv` toward zero, exactly three rounding sites (R-400, R-750, R-1050). The eslint rule backs this; don't argue with it, and never "just use a float briefly."
5. **Spec first.** Any unit worth more than an hour gets a prose spec in `/spec` before implementation — what it does, its boundaries, its failure modes. The build docs are the outer specs; `/spec` refines them.
6. **Fixtures never bend.** The determinism fixtures and phase-0 ports change only when a Part 12 decision changed the arithmetic, and the commit message cites the decision. A red fixture means the code is wrong.
7. **Misfits are findings.** If content, a feature, or a page cannot be expressed inside the settled model, classify it — additive or structural — write it as a finding against the corpus (a note, and tell Dylan), and do not work around it. The rule that built the design keeps building the site.
8. **The three laws of the playtest build** (`beta-spec.md`): everything visible; every provisional number a hard-labeled PLAYTEST tunable, changeable live, logged on change; every log to the database. Every new surface is checked against all three before it merges.
9. **One pipeline for content.** Anything that creates game content goes through the asset pipeline (`authoring-pipeline.md`) — including super-admin and agent-drafted content. Never add a side door, including "just this once" seed scripts: seeds call the same validator.
10. **Agent-drafted ≠ player-facing.** Claude drafts mechanics and data; player-facing prose and art are human-approved, enforced by schema (`agent_prose_forbidden`) and by `authored_by`/`approved_by` provenance. This is a founding rule of the project, not a style preference.
11. **Server is authoritative.** Clients predict optimistically with the same engine and are overwritten by the `records` stream. No client-trusted state, ever.
12. **Secrets never in the repo.** Env vars validated at boot; Fly/Actions secrets only.

## How to work

- **Session start:** read `PROGRESS.md`, run `pnpm test`, confirm green before touching anything.
- **Session end:** typecheck, tests, lint, fixtures all green → update `PROGRESS.md` (what was done, what is next, any findings) → commit and push. A session that can't get green documents exactly what is red and why in `PROGRESS.md` before stopping.
- **Commits:** small, present-tense, cite the build doc or spec section they implement (`M4: attempt interface — beta-spec.md developer page, items 2–3`).
- **Stack discipline:** the choices in `stack-and-hosting.md` are made. No new frameworks, no ORMs, no state-management libraries, no CSS systems without a written case to Dylan first. Boring is a feature; Tier 3 stays empty.
- **Testing:** engine logic → fixtures and property tests (fast-check for apportionment/guards invariants). Server → integration tests against real Postgres (the compose one). Client → component tests for the attempt interface and expansion; a Playwright smoke of the M4 scripted scene.
- **When the docs conflict** (corpus vs build docs vs code): corpus wins, then build docs, then code — and the conflict itself gets reported to Dylan and fixed at the highest level it exists.

## The scripted scene (the repo's heartbeat test)

Two players and a GM: open a scene → GM declares the lock (threshold_set with downside bar) → player A attempts (5 Attempt Points split, d100), resolution expands → enemy vector at player B → B reacts (respond timing, doubloons spent) → A Repins an incoming blow (cost named) → a Proposal times out to its default → Ordered time exits. Runs as a Playwright test from M4 on; every milestone after must keep it green. It is the whole game in one minute, and it is the demo Dylan shows people.
