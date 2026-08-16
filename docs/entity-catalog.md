# Entity Catalog

**What tabletop games actually track, with real numbers.**

Reference material, not an argument. Organized so you can browse and compare rather than read straight through. Roughly 90 systems, drawn from SRDs, official references, and primary sources; anything I couldn't verify is flagged rather than guessed.

**How to use it:** Part 1 is the comparison layer — scan for shapes you like. Parts 2–7 go deeper on each dimension of an entity. Parts 8–10 cover non-people: vehicles, organizations, places. Part 11 collects the reusable primitives worth stealing regardless of what you build.

⚠️ marks a number I could not verify against a source this session.

---

# PART 1 — MASTER COMPARISON

## 1.1 Attribute schemes

| System | Attributes | Count | Scale | Average | Generation |
|---|---|---|---|---|---|
| OD&D / AD&D / B/X | STR INT WIS DEX CON CHA | 6 | 3–18 | 10–11 | 3d6 in order |
| D&D 3.x / 5e / 2024 | STR DEX CON INT WIS CHA | 6 | 1–20 (PC cap) | 10 | 4d6 drop lowest; array; 27-pt buy |
| D&D 4e | same 6 | 6 | 1–30 | 10 | as above, **+½ level to nearly everything** |
| Pathfinder 2e | same 6 | 6 | −1 to +4 mod | +0 | boost-based, no raw scores at play |
| Traveller | STR DEX END INT EDU SOC | 6 | 2–12 | 7 | 2d6 each, in order |
| BRP / RuneQuest | STR CON SIZ INT POW DEX CHA | 7 | 3–18 | 10.5 | 3d6 / 2d6+6 |
| Call of Cthulhu 7e | STR CON SIZ DEX APP INT POW EDU LUCK | 9 | 15–90 | 50 | 3d6×5 / (2d6+6)×5 |
| Delta Green | STR CON DEX INT POW CHA | 6 | 3–18 | 10.5 | 3d6 |
| Pendragon | SIZ DEX STR CON APP | 5 | 5–21 | ~10 | culture-based allocation |
| WFRP 4e | WS BS S T I Ag Dex Int WP Fel | 10 | 1–100 | ~30 | 2d10 + species base |
| GURPS 4e | ST DX IQ HT | 4 | open, ~1–20 | 10 | point-buy; ST/HT 10pts, DX/IQ 20pts per level |
| Hero System 6e | STR DEX CON INT EGO PRE OCV DCV OMCV DMCV SPD PD ED REC END BODY STUN | 17 | open | varies | point-buy, all bought directly |
| Savage Worlds | Agility Smarts Spirit Strength Vigor | 5 | d4–d12 | d6 | 5 points, 1 pt = 1 die step |
| Fate Core | **none** — skills only | 0 | ladder −2 to +8 | +1 | pyramid |
| Cortex Prime | optional; often Physical/Mental/Social | 0–6 | d4–d12 | d6 | array assignment |
| Genesys | Brawn Agility Intellect Cunning Willpower Presence | 6 | 1–5 | 2 | 10 × new rating in XP |
| Cypher | Might Speed Intellect (as **pools**) | 3 | ~7–20 | ~10 | type array + 6 free |
| Fudge | free-defined | any | Terrible→Superb (7 rungs) | Fair | free levels = ½ × count |
| Risus | **none** — clichés only | 0 | 1–6 dice | 2 dice | 10 dice, max 4 per cliché |
| Open D6 | Reflexes Coordination Physique Knowledge Perception Presence | 6–7 | 1D–5D | 2D | dice allocation |
| World of Darkness | 3×3 grid: Str Dex Sta / Cha Man App / Per Int Wit | 9 | 1–5 dots | 2 | 7/5/3 dot spread |
| Chronicles of Darkness | Power/Finesse/Resistance × Physical/Social/Mental | 9 | 1–5 | 2 | 5/4/3 |
| Exalted | STR DEX STA CHA MAN APP PER INT WIT | 9 | 1–5 | 2 | caste priority |
| Shadowrun 5e | BOD AGI REA STR WIL LOG INT CHA (+ EDG, ESS, MAG/RES) | 8 + special | 1–6 typical | 3 | priority table |
| Apocalypse World | Cool Hard Hot Sharp Weird | 5 | −3 to +3 | 0 | playbook arrays |
| Dungeon World | STR DEX CON INT WIS CHA | 6 | −1 to +3 mod | +0 | array, D&D-shaped |
| Masks | Danger Freak Savior Superior Mundane | 5 | −2 to +3 | 0 | playbook |
| Monsterhearts | Hot Cold Volatile Dark | 4 | −1 to +2 | 0 | playbook |
| Blades in the Dark | 12 actions under Insight / Prowess / Resolve | 12 | 0–4 dots | 1 | 7 dots, max 2 at start |
| Burning Wheel | Will Perception Power Forte Agility Speed | 6 | 1–10 (exponent) | 3–4 | lifepath-derived |
| Into the Odd / Cairn | STR DEX WIL | 3 | 3–18 | 10.5 | 3d6 in order |
| Electric Bastionland | STR DEX CHA | 3 | 3–18 | 10.5 | 3d6 |
| Knave 2e | 6 abilities | 6 | 0–10 | ~2 | level-based |
| Mörk Borg | Agility Presence Strength Toughness | 4 | −3 to +3 | 0 | 3d6 table |
| Troika | Skill, Stamina, Luck | 3 | Skill 3–8, Stam 12–24, Luck 6–12 | — | dice |
| Mothership 1e | Strength Speed Intellect Combat | 4 | %, ~20–50 | — | class-based |
| Ironsworn | Edge Heart Iron Shadow Wits | 5 | 1–3 | 2 | array 3/2/2/1/1 |
| Mausritter | STR DEX WIL | 3 | 2–12 ⚠️ | 7 | 2d6 |
| Lasers & Feelings | **one number** | 1 | 2–5 | 3–4 | pick |
| Honey Heist | Bear, Criminal (always sum to 6) | 2 | 1–5 | 3 | pick |
| Wanderhome | **none** — no dice at all | 0 | — | — | playbook + natures |

## 1.2 Core resolution

| System | Dice | Success | Outcome bands |
|---|---|---|---|
| D&D 3e–5e | d20 + mod | ≥ DC | binary + nat 20/1 |
| D&D 4e | d20 + mod + ½ level | ≥ Defense | binary |
| Pathfinder 2e | d20 + mod | ≥ DC | **4 bands**: crit fail / fail / success / crit success (±10) |
| Traveller | 2d6 + DM | ≥ 8 | Effect = margin |
| BRP / CoC | d100 | ≤ skill | fumble / fail / success / hard (½) / extreme (⅕) / crit (⅒) |
| Pendragon | d20 | ≤ skill, high wins | crit on exact |
| WFRP 4e | d100 | ≤ skill | Success Levels = tens digit difference |
| GURPS | 3d6 | ≤ skill | margin; crit on 3–4, fumble 17–18 |
| Hero System | 3d6 | ≤ 11 + OCV − DCV | margin |
| Savage Worlds | trait die + Wild Die (d6), exploding | ≥ 4 | **raises** every +4 |
| Fate | 4dF (−1/0/+1) + skill | ≥ opposition | shifts |
| Cortex | pool of varied dice, sum best 2 | ≥ difficulty | effect die from remainder |
| Genesys | symbol dice | net Success | Success/Advantage/Triumph/Threat/Despair on 2 axes |
| Cypher | d20 | ≥ task level × 3 | player rolls everything |
| World of Darkness | d10 pool | ≥ difficulty (6–8) | successes counted; botch on 0 + a 1 |
| VtM V5 | d10 pool | ≥ 6; two 10s = crit | messy crit / bestial failure via Hunger dice |
| Shadowrun 4e+ | d6 pool | 5–6 = hit | glitch if >half show 1 |
| Exalted | d10 pool | ≥ 7, 10s = 2 | threshold successes |
| L5R 4e | roll X keep Y d10, exploding | sum ≥ TN | raises (+5 TN each) |
| Burning Wheel | d6 pool | ≥ 4 (shade-dependent) | successes vs obstacle |
| PbtA | 2d6 + stat | 10+ / 7–9 / 6− | **3 bands, always** |
| Forged in the Dark | d6 pool, take highest | 6 / 4–5 / 1–3; two 6s = crit | × Position × Effect |
| Into the Odd | d20 | ≤ ability (saves only) | **attacks always hit** |
| Mörk Borg | d20 ± ability | ≥ DR (usually 12) | binary |
| Troika | 2d6 | ≤ Skill + relevant | binary |
| Ironsworn | d6 + stat vs 2d10 | beat both / one / neither | strong / weak / miss |
| Mothership | d100 | ≤ stat or save | crit on doubles |
| Ten Candles | d6 pool = lit candles | any 6 | candles go out |

## 1.3 Health and depletion models

| System | Model | Numbers | Death |
|---|---|---|---|
| D&D 5e | HP pool | class die + CON per level | 0 HP → 3 death saves |
| Pathfinder 2e | HP + **dying 1–4** condition | ancestry + class + CON | dying 4 |
| Traveller | **3 characteristics ARE the HP** — damage to STR/DEX/END | 2–12 each | all three at 0 |
| BRP/RuneQuest | total HP + **7 hit locations** | (CON+SIZ)/2 | location or total |
| CoC 7e | HP = (CON+SIZ)/10 | ~10–15 | 0 = dying |
| Delta Green | HP = (STR+CON)/2 | ~10 | 0 |
| WFRP 4e | Wounds = SB + 2×TB + WB | ~10–16 | 0 → critical wounds |
| GURPS | HP = HT ⚠️, shock/stun thresholds | ~10 | −5×HP |
| Hero System | **BODY and STUN separately** | BODY 10, STUN 20 | BODY 0 |
| Savage Worlds | **Wounds 0–3** + Shaken | 3 wounds | Incapacitated |
| Fate | **stress boxes + consequences** (mild/moderate/severe) | 2–4 boxes | taken out / concede |
| Cypher | **3 pools ARE health** — Might/Speed/Intellect | ~10–20 each | damage track 4 steps |
| World of Darkness | **7 health levels with penalties** | −0/−1/−1/−2/−2/−5/incap | Incapacitated |
| Shadowrun | Physical + Stun monitors | 8 + BOD/2 and 8 + WIL/2 | overflow |
| Exalted | health levels −0/−1/−1/−2/−2/−4/Incap | 7 | Incapacitated |
| Apocalypse World | **harm clock 0–6** | 6 segments | 12 o'clock |
| Dungeon World | HP + **debilities** (attribute penalties) | class-based | 0 → Last Breath |
| Masks | **5 named conditions**, no HP | Angry/Afraid/Guilty/Hopeless/Insecure | none — conditions block moves |
| Blades in the Dark | **harm ladder 4 levels** + stress 9 | L1 lesser / L2 moderate / L3 severe / L4 fatal | L4 |
| Into the Odd / Cairn | HP → STR → **STR save** → death | HP 1–6, STR 3–18 | STR 0 |
| Knave 2e | HP, then **wounds fill inventory slots** | — | slots full |
| Mörk Borg | HP, then broken table | — | — |
| Mothership | Health → **wounds** → death save | — | — |
| Heart / Spire | **stress on 5 resistances** → **fallout** | resistance-specific | severe fallout |
| Trophy Dark | **Ruin 1–6 only** | starts 1 | Ruin 6 |
| Ironsworn | Health / Spirit / Supply meters + momentum | 0–5 each | debilities |
| Ten Candles | candles going out | 10 → 0 | all dark |

---

# PART 2 — ATTRIBUTES IN DETAIL

## 2.1 The D&D modifier curve, edition by edition

The thing most people copy without noticing it changed three times.

| Edition | Curve | Modifier range |
|---|---|---|
| OD&D | **no general curve** — each ability has bespoke rules, most scores do nothing | mostly ±1 |
| AD&D 1e/2e | **no general curve** — per-ability sub-tables, non-linear, many columns; 18/01–18/00 percentile strength for fighters | −3 to +3 hit, −1 to +6 damage |
| B/X, BECMI | **single ladder**: 3 = −3, 4–5 = −2, 6–8 = −1, 9–12 = 0, 13–15 = +1, 16–17 = +2, 18 = +3 | −3 to +3 |
| 3.x onward | `mod = floor((score − 10) / 2)` | −5 to +10 |

The 3e formula is the one everyone remembers, and it's the *fourth* answer to the question. The originals mostly didn't have a general rule at all.

## 2.2 Traveller's characteristic DM table

The cleanest compression of a 2–12 range into a small modifier:

| Score | 0 | 1–2 | 3–5 | 6–8 | 9–11 | 12–14 | 15+ |
|---|---|---|---|---|---|---|---|
| DM | −3 | −2 | −1 | +0 | +1 | +2 | +3 |

## 2.3 The World of Darkness grid

Nine attributes as a 3×3 matrix, which is the most structurally elegant attribute scheme in the hobby:

| | Power | Finesse | Resistance |
|---|---|---|---|
| **Physical** | Strength | Dexterity | Stamina |
| **Social** | Presence | Manipulation | Composure |
| **Mental** | Intelligence | Wits | Resolve |

Every attribute has a defined position in two dimensions. Nothing is arbitrary, and adding a tenth would break the shape — which is a feature.

## 2.4 Blades' twelve actions

Three attributes that exist only as *groupings* of four actions each. You never roll the attribute; you roll the action. The attribute is used only for resistance rolls.

| Insight | Prowess | Resolve |
|---|---|---|
| Hunt | Skirmish | Attune |
| Study | Wreck | Command |
| Survey | Finesse | Consort |
| Tinker | Prowl | Sway |

Note these are **verbs, not qualities.** Not "Strength" but "Wreck." That's the PbtA-lineage move: describe what you *do*, not what you *are*.

## 2.5 Apocalypse World's five

`Cool · Hard · Hot · Sharp · Weird`, range −3 to +3.

None are qualities of a person in any ordinary sense. They're *approaches to the fiction* — and each is bound to specific moves rather than being generally applicable:

| Move | Stat |
|---|---|
| Do something under fire | Cool |
| Go aggro on someone | Hard |
| Seize something by force | Hard |
| Seduce or manipulate someone | Hot |
| Read a sitch | Sharp |
| Read a person | Sharp |
| Open your brain to the psychic maelstrom | Weird |
| Help or interfere with someone | **Hx** (the relationship stat) |

That last row matters: a *relationship* value sits in the same slot as an attribute.

## 2.6 The one-number games

**Lasers & Feelings** — a single integer 2–5. Roll **under** it for LASERS (tech, rationality, precision), **over** it for FEELINGS (intuition, passion, diplomacy). Rolling *exactly* your number is "Laser Feelings": ask the GM a question, answered honestly.

One integer simultaneously encodes capability, characterization, and thematic position, and the exact-match rule turns a two-sided axis into three outcome classes. The cost: with only four values, two characters sharing a number are mechanically identical.

**Honey Heist** — Bear and Criminal, always summing to 6. Acting as one raises it and lowers the other. A slider, not two stats.

---

# PART 3 — SKILLS

| System | Count | Scale | Relationship to attributes |
|---|---|---|---|
| D&D 5e | 18 | proficiency bonus (+2 to +6), binary | attribute + proficiency |
| Pathfinder 2e | ~17 | Untrained/Trained/Expert/Master/Legendary | proficiency + level + attribute |
| GURPS 4e | 300+ | relative to a controlling attribute | attribute + difficulty offset |
| BRP / RuneQuest | ~50 | percentage 0–100+ | starting % derived from characteristics |
| Call of Cthulhu 7e | ~60 | percentage | mostly independent; EDU-driven allocation |
| WFRP 4e | ~40 | advances added to characteristic | characteristic + advances |
| Traveller | ~40 | 0–4 typical | separate; characteristic DM added |
| World of Darkness | 30 | 1–5 dots | pooled: attribute + ability dice |
| Shadowrun 5e | ~70 | 1–12 | pooled: attribute + skill |
| Savage Worlds | ~25 | d4–d12 | linked attribute sets cost |
| Fate Core | 18 | ladder | **no attributes — skills are everything** |
| Blades | 12 actions | 0–4 dots | actions *are* the skills |
| PbtA | **none** | — | moves replace skills entirely |
| Into the Odd / Cairn | **none** | — | removed on purpose |
| Shadowdark | **none** | — | stat checks only |
| Knave | **none** | — | items grant capability |

The interesting split: as you go down this list, "what can my character do?" stops being answered by a list and starts being answered by *equipment*, *moves*, or *fictional positioning*.

---

# PART 4 — HEALTH AND DEPLETION, IN DETAIL

## 4.1 World of Darkness health levels

Seven levels, each with a *named severity* and a *dice penalty*:

| Level | Penalty |
|---|---|
| Bruised | −0 |
| Hurt | −1 |
| Injured | −1 |
| Wounded | −2 |
| Mauled | −2 |
| Crippled | −5 |
| Incapacitated | — |

This is the canonical **death spiral**: getting hurt makes you worse at not getting hurt. Loved for tension, criticized for making losing fights unwinnable.

## 4.2 Blades' harm ladder

Four levels, each with a *named mechanical consequence* rather than a number:

| Level | Effect |
|---|---|
| **1 Lesser** (2 slots) | reduced effect |
| **2 Moderate** (2 slots) | −1d to affected rolls |
| **3 Severe** (1 slot) | need help to act |
| **4 Fatal** | you're dying |

Overflow escalates *up a row* — two Lesser harms of the same type become a Moderate. Filling level 3 triggers a catastrophe. Each harm is also a written phrase ("Broken Leg", "Shaken"), so it's simultaneously a number, a name, and a fiction.

**Stress**, separately: 9 boxes, spent to resist consequences or push yourself. Filling it takes **Trauma** — one of Cold, Haunted, Obsessed, Paranoid, Reckless, Soft, Unstable, Vicious. **Four traumas and the character retires.** So the character's *lifespan* is a resource, not their body.

## 4.3 Masks' conditions

No hit points at all. Five named emotional states, each blocking specific moves:

`Angry · Afraid · Guilty · Hopeless · Insecure`

Clearing one requires a *specific fictional act* — you must flee something to clear Afraid. And for NPCs: marking a condition forces the GM to make a move from a list, so damage always changes the world rather than decrementing a counter.

## 4.4 Into the Odd's three-stage collapse

The most compact serious health model found:

1. Damage hits **HP** (1–6, "ability to avoid life-threatening damage" — explicitly not meat).
2. Excess subtracts from **STR**.
3. On any STR loss, make a **STR save**. Fail = Critical Damage: you can't act, need an ally's help plus a rest, and die within an hour untreated.
4. **STR 0 = death.**

Attacks always hit. There is no attack roll. Damage is a die, minus Armour.

## 4.5 Traveller's characteristics-as-health

Damage is applied directly to **STR, DEX, and END**. Your capability *is* your durability, and being hurt makes you worse at everything the hurt stat governs. No separate HP field exists.

## 4.6 Hero System's two-track damage

**BODY** (real injury, ~10) and **STUN** (incapacity, ~20) tracked separately, with different recovery rates. A punch does mostly STUN; a sword does both. It's the most explicit separation of "hurt" from "out of the fight" in the hobby.

## 4.7 Stress-and-fallout (Heart, Spire)

Five **resistances** — Blood, Mind, Silver, Shadow, Fortune (Spire) — each accumulating stress independently. When stress is marked you roll against the total; failure means **fallout**, a narrative consequence scaled minor/major/critical, which then *clears* the stress.

The structural move: stress isn't damage, it's *pressure*, and the release valve is a story event rather than a heal.

## 4.8 Trophy Dark's single number

**Ruin, 1–6.** That's the whole character mechanically, alongside skill words. Roll light dice (safe) or dark dice (risky); dark dice can raise Ruin. At Ruin 6, the character is lost to the forest.

One ascending counter, one terminal threshold, no HP.

---

# PART 5 — CREATURE AND NPC BLOCKS

## 5.1 AD&D 1e Monster Manual — 16 fields

`Frequency · No. Appearing · Armor Class · Move · Hit Dice · % in Lair · Treasure Type · No. of Attacks · Damage/Attack · Special Attacks · Special Defenses · Magic Resistance · Intelligence · Alignment · Size · Psionic Ability`

**No ability scores.** And note that four of the sixteen aren't creature state at all — Frequency, No. Appearing, % in Lair, and Treasure Type are random-encounter-generator configuration and loot tables, stapled to the creature because the book had nowhere else to put them.

B/X adds **Morale** and XP value. Morale is an NPC-only stat with no PC equivalent, and the reason is structural: the player supplies PC behavior, so nothing needs to encode it.

## 5.2 The symmetry experiment and its retreat

| Edition | Approach |
|---|---|
| OD&D | Hit Dice generates nearly everything; AC, movement, HD, plus an exception list |
| AD&D | 16 fields, no ability scores |
| **3e** | **Full PC data model on every monster** — six abilities, skills, feats, BAB, saves, class levels, templates. NPC classes (Commoner/Expert/Warrior/Adept/Aristocrat) invented to make it affordable |
| **4e** | **Explicit break.** Monsters no longer built from classes. **Role** (Brute/Soldier/Skirmisher/Lurker/Artillery/Controller + Leader) and **Type** (Minion = 1 hp / Standard / Elite = 2 slots / Solo = 5 slots). Attack, damage, HP, defenses are **table lookups by level and role**, not sums |
| 5e | Middle path. Ability scores return but are largely vestigial. CR + proficiency + bounded accuracy. DMG process is "design by feel, then check against the CR table" |
| 2024 | Initiative printed in the block; Gear, Habitat, and Treasure fields return; PC-species humanoids removed from the Monster Manual |
| **PF2** | **Doctrine stated outright**: "Creatures aren't built the same way PCs are... based on benchmark final numbers rather than combining each individual modifier together... top-down design" |

4e's monster math was compact enough to fit on a business card: to-hit ≈ level + 5, damage ≈ 8 + level. It also *failed on its own terms* — monsters gained 8 HP per level while PC damage grew slower, so time-to-kill drifted from 4 hits at level 1 to 7 at level 30.

## 5.3 Where symmetry survives

**Into the Odd, Cairn, Electric Bastionland**: monsters use the *identical* schema as PCs. A monster is STR, DEX, WIL, HP, Armour, damage, plus one line of special. Hirelings have 10 in everything and d6 HP.

The pattern across the whole record: **every game that grew a large PC schema eventually broke the monster off it. Every game with a tiny PC schema kept them unified.** Symmetry becomes affordable again below a certain schema size.

## 5.4 The OSR reformulation

Chris McDowall's three-part monster, none of which are numbers:

- **Core** — its one power
- **Balance** — its one constraint (need not be physical: immateriality, environmental binding, a specific vulnerability)
- **Seasoning** — the narrative hook

---

# PART 6 — NON-NUMERIC STATE

## 6.1 Conditions

D&D 5e's fifteen: `blinded · charmed · deafened · frightened · grappled · incapacitated · invisible · paralyzed · petrified · poisoned · prone · restrained · stunned · unconscious` + exhaustion 1–6.

The thing a condition does that a modifier cannot: **it's a type other rules can key on.** "Advantage against a prone target," "immune to charmed," "ends the frightened condition" — none of those can be written against a −2. The number is magnitude; the name is interface.

Counter-current worth noting: 2024 converted exhaustion from a six-step ladder with distinct effects into a flat cumulative −N. Graded named states are expensive to maintain.

## 6.2 Fate aspects — one type, four lifetimes

An aspect is free text that is (i) always true in the fiction, (ii) invocable for a fixed bonus at a fate-point cost, (iii) compellable against you for a fate point.

The elegance is that Fate has essentially **one non-numeric type**, differentiated only by scope and lifetime:

| Kind | Scope | Lifetime |
|---|---|---|
| Game aspects | world | permanent |
| Character aspects | entity | permanent |
| Situation aspects | **zone or scene** | scene |
| Consequences (injuries are aspects) | entity | multi-scene |
| Boosts | anything | single use, expire on invoke; **cannot be compelled** |

So: `aspect = (text, scope, lifetime, free_invocations)`.

Known weakness: free text underconstrains. Fate needed a published taxonomy of aspect *types* — go-to, GM hook, fate-point generator, contextualizer, wild card — because "write a phrase" gives players no guidance on what makes an aspect do work. **Expect any free-text state field to need an authoring taxonomy on top of it.**

## 6.3 City of Mist statuses — named state with magnitude

Tags replace numeric stats entirely; each applicable tag = 1 Power, and tags stack.

**Statuses** are named states with a tier 1–6. Tiers 1–4 add or subtract Power; tier 5 = out of commission for that condition; tier 6 = permanent transformation.

The critical rule: **only the highest applicable status tier applies. max(), not sum().** That single choice eliminates the entire stacking-nightmare category.

Three tag classes: Story Tags (temporary, anyone can use), Power Tags (permanent, beneficial), Weakness Tags (permanent, dramatic flaws).

## 6.4 Apocalypse World gear tags

A weapon is literally the string `2-harm hand messy`.

One magnitude (`2-harm`), one range tag (`hand`), and N behavioral flags (`messy`) in a single compact record. Tags are cheap, composable, and let one record carry both magnitude and behavior **without a schema change**. This is arguably the most transferable idea in the whole corpus for a system that wants extensibility.

## 6.5 Burning Wheel's Beliefs, Instincts, Traits

- **Beliefs** (3, player-authored, rewritten often) are statements *the GM is instructed to attack*. Inputs to scenario generation, not modifiers.
- **Instincts** are conditional always-on rules — "Always draw first."
- **Traits** split three ways: Character (pure descriptor, zero mechanical weight), Call-on (grants a reroll in a named situation), Die (grants dice).

That last split is instructive: **the same field type spans zero mechanical weight to full mechanical weight**, declared per instance.

All three wire into **Artha** (Fate, Persona, Deeds), which is the actual engine rather than a bolt-on: Fate buys open-ended 6s, Persona buys +1d each and can cheat death, Deeds buys rerolls. Caps per test: 1 Fate, 3 Persona, 2 Deeds. Artha is *both consumed and recorded* — marked next to the ability tested and next to the relevant Belief. **20 Fate + 10 Persona + 3 Deeds marked on one ability = Epiphany**, which advances its shade.

## 6.6 Relationship encodings

The same concept, six ways:

| Game | Encoding |
|---|---|
| Dungeon World | **Bonds** — free text, resolved for XP |
| Apocalypse World | **Hx** — an integer per other PC, feeding help/interfere |
| Monsterhearts | **Strings** — countable tokens one character *holds over* another |
| Masks | **Influence** — a binary flag |
| Delta Green | **Bonds** — numeric, and burnable as a sanity buffer |
| Smallville | relationship values that *are* the dice pool |

Every one of these stores the relationship as a list on one endpoint. That's why relationship mechanics chronically go asymmetric and desync in play — **a relationship is an edge, and every system in the hobby models it as a field.**

## 6.7 Clocks

Origin: Apocalypse World fronts used countdown clocks as campaign-scale checklists. Forged in the Dark generalized them into progress trackers at any scale — 4 segments (complex), 6 (complicated), 8 (daunting).

Formally a clock is just `(name, filled, size, visibility)`. All the value is in convention. Three properties worth noting:

- **Segments are fungible** — heterogeneous actions advance the same clock.
- **Completion is a fictional event, not a threshold** — the clock filling *is* "you get into the inner sanctum."
- Harper's own framing: a clock **displays** the situation, it doesn't drive it. "Like a speedometer — it shows the speed, it doesn't determine it." Designers routinely get this backwards.

## 6.8 Inventory as capability

Where carrying capacity isn't a limit but *is* the character:

| Game | Mechanism |
|---|---|
| Into the Odd | **Three Bulky items reduces you to 0 HP** |
| Cairn | 10 slots (6 backpack + 2 hands + 2 worn); **a full inventory means 0 HP** |
| Knave 1e | Slots = Constitution defense — the same number is both |
| Knave 2e | **Wounds physically occupy inventory slots** |
| Mausritter | Grid inventory; **conditions take up slots** |
| Black Hack 2e | Items carried ≤ STR |

No weight numbers anywhere. The constraint is countable and visible instead of computed.

---

# PART 7 — PROGRESSION

| System | Trigger | Cadence |
|---|---|---|
| OD&D / B/X | **Gold-for-XP** (earned *and* spent) | treasure-driven |
| D&D 3e–5e | Combat XP, or milestone | encounter or scene |
| Dungeon World | End-of-session questions: learn about the world / overcome a notable monster / loot memorable treasure; + alignment; + resolve a bond | session |
| PbtA generally | **Mark XP on a 6−** (failure advances you) | roll |
| Apocalypse World | Highlighted stats — *other players* choose which of your stats earns XP | scene |
| Blades | Playbook trigger + express beliefs/heritage + struggle with vice/trauma + desperate action | session; ~6–8 XP per advance ≈ every 2–3 sessions |
| Burning Wheel | Test counting per ability (routine/difficult/challenging quotas) + Artha | per test |
| BRP / CoC | **Checkmark on success**, roll to improve later | per skill use |
| Electric Bastionland | **Scars** — you advance by nearly dying | HP hitting exactly 0 |
| Traveller | Career terms during character generation; almost none afterward | pre-play |
| Pendragon | Winter phase, annual, mandatory | one game-year |
| Fate | Milestones (minor/significant/major) | arc |

Note the extremes: Traveller front-loads everything into character creation and then essentially stops. Electric Bastionland has no XP at all and advances you through injury. PbtA pays you for failing.

**One documented failure worth knowing:** in a 2d6+stat system, the +2 → +3 jump is disproportionately powerful — success becomes routine and the dramatic tension of partial success disappears. **The tighter your dice curve, the shorter your viable advancement runway.** PbtA's real ceiling is about three levels of vertical growth.

---

# PART 8 — VEHICLES, SHIPS, MECHS

## 8.1 The three architectures

**Parallel** — its own unrelated field set (BattleTech, Car Wars, Traveller ships).
**Isomorphic** — same field names, relabeled (Star Trek Adventures, Shadowrun, FFG Star Wars).
**Universal** — literally the same primitives (Hero System, Fate).

And a second, independent axis that most failures live on: **who plays it.** The pilot rolls, the ship rolls, each crew member holds a station, or the GM runs it.

## 8.2 Mongoose Traveller 2e / Cepheus — the most implementable ship model

**Field list:**
```
Name, Tech Level
Hull:         tons; configuration (standard/streamlined/distributed/planetoid);
              Hull points; Structure points
Armour:       type + points
Drives:       J-drive letter → Jump-n; M-drive letter → Thrust n;
              Power plant letter → rating n
Fuel:         tons; weeks of endurance; number of jumps
Computer:     Model n, rating
Sensors:      suite + DM
Staterooms, Low berths, Hardpoints, Fire control
Weapons:      turrets/bays, ammunition
Screens, Small craft, Cargo
Crew:         pilot/navigator/engineer/gunner/steward/medic/marine counts
Passengers:   high/middle/low
Cost, Build time
```

**Derived formulas:**

| Stat | Formula |
|---|---|
| Hull points | 1 per 50 tons displacement |
| Structure points | 1 per 50 tons (min 1) |
| Jump fuel | 0.1 × hull tons × jump number, per jump |
| Power plant fuel | ⌊plant tons ÷ 3⌋ per week, min 2 weeks |
| Bridge | MCr 0.5 per 100 tons |
| Hardpoints | 1 per 100 tons |
| Power plant rating | must be ≥ max(jump rating, thrust rating) |

**The key tradeoff lever:** a drive letter is a *fixed tonnage of hardware*. Performance is that hardware divided by hull size. A 100-ton hull with a B-drive gives 4G; a 200-ton hull with the same B-drive gives 2G. One table, one elegant constraint.

**Who acts:** the ship rolls 2d6 initiative (+1 for higher Thrust, plus the Captain's Tactics effect). **The ship has the initiative; the crew have the actions.** Each named position gets its own action:

| Position | Skill | Does |
|---|---|---|
| Captain | Tactics | initiative bonus, orders |
| Pilot | Pilot | manoeuvre, evade |
| Sensors | Electronics | acquire lock (+1/+2 to gunners) |
| Gunner | Gunner | attack |
| Engineer | Engineer | drive/power management |
| Damage Control | Mechanic | repair |

**Damage model** — a genuinely well-shaped four-step process:

1. Roll to hit; range sets difficulty per weapon type (meson guns are *best* at long range; sandcasters only work at short).
2. **Subtract Armour from damage.**
3. Convert the remainder into *hits*: 1–4 = Single Hit, 5–8 = Two Singles, 9–12 = Double, 13–16 = Three Singles, 17–20 = Two Singles + Double, 21–24 = Two Doubles, 25–28 = Triple…
4. Roll location on one of **two tables, gated on whether Hull is exhausted:**

| 2d6 | External (Hull > 0) | Internal (Hull = 0) |
|---|---|---|
| 2 | Hull | Structure |
| 3 | Sensors | Power Plant |
| 4 | M-Drive | J-Drive |
| 5 | Turret | Bay |
| 6 | Hull | Structure |
| 7 | Armour | Crew |
| 8 | Hull | Structure |
| 9 | Fuel | Hold |
| 10 | M-Drive | J-Drive |
| 11 | Sensors | Power Plant |
| 12 | Hull | Bridge |

5. **Every system dies in three hits, with escalating effects:**

| System | 1st hit | 2nd | 3rd |
|---|---|---|---|
| M-Drive | Thrust −1 | Thrust halved | disabled |
| J-Drive | DM−2 to jump | disabled | destroyed |
| Power Plant | damaged | radiation crew hit | ship dead |
| Turret / Bay | DM−2 | disabled | destroyed |
| Bridge | crew hit | no pilot/sensor actions | destroyed |

**Scale, refreshingly blunt:** ship weapons take DM−4 against person-sized targets, and their damage is multiplied at personal scale (a beam laser does 1d6 × 50 to a person). No silhouette ladder — the multiplier *is* the scale rule.

## 8.3 Lancer — the pilot/mech coupling

The cleanest treatment of "an entity that contains another entity."

**Pilot stats:** HP = 6 + Grit · Evasion 10 · E-Defense 10 · Speed 4 · Armor 0 · Grit = ⌈License Level ÷ 2⌉ · License Level 0–12.

**The coupling — four pilot skills feed the mech's derived stats:**

| Mech Skill | Grants per point |
|---|---|
| **HULL** | Mech HP +2; Repair Cap +0.5 |
| **AGILITY** | Evasion +1; Speed +0.5 |
| **SYSTEMS** | E-Defense +1; Tech Attack +1; SP +0.5 |
| **ENGINEERING** | Heat Cap +1; Limited Systems +0.5 |

**Frame stat block:**
`size · structure · stress · armor · hp · evasion · edef · heatcap · repcap · sensor_range · tech_attack · save · speed · sp · mounts[] · traits[] · core_system`

Real frames, for shape:

| Frame | Size | Struct | Stress | Armor | HP | Eva | EDef | Heat | Rep | Sens | Tech | Save | Spd | SP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Everest | 1 | 4 | 4 | 0 | 10 | 8 | 8 | 6 | 5 | 10 | 0 | 10 | 4 | 6 |
| Barbarossa | 3 | 4 | 4 | 2 | 10 | 6 | 6 | 8 | 4 | 10 | −2 | 10 | 2 | 5 |
| Goblin | ½ | 4 | 4 | 0 | 6 | 10 | 12 | 4 | 2 | 20 | +2 | 11 | 5 | 8 |
| Saladin | 2 | 4 | 4 | 1 | 12 | 6 | 8 | 8 | 4 | 10 | 0 | 10 | 3 | 8 |

Note **Structure and Stress are both 4 for every frame** — the frame varies in everything else, but the "how many catastrophic events can it survive" number is universal. Structure absorbs HP depletion; Stress absorbs heat. Two parallel three-strikes tracks.

## 8.4 What a vehicle stat block tends to contain, across systems

Pooling the field lists, the recurring dimensions are:

- **Size / silhouette / scale class** — nearly universal, and it's what makes cross-scale interaction adjudicable
- **Structural integrity**, usually split into an outer layer (armour/hull) and an inner one (structure/frame)
- **Mobility**, usually two numbers: speed and handling/agility
- **Crew requirement and stations**
- **Mount points / hardpoints** — a capacity limit on capability
- **A heat, strain, or power budget** — the thing that limits how much you can do at once
- **Location-based damage** in the simulationist end, single-pool in the narrative end

---

# PART 9 — ORGANIZATIONS, DOMAINS, PLACES

## 9.1 Blades in the Dark — the crew

**Complete field list:**
```
name · crew_type · reputation (Ambitious/Brutal/Daring/Honorable/
  Professional/Savvy/Subtle/Strange) · lair · hunting_grounds
tier            0–VI, starts 0
hold            {weak, strong}, starts strong
rep             0–12, starts 0
turf            0–6
coin            starts 2; cap 4 in lair, 8 with Vault, 16 with Vault×2
heat            0–9, rolls over
wanted_level    0–4
crew_xp         track
special_abilities[] · upgrades[] · cohorts[] · claims[] · contacts[]
```

**Faction status ladder, −3 to +3** — tracked per faction:

| | |
|---|---|
| **+3 Allies** | helps even against their own interest; expects the same |
| **+2 Friendly** | helps if it creates no serious problems |
| **+1 Helpful** | helps if it costs nothing significant |
| **0 Neutral** | default |
| **−1 Interfering** | takes cheap opportunities to hurt you |
| **−2 Hostile** | actively seeks to hurt you, short of serious risk |
| **−3 War** | **+1 heat per score, −1 hold, PCs get 1 downtime action instead of 2** |

**No faction HP.** Degradation is the hold bit plus Tier: an operation targeting a known vulnerability costs the target a level of hold; if hold was already weak, it loses a Tier and stays weak.

**Economy:**

| Resource | Gained | Spent |
|---|---|---|
| rep | 2 per score, **+1 per Tier the target is above you, −1 per Tier below** | fills at 12 − turf; buys hold or Tier |
| coin | 2 minor / 4 small / 6 standard / 8 big / 10+ major job; minus a tithe of **Tier + 1** | Tier advance = **new Tier × 8** |
| turf | seized claims, max 6 | each point reduces the rep threshold by 1 |
| heat | 0 quiet / 2 contained / 4 loud / 6 wild; +2 if killing | reduce-heat downtime; cleared by incarceration |

**Downtime is rationed:** 2 activities per character per phase, 1 during war. Extras cost 1 coin or 1 rep. Six activities compete for two slots: Acquire Asset, Long-Term Project, Recover, Reduce Heat, Train, Indulge Vice.

That scarcity is why it works. Compare D&D 5e's downtime — fifteen activities, no budget, no opportunity cost, payoffs deliberately capped below adventuring — which was so comprehensively ignored that Wizards replaced the rules twice.

## 9.2 ACKS — the fully economic domain

The most explicitly financial model in the hobby. Everything reduces to gold per peasant family per month.

```
classification      civilized (within 50 mi of a city) | borderlands | wilderness
area_sq_miles       min 1; typical 32 (one 6-mile hex); max 500
land_revenue        3d3 gp/family/month, ROLLED ONCE, PERMANENT (3–9, avg 6)
families            each ≈ 5 people
stronghold_value_gp
morale              −4 to +4; base = ruler's CHA modifier; drifts toward base
tax_rate_gp         default 2 gp/family/month
garrison_spend_gp   required: civilized 2 / borderlands 3 / wilderness 4
vassals[]           each a domain assigned to a henchman
urban_settlements[] families 75–100,000; investment gates population cap;
                    market class I–VI derived from population; own morale track
```

**Cadence:** monthly population roll, revenue, expenses, vassal duty. Seasonal (every 3 months) morale roll and festival obligation.

The `land_revenue` field is the interesting one — rolled once at acquisition, permanent, and it's the domain's quality gene. Two domains of identical size can differ by 3× in value forever.

## 9.3 Ars Magica — the covenant

A persistent entity with its own life stages (Spring/Summer/Autumn/Winter), built in **Build Points**: low ≈ 200, medium ≈ 800, powerful ≈ 2000.

**The mechanic worth stealing: Boons are paid for by Hooks.** Every advantage the covenant has must be balanced by a problem — and Hooks are GM plot hooks. **It converts adventure seeds into a currency players want to spend.**

Vis economy: renewable annual sources cost 5 BP per pawn/year; stockpiles 1 BP per 5 pawns. Library = summae (reusable) + tractatus (one-shot) + lab texts. And a hard rule: **covenants do not gain Build Points during play** — in-play growth is organic, through magi creating and trading.

Time unit is the **season**, four per year, per magus. That's four decisions per character per game-year — the highest decision density of any between-session system found.

## 9.4 Pendragon — manor and winter

The only major system where the campaign clock is **calendrical and mandatory**: one adventure per game-year, aging is automatic, so retirement and succession are *scheduled* rather than accidental. The Great Pendragon Campaign spans ~80 years and is designed to outlive its player characters.

The **Winter Phase**, 6e, eleven steps: Solo Scenario → Personal Events → Experience Rolls → Economic Circumstances → Aging → Squire & Maiden → **Horse Survival** → Training & Practice → Tally Glory → Prestige Reward → Family Rolls.

Older-edition detail: a global 1d20 weather roll plus 2d6−7 per manor, cross-referenced against Stewardship for next year's standard of living. Aging rolls from **35+**. Experience improves by rolling 1d20 *over* your current score. Passive glory from traits and passions at 15 or 25 points each, capped at 100. **Heirs inherit one quarter of a parent's glory at age 14.**

And the trait system: **13 opposed pairs** (Chaste/Lustful, Energetic/Lazy, Forgiving/Vengeful, Generous/Selfish, Honest/Deceitful, Just/Arbitrary, Merciful/Cruel, Modest/Proud, Pious/Worldly, Prudent/Reckless, Temperate/Indulgent, Trusting/Suspicious, Valorous/Cowardly) — each pair sums to 20, and high scores can compel behavior.

## 9.5 Stars Without Number — factions

`Force · Cunning · Wealth` (each ~1–8), plus HP and a list of **Assets**. Assets are purchased with the corresponding attribute and have their own stats. Factions take turns on a defined cadence, roll against each other, and can be destroyed.

The important structural choice: a faction's *capabilities* are its assets, which are individually destructible. Losing HP is losing infrastructure, not morale.

## 9.6 Traveller's Universal World Profile

A whole planet as nine characters: `A788899–A`

```
A 7 8 8 8 9 9 – A
│ │ │ │ │ │ │   └── Tech Level
│ │ │ │ │ │ └────── Law Level
│ │ │ │ │ └──────── Government
│ │ │ │ └────────── Population (order of magnitude)
│ │ │ └──────────── Hydrographics (tens of percent)
│ │ └────────────── Atmosphere
│ └──────────────── Size (diameter)
└────────────────── Starport class
```

Selected decode tables:

**Population** (2d6−2, order of magnitude): 0 = uninhabited · 1 = single family · 2 = 100+ · 4 = 10,000+ · 6 = 1,000,000+ · 9 = 1 billion+ · C = 1 trillion, a world-city.

**Government** (2d6−7 + Population): 0 None · 1 Company · 2 Participating Democracy · 3 Self-Perpetuating Oligarchy · 4 Representative Democracy · 5 Feudal Technocracy · 6 Captive Government · 7 Balkanisation · 8 Civil Service Bureaucracy · 9 Impersonal Bureaucracy · A Charismatic Dictator · B Non-Charismatic Dictator · C Charismatic Oligarchy · D Religious Dictatorship.

**Law Level** is one digit with **six parallel meanings** — weapons banned, drugs, information, technology, travellers, and psionics all read off the same number in different columns.

And a hard cross-field constraint baked into the schema: **if Population = 0, then Government, Law Level, and Tech Level are all forced to 0.**

---

# PART 10 — TRAVELLER'S UNIVERSAL PROFILES IN FULL

The single most relevant precedent for a system that wants one representation across people, places, and things.

## 10.1 The shared alphabet — pseudo-hex

Every profile packs one value into one character. **I and O are never used**, because they look like 1 and 0.

| 0–9 | A | B | C | D | E | F | G | H | J | K | L | M | N | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0–9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 |

## 10.2 UPP — Universal Personality Profile

Six characters, no separators: `STR DEX END INT EDU SOC`

`A97642` = STR 10, DEX 9, END 7, INT 6, EDU 4, SOC 2.

Alternate labels exist for non-humans and robots — DEX becomes Agility or Grace, END becomes Stamina or Vigour, EDU becomes Training or Instinct, SOC becomes Charisma or Caste. **The slot means something structurally; the label is per-kind.**

Optional extra characters get appended in play: Psionic Strength, Sanity, Territory, and in some editions Wealth, Luck, Morale. That variable length is a real cost of the design.

## 10.3 USP — Universal Ship Profile

```
TT-1234567-890ABC-DEFGH-I    MCr cost, tonnage
│  └──────┘ └────┘ └───┘ └── fighter squadrons
│  performance defence offence
└── ship type code
```

| Block | Positions | Fields |
|---|---|---|
| Type | — | 2–4 alphanumerics (AF = far trader, XCF = express courier, BC = battle cruiser) |
| Performance | 1–7 | tonnage · **hull configuration** · jump rating · manoeuvre rating · power plant · computer model · crew code |
| Defence | 8–13 | armour · sandcasters · meson screen · nuclear damper · force field · repulsors |
| Offence | 14–18 | lasers · energy weapons · particle accelerators · meson guns · missiles |
| Tail | 19 | fighter squadrons |

**Configuration codes** — the entire hull-shape/streamlining/price tradeoff in one character:

| Code | Configuration | Streamlining | Price |
|---|---|---|---|
| 1 | Needle / Wedge | Streamlined | +20% |
| 2 | Cone | Streamlined | +10% |
| 3 | Cylinder | Partial | ±0 |
| 4 | Close Structure | Partial | −40% |
| 5 | Sphere | Partial | −30% |
| 6 | Flattened Sphere | Streamlined | −20% |
| 7 | Dispersed Structure | Unstreamlined | −50% |
| 8 | Planetoid | Unstreamlined | ±0 |
| 9 | Buffered Planetoid | Unstreamlined | ±0 |

**A real decode** — Empress Marava class Far Trader, `AF-21211R1-000000-00000-0`, MCr59, 200 tons:
200 tons · needle hull, streamlined · Jump-2 · 1G · power plant 1 · computer Model/1 bis · crew code 1 · no defences · unarmed · no fighters.

## 10.4 The part that matters most — in-band annotation

The USP is designed to be **decorated in place**, and this is the idea worth stealing outright.

**Parentheses = a supplementary value on the preceding field.**
`FC-R4425J3-29(B,G)9901-9(B,G)9(4,5)999(42,60)-30` — extra jump fuel after the jump digit, agility after the manoeuvre digit, frozen watch after crew, batteries-bearing / batteries-total after each weapon.

**Square brackets = damage, recorded without mutating the base value.**
`BC-A244(1)[3]7G2-000510-5(2)[1]02(2)03(2)-0` — the manoeuvre drive has taken a hit `[3]`; one laser battery `[1]` is knocked out.

The base profile never changes. Damage is a decoration on top of it. **The printed USP is a fold of (design record + damage records)** — which is the ledger pattern, invented in a tabletop wargame in 1979 because there was no other way to keep a ship's identity stable while its state changed.

---

# PART 11 — REUSABLE PRIMITIVES

Things worth stealing regardless of what the rest of the system looks like.

**Blades' magnitude table.** One 0–6 ladder reused as tier, gang scale, item quality, cohort quality, supernatural force, and the target for acquiring an asset:

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Area | closet | small room | large room | small bldg | large bldg | city block | — |
| Scale | 1–2 people | 3–6 | 12 | 20 | 40 | 80 | 160 |
| Duration | moments | minutes | an hour | hours | a day | several days | a week |
| Range | reach | a dozen paces | a stone's throw | down the road | several blocks | across the district | across the city |
| Quality | Poor | Adequate | Good | Excellent | Superior | Impeccable | Legendary |
| Force | Weak | Moderate | Strong | Serious | Powerful | Overwhelming | Devastating |

One ladder, six meanings, learned once.

**The single "how much does this matter" scalar.** Every system that generalizes converges on one: Hit Dice → level → Challenge Rating → Blades' Tier → Fate's skill rating for non-people → "Danger Level 1–10." Cypher is purest: a creature's level *is* the target-number generator for everything about it.

**max() rather than sum() for stacking states.** City of Mist. Eliminates an entire category of problem.

**Named states as types, not modifiers.** A condition is something other rules can key on; a −2 isn't.

**Tags as compact composite records.** `2-harm hand messy` — magnitude, range, and behavior in one string, extensible without a schema change.

**Aspects as one type with a lifetime field.** `(text, scope, lifetime, free_invocations)` covers permanent character traits, scene features, injuries, and one-shot boosts.

**Countable constraints instead of computed ones.** Inventory slots instead of weight. Visible, fast, and it can become the character (Cairn's full pack = 0 HP).

**Derived values as defaults with recorded overrides.** The 3e failure wasn't derivation — it was derivation with no way to record "I overrode this on purpose." Store the value, the derived default, and the reason.

**Rationed action budgets, not activity lists.** Blades gives two downtime actions and prices extras. 5e listed fifteen with no budget and was ignored.

**Boons paid for by Hooks.** Ars Magica converts GM plot seeds into a resource players spend to get advantages.

**Two location tables gated on a threshold.** Traveller's external/internal split — the same roll means different things once the outer layer is gone. Cheap escalation with no extra bookkeeping.

**Three hits kills any system.** Traveller ships. Uniform degradation with per-system flavor, so you never need a per-system HP number.

**Fixed-width, human-readable, machine-parseable records.** The Traveller profile family. Ordinal rather than categorical wherever possible, with deliberate collision-avoidance in the alphabet.
