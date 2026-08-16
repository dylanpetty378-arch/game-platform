# Tabletop Field Survey — What It Means For This Project

Synthesized from nine parallel research passes, August 2026. Organized by consequence for the design, not by topic. Everything here is oriented toward one question: what should change about the plan.

Sourcing caveat up front: several passes hit search-budget limits and Reddit was blocked at the proxy throughout, so community-sentiment claims are thinner than the market and design-literature claims. Where a number is soft, it says so.

---

## 1. The tool that reorganizes everything

The single most useful thing to come out of this survey is a diagnostic, and it should be applied to every design decision from here forward.

**Paper constraints produce cost problems. Human constraints produce value problems. Automation lowers cost. It cannot manufacture value.**

A rule gets abandoned at a table for one of two reasons: it costs more than it's worth, or it isn't worth anything. Both look identical in practice — the rule stops being used — which is why the design literature keeps conflating them and why "we finally fixed encumbrance" keeps failing.

**The test:** if a perfect, free, invisible robot did every calculation and every write-operation for this subsystem, would the table still want it in the game?

- **Yes** → cost failure → paper problem → automate it.
- **No** → value failure → design problem → cut it or rebuild the choice it was supposed to create.

The corollary matters more than the test: **automating a value-failed subsystem is actively harmful.** You convert an ignored rule into an invisible one, and now the table can't even notice it to argue with it.

The proof case is light and torch tracking. Every paper-side fix ever proposed is a write-operation reduction technique — slots, usage dice, bundling. None of them made anyone want the subsystem. What experienced GMs said actually fixed it was making light *matter*: targetable in combat, a vulnerability, a puzzle input. That's a value fix. Perfect automated tracking would have changed nothing.

### What this does to the seven constraints

Sorting our earlier list through the test:

**Genuine paper problems, fully dissolved by the medium** — continuous-state bookkeeping, off-screen world simulation, rules retrieval, in-resolution arithmetic, character creation arithmetic, prep-as-transcription, random generation, continuity recall. All real. All table stakes. **None of them differentiate**, because every VTT already claims them and the ones that don't are free.

**Human problems the medium barely touches** — scheduling and attrition, the invention half of GM burnout, mismatched play expectations, alpha-player dynamics, analysis paralysis, system mastery as social exclusion, blank-page anxiety, table chemistry.

**The three places the medium gives real leverage on a human problem:**

1. **Hidden and asymmetric information** — paper handles this with GM-screen kludges. This is also the structural fix the alpha-player literature identifies: the disease is a game with a solvable optimal line and complete shared information.
2. **Progressive disclosure** — paper physically cannot withhold a rule until it's relevant. Digital can. This is a real, uncopyable advantage.
3. **Asynchronous scheduling** — the only design-side lever on the single largest cause of campaign death.

That is the competitive surface. Three items, not seven. The other four are necessary and insufficient.

### The hard middle — where the distinction earns its keep

Combat length decomposes into per-action resolution overhead (paper), decision latency (human), round count from HP math (design), and dead time × turn count (structural). Digital fixes only the first, which is usually the *minority* of elapsed wall-clock time. **This is why VTTs demonstrably speed up arithmetic and demonstrably do not make combat feel short.** Measure only the part you fixed and you'll conclude the medium was the problem and be wrong.

Character creation decomposes identically. Rules lookup: search solves retrieval, not "I didn't know this rule existed" and not "the rule doesn't cover this case."

And one active harm vector worth naming: **code-enforced rules destroy the ruling space that fiction-first play depends on.** A medium change that solves a cost problem can eliminate a value source. This is the strongest independent argument for the ledger-not-rules-engine position already in the brief — it arrives from a completely different direction and lands in the same place.

---

## 2. The business reality

This is the least pleasant section and the most important one.

### Charging for tabletop software is over, and it ended recently

Within a four-month window in late 2025:

- **Fantasy Grounds went free-to-play** (Nov 2025), abandoning both its $39.99 and $149.99 one-time tiers and its subscriptions. Revenue is now content only.
- **Alchemy removed all free-tier limits** (Nov 2025), moving to a $5/mo voluntary supporter model.
- **D&D Beyond Maps was made free to everyone** (Sep 2025), previously subscription-gated.

Meanwhile **Sigil** — Wizards' 3D VTT, the best-funded attempt in the history of the category — launched Feb 2025, lost ~90% of its team to layoffs three weeks later, was cancelled Oct 2025, and its servers go dark 31 Oct 2026 with all user content destroyed. The internal statement: "our aspirations for Sigil as a large, standalone game with a distinct monetization path will not be realized."

This is the second time Wizards has failed at a first-party VTT; the D&D Insider Virtual Table died in 2012.

**If Hasbro cannot monetize standalone tabletop software to D&D players, the willingness-to-pay problem is structural, not executional.**

The reference price that now defines expectations is **Foundry at $50 one-time, perpetual, self-hosted, free updates forever.** A GM who has paid that once will not pay a subscription.

### The willingness-to-pay ladder

What this audience demonstrably pays:

| For | Price |
|---|---|
| A human GM running a session | **$20–30/session** |
| An official sourcebook | $25–30 |
| Indie PDF rulebook | $10–25 |
| VTT subscription, mid tier | $6–11/mo |
| VTT, perpetual license | $50 once |

Read it as: **high willingness to pay for content and human labor, low willingness to pay for tooling.** Tooling is perceived as infrastructure that should be free — and now largely is.

Validation of the services observation: StartPlaying has ~5,000 pro GMs, ~80,000 players, has paid out **over $50M to GMs since 2019**, and raised its take rate from 10% to 15% in Jan 2025 without losing supply.

### The publishing numbers

RPG crowdfunding, full series:

| Year | Projects | Total | Median |
|---|---|---|---|
| 2013 | 267 | $10.99M | **$10,410** |
| 2019 | 839 | $33.53M | $6,442 |
| 2021 | 1,460 | $91.37M | $6,886 |
| 2023 | 1,908 | $73.73M | $4,723 |
| 2024 | 2,190 | $91.04M | $3,867 |
| **2025** | **2,331** | **$66.99M** | **$3,640** |

Project count up 8.7x since 2013. **Median funding down 65%.** 2025 set a record for project count, the lowest mean since 2014, and the lowest median ever recorded, while total dollars fell 26% year over year.

Of 2,331 funded projects in 2025: 71 cleared $100k (3.0%), six cleared $1M (0.26%). The top three were ALIEN (licensed IP), Shadowdark (post-ENNIE-sweep incumbent), and Fabula Ultima (established). Q1 2026 analysis, verbatim: *"most successes stem from already popular properties."*

For scale on the ceiling: **Evil Hat — a respected publisher with a twenty-year catalogue — did $600k in 2025.**

### The bottleneck is distribution, and the currency is an owned audience

The evidence converges hard and from multiple directions:

- **It is not product.** 2,331 funded projects in 2025. Supply of competent original systems vastly exceeds demand. A better game does not get found.
- **It is not capital.** Shadowdark was self-published by one designer with no funding and hit $2.4M on its second campaign — she had an audience, built by giving away content and sweeping the 2024 ENNIEs. Hasbro had unlimited capital and wrote off $56M on cancelled D&D games plus the entire Sigil team.
- MCDM's $12.8M lifetime crowdfunding came from a YouTube channel built *before* the first campaign. Daggerheart went from zero to a top-3 system in one year on Critical Role's existing audience.

And the structural reason capital doesn't help: **the channels that work are editorial and cannot be purchased.** Newsletters (the Glatisant), reviewers (Questing Beast et al.), awards (ENNIEs are free to enter), and actual play. The purchasable channels — Kickstarter category browse, itch discovery, podcast ads at a $22 gaming-category CPM — don't convert. Reddit forbids promotion outright.

### What this means for sequencing

**Audience → system → software.** Every failure in the record inverted this order; every success followed it.

Software revenue for a bespoke original system is bounded by players of that system, which is zero at launch. Realistic year-one direct software revenue is approximately **$0 regardless of quality.** At $5/mo, $60k/yr requires 1,000 continuously-paying subscribers, which at typical freemium conversion needs 20,000–33,000 active free users — and only the GM pays, so several times that in registered accounts. That's top-ten-system play share.

**The software is not a revenue line. At best it is the differentiator that makes the system findable; at worst it is the maintenance obligation that ends the project.**

One structural churn problem unique to this category: a campaign has a natural end and campaigns collapse constantly. When the group stops meeting, the GM cancels. Churn is driven by an exogenous social event no product feature can influence.

### The one genuinely good piece of news

The 2023 OGL crisis ended with SRD 5.1 and 5.2 released **irrevocably under Creative Commons.** The legal moat around building tabletop software is gone permanently. The OrcPub failure mode — free tool killed by cease-and-desist — no longer exists.

---

## 3. What the research validates

### The async gap is real, large, and unserved

Forum play-by-post is measurable and alive: **RPoL has 4,314 active games, 128,771 registered users, ~9M posts, 8+ new games created per day.** Myth-Weavers has 1,350+ active games across 148 systems. Discord PBP is larger and entirely uncounted.

Every named failure mode of play-by-post is structural and software-addressable:

- glacial pace
- ghosting and dropout as the dominant killer
- **the GM's posting rate as a single point of failure**
- initiative-order combat as the specific place games die
- player count inversely correlated with pace

**Not one platform in the VTT space is designed for this.** They are all built for a synchronous session — which the hobby's own leadership says is getting harder to schedule. Dan Ayoub, SVP and head of D&D, at GamesBeat Summit on 3 Aug 2026: the most consistent feedback he receives is that *"players' lives have changed in such a way that makes D&D impractical. How do we create other forms of engagement — whether you have 20 minutes or 6 hours?"*

The largest company in the category has publicly identified the problem and is chasing it with seasonal content and shorter experiences. That is confirmation of the thesis and a warning about the clock.

### The four-layer model, and the mortality answer

The layered model — ruleset / setting / adventure / campaign — is well-supported, and the adventure layer does more work than expected.

**The only design-side intervention against campaign mortality with any community validation is a structurally terminating campaign.** Groups running deliberate ten-session arcs with fixed endings report finishing them. Everything else in the literature is a GM-behavior recommendation, not a design one.

That's not an argument for short sessions — it's an argument for the adventure layer having a *shape and an ending*, which is already in the model. The exit ramp is a structural feature, not a failure.

Data on mortality is genuinely bad — the best available is a self-selected forum poll (n=263) showing 28% of respondents never finished a campaign, and a D&D Beyond level distribution routinely misused as attrition data. The widely-quoted "37% never finish" figure has no traceable provenance. Don't cite it. But the *reasons* cited are consistent everywhere: scheduling and adult life first, player churn second, GM burnout third.

### Rationed budgets solve the between-session fairness problem

This answers the concern directly: how do you let players act between sessions without disadvantaging those who don't?

**Blades in the Dark:** two downtime activities per character, free. Extras cost coin or reputation. Six activities compete for two slots.

**D&D 5e:** fifteen listed activities, no budget, no opportunity cost, payoffs deliberately capped below adventuring. Comprehensively abandoned; Wizards replaced the rules twice and a reviewer's summary is that they "felt like a tax to players."

**The principle: between-session decisions require a rationed action budget, not an activity list.** Every system that produces real between-session decisions rations something — actions, seasons, years, coin, morale, supplies. Every system that fails offers a menu without a budget.

A budget is also the fairness mechanism. If everyone gets two actions per cycle, the player with fifteen spare hours and the player with twenty spare minutes make the same number of decisions. The engaged player gets to think harder, not act more.

Also relevant: Ars Magica gives each magus four seasons per year with competing uses, and Pendragon's Winter Phase is an eleven-step mandatory annual procedure. Both are the highest-decision-density between-session systems in the hobby, and both are hand-maintained. This is a genuine cost failure by the robot test — automate freely.

### Asymmetric rules: validated, with a specific pattern

The pattern the research supports is **"differentiate the verbs, share the physics."**

Systems with the deepest rules-level asymmetry — Ars Magica's magi versus grogs, D&D's casters versus martials — have the hobby's longest-running spotlight-balance complaints, and both address them non-mechanically (troupe rotation, DM pacing). Systems that wanted asymmetry without the spotlight problem — Blades, PbtA — pushed it into move and ability lists layered over an **identical resolution and consequence chassis**.

That maps cleanly onto the three ruleset tiers. Base layer = the physics, shared and fully open. Setting layer = the vocabulary and the world's rules. Individual layer = the verbs, private, genuinely different per player.

One warning from Band of Blades, which distributes GM-adjacent authority across Commander, Marshal, and Quartermaster roles: those roles produced "practically never embodiment type roleplay." **If you split authority, give each role a character, not just a domain.**

### Tooling drives adoption — but isn't sufficient

**Lancer is the #3 most-played system on Foundry VTT in 2026, above Call of Cthulhu and Warhammer Fantasy.** An indie mech game. The reason is COMP/CON — free, open source, and the only tractable way to build a Lancer mech. Daggerheart hit #9 within a year on the back of Demiplane, with 500,000+ characters created by Aug 2025.

Counter-example: **Shadowdark reached $2.4M with essentially zero first-party digital tooling.**

Tooling is a lever, not a requirement. But it's a real one, and it's the lever available here.

### The number to beat

**57% of GMs spend 2+ hours preparing a 4-hour session**, with 29% spending 3+ (n=3,663, self-selected). Any tool that adds prep has to return more than it takes — which is exactly why the two VTTs that are growing are the two with the lowest setup cost: Owlbear Rodeo (drag a map, share a link) and D&D Beyond Maps (maps arrive pre-placed because you bought the book).

---

## 4. What the research corrects

### A world that runs continuously without a deadline is a welfare hazard

This is the sharpest correction, and it cuts against something we'd been treating as pure upside.

Every durable asynchronous form in history ran on **a shared, externally-enforced deadline.** Play-by-mail's fortnightly cycle. Diplomacy's phase timer. Correspondence chess at 30–60 days per ten moves. The cadence *is* the product.

The counter-example is **Neptune's Pride** — continuous real-time progression that runs whether or not you're logged in. It's notorious for sleep deprivation and damaged friendships. (That reputation is widely reported and I could not verify it directly this pass, so treat the anecdote as soft — but the mechanism is sound.) **Without a turn boundary, engagement becomes vigilance,** and the player who checks at 3am gains a real advantage over the one who doesn't.

**A deadline you cannot privately renegotiate protects players from each other and from themselves.** "The world keeps moving" needs to mean "the world advances on a cadence everyone can see," not "the world runs in real time."

### Simulation without curation produces noise, not life

Constraint five — simulate what the setting needs — is where this bites hardest.

Tynan Sylvester's *The Simulation Dream* is the essential result: there is the **Game Model** (what the code simulates) and the **Player Model** (what the player mentally reconstructs). **Only the Player Model produces experience.** Anything in the Game Model that doesn't transfer is worthless cost.

The tombstone is Ultima Online's ecology. Richard Garriott: *"We'd spent an enormous amount of time and effort on it. But what happened was all the players went in and just killed everything... literally no-one ever noticed — ever — and we eventually just ripped it out."*

Kate Compton's companion point: *"I can easily generate 10,000 bowls of plain oatmeal, with each oat in a different position."* Mathematical uniqueness is not perceived novelty.

And the structural consequence: **the simulated world is not itself a story.** Raw event logs require narrativization. The academic work on "story sifting" treats curation as a separate first-class subsystem whose job is to search the event chronicle for narratively interesting sequences — revenge cycles, betrayed contracts, consequences that close a loop opened months ago.

**This is a component the design doesn't currently have, and it's not optional if the world is going to run at a scale nobody can hold.** The simulation layer produces material; a curation layer decides what gets surfaced to whom. Building the first without the second produces a very expensive random number generator.

Two architectural requirements fall out: preserve **causal links** between events, and tag events with **abstract properties** so patterns can match flexibly. Both are cheap at design time and impossible to retrofit.

Techniques worth stealing wholesale:

- **RimWorld's named storytellers** (Cassandra Classic, Phoebe Chillax, Randy Random) — the player picks a pacing personality. This converts "the RNG screwed me" into "Randy is like that." **Attributable randomness feels authored; anonymous randomness feels arbitrary.**
- **Caves of Qud's history-as-testimony** — generated history is presented as word of mouth and ancient texts, explicitly allowing bias and conflicting accounts. This turns generator incoherence into a diegetic feature. Nearly free, enormous payoff.
- **Hair complexity** — non-feedback flavor detail (Dwarf Fortress dwarf appearances, Prison Architect prisoner backstories). Highest aliveness per unit of effort in the entire design space.
- **Show the forces, not the state.** Present consequences with visible causes rather than attributes.
- **Name everything that recurs.** Names are the cheapest legibility technology available.

And the honest warning from Crusader Kings: *"when the story engine isn't firing, your actions can feel rote and uninspired."* Every simulation-driven long-form game has a between-beats dead state and needs a designed answer for it, not more simulation.

### The moderation wall, and the Czege Principle

Every tradition in this survey hit the same wall: **the most valuable content is human-moderated, and human moderation does not scale.** Play-by-mail automated the arithmetic and kept the prose until the prose became unaffordable. MUSHes distributed world-building to players and still burned out their staff. LambdaMOO's wizards formally resigned from social governance in 1992. Ultima Online's volunteer moderators sued and settled in 2004. Large larps solve it only by paying in ratio — a big crew corps per player.

There are exactly three answers: automate the moderation, convert the players into moderators with structure, or price it honestly. **The forms that survived the internet transition — correspondence chess, automated Diplomacy — are precisely the ones whose per-turn human labor was already zero.**

Separately, a hard constraint on GM-less play. **The Czege Principle:** creating your own adversity and its resolution is boring. The documented workaround is the **Surprise by Complexity Principle** — when you create the adversity, you should not be sure you can solve it. This binds *harder* on automated systems, not softer, because a transparent generator is a solvable one. Genuine epistemic uncertainty on the player's side is a design requirement for any GM-less tier, not a nice-to-have.

---

## 5. Structures nobody in this space is using

Four things from adjacent forms that map directly onto this design and appear nowhere in the current tabletop software landscape.

### The turn report

Play-by-mail's central artifact: a **personal, private, bounded document that arrives on a schedule**, addressed to you, about your things, readable in one sitting, ending in a decision you have to make. Turn results were narrative prose, not state dumps — six to twenty pages typically.

Nothing in modern asynchronous play has replaced it, and it is the strongest retention artifact any of these forms produced. It is also the natural output of a world that advances on a cadence.

The failure boundary is documented too: *Empyrean Challenge* reportedly generated **1,000-page** turn results. **Reading cost must stay below decision value.** Cap the report.

### The press corps

Megagames run 30–100 players in parallel with a Control team, and they include dedicated **press roles** — players whose job is to report on what other teams are doing. This is a *player-operated curation layer*: someone whose function is to sift and broadcast the interesting parts of everyone else's play.

This is simultaneously an answer to the exclusion problem in parallel play, a distribution mechanism for the curation layer above, and a role for a player who can't make the main session. It is the most directly stealable structure in the entire survey.

Megagames also supply the general recipe for keeping large groups occupied in parallel: give every participant a role with private information, **at least two overlapping affiliations** so no single scene is their only outlet, an escalation path to a referee, and an obligation to someone else that generates inbound contact.

### Graceful absorption of absence

**Every durable asynchronous form has an explicit, designed answer to "what happens when someone doesn't show." Forms without one die at the first missed session.**

- **Diplomacy** has standby players as a named hobby institution, with dedicated literature on replacement procedure, plus civil disorder rules for abandoned positions.
- **webDiplomacy** lets a game creator set a **minimum reliability rating** to join and a number of missable phases before automatic removal — flaking becomes a public, portable reputation rather than a private failure.
- **Oath** has the *Clockwork Prince*, which automates the incumbent seat for reduced player counts. A persistent world with designed NPC-ification of an absent player.
- **Pandemic Legacy** advances the calendar on a loss — **failure is a fork with its own authored content, not a hole.** The campaign structurally cannot stall.
- **Gloomhaven** scales scenarios to player count and makes character retirement a rewarded event rather than an attrition failure.

This is the design requirement behind "two players show up and play without the GM." It's not a feature; it's the thing that determines whether the campaign survives contact with adult schedules.

### Victory conditions scaled to starting position

*Hyborian War* ran 36 asymmetric kingdoms on one scoreboard by rating each player's victory conditions **relative to their own starting position** rather than absolute territory. Directly applicable to a shared world with unequal characters and unequal engagement levels.

---

## 6. Open questions this survey did not answer

- **No credible data exists on campaign mortality, or on what share of the hobby plays asynchronously.** Roll20's Orr Industry Report appears discontinued (last useful data Q4 2021), Wizards runs surveys and doesn't publish them, and the only public in-person/online split is from April 2023. If those numbers matter, they'd have to be gathered directly.
- **No public churn or free-to-paid conversion data exists for any tabletop software product.** None. Any model has to use general SaaS benchmarks and flag them as such.
- **No reliable unit-sales figures exist for any RPG book** — BookScan doesn't cover the hobby channel, which is a hard measurement limit rather than a research failure.
- **Published TTRPG market-size figures are unusable.** Two "independent" research firms return identical numbers to three decimal places ($2.408B and $2.41B for 2026, both at 11.84% CAGR). A bottom-up reconstruction from D&D's ~$296M, total global RPG crowdfunding of $67M, and the known publisher tiers gets to roughly $0.5–0.9B, not $2.4B.
- **Role, Inc. — the closest thing to a direct precedent — appears dormant but has not shut down.** Site live, store functional, © 2026, CHROME still listed and free. But the last blog post is 22 December 2023 and there has been no press coverage since 2023. Treat platform continuity as an open risk, and treat the category gap as unexplained rather than proven empty.
