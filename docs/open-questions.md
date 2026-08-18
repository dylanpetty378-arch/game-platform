# Open Questions

*Everything not yet decided, in one place, organised by when it has to be answered.*

Every question here gives: **what it is**, **why it matters**, **what is blocked by it**, **the options with their consequences**, and **a lean** where I have one. A lean is a recommendation, not a decision.

Where a question was already answered elsewhere and only *looks* open, it is not in this document. Where a question is genuinely unanswerable without playing the game, it says so.

**Five parts, in the order the answers are needed:**

| Part | | Blocks |
|---|---|---|
| **1** | Repair decisions | ~~Everything~~ — **CLOSED August 2026.** Record in `work-repair.md` |
| **2** | Decisions made while filling the lists | Phase 1 |
| **3** | Decisions needed before any code | Phase 3 |
| **4** | Decisions needed before content and launch | Phases 6–8 |
| **5** | Questions only Dylan can answer | The shape of the product and the business |

---

# Part 1 — Repair decisions — ~~OPEN~~ **CLOSED, August 2026**

**All of Part 1 is answered.** Q1.1 through Q1.5 were the four foundation findings plus the determinism set, and every one is now decided, recorded in `dictionary.md` Part 12 with its reasoning, and covered by a numeric test in `phase-0-checks.py`.

The full record of what was decided and why is **`work-repair.md`**. In one line each:

| | Was | Now |
|---|---|---|
| **Q1.1** Do whole Attempt Points survive? | Granularity waste and all-in dominance | **Yes.** Resolution is one integer operation, `⌊points × magnitude ÷ total points⌋`. All-in is answered by requiring a downside bar in authored content, not by changing the arithmetic |
| **Q1.2** What bounds standing self-scoped vectors? | Nothing | **Content pricing, not an engine limit.** R-780 reserved as insurance, unbounded in v1 |
| **Q1.3** Can an interior Channel ever be worth placing? | No — pure was 7× better | **Yes.** A universal flat Guard now acts on the packet total and is redistributed. Every direction lands the same |
| **Q1.4** Where does Enhancement Capacity clamp? | Three holes | **Percentages, and only percentages.** Absolutes are bounded by Participation Capacity instead. Baselines are stated in points and their inflation is clamped by the same Capacity (summed-Baseline ceiling open — Q3.2). The ceiling belongs to the task, never the source |
| **Q1.5** The determinism set | Four undeclared rules | **All four declared.** Apportionment dissolved; three rounding sites (R-400, R-750, R-1050), all truncating toward zero; Shaping is stated in points, has two forms, and runs Bonus Points → Baseline; log-integers are never added |

**One question was promoted into this phase and answered with it.** A17, crossing Scales, was ranked Medium and turned out to be Substrate: a default conversion rule now ships at R-750, and **Scale belongs to the part as well as the whole** — a Scale-4 airship has Scale-1 doors and rigging, and the Scale that applies is the Scale of the thing actually targeted.

**What is still open from this territory, deliberately:**

- **How many Attempt Points a character has, and where they come from.** Belongs to L29 and to beta play — see Q3.1.
- **Whether the Shaping order feels right.** Arithmetically arbitrary, so only play can say. On the playtest watchlist.
- **Whether the all-in authoring requirement holds at a live table.** Instrumented rather than assumed: the tooling counts tasks that ship with no downside bar.

---

# Part 2 — Decisions made while filling the lists — **CLOSED, August 2026**

**Every list is settled except L6, which is drafted at seven and closes in Phase 2 against real content, and L4, which is provisional at twenty-four and also closes against content.** The arguments are in `list-log.md`; the one-line reasons are in `dictionary.md` Part 12.

| | Answer |
|---|---|
| **Q2.1** Capacities | Became **L29**: seven attempt Domains, fifteen attempt Dimensions, Specialisations as a third layer |
| **Q2.2** Dimension Spaces | **Five** — physical, mental, social, mystic, attempt. A Space limits a *vector*, never an ability |
| **Q2.3** The Socket list | **Two: Place and Resolution.** Time and Budget became Substrate; Landing was retired when the Track merge removed its job |
| **Q2.4** The Economy | **One unit, the doubloon.** A cost is `cost` · `timing` · `cap`. No denominations, nothing divides |
| **Q2.5** Listener cascades | Depth **32** · **halt and write a Record** at the limit · order by semantic class then `(layer, component_id, listener_id, target_entity_id)` |
| **Q2.6** Aggregation | Collapsed with the Track merge: Track clamps · Tag membership unions and magnitudes add · Capacity needs none · Relationship never merges |
| **Q2.7** Timing carry-overs | Four timings — `own`, `any`, `respond`, `interrupt` — with `trigger` as a separate optional field |
| **Q2.8** Is the Verb set complete? | **Still open, deliberately.** Seven drafted; closes in Phase 2 against content. See below |
| **Q2.9** The non-blocking lists | Still pending, and still not blocking: L10–L13, L19, L20, L24, L30 |

## Q2.8 · Is the Verb set complete? — **the one irreversible decision**

**Seven drafted:** `Push` · `Set` · `Place` · `Repin` · `Link` · `Create` · `Decide`.

**Deliberately not closed.** L6 closes against the *finished* set, and the finished set includes content that does not exist yet. Locking it now would be settling against imagination, which is precisely what the rule exists to prevent.

**The closing procedure:** take every entry from every other list plus every worked example; for each, assume the fiction has already decided what happened, write only what changed in the world, then ask which Verbs express it.

> **If a consequence needs an operation not on the list, that is a real finding.**
> **If it merely needs a Tag, a Channel, or a Component formula, it is not.**

**Blocks:** nothing yet. No Substrate code should depend on the Verb set being final until Phase 2 closes it.

---

## Q2.10 · How is magnitude produced? — **provisional answer, August 2026; final formula still the Resolution Socket's**

**PLAYTEST tunable: the Attempt roll defaults to d100 (two d10s), with d20 as the named alternate, and the beta's tuning console accepts arbitrary dice expressions** — swapping the expression mid-campaign is the point, because the formula gets found by comparing feels against logs. The Socket contract is unchanged: whatever ships must publish its distribution.

*"A combination of modifiers and a dice roll."* The formula waits until content exists and real numbers can be seen. It is the **Resolution Socket's** business, and the Socket's *contract* is already decided even though the formula is not: **the occupant must publish its distribution**, because rule 19 requires any likelihood-expressing Lens to be Calibrated against it.

**Blocks:** every worked example that needs a number, and therefore most of Phase 2's arithmetic. **It does not block writing the content itself.**

---

# Part 3 — Decisions needed before any code

---

## Q3.1 · How many Attempt Points? — **ANSWERED, August 2026**

**They scale with the character — start around 3, grow to as many as the character can use. Playtest default: 5, as a PLAYTEST tunable.** The scaling curve belongs to character creation, which is Phase 2 work; the natural home remains a Capacity — *capacity to divide attention* — which keeps it kind-agnostic, lets a distracted character have fewer and a practised one more, and makes it a progression axis that **cannot inflate damage**, because points buy precision rather than power.

**Blocked by it.** Character creation, progression, the interface, and every Threshold's difficulty.

---

## Q3.2 · Is there a ceiling on summed Baseline shares?

Baselines raise total effect. Eight of them on eight Dimensions multiplies total effect several times over.

**Open:** whether the ceiling exists at all, and if it does, whether it shares Enhancement Capacity's budget or holds its own. **Related to Q1.4** and probably answered by the same decision.

---

## Q3.3 · Entering Ordered time — **ANSWERED, August 2026**

**Adopted: a vector placed on an unwilling target opens Ordered time; manual initiation always exists.** The two-allies-racing case is covered by manual initiation and known to sit outside the rule.

**Entry is base Ruleset, not the Substrate's** — three Substrate rules were tried and each failed on a real case:

- Ally/enemy labels → undefined for strangers, under the open-world rule.
- *"A Moment that doesn't exist yet"* → catches everything, since every future Moment is yet to exist.
- *"Anchored to another Entity"* → wrongly drags healing an ally into combat.

**Leading candidate:** a vector placed on an **unwilling target**, where willingness is a property of the placement — declared by content, refusable by the target's controller — and never a stored relationship label. Manual initiation always exists as well.

**The case it does not catch:** two allies racing to cut the same rope. Nobody is unwilling and ordering still matters. Manual initiation covers it, but it is worth knowing the rule is incomplete by design.

---

## Q3.4 · Does the Record shape carry `delivery` from day one?

Absent means *everyone*, so it can be added later without breaking history. **Cheap, not urgent.**

**But the coupled decision is not deferrable:** the server folds and is authoritative. If clients ever fold from Records, the first withheld Record silently diverges that client's state. Decide `delivery` whenever; decide server-side folding before the first commit.

---

## Q3.5 · Turn position and defensive load — **premise disputed; instrumented, not ruled on**

**Dylan's read, August 2026: unfounded.** End-of-round effects land after everyone by definition, and most vectors land at the start of the *target's* turn — so every target accrues one round of arrivals regardless of initiative position. Rather than argue it on paper, **the beta logs arrivals-per-Moment per creature**; if a positional skew is real, the data will show it.

Everything pinned to your turn lands at once. So the creature that acts last in a round eats an entire round of accumulated vectors in one resolution, and the one that acts first eats almost none — a large swing, decided by initiative rather than by any decision the player made.

**This is base Ruleset's problem, which means it is versionable** — but every piece of content will be balanced against whatever the default does. Options: stagger arrivals within a round, cap arrivals per Moment, or accept it and design initiative around it.

---

## Q3.6 · Shared-Track double-spend across simultaneous scenes — **beta default set, provisionally**

**Beta default: reserve at declaration.** When a scene spends from a Track shared with a simultaneous scene, the amount is held the moment it is declared, so the other scene sees the reduced balance immediately. On a server this is trivial, and it is the strictest option — relaxing later is safe, tightening later is not. Kept provisional pending play.

Two scenes are simultaneous until their shared Moment. If both spend from the same faction treasury, both spends are valid in their own scene and the conflict only surfaces later.

**Participation Capacity solves the *unique object* case.** It does not solve the *divisible resource* case. This needs a rule and does not have one.

**Options:** reserve at declaration; resolve overdrafts at the shared Moment with a declared rule; or forbid cross-scene spending of shared payable Tracks entirely.

---

## Q3.7 · Contributor ordering at a full Participation cap — **ANSWERED, August 2026**

**Declaration order — whoever presses the button first.** When a capped stat fills, its button disables; contributors can still add to the uncapped stats of the party-sized roll. Outside Ordered time, simultaneous declarations break by nimbleness — the MOVEMENT Dimensions — then the stable key. The async-fairness consequence (rewarding whoever checks their Dispatch first) goes on the Phase 5 watchlist.

The dictionary used to claim conflicts need no tiebreak because Participation Capacity settles them. The adversarial review (A13) showed that is false: two contributors, one open slot, and nothing declared decides who is in. That is a determinism hole — the Fold must produce the same answer everywhere — and, in asynchronous play, a fairness question, because "first to submit" quietly rewards whoever checked their Dispatch soonest.

**Options:** declaration order by Record sequence (deterministic, and honest about the async bias); a stable entity key (deterministic and arbitrary); the target's controller decides via a Proposal (fair, adds a human Decider with a Moment and default); or a declared per-Setting rule through the Place occupant.

**Blocked by it:** any content using Participation Capacity — which includes the cooperative-lockpicking scene the pitch leads with.

---

## Q3.8 · Listener semantic classes and the total order — **ANSWERED, August 2026**

**Three classes, in firing order: `substrate` (engine-declared watches) → `mandatory` (Component Listeners) → `elective` (player-parameterised Standing Orders)** — mandatory-before-optional, the one ordering the field fully specified. **`source_record_id` joins the key as its final component**, closing the collision the research found: `(class, layer, component_id, listener_id, target_entity_id, source_record_id)` is a total order.

L26 settled the simultaneous-Listener order as *semantic class first, then `(layer, component_id, listener_id, target_entity_id)`* — and never enumerated the classes. An undefined term inside a determinism-critical sort. Separately, `research-listeners.md` showed the four-tuple is not a total order: the same Listener firing for the same target from two sources in one Moment collides, which argues for `source_record_id` as a final component.

**Both halves need one written answer before any code.** Neither changes the design's shape; both change whether two machines fold identically.

---

## Q3.9 · The base Creature's social and mystic Tracks — **ANSWERED, August 2026**

**The split: `standing` joins the base person, so anyone can be slandered out of the box; `working` and `essence` attach per character.** A person with no `essence` cannot be soulburned, and no rule says so — the same absence-is-immunity logic the design already runs on.

L3 gives `Creature` no `standing`, `regard`, `working` or `essence` Track — yet seventeen of the eighty-eight Channels land *only* on those axes (the nine pure-standing and eight pure-mystic pushes — praise, scorn, slander, drain and their kin), and creatures are their obvious targets. Under *absence is immunity*, the base person is therefore immune to all social and mystic harm unless a Setting adds the Tracks. `regard` landing on Connections is by design; the rest looks like an omission, and no Part 12 row records it as a choice.

**Options:** add the Tracks to the base Creature bundle; leave them to Settings and accept that the base game has no social or mystic consequence; or split — `standing` base, `essence` Setting.

**Blocked by it:** the first paper scene where anyone tries social pressure.

---

## Q3.10 · The Record-shape Listener form — **ANSWERED, August 2026: it stays, with the objections met**

**Records must be listenable — reflection and retribution depend on it.** The three research objections and their answers, now in Part 12: edge-triggering by construction (a Listener matches only Records written since its last evaluation Moment); compensation-aware matching (a Record superseded before the evaluation Moment does not match); and the form participates in the same cascade depth and per-Moment accounting as every other form, so termination is enforced dynamically where it cannot be proven statically.

L26 adopted "a Resolution Record matching a shape" as a condition form — `dictionary.md` calls it the one that carries the most weight. `research-listeners.md` argues against exactly that form at length: it has no natural edge-triggering, it false-matches Records later corrected by compensation, and it destroys the static triggering-graph termination check — proposing Moment-scoped derived quantities instead. The settlement post-dates the research, but the six counter-arguments were never answered in writing.

**The ask is not a redesign — it is a written rebuttal or a reopening**, before the form is load-bearing in code. If the rebuttal exists in someone's head, Part 12 is where it goes.

---

# Part 4 — Decisions needed before content and launch

---

## Q4.1 · Which instrumentation surfaces ship to real tables?

Some are so good that hiding them behind a tester flag is a mistake — resolution expansion, notes, the event log. Some would ruin a scene if a player opened them mid-fight — time travel, what-if, direct state authoring.

**The interesting one is what-if.** Given to players, it is the missing learning gradient for a system whose failure mode is *"I have no idea why that didn't work."* Given to players *mid-scene*, it is a solver.

---

## Q4.2 · Threshold visibility — **beta stance set; release default still a Phase 5 measurement**

**In the developer beta, everything is visible — nothing hidden in the slightest**, because the testers are developers of the game and the build exists to be seen through. The near-miss reveal (hidden at declaration, shown in the post-resolution breakdown) is the leading candidate for the release default, evaluated later against beta logs.

It is a built-in GM setting, so both work. **But the default decides what the game is**, because allocating against bars you cannot see is the source of the tension — and it is also the source of the frustration.

**Untestable on paper alone.** This is a Phase 5 measurement.

---

## Q4.5 · What is solo play, exactly? — *new with the brand, August 2026*

The Vectus identity board promises it twice: *"Jump in solo"* and *"Play solo or together — your choice."* The corpus never scoped a solo mode. Standing orders, asynchronous reports and authored content get most of the way to a GM-less loop — but somebody has to design who sets the Thresholds, who plays the world, and what a solo session's Dispatch looks like. Until that is scoped, the brand promise is ahead of the roadmap, which is the one kind of debt a brand should not carry long.

**Options:** authored solo Adventures (content plays the GM — rails plus Deciders with defaults); an oracle-style GM emulator as a Component; or narrowing the promise to "start solo, learn solo" (character creation and tutorials) until one of the first two exists.

---

## Q4.3 · What does a Component look like to a customer?

An expansion? A subscription tier? A class? A rules module? **The mental model determines the price point, and the price point is close to irreversible after launch.**

---

## Q4.4 · Which Asset types get user authoring, and in what order?

Every authoring surface is a real unit of work, and authorable types are what let users build without buying — which is a commercial decision as much as a technical one.

---

# Part 5 — Questions only Dylan can answer

No amount of research substitutes for these, and several of them change everything upstream.

---

## Q5.1 · Is the ruleset ever a book? — **ANSWERED, August 2026: no**

**The game is unplayable without the computer, so the ruleset is software and web documentation.** If a book ever exists it is a reference to the website, printed after success — never the product. The single-work trademark trap and the art-cost structure both largely dissolve; the platform filing basis stands. The plan: copyright the website, create a business entity to house the project.

**The highest-consequence unanswered question in the project.**

If a printed or PDF core book exists as a saleable object, it inherits the entire art-cost structure *and* the single-work trademark problem — a title of a single creative work is not registrable.

If it is only ever software and web documentation, **both problems largely dissolve**, because software and games are explicitly exempt from that trademark bar.

This decides the branding strategy, the art budget, and the legal filing, and it can be answered today.

---

## Q5.2 · Can the game be played without your server?

Not *would anyone* — **can it.**

This decides whether the obsolescence objection (*"what happens to my campaign when you stop paying for hosting"*) has a structural answer or only a rhetorical one. It is an architecture decision wearing a marketing question's clothes, and the append-only Ledger plus byte-identical export is most of the answer already — if you commit to it.

---

## Q5.3 · Do you genuinely want third-party Component authors?

*Users author instances, never types* is a hard architectural line, enforced structurally.

**If it holds absolutely, there is no third-party ecosystem** — which removes the most powerful free marketing this hobby has, and reads to part of the audience as a closed platform.

**If there is a sanctioned path for a developer to author types**, then: who is eligible, what does it cost them, and what stops the type space becoming incoherent?

---

## Q5.4 · System, platform, company — **ANSWERED, August 2026**

**The system and the platform are one and the same, under one name. The company might carry a different name** — decided separately, alongside the business entity.

Three is more flexible and three times the trademark cost. One is cheaper and fuses everything to a single name.

**Everything in the naming work depends on this**, and it is executable immediately once it is answered.

---

## Q5.5 · Are you willing to be personally visible?

A named human building in public is the cheapest acquisition channel available, and the strongest counter-signal against AI-slop suspicion in a market that is currently very alert to it.

It is also exposure you may not want, and it fuses the brand to you in a way that is hard to undo.

---

## Q5.6 · Which invented words must a player hold in their head to take a turn? — **direction set by the brand, August 2026**

**The Vectus board answers the register question:** players meet the eight steps — Intent, Direction, Force, Interaction, Layers, Resolution, Outcome, Your Story — plus *vector*, *magnitude*, *chance* (`brand-identity.md`). The engine register never reaches a player screen. What remains open is exactly which mechanical terms survive on the character sheet. You know this and I do not. **That list is the only one the jargon research applies to.** Everything else is documentation and can be as precise as you like.

The related question: **would you accept the community renaming things?** They will. If that would be intolerable, the player-facing vocabulary has to be *sayable* rather than merely correct — because sayable wins every time.

---

## Q5.7 · What happens if it works?

Three thousand people playing asynchronously, generating support load, while you have a full-time job and two young stepkids. **The failure mode here is public** — an unanswered Discord and a stale changelog is how a platform brand dies visibly.

This is worth an answer before launch, not after.

---

# The short version

**Already answered:** Q1.1 through Q1.5, plus A17. Closed in Phase 0, recorded in `work-repair.md` and `dictionary.md` Part 12, tested in `phase-0-checks.py`.

**Answer today because they change everything upstream:** Q5.1 (is it ever a book) and Q5.4 (what is the brand).

**Answer while filling the lists:** all of Part 2 — and **Q2.8 last, alone, with more care than anything else in this file.** It is the only decision here that cannot be revised at any price.

**Answered August 2026:** Q3.1, Q3.3, Q3.7, Q3.8, Q3.9, Q3.10, Q5.1, Q5.4 — plus provisional playtest answers for Q2.10, Q3.6 and the Q4.2 beta stance. **Still needed before the first engine commit:** Q3.2 (deferred to playtest by choice), Q3.4's server-folding confirmation, and Q3.5's instrumentation hook in the beta.

**Answer with playtest data, not by thinking:** Q1.1's final form, Q4.1, Q4.2.
