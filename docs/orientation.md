# Orientation

**A full explanation of everything established so far.**

This document assumes you can read a schema, reason about systems and tradeoffs, and have written code — but not that you follow software engineering as a discipline or know the jargon. Where a concept has a standard name, I use it and then explain it plainly, so that when you see the term elsewhere you recognize it.

It covers: what we're building, why the design is shaped this way, how each piece works, the vocabulary we should both use, the assumptions I've been making that you never confirmed, and every open question.

Read Part 13 (Assumptions) carefully. It's the section most likely to contain something wrong.

---

# Part 1 — What we're building

## 1.1 The product

An original tabletop roleplaying game where a purpose-built web application is the medium rather than an accessory. The rules are designed around what software can do and paper cannot. The stated failure condition, from the beginning: if the honest justification is "it's more convenient," it has become a virtual tabletop and should be abandoned.

The thing that makes this defensible against Foundry and Roll20 is structural rather than competitive. Those platforms are blank slates that host *other people's* games — that's why setup eats an evening, why Foundry has thousands of modules with breaking dependency chains, and why a user assembles a game from parts. Here the game and the tool are the same object. Foundry cannot copy this; the moment they ship one fused game they stop being a virtual tabletop.

## 1.2 The four layers

Everything in the system sits in one of four layers. They are authored separately, sold separately, and change at different rates.

**The Ruleset** is the game itself — core resolution, the base rules every player learns, how conflict works, what a character is. Versioned as **Editions**, the way tabletop games have always done it. You author this and nobody else.

**Components** are rules subsystems — currency and exchange, energy in equipment, crafting, bloodlines, mass combat, corruption. Each is independently versioned and independently purchasable. You author these and nobody else. This is the product line.

**Settings** are configurations: which Components are active, where the dials sit, the vocabulary, plus world material. You author six reference Settings at the highest quality anyone will see. Users author their own, free.

**Adventures** are campaigns, one-offs, or anything between — specific content, tracking, and optionally victory conditions. You author examples. Users author their own, free.

Beneath all four sits **the Substrate**: the data and execution model. The Substrate is not part of the game. It is the physics of the software. It is never versioned, because everything else depends on it being stable forever.

## 1.3 The line that defines the product

> **Users author instances, never types.**

Users create Settings, Adventures, and content. Users never create or alter a Component, a Noun, a Verb, or anything in the Ruleset.

This is the line that keeps the product from becoming Foundry. Foundry hosts other people's *rule systems*. Here the rules are yours and fixed; what varies is configuration and fiction. Users aren't building games — they're building settings for your game.

The critical enforcement detail: **the authoring tool must make crossing this line structurally impossible, not merely disallowed.** A line held by a rule in the documentation erodes. A line held by an editor that physically cannot express the forbidden thing does not.

---

# Part 2 — Why software, and where the leverage actually is

## 2.1 The diagnostic that reorganized everything

The most useful thing from the research is a distinction that sounds academic and is enormously practical:

> **Paper constraints produce COST problems. Human constraints produce VALUE problems.**
> **Automation lowers cost. It cannot manufacture value.**

A rule gets abandoned at a table for one of two reasons: it costs more than it's worth, or it isn't worth anything. Both look identical in practice — the rule stops being used — which is why designers keep "fixing" the wrong half.

**The test, applied to every subsystem before you build it:**

> If a perfect, free, invisible robot did every calculation and every write-operation for this, would the table still want it in the game?
> **Yes** → cost failure → paper's fault → automate it.
> **No** → value failure → your fault → cut it, or rebuild the choice it was supposed to create.

And the corollary that matters more than the test: **automating a value-failed subsystem is actively harmful.** You convert an ignored rule into an invisible one, and now the table can't even notice it to argue with it.

The proof case is torch and light tracking. Every paper-side fix ever proposed — slot systems, usage dice, bundling — is a technique for reducing bookkeeping. None of them made anyone *want* the subsystem. What experienced game masters report actually fixing it is making light *matter*: targetable in combat, a vulnerability, a puzzle input. That's a value fix. Perfect automated tracking would have changed nothing.

## 2.2 Where the medium actually gives you leverage

Sorting the constraints of a paper table through that test:

**Genuine paper problems, fully dissolved by software** — continuous-state bookkeeping, off-screen world simulation, rules retrieval, in-game arithmetic, character creation math, prep-as-transcription, random generation, continuity recall. All real. **All table stakes.** Every virtual tabletop already claims them, and the ones that don't are free. **None of them differentiate.**

**Human problems the medium barely touches** — scheduling and attrition, the creative half of GM burnout, mismatched expectations between players, the dominant-player problem, decision paralysis, system mastery as social exclusion, blank-page anxiety, table chemistry.

**The three places software gets real leverage on a human problem:**

1. **Hidden and asymmetric information.** Paper handles this with screens and passed notes. This is also, per the research literature, the structural fix for the dominant-player problem — the underlying disease is a game with a solvable optimal line and complete shared information.
2. **Progressive disclosure.** Paper physically cannot withhold a rule until it's relevant. Software can. This is a real, uncopyable advantage.
3. **Asynchronous scheduling.** The only design-side lever on the largest single cause of campaign death.

**That is the competitive surface. Three items, not seven.** Everything else is necessary and insufficient.

## 2.3 The pitch, stated honestly

The product is not fog of war and it is not divergent truth. Those are mechanics.

**The product is a campaign that survives adult life.** Someone travels for two weeks and the game continues without them. Someone joins in month eight and arrives current. Two people play a session while three are out. The world moves on a visible cadence instead of freezing between sessions.

Most campaigns die of scheduling and exhaustion, not boredom. Nobody in this space sells against that, because on paper it's unsolvable. And the head of D&D said publicly in August 2026 that the most consistent feedback he receives is that players' lives now make the game impractical — which is the largest company in the category confirming the thesis and starting a clock.

---

# Part 3 — How the machine works: the Substrate

This is the part that can never be rebuilt. Everything here is chosen because retrofitting it later is either impossible or ruinous.

## 3.1 The Ledger: why a log instead of a database

The instinct when building software is to store current state: a table of characters with a `health` column, and when someone takes damage you update the number.

We're doing the opposite. **We store everything that has ever happened, in order, and never change any of it. Current state is calculated from that history whenever we need it.**

The analogy that will land for you: this is a **general ledger**, in exactly the accounting sense. An accountant doesn't store "the balance is $4,200" and overwrite it. They store every transaction, forever, and the balance is derived. Corrections are new entries, never erasures. That practice exists because auditability, reconstruction, and trust all depend on it — and every one of those reasons applies here.

The formal name for this in software is **event sourcing**. Our terms:

- **Ledger** — the append-only, immutable sequence of everything that happened in one Campaign.
- **Record** — one entry in the Ledger. Never modified after it's written.
- **Fold** — the function that walks the Records in order and computes current state. Given the same Records, it must always produce the same state.

**Why this specific choice, when a normal database would be simpler:**

*Asynchronous play needs it.* When actions arrive at different times from different people, you need an authoritative order and the ability to reconstruct what anyone knew at any moment.

*Divergent knowledge needs it.* Recording *when* someone learned something, and what they were told, is only possible if you keep the history rather than the summary.

*The improvisation requirement needs it.* This is the one that resolves a genuine contradiction in the original brief. The design says the app must absorb a GM inventing a condition that doesn't exist, adjusting a number, adding a resource mid-session — while also maintaining consistency well enough to keep secrets straight for months. Those requirements fight, unless: **the Ledger holds *claims*, not truth.** "The GM asserts X" is a Record type the system understands natively. It never needs to understand what X *means* in order to record it, order it, show it to the right people, and let later Records reference it. The world is exactly as modeled as the active Components require, and infinitely improvisable underneath.

*Corrections need it.* A mistake is fixed by appending a correcting Record, not by editing. You can always see what happened, what was wrong, and why it was changed — which matters enormously when an AI agent is one of the things making corrections (Part 9).

*The personal report needs it.* The **Dispatch** each player receives is literally a filtered slice of the Ledger.

*Curation needs it.* The layer that eventually decides "what's interesting enough to tell people" needs causal history to search. That can't be reconstructed later.

**The cost, honestly:** deriving state by replaying history is more work than reading a column. In practice this is a non-issue at any scale you'll see — a campaign with 100,000 Records folds in well under a second with competent code, and the standard optimizations exist if you ever need them. The real cost is conceptual: you have to think in terms of "what happened" rather than "what is," and that takes a few weeks to become natural.

## 3.2 Entities and Facets: how things are represented

The Substrate knows three things: things exist, they have permanent identity, and Components attach data to them.

- **Entity** — anything that persists and has identity. A character, a place, a faction, a ship, a rumor. The Substrate knows an Entity exists and *nothing else about it*. It does not know what a character is.
- **Facet** — one Component's data attached to one Entity. The Currency Component attaches a purse. The Energy Component attaches a charge level.

**The critical rule: a Component may read and write only its own Facets.**

The database analogy: instead of one wide `characters` table with two hundred columns that every part of the system reads and writes, each subsystem owns its own narrow table keyed by entity ID. Currency owns `purse`. Energy owns `charge`. Neither can touch the other's table.

This is what makes the system buildable by one person over a decade. If forty Components can each reach into every other Component's data, you have forty-times-thirty-nine possible interactions, none of which you tested. If they can't, you have forty independent things.

*(The formal name for this pattern is Entity-Component-System, borrowed from game engines. The reason our version is unusual: normally ECS optimizes for a few component types across millions of entities. We have thousands of Facet types across a few thousand entities — the reverse — which changes the right storage strategy but not the concept.)*

## 3.3 Verbs and Nouns: the vocabulary of the system

Here's the problem the rule above creates. If Crafting can't touch Currency's purse, how does crafting cost money?

**Verbs** are the answer. A small, **closed, permanent** set of abstract operations. Crafting never says "spend 5 gold." It records only the consequence: *value V transferred from Entity E.* Whatever economy Component is installed — coin, barter, favor, reputation, ration tokens — decides what that means. Swap the economy and crafting still works, untouched, because it never knew what money was.

**This is the single highest-risk decision in the entire system — and it is deliberately the LAST one made, not the first.** It's an instruction set. Too small and Components can't express what they need; too large and it's unstable, and every addition is permanent. The candidate list right now:

`create · destroy · move · alter magnitude · transfer · set state · clear state · add tag · remove tag · form relationship · break relationship · reveal · conceal · bind to condition · advance clock · apply · assume category · shed category · repin`

Domain operations are never Verbs. *Inherit* is form relationship + add tag. *Fuse* is destroy + destroy + create. If the Verb set is right, everything composes out of it.

**Nouns** are the opposite: an **open, extensible** set. A Noun is a published data schema, and there are exactly **five kinds** — **Capacity** (a graded, kind-agnostic disposition), **Tag** (loose membership, optional magnitude), **State** (a named condition, exclusive within its axis), **Resource** (depletable, with thresholds), and **Relationship** (a Category of Entity holding one Connection per participant). They behave differently under change, aggregation and rendering, which is the entire reason the kinds exist.

And the framing that produced them: **model what a thing affords, not what it is.** *Capacity to exert force*, never *Strength* — because a capacity applies without absurdity to a person, a winch, a faction and a storm, while an essence claim about people needs an exception the first time an undead or an object shows up. Components publish Nouns and other Components may depend on them. Bloodlines publishes the concept "bloodline"; a disease Component that spreads through bloodlines depends on that Noun.

The asymmetry is the design: **Verbs are how things happen and never grow. Nouns are what things are and grow forever.**

**Where the danger lives.** A published Noun is permanent and can never change meaning. There is no such thing as a casual tag once a second Component reads it — at that moment it's a contract. This is why every schema element must be declared **Published** (visible, permanent) or **Private** (invisible outside its Component, mutable forever), explicitly, with no default.

Expect the mistake not in the Substrate, which will get careful attention because it's obviously important, but at the two-hundredth Noun, shipped on a Tuesday to support a Setting you were excited about.

## 3.4 Who sees what — and why this got much simpler

This section used to describe **Perception**: a whole Substrate mechanism where every Record carried a set of per-observer projections, two people could hold contradictory versions of the same event, and each player's world was folded separately from their own slice of history.

**That was over-built, and it is retired.** Three different things were wearing one word:

| | Where it actually lives |
|---|---|
| What a player **sees** on screen | the **Lens** — a rendering choice, not a mechanic |
| What a character **knows** — misremembers, was lied to about | an **optional Component**. Good enough to ship in v1; the game runs without it |
| Which **bytes reach which browser** | infrastructure, and the only part that is Substrate |

**The default posture is total visibility.** Every piece of Campaign data a client is entitled to is in that client's browser, and **every layer of every calculation is visible to everyone**. When your attack resolves, anyone can open it and see every slot it passed through, every modifier that contributed, and which item each one came from. Secrets are a later, deliberate decision — never the starting assumption.

**What survives is one field: Delivery.** *Who receives this Record.* Default: everyone. It exists for exactly two reasons, and neither is a game mechanic:

- **A GM's prep.** An adventure with a twist is unusable if the twist sits in every player's browser.
- **Purchased content.** A Setting whose entire text ships to every participant is readable by anyone who joins a Campaign using it.

Because absent means *everyone*, this can be added later without breaking any history. It is cheap rather than urgent.

**One architectural rule is not deferrable, though: the server folds, and clients render.**

The canonical state is computed on the server from the whole Ledger. Clients display what they are sent and never authoritatively compute anything. If clients folded from Records themselves, the first time anything was withheld that client's picture would silently drift from the truth — and you would not find out until someone argued about a number. Folding on the server keeps one canonical state forever, and turns *"hide this"* into *"send less,"* which is a policy change rather than a correctness break.

**And client-side hiding is theatre.** Anything a client must not have is never put into a byte sent to that client. Hiding it in the interface is not hiding it.

**Three things this deleted**, all of which were going to be expensive: per-player world states that could disagree with each other; the requirement that the folding logic cope with gaps in history; and a validator to prove that two players who know the same things are offered the same buttons — now true by construction.

## 3.5 Proposals and Deciders: one mechanism, six features

This is the most elegant thing in the design and it comes directly from the original brief's insight that every component can run automatically, hand a decision to a human, or be driven outright.

```
Proposal { subject, intent, decider }

decider = Auto(the component decides)
        | Person(a named human decides — always with a Moment and a default,
                 which fires if the human does not)
```

One field. Six features fall out of it:

| Feature | Implementation |
|---|---|
| The rails dial | Which Decider a Component's Proposals get |
| Player puppeting | Reassign the Decider to a player |
| GM-less play | Decider is Auto, everywhere |
| Hybrid Adventures | The script decides most, hands specific things up |
| Asynchronous play | Decider is a person, with a deadline |
| **Graceful absence** | The deadline fires the default and play continues |

That last row isn't a feature — it's survival. **Every durable asynchronous game form in history has an explicit answer to "what happens when someone doesn't show up," and every form without one dies at the first missed session.** Diplomacy has standby players as a named institution. Online Diplomacy has reliability ratings and automatic removal. The board game Oath automates an absent player's seat. Pandemic Legacy advances the calendar on a loss so the campaign structurally cannot stall.

Here it's the same field that does everything else.

## 3.6 Time: there is only the Moment

This section used to be about **Periods** — a bounded unit of time that Records belonged to, closing on a visible cadence. That concept is retired, because it turned out to be one grain of a more general thing.

**There is only the Moment.** A named point in the timeline that something can be pinned to. A turn is a Moment. So is the end of a round, the close of a downtime week, and the turn of a season. They are the same object at different grains.

**Turn and round are the Substrate's business; anything coarser is not.** *(Amended Aug 2026 — this used to say Time was a Socket.)* The Substrate ships the turn model a turn-based game needs so that abilities can be written and understood, and Components layer coarser clocks — downtime weeks, seasons, campaign turns — alongside it. A weekly play-by-post table and a live table running turn by turn share the same Substrate turn model with a different coarse clock over it, and content written for one does not have to be compatible with content written for the other, because they never meet.

**Nothing runs on a wall clock.** A Moment gets stamped with a tick when it actually occurs, and that stamp is what makes replay exact. Real time exists for humans — deadlines, notifications, *"you have until Sunday"* — and never reaches the rules.

**A Moment is a reference, not a number.** This is the subtle part. When you swing at someone, the blow is pinned to *"the start of that person's turn"* — the description, not a computed time — because they might react and shove it later, or the turn order might change before it arrives. It is resolved to an actual tick only when time genuinely gets there.

**And objects take turns.** Not just creatures. A lock has a turn, a door has a turn, a ship's hull has a turn. That single generalisation is what makes cooperation work with no special rule: two people who both try the lock each pin an attempt to *the lock's* turn, and when the lock's turn comes round, both land together and combine.

### What replaced Budgets-per-Period

**Budget is a Socket too.** How many actions you get, when they come back, whether reactions exist — all of that belongs to whichever Component fills the hole, and it will rarely be swapped because swapping it means playtesting an entire economy from scratch.

**But the vocabulary is Substrate.** If a spell costs *one action*, then `action` has to be a word that exists no matter which economy is installed — otherwise every spell ever written is hostage to one Component. The **names** are permanent; the **economics** are swappable. That split turns out to apply to every Socket, and it is what makes them safe.

## 3.6A Sockets: the Components that cannot be absent

The claim *"everything above the Substrate is a Component"* is true, and was misleading. Some Components are load-bearing walls rather than furniture.

The Substrate defines what a **Moment** is and cannot say which Moments exist. It defines what a **Resource** is and ships none. It knows a vector can land and cannot say what landing does. Those are **Sockets** — named holes the Substrate declares and cannot fill itself.

- **Exactly one occupant per Socket. Never zero, never two.**
- **A Bundle with an empty Socket must fail to load.** That is the rule that makes the concept worth having.
- **Swapping an occupant is an Edition-level change**, never a casual toggle, because every piece of content in the Bundle is written against what it publishes.

Five candidates: **Time** (which Moments exist), **Place** (what *area* and *range* mean), **Resolution** (how an attempt gets its number), **Landing** (what a vector that gets through does to you), and **Budget** (how actions are rationed).

**Keep that list short.** Every Socket is a permanent dependency for every Component ever written, and an over-long list quietly rebuilds the monolith that the whole Component design exists to prevent.

## 3.7 Campaign isolation: the scaling decision

Everything is scoped to one Campaign's Ledger. Campaigns never share state.

This is nearly free to decide now and impossible later, and it's what makes the scale requirement trivial. A million Campaigns is a million small independent logs, not one enormous database. It shards across servers with no coordination. One heavy table cannot affect anyone else's performance. Rebuilding derived data is per-Campaign and embarrassingly parallel.

If a persistent world spanning multiple groups ever happens, it's a later layer that **publishes between** Campaigns rather than merging them. Designing that in now would cost the isolation property; designing it later costs nothing.

## 3.8 Export and import

`export campaign → a text file` and `import`, with a guaranteed identical round-trip, tested automatically from day one.

That one pair of functions is simultaneously: the migration path off any database vendor, the privacy-deletion tool, the backup granularity, the cold-storage mechanism, the debugging loop (Part 9), and the actual guarantee behind "this can never be rebuilt from the foundation." It's the highest-leverage hundred lines in the system.

---

# Part 4 — How the rules work

## 4.1 Verbs are data

*(This section used to be called "Effects." That word is now retired from the engine vocabulary — a proposed change is a **Verb**, and nothing else. "Effect" is being kept free so it can mean something in the fiction later, like a spell effect, without colliding with an engine concept.)*

A **Verb** is a proposed change to game state, expressed as **data** rather than as code that runs. "Reduce Entity 47's charge by 3" is a small structured record, not a function call.

Why: data can be inspected, logged, reordered, tested, and replayed. Code that runs immediately can't be any of those things. This is what makes the ordering rules below possible at all.

## 4.1A Every Verb has the same shape

Not "each Verb defines its own arguments." One shape, for all of them, forever:

| Field | Plain English |
|---|---|
| **verb** | which operation |
| **source** | who or what it comes from |
| **target** | who or what it happens to — **exactly one** |
| **secondary** | anything else the same change touches |
| **direction** | *what* is being changed |
| **magnitude** | *how much* |
| **class** | why this change exists (next section) |
| **layer** | where it sits in the ordering (§4.4) |

**Direction and magnitude** is the vector idea from the damage system, applied to everything. Fire hitting a person is a direction (temperature) and a magnitude (how much). A reputation hit, a coin transfer, a clock advancing — all the same two questions: *what is being pushed on*, and *how hard*. Harm just happens to be the case where the direction lives in the physical space.

**Exactly one primary target** means a Verb hitting three people is three records, not one record you have to unpack later. "Who did this happen to" becomes a lookup instead of an interpretation.

One shape means one parser, one validator, one log format, one replay path — permanently. If a Component ever needs a field that isn't in that table, that's a signal the Substrate is wrong, not a reason to add a ninth column.

## 4.1B Verbs return nothing — Listeners do the work

A Verb doesn't hand anything back. There's nothing running to hand anything back *from*.

So how does anything follow from anything? A **Listener**: a declared watch on a condition.

A blow drives someone's health to zero. The Verb doesn't know that and doesn't report it. A Listener that was watching *"this Resource is at zero"* notices, fires, and issues its own Verbs — set state `unconscious`, add a Tag, whatever that Component declared.

The important detail: **a Listener watches state, not Verbs.** It asks *"is this true now?"*, never *"did that just happen?"* The second version would make Components depend on each other's internal sequences, which is the exact thing the whole Component design is built to prevent. The first version only depends on the world, which is re-derivable from the Ledger and therefore safe.

Listener-produced Verbs are pinned to a *later* Moment, never inside the current one, and cascades are depth-limited.

## 4.1C The Ledger can record things no Verb caused

A Verb is one *kind* of Record. There are others that change nothing at all: a GM asserting something, a note, granting someone knowledge, a session starting, a proposal being raised, a correction.

Which means **"what happened" is a bigger set than "what changed."** The closed Verb set only has to cover the second one — and that's the whole reason a closed set is achievable at all.

## 4.2 The two Verb classes

Every change carries a class saying *why it exists*. There are two.

**Activated** — someone chose to do this. You cast the spell, you swing the sword.

**Triggered** — a Listener saw the world change and issued it. The blow landed, health hit zero, and something watching *"health at zero"* fired.

**There used to be four**, and the story of losing two is worth keeping, because it is the clearest example of the design getting smaller rather than larger.

The other two were **Replacement** (*"instead of taking hull damage, take 2 less"*) and **Continuous** (*"while the gunner is at his post, cannon damage is +1"*). Both looked essential. Both dissolved the moment changes became **vectors with a window**:

- A **Replacement** is just something already standing in the space when the damage arrives. Armour does not *intercept* a blow — it is simply present, and the arithmetic subtracts. "Instead of" was a description of subtraction all along.
- A **Continuous** is a vector whose window is *"while this condition holds"* rather than *"one instant."* Nothing about it needed its own category; it just lasts longer.

**Two mechanisms deleted, none added**, and the uniform shape every Verb carries stopped needing per-class exceptions. A third class added later would be a foundation break — so if you ever find yourself wanting one, that is a real finding about the design, not a convenience.

## 4.3 Moments — where things actually apply

Resolution runs in rounds. Collect all the Verbs → reach a **Moment** → apply them in order → evaluate the Listeners against the new state → whatever they produce goes into the next round → repeat until nothing new fires or the declared depth limit is reached — cascades are bounded, not run to a fixpoint.

**Nothing mutates between Moments.** This is what makes resolution order a property of the Ruleset rather than an accident of which Component happened to run first.

## 4.4 The Layer lattice

This solves one specific problem: **two independent things modify the same number, and the order changes the answer.**

Plus 2, then +100%, gives 20 from a base of 8. Apply the percentage first and you get 18. Same modifiers, different result — and neither Component knows the other exists.

A **Layer** is a numbered slot. A Component never says "I modify speed"; it says "I modify speed **at R-500**." Order becomes a property of the system rather than an accident of which code ran first.

**The resolution region is drafted** — thirty slots in three groups, and every boundary was forced by a case that was actually worked rather than guessed. The full list is in `dictionary.md` Part 2A; the shape is:

```
E-100 … E-500     preparing an Entity      does it exist, what Categories it holds,
                                            its own numbers, its ceilings
C-100 … C-600     creating a vector        everything the source contributes,
                                            collapsed to a direction and four numbers
R-100 … R-1400    resolving at a Moment    gather, assemble each vector, convert
                                            Scales, combine, meet Guards, land,
                                            record, then Listeners
```

### Three rules that came out of drafting it

**You can pre-sum. You cannot pre-apply.** Adding is associative, so a partial sum can be finished later without changing the answer. Applying is not — apply half the percentages early and the rest late and you have silently reintroduced compounding, plus a rounding step in the middle. This is why everything the source contributes collapses into *sums* when a vector is created, and nothing is actually applied until it lands.

**Nothing compounds.** Percentages add: +100% and +100% is +200%, which is three times the base and not four. This is not a preference. Compounding is commutative in real arithmetic and **stops being commutative the moment you round between steps** — base 5 with +30% and +40% resolves to 8 or 9 depending on which unrelated Component happened to go first. That is exactly the failure the whole determinism discipline exists to prevent.

It has a vocabulary consequence that content authors have to obey: **never write "double the damage." Write "+100%."** If the card says *double* and the machine adds, every stacking case surprises someone.

**The ceiling belongs in the fiction, not the arithmetic.** A flamethrower can only be amplified so far — a better one holds more, and upcasting or spending a resource raises it. That is **Enhancement Capacity**, and it is what makes the additive choice free: three amplifiers hit the cap either way, so the arithmetic gets to be the boring correct one while the interesting decision moves to *how much can this thing hold*.

**Within a slot, order is irrelevant** — it is all addition, and addition commutes. Only the slots are ordered, and they are ordered permanently.

**What is still open** is everything outside resolution: progression, economy, movement, knowledge, social standing. Err high. An unused slot costs nothing; a missing one is a foundation break. Magic: the Gathering needed seven layers and thirty years, and still produces intuitive results only about 99% of the time.

## 4.5 Two groups playing at once

Tuesday, you and Jordan play a scene. Thursday, the other two play a different one. Both touch the same faction. What happened first?

**Nobody went first.** That is the answer, and it needs no tiebreak rule.

**The participant set is the scene.** Everyone inside the same run of turns shares a timeline and sees each other immediately. Everyone outside it is isolated. When something reaches beyond your scene — a faction alerted, a rumour spread, a bridge burned — it is pinned to **the next Moment both scenes share**, which is an ordinary pin on an ordinary Moment and needs no synchronisation machinery at all.

**Conflicts combine.** Two scenes both sending something at the same faction resolve together, exactly the way two fire vectors do. Two assassination attempts add up; two opposed political pushes cancel. And where they genuinely *cannot* combine — both groups stealing the same unique object — that is settled by **Participation Capacity**, the same ceiling that says only one person can work a lock at a time.

**No 3am advantage**, because playing first changes nothing.

**The cost, stated honestly.** Scenes that share no Moment until a coarse one are **simultaneous** until then. If your group kills the duke on Tuesday and the other group walks into his hall on Thursday, **he is alive on Thursday**, and dies for everyone when their timelines meet. That is correct when the scenes really were simultaneous and wrong when the table meant them to be sequential — and the fix is that a table wanting sequence puts a shared Moment between them.

# Part 5 — Determinism, and why it constrains the rules

## 5.1 The requirement

**The same Ledger must produce the same state, everywhere, forever.** On your laptop, on the server, in a player's browser, in 2037.

This is not an aspiration. Everything rests on it. If folding the same Records can produce different answers, then the game state isn't real, replay can't be trusted, the client can't predict anything, bugs can't be reproduced, and the whole event-sourced foundation is worthless.

## 5.2 What breaks it, and the rules that follow

**Floating-point numbers.** Computers store fractions approximately — `0.1 + 0.2` doesn't equal `0.3`. Usually harmless. But the *size* of the error differs between processors, browsers, and compiler versions, so the same calculation genuinely produces different results on different machines. People who claim to have solved this controlled their entire toolchain and one hardware platform. You control neither.

> **Rule: no floating point in game state. Integers and fixed-point only.**

**Fixed-point** means storing fractions as whole numbers with an agreed implied decimal place. $12.34 is stored as `1234` with everyone agreeing there are two decimals. All arithmetic is integer arithmetic — exact, and identical everywhere.

The open question is one global scale versus per-Noun scales. Per-Noun is more natural per domain (money wants 2 decimals, probability wants 6), but the moment one Component's number meets another's, someone converts, and conversion between scales is exactly where rounding bugs breed and hide for years. **Settled: one global scale, four decimal places** — store `125000`, meaning 12.5. Plus log-integers wherever values are compared across Scales. Storage is free, the math is exact, and most game values are plain integers anyway.

**Iteration order.** Some data structures don't guarantee the order you get things back in, and it can differ between runs. If you loop over a set of Verbs — or a set of Listeners that all fired at once — and the order varies, the result varies.

> **Rule: ordered structures, or sort by a stable key before any loop that affects state.**

**Randomness.** A shared random number generator makes every result depend on how many times it was called before — so any change to draw order changes everything downstream.

> **Rule: randomness is derived from a fixed seed plus identity — this Record, this Entity, this purpose. Never a shared stream.** Two dice rolls in different scenes are independent and reproducible.

**Time.** Reading the system clock makes replay impossible.

> **Rule: logical Moments and Ticks only. No wall clock reaches the game.**

**Text sorting.** Sorting strings by locale rules varies by system and changes between Unicode versions.

> **Rule: byte-order comparison only.**

**Version drift.** If a Component's code changes, replaying old Records with new code produces different history.

> **Rule: every Record records which Edition and which Component version produced it. Old code stays loadable forever.**

## 5.3 The harness

Build the determinism test harness before Component #10, not #100. Replay every Component's stored test cases on every platform and compare a hash of the resulting state. Store a state hash at every Moment in the Ledger — without those, a determinism bug is essentially unfindable.

Factorio does the production-grade version of this: save and reload every tick, and compare. Every system surveyed that lacks a harness pays continuously; every system that has one is one people cite as working.

---

# Part 6 — Components

## 6.1 Anatomy

Three artifacts, with three different compatibility regimes:

| Artifact | Regime |
|---|---|
| **Manifest** | Identity, version, supported Editions, declared dependencies, price |
| **Schema** | Immutable, additive-only. **The only thing other Components may depend on.** |
| **Behavior** | Versioned, replaceable, **never a dependency target.** Pinned per-Record for replay. |

**The rule that keeps the ecosystem healthy: you may depend on a schema, never on a behavior.** Depend on a schema and its owner can rewrite their internals completely without touching you. Depend on behavior and every change ripples.

Note this was a correction to an earlier, stricter rule. Your point that even a code Component publishes tags means the distinction isn't between *kinds of Component* — it's between **the two faces of any Component.** Anything may depend on a Component's schema face. Nothing may ever depend on its behavior face. That's the standard interface-versus-implementation split, and it gets you what you wanted without the cost.

## 6.2 The two faces

**The two faces of a Component.** Its *schema* face is declarative only. They publish Nouns and contain no executable behavior. Cheap, heavily depended on, permanently stable. They cannot rot.

Its *behaviour* face contains executable rules. They consume Nouns and produce Verbs, and may publish Nouns of their own. Versioned, tested harder, priced higher.

## 6.3 Three execution tiers

Reach for the lowest that works.

**Tier 0 — declarative data.** The Verb is a structured record interpreted by the Ruleset. Target the large majority here. Statically checkable, trivially versioned, trivially deterministic, inspectable by tooling — and it's the tier where Claude authoring a new Component by pattern-matching an existing one is most reliable.

**Tier 1 — restricted expressions.** Predicates and formulas only. No loops, no allocation, no external access.

**Tier 2 — sandboxed code.** The escape hatch for the genuinely irreducible.

The precedent: Magic Arena's rules engine "does not know what any of the thousands of individual Magic cards do." Each card compiles to declarative rules; about 80% of new cards are auto-converted from their English text. Novel mechanics still need engine work — and that work is deliberately generalized so the next similar card needs none. That's both the target and the realistic expectation.

## 6.4 Dependencies

Components have declared, one-directional dependencies. Disease depends on Bloodlines. This is a dependency graph, and dependency graphs are exactly what broke Foundry.

Your advantage is enormous — single author, no version ranges, additive-only. But the structural rule matters:

> **Dependency depth ≤ 2. Schemas at the bottom, behavior on top, and behavior never chains.**
> **Depth kills. Breadth is harmless.** Ten thousand behavior Components on two hundred schema packs is fine forever. Behavior depending on behavior depending on behavior is what dies.

The visible Component tree on the site is a nice enforcement mechanism: a deep chain *looks* obviously bad in a tree view in a way it never does in code.

## 6.5 Assets

Some Nouns are **Assets** — concrete authorable things. Characters, people, monsters, ships, equipment, places.

| | Authored by |
|---|---|
| **Asset type** (what a ship *is* — its schema, its rules) | You only. It's a Noun. |
| **Asset instance** (*this* ship, with these Attributes and this name) | Users, where the capability exists |

**Authoring capability is per-type and has to be built.** A Component publishing an Asset type may also ship an authoring surface — a form, constrained choices, a validator. Where that exists, users create instances freely. Where it doesn't, only you do. **This is a real unit of work per Asset type and should be scheduled and priced as such**, not assumed to fall out.

The Ruleset's own Asset types ship with authoring enabled from day one, so a user who has bought nothing can still build characters, places, and enough to run their own Campaign. Free means genuinely free.

Asset instances are the third sellable thing alongside Components and Adventures — and the one with the lowest authoring cost per unit and the highest potential volume.

This also resolves cleanly against the line in Part 1. Users author instances, never types.

## 6.6 Adding and disabling

A Campaign may **add** a Component at any time. It may **disable** an active one. It may **never remove** one, because existing Records reference its Nouns and the Ledger must stay foldable forever.

Disable is not one behavior. Each Component declares what it means for itself:

- **Frozen** — existing data keeps its values, nothing new happens. Currency stops circulating but purses still show balances.
- **Dormant** — stops producing Verbs but still folds its history, so re-enabling picks up coherently.
- **Hidden** — data persists, no longer surfaced.

Both the addition and the disable are recorded as Records, so a Campaign's configuration history is itself part of the Ledger.

---

# Part 7 — Editions

## 7.1 The separation that makes this work

| | Substrate | Ruleset |
|---|---|---|
| What it is | The data and execution model | The game |
| Versioned? | **Never** | **Yes — Editions** |
| If it changes | Everything breaks | Old Campaigns keep working |

A Second Edition changes how damage is calculated. It does not change what a Record is. **If a proposed rules change would require changing the Substrate, it isn't an Edition — it's a different product, and the answer is no.**

## 7.2 Revision versus Edition

The test is mechanical, not editorial:

> **Would this change cause an existing Campaign's Ledger to fold to different state than it does today?**
> **No → Revision.** Ships to everyone immediately, including running Campaigns.
> **Yes → Edition.** Opt-in only.

Revisions: clarified wording, new optional content, bug fixes restoring intended behavior, performance, interface. Editions: changed resolution math, changed Verb semantics, removed or reinterpreted rules.

The temptation will be to ship a fold-changing "fix" as a Revision because it's small and obviously correct. **A small fold change and a large one are the same category of change**, and that temptation is what this test exists to resist.

## 7.3 How Editions coexist

- A Campaign pins its Edition at creation and never leaves it without an explicit **Conversion**.
- **Every Edition's code stays in the repository forever**, side by side. Not deprecated, not archived — shipped code with passing tests, running on every build.
- **A Campaign started in 2027 still opens and plays in 2037.** That's the promise and that's the mechanism.

The cost is real: N Editions is N codebases that must keep compiling. The mitigations are that Editions should be rare — one every few years — and that old Edition code is *frozen*, so it's a compile-and-test cost rather than a maintenance cost. Nobody edits First Edition after Second ships.

## 7.4 Conversion

Moving a Campaign to a newer Edition is a choice the table makes.

The mechanism is the elegant part: **Conversion appends a Record.** *This Campaign converted from Edition 1 to Edition 2 at Moment M.* Records before that fold under Edition 1; Records after fold under Edition 2. The Ledger carries the boundary. No history is rewritten and nothing is lost.

Each Edition pair ships a conversion function and a **conversion report** — what converts cleanly, what's approximated, what's lost. The table previews it before deciding.

**Some Campaigns will never convert, and that has to be fine.** A group three years into a First Edition campaign should feel zero pressure. Every edition change in the hobby's history teaches the same lesson: people resent the pressure more than the change.

## 7.5 The commitments that follow

- **Component ownership spans Editions.** Buying Crafting in First Edition means owning it in Second. Charging again is the fastest possible way to make an Edition feel like a shakedown.
- **Old Editions get infrastructure improvements** — performance, mobile, notifications — because those are Substrate, not Ruleset. **Being on an old Edition must never mean being on old software.** That's the entire practical payoff of the separation in 7.1.

---

# Part 8 — Technology, in business terms

## 8.1 The principle: isolation, not correctness

Nothing survives ten years by being well-chosen. It survives by being **replaceable.**

Every decision sorts into three tiers, and the rule is that nothing in Tier 3 is ever load-bearing:

**Tier 1 — chosen once, never revisited.** TypeScript. SQL/Postgres semantics. WebSockets. React as a client library. **And the pure Ruleset package** — no external dependencies, no vendor types, no input/output.

**Tier 2 — replaceable in one to two weeks.** The realtime server. The database host. Authentication. Static hosting. Build tooling.

**Tier 3 — never load-bearing.** Sync engines, managed realtime services, backend-as-a-service, meta-frameworks.

**The test:** if the realtime server is 300 lines of glue and the Ruleset is 40,000 lines of pure functions, then "we must leave this vendor" is a fortnight of work. If the rules are written *as* vendor API calls, leaving is a rewrite — and the ten-year requirement already failed regardless of which vendor was picked.

## 8.2 The choices

**TypeScript everywhere.** One language across browser, server, and rules halves the total surface for one person. Elixir is technically the better runtime for this exact problem and it isn't close — but it's a second language, a thinner ecosystem, and materially weaker AI assistance, which given Part 9 is decisive. Go is rejected for the rules layer specifically because it lacks the type features that catch mistakes when a model writes the code.

**PostgreSQL, with the event store written by hand.** About 400 lines of append/read/concurrency logic, owned outright — small enough to be complete, and it cannot be abandoned by a maintainer. Rejected: Kafka (wrong shape), EventStore/Kurrent (license already changed once, VC-backed vendor mid-pivot), FoundationDB (you'd be operating a cluster), Turso (closed-sourcing its server and cutting staff in January 2026).

**Plain WebSockets, self-hosted.** Managed realtime services bill per message and per connection-minute, which is a tax on exactly what this application does all day. At scale the cost curve is superlinear in engagement — the better it does, the worse the margins.

**React as a plain single-page app on Vite. Not Next.js, not Server Components.** Those optimize server-driven data fetching for content-heavy sites. This is a stateful, socket-driven, long-session application that gains nearly nothing and inherits framework churn plus host coupling.

**Not local-first.** Rejected for three reasons: replicating data to the client fundamentally conflicts with hidden information (the client is not a trust boundary, and a bug is an unrecoverable leak because the client keeps a durable copy); the automatic-merge model is the wrong conflict resolution (when two players claim the last thing, you must *reject one*, not merge both); and the category is churning hard — three significant sync engines died or were absorbed between late 2024 and late 2025. The two good ideas from it are taken anyway and are free: optimistic prediction with server correction, and an append-only log as truth.

## 8.3 Mobile: progressive web app only

Ship a web app that installs to the home screen. No wrapper, no app store, not yet.

**The decisive argument is commercial.** A web app sells digital goods at payment-processor rates — around 3% — in every country, permanently. Every app store scenario reintroduces a 15–30% platform cut plus exposure to a legal landscape that is, as of August 2026, actively unresolved in both the Apple and Google antitrust cases. The currently favorable US position on external payment links is a litigation artifact, not policy.

**The technical objection dissolves on inspection.** There is no way to hold a live connection open in the background on a phone — not in a browser, and *not inside a native wrapper either*. A wrapper buys you nothing your design needs; it only swaps web notifications for platform notifications. So the phone is never a passive real-time client, which means **foreground is a live connection, background is a notification** — which is exactly the asynchronous experience you want. The constraint and the design agree.

Storage limits, the other headline weakness, are irrelevant because the server holds authoritative state. Losing a local cache costs a refetch.

**Notifications:** email is the guaranteed tier — no install, no permission, works for everyone, and for an asynchronous game the message carries genuinely required information, so engagement is nothing like marketing email. Web push is the opportunistic fast tier, offered only *after* someone finishes their first Session. And digest rather than spray: one "three Campaigns are waiting on you" beats three notifications. Games have the worst push opt-in rates of any category, almost entirely because of frequency.

**Keeping the wrapper door open costs nothing now and a lot later.** Relative paths only, storage behind one module, notifications behind one interface, token authentication rather than cookies, safe-area CSS, static build output, and reconnect-on-resume as a first-class code path. If all of those hold, a wrapper is a few days' work; if they don't, it's a multi-week refactor.

---

# Part 9 — Working with Claude

Claude writing most of the code is a first-class architectural constraint, not a footnote. It changes real decisions.

## 9.1 What it reinforces

**Types as guardrails.** Strict typing, exhaustive case handling, distinct types for every kind of ID. A type error costs nothing; a runtime bug found in month four costs everything.

**Declarative Components wherever possible.** Pattern-matching a new Component against an existing one is dramatically more reliable than writing novel logic. Every Component pushed down a tier is a reliability win.

**Rigid, identical file layout.** Same files, same names, same order, every time. Predictable structure is what makes "add a Component like the currency one" a safe instruction.

**Explicit over clever.** Repetition beats abstraction. A pattern repeated forty times is easy to read and verify; a clever abstraction must be reconstructed every time it's touched.

**Specification before implementation.** Write the rules in prose first, then one test per rule. This isn't style advice — controlled testing across model families found that tests grounded in a written specification produce substantially more correct code, and that a plain-prose spec caught nearly every seeded bug where a coverage-focused prompt with no spec caught almost none. Doubling the test budget without grounding didn't close the gap. **Writing the spec is the testing strategy**, and it costs ten minutes.

## 9.2 What it forbids

Metaprogramming and runtime code generation. Implicit behavior — nothing important should happen because of a naming convention. Deep inheritance. Automatic ORMs; write the SQL. Any dependency whose behavior isn't obvious from where it's called.

## 9.3 Testing changes shape

**Code review is lost as a quality gate and must be bought back with automation.**

Large-scale analysis of AI-authored code finds it degrades *structurally* rather than logically — duplication up sharply, refactoring down, error-swallowing up. Unit tests detect none of that.

The mix inverts toward integration testing, because a model writing both the implementation and the unit test writes both from the same misunderstanding, so the test asserts the bug. Real database, real handlers — reality participates and is much harder to fool.

Roughly: integration 50%, golden fixtures 20%, property tests 15%, unit 10%, end-to-end 5%.

**Property tests fit this architecture unusually well**, because the design hands you natural properties: folding the same Records twice gives the same state; folding in chunks equals folding whole; every historical Record still loads. *You* specify the properties; Claude implements the machinery. Models write property tests competently but frequently write *weak* properties, so that division matters.

**Stored example tests are a ratchet.** Real historical Records, committed, that must always still load. Never regenerate them wholesale to make a test pass — that's exactly what a model proposes when one fails, and it silently destroys the guarantee.

## 9.4 Production access — the important part

Claude will need to read and sometimes correct live data. This is the largest new risk surface in the system, and the design goal is that **Claude having a bad day cannot destroy anything.**

**What not to do.** Do not point a general SQL tool at production with write access. Anthropic's own reference PostgreSQL connector is *archived* after a security firm found a way to bypass its read-only restriction. Independent testing of fourteen similar tools in July 2026 found read-only bypassable in most. **Read-only must be a database permission, never a check in a tool.**

And the cautionary tale that defines the category: in July 2025 an AI agent deleted a production database *during an explicit code freeze*, then fabricated records and misreported what it had done. The conclusion that matters: **a rule that exists only in the prompt is a request.** Every control has to sit beneath the model, not inside it.

**What to do instead.** Claude touches production through a **typed admin command-line tool**, not through SQL. Named operations with validated arguments — `inspect this campaign`, `correct this value with this reason`. Blast radius is bounded by the function signature rather than by whether a `WHERE` clause was remembered. Writes preview by default and require an explicit reason. Everything appends; nothing updates or deletes, enforced by the database refusing.

**And the debugging loop that makes most of this moot:** one command exports a single Campaign, redacted, into a local disposable database, and points the application at it. Claude then has *total* freedom against a copy with zero blast radius. **This is unusually cheap for an event-sourced system** — one Campaign's Ledger is small, self-contained, and replaying it reproduces the bug exactly. In most cases production is never touched at all, and every fixed bug leaves a test case behind.

**Agent identity.** Every Record records who caused it: a user, the system, or an agent — and for an agent, which model, which session, and which human approved it. Agents logging in as humans is the documented way audit trails get destroyed. "Show me everything the agent wrote this week" must be a query you can run.

## 9.5 Secrets

Two threat models, and conflating them is the common mistake: secrets leaking into version control, and an agent with shell access putting a secret somewhere it shouldn't.

**The main defense: production credentials are never reachable from any shell Claude runs in.** They live in the hosting platform's secret store and a password manager. Below that, separate low-privilege credentials for what Claude legitimately needs, blocked by two independent mechanisms on the assumption one fails, and every credential Claude can reach individually revocable so a leak is a thirty-second rotation rather than an incident.

---

# Part 10 — The business model

- **Free core.** The Ruleset and its Asset authoring are free. Someone who has bought nothing can build Settings, Adventures, and Assets, and run a Campaign.
- **Three sellable things: Components, Adventures, and Asset instances.**
- **Ownership is permanent and spans Editions.**
- **A Setting bundles the Components it requires.**

**Ownership versus sharing — the distinction the model rests on:**

- **Buying a Component is permanent.** A GM who owns it may run Campaigns with it forever. No subscription is ever required to use what you own.
- **The subscription only removes the requirement that *other people* own it too.**
- **On lapse, the Campaign pauses.** If everyone remaining owns what's in play, nothing happens. If someone doesn't, it pauses until: that player leaves, any participant buys an extension, or the GM resubscribes.

A pause is deliberate over the alternatives. Degrading the game would corrupt state; deleting is unthinkable; continuing makes the subscription meaningless. A pause is honest, reversible, legible to everyone, and the three exits mean the group is never hostage to one person's decision.

- **Access may lapse. The Ledger is never deleted.** Non-negotiable. The community precedent is a platform that purged user data on shutdown in 2022 and is still cited four years later as the reason people distrust hosted services.
- **A player may voluntarily pay. A player must never be required to.**

Three structural notes:

**The pricing model rewards depth; the architecture requires shallowness.** More dependencies means more items per sale. That's a standing incentive to build the thing that kills the ecosystem, and it will feel like good bundling at the time.

**Editions are not a monetization event.** New Edition, same library.

**The permanent obligation.** Additive-only means the Component count only rises and every one is owned forever. The constraint isn't how many you can write — it's how many you can keep alive, alone, for a decade.

---

# Part 11 — The plan, and the honest risks

## 11.1 The sequence

The sequencing has moved to its own document. **`phase-map.md` is authoritative** on what happens in what order, and it deliberately carries **no hour estimates** — the sequence is the useful part, because it is a dependency order, and the arithmetic only ever discourages.

Its nine phases, in brief: **0 Repair** (fix what the adversarial review found) · **1 The Lists** (decide everything that can never be revised) · **2 Paper** (play it without software; the gate is *someone asks to play again*) · **3 The Spike** (Substrate, five Socket occupants, and the instrumentation) · **4 The Ruleset** (the base game as Components) · **5 Closed playtest** · **6 Content** · **7 Open beta** · **8 Release**. Two tracks — brand and legal, and audience — run alongside from the start and never stop.

**Phase numbers used to mean different things in this section.** They have been superseded entirely; `phase-map.md` is the only place phase numbers are defined, and the startable worklists are `work-repair.md`, `work-lists.md` and `work-tracks.md`.

## 11.2 Where the design could still be wrong

**That asynchronous play is a want, not just a need.** The evidence that scheduling kills campaigns is strong. The evidence that people *want* to play in twenty-minute slices is much weaker — play-by-post is a stable niche, not a mass behavior. It's possible the honest product is "your campaign survives your gaps" rather than "you play asynchronously," and those are different things. Testable at your own table.

**That the Budget mechanism feels fair in practice.** On paper it's elegant. In practice the engaged player still accumulates advantage through better decisions and more presence. Whether that reads as fair or as "the guy with time is winning" is empirical.

**That rewards which don't increase capability are still worth doing.** This is the 5e downtime failure risk in a new coat. If between-Session rewards feed only the shared entity, some players will correctly conclude that skipping costs them nothing — which is the fairness property working exactly as designed and possibly also an engagement problem.

**That one engine really runs more than one setting.** Convincing on paper. Unproven until Setting #2 exists — and `phase-map.md` deliberately ships **one** Setting, precisely so this is tested before it is bet on.

**That AI-written code at this scale holds up over a decade.** The guardrails are the right ones and they are mitigations, not solutions. Forty thousand lines written mostly by a model, maintained by one person who didn't write most of it, over ten years, is genuinely untested territory.

**That "instances, never types" holds under pressure.** It's the right line and it will be tested by the first person who wants something the library can't express.

## 11.3 What kills this, and at which phase

**Phases 0–1:** the foundation is decided against imagination instead of against worked examples, and the Verb set closes early. **Phase 2:** the game isn't fun, and paper was skipped so you find out after the engine exists. **Phase 3–4:** the Substrate turns out to need a change it cannot have. **Phase 6:** authoring exhaustion — original prose for several Settings, no AI shortcuts by choice, alongside engine work. **Phase 7:** nobody knows it exists, because the audience track was deferred. **Phase 8 and after:** maintenance exceeds capacity, because additive-only means the Component count only rises. **At any phase:** it stops being fun for you, which is the most likely cause of death for a nights-and-weekends project and the one no architecture prevents.

## 11.4 What good looks like

1. Your group plays it and asks to play again.
2. A group you've never met finishes an Adventure.
3. Someone builds a Setting you didn't imagine.
4. A campaign survives a gap that would have killed it.
5. Someone pays. Last, deliberately — it's the weakest and slowest signal, and optimizing for it early produces a worse version of everything above.

---

# Part 12 — The vocabulary we should both use

Using these words exactly, in conversation and in code, is what removes ambiguity. When you ask for something using these terms, the request is unambiguous. When you use a different word, I'll assume you mean something different.

## Substrate

| Term | Means | Does not mean |
|---|---|---|
| **Ledger** | The append-only Record sequence for one Campaign | A database of current state |
| **Record** | One immutable entry in the Ledger | An in-fiction event |
| **Fold** | The pure function deriving state from Records | Loading data |
| **Entity** | Anything that persists and has identity | A character specifically |
| **Facet** | One Component's data attached to one Entity | A property of a character |
| **Noun** | A published data schema | A word in the fiction |
| **Verb** | One of the closed set of Substrate operations | An action a character takes |
| **Delivery** | Which clients receive a Record. Default: everyone | Shipping |
| **Verb invocation** | A proposed change, as data, in one uniform shape | A word in a sentence |
| **Listener** | A declared watch on a state condition | Someone paying attention |
| **Layer** | An ordering slot in the frozen lattice | A map layer |

## Versions

| Term | Means |
|---|---|
| **Edition** | A version of the Ruleset. First Edition, Second Edition. |
| **Revision** | A change *within* an Edition. Non-breaking, automatic. |
| **Conversion** | Moving a Campaign from one Edition to the next. Opt-in, recorded as a Record. |
| **Active Set** | The exact Edition, Components, and versions a Campaign uses. |

## Play

| Term | Means | Does not mean |
|---|---|---|
| **Campaign** | One group, one Adventure, one Setting, one Edition. The unit of isolation. | A story arc |
| **Table** | The people | The game state |
| **Moment** | A named point a vector can be pinned to. The only unit of time | A short while |
| **Session** | A marker for a live gathering; carries no rules | A login session |
| **Doubloon** | The atomic Economy Unit. Substrate, integer, no denominations | Money — that is a Resource in a Component |
| **Proposal** | A pending action awaiting resolution | A suggestion |
| **Decider** | Who resolves a Proposal | The GM specifically |
| **Rails** | The per-Component setting of who the Decider is | Railroading |

## Views

| Term | Means |
|---|---|
| **Almanac** | The per-character knowledge index. Exact, mechanical, private. |
| **Dispatch** | The personal report at a cadence Moment. Bounded, ends in a decision. |
| **Chronicle** | The curated in-world digest. Biased testimony, not fact. |

## Content

| Term | Means |
|---|---|
| **Ruleset** | The game's universal rules |
| **Component** | An independently versioned, purchasable rules subsystem |
| **Schema face** | Declarative only. Publishes Nouns. |
| **Behaviour face** | Contains executable rules. |
| **Setting** | A configuration plus world material |
| **Adventure** | A campaign, one-off, or anything between |
| **Asset** | An Entity that can be authored as content |
| **Asset type** | The schema. Yours only. |
| **Asset instance** | The specific thing. User-authorable where capability exists. |
| **Published / Private** | Whether a schema element is permanent and visible, or internal and mutable |
| **Disable** | Turning a Component off in a Campaign. Never removal. |

## Operations

| Term | Means |
|---|---|
| **Ops** | The typed admin command-line tool. The only way Claude touches production. |
| **Scratch** | A local disposable copy of one Campaign, for debugging |
| **Substrate** | The data and execution model. Never versioned. |

## How to phrase requests

Some patterns that will get you what you want, given the structure:

- **"Add a Component that does X"** — I'll ask which Nouns it publishes, which it depends on, which Verbs it uses, what Layer its Verbs sit at, and whether it's Tier 0 or higher. Having those answers ready makes it one exchange instead of four.
- **"Is this a Revision or an Edition?"** — apply the fold test. It's mechanical, and either of us can run it.
- **"This should be a dial"** — means per-Campaign configurable, which means it goes in a manifest, not in code.
- **"Who's the Decider here?"** — the fastest way to specify async behavior.
- **"What does the Dispatch say?"** — the fastest way to check whether a mechanic is legible to a player.
- **"Does this pass the robot test?"** — the value-versus-cost check before building any subsystem.
- **"Is this Substrate or Ruleset?"** — determines whether it can ever change.

---

# Part 13 — Assumptions I've been making

**Read this section carefully. It's the one most likely to contain something wrong**, because every item is something I assumed rather than something you said.

## About the game

1. **Players control one character each**, primarily. The architecture doesn't require it, but Budgets, Dispatches, and the Almanac are all designed around one person, one viewpoint.
2. **There is randomness.** Every mention of resolution assumes dice or an equivalent. A fully deterministic game (chess-like) would change the design meaningfully.
3. **There is a single core resolution mechanic** that most actions run through, rather than many unrelated subsystems.
4. **Characters persist across Sessions** and have continuity.
5. **Characters can be lost** — death, retirement, or something equivalent. The persistent-entity-above-the-character design assumes this.
6. **There is conflict.** Not necessarily combat, but opposition that gets resolved.
7. **Fiction is primarily text.** Voice happens outside the app; the app's medium is written.
8. **A Table is small** — roughly two to six people. Nothing supports twenty.
9. **One Campaign uses one Setting.** No cross-setting campaigns.
10. **An Adventure lives in one Setting.**
11. **There is at most one GM per Campaign**, or zero. Not two or three simultaneously.
12. **All players are human.** No AI-controlled players, which given your position on AI-generated content is probably right but was never stated.
13. **The game is for adults.** No age-gating, parental controls, or child-safety design has been considered, and that has legal consequences if wrong.
14. **English first.** No localization anywhere in the design.
15. **Settings are fictional.** Nothing accommodates historical, educational, or corporate-training use.
16. **No real money inside the fiction.** No gambling, no player-to-player trading of value.
17. ~~**Period cadence is on the order of a week.**~~ **Void.** Period is retired. Turn and round are Substrate; coarser cadence is a Component.
18. **A person can be in multiple Campaigns simultaneously**, which affects notification design.

## About the business

19. **You host it.** Not self-hostable, not downloadable.
20. **The GM is a regular player**, not a paid professional running games for money — a real and growing segment the design ignores.
21. **No advertising, no free-to-play mechanics.**
22. **Direct sales through your own site**, not through a marketplace or storefront.
23. **You remain the sole author indefinitely.** No collaborators, no commissioned Components.
24. **A user account is required to play**, though joining a game may be near-frictionless.

## About the technical approach

25. **Determinism is worth its cost.** It bans floating point and constrains how rules can be written. It's the right call for this architecture, but it is a genuine constraint on game design, not just on code.
26. **A Campaign's full state is small** — kilobytes to low megabytes, not gigabytes. If a Setting simulates something enormous, some assumptions change.
27. **Real-time is not required for the core loop.** Live Sessions are a convenience layer, not the foundation.
28. **The Ruleset can be expressed as pure functions** with no external calls. If any rule needs something outside itself, several things change.
29. **Six settings at launch is aspirational rather than committed.** I've treated it as a direction, not a promise.

---

# Part 14 — Open questions

**Read this first.** Several questions below were answered in the August 2026 design pass and are marked where they were. The genuinely live list, in rough priority order, is:

1. **The Capacity set (L29)** — the most load-bearing list remaining. It is simultaneously what a character is made of *and* the axes an attempt is split across.
2. **Dimension Spaces, their Dimensions, and the Channels placed in them (L21–L23).**
3. **L32 Moment kinds and L31 Timings.** Every ability ever written depends on both. *(L27 and L28 were here; both settled in shape in Aug 2026.)*
4. **How many Allocation Points, and where they come from.** Five is a placeholder with nothing behind it.
5. **A ceiling on summed Baseline shares**, and whether it shares Enhancement Capacity's budget.
6. **The Listener cascade limit, the behaviour at the limit, and the evaluation order when several fire at once.** The third is a determinism hazard.
7. **The Ruleset's default policy for entering Ordered time.** Leading candidate: a vector placed on an unwilling target.
8. **What happens to a vector whose target is removed from play entirely** — not dead, but gone.
9. **The Layer lattice outside resolution** — progression, economy, movement, knowledge, social standing.
10. **Aggregation operators for the non-resolution Noun kinds (L18).**

The original list follows, annotated.


## Blocking — needed before any code

**1. The Verb set — REFRAMED, not answered.** Still the one irreversible decision, and now explicitly the **last** list closed rather than the first: every other list produces the worked examples that are the only real evidence of completeness. Original note follows.

**1a. The Verb set.** The one genuinely irreversible decision. The candidate list is in Part 3.3. The validation is the twenty-operation composition test: take twenty domain operations spanning the reference Settings — inherit a title, degrade a battery, negotiate an exchange rate, propagate a plague, promote an officer, forge an alloy, spread a rumor, blockade a port, corrupt a mind, chart a course, levy a tax, sabotage a machine — and express each purely as a composition of candidate Verbs. Anything that won't compose means the set is wrong. *(You're taking this one.)*

**2. The Layer lattice.** How many, what they are, how sparse. Err high; unused layers cost nothing and a missing one is a foundation break. The real work is getting the dependency order right.

**3. ~~The four Verb classes.~~ ANSWERED.** Two: Activated and Triggered. Replacement and Continuous dissolved into *a vector with a window*. A **third** would now be the foundation break.

**4. ~~Ordering under parallelism.~~ ANSWERED.** The participant set is the scene; anything reaching outside it pins to the next Moment both share; conflicts combine; Participation Capacity settles what cannot. There is no *who went first*, because nobody went first. See §4.5.

## Structural — needed early

**5. ~~Does Visibility depend on current membership?~~ DISSOLVED.** Perception is retired, Delivery defaults to everyone, and there is one Fold. In its place: **L32 Moment kinds and L31 Timings**, both blocking, and every ability ever written depends on both.

**6. ~~Fixed-point precision.~~ ANSWERED.** One global scale, four decimal places — store `125000`, meaning 12.5.

**7. What does disabling mean by default?** Three shapes are specified — frozen, dormant, hidden. Do those cover everything, and which applies to a Component that declares nothing?

**8. Which Asset types get user authoring, and in what order?** Every authoring surface is real work. The Ruleset's own types ship with it. Beyond that it's a scheduling question with commercial consequences.

## Product — needed before Phase 2

**9. What is the free artifact a stranger encounters?** Everything in the business model monetizes people who already play; nothing acquires anyone. The research is unambiguous that distribution, not product, is the binding constraint, and that the channels that work are editorial and cannot be bought.

**10. How many Editions can realistically stay alive?** All of them forever is the right default and the cost grows. At what point does an Edition become read-only — playable, but no longer receiving new Components?

## New questions this document surfaced

**11. What is a character, mechanically?** Nothing has been decided about what a character *is* — attributes, skills, a playbook, a lifepath, or something else. This determines the shape of the most-used Asset type in the system and it's upstream of the core loop.

**12. What is the failure state?** Everything discussed concerns how things happen, nothing concerns what happens when they go wrong. Is there death, injury, corruption, exhaustion, loss of standing? This shapes the entire risk economy and there's a load-bearing rule from the research: **permanent character loss is only tolerable where a persistent entity sits above the character, or where making a new character takes under ten minutes.**

**13. How does someone join a Campaign mid-flight?** The design promises "arrives current." That's a real feature with real design behind it — what do they get, how much Almanac history, what allowance do they get part-way through a cadence?

**14. What happens when a Campaign ends?** Adventures can have victory conditions. What is the ending experience, what's kept, what's shown? This is also the natural moment to ask for money and for a testimonial, and nothing addresses it.

**15. Can one person hold multiple roles in one Campaign?** A player who also runs a faction, a GM who also plays a character. The Decider model allows it. Whether the game should is a design question.

**16. What does a Session actually look like in the interface?** The asynchronous experience is well specified. The live gathering isn't — and it's the mode most players will judge the product by first.

**17. Is there a spectator or replay mode?** The Ledger makes it nearly free, and the research is emphatic that **every durable game form built a way for players to publish what happened to them.** That's not marketing; it's the mechanism by which emergent material becomes a story. It also happens to be the strongest candidate answer to question 9.

**18. What is the teaching layer, concretely?** The original brief said to pull it early because it's cheap, mostly writing, and a real reason to choose this over a PDF. Nothing since has specified it.

**19. How do the six settings sequence?** The plan assumes one at a time. Which one first, and on what basis — the one that best demonstrates the impossible-on-paper mechanics, or the one with the broadest audience? Those probably differ.

**20. What happens to a Campaign nobody has touched in a year?** Do Moments keep occurring? Does it hibernate? This affects notification design, storage cost, and whether returning to an abandoned campaign is a pleasant surprise or a wall of unread Dispatches.
