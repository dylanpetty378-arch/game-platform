# The authoring pipeline

*How everything in the game gets made — features, equipment, abilities, creatures, Thresholds, Settings, Adventures, character-creation flows — whether a GM makes it in the studio or Dylan and Claude design it in chat and inject it. **One pipeline, two doors, identical validation.** This is the load-bearing rule of the whole content system, set by Dylan: super-admin content follows the same process a GM would use — the access is wider, the door is the same.*

## The two hard lines (from the settled design)

1. **Users author instances, never types** (`../substrate-checklist.md` I6). Authorable: Entities with Categories and Attribute values, Thresholds, Enhancement/Participation Capacities, Guards, Standing Order parameters, abilities composed of existing pieces. **Structurally never authorable in the studio**: a Verb, a Dimension, a Layer, a doubloon cost *shape*, a Timing, a Listener template, a **Channel**. The studio's forms make the second list *impossible*, not merely forbidden — there is no UI that could emit one. New types are code, shipped through the `vectus` repo by Dylan.
2. **The no-AI-content rule at the pipeline level**: Claude may draft *mechanics and data* (stat blocks, numbers, Threshold sets, compositions). Player-facing **prose and art are human** — the payload schemas separate `mechanics` from `prose` fields, agent-authored versions with non-empty prose fields fail validation with `agent_prose_forbidden`, and every published version records `authored_by` + a human `approved_by`.

## Asset kinds (the closed union; each has a zod payload schema in `/shared/assets/`)

| kind | What it is | Compiles to |
|---|---|---|
| `feature` | A character option — a named capability with its mechanics | Capacities granted, Specialisations, Bonus Point grants, Listeners from the 7 forms |
| `ability` | An activated action | A cost `{cost, timing, cap}`, vector template(s): Channel + magnitude formula in points, Guards, Repin riders |
| `equipment` | An item | Item-Category Entity template: Tags with magnitudes, Guards, Enhancement/Participation Capacities, ability grants |
| `creature` | A stat block | Creature-Category Entity template: Capacities (the 15), Tracks with maxima, Tags, abilities, standing orders |
| `threshold_set` | A reusable challenge (the lock with its needle) | Thresholds with read modes (sum/highest/each) **and the downside bar the form always offers** |
| `setting` | A world | Its Dynamic Signal color, its asset scope, Place-occupant config, which Tracks attach per-character (`working`/`essence` per Q3.9), tone text (human prose) |
| `adventure` | A run of content | Scenes, Entities, threshold_sets, rails + Decider defaults — the GM-less module machinery (Q4.5) lives here |
| `creation_flow` | Character creation itself, as data | Ordered steps (choose kind → assign Attempt Points → pick features/equipment → …) each referencing asset queries — **so creation is designed in chat and injected as content, not rebuilt as code** |
| `component_config` | Configuration *of* a shipped Component | Only parameters the Component's code declares configurable |

Scopes: `base` (the game itself — super-admin only), `setting` (belongs to a Setting), `campaign` (a GM's homebrew, visible to their table). A campaign's Active Set pins Setting + versions.

## The lifecycle

```
draft ──validate──▶ validated ──publish (human click)──▶ published ──▶ retired
  ▲                    │
  └──── edit = new version; published versions are immutable ────┘
```

**Validate = the expressibility check (L30, realized).** The server compiles the payload into engine terms — the Verbs, vectors, Channels, Tags, Tracks and Listeners it amounts to — using the actual `/ruleset` package, and stores both the compilation and the report. Failure modes are precise, and **classified**, exactly as the phase-map's authoring loop demands:

- `invalid` — schema/reference errors (names a field).
- `misfit:additive` — expressible only with a new Tag/Channel/Track/Moment kind: allowed to publish at `campaign` scope with the misfit flagged; at `base`/`setting` scope it blocks and files the misfit as a finding (a `note` of kind `balance` anchored to the version, surfaced on `/admin`).
- `misfit:structural` — needs an operation outside the Verb shape or a field outside the model: **always blocks, every scope**, files the finding loudly. This is the "stop and say so" rule with teeth.

Publishing additionally: dry-run-resolves each vector template at magnitudes {1, 10, 100} through the pipeline (catches arithmetic surprises), pins the edition/component versions validated against, and requires `approved_by`.

## Door one: the studio (`/studio`, GMs)

Form-per-kind, built from the same zod schemas (schema-driven forms — one renderer, per-kind field configs). Live compilation preview on every change: the right-hand pane shows what the asset compiles to, in engine terms, because law 1 applies to authoring too. The Threshold form's downside-bar field is always present and its omission is counted (the A1 instrument). A "start from" button clones any published asset the author can see.

## Door two: bulk inject (`/admin/inject`, super-admin)

Paste or upload JSON: `{ assets: [{ kind, scope, name, payload, agent_label }] }`. Each item runs the **identical** validate step, the screen shows the per-item report (compilation, misfits, prose violations), and Dylan publishes the passing set with one click — `authored_by: { kind: 'agent', label }`, `approved_by: Dylan`. Items that fail export back as JSON with inline errors, ready to hand back to the drafting chat. The JSON format **is** the zod schemas — `pnpm asset-schema` emits a JSON Schema bundle for any Claude chat to draft against, and that bundle's URL is in the repo README so drafting sessions never guess.

## Components and Settings — how the crucial machinery surfaces

- **Components are code**, one directory each in `/components`, loaded by manifest (`name, version, layers-touched, listeners, configurables`). The site *surfaces* them: `/campaigns/new` and the campaign settings page show the registry, an Active Set editor pins versions, and `component_config` assets carry per-campaign configuration. Depth ≤ 2 and no cross-Component reads are enforced by the manifest loader at boot, not by review.
- **Settings are content** — a `setting` asset plus everything scoped to it. Creating a Setting in the studio is: name it, pick its Signal color (the brand's Dynamic Signal made functional), choose per-character Track attachments, then author or adopt scoped assets. A campaign selects exactly one Setting.
- **Editions** exist in the schema (`records.edition`, pinned per campaign) but only e1 exists; the conversion machinery waits, as designed.
