# The Dictionary

**The permanent reference for this platform.** Every term, every list, every decision.

Two rules for this document:

1. **Every word used in the system is defined here, exactly once.** If a term is used in code, in a design conversation, or in player-facing text, its definition lives here and nowhere else.
2. **Every list the system needs appears here**, including the ones that don't exist yet. A list that isn't written down is a decision nobody made.

Status markers on lists: **SETTLED** (decided, permanent) · **PARTIAL** (shape decided, contents open) · **PRELIMINARY** (a candidate set exists, deliberately not frozen) · **PENDING** (not yet started) · **RETIRED** (the list was deleted; its number is left vacant). A list may also be **BLOCKING**, meaning nothing can be built until it is done, and L6 is **CLOSE LAST** by decision.

Sections marked **PROVISIONAL** are settled in shape with their open questions listed inline.

---

# Part 1 — Structure

## Substrate
The data model, the instruction set, the execution semantics, and the frames everything runs inside. **Never versioned.** Everything that is not the Substrate is a Component.

## The test for what belongs in the Substrate

> **If it is only true in some Settings, it belongs to a Component. If it is true in all of them, it belongs to the base Ruleset — and if the Substrate cannot function without it, it is a Socket.**

Three tiers, one question. This is the sharpest statement of the Substrate line we have, and it settles arguments that otherwise run on taste: a Setting's particular pantheon is Setting-specific, so it is a Component. Bodies and minds exist in every Setting, so they are base. Time must exist for anything to be pinned at all, so it is a Socket.

## Component
Any rules subsystem. Independently versioned and purchasable. **The base game is built as Components** — default progression is a Component, default harm is a Component. Only Dylan authors Components.

## Socket
**A named hole in the Substrate that some Component must fill.** The Substrate declares the Socket and its contract; it never supplies the occupant.

Most Components are furniture — add them, remove them, the game still runs. A Socket occupant is a load-bearing wall. Exactly one Component fills each Socket at a time, **never zero and never two**, and a Bundle with an empty Socket must fail to load. CI-enforceable.

The Socket's *contract* is Substrate, and therefore frozen forever. The *occupant* is a Component and can be swapped — but swapping one is an Edition-level change, never a casual toggle, because everything else in the Bundle is written against what it publishes.

### Every Socket has two halves

**Vocabulary — Substrate.** The names content is allowed to depend on. A spell costing *one action* needs `action` to be a word that exists no matter which Budget occupant is installed. A vector pinned to *the start of the target's turn* needs `start of turn` to be a Moment kind that exists no matter which Time occupant is installed. Vocabularies are **additive-only**: new names may be published forever, none may be removed or redefined.

**Behaviour — the occupant.** How many actions you get and when they come back. Which Moments exist, in what order, and who is in them. All of it swappable, none of it something content names directly.

The split is what makes a Socket safe. Without it, either content depends on an occupant's internals — and swapping breaks every spell ever written — or the Substrate ends up owning the economy it was trying to delegate.

Sockets are why "everything above the Substrate is a Component" was true but misleading. It still is true. Some of those Components just cannot be absent.

**Three Sockets, Aug 2026: Place, Resolution, Landing.** Time and Budget were Sockets until August 2026 and are now Substrate — see *Why Time and Budget are not Sockets*, below.

**Socket occupants are frozen per Setting.** Not a live toggle, not a house rule. A Setting is a Bundle plus world material, and its Socket occupants are part of its identity; changing one produces a different Setting, and moving an existing Campaign across is a Conversion. Components, by contrast, may be added or removed within a Setting.

**LIST: Sockets — L27.**

## Why Time and Budget are not Sockets

They were, and the reasoning was sound: the Substrate cannot run without *some* answer to "which Moments exist" or "what does an ability cost." That is the Socket test and both passed it.

What the test misses is that **a Socket is a hole in the explanation, not just in the code.** A rulebook that says *"this costs 3 doubloons; how many doubloons a turn holds depends on your Setting's Budget occupant"* is much worse to read than *"you get three actions."* Worse, every worked example has to caveat itself, which makes the whole documentation set — and every spell, ability and item ever written — harder to understand than it needs to be.

The objection to moving them up was that a Setting might want turns lasting a week, or a month, or no turn order at all, and freezing one turn model forever would make those impossible.

**That objection dissolves once you remember a Component adds rather than replaces.** A month-scale downtime structure does not have to be compatible with second-scale abilities — content written for one simply does not apply to the other. So the Substrate ships what a turn-based game needs for abilities to be written and understood, and Components layer coarser clocks and richer economies alongside it, forever.

The price, stated plainly: **the turn model is the first actual game-design decision frozen into the Substrate.** Everything before it was machinery — Verbs, layers, arithmetic, no opinions. This one is an opinion, it is unversioned, and it can never be fixed. That is why it gets its own lists (L31, L32) and the same attack treatment every other settled list got.

## Bundle
A named, curated set of Components at pinned versions. **Valid only if every Socket is filled.**

## Ruleset
*The* standard Bundle — the default game. Versioned as **Editions**.

## Setting
A Bundle plus world material, vocabulary, and dial settings. Authorable by users.

## Adventure
Content and shape — specific tracking, optional victory conditions, a beginning and an end. Authorable by users.

## Edition
A version of the Ruleset. First Edition, Second Edition. Campaigns pin one forever and never leave it without an explicit Conversion.

## Revision
A change *within* an Edition. Non-breaking, automatic. The test: would this change cause an existing Campaign's history to produce different state? No → Revision. Yes → Edition.

## Conversion
Moving a Campaign from one Edition to the next. Opt-in, previewable, recorded as a Record in the Ledger so history before and after fold under different rules.

---

# Part 2 — What exists

## Entity
Any noun. Anything the system tracks separately, with its own identity, that persists.

**Test:** if a Verb can point at it, it is an Entity.

A character is an Entity. A sword is an Entity. A rumour is an Entity — it gets passed, changes, can be traced and suppressed. A wound is *not* — it is a State on an Entity.

**An Entity can be created mid-sentence with nothing filled in.** A GM saying "there's a crowbar by the door" creates a valid Entity with a name and an ID and no other data. Everything else may stay blank forever.

**Nothing is deleted.** The Ledger only appends, so `destroy` records "no longer present" rather than removing anything.

## Category
A label on an Entity saying what kind of thing it is. **An Entity may carry many.** Each Category brings a set of Attributes with it, empty until filled.

A haunted ship is `structure` + `vehicle` + `haunted`. A player's character is `person` + `character`. Categories compose rather than nest — there is no single tree that everything hangs from.

*(This is what library science calls **faceted classification**: instead of one hierarchy where every thing has exactly one place, you use several independent label sets that combine. It is the approach that survived — see `categorization-and-action.md`.)*

**LIST: Categories — PENDING.** See L1.

## Attribute
A named value attached to an Entity. Attributes come from two places:

- **Universal Attributes** — present on every Entity regardless of Category.
- **Category Attributes** — added by each Category the Entity carries.

**LIST: Universal Attributes — PENDING.** See L2.
**LIST: Category Attributes, per Category — PENDING.** See L3.

## Noun
A published data schema — the shape of something the system can hold. **Nouns are one of five kinds and no others:** Capacity · Tag · State · Resource · Relationship. They behave differently under change, aggregation and rendering, which is why the kinds exist at all. Nouns are extensible forever; Verbs are not.

## Actor
Who or what wrote a Record. `user` · `system` · `agent`. An agent Record also carries the model, the session, and the human who approved it. **Agents never write as humans.**

## Facet
One Component's data attached to one Entity. A Component declares which Categories it attaches to, and may read and write only its own Facets.

## Tag
A label attached to an Entity indicating membership in a loose group, carrying an optional magnitude. Non-exclusive — an Entity may hold any number of Tags simultaneously and they never conflict.

*Flammable. Metal. Sacred. Swordfighting 3. Waterlogged 2.*

**Tags are identified by ID, not by name.** A `flammable` Tag published by the core Ruleset and a `flammable` Tag published by a Setting are **different Tags with different IDs**, and the system never treats them as the same thing. An index records each Tag's origin.

**Tags never imply other Tags.** If metal things conduct, the Component asserts both Tags. No inference, no chains.

**Tag combinations may produce effects**, but through a Component's formula, never through the Tag system itself.

**LIST: Core Tag vocabulary — PENDING.** Keep under thirty.

## State
A named condition, optionally with magnitude, **exclusive within its axis**. Prone or standing, never both.

**The Substrate defines the shape of a State and ships almost none of them** — the same treatment Resources get. Most States live in Components. A State definition carries: a name, its axis, whether it has a magnitude, and an **optional maximum**. The max is what keeps *poisoned 47* from being reachable now that values add by default.

**States end through a Verb.** Nothing else clears them. A duration is a clock that fires a Verb; a condition is a trigger that fires a Verb.

**The line between State and Resource:** continuous number → Resource. Small set of named alternatives → State. Crossing a Resource threshold can set a State.

**LIST: State axes — PENDING.**

## Resource
A depletable, replenishable value with named thresholds.

**The Substrate defines what a Resource is and ships none.** Health is a Component. Coin is a Component. Stress is a Component. A setting may have none of them.

## Relationship
**A Category of Entity**, not a special structure. A Relationship Entity has its own Attributes, and contains one **Connection** for each participating Entity.

Participating Entities hold the Relationship's ID, the same way a character holds the ID of a sword they carry.

## Connection
One participant's side of a Relationship. Carries labelled magnitudes describing that participant's stance — trust, obligation, resentment, ownership — each as a separate named value.

**Connections are stored per participant, independently.** A loves B while B tolerates A is the normal case, not an exception.

## Asset
An Entity that can be authored as content: a character, a creature, a place, an item, a faction. **Asset types are authored only by Dylan; Asset instances may be authored by users** where the authoring capability exists.

**LIST: Asset types — PENDING.**

---

# Part 2A — Channels, Dimensions, and how anything affects anything

**This is the core mechanism of the system.** It governs every interaction between any two things, not just damage.

## Dimension
A named axis along which effects can act. *Thermal. Kinetic. Vital.* A Dimension is not a damage type — it is one of the underlying directions damage types are built from.

**LIST: Dimensions, per Space — PENDING.**

## The Channels — SETTLED, Aug 2026 (L23)

**Eighty-eight.** Every row sums, in absolute value, to exactly **100**. No two share a position. Every Dimension is used on both signs.

Read the signs: **all-negative harms, all-positive helps, and mixed is a visible trade.** Only three of the eighty-eight are mixed — `humble`, `menace` and `enthrall` — and each is a trade you would want to see.

```
                P    P    P    P    P    P    P    M    M    M    S    S    Y    Y
             temp intg subs vitl vigr mobl acui comp clar will rgrd stnd work essn

── FORCE & WEAPONS
impact            -100                                                            
pierce             -80       -20                                                  
rend               -60       -40                                                  
bleed              -30       -70                                                  
crush              -70  -30                                                       
stagger            -50            -50                                             
concussion         -50                                -50                         
knockdown          -40                 -60                                        

── ELEMENTS
fire         +100                                                                 
frost        -100                                                                 
lightning     +30  -70                                                            
blast         +50  -50                                                            
shockwave          -60                      -40                                   
acid                   -100                                                       
molten        +50       -50                                                       
scald         +60            -40                                                  
frostbite     -50            -50                                                  
exposure      -40                 -60                                             
flash                                       -70       -30                         

── AFFLICTION
venom                        -70                      -30                         
blight                  -50  -50                                                  
agony                        -50                      -50                         
fatigue                           -70            -30                              
wither                       -60  -40                                             
rot                     -60       -40                                             
numb                                   -40  -60                                   

── BINDING & MOVEMENT
slow                                  -100                                        
entangle                          -30  -70                                        
snare                        -20       -80                                        
cripple                      -40       -60                                        
pin                -50                 -50                                        
petrify            +40                 -60                                        

── FEAR & MIND
dread                                           -100                              
terror                            -30            -70                              
confusion                                            -100                         
panic                                            -60  -40                         
charm                                                 -30  -70                    
domination                                                -100                    
despair                                          -50       -50                    
compel                                                     -60       -40          
daze                                        -40       -60                         
madness                                          -50  -50                         
transfix                               -50       -50                              

── STANDING
praise                                                         +100               
scorn                                                          -100               
endorse                                                             +100          
discredit                                                           -100          
champion                                                        +60  +40          
slander                                                         -70  -30          
denounce                                                        -20  -80          
humble                                                          +50  -50          
menace                                                          -50  +50          
humiliate                                        -50                 -50          
embolden                                         +60                 +40          
enthrall                                                   -50  +50               

── MYSTIC
enchant                                                                  +100     
dispel                                                                   -100     
infuse                                                                        +100
drain                                                                         -100
ward                                                                      +60  +40
siphon                                                                    -50  -50
bind                                                                      +70  -30
surge                                                                     -40  +60
curse                        -30                                -30       +40     
blessing                     +30                 +30                      +40     
soulburn                     -40                                               -60
hallow                                           +40                      +60     

── RESTORE & PROTECT
mend                        +100                                                  
rally                            +100                                             
courage                                         +100                              
lucidity                                             +100                         
unbind                                                    +100                    
brace             +100                                                            
seal                   +100                                                       
haste                                 +100                                        
keen                                       +100                                   
regenerate                   +60  +40                                             
fortify            +60  +40                                                       
bolster            +60       +40                                                  
preserve                +60  +40                                                  
steady                                           +50  +50                         
soothe                            +40            +60                              
sharpen                                     +40       +60                         
vigilance                                   +60       +40                         
quicken                                +60  +40                                   
steel                                            +50       +50                    
freedom                                +60                 +40                    
cleanse                      +50                                          -50     

             temp intg subs vitl vigr mobl acui comp clar will rgrd stnd work essn
used  +         5    4    3    6    3    3    4    7    4    3    4    4    6    3
used  −         3   12    5   13    7    9    4    8    9    5    5    6    4    4
```

### The trades are the point

| | | |
|---|---|---|
| **`petrify`** | mobility −60 · integrity **+40** | turned to stone: harder to break, and you cannot move |
| **`enthrall`** | will −50 · regard **+50** | they obey you *and* adore you |
| **`menace`** | regard −50 · standing **+50** | liked less, feared more |
| **`humble`** | regard **+50** · standing −50 | liked more, diminished |
| **`cleanse`** | vitality +50 · working −50 | cures the poison *and* strips the curse |
| **`concussion`** | integrity −50 · clarity −50 | breaks and rattles, in one Channel |

### Two rules this list is held to

**No two Channels may share a position.** If they do, they *are* the same Channel with two names — which is D&D's force-versus-thunder problem, visible here as identical coordinates. **CI rejects it**, and no other system in the field can even detect it.

**Every Dimension must be used on both signs.** Otherwise an axis quietly dies because nothing ever pointed at it — which is exactly how a quarter of one published bestiary ended up immune to poison while almost nothing resisted force.

### What is deliberately not here

**Silence, invisibility, knockback, aging, size change.** Each has a home elsewhere: knockback and size are the Place Socket and Scale; invisibility is a Tag; silence and aging are States set by Thresholds *on* these vectors. **Conditions are not Channels** — five unrelated published systems reached that conclusion independently, and putting them in the same list is what produced the dead type.

**Expected to shrink.** The closest pairs, and the first candidates to go: `blast` beside `lightning`, `bleed` beside `rend`, `rot` beside `blight`, `pin` beside `snare`.

---

## Dimension Space
A named set of Dimensions that belong together and can interact. Packets only interact with other Packets in the same Space. **Two Packets in different Spaces never interact at all**, which is how the system stays comprehensible as it grows.

**Five Spaces — SETTLED, Aug 2026 (L21).**

| Space | What it governs |
|---|---|
| **physical** | Bodies and matter |
| **mental** | The inside of one mind |
| **social** | The space *between* minds — what others think of you and owe you |
| **mystic** | Workings, and what unmakes them — magic, ki, mana, cultivation, divinity |
| **attempt** | How well someone did at something. Two layers — seven **Domains**, fifteen **Dimensions** (L29, settled) |

### A Space limits a vector, never an ability

**One ability places as many vectors as it needs.** A poisoned blade is one thing in the fiction that places *two* vectors: a physical one and a mental one. They resolve independently and each meets its own Guards.

So *"physical and mental never interact"* does not mean a poison cannot do both. It means the two parts are computed separately and do not cancel each other — which is right, because armour should not blunt a hallucination. **The walls are much cheaper than they look, and that is what makes four Spaces comfortable rather than restrictive.**

### Which Space a vector belongs to

> **A vector's Space is decided by what it changes, not by what caused it.**
>
> - changes a body or matter → **physical**
> - changes what is happening inside one mind → **mental**
> - changes how others regard or treat someone → **social**
> - is how well someone did at something → **attempt**

Intimidating a man in a tavern makes him afraid (**mental**) *and* makes the room see you as dangerous (**social**). One action, two vectors, no ambiguity. A charm spell is purely mental — it is not persuasion, it is tampering. Persuasion is purely social — you did not reach into their head, you changed what they owe you.

### Why mystic is a Space, and how it avoids swallowing everything

**The deciding case is counterspelling**, exactly as psychic harm decided `mental`. A counterspell meets a spell and unmakes it — that is the fire-meets-ice property, and no axis in the other four Spaces can host it. Dispelling, ward-breaking, severing a binding, draining someone's power: none of these change a body, a mind, or a standing.

**The rule that stops it eating the game** is the one already in force: *a vector's Space is decided by what it changes.*

> **A working's *effects* live in whatever Space they change. The working's *own existence* lives in `mystic`.**

Magical fire burns you in `physical` `temperature`, and plate armour, water, and being made of fire all help exactly as much as they would against a torch. The **spell** — its taking hold, its persisting, its being interruptible — is the mystic part.

Which produces something settings with magic have always had and no system models cleanly: **two independent defences against one fireball.** *Dispel it* is a mystic-Space cancellation before it ever resolves. *Survive it* is a physical-Space one. A wizard and a fire elemental defend against the same spell in different Spaces, and neither defence is a special case.

**This overrides the Component test, deliberately, and it is worth knowing it was an override.** *If it is only true in some Settings, it is a Component* would put magic in a Component, and a hard-science Setting genuinely has no mystic content. Two things outweigh it:

1. **An empty Space costs nothing.** A Setting with no magic simply has no Channels in it.
2. **If each magic Component published its own Space, no two could ever meet.** A druid's working and a necromancer's would be arithmetically unable to touch, and counterspelling across traditions would be impossible. That is a large loss for a platform whose whole claim is that independently authored content composes.

The split that resolves it: **the Space is infrastructure, the Channels are content.** The base Ruleset ships `mystic` as shared arithmetic; Components fill it with the Channels and Resources that make a tradition — ki, mana, cultivation, divinity. The same relationship `physical` has to `fire`.

### Why mental is separate from social

The deciding case is **psychic harm**. Under three Spaces a mind flayer's blast has to be `vital`, which is not a body injury, or social pressure, which it is not either. Neither is honest.

The separation also buys two things worth having. **Mental Guards become a real category** — *mental fortitude* stops being a saving throw and becomes a Guard sitting on you, working exactly like armour. And **the bard bolstering you against a dragon's terror now works arithmetically**: both are mental vectors of opposite sign, and they cancel, even though one came from a friend talking and the other from a monster existing. That is the fire-and-ice property appearing in a completely different domain, which is the best evidence so far that the model generalises.

### Adding a Space later

**Adding a brand-new Space is free** — purely additive, because nothing existing interacts with it anyway. **Splitting or merging existing Spaces is an Edition break**, because things that used to cancel stop, or things that never met start.

So a Setting that needs a Space of its own in year three may have one, published by a Component. The discipline is that the base five should carry almost everything, and a new Space needs a real argument: *this genuinely does not change a body, a mind, a standing, a working, or how well someone did.*

**LIST: Dimension Spaces — L21, SETTLED.**

## Dimension and Resource are two ends of one pipeline, never alternatives

A **Dimension** is the transient side: the axis a push travels along, where things cancel and combine. A **Resource** is the persistent side: what survives the pipeline and accumulates. `temperature` is a Dimension; the injury it lands into is a Resource.

**So asking whether a thing is "a Dimension or a Resource" is the wrong question — anything that is a Dimension automatically also has a Resource, because that is what Landing means (L25).** The real question is narrower:

> **Is there something that is meaningfully the opposite of this, that should meet it and cancel it *before it lands*?**

If yes, it earns a Dimension, and it gets a Resource for free. If no, it is only ever a Resource that goes up and down, moved by Verbs.

## The Dimensions — SETTLED, Aug 2026 (L22)

**Fourteen, across the four non-attempt Spaces.** The `attempt` Space's fifteen are in Part 2C and are not available to Channels.

### The sign convention — one rule, everywhere

> **Every Dimension is a property of the target. Negative always means *less of it* — damaged, taken away, diminished. Positive always means *more* — restored, given, strengthened.**

Two axes are **bipolar**, where displacement either way is what matters and neither sign is the harm direction: **`temperature`** and **`working`**.

**Why it had to be this way.** The first draft pointed the physical axes one way and the mental, social and mystic axes the other, so a blow that rattled the mind read as `kinetic +5 / clarity −5` — two harms, opposite signs, unreadable. Under the rule above the same Channel is `integrity −5 / clarity −5`, and **you can now tell what a Channel does from its signs alone**: all-negative harms, all-positive helps, and mixed is a visible *trade*. Across all 88 Channels only three are mixed, and every one of those is a genuine trade.

**physical**

| Dimension | Positive | Negative | The pair that proves it |
|---|---|---|---|
| **temperature** | hotter | colder | fire and frost — the reference case for the whole model. **Bipolar** |
| **integrity** | repaired, reinforced | broken by force | a charge meeting a shield wall |
| **substance** | sealed, restored | dissolved, corroded | acid meeting a mending ward |
| **vitality** | healed, cured | wounded, poisoned, diseased | a regeneration aura meeting incoming venom |
| **vigor** | rested, energised | exhausted, spent | a forced march meeting a stimulant |
| **mobility** | hastened, freed | slowed, restrained, rooted | a haste meeting an entangle |
| **acuity** | keen, sharp-eyed | blinded, deafened, numbed | a light spell meeting a blinding flash |

**`mobility` and `acuity` were missing entirely**, and building the Channel table is what found them. Slow, haste, entangle, root, blind, deafen and numb — two of the most-used effect categories in any game — had no axis at all and would have had to be faked as States.

**mental**

| Dimension | Positive | Negative | The pair |
|---|---|---|---|
| **composure** | steady, emboldened | shaken, afraid | the bard's encouragement meeting the dragon's terror |
| **clarity** | lucid, sharp | confused, deceived | a clarity effect meeting an illusion |
| **will** | your mind is your own | dominated, compelled | breaking a charm meeting the charm |

*Afraid, confused and controlled are three different bad nights. Being dominated is not being confused — you are perfectly lucid and cannot stop.*

**social**

| Dimension | Positive | Negative | The pair |
|---|---|---|---|
| **regard** | admiration, warmth | contempt, disgust | praise meeting slander |
| **standing** | authority, position raised | diminished, discredited | being vouched for meeting being denounced |

*A feared crime boss has standing without regard; a beloved fool has the reverse.*

**mystic**

| Dimension | Positive | Negative | The pair |
|---|---|---|---|
| **working** | a working imposed on the target | workings unmade | **counterspell meeting the spell** — the case that created this Space. **Bipolar**: a blessing and a curse both impose |
| **essence** | powered | drained, burned out | a vampiric drain meeting an infusion |

### The test, and the anti-test

> **Is there something meaningfully the opposite of this, that should meet it and cancel it *before it lands*?**

If yes it earns a Dimension, and gets a Resource for free because that is what Landing means. If no, it is a **Tag**, a **State**, or a Resource moved by Verbs.

**The anti-test catches most bad candidates: a Dimension whose opposite side you cannot describe is not a Dimension.** `piercing` has no opposite — it is a Channel positioned mostly on `integrity`. `holy` has no opposite that is not simply "unholy," which is the same axis.

### Wards and regeneration cancel; healing restores

`vitality`'s **positive** side is mending in flight — a regeneration aura standing on you, meeting incoming poison at R-1000. That is a different mechanism from restoration applied afterwards at R-1250, and both are legal. Settings have always drawn this distinction without being able to say why; here it falls out of which layer the vector resolves at.

### Broadcast, or per-pair

`trust` passes the opposite test — building confidence against sowing suspicion — and is still **not** a Dimension, because trust is inherently *per-pair*. That gives the discriminator for this Space:

> **A social Dimension is something that can be pushed at someone from outside. A per-pair state is a Connection on a Relationship.**

### The asymmetry that governs this list

**A missing Dimension is recoverable.** Add one in year three; unspecified defaults to zero; nothing that exists folds differently.

**A Dimension that turns out to be two things is not.** Splitting it changes what every existing Channel means.

**And each one costs** — every Dimension widens every vector in its Space, every Guard that wants full coverage, and every Channel's position statement. **Err few.**

## Channel
A named **direction over every Dimension there is** — an integer on each, in **hundredths**. A Channel carries no size of its own.

`fire` is not a special thing the code knows about. It is a name for a position:

```
fire         temperature +100
frost        temperature −100
impact                          integrity −100
lightning    temperature  +30   integrity  −70
concussion                      integrity  −50   clarity −50
venom                                            clarity −30   vitality −70
```

### A Channel is not confined to one Space

**This was wrong in the first draft and it mattered.** A Channel positions over *all* Dimensions, and Spaces are a property of **Dimensions** — which of them can cancel each other — not of Channels. There is no such thing as *which Space is this Channel in*.

Fatigue tires the body and dulls the spirit. Poison sickens and clouds. A concussion breaks and rattles. None of those could be written when a Channel lived in one Space, and all of them are ordinary.

**Why the sum still spans everything.** The obvious alternative — *a Channel gives 100% to every Space it touches* — makes breadth free, and therefore makes every multi-Space Channel strictly better than a single-Space one at the same magnitude. Guards do not fix it, because Guards are per-Space too:

```
armour 3, mental fortitude 3
  pure exhaustion, magnitude 10          → physical 7, mental 0
  fatigue at 100%/100%, magnitude 10     → physical 7, mental 7
```

**And nothing is lost by summing across Spaces**, because the same effect is still reachable — it just has to say so in the magnitude:

```
100% to each Space:  fatigue,  magnitude 10   →  10 physical, 10 mental
summing to 100:      fatigue 50/50, magnitude 20  →  10 physical, 10 mental
```

Identical. The only difference is that the doubling appears in the magnitude, where a designer can see it and price it, instead of hiding in the Space count. **Breadth means thin, and a Channel's position prices itself** — which is the whole reason for a coordinate model.

### Two rules that fall out of it

**A Channel's components must all land on the same target.** Intimidating a man makes *him* afraid and makes *the room* see *you* as dangerous — two targets, so that is one ability placing two vectors, never one Channel.

**"Universal" Guards are universal within a Space.** Armour 3 reduces the physical portion of a `concussion` and leaves the clarity portion alone. Otherwise plate blunts a headache.

**A base Channel's values sum, in absolute value, to exactly 100.** That is why lightning is `30 / −70` and not `100 / −100`. It makes magnitude mean the same thing for every Channel — one unit of fire and one unit of lightning are one unit of force applied — and it makes a magnitude of 1 mean the same amount of force whichever Channel carries it. Sum-of-absolute-values, never a square root; there are no square roots anywhere in this system.

Creating a new damage type means **placing it in the Space** — nothing else. Its relationship to every existing type is then already determined.

**LIST: Named Channels and their positions — L23, SETTLED.** Eighty-eight, in Part 2A.

## Direction and magnitude — the two halves of a vector

Every vector is two separate things, and keeping them separate is what makes the arithmetic work.

**Direction** is a set of **whole percentages** — how much of this thing is each Dimension. They sum, in absolute value, to exactly 100. `fire` is 100 temperature. `lightning` is 30 temperature and −70 integrity. Integers, never decimals.

**Magnitude** is a **whole number** — how much there is of it. An integer, at a Scale.

**Resolved value on a Dimension = direction × magnitude.**

```
fire,      magnitude 8   →  temperature +8
cold,      magnitude 6   →  temperature −6
lightning, magnitude 10  →  temperature +3   integrity −7
```

**A Channel's direction is never modified.** It belongs to the Channel and states what kind of thing this is. Nothing bends it — all modification of a harm vector happens to magnitude.

*An **attempt's** direction is a different thing: it is computed from the player's Allocation Points rather than declared by a Channel, and **Shaping** acts on the allocation before a direction exists. See Part 2C. The rule that a declared Channel is immutable is untouched by it.*

## Nothing is computed until it resolves

**A vector's magnitude is not assembled when the vector is placed. It is assembled at the Moment it resolves.**

This is forced by cooperative play. One pyromancer throws a fireball on their turn; a second casts an amplifier before it lands. If the fireball's number were fixed when it was thrown, the amplifier could never reach it. So a placed vector carries its *ingredients* — a base magnitude and a list of modifiers — and the arithmetic happens once, at the Moment, with everything that is present by then.

This makes the model simpler, not more complex: there is exactly one place where anything is computed, which is the same "gather everything present and resolve once" rule that governs the rest of the system.

## Snapshot and ambient modifiers

A modifier is captured at one of two times, and this is a field on the modifier:

- **Snapshot** — captured when the vector is placed. The sword you swung *with*. Frozen at placement, applied at resolution. Dropping the sword afterwards changes nothing.
- **Ambient** — present at the target or in the area at the Moment of resolution. The amplifier cast after the fireball was thrown; the vulnerability the target picked up in between.

**Default:** source-side modifiers snapshot; target-side and area-side modifiers are ambient. Content may declare otherwise.

Both kinds sum together at resolution. They are the same mechanism with different capture times.

## Three roles, one mechanism

Everything that can be placed is the same kind of object — pinned to a Moment, with a scope, a window, an identity, and a Layer. **The Layer is what makes it one of three things**, because the Layer says where in the pipeline it acts:

| Role | Carries | Acts at | Example |
|---|---|---|---|
| **Vector** | direction + magnitude | the combine stage | a fireball, a shove, a heal |
| **Modifier** | a condition + a percentage or an absolute | the magnitude stage, *before* combining | *+100% to temperature-positive*, *+2 fire* |
| **Guard** | a value per Dimension — proportional or flat | the subtract stages, *after* combining | armour, resistance, a ward, a vulnerability |

All three are Entities. All three can be repinned, dispelled, or destroyed. None of them is a special case in the engine — they differ only by Layer.

## Magnitude assembly — percentages, then absolutes

Two kinds of modifier act on magnitude:

| | Example | Type |
|---|---|---|
| **Percentage** | *+100% to temperature-positive vectors* | proportional |
| **Absolute** | *+2 to temperature-positive vectors* | flat |

```
R-200   ambient modifier tiers  modifiers that modify modifiers, highest tier down
R-300   percentage modifiers    SUM them — the carried snapshot total plus ambient
R-350   Enhancement Capacity    CLAMP the summed percentage; record the overflow
R-400   apply, once  ─────────► the only multiplication; truncate toward zero
R-500   absolute modifiers      add them
R-600   clamp                   floors, ceilings, immunity
```

*(Slot numbers are the R-region of the lattice under **"At the Moment"**, below. There is one numbering scheme, not two. The base magnitude is carried on the vector from C-600 and is the input to R-300, not a slot of its own.)*

**Applied per vector, independently.** A modifier conditioned on fire must scale the fire vector and leave the cold vector in the same Packet untouched. This is why assembly precedes combination.

**Percentages sum; they never compound.** +100% and +100% is +200% — the result is **three times** the base, not four. This is not an accident and it has a content consequence: *never write "double the damage."* Write *+100%*. The vocabulary must match the arithmetic or every stacking case will surprise someone.

**Percentages resolve before absolutes.** A flat bonus is therefore never inflated, so its worth stays constant. Reversing the order changes every answer in the game, so the order is fixed permanently.

**A modifier that creates a vector does not also modify it.** No double-dipping. One pass per modifier per vector.

**Immunity is a clamp, not a −100%.** Percentages sum, so a −100% "immunity" would be cancelled by any +50% modifier an enemy applies. Immunity clamps the magnitude to zero at R-600, where nothing can add it back. This is the reason the clamp layer is load-bearing rather than decorative.

**Rounding mode: truncate toward zero**, applied once at R-400. Toward zero rather than down, so signed values (cold is negative temperature) behave symmetrically. A knowable consequence: a target with a percentage reduction fares very slightly differently against many small hits than against one large one. That is deliberate and stable, not drift.

### Why percentages must sum rather than compound

Compounding is commutative in real arithmetic and **stops being commutative the moment you round between steps.** Base 5, with +30% and +40%:

```
5 × 1.3 = 6.5 → 6   then 6 × 1.4 = 8.4 → 8
5 × 1.4 = 7.0 → 7   then 7 × 1.3 = 9.1 → 9
```

Eight or nine, depending on which of two unrelated Components happened to go first. That is precisely the failure the whole determinism discipline exists to prevent. *(Both lines truncate toward zero, as the rule requires — the order-dependence is not an artefact of the rounding mode, it survives every mode.)*

Summing gives `5 × 1.70 = 8.5 → 8`, in every order, forever.

The alternative — compound without rounding between steps, round once at the end — requires multiplying two fixed-point numbers together repeatedly, which is the one operation this system is built to avoid.

## Capacity — the ceiling on how much can be poured into a thing

**Every vector has a limit on how much enhancement it can carry.** A flamethrower can be enhanced by a pyromancer, but only so far — past that, it is more than the gun can hold. A better gun holds more. Upcasting raises the ceiling. So does spending a Resource.

This is a **Capacity** in the exact sense of the five Noun kinds: a graded, kind-agnostic disposition. *Capacity to be enhanced.* It applies to a gun, a spell, a ritual, a bribe, and a fortification without absurdity, because it never claimed to describe what any of them are.

**Enhancement Capacity** bounds the total a vector's magnitude may reach, at R-350, between summing and applying. **Stated as a ceiling on the total, where 100% means no enhancement at all** — a lock at 100% cannot be helped by anything; a good flamethrower at 250% can be brought to two and a half times its base.

**Attempt Capacity** bounds how much total *attention* a task will absorb, as a percentage. A lock at **200%** absorbs the equivalent of two people's full attention: three people at 50%, 60% and 40% fit inside it; a fourth at 60% would push past 200% and be clipped. It is measured in **attention, not competence** — a master and a fumbler each consume the same budget at 100%, because space at the keyhole is space at the keyhole.

**Participant Capacity** bounds how many distinct sources may contribute at all. A lock at *three* takes three people, however many are standing in the corridor.

**Both exist, both are optional, and both are needed**, because neither catches what the other does:

```
Attempt Capacity 200%, ten people each spending 1 of 5 points   →  20% each, 200% total.  FITS.
```

A share budget alone admits the crowd. **Participant Capacity is what stops ten people each dabbling one point and never failing at anything.** And Attempt Capacity is what stops three specialists each going all-in. Worked, against the same lock:

```
Participant Capacity 3 · Attempt Capacity 200%

  three specialists, all-in    3 admitted · 100% each · 200% used  →  PRECISION 18
  ten dabblers                 3 admitted ·  20% each ·  60% used  →  PRECISION  3
```

Depth beats a crowd at a task, which is right, and the crowd is not merely diluted — it is turned away at the door.

**Three ceilings, three different things bounded.** They are easy to blur and they are not the same:

| | Bounds | Answers |
|---|---|---|
| **Enhancement Capacity** | amplification of one vector's magnitude | *how far can this be buffed?* |
| **Attempt Capacity** | accumulated attention from all comers | *how much total effort will this absorb?* |
| **Participant Capacity** | the number of distinct contributors | *how many can get their hands on it?* |

**Capacity bounds enhancement only, never reduction.** There is no ceiling on how much something can be weakened or resisted — a Guard reaching 100% is immunity, a legitimate thing to be rather than an overflow to clip. The concept exists to stop *runaway amplification*, which is the only direction that runs away.

**Enhancement Capacity clamps percentages. It does not clamp absolutes, and this is deliberate.** A flat `+2` is worth exactly 2 no matter how many amplifiers are present, so absolutes cannot run away by stacking the way percentages can — they grow linearly in the number of contributors, and **the number of contributors is already bounded by Participation Capacity.** Percentages get the ceiling because percentages are the direction that compounds; absolutes get the participant limit, which is the bound that fits them. Two different problems, two different walls, neither redundant.

The consequence worth stating plainly: *a lock at Enhancement Capacity 100% cannot be **amplified**, but it can still be helped by a flat bonus.* That is the intended reading, not a leak.

**Enhancement Capacity belongs to the task or the target, never to the source.** The lock says how much help it absorbs; the gun says how much amplification it holds. If it belonged to the source it would be shoppable — the party would route every vector through whoever holds the highest ceiling, and Capacity would become a party resource instead of a property of a thing in the world.

**A Baseline is a percentage, so the percentage ceiling covers it.** Summed Baseline shares are clamped by the same Enhancement Capacity, at the same place, for the same reason.

**The Capacity that clamps a vector is read from the TARGET, at R-100, in the gather.** It is not captured from the source at creation. That was the earlier rule and it was retired in Phase 0 — a source-owned ceiling is shoppable, and the party would route every vector through whoever held the highest.

Acyclicity is preserved a different way: the Capacity is read **once, at the gather, before any modifier at R-200 or later**, so nothing that spends a Capacity can also raise it mid-resolution.

### Why this matters more than it looks

It moves the stacking problem out of the arithmetic and into the fiction, which is the right place for it.

Once a ceiling exists, **the choice between summing and compounding percentages stops mattering for balance.** Three pyromancers on a cheap gun hit the cap either way. So summing — which is what determinism requires — costs nothing, and the interesting decision becomes *how much can this thing hold*, which is a design lever rather than an arithmetic accident.

It is also a whole progression axis. Better gear, upcasting, spending Resources, ritual preparation — all of them raise a ceiling rather than adding another number to a stack.

### Overflow

**The Substrate clips the excess and records it. It does not decide what the excess means.**

The overflow amount goes into the Resolution Record, where a Listener can see it. A Component then decides whether the gun overheats, the barrel cracks, the ritual backfires, or nothing happens at all. Backfire is content; clipping is engine.

**Asymmetric on purpose.** Amplification compounds toward absurdity; reduction converges on zero. Only one of those needs a wall.

## Modifier tiers

A modifier may target another modifier — *"enhancement spells you cast are 50% stronger."* Each modifier carries a **tier**, a small integer. Tiers resolve from highest down; within a tier everything sums.

**There is no maximum tier, and none is needed.** The set of modifiers present at a Moment is finite, so sorting by tier and working down always terminates. What is needed is not a ceiling but an acyclicity rule:

> **A modifier may only affect modifiers at a strictly lower tier.**

Checkable on a single modifier at authoring time, needs no global bound, and leaves no arbitrary number to regret later.
## What is a percentage and what is a whole number

| | Type | Modified by |
|---|---|---|
| **Direction** (a Channel's Dimension values) | percentages, summing in absolute value to 1 | nothing, ever |
| **Attempt direction** (from Allocation Points) | percentages, summing in absolute value to 1 **before Shaping**; a Baseline may push the sum above 1 | Shaping, at allocation time |
| **Magnitude** | whole number | percentage then absolute modifiers |
| **Percentage modifier** | percentage | sums with other percentages |
| **Absolute modifier** | whole number | adds after percentages |
| **Guard** | proportional (a percentage) or flat (a whole number), in resolved units | its own modifiers |
| **Resolved value** | fixed-point | produced at R-700, scaled at R-750, combined within a source at R-800, met by flat Guards at R-850, combined across sources at R-1000, met by proportional Guards at R-1050 |
| **Scale** | log-integer, kept separate | — |

## Packet
A set of vectors travelling together, produced by one attempt and resolved as a unit.

**Vectors in a Packet stay distinct.** A flaming sword blow is recorded as an `impact` vector *and* a `fire` vector, not as one merged direction. The resolved numbers come out identical either way, but keeping them separate preserves *which Channel this came from*, so any rule that cares about fire by name still can.

## Guard
A protection belonging to a target, acting on the **combined** per-Dimension total.

> **Damage cancels out before it reaches the target. That is the rule.**
> Everything incoming meets everything else first. Only what is left over is checked against the target's Guards.

**A Guard's value is how much it removes. Positive removes.** That is the whole convention, and it is worth stating flatly because the opposite reading is easy to fall into.

| Form | Example | Value | Acts |
|---|---|---|---|
| **Proportional** | *made of rock: integrity 50%* | a percentage | R-1050, summed, applied once to the combined total |
| **Flat, universal** | *plate armour: 3* | a whole number, in resolved units | R-850, **once per contributing source**, subtracted from that source's packet total, then redistributed |
| **Flat, Dimension-named** | *plate armour: integrity 3* | a whole number, in resolved units | R-850, once per source, from that Dimension only |

Proportional Guards **sum**, and may legitimately reach 100% — that is what immunity is. Clamped at 100%, because removing more than everything would be healing, and healing is a **Landing** rule, not a Guard overflow.

**The two forms act at different points, and the difference is the point.** A **flat** Guard is armour: it meets each blow, so it acts **once per contributing source**, at R-850, before anything cancels. A **proportional** Guard is what you are made of: it acts **once on the combined total**, at R-1050, after everything has cancelled. Five attackers each pay the armour; being half made of rock halves whatever is left at the end.

### Restoration is a vector too — it just resolves at a later layer

**Healing is an ordinary vector with a negative magnitude.** Nothing about it is special-cased: it has a direction, it has a magnitude, it is placed and pinned like anything else, and it runs the same assembly.

**What differs is where it resolves. A restorative vector is pinned to R-1250**, after harm has fully landed, rather than combining with harm at R-1000.

Everything people expect of healing then falls out of the layer choice, with no exception written anywhere:

- **No Guard touches it** — not because Guards are told to skip it, but because R-850 and R-1050 are already behind it by the time it resolves. Armour reducing a heal would be absurd, and the lattice makes it impossible rather than forbidden.
- **It never cancels incoming harm** — it is not present at R-1000, so there is nothing to cancel against. A heal is not a shield; stopping a blow before it lands is what Guards and standing vectors are for, and the layers keep the two jobs apart on their own.
- **Timing cannot be gamed.** Harm lands, then restoration resolves, so a heal at the same Moment and a heal a Moment later come out the same:

```
knight in plate 3, poison −6, cleric restores 6
  poison, guarded per source, lands at R-1200   −3
  restoration resolves at R-1250                +6
  same Moment → net +3        delayed one Moment → net +3
```

Had restoration combined at R-1000 like harm, those two answers would have differed by exactly the Guard's value, so delaying a heal would have been free profit.

**This is a layer decision, not an exception to the vector model.** That is the point of having a lattice: *when* a thing resolves is the lever, and it is enough to express something that would otherwise need a special case.

**Which Dimension restoration uses is an L22 question**, not a Substrate one — its own Dimension, or the negative magnitude of an existing one. Either works. What the Substrate fixes is only the layer.

A Guard is stated in **resolved units**, never in direction units, and is never multiplied by a direction.

### A universal flat Guard acts on the total, not per Dimension

This is the one place the earlier rule was wrong, and it mattered.

**Subtracting a flat Guard from every Dimension separately made mixed directions strictly worse than pure ones.** Against armour 3, at magnitude 10: pure fire landed 7, a 0.3/0.7 direction landed 4, an even three-way landed 1. Same attack strength, a 7× spread. Nobody would ever have placed a Channel anywhere but on an axis, which would have deleted the reason Dimension Spaces exist.

**The rule now:**

1. Take the **packet total** — the sum of the absolute values across every Dimension.
2. Subtract the Guard from that total. Floor at zero.
3. **Redistribute what remains** across the Dimensions in proportion to their pre-Guard absolute values, using the same integer apportionment as Allocation Points (Part 2C): floor each share, then hand the remainder out largest-first, ties by Dimension index.
4. **Signs are preserved, and a Guard reduces toward zero and never past it.** Armour can stop harm; it can never turn harm into its opposite.

```
flat Guard 3, magnitude 10

  pure          [10]           → [10]              lands 7
  0.3 / 0.7     [3, 7]         → [2, 5]            lands 7
  even 3-way    [4, 3, 3]      → [3, 2, 2]         lands 7
  even 4-way    [3, 3, 2, 2]   → [2, 2, 2, 1]      lands 7
  with a negative [6, −4]      → [4, −3]           lands 7
```

**Every direction lands the same total.** The dominance is gone, and it is gone by arithmetic rather than by content discipline.

**A Dimension-named flat Guard still acts on that Dimension alone**, which is correct — that is what specific resistance means, and a mixed attack *should* pay `integrity 3` only on its integrity part. The two idioms coexist: **universal flat Guards are generic toughness; named Guards are specific resistance.**

**Named acts before universal within R-850, and the order is declared because they do not commute.** Against `[temperature +2, integrity −8]` with a named integrity Guard 6 and a universal Guard 6, named-first lands 0 and universal-first lands 1; across a small exhaustive sweep roughly a third of combinations disagree. Specific resistance meeting the thing it names first is the only reading in which naming a Dimension means anything.

**A universal flat Guard may not be negative.** A vulnerability is a **proportional** Guard at R-1050, or a Dimension-named flat Guard. A negative universal Guard would add magnitude to a packet, which breaks *reduces toward zero and never past it*, and against a fully cancelled packet it has nothing to redistribute across, so the magnitude would silently vanish.

Step 3 is not a rounding site. Nothing is lost — the remainder is handed out, not dropped.

**A Guard has a polarity and a value, and they are separate things.**

- **Polarity** — which side of the Dimension it covers. An **unpolarised** Guard on `temperature` removes heat and cold alike. A **polarised** Guard covers one side only: *temperature-positive 100%* is a fire elemental, which shrugs off heat and still feels cold.
- **Value** — positive removes; **negative adds**. A Guard of `temperature −50%` is a **vulnerability**, and the target takes 150% of the net heat. Same mechanism, other sign of the value.

### Where a thing lives decides when it acts

There is no judgement call and no fork:

- Attached to the **source or the vector** → a **Modifier**, acting per vector at R-300, before anything combines.
- Attached to the **target** → a **Guard**. A flat one meets each contributing source at R-850; a proportional one meets the combined total at R-1050.

A negative modifier on a caster weakens their fire before it meets anything else. A vulnerability on a victim amplifies whatever is left after everything has cancelled. Content authors never choose a layer; the side chooses it for them.

### Worked: the fire elemental

Two entirely ordinary things — a standing fire vector as an aura, and a signed Guard of 100% against temperature-positive. No new machinery.

```
a cold bolt arrives, magnitude 8              temperature −8
its own fire aura is present, magnitude 5     temperature +5
                                              ───────────
R-850 flat guards, per source                 none present
R-1000 combine across sources                 temperature −3
R-1050 guard: 100% temperature-POSITIVE           does not apply — the net is cold
                                              ───────────
                                              takes 3 cold
```

The aura cancelled 5 of the incoming cold before the elemental was ever checked. Had the incoming been fire, the net would be temperature +13 and the signed Guard would take all of it, including the elemental's own aura. It is never hurt by its own fire, and never protected from cold by it — only shielded to the extent the fire cancels the cold first.

**LIST: Guard presets — PENDING.**

## Transient / Persistent
Every Channel is one or the other.

- **Transient** — exists for an instant. Fire, force, a shove.
- **Persistent** — part of what a thing *is*. Health, standing, structural integrity.

## When work happens: creation, or the Moment

**You can pre-sum. You cannot pre-apply.**

That one sentence decides which work moves to the moment a vector is created and which has to wait until it lands. Summation is associative, so a partial sum can be finished later without changing the answer. Application is not — apply half the percentages early and the rest late and you have silently reintroduced compounding, plus a rounding step in the middle.

So a placed vector is **a direction, four numbers and a pin**, and it never looks at its source again.

### At creation

```
C-100  read the source's current prepared state
C-200  resolve snapshot modifier tiers
C-300  SUM snapshot percentages                  → one number
C-400  SUM snapshot absolutes                    → one number
C-500  (retired — Capacity is read from the target at R-100)
C-600  fix direction and base magnitude
```

Three consequences, all good:

1. **A pending vector cannot change retroactively.** Drop the sword after swinging and the blow is unaffected, because the sword's contribution is already a number.
2. **The Fold never reconstructs the past.** Replay reads a direction, four numbers and a pin instead of re-deriving what gear the source held three rounds ago.
3. **A player can be shown a preview when they declare** — *"your fireball: 12, before whatever it meets on arrival."* A preview is rendered, never stored, and never fed back into the Fold; it is the client running the pipeline against what is known so far. That matters most in asynchronous play, where you declare on Tuesday and it lands on Thursday.

Provenance is not lost: the vector carries the sums, and the placement Record carries the itemised breakdown for the explanation channel. Numbers for the Fold, reasons for the human.

### At the Moment

```
R-100   GATHER              every vector, modifier and Guard scoped to this target
R-200   ambient tiers       resolve, highest down
R-300   percentages         carried snapshot total + ambient    SUM
R-350   Enhancement cap     CLAMP; record the overflow
R-400   apply               the one multiplication; truncate toward zero
R-500   absolutes           carried total + ambient, add
R-600   vector clamp        floors, ceilings, immunity
R-700   resolve             direction × magnitude → values per Dimension
R-750   scale               convert to the TARGET's Scale; truncate toward zero
R-780   standing cap        RESERVED — ceiling on standing self-scoped cancellation.
                            Unbounded in v1
R-800   combine per source  sum per Dimension, within each contributing source
R-850   Guard flat          ONCE PER SOURCE, on the sides it covers; redistribute
R-1000  combine all         sum across sources — THIS is where cancellation happens
R-1050  Guard proportional  SUM, apply once to the total, clamp 100%; truncate
R-1100  target clamp        the target's own floors and ceilings on the combined total
R-1200  land                transient → persistent          (Landing Socket)
R-1250  restore             restorative vectors — same machinery, a later layer
R-1300  record              write the Resolution Record
R-1400  listeners           evaluate against the new state
```

**R-100 runs once for the target** — it is the gather. **R-200 through R-750 run per vector, independently.** **R-780 through R-850 run once per contributing source.** **R-1000 onward run once for the target.**

**Thirty slots: E×5, C×6, R×19.**

**Two things changed here in Phase 0's re-attack, and they are the whole reason for the per-source region.**

**Flat Guards act once per source, not once per Moment.** Everything aimed at a creature lands at the start of its turn, so a Guard applied to the whole packet was paid once no matter how many people were swinging:

```
knight in plate, universal flat 3
  1 attacker  × 10    once per Moment  7 lands      once per source   7 lands
  5 attackers × 10                    47 lands                       35 lands
  8 attackers × 10                    77 lands                       56 lands
```

Armour became irrelevant exactly as the fight got harder, and no player chose that. Each blow meets the armour, which is also what armour does.

**Cancellation moved to R-1000, after flat Guards and before proportional ones.** That keeps the fire elemental exactly as it was — a cold bolt of 8 meeting its own aura of 5 still combines to 3 before the temperature-positive Guard is consulted — while letting armour act per blow.

### Entity preparation

Read whenever an Entity's state is needed — at C-100 for a source, at R-100 for a target.

```
E-100  Existence            is this Entity in play
E-200  Categories           which it holds → which Attributes exist
E-300  Base attributes
E-400  Attribute modifiers  proportional, then flat
E-500  Capacities
```

### Why each boundary exists

Every one is forced by a case that was actually worked, not chosen for tidiness.

| | |
|---|---|
| C-300 sums but never applies | applying early reintroduces compounding and a second rounding step |
| E-500 before R-100 | a Capacity must be settled before the gather reads it |
| R-300 before R-800 | a fire-conditioned modifier must scale the fire vector and leave the cold vector beside it alone — this is what makes cooperative buffing work |
| R-400 before R-500 | a flat bonus is never inflated, so its worth stays constant |
| R-600 after R-500 | immunity clamps last within the vector, so nothing adds back past it |
| R-1000 before R-1050 | **damage cancels before what you are made of is consulted** |
| R-850 before R-1000 | armour meets each blow, before anything cancels — five attackers each pay it |
| R-1250 after R-1200 | a restorative vector resolves after harm has landed, so no Guard has a chance at it and timing a heal cannot game it |
| R-1300 before R-1400 | a Listener reads the Resolution Record, so the Record must exist first |

Within R-300, R-800 and R-1000, order is irrelevant — addition is commutative. **Within R-850 it is not**: a Dimension-named flat Guard acts before a universal one. **Only the slots are ordered, and they are ordered permanently.**

## The Resolution Record

Written per target, per Moment. **It stores the inputs and a hash; every layer is derived.**

Stored — inputs only:

- the vectors, modifiers and Guards present, by ID
- the Moment, the Edition and the pinned Component versions
- the PRNG draws consumed, by `(record_id, entity_id, purpose)`
- a **state hash** of the result

Derived, never stored — including the ones it is tempting to store: the assembled magnitude of each vector, the resolved values per Dimension before and after Guards, what was converted to persistent state, and the **overflow** (enhancement clipped by Capacity). Every one of these is a slot value, and slot values are recomputed.

Derived on demand, never stored: **the intermediate value at every slot the resolution passed through.** The Fold is deterministic and the Component version is pinned per Record, so recomputing produces the same picture forever — and the hash makes the recomputation self-checking. Storing what can always be recreated would multiply the size of exactly the case that hurts: a long fight with many participants.

**The derived expansion is not a debugging luxury.** The interface shows a player their attack assembling on their own turn and completing on the target's, one slot at a time, and the explanation channel answers *"why was it 17?"* from the same computation. One requirement serves the animation, the tooltip and the bug report.

One object, three needs, which is why it is Substrate rather than a log line:

1. **Reflection and retribution.** *Half the damage bounces back* is a Listener reading this Record and placing a new vector. That is a Component, but the Substrate has to make it possible — and it does, without breaking the rule that Listeners watch state rather than events, because the Record **is** state.
2. **Backfire.** A Listener reads the overflow and decides the gun overheats.
3. **Reading the past.** Every question of the form *why was it 17* is answered from here, and nowhere else.

**Reflected and triggered vectors pin to a later Moment, never the current one.** That is what stops A reflecting to B reflecting back to A inside one resolution — bounded by turn structure rather than an engine limit, the same trick as requiring a `repin` to name a cost.

### Worked: two pyromancers

Pyro-1 throws a fireball at the Bruteling on their own turn. Base magnitude 8, Channel `fire`, pinned to the Bruteling's turn start. Pyro-1 carries a Flametongue: *+50% to temperature-positive*, **snapshot**.

Pyro-2, on their turn, casts *Amplify Flame* on the Bruteling: *+100% to temperature-positive*, **ambient**, window one round.

At the start of the Bruteling's turn:

```
percentages   +50% (snapshot)  +100% (ambient)   →  SUM +150%
magnitude     8 × 2.5                            →  20
direction     fire = temperature 1.0                 →  temperature +20
guard         temperature 3                          →  temperature  17
convert                                          →  17
```

Without Pyro-2: `8 × 1.5 = 12`, less 3, **9 damage**. The amplifier nearly doubled the outcome, and it did so *after* the fireball was already in flight.

Add a third pyromancer with another *+100%*: the sum is +250%, so `8 × 3.5 = 28` — against `8 × 1.5 × 2 × 2 = 48` if percentages compounded.

The cleanest way to see it: **two bare +100% modifiers give +200%, which is three times the base, not four.** Percentages add. Which is why content must write *+100%* and never *double* — the word implies an arithmetic the system does not perform.

### Why it works arithmetically

One multiplication per vector, then addition and subtraction on a fixed list of Dimensions. No angles, no square roots, no compounding, one rounding point per vector. And no consistency check between Channels is needed — **any set of positions summing to 1 is valid**, so a Component can never declare something that contradicts what already exists.

### Where rounding happens

**Once per vector, at R-400**, where the summed percentage is applied and magnitude becomes a whole number, truncated toward zero. Everything after is exact for the vector's own assembly: fixed-point direction × integer magnitude loses nothing, and R-500 onward are addition and subtraction.

**There are exactly three rounding sites, and no more may ever be added without an Edition.**

| Site | What rounds | Mode | Scope |
|---|---|---|---|
| **R-400** | the summed percentage applied to magnitude | truncate toward zero | per vector |
| **R-750** | Scale conversion to the target's Scale | truncate toward zero | per vector |
| **R-1050** | a proportional Guard applied to a resolved total | truncate toward zero | per target |

**R-1050 was previously claimed not to exist.** It does: a proportional Guard is a fixed-point percentage applied to an already-resolved fixed-point value. The old claim that *"two fixed-point numbers are never multiplied together"* was false, and is retired. What is true is narrower and still worth saying: **inside one vector's own assembly there is one multiplication and one rounding.**

**R-850 is not a rounding site.** The flat Guard subtracts a whole number and redistributes a whole number; see *Guard* in this Part.

**CI must fail on a fourth site.** A property test walks the pipeline and asserts exactly three truncations. If you can add one silently, the gate is missing.

**Every truncation is visible.** A rounding step is its own line in the resolution expansion, flagged, showing the value before and after and how much was lost. Rounding is where a system quietly stops making sense to a player, so it is never allowed to happen off-screen. See L30.

Persistent state is stored in fixed-point, so **Landing** (R-1200) needs no second rounding. Display rounds; the Fold never does.

## Alignment
How much two Channels point the same way, computed from their positions. **Always derived, never declared.**

Nothing in the resolution pipeline consumes it — combination is per-Dimension addition and needs no notion of alignment. It exists for **presentation and authoring**: a Lens showing *"your fire is working against your ally's frost,"* and a tool warning a content author that a new Channel sits almost on top of an existing one.

---

# Part 2B — Timing: when things land

**PROVISIONAL — Aug 2026.** The shape below is settled; the marked questions are not.

## The one resolution rule

> **At each Moment, for each Entity, gather every vector present — pending arrivals and standing vectors whose Scope covers it — combine them by the Part 2A rules, and resolve once.**

Everything else in this Part is a consequence of that sentence.

## Moment
A named point in the timeline that a vector can be pinned to. *Start of an Entity's turn. End of an Entity's turn. End of the current round. Now.*

A Moment is a **reference, not a number.** A vector pinned to *"the start of Kira's turn"* stays pinned to that description, not to a tick computed when the vector was placed — because a reaction may re-pin it, and turn order may change before it arrives.

The Substrate guarantees Moments are **totally ordered** and stamps each with a tick **when it actually occurs**, which is what makes replay exact.

**The Substrate knows what a turn is.** Round, turn, and **turn ownership** — *mine* versus *not mine* — are Substrate concepts, along with the named Moment kinds content pins to. Without ownership a reaction is inexpressible portably, and a reaction is not a genre feature. **LIST: Moment kinds — L32.**

*How* turn order is produced — an initiative roll, a fixed order, side-based alternation — is base Ruleset, not Substrate. Coarser clocks (downtime weeks, seasons, campaign turns) are Components, added alongside and never replacing.

## Loose time and Ordered time

Two modes, and the difference is only how fine-grained the Moments are.

- **Loose time** — Moments exist but nobody has a turn. The only anchor available is *next Moment*. Things that need no turn-anchored Moment simply happen.
- **Ordered time** — a per-Entity turn sequence exists, so *"the start of Kira's turn"* has a referent.

**Entering Ordered time — base Ruleset decides.** This is deliberately *not* a Substrate rule. Three candidate rules were tried and each failed on a real case: keying it to ally/enemy labels is undefined for strangers under the open-world rule; keying it to "a Moment that doesn't exist yet" catches everything, since every future Moment is yet to exist; keying it to "anchored to another Entity" wrongly drags healing an ally into combat.

The pattern in those failures is that this is a **game-design** rule, not an engine rule. So the Substrate defines what Ordered time *is*, and leaves *entry to it* to the base Ruleset, where it stays revisable forever.

**Ordered time can also be started manually at any time**, by anyone at the table. That path always exists.

**The Ruleset's default policy — PENDING.** The leading candidate is *a vector placed on an unwilling target*, where willingness is a property of the placement (declared by content, refusable by the target's controller) and never a stored relationship label. It handles every case tried so far: self-targeting and healing an ally are consensual and start nothing; a blow at a guard is not. Contested cases with no unwilling creature — two allies racing to cut the same rope — fall to manual initiation.

**Leaving Ordered time.** Ordered time ends when **no vector remains anchored to another Entity's Moment** and no participant places a new one. Passing your turn places nothing; it does not end Ordered time by itself.

A five-round storm holds the table in Ordered time **only while someone is in it.** With a creature inside, the storm's arrivals anchor to that creature's turns — a non-source anchor, so Ordered time continues. With the area empty, the storm anchors to nobody and the table can leave, re-entering if someone walks back in. That is not a separate rule; it falls out of the anchor test.

A **reactive** standing vector — a ward that waits to be hit — is anchored to nothing and therefore never holds Ordered time open. Only **scheduled** vectors with a live non-source anchor do.

## A vector is not placed and applied — it is placed and *pinned*
Issuing a Verb does not change anything. It puts a vector into the world with:

| | |
|---|---|
| **arrives_at** | the Moment it resolves — a reference, not a tick |
| **window** | how long it persists once arrived: one Moment, N rounds, or *while a condition holds* |
| **scope** | who or what it covers: one Entity, an area, a Relationship |

## The default anchor
**Anything targeting a creature lands at the start of that creature's turn**, unless something says otherwise.

Landing sooner costs more — extra action economy, a resource, a condition met. Landing later is what you get for spending less, or the price of something powerful. That trade is a Component's business; the Substrate only carries the resulting Moment.

## There is no difference between an attack and an aura
A sword blow is a vector with a window of one Moment and a scope of one creature. A five-round ice storm is a vector with a window of five rounds and a scope of an area. A permanent ward is a vector whose window is *while this State holds*. **One object, three windows.** No separate mechanism for damage, duration, or auras.

## Counteraction is arithmetic, not a rule
Two vectors present at the same Moment combine per Dimension. A cold Packet at temperature −6 and a fire Packet at temperature +4, arriving together, resolve as temperature −2. Nothing "dispelled" anything; the numbers simply added.

**Note the consequence:** if the fire is *stronger* than the cold, the ally takes fire damage from their own side's spell. That falls out of the arithmetic and is not a bug.

## Pending vectors are Entities
A pending vector persists, has identity, and other things need to refer to it — a reaction targets *that incoming blow*. By the Entity test in Part 2 — *if a Verb can point at it, it is an Entity* — it is one.

This is load-bearing: it means reactions, counters, deflections, and dispels are ordinary Verbs aimed at the vector rather than at a creature, and need no new machinery. It also means a Listener can watch *"a cold vector is inbound at me"* without violating the rule that Listeners watch state and not Verbs — **a vector in flight is state.**

## Repin
Changing a pending vector's Moment. A reaction that pushes an incoming blow from the start of your turn to the end of it is a `repin`.

**There is no cap on repins.** The bound is economic, not structural: **a repin must name a cost** — a Budget item, a resource, something finite. A repin that costs nothing could be issued forever, and since Ordered time cannot end while vectors are pinned, a free repin traps the table in combat permanently. Requiring a declared cost is CI-checkable and removes the failure mode without an arbitrary engine limit.

*Player-chosen* repins are bounded by that cost. **Automatic repins issued by a Listener are still subject to the cascade limit** — that path has no player spending anything.

Candidate Verb for L6: `repin`.

## Landing on the dead
**There is no special case for death.** A vector pinned to a target lands when its Moment arrives, whatever state the target is in by then. If someone kills you before the blow arrives, the blow arrives anyway and whatever the rules say about striking a corpse is what happens.

This works because death is a **State**, not an absence. The Entity still exists — consistent with the Ledger never deleting anything. Content declares the rest: a five-round storm's own text says who takes damage and when.

**`destroy` stays in the Verb set**, but it is rare and it means *removed from play entirely* — not killed. Killing is a State.

## The two axes of a standing vector

Independent, and all four combinations are real:

| | **Durable** — survives use unchanged | **Depleting** — drains as it absorbs |
|---|---|---|
| **Reactive** — waits to be hit | resistance / a Guard (Part 2A) | a shield with hit points |
| **Scheduled** — fires at Moments | an aura that burns every round | a fading effect that weakens each round |

*Reactive vs scheduled* is what determines whether a vector holds Ordered time open. *Durable vs depleting* is what determines whether it needs a pool. Names for the four to be settled later.

## Leaving and re-entering Ordered time

**Windows freeze; they do not convert.** A ward with three rounds left when Ordered time ends keeps a label saying *three rounds remaining*. It does not decay, and it does not translate into some coarser unit. If Ordered time resumes, it picks up exactly where it stopped.

Outside Ordered time, standing things simply record **when they were activated or became present**. Turning one off is the holder's choice, not the engine's.

**Pending arrivals cannot survive the transition**, and nothing special is needed to guarantee it: Ordered time cannot end while anything is still anchored to another Entity's Moment. A blow in flight blocks the exit until it lands. Only **reactive** standing things — a ward waiting to be hit — persist, and those are what freeze.

**A knowable consequence.** A party can raise wards, end the fight, and carry those wards indefinitely. That is a deliberate outcome of freezing rather than converting. Where content does not want it, the fix is content's: a window may declare a coarse expiry alongside its fine one — *three rounds, or until the end of the day* — and the engine needs no rule for it.

## Scenes, and the Moment they share

**The participant set is the scene.** Everyone inside the same Ordered time shares a timeline and sees each other immediately. Everyone outside it is isolated.

**A vector whose scope reaches outside its participant set is pinned to the next Moment shared by both.** That is an ordinary pin on an ordinary Moment — no separate synchronisation machinery. Two groups playing on different evenings each resolve their own scene, and anything that leaks between them lands where their timelines meet.

**Conflicts need no tiebreak.** Two scenes sending something at the same faction combine there, exactly as two fire vectors do. Where they genuinely cannot combine — both groups stealing the same unique object — **Participation Capacity** settles it.

There is no *"who went first,"* because nobody went first.

**Substrate guarantee:** any two participant sets must eventually share a Moment. Without it, two scenes could drift apart forever and a leaked consequence would never land.

**The cost, stated plainly.** Scenes that share no Moment until a coarse one are **simultaneous** until then. If one group kills the duke on Tuesday and another walks into his hall on Thursday, he is alive on Thursday and dies for everyone when their shared Moment arrives. Correct when the scenes really were simultaneous; wrong when the table meant them to be sequential. A table wanting sequence puts a shared Moment between them.

**PENDING** — the open timing questions:

- What happens to a vector whose target is **removed from play entirely** — not dead, but gone. Fizzle and record it, or resolve against nothing?
- Names for the four standing-vector kinds.

---

# Part 2C — Attempts: an attempt is a vector too

**PROVISIONAL — Aug 2026.** The shape is settled; the marked questions are not.

## The one rule

> **An attempt is a vector. Its direction is what you are trying to do. Its magnitude is how well it went — signed, so a failure is the same direction with a negative magnitude.**

Things in the world declare **Thresholds** on that vector. Whatever thresholds are crossed, happens.

**A consequence is graded by distance from the bar, never by an absolute value below zero.** You needed 5 and came in at 2, so you are 3 short; you needed 2 stealth and put nothing there, so you are 2 short and the guard notices by that much. This is the same reading as *how far under the target number did the roll land*, and it matters because the alternative made **zero a safe place to be** — an axis you ignored would have been protected from a bad failure while an axis you tried on and botched was not.

**An attempt with no points spent anywhere is not a legal attempt.** There is no direction, and the arithmetic has nothing to divide by.

That is the whole of resolution. It is the same machinery as harm, in a different Dimension Space.

## Direction comes from the declaration; magnitude comes from the resolution

Exactly as with a spell: the Channel is fixed by what you cast, and the magnitude comes from how it went.

## The attempt Space is two layers — Domains and Dimensions

**SETTLED Aug 2026 (L29).** The `attempt` Space has **fifteen Dimensions**, grouped into **seven Domains**.

| Domain | The outcome | The routes to it |
|---|---|---|
| **FORCE** | make something move, break, or hold | `power` · `momentum` |
| **PRECISION** | do something exactly right | `control` · `timing` |
| **MOVEMENT** | get there, get away, or not be where it lands | `agility` · `pace` |
| **AWARENESS** | know what is there | `senses` · `study` |
| **INFLUENCE** | change what a mind does | `appeal` · `pressure` · `bargain` |
| **GUILE** | not be found, or not be understood | `stealth` · `deceit` |
| **RESOLVE** | hold, resist, endure | `grit` · `focus` |

**A Domain is an outcome; its Dimensions are genuinely different routes to that outcome.** Two characters can clear the same FORCE bar, one through `power` and one through `momentum`, and neither has to argue about which applies. That is the athletics-versus-acrobatics problem solved structurally rather than by ruling.

### A Domain has no number

**Nothing stores a FORCE.** A Domain is a label on a set of Dimensions and nothing more. When a bar is set on a Domain it reads the sum of that Domain's Dimensions at that moment, and then the sum is gone.

Which settles the arithmetic without a decision: **the Domain is definitionally the sum of its parts**, so Dimensions resolve first and the Domain is read off them. One consequence falls out and is worth having — **concentrating a Domain's points on one Dimension is weakly better than splitting them inside it**, because truncation is per-Dimension. Hedging *within* a domain costs you a little; hedging *across* domains is the real decision.

### Who chooses what

**The Domain is not a choice.** It falls out of what is being attempted, and the GM names it. This is the whole answer to *how does a newcomer know what to roll* — the hard question is already answered by the fiction, and only the route is the player's.

- The GM names the **Domain**. The player must spend **at least one point** inside it.
- The GM may instead name a specific **Dimension**, which is harder — the player must spend at least one point *there*, and has to work out which route the situation actually wants.
- Everything else the player allocates is theirs, spent against bars they may not know exist.

That last line is the game. The GM knows the lock opens at PRECISION 10, that someone hears below GUILE 5, and that a needle waits below AWARENESS 5. The players know only that this is a PRECISION problem.

### Specialisations — the third layer

A **Specialisation** is a named narrowing of one Dimension that grants **Bonus Points** on it when its scope applies: `appeal (among dockworkers)`, `stealth (in cities)`, `control (with locks)`, `grit (against cold)`.

It is the Shaping machinery that already exists, so it needs no new mechanism and cannot inflate an attempt — Bonus Points add to the Dimension and to the total together.

**A Specialisation must be strictly narrower than its Dimension and may never substitute for one.** It must name a scope: a place, a people, a kind of thing, or a condition. The authoring tool enforces the shape; the breadth rule is the one thing a human has to judge.

## Allocation Points — how a player sets a direction

A character has a number of **Allocation Points** and places them across what they are attending to. **Direction is the proportion of the points actually spent.**

```
2 points on the lock, 1 on watching, 1 on keeping quiet   →   50% / 25% / 25%
1 point on the lock, nothing else                          →   100% / 0 / 0
```

### The resolved value is one integer operation — the percentages are never materialised

> **`value on axis i = ⌊ pointsᵢ × magnitude ÷ total points ⌋`**
>
> Whole numbers in, whole numbers out, truncating toward zero. **A share is never stored as a decimal and never multiplied by anything.**

This matters more than it looks, because the obvious alternative — work out the share, then multiply — gives different answers:

```
6 points as 3 / 2 / 1, magnitude 12

  share first    0.5, 0.3333, 0.1666  ×12  →   6, 3, 1     total 10, and 2 vanish
  integer first  ⌊3×12/6⌋ …            →   6, 4, 2     total 12, nothing lost
```

Against the standing lock — manipulation 5, needle 4, corridor 1 — those two readings tell **different stories**: share-first misses the needle at 3 against 4; integer-first spots it at exactly 4. Integer-first is the rule.

It also removes an entire class of problem. There is no fixed-point direction for an attempt to be wrong about, no apportionment method to choose, and therefore **no Alabama paradox** — no case where spending one more point makes an axis go *down*. An attempt's direction is stored as **whole point counts plus a total**, not as percentages. Percentages are a display convenience.

**Spreading still costs something, and the cost is the truncation.** The magnitude lost across `k` axes is always less than `k`, so it is negligible on a big roll and brutal on a small one — spread 8 points across 8 axes on a roll of 7 and every axis truncates to zero. That is the intended penalty for attending to too many things at once, and it scales itself: a competent character barely notices, a desperate one is punished for hedging.

Three properties worth noticing:

**The direction cannot be invalid, by construction.** A player never types a decimal, and the resolved values are computed from integers in one step; only a **Baseline** may push the summed shares above 1, and only at allocation time.

**Points buy precision, not power.** The magnitude is whatever it is; points only decide how it is carved up. One point all-in is 100%, the same as five points all-in. What more points buy is the ability to say 50/25/25 instead of only 50/50 or all-in. **More points is strictly more flexibility, never more force** — which means allocation can never inflate damage, and progression along this axis cannot break balance.

**Everything you did not allocate to resolves at zero.** That is the whole tension: you are spending attention against a situation you may not fully understand. Allocate to stealth when nobody is listening and it is simply wasted. **By default the GM knows what the bars are and you do not — Threshold visibility is a GM setting (Part 5), and hiding the bars is what creates the tension.** Which is what makes information worth having — knowing there is a needle in the lock changes how you spend.

**PENDING — how many points, and where they come from.** Five is a placeholder with nothing behind it. The natural home is a **Capacity** — *capacity to divide attention* — which would make it kind-agnostic and let a distracted character have fewer and a practised one more.

## Shaping — how gear changes the split

Gear can change the *shape* of an attempt, not just its size. **There are two forms, and both are stated in points**, because points are what a player actually has.

> **The order is fixed and permanent: Bonus Points → Baseline.**

They do not commute. Raw 1 / 2 / 1 at magnitude 12, with `+3 points on manipulation` and `manipulation counts as at least 3 points`:

```
Bonus Points first   4/2/1 of 7   →   6, 3, 1     the Baseline is already met, so it does nothing
Baseline first       3/2/1 of 4   → +3 → 6/2/1 of 7  →  10, 3, 1
```

Declared once, here, and never varied by content.

**~~Demand~~ is retired.** It was a third form that forced a minimum allocation and squeezed everything else into what remained. Nothing in the design ever asked for it, forcing a player to spend their own points somewhere is a strange thing to want, and it was the only form that had to be stated as a percentage — which reintroduced exactly the rounding problem integer allocation removed. A cost belongs in the **Budget**, or as a **Guard** or **State** on the character. It does not belong in Shaping.

### Bonus Points — redistributive
The item **adds points to one Dimension**, provided the character has committed at least one there themselves. The points go into the total as well, so everything else is diluted.

```
1 manipulation, 2 perception, 1 stealth      4 points     at magnitude 12  →   3, 6, 3
+3 manipulation from the tools               7 points     at magnitude 12  →   6, 3, 1
```

Your manipulation went up and your perception went down. **The attempt is reshaped, not enlarged** — which is what makes this form structurally safe. No number of Bonus Point items can inflate an attempt.

### Baseline — additive
The item guarantees a Dimension **counts as at least N points**, and **takes nothing from anywhere else** — the total is not raised, so your own points keep their full value.

```
1 manipulation, 2 perception, 1 stealth      4 points     at magnitude 12  →   3, 6, 3
manipulation counts as at least 3 points     3/2/1 of 4   at magnitude 12  →   9, 6, 3
```

The resolved values now sum to 18 against a magnitude of 12. **That is the one legitimate way an attempt exceeds its own magnitude**, and it is deliberate: **a Baseline is a real increase in total effect**, which is what makes it worth owning. Its value is greatest when you allocate *least* to that Dimension — the tools carry the lock while you watch the corridor.

**Baselines take the highest, never the sum.** Two sets of lockpicks do not stack; the better one applies. Since `max` is order-free, any number of Baselines on one Dimension is deterministic and safe.

**The ceiling is Enhancement Capacity — the same one, not a second.** Everything that enhances sums into one number and that number is clamped: a Capacity of 200% with a Baseline plus two helpers summing past it simply stops at 200%. **A Baseline contributes the increase it caused, not its face value** — lifting manipulation from 1 point to 3 contributes the 2 it added, because counting all 3 would charge you twice for the point you spent yourself. **The Capacity belongs to the task**, so it is the lock that says how much shaping it will tolerate.

### Against the same lock

Opens at `manipulation 5`, needle spotted at `perception 4`, guard hears you at `stealth 1 or below`. Magnitude 12, allocation 1 / 2 / 1.

| | manipulation | perception | stealth | |
|---|---|---|---|---|
| nothing | 3 ✗ | 6 ✓ | 3 ✓ | the lock holds |
| **Bonus Points +3** | 6 ✓ | 3 ✗ | 1 ✗ | in, but the needle gets you and the guard hears |
| **Baseline 3 points** | 9 ✓ | 6 ✓ | 3 ✓ | in, unstung, unheard |

**That is the difference between the two forms, in one table.** Bonus Points move your attention and something else pays for it. A Baseline adds effort that was never yours to spend — clearly the stronger item, which is correct, and why its ceiling is the thing that keeps it honest.

### Three properties worth holding

**Bonus Points cannot inflate anything.** Redistribution only, so that form is structurally safe and needs no balancing beyond taste.

**Baselines can.** They raise total effect, so they belong on the same shelf as Enhancement Capacity — a real power lever that needs a real ceiling.

**All of it must be visible.** A player who allocated 25/50/25 and watches the attempt resolve at 75/50/25 will assume the interface is broken unless the shaping appears as its own named step in the animation, attributed to the item that caused it.

**Shaping is snapshot only, never ambient** — carried by the actor, never present at the target. Direction is fixed when the vector is created, and keeping it fixed is what makes a placed vector a direction, four numbers and a pin. Something wanting to reshape another's attempt acts on magnitude instead, where ambient modifiers already live.

## Worked: one lock, three ways

The lock opens at `manipulation 5`. Its hidden needle is spotted at `perception 4` and fires otherwise. The corridor alerts the guard at `stealth 1` or below. **Magnitude 12 in every case** — the same roll.

**Four points: 2 on the lock, 1 watching, 1 quiet.** → 50 / 25 / 25

```
manipulation  0.50 × 12 = 6    needs 5    ✓  it opens
perception    0.25 × 12 = 3    needs 4    ✗  the needle gets you
stealth       0.25 × 12 = 3    over 1     ✓  nobody hears
```

**One point, all on the lock.** → 100 / 0 / 0

```
manipulation  1.00 × 12 = 12   needs 5    ✓  it opens easily
perception    0    × 12 = 0    needs 4    ✗  the needle gets you
stealth       0    × 12 = 0    under 1    ✗  the guard comes
```

**Four points: 1 on the lock, 2 watching, 1 quiet.** → 25 / 50 / 25

```
manipulation  0.25 × 12 = 3    needs 5    ✗  the lock holds
perception    0.50 × 12 = 6    needs 4    ✓  you spot the needle
stealth       0.25 × 12 = 3    over 1     ✓  nobody hears
```

Identical resolution three times. **In-but-stung**, **in-stung-and-caught**, and **stopped-but-safe** — decided entirely by how the effort was split. That is the game, and it needed no new machinery.

**And failure has magnitude too.** The first split — 50 / 25 / 25 — at magnitude **−4** gives `manipulation −2.0`, `perception −1.0`, `stealth −1.0`: locked, needled, and heard. If the corridor also declares *a clatter at stealth −0.5 or worse*, heard loudly.

## Where the outcome goes next

**The resolved magnitude becomes the base magnitude of the vectors the attempt places.** A sword swing that resolves at 12 places a bigger blow than one that resolves at 4. Content decides the relationship — *damage = attempt magnitude*, or *+2*, or whatever the weapon says.

**Thresholds place additional vectors.** *At manipulation ≥ 10 you also break the mechanism.* *At stealth ≤ −0.5 a noise vector goes out to everyone nearby.*

So the two mechanisms cover everything: the main consequence **scales** with magnitude, and extra consequences **fire** at bars.

## Objects take turns

**The default anchor — *things land at the start of the target's turn* — applies to any Entity, not only creatures.** A lock has a turn. So does a door, a trap, a ritual circle, a ship's hull.

That single generalisation is what makes cooperation work, with no "help action" and no separate mechanism:

```
turn 1   Ilya attempts the lock              → a vector pinned to the lock's turn
turn 2   Vex attempts the same lock          → a second vector, same pin
turn 3   THE LOCK'S TURN                     → both combine; Thresholds are checked
```

**Which creates a window.** Everyone who wants to contribute has until the lock's turn comes round. Miss it and your attempt lands on the *next* one, against a lock that may already be open — or already alarmed. Where an object sits in the turn order is therefore a real tactical fact, and how turn order is produced is base Ruleset's business to decide.

**Participant Capacity** bounds how many may pile in — a lock at *three* takes three people and no more. **Attempt Capacity** separately bounds how much total attention the lock will absorb, as a percentage, so three specialists going all-in are clipped at the ceiling while ten dabblers are turned away at the door by the participant count. Neither catches what the other does, which is why both exist.

An opposed action is the same machinery: two vectors pointing opposite ways in the same Space, combining at the target's turn. Two people wrestling cancel out. No separate opposed-roll rule.

## What this deletes

| Gone | Because |
|---|---|
| **Degree** as its own concept | it is the magnitude |
| **Cost** as a second axis | costs are consequences at other Thresholds, on other Dimensions |
| A **ladder of named outcome steps** | the Substrate declares none; the things being interacted with declare their own bars |
| The **scalarization rule** | there is no pair of scalars left to rank |
| **Difficulty** as its own machinery | it is a Threshold |

## What magnitude means

There is no cap on magnitude, in either direction, and there should not be. Rough shape across a campaign's arc: **under 10 early, under 50 in the middle, under 100 late.** That is design guidance for playtesting, not an engine rule.

**Do not confuse this with Scale.** Two different things:

| | |
|---|---|
| **Magnitude** | how much of this particular thing there is. A number, uncapped, negative where a failure warrants it |
| **Scale** | the log exponent on an Entity — a spaceship sits at a different Scale from a person, and it multiplies everything about that Entity. Addition is only legal within one Scale |

**The one safeguard worth having.** A trap declaring *"spotted at 4"* only means something if a magnitude of 4 feels the same in every Ruleset. That holds while one person designs and playtests all of them. To keep it holding later, **every Ruleset declares a magnitude reference** — *a competent attempt at an ordinary task produces about 5* — so content and CI have something to check against instead of a silent mismatch.

## An attempt runs the whole pipeline

Percentages, absolutes, Capacity, clamps — all of it, exactly as a damage vector does. A *+50% at picking locks* buff has to live somewhere, and that is where it lives.

Which also means the same layer-by-layer animation that shows a fireball assembling shows a lockpick assembling.

**PENDING** — what remains genuinely open:

- **How many Allocation Points, and where they come from.** (Also flagged above.)
- ~~The contents of the Capacity list (L29)~~ — **settled Aug 2026.** Seven Domains, fifteen Dimensions; see Part 2C.

### What a point may be placed on

**Correction, Aug 2026.** An earlier draft said a Dimension list must be closed and frozen, and that this forced points onto a small fixed set. That was too strong.

**Dimension lists are additive-only, like everything else in the system — not frozen.** A Component may add a Dimension to a Space, forever. Nothing that already exists breaks, because every Dimension is independent, all arithmetic is per-Dimension, and an unspecified Dimension defaults to zero. Fire stays temperature 100 when `sonic` is added in year five; it simply has no sonic component. No existing Campaign folds differently, so this is a Revision and not an Edition.

Even the balance worry is smaller than it first looked. **A Guard that covers all Dimensions covers new ones too** — armour that stops the first 3 of everything stops the first 3 of a Dimension invented years later, with no revision. Only a Guard that *names* specific Dimensions misses a new one, and that is correct behaviour rather than a defect: armour rated for heat should not stop a kind of harm it was never built for.

**In the attempt Dimension Space, the Dimensions *are* the Capacities.** That is the reconciliation: a point is placed on a Capacity, and that Capacity is a Dimension of the Space the attempt resolves in. One list, two jobs.

**So points still go on Capacities, but for softer reasons.** The number of Dimensions is the width of every vector in the system, and — more importantly — the attempt Dimensions *are the interface the player sees*. Splitting attention across eight Capacities is a legible choice. Splitting it across two hundred skills is a spreadsheet.

*Thieves' tools* is therefore not a Dimension. It is an **Entity** — a piece of gear in an inventory — that supplies a modifier to attempts with a manipulation component. A Component should add a Dimension only when it genuinely needs a **new axis of the world**, never one per skill.

## Gear contributes itself

**Equipment an Entity carries supplies its modifiers automatically**, to any attempt whose direction matches what the gear affects. Nobody hunts through an inventory for applicable bonuses and nobody remembers to apply them.

**And it shows its work.** Every contribution appears in the layer-by-layer animation, so a player watching their attempt assemble sees *thieves' tools, +2* arrive as its own step. Automatic is only acceptable because it is visible — silent bonuses are how a player stops trusting the numbers.

This is the clearest thing the software does that a paper table cannot: the arithmetic is complete and correct without anyone tracking it, and legible without anyone explaining it.

**LIST: the attempt Domains and Dimensions — L29, SETTLED and Component-extensible.** See Part 2C. Note these are *not* the same list as an Entity's Attributes: an Entity's Attributes are its base definition (L2, L3), and a Dimension value is derived from them by formula. A relationship never rolls an attempt; a building never attempts a grapple.

---

# Part 3 — What can change

## Verb
One of a small, closed set of Substrate operations. **A taxonomy of state change, not of activity.** Nothing in the set is about attacking, persuading, or crafting — those are fictional descriptions of attempts. The Substrate records only what changed.

A Verb is **data, not code.** Writing a Verb down does not make it happen; it is a proposed change that a Moment later applies.

**LIST: Verbs — PRELIMINARY, closed at the end.** See L6. The candidate set is deliberately not being finalised now. The system will be designed first, then the candidate list run against the finished system to see what it can't express.

## Verb shape
**Every Verb has the same shape.** Uniformity is the point: one parser, one validator, one log format, one replay path, forever.

| Field | What it is |
|---|---|
| **verb** | which operation, from the closed set |
| **source** | the Entity the change comes from |
| **target** | the primary Entity being changed — **every Verb has exactly one** |
| **secondary** | zero or more additional Entities the same invocation touches |
| **direction** | *what* is being changed — a set of per-Dimension percentages summing **in absolute value** to 1. For harm this is a declared **Channel**; for an attempt it is computed from **Allocation Points**, and a **Baseline** may push that sum above 1 by construction (Part 2C) |
| **magnitude** | *how much* — a whole number, signed, at a declared **Scale** |
| **class** | why this invocation exists (see below) |
| **layer** | where it sits in the ordering lattice |

Direction plus magnitude is exactly the vector idea from Part 2A, applied to every Verb rather than only to damage: *what is being pushed on*, and *how hard*.

The one-primary-target rule exists so that "who did this happen to" is never ambiguous in the Ledger, and so a Verb affecting three people is three Records, not one Record needing interpretation.

**Every Verb invocation is written to the Ledger in this shape.**

## Verb class
Why a Verb invocation exists. **Two, frozen.**

- **Activated** — something chose to do this.
- **Triggered** — a Listener fired and issued it.

*There used to be four.* **Replacement** *and* **Continuous** *both dissolved into a **vector with a window**: a vector already standing in the space* is *"instead of," and a vector whose window is "while this condition holds"* is *"continuous." Two mechanisms deleted, none added.*

## Verbs return nothing
A Verb produces no return value. Nothing reads "what a Verb gave back," because nothing is running when the Verb is written down.

Consequences that follow from a Verb are found by **Listeners**, not returned.

## Listener
A declared watch on a condition. When a Moment resolves and the condition becomes true, the Listener fires and produces further Verbs, pinned to a later Moment.

The canonical example: a Verb drives a Resource to zero. The Verb does not know or report this. A Listener watching "this Resource at zero" fires and issues its own Verbs — set state *unconscious*, add tag, whatever the Component declares.

Rules:

- A Listener is **data**, declared by a Component, never arbitrary code.
- A Listener watches **state**, not Verbs. It asks "is this now true," not "did that just happen." State is stable; the sequence of Verbs that produced it is not.
- Listener-produced Verbs carry class **Triggered** and are pinned to a **later** Moment, never resolved inside the current one.
- Cascades are bounded. A depth limit is set in the Substrate and exceeded cascades are recorded as such. — **PENDING: the limit, and what happens at it.**
- **LIST: Listener condition forms — PENDING.** What a Listener is allowed to watch: threshold crossings, State entry/exit, Tag presence, Relationship formation, clock arrival.

## ~~Barrier~~ — retired
**A Barrier is a Moment.** The point where accumulated Verbs are applied is the Moment they were pinned to, and nothing changes between Moments. One word, not two.

## Layer
An ordering slot in a fixed lattice, used to sequence Verbs. A Component declares which Layer its Verb belongs to; it may never invent one.

**LIST: Layers — PARTIAL.** See L7.

## The frame rule
**Everything not named in a Verb is unchanged, by definition.** State transition is a function on a set. The cost: anything you fail to list silently does not happen.

## Records without Verbs
**The Ledger does not require a Verb to record something.** A Record is any immutable entry. Verb invocations are one kind of Record; there are others that change no state at all — a GM assertion, a note, a Session boundary, a Proposal being raised, an out-of-band correction.

Consequence: *"what happened"* is a strictly larger set than *"what changed."* The Verb set only has to cover the second.

**LIST: Record types — PENDING.** See L13.

---

# Part 4 — Resolution

## Outcome
**Superseded — see Part 2C.** An attempt is a vector: direction is what you were trying to do, signed magnitude is how well it went. There is no separate Degree, no separate Cost, and no ladder of named steps.

*Degree* was the magnitude. *Cost* was consequences at other Thresholds on other Dimensions. *Scalarization* had nothing left to rank once the two axes collapsed into one vector.

## Threshold
**See Part 2C.** A bar declared by a thing in the world, on one Dimension of an outcome, on a **Domain** (the sum of its Dimensions), or on the total. Whatever bars are crossed, happens.

**A Threshold declares how it reads multiple contributors.** Three modes:

| Mode | Reads | Because |
|---|---|---|
| **sum** | every contributor's value added | effort accumulates — the lock, the barred door, the ritual |
| **highest** | the best single contributor | one person spotting the needle is enough for everyone |
| **each** | evaluated separately against every contributor | a fear aura, a spreading poison — declared once, landing person by person |

**There is deliberately no *lowest* mode.** A weakest-link rule would mean that bringing more people makes a party *less* stealthy, and — more importantly — it would teach players not to participate. Where individual jeopardy is wanted, that is **each**, usually alongside a Participant Capacity of one.

## ~~Difficulty~~ — retired
**It is a Threshold.** Set by the GM, or by an Adventure's script. Not separate machinery, and not a separate word.

## Challenge Profile
The measure of how demanding an Entity is. **Not a single number.** A set of named axes, each rated, plus a scalar summary computed from them by an explicit formula.

Displayed as a shape (a radar chart) for reading at a glance; **the shape is never the score** — a radar area is order-dependent and quadratic, so it can never be a number.

**LIST: Challenge Profile axes — PENDING.**

---

# Part 5 — Time, knowledge, decision

## ~~Period~~ — retired as a Substrate concept
**There is only the Moment.** A turn, a round, a downtime week and a season are all Moments at different grains. **Turn and round are Substrate. Everything coarser is a Component.** Nothing about cadence beyond the turn belongs in the Substrate.

The word remains available to a Component that wants it.

## Tick
The stamp on a Moment when it actually occurs. Logical only, never a clock. This is what makes replay exact while the pending side of the world stays symbolic.

## Session
A marker for a live gathering. Carries no rules; exists so Dispatch and Chronicle can point at one.

## Doubloon
**The atomic Economy Unit. Substrate, frozen, integer only.** Every cost in the game is a whole number of doubloons. Stored as a 64-bit integer — chosen deliberately too wide, because a currency's *range* is as permanent as its meaning and the field that could not widen is the recorded failure everywhere it has happened.

*(Working name. Renaming it later is free: it is one Substrate word with no arithmetic attached, and the naming pass comes after the lists.)*

**No denominations.** There is no `action`, no `quick`, no ladder of named multiples. That was proposed and cut: a size vocabulary sitting beside a timing vocabulary made authoring roundabout, because "reaction" is a *when* and "action" is a *how much*, and putting them in one list is the fusion that D&D's own designer disowned. A cost is a number; a timing is a name.

**Nothing ever divides.** Costs are authored in doubloons and folded in doubloons. A Lens may render a cost as a fraction of a turn for display, and a Lens is already exempt from the arithmetic rules — but no division happens anywhere in the Fold, so the denomination question introduces no rounding site.

## Cost
**The shape of what an ability takes, and it is not one field.**

| Field | Meaning | Status |
|---|---|---|
| `cost` | how many doubloons | required |
| `timing` | a named member of the closed timing set — *when you may pay* | required |
| `cap` | how often, per Moment or per round | optional, usually absent |

More fields are expected; these three are the floor.

**The point of the split is that cost and timing are orthogonal.** A 10-doubloon reaction and a 40-doubloon reaction are both reactions. Price says how much it takes out of you; timing says when you may pay it. Fusing them into one slot is what produced *bonus action*, and its designer's published verdict is that the fusion is why it failed.

**Frequency stays out of the timing name.** "Once per turn" is `cap`, not a timing — otherwise the cap gets smuggled into the name and the fused-slot problem returns by the back door.

**LIST: Timings — L31.**

## Budget
**How many doubloons an Entity gets, and when they refresh.** Base Ruleset, not Substrate — the allowance is a playtest number and freezing it forever would be a needless permanent bet. *That* an allowance exists and refreshes is Substrate, because `repin` bounding depends on it.

**Two findings from the field that constrain any allowance chosen:**

- **No single price may consume the whole budget.** Rolemaster Unified shipped four action points per round with a full attack costing four, and movement simply stopped happening until it was patched. CI-checkable: `max(price) / allowance` well below 1.
- **Keep the fastest-to-slowest allowance ratio under about 2:1.** Systems that vary the *budget* per character — HERO's SPD 1–12, Shadowrun's initiative passes — all generate the same recorded complaint, that the fastest character gets as much screen time as everyone else combined. Vary what a doubloon buys, not how many you get.

## ~~Perception~~ — retired as a Substrate concept
**Every piece of Campaign data a client is entitled to is available in that client's browser.** What a player *sees* is the **Lens**. What a character *knows* is a **Component** — optional, shipping in v1 because it is good, and not required for the game to run.

**Every layer of a Resolution Record is visible to everyone, by default.** The whole calculation, every intermediate, every contributing item. Secrets are a later deliberate decision, never the default posture — and where one is wanted, **Delivery** is the mechanism.

## Delivery
**One field on a Record: who receives it. Default, everyone.**

Not a game mechanic — infrastructure, and the one part of the old Perception idea that a Component cannot supply, because a Component cannot decide what the server sends. It exists for exactly two reasons:

1. **A GM's prep.** An adventure with a twist is unusable if the twist sits in every player's browser.
2. **Purchased content.** A Setting whose full text ships to every participant is readable by anyone who joins a Campaign using it.

Absent means everyone, so this can be added later without breaking history.

## The server folds; clients render
**Tier 1, and not deferrable.** The canonical state is folded on the server from the full Ledger. Clients render what they are sent and never authoritatively compute.

If clients folded from Records, any later restriction on which Records a client receives would make that client's Fold silently diverge. Folding on the server keeps one canonical state forever and turns *"hide this"* into *"send less."*

**Client-side hiding is theatre.** Anything a client must not have is never serialised into a byte sent to that client.

## Proposal
A pending action awaiting resolution. Carries a subject, an intent, and a Decider.

## Decider
Who resolves a Proposal.

- **Auto** — a Component decides.
- **Person** — a named human decides, **and always carries a Moment and a default.**

**A human decider with no fallback is never legal.** In a campaign that runs for months across time zones, one person going quiet behind an open-ended decision stops everything behind it — which is the single most common way an asynchronous game dies. A live table is served by a very long deadline, which costs nothing.

*A table vote is `Auto`* — a Component that reads submitted preferences. Adding a `Vote` kind would freeze one voting rule into the Substrate forever and buy nothing.

One field. It produces the rails dial, player puppeting, GM-less play, hybrid Adventures, asynchronous play, and graceful absence.

## Rails
The per-Component setting of who the Decider is. Set by the player, the GM, or the table, as each Component declares. Socket occupants are Components, so they have rails too — *does the app run initiative* is a base-Ruleset dial.

**Threshold visibility is a built-in setting**, not a per-Component rail: the GM decides whether the table plays with the bars shown or hidden. Same content, two very different games.

## Standing Order
A player's pre-declared response to a condition — *if I am attacked while away, brace: 3 points guard, 2 perception.*

**It is a Listener**, so it needs no new machinery. But the authoring line holds: **the Component publishes the Listener template; the player fills in the parameters.** *Defensive stance* is the Component's. *3 and 2* is the player's.

A default action must include a **default allocation**, not just a default verb — direction is half of every attempt.

This is what makes absence survivable. A player away for two weeks leaves standing orders instead of a hole.

---

# Part 6 — Presentation

## Lens
A read-only projection of Substrate state into what one participant sees, plus a dice procedure for how they experience resolution.

- Chosen per character, changeable at any time, in either direction, with no restriction.
- **Never changes what a character can do.**
- All writes happen at the Substrate; Lenses only render.
- **Not part of the Fold** — so Lens formulas are exempt from additive-only and can be rewritten retroactively without breaking history.

## Calibration
**A Lens is a view of the data. Most Lenses need no calibration at all** — one that shows raw numbers, or a filtered subset, or an in-fiction description, is just a view, and the base data being consistently readable is what makes it work.

Calibration bites on exactly one kind of Lens: **one that expresses a likelihood.** *"You'll probably make this."* A green/amber/red bar. Anything asserting odds. Such a Lens is making a claim about the Resolution Socket's distribution, and if the claim is wrong it is lying to the player. So a likelihood-expressing Lens must reproduce **the same distribution over magnitude** the Resolution Socket actually produces. Machine-checkable by sampling both.

**The knock-on constraint is on the Socket, not the Lens: the Resolution occupant must publish its distribution.** Not merely "returns a signed magnitude." Without a published distribution nobody could write an odds-expressing Lens even if they wanted to — and that clause is decidable now, while the magnitude formula itself is still open.

## Explanation channel
How a Lens narrates a Substrate change it cannot display. *"The curse is taking hold,"* never *"bloodline resistance −3."*

## Almanac
The per-character knowledge index. A view over Campaign data produced by a Lens or a Component, not a separate store. Answers "what does my character know?"

## Dispatch
The personal, private, bounded report delivered when a cadence Moment arrives. About your things, readable in one sitting, ending in a decision.

## Chronicle
The curated in-world digest — rumours, reports, hearsay. Rendered as testimony with bias and provenance, never as fact. **The Almanac is accurate; the Chronicle is interesting.**

---

# Part 7 — Numbers

## Fixed-point integer
The standard number representation. A whole number in a declared unit, with an agreed invisible decimal place. **Four decimal places** — store `125000`, meaning 12.5.

**Used wherever values are added:** resources, budgets, accumulations, capacities.

## Log-integer
The representation for quantities spanning enormous ranges. Store `1000 × log₁₀(value)` as a whole number.

- ±18,000 covers thirty-six orders of magnitude.
- **Multiplication and division become exact integer addition and subtraction.** No rounding ever.
- Ratios become differences — which is the meaningful comparison anyway.

**Used wherever values are multiplied or compared across scales:** mass, structural magnitude, energy, scale gaps.

**Log-integers are never added.** Adding them requires a lookup table, table lookup is lossy, and lossy addition is **not associative** — `(a ⊕ b) ⊕ c ≠ a ⊕ (b ⊕ c)` — which would break the promise that the same Ledger folds the same way everywhere. Sorting first makes it deterministic without making it correct, because two different sort keys give two different answers.

**So: compare and multiply only.** Multiplication and division are exact integer addition and subtraction of the exponents. Where things must be *summed*, they are converted into ordinary integers within one Scale, summed there, and converted back. No table ships, and there is nothing to version.

## Scale
A small whole number on an Entity. Each step is a factor of ten.

```
effective magnitude  =  attribute × 10^scale
```

A person is scale 0. A ship might be scale 3. **Attributes stay linear** — strength 11 is one unit above strength 10, at every scale — while the Scale number carries the orders of magnitude. Two ships at 10 and 11 differ by the same *proportion* as two people at 10 and 11, which is what makes it feel right.

**Addition is only defined within one Scale.** Two people's strength adds. A person's strength and a warship's do not. This is enforced, not merely discouraged: it makes it impossible for a small value to silently vanish into a large one.

### Crossing Scales — the default rule

Values are converted to **the target's Scale**, then added as ordinary integers.

> **`converted = magnitude × 10^(source Scale − target Scale)`, truncated toward zero.**

This happens at **R-750**, as its own visible slot, because a player who does nothing has to be able to see *why*.

```
your punch, magnitude 8 at Scale 1, against a Scale 4 airship
    8 × 10⁻³  =  0            nothing happens, and the expansion says so

the airship rams you, magnitude 8 at Scale 4, against Scale 1
    8 × 10³   =  8000         you are gone
```

Both are correct. A Component may declare its own cross-Scale rule; this one ships so the common case is free and nobody is tempted to flatten the world to Scale 0 to avoid the work.

### Scale belongs to the part, not only to the whole

The default rule alone is too blunt: `8 at Scale 1 → Scale 2` is **0**, which would mean a person cannot meaningfully hurt a warhorse or a rowboat. That is wrong, and the fix is not to soften the arithmetic.

**An Entity's parts carry their own Scale.** A Scale-4 airship has Scale-1 doors, ropes, hatches and crew. You do not punch the airship — you cut its rigging, pick the lock on its hold, set fire to its sails, and each of those is a Scale-1 interaction with a Scale-1 thing that happens to belong to a Scale-4 thing.

This is what makes Scale usable rather than a wall. **The Scale that applies is the Scale of the thing actually targeted**, and targeting the whole hull of a warship with a knife correctly does nothing at all.

Consequences: an Entity may hold parts, a part carries its own Scale and its own Thresholds, and destroying enough parts is how a small thing brings down a large one. **What counts as a part, and how parts roll up into the whole, is a Component question** — the Substrate only guarantees a part can carry its own Scale.

## Why not mantissa-and-exponent
Storing a number as (value, power of ten) is **decimal floating point**. It can be made deterministic, but only by pinning precision, rounding mode, normalisation policy, operation order, and library version — and even then, folding Records one at a time gives different answers than folding them in batches. See §Part 8.

## Vector — three different things
The word covers three objects and only one is geometric. Conflating them produces numbers that look plausible and mean nothing.

- **Geometric vector** — magnitude and a real direction (an angle) in space. A force. All axes are the same kind of thing. Addition by the parallelogram rule is genuinely correct.
- **Labelled tuple** — an ordered list of named values, like a spreadsheet row. `{force: 14, insight: 6}`. **No real direction, no natural length.** Any "overall size" is a formula you chose, not a fact.
- **Magnitude with a label** — "3 fire damage," "flammable 2." **Not a vector.** Only same-label addition is legal. There is no angle between fire and cold.

**In this system, Tags and Attributes are the second and third kinds.** Only physical forces, if ever modelled, are the first.

---

# Part 8 — Rules that constrain everything

## Additive-only
Nothing is ever removed, renamed, or given a new meaning. Numeric IDs are permanent and never reused. Deleted IDs are reserved.

## Open world
**Absence of information is not information.** If nothing has said whether a chair is flammable, the answer is *unknown*, not *no*.

**With a declared soft default.** For practical resolution, unspecified Tags are treated as absent — a fireball does not stop to ask about every object in its radius. The soft default is a **resolution convenience**, not a recorded fact: the chair is never *recorded* as non-flammable, so a Component added in year three can fill in the truth without rewriting history.

Rules are written positively — *"if known flammable, then…"* — never as *"if not flammable."* If a Component genuinely needs "definitely not flammable," that must be recorded explicitly as its own fact.

## Determinism
The same Ledger must produce the same state everywhere, forever.

- No floating point.
- No wall clock — logical Moments and Ticks only.
- Ordered iteration, or sort by a stable key first. **This is required for arithmetic correctness, not just for tidiness** — changing the order of additions changes results.
- Counter-based randomness keyed by `(record, entity, purpose)`, never a shared stream.
- Byte-wise string comparison, never locale-aware sorting.
- Never take a square root in simulation state. Compare squared values instead.
- Edition and Component version pinned per Record.

## No inference
Tags do not imply Tags. Categories do not imply Categories. Anything derived is derived by an explicit formula in a named Component, never by the system reasoning on its own.

---

# Part 9 — Operations

## Ledger
The append-only, immutable sequence of everything that happened in one Campaign. The single source of truth.

## Record
One immutable entry in the Ledger. Never modified. A correction is a new Record.

## Fold
The pure function deriving current state from a sequence of Records. Deterministic, total, no outside access.

## Campaign
One group, one Adventure, one Setting, one Edition. **The unit of isolation** — Campaigns never share state.

## Table
The people in a Campaign, as distinct from the Campaign, which is the state.

## Active Set
The exact Bundle, Components, versions, and Edition a Campaign uses. Hashed and recorded. **Components may be added and disabled, never removed.**

## Ops
The typed admin command-line tool. The only way Claude touches production data.

## Scratch
A local disposable copy of one Campaign, redacted, used for debugging.

---

# Part 10 — Words we do not use

| Don't say | Say | Why |
|---|---|---|
| Event | Record | "Event" also means something in the fiction |
| Module | Adventure | |
| Plugin | Component | |
| Attribute (for a capacity) | Capacity | An Attribute is any named value on an Entity. A **Capacity** is the graded, kind-agnostic sort — say Capacity when you mean one |
| Stat | Attribute | |
| Class / race | Category, or Tags | |
| Buff / debuff | Modifier, or State | A buff is a Modifier if it acts per vector, a State if it is a named condition. It is never a Verb — a Verb is what *places* it |
| Effect | Verb | **Reserved.** "Effect" is kept free for an in-fiction meaning later — a spell effect, a status effect. It is not a Substrate word. |
| Roll | Resolution, or magnitude | The roll is a Lens artifact; the magnitude is real |
| Damage | *fine as plain English; never a Substrate term* | A harm vector is a vector. There is no `damage` field, and the Substrate ships no health |
| Relation | Relationship | One word for the thing, everywhere. A Relationship is a Category of Entity holding one Connection per participant |
| Period | Moment | Retired. A duration is two Moments; there is no separate unit |
| Barrier | Moment | Retired. The point where accumulated Verbs are applied *is* a Moment |
| Degree, Cost, Outcome (as machinery) | *retired* | The two-axis outcome and the outcome ladders are gone. An attempt is a vector: direction and magnitude |
| Perception | Delivery, or Lens | Retired **as machinery**. Who receives a Record is `delivery`; what a participant sees rendered is a Lens. The *word* stays available as a **Capacity** name — `perception` is used that way in the Part 2C examples |

---

# Part 11 — Every list

Every list the system needs, written up so it can be picked up cold. **A list not written down is a decision nobody made.**

Each entry says what the list is, what breaks without it, what shape an entry takes, what the hard part is, and where to start.

**Thirty-two numbered, thirty live.** L8 and L9 are retired; L31 (Timings) and L32 (Moment kinds) were added in August 2026 when Time and Budget moved into the Substrate. Sixteen are marked **BLOCKING**: L1, L2, L3, L4, L5, L7, L18, L21, L22, L23, L25, L27, L28, L29, L31, L32. **Four are settled** — L21, L22, L23, L29 — leaving twelve. **L6 is not on that list and is the most important of all**; it is marked CLOSE LAST because it is closed against the finished set, not before it. Four more are **SETTLED** (L14–L17). The rest are PENDING but not blocking.

**The canonical order, and this document is the tiebreaker if another says otherwise:**

```
L21 → L29 → L22 → L23 → L32 → L31 → L27/L28 → L1/L2/L3 → L4/L5/L18/L25 → L7 → L26 → L6
```

L21 came before L29 because the attempt Dimensions live inside the attempt Space, so the Space had to exist first. L32 comes before L31 because a timing is defined in terms of Moment kinds and turn ownership. **L6 is last, always** — it is the one genuinely irreversible decision, and the evidence for its completeness is the worked examples every other list produces.

**Research standing behind the unsettled lists is in `lists-research.md`**, with the full reports in `research-timing.md`, `research-listeners.md`, `research-states.md` and `research-entities.md`.

---

## L1 · Categories — PENDING · BLOCKING

**What it is.** The labels an Entity may carry saying what kind of thing it is. An Entity may carry several at once; each brings its own Attributes.

**What depends on it.** L3 (Category Attributes) entirely. Every authoring form. Which Components attach to which Entities.

**Shape of an entry.** A name, a description, the Attributes it adds, and whether it can combine with everything or conflicts with anything.

**Constraints.** Permanent once shipped. Compose rather than nest — no single tree. Should stay small; Tags carry the long tail.

**Working draft.** Physical: `being` · `object` · `structure` · `place` · `substance`. Non-physical: `group` · `relationship` · `information` · `occasion`. Overlays: `character` · `vehicle` · `container` · `portal`.

**The hard part.** Deciding what is a Category versus a Tag. A Category adds *structure* (new Attributes); a Tag adds *membership* (no new fields). If it doesn't need new Attributes, it's a Tag.

**Start by** taking twenty things from across the reference Settings — a warship, a plague, a guild, a mountain pass, a forged letter — and asking which Categories each needs. The ones nothing needs, cut.

---

## L2 · Universal Attributes — PENDING · BLOCKING

**What it is.** Attributes present on every Entity, regardless of Category.

**What depends on it.** Everything. This is the smallest and most permanent list in the system.

**Shape of an entry.** A name, what it means, its Dimension Space if it has one, and its default when unspecified (which under open-world is *unknown*, not zero).

**Constraints.** Keep it brutally short. Anything not needed by literally every Entity belongs in L3.

**The hard part.** Almost nothing is genuinely universal. Identity and Scale are. Beyond that, be suspicious of every candidate.

**Start by** writing down what a bare Entity created mid-sentence by a GM — "there's a crowbar by the door" — must have to be valid. That is the list.

---

## L3 · Category Attributes — PENDING · BLOCKING

**What it is.** The Attributes each Category adds. Depends on L1.

**Shape of an entry.** Category name, then per Attribute: name, meaning, Dimension Space, default.

**The hard part.** Overlap. If both `being` and `vehicle` want a "speed," is that one Attribute defined once, or two? Rule of thumb: if the same word means the same thing, define it once at the most general Category that needs it.

**Start by** doing `place` first. It is the smallest, and it is the first thing anyone building a setting authors.

---

## L4 · Core Tag vocabulary — PENDING · BLOCKING

**Research: `lists-research.md` §5.** The number that matters: Magic has published **222 keywords in 33 years** and keeps **~17 always-live**. There is no cap on the total vocabulary; there is a hard cap around 15–20 on the always-on set. *Never implies another Tag* is strongly validated — and the gate has to forbid **derivation at read time**, not just declaration, or a Component reintroduces hierarchy in behaviour while passing the schema check.

**What it is.** The Tags the base Ruleset ships with, which every Component may rely on existing.

**Shape of an entry.** A namespaced ID, a name, whether it carries a magnitude, and a plain-language meaning.

**Constraints.** **Under thirty.** Every seed Tag is permanent. Tags never imply other Tags. Identified by ID, so a `flammable` from a Setting is a different Tag from the core one.

**The hard part.** This is where a list quietly grows to two hundred, because each addition seems obviously necessary at the time. The discipline is asking: does a *base-game Component* need this, or does it just feel useful?

**Start by** listing only what the base Ruleset's own Components read. Nothing else qualifies.

---

## L5 · State axes — PENDING · BLOCKING

**Research: `lists-research.md` §3.** Seven candidate axes, and two hard findings: magnitudes **take the higher, never add** (additive stacking makes any repeatable source unbounded), and **condition implication is a live maintenance cost** in shipping systems — the same failure as tag hierarchy.

**What it is.** Each axis is a set of mutually exclusive States. Posture is an axis: standing, prone, seated. Consciousness is another.

**Shape of an entry.** Axis name, the States on it, which is the default, and what each does.

**Constraints.** Only one State per axis at a time. States end only through a Verb. If two sources apply the same State, only the highest magnitude counts.

**The hard part.** Distinguishing an axis from a Resource. Continuous → Resource. Small set of named alternatives → State axis. Thresholds on a Resource may *set* a State, which is the bridge.

**Start by** listing the axes, not the States. Axes are the permanent part; States can be added to an axis later.

---

## L6 · Verbs — PRELIMINARY · CLOSE LAST

**What it is.** The closed set of operations that change state. **A taxonomy of consequence, not of activity** — nothing about attacking, persuading, or crafting.

**Status — deliberate.** This list is *not* being settled now. It is the last list closed, not the first. Every other list (Categories, Attributes, States, Channels, Dimensions, Layers, aggregation, conversions) produces concrete examples; those examples are the evidence for whether the Verb set is complete. Settling Verbs first means settling them against imagination instead of against the system.

**Preliminary candidates.** create · destroy · move · alter magnitude · transfer · set state · clear state · add tag · remove tag · form relationship · break relationship · reveal · conceal · bind to condition · advance clock · apply (deliver a Packet) · assume category · shed category · **repin** (change a pending vector's Moment)

**Note on `destroy`:** kept, but rare — it means *removed from play entirely*, never *killed*. Death is a State. `clear state` may still turn out to be `set state` to null.

Three of those were added by running the consequence test on eight fictional actions: *apply* (burning down a warehouse delivers a Packet to a thing, which no other Verb expresses), and *assume/shed category* (a character becoming undead changes what Attributes it even has). *clear state* may be redundant with *set state* to a null value — decide at closing time, not now.

**Uniform shape.** Every Verb carries the same fields: verb · source · target (exactly one) · secondary (zero or more) · direction · magnitude · class · layer. See Part 3, *Verb shape*. A Verb that needs a field outside this shape is a finding about the Substrate, not a reason to widen the shape.

**Constraints.** Closed and permanent *once closed*. This is the one genuinely irreversible decision in the system.

**The closing procedure.** When L1–L5, L7, L18, L21–L23 and L25–L29 are done: take every entry across those lists and every worked example produced along the way. For each, *assume the fiction has already decided what happened*, write only what changed, then which Verbs express it. **If a consequence needs an operation not on the list, that is a real finding. If it merely needs a Tag, a Channel, or a Component formula the list lacks, it is not.** Then, and only then, freeze.

**The hard part.** Resisting the urge to add a Verb for something that is really a Component's behaviour composed from existing Verbs.

**Depends on:** everything. **Blocks:** writing any Substrate code.

---

## L7 · Layers — PARTIAL · BLOCKING

**What it is.** The fixed precedence lattice. A Component never says "I modify speed" — it says "I modify speed *at R-500*."

**Status.** The **resolution region is drafted** — three regions and thirty slots (E×5, C×6, R×19), in Part 2A, every one forced by a worked case rather than guessed. Phase 0 added R-750 (Scale conversion), R-780 (standing-vector cap, reserved), R-850 (flat Guards, per source), and split the combine into R-800 (within a source) and R-1000 (across sources). What remains is everything outside resolution: progression, economy, movement, knowledge, social standing.

**Shape of an entry.** A number, a name, what belongs there, and which earlier layers it may depend on.

**Constraints.** Fixed and permanent. Numbered with gaps so slots can be inserted later — 100 across most of a region, 50 where two stages already sit close (R-300 and R-350). **Each layer may depend only on layers before it** — getting that dependency order right *is* the work.

**The hard part.** Err high. An unused layer costs nothing; a missing one is a foundation break. Magic needed seven and thirty years, and still surprises people about one time in a hundred.

**The test that produced the drafted region, and should produce the rest:** take a mechanic you want, write out what must already be settled before it can be computed, and see whether an existing slot supplies it. Every slot in Part 2A came from a case where the answer was no.

---

## L8, L9 — RETIRED

*Degree steps* and *Cost steps* were the two axes of the old Outcome. Both were deleted when an attempt became a vector: **Degree is the magnitude**, and **Cost is consequences at other Thresholds on other Dimensions**. The numbers are left vacant rather than reused, because a list number is permanent.

---

## L10 · Challenge Profile axes — PENDING

**What it is.** The vertices of the challenge shape — the named axes on which an Entity's difficulty is rated.

**Constraints.** The shape is a *picture*, never the score. The scalar is computed separately by an explicit formula, because the filled area of a radar chart depends on the order the axes are drawn in and on how many there are.

**The hard part.** Choosing the scalar formula, which is itself a design decision: a weighted sum says strengths and weaknesses trade freely; a geometric mean says a glaring weakness genuinely lowers the threat; taking the maximum says a thing is as dangerous as its worst trait.

---

## L11 · Asset types — PENDING

**What it is.** Which Entities get a real authoring surface — a screen where a user fills in blanks and gets a usable object.

**Working draft.** character · creature · place · item · faction. Vehicles are items with a Scale and a crew Relationship.

**Constraints.** Every authoring surface is real, permanent work. A sixth type means a sixth screen maintained forever.

**Order.** Place first (cheapest, and the first thing a setting-builder makes), then character (highest volume). Faction last — that is where the hard design questions live, and they are easier after the other four.

---

## L12 · Rails binding scopes — PENDING

**What it is.** For each Component, who sets its rails dial: the player, the GM, or the table.

**The hard part.** Some are obviously personal ("auto-resolve my downtime"). Some are inherently shared ("does the app run initiative"). The list is of the *scopes*, and each Component then declares which it uses.

---

## L13 · Record types — PENDING

**What it is.** The kinds of entry that can appear in the Ledger.

**The Ledger does not require a Verb to record something.** A Verb invocation is one Record type. The others change no state and are still permanent history.

**Must include** `the GM asserts X` as a first-class type — that is what makes the system able to absorb improvisation without understanding it.

**Likely members.** verb invocation · GM assertion · note · Moment boundary · Session boundary · proposal raised · proposal decided · compensation · supersession · Edition conversion applied · listener fired · Active Set change · cascade limit reached.

**The hard part.** Keeping non-Verb Records genuinely inert. The moment a "note" starts changing state, the Fold stops being a function of Verbs and the whole determinism argument collapses.

---

## L14 · Actor kinds — SETTLED

`user` · `system` · `agent`. An agent Record also carries the model, the session, and the human who approved it. **Agents never write as humans.**

---

## L15 · Verb classes — SETTLED

`Activated` (something chose to) · `Triggered` (a Listener fired and issued it).

**Two.** Replacement and Continuous were deleted when they turned out to be *a vector with a window*. A third class is a Substrate break and should be treated as a genuine finding, never a convenience.

---

## L16 · Decider kinds — SETTLED

`Auto` (a Component decides) · `Person` (a named human, **always carrying a Moment and a default**).

**Two.** A human decider with no fallback is never legal — it is how an asynchronous campaign dies. A table vote is `Auto`.

---

## L17 · Noun kinds — SETTLED

`Capacity` · `Tag` · `State` · `Resource` · `Relationship`. Each behaves differently under change, aggregation, and rendering.

**The word is *Relationship*, never *Relation*.** It is a Category of Entity holding one Connection per participant — not an edge.

---

## L18 · Aggregation operators — PENDING · BLOCKING

**What it is.** How two changes to the same thing combine, declared per kind of value and per attribute.

**Why it matters.** This is the single most likely source of "the same history produced different state," because two independently written Components otherwise produce order-dependent numbers.

**Shape of an entry.** The operator, what it does, and which kinds of value it is legal for.

**Known constraints.** Capacities plausibly add and multiply. Resources clamp. States take the highest applicable rather than the sum. Tags are set union. Relationships likely need their own rule. Channels add per Dimension.

---

## L19 · Causal tag vocabulary — PENDING

**What it is.** Component-agnostic tags attached to Records describing what *kind* of thing happened, so patterns can be found later.

**Why it matters now even though the feature is later.** Tags are cheapest and most accurate captured as they happen. They are an **optional additive field**, so Records written before tagging exists simply carry none, and a Component can derive tags retroactively from Verb patterns — less accurately than the emitting Component could have tagged them. **This is the easiest item in the system to skip and among the most annoying to have missed.**

**Shape of an entry.** A tag, and what kind of event it marks. *Betrayal. Escalation. Reversal. Debt incurred. Promise made.*

---

## L20 · Lens tiers — PENDING

**What it is.** The named complexity levels a player chooses between.

**Constraints.** Names must not imply a skill ladder. A twenty-year GM should be able to pick the simplest one without it sounding like training wheels. Names describing *character* rather than *level*.

---

## L21 · Dimension Spaces — **SETTLED, Aug 2026**

**Four: `physical`, `mental`, `social`, `attempt`.** Full definitions and the reasoning are in Part 2A under *Dimension Space*; the conversation that produced them is in `list-log.md`.

**The test used.** *Should these two things ever be able to cancel each other out?* If yes, same Space.

**What decided the fourth.** Psychic harm has no honest home under three — it is not a body injury and it is not social pressure. Splitting `mental` out also moved `resolve` off the social Space, which left social cleanly about standing and obligation.

**Rejected, with reasons:** `wealth` (money is a Resource, not a direction — a bribe is a social vector *paid for* with a Resource) · `knowledge` (a Tag or an Almanac entry; it is not a push and it does not cancel) · a separate `spirit`/`divine` Space (**folded into `mystic`**, so a miracle and a spell can meet).

---

## L22 · Dimensions, per Space — **SETTLED, Aug 2026**

**Twelve across the four non-attempt Spaces**, plus the fifteen attempt Dimensions from L29. Full tables, the test, and the reasoning are in Part 2A; the argument is in `list-log.md`.

`physical` — temperature · integrity · substance · vitality · vigor · mobility · acuity
`mental` — composure · clarity · will
`social` — regard · standing
`mystic` — working · essence

**Expected to move.** These will be tested for the first time when items, characters and magic systems are actually written, and additive-only means adding then is free. What is expensive is discovering that one of these was really two.

**Held back, with reasons:** `trust` (per-pair, therefore a Connection, not a broadcast axis) · `corruption` / `taint` (Setting-specific, therefore a Component) · `piercing`, `holy` (no describable opposite — Channels, not axes).

---

## ~~L22 · Dimensions, per Space~~ — superseded by the above

**What it is.** The axes inside each Space. **These are what create every relationship between every Channel**, so this list is doing more work than any other.

**Shape of an entry.** Space, Dimension name, what the positive and negative ends mean.

**Constraints.** Permanent. Adding a Dimension later is safe (existing Channels sit at zero on it); removing or redefining one is not.

**The hard part.** Getting the axes right so that the Channels you want land in sensible places *without anyone tuning the relationships by hand*. If fire and cold don't naturally end up opposed, the axes are wrong.

**Start by** listing the Channels you know you want first, then working backwards to the smallest set of axes that positions them all correctly relative to each other.

---

## L23 · Named Channels — **SETTLED, Aug 2026**

**Eighty-eight**, positioned in hundredths over all fourteen non-attempt Dimensions. The full table is in Part 2A; the argument and the research are in `list-log.md`.

**Two invariants, both CI-checkable:** every row sums in absolute value to exactly 100 · no two Channels share a position.

**A Channel is not confined to a Space.** Spaces partition Dimensions, not Channels — `fatigue`, `venom`, `concussion`, `curse` and eighteen others cross Space boundaries, and could not be written under the first draft.

**Expected to shrink**, and the tightest pairs are named in Part 2A.

---

## ~~L23 · Named Channels~~ — superseded by the above

**What it is.** Damage types and their equivalents, each defined as a position in a Space.

**Shape of an entry.** Name, Space, a value on each Dimension, and whether it is Transient or Persistent.

**Example.** `fire` — temperature +100, everything else 0.

**Constraints.** Once a Channel is placed and shipped, its position is permanent — every Guard and every other Channel's behaviour against it depends on where it sits.

**The good news.** A Channel added in ten years is automatically correct against every existing Channel, because the relationships are derived from position rather than declared.

---

## L24 · Guard presets — PENDING

**What it is.** Named shorthands for common protections. "Fire resistance," "insulated," "armoured."

**Shape of an entry.** A name and a value on each Dimension.

**Note.** These are conveniences, not mechanisms. A Guard is just Dimension values; the presets exist so authors do not hand-enter the same numbers repeatedly.

---

## L25 · Transient-to-Persistent conversions — PENDING · BLOCKING

**OPEN DECISION — does the packet handed to Landing carry the contributor breakdown, or only the combined totals?**

Worked example. A Setting lands `vitality` two ways: every surviving point reduces a `health` Resource, **and** a single landing over 10 applies the State `maimed`.

```
Kira is struck by three attackers in the same Moment.
Surviving vitality contributions:      −6      −5      −4
R-1000 combines across sources:            vitality −15
```

The pool rule is unambiguous: `health −15`. The bar rule is not. **The packet is 15, which clears the bar — but no single blow was over 10.** And the packet arriving at R-1200 is just `[vitality −15]`; it has forgotten that it was three contributions.

The two readings are different games. **Sum** means three small attackers can maim by teaming up. **Highest** means only one big blow can — which is exactly the all-in-strike incentive recorded in Mythras. Both are legitimate; the Substrate currently cannot express the second at Landing, because the information is gone by then.

The Threshold aggregation modes (`sum`, `highest`, `each`) already exist as vocabulary — but they were settled for Thresholds *earlier in the lattice*, where contributors are still separate. Landing is downstream of R-1000.

**Recommendation: carry the contributor list into Landing.** Three reasons. R-850 already operates per contributing source, so the breakdown exists inside the lattice anyway and is not new work. The Resolution Record is already required to make every slot derivable, so it is already being written down. And the field's best landing mechanisms — GURPS's major wound, Mythras's Serious/Major wounds, Blades' harm levels — all read **highest**, so refusing it would rule out most of the good precedents.

**The cost of saying yes:** the Landing Component becomes order-sensitive and needs its sort key stated in its SPEC, and the packet is bigger. **The cost of saying no:** `highest` and `each` are simply unavailable at Landing, forever.

**Research: `lists-research.md` §4.** Eleven landing models are catalogued there, with a proposed model for each of the fourteen Dimensions and a precedent for each. The three findings that change the shape of this list: the universal architecture in the field is **buffer → convert → name** (so the buffer belongs to the Landing Component and is never durable); **nothing uses an ablative pool for a capability axis**, which splits the physical block cleanly; and **the social axes never land on the target** — they land on a Connection or a public accumulator.

**What it is.** How a Packet that survived Channel interaction and Guards becomes an actual change to something Persistent.

**Why it matters.** This is the last step of every interaction in the game, and it is where "you took 4 damage" actually happens.

**The open question.** Given a surviving Packet with values spread across several Dimensions, how much Health is lost? Sum of magnitudes? Weighted per Dimension? A separate conversion per Persistent Channel?

**The hard part.** Different Persistent Channels probably convert differently — the same Packet might cost a lot of Health and no Standing, and a different one the reverse. That suggests one conversion rule *per Persistent Channel*, which is more work but more expressive.

---

## L26 · Listener condition forms — PENDING

**What it is.** The closed set of things a Listener is allowed to watch. Verbs return nothing; Listeners are how anything ever follows from anything.

**Sketch, not a proposal.** resource crosses a threshold · state entered · state exited · tag gained · tag lost · relationship formed · relationship broken · clock reaches a value · category assumed or shed.

**Constraints.** A Listener watches **state, not Verbs** — "is this now true," never "did that just happen." Declared as data by a Component, never as code. Evaluated at R-1400, produces Verbs pinned to a **later Moment**, class `Triggered`.

**The hard part.** Cascade depth. Listener A fires B fires C. Needs a hard limit, a deterministic evaluation order across simultaneously-satisfied Listeners, and a defined behaviour at the limit. **All three PENDING.** Get the ordering wrong and the same Ledger folds differently on two machines.

**Depends on:** L5 (States), L7 (Layers). **Blocks:** any Component with a consequence.

---

## L27 · Sockets — PENDING · BLOCKING

**What it is.** The named holes in the Substrate that a Component *must* fill. Exactly one occupant each, never zero, never two. A Bundle with an empty Socket must fail to load.

**Three, as of August 2026.** Time and Budget were on this list and moved into the Substrate; see *Why Time and Budget are not Sockets* in Part 1. Dropping from five to three also dissolved the cross-Socket vocabulary problem — Time and Budget were the two whose published names everything else had to reach across.

| Socket | Vocabulary it publishes (Substrate, additive-only) | Behaviour it owns (the occupant) | Without it |
|---|---|---|---|
| **Place** | how position and scope are named — here, near, within, containment | what a place *is*, how distance works, what Scale means for a part of a whole | nothing has a location, so nothing can be area-scoped, and nothing knows the door belongs to the ship |
| **Resolution** | that an attempt returns a signed magnitude, **and the distribution it is drawn from** | how the magnitude is produced — dice, cards, deck, auction | no attempt produces a number |
| **Landing** | what persistent state each Dimension may address (**= L25**) | how a landed vector becomes persistent state | vectors arrive and nothing happens |

**Place is settled as a Socket, and the argument for it is not the obvious one.** The obvious argument — that distances differ between settings — could be answered by telling people to scale the numbers, and that is what most games do. The real argument is that a game about insects, a game about galaxies, a game where everyone teleports at will, and a game set in a five-dimensional astral sea are not the same game with different numbers, and the engine should not force them to pretend they are. A Setting with no distance at all — everything is *here*, *adjacent* or *far* — is a legitimate occupant, and the Substrate should not be able to tell.

The second argument is arithmetic: **Scale belongs to the part as well as the whole.** A Scale-4 ship has Scale-1 doors, and R-750 reads the Scale of the thing actually targeted. Something has to know the door is part of the ship, that is containment, and containment is Place. A Substrate that cannot answer *is A inside B* cannot do its own arithmetic.

**Resolution's contract has one clause that is decidable now.** The occupant must publish its distribution, because rule 19 requires any likelihood-expressing Lens to be Calibrated against it. An occupant that cannot state its distribution cannot ship, no matter how good its dice are. The *formula* stays open; the *contract* does not.

**Resolution may be one occupant with dials.** A default with options players choose between is fine — but the choice is made at Setting creation and pinned, never toggled live. Two people folding the same Ledger with different options selected would get different states, and that is the whole determinism guarantee gone.

**Landing's Vocabulary is L25**, which is now a fourteen-row table — one per non-attempt Dimension. So Landing's contract can be written today and its Vocabulary filled when L25 closes.

**The hard part.** Keeping it at three. Every Socket is a permanent dependency for every Component ever written, and each one is also a hole in the documentation. A capability belongs in a Socket only if the Substrate genuinely cannot function without it **and** freezing one answer would make a whole class of Setting impossible.

**Depends on:** nothing now. **Blocks:** the Component contract, and the rule that makes a Bundle valid.

---

## L28 · Economy — PENDING · BLOCKING

**What it is.** The atomic unit a cost is denominated in, and the shape of a cost. Substrate, because every ability ever written depends on both.

**Settled in principle, August 2026:**

- **One unit, the doubloon.** Integer, 64-bit, frozen. No denominations, no named rungs — see *Doubloon* in Part 5 for why the ladder was cut.
- **A cost has at least three fields** — `cost`, `timing`, `cap` — and cost and timing are orthogonal. See *Cost* in Part 5.
- **`reaction` is not a unit and not a size.** It is a timing: doubloons spent during a Moment you do not own. That is why a 10-doubloon reaction and a 40-doubloon reaction are both reactions.
- **`attention` is not a unit.** It is doubloons in the `committed` spend mode — concentration is effort you spent that stays spent.
- **`strain` is not a unit.** It accumulates against you rather than being spent, which makes it a Resource. Exhaustion is already settled as a `vigor` push plus a Resource; a second name for it was duplication.

**Spend modes — Substrate.** `spent` (gone until refresh) and `committed` (unavailable until something releases it). These are shape, not meaning, so they belong in the frozen half: a `repin` has to know whether the cost it names can be paid from something already committed, and nothing else can answer that.

**Still open.** The allowance (base Ruleset, deliberately deferred to playtest — see *Budget*), and whether a second, non-convertible unit is ever needed.

**One hard rule if a second unit is ever added: it is never convertible with the first.** Any two-way conversion between action currencies is round-trip arbitrage. The recorded case is two Minecraft mods disagreeing on an energy exchange rate — 8:1 against everyone else's 4:1 — where nothing crashed, no value went out of range, and the symptom was simply 80k appearing where 40k was due. In an economy a rate disagreement is not a display bug; it is a money printer, and players find it before the designer does.

**The field's warning about the price list.** Every fine-grained action currency that failed — Exalted 2e's ticks, Rolemaster's percentage-of-round, the original X-COM's Time Units — failed because of the *price list*, not the atom. Every one that survived kept the list tiny: Feng Shui has essentially one price, Pathfinder 2e works because almost everything costs exactly one. **The atom may be fine; the published set of prices must stay short.**

**Depends on:** L31 (Timings), for the second field. **Blocks:** every spell, attack and ability ever written.

---

## L31 · Timings — PENDING · BLOCKING · **NEW, Aug 2026**

**What it is.** The closed, named set of answers to *when may this be paid for and used*. One word on an ability, the way a Channel is one word on a vector.

**Why it is named rather than written out.** The alternative — every ability hand-writing an eligibility condition — was tried on paper and is unusable: to say *"this is a reaction"* an author had to write three lines of condition. Naming it is the same move the whole design already makes. A Channel is a named position over fourteen Dimensions; nobody writes the coordinates. A timing is a named position in the time model; nobody writes the condition.

**The structural finding from the field.** Magic and Yu-Gi-Oh independently converged on the same four-way split of *how an ability is used at all* — activated, triggered, static, and resolution instructions. Three of those four are already other machinery here:

| Their category | Ours |
|---|---|
| Activated | an ability with a `cost` and a `timing` |
| Triggered | a **Listener** — already class `Triggered`, already pinned to a later Moment |
| Static | a **Modifier** or a **Guard** — present at R-200/R-300 or R-850/R-1050, never resolved |
| Spell ability | the vector's own resolution |

**So L31 is only about the activated case**, which shrinks it a great deal. And the systems that survive keep the set tiny: Magic has two speeds, Yu-Gi-Oh three, Pathfinder 2e two. D&D 4e had seven action types with a substitution hierarchy and it is the recorded failure.

**Candidates — six, and at least one should be cut.** See `lists-research.md` for the evidence behind each.

`own` · `any` · `respond` · `interrupt` · `pending` · `standing`

**Three questions the list has to answer:**

1. **Is `interrupt` worth it?** Resolving *before* the thing that prompted it — and possibly preventing it — is the most satisfying play in any game that has it, and the largest single source of table arguments, because "before" means rewinding something already declared. D&D 4e had it; 5e cut it.
2. **Is `standing` a timing at all**, or is it just *"this is a Modifier, not an ability"*? Leaning cut.
3. **Does `any` need to exist**, or is it `own` plus `respond` with no condition?

**The cost of a large set is not the number of names — it is the pairwise interactions.** Two names have one interaction; seven have twenty-one. That is the arithmetic behind 4e's action-economy complaints.

**Depends on:** the Substrate time model. **Blocks:** L28, and every ability ever written.

---

## L32 · Moment kinds — PENDING · BLOCKING · **NEW, Aug 2026**

**What it is.** The named points a vector may be pinned to. Substrate, frozen, additive-only.

**Candidates:** start of my turn · end of my turn · start of the round · end of the round · start of a named Entity's turn · end of a named Entity's turn · immediately · entry to Ordered time · exit from Ordered time.

**The one that carries weight is turn ownership** — *mine* versus *not mine* — because `respond` and `interrupt` are defined in terms of it. Without ownership as a Substrate concept, a reaction cannot be expressed portably at all.

**What is deliberately not here:** anything coarser than a round. Downtime weeks, seasons and campaign turns are Components, layered alongside. Content written for second-scale play and content written for month-scale play do not have to be compatible, because they never meet.

**Depends on:** nothing. **Blocks:** L31, L28, L26.

---

## L29 · Attempt Domains and Dimensions — **SETTLED, Aug 2026**

**Seven Domains, fifteen Dimensions.** The list, the structure and the allocation rules are in Part 2C; the research and the argument are in `list-log.md`.

**Still open, deliberately:** how **magnitude** is produced — *"a combination of modifiers and a dice roll,"* with the exact formula deferred until every list is filled and the real numbers can be seen. Tracked in `open-questions.md`. The list does not depend on it; every worked example does.

---

## ~~L29 · Capacities~~ — superseded by the above

**What it is.** The graded, kind-agnostic dispositions an Entity has, **and** the Dimensions of the attempt Dimension Space. One list doing two jobs, which is what makes it the single most load-bearing decision in the system.

**The test per candidate.** State it as a capacity rather than a quality, then check it applies without absurdity to a person, a ship, a faction and a storm. *Capacity to exert force* passes. *Strength* does not.

**The other test, easy to skip.** What you deliberately leave off. Nothing above the Substrate can put it back, and this is where the stance lives.

**Shape of an entry.** A name stated as a capacity, what it affords, and the four-way absurdity check.

**Anything may attempt. — SETTLED, Aug 2026.** The Substrate never forbids an Entity from making an attempt, and no Category gates it. A ship, a faction, a storm, a lock may all carry attempt Dimensions; whether any given one *does* is an authoring decision, not a schema rule. The reasoning is Dylan's: *"No reason to restrict something that the GM doesn't have to allow."*

This falls out of **absent is not zero** rather than needing a rule of its own — an Entity with no points in any attempt Dimension simply cannot attempt anything, and nothing had to say so. It also means the strongest precedent in the field (Star Trek Adventures, where a ship *assists* but never rolls) is available as a **content** stance, not a Substrate one: a Setting that wants ships to assist rather than act simply does not give them attempt Dimensions.

**Constraints.** Additive-only and **Component-extensible** — a Component may publish a new Capacity forever. But every Capacity is also an axis a player can spend Allocation Points on, so the set is the interface, and it should stay small enough to choose between at a glance.

**The hard part.** Resisting one Capacity per skill. *Thieves' tools* is gear supplying a modifier to `manipulation`, not a Capacity of its own.

**Depends on:** L21 (Dimension Spaces) — which Spaces exist has to be settled first, because the Capacities *are* the Dimensions of the attempt Space. **Blocks:** L2, L3, L22, the character sheets, and every piece of content ever written.

---

## L30 · Instrumentation surfaces — PENDING

**What it is.** Everything the build has to expose so it can be developed and playtested at all: what is logged, what is inspectable, what a tester may change, and what a tester may write down.

**Why it is a list rather than a feature.** Because it has to be decided alongside the Substrate, not after it. A Record shape that cannot answer *"why did that happen"* is not fixable later without a migration, and a Fold with no seam for a tester to poke is not a Fold anyone can playtest.

**Shape of an entry.** A surface, who may use it, whether it writes to the Ledger, and whether it exists in production or only in a test Campaign.

**Sketch, not a proposal.** total event log with search · the full Resolution Record expanded layer by layer for any resolution ever · a state inspector at any Moment · time-travel to any Moment and fork · an inline note anchored to any Record, Entity or Moment · a what-if that re-resolves with changed inputs and never writes · Active Set swapping mid-Campaign in a test Campaign · a tester account kind with its own permissions · a session recorder that replays a whole play session at speed · determinism diffing across two machines.

**The hard part.** Deciding which of these ship to real tables. Some are so good that hiding them behind a tester flag would be a mistake; some would ruin a game if a player saw them mid-scene.

**Depends on:** the Record shape, the Resolution Record. **Blocks:** the first playtest.

---

# Part 12 — Decisions log

Decisions recorded with their reasoning, so they can be revisited intelligently.

| Date | Decision | Reasoning |
|---|---|---|
| **Aug 2026** | **Anything may attempt — no Category gates it** | *"No reason to restrict something that the GM doesn't have to allow."* Falls out of *absent is not zero* rather than needing its own rule. A Setting that wants ships to assist rather than act simply gives them no attempt Dimensions — a content stance, not a Substrate one |
| **Aug 2026** | **Points spent this Moment must be readable state** | Otherwise the escalating-repetition penalty every fungible economy needs is inexpressible, because a Listener watches state and never Verbs. Dylan: *"points being spent is a good way to deal with turn-based economy. Just that there will also be more to it"* — so more spend-visible state is expected, and the shape should not assume this is the only field |
| **Aug 2026** | **Time and Budget move from Sockets into the Substrate; three Sockets remain** | A Socket is a hole in the *explanation*, not just the code — every worked example had to caveat itself, which made every spell and ability harder to understand than necessary. The objection (a Setting wanting week-long turns) dissolves because a Component **adds** rather than replaces: month-scale play never uses second-scale abilities, so they need not share a machine |
| **Aug 2026** | **Socket occupants are frozen per Setting** | Stronger and cleaner than "Edition-level change." The occupants are part of a Setting's identity; changing one produces a different Setting, and moving a Campaign across is a Conversion. Components stay swappable within a Setting |
| **Aug 2026** | **Place is a Socket** | Not because distances differ — that could be answered by scaling numbers. Because a game about insects, a game about galaxies, one where everyone teleports, and one set in a five-dimensional astral sea are not one game with different numbers. Second argument: Scale belongs to parts as well as wholes, so something must know the door belongs to the ship, and that is containment |
| **Aug 2026** | **One Economy Unit — the doubloon. No denomination ladder** | A size vocabulary (`action`, `quick`) beside a timing vocabulary made authoring roundabout, because "reaction" is a *when* and "action" is a *how much*. Fusing them is what produced *bonus action*, which its own designer has publicly disowned |
| **Aug 2026** | **A cost is at least three fields: `cost`, `timing`, `cap`** | Price alone cannot express opportunity. Orthogonal fields make a 10-doubloon reaction and a 40-doubloon reaction both legal and both reactions — the thing a fused slot cannot do. Frequency stays out of the timing name or the fusion returns by the back door |
| **Aug 2026** | **Timings are a named closed set (L31), not hand-written conditions** | Writing the condition out took three lines to say "reaction." Naming it is the same move Channels already make: a named position, never the coordinates. The field's evidence is that the surviving speed sets are tiny — Magic 2, Yu-Gi-Oh 3, PF2e 2 — and that D&D 4e's seven is the recorded failure |
| **Aug 2026** | **Calibration applies only to Lenses that express likelihood** | A Lens is a view of the data; most need no calibration. The rule bites only where a Lens asserts odds, because that is a claim about the Resolution Socket's distribution. Knock-on: the Resolution occupant must **publish** its distribution — decidable now, while the magnitude formula stays open |
| Aug 2026 | Base Ruleset is built as Components, not a monolith | Otherwise every swappable piece needs a bespoke hook invented in advance |
| Aug 2026 | Verbs are a taxonomy of consequence, not activity | Every attempt at action primitives has failed; consequence is finite where action is infinite |
| Aug 2026 | Model what a thing affords, not what it is | Fixed property lists across all kinds have failed in five fields independently |
| Aug 2026 | Entity = any noun; Categories are multi-select | Faceted classification composes; hierarchies don't |
| Aug 2026 | Relationship is a Category of Entity | Makes relationships first-class without a special structure |
| Aug 2026 | Tags carry optional magnitude; identified by ID not name | Solves skills-and-competences without expanding the attribute set |
| Aug 2026 | Tags never imply Tags | Inference plus open-world assumption is slow and unpredictable |
| Aug 2026 | States end only through a Verb | One mechanism instead of three |
| Aug 2026 | Substrate defines Resources but ships none | A setting may legitimately have no health, no money, no stress |
| Aug 2026 | Open world, with a soft default of absent | Preserves history under additive change without requiring exhaustive tagging |
| Aug 2026 | Fixed-point integers for addition; log-integers for scale | Deterministic; avoids floating point entirely; ratios become differences |
| Aug 2026 | Challenge is a profile with a separately computed scalar | A measured 2.34× swing came from reordering axes on identical data |
| Aug 2026 | Channels are positions in a Dimension Space | Relationships between Channels are derived, not declared — so they can never contradict, and a new Channel is automatically correct against every existing one |
| Aug 2026 | Channels combine by per-Dimension addition | Exact whole-number arithmetic; no angles, roots, or rounding |
| Aug 2026 | Guards subtract per Dimension, floored at zero | Over-penetration falls out of the arithmetic with no special rule |
| Aug 2026 | Transient Channels fully resolve before touching Persistent ones | A property of what the Channels are, not a maintained priority list |
| Aug 2026 | Channels never merge — only magnitudes change | Keeps per-type Guards possible after Channels have interacted |
| Aug 2026 | Attributes are linear; Scale is a separate small exponent | Preserves relative differences at every scale; 10 vs 11 means the same thing for a person and a warship |
| Aug 2026 | Addition is only legal within one Scale | Makes silent loss of small values impossible rather than merely unlikely |
| Aug 2026 | "Effect" retired as a Substrate word; a proposed change is a **Verb** | One word for one thing. "Effect" is reserved for an in-fiction meaning later |
| Aug 2026 | The Verb list is closed **last**, not first | Every other list produces the examples that are the only real evidence of completeness |
| Aug 2026 | Every Verb has one uniform shape | One parser, one validator, one log format, one replay path — forever. A Verb needing an extra field is a Substrate finding |
| Aug 2026 | Exactly one primary target per Verb, plus secondaries | "Who did this happen to" is never ambiguous in the Ledger; three people means three Records |
| Aug 2026 | Direction + magnitude on every Verb, not just harm | The Channel/Dimension idea generalises: *what is pushed on*, and *how hard* |
| Aug 2026 | Verbs return nothing; **Listeners** carry consequence | Nothing is running when a Verb is written down. A return value would smuggle execution into data |
| Aug 2026 | Listeners watch state, not Verbs | State is stable and re-derivable; the sequence of Verbs that produced it is not |
| Aug 2026 | The Ledger does not require a Verb to record something | "What happened" is strictly larger than "what changed" — the Verb set only has to cover the second |
| Aug 2026 | Replacement and Continuous collapse into **a vector with a window** | A vector already standing in the space *is* "instead of"; a condition-scoped vector *is* "while true." Two mechanisms deleted, none added |
| Aug 2026 | A Verb is placed and **pinned**, not applied | Timing becomes data on the vector rather than structure in the engine |
| Aug 2026 | A Moment is a reference, not a tick | Reactions can repin, so arrival cannot be computed at placement time |
| Aug 2026 | Pending vectors are Entities | Reactions, counters and deflections become ordinary Verbs aimed at the vector; and a vector in flight is *state*, so Listeners can watch it without watching Verbs |
| Aug 2026 | No difference between an attack and an aura | Both are vectors; duration is the window, area is the scope |
| Aug 2026 | Ordered time ends when nothing is pinned to a turn-anchored Moment | An observable state, not a judgement call |
| Aug 2026 | No cap on repins; instead **a repin must name a cost** | Bounded by economy rather than by an arbitrary engine limit, and CI-checkable |
| Aug 2026 | No special case for death | Death is a State and Entities persist, so a blow landing on a corpse needs no rule |
| Aug 2026 | Standing vectors vary on two independent axes: reactive/scheduled and durable/depleting | All four combinations are real mechanics; only reactive/scheduled affects whether Ordered time stays open |
| Aug 2026 | **Sockets** — some Components are mandatory | The Substrate declares holes it cannot fill itself. Time is the proof |
| Aug 2026 | Every Socket has two halves: **Vocabulary** (Substrate, additive) and **Behaviour** (the occupant) | Content names `action` and `start of turn`; it never names an occupant's internals. Without the split, swapping an occupant breaks every spell ever written |
| Aug 2026 | **Period retired.** There is only the Moment | A turn, a round, a downtime week and a season are the same thing at different grains. *(Amended Aug 2026: turn and round are Substrate; anything coarser is a Component.)* |
| Aug 2026 | **Budget is a Socket**, but Economy Unit *names* are Substrate | *Costs one action* has to keep meaning something whichever economy is installed |
| Aug 2026 | Windows **freeze** when Ordered time ends; they never convert | A ward with three rounds left keeps three rounds left. Simpler than a conversion table, and it resumes exactly where it stopped |
| Aug 2026 | Pending arrivals cannot survive leaving Ordered time | Nothing special needed — the exit is already blocked while anything is pinned to a turn |
| Aug 2026 | Cross-scene vectors pin to **the next Moment both share** | No synchronisation machinery. The Substrate guarantees such a Moment eventually exists |
| Aug 2026 | **Perception retired.** All entitled data is in the client; the Lens decides what is shown | Three things were being conflated. Rendering is the Lens, in-fiction knowledge is an optional Component, and only delivery is infrastructure |
| Aug 2026 | **Every layer of a Resolution Record is visible to everyone** | Secrets are a later deliberate decision, not the default posture |
| Aug 2026 | **Delivery** — one Record field, default everyone | The only part a Component cannot supply, because a Component cannot decide what the server sends. Exists for GM prep and purchased content |
| Aug 2026 | **The server folds and is authoritative; clients render** | Tier 1, not deferrable. Client-side folding would silently diverge the moment anything is withheld |
| Aug 2026 | **Belief-folds deleted.** There is one Fold | No per-observer state, no gap tolerance, no client computing a possibly-wrong world |
| Aug 2026 | The information-set invariant is satisfied by construction | Everyone sees everything, so every action menu is identical. No validator needed |
| Aug 2026 | Provenance is not a Record field | A Chronicle Component emits its own `rumour` Records carrying source and reliability in the payload |
| Aug 2026 | A **Proposal is a pending Entity** using the same pinning machinery as a vector | Repinnable, cancellable, queued. *"Give me another day"* is a `repin` and costs something |
| Aug 2026 | A human Decider **always carries a Moment and a default** | An open-ended human decider is how an asynchronous campaign dies. A live table uses a very long deadline |
| Aug 2026 | Threshold visibility is a built-in GM setting | Same content, two very different games |
| Aug 2026 | **Standing Orders are Listeners the player parameterises** | The Component publishes the template, the player fills the values — so the authoring line holds. A default must include a default *allocation*, not just a verb |
| Aug 2026 | Values add by default, unless something declares otherwise | One rule for vectors, States, Tags and everything else |
| Aug 2026 | ~~No multiplication anywhere~~ — **corrected**. Direction and magnitude are separate, and resolved value = direction × magnitude | Fixed-point × integer is exact, so the one multiplication costs nothing. Two fixed-point numbers are never multiplied |
| Aug 2026 | A base Channel's direction values sum in absolute value to 1 | Makes magnitude mean the same thing for every Channel, and makes a direction modifier read as a fraction of a unit |
| Aug 2026 | **Direction is never modified.** All modification is to magnitude | Direction says *what kind*; magnitude says *how much*. Bending direction would make one number mean two things |
| Aug 2026 | Percentage modifiers **sum**; they never compound | Compounding stops being commutative the moment you round between steps — demonstrated with 5, +30%, +40% giving 8 or 9 by order |
| Aug 2026 | Percentages resolve before absolutes, on separate Layers | A flat bonus is never inflated, so its worth stays constant. The reverse order changes the answer, so the order is fixed permanently |
| Aug 2026 | A modifier that creates a vector does not also modify it | No double-dipping; one pass per modifier per vector |
| Aug 2026 | Rounding happens once per vector, at the percentage step, truncating toward zero | Everything downstream is exact. Toward zero keeps signed values symmetric. Persistent state is fixed-point so no second rounding is needed |
| Aug 2026 | **Magnitude is assembled at resolution, not at placement** | Forced by cooperative buffing: an amplifier cast after a fireball is thrown must still reach it. Also collapses everything into one computation point |
| Aug 2026 | Modifiers are **snapshot** or **ambient** | The sword you swung with, versus the vulnerability you had when it landed. One mechanism, two capture times |
| Aug 2026 | Vector, Modifier and Guard are the same object distinguished only by **Layer** | The Layer says where in the pipeline it acts. No special cases in the engine |
| Aug 2026 | Magnitude assembly happens **per vector, before combination** | A fire-conditioned modifier must scale the fire vector and leave the cold vector beside it alone |
| Aug 2026 | Immunity is a **clamp**, never a −100% modifier | Percentages sum, so a −100% would be cancelled by any enemy buff. This is what makes the clamp layer load-bearing |
| Aug 2026 | Content never says "double" — it says *+100%* | Two doublings give ×3, not ×4. The vocabulary has to match the arithmetic |
| Aug 2026 | Modifiers carry a **tier**, so a modifier can modify a modifier | Resolved highest tier down; within a tier everything sums |
| Aug 2026 | **Enhancement Capacity** — a ceiling on how much enhancement a vector can carry | Moves the stacking problem out of the arithmetic and into the fiction. A better gun holds more; upcasting raises it; Resources can buy it |
| Aug 2026 | Capacity makes the sum-vs-compound choice free | With a ceiling in place, three amplifiers hit the cap either way — so summing costs nothing in balance and buys determinism |
| Aug 2026 | **Capacity bounds enhancement only, never reduction** | Amplification compounds toward absurdity; reduction converges on zero. Only one direction runs away. Protection Capacity dropped |
| Aug 2026 | A vector's Capacity is captured at creation, from its source | Nothing that spends a Capacity can also raise it mid-flight; keeps the arithmetic acyclic |
| Aug 2026 | Overflow is clipped and **recorded**, never interpreted, by the Substrate | Backfire is a Component reading the overflow. Clipping is engine, drama is content |
| Aug 2026 | Guards take proportional **and** flat forms, in that order | Same structure as magnitude assembly, for the same reasons |
| Aug 2026 | **Damage cancels before it reaches the target.** One rule, no fork | Everything incoming meets everything else first; only the remainder is checked against Guards. Where a thing lives decides when it acts — source-side is a Modifier, target-side is a Guard |
| Aug 2026 | Guards may be **signed**; a negative Guard is a vulnerability | *100% against temperature-positive* is a fire elemental: shrugs off heat, still feels cold |
| Aug 2026 | **No maximum modifier tier.** The rule is acyclicity, not a ceiling | Finitely many modifiers are present, so working down the tiers always terminates. A modifier may only affect strictly lower tiers — checkable per modifier, no arbitrary number to regret |
| Aug 2026 | **Pre-sum, never pre-apply.** A placed vector is a direction, four numbers and a pin | Summation is associative so partial sums finish later unharmed; application is not. Everything source-side collapses at creation and never looks back |
| Aug 2026 | The Resolution Record **stores inputs and a hash; layers are derived** | The Fold is deterministic, so every intermediate is recomputable with the pinned Component version. Storing them would store what can always be recreated — and the hash makes recomputation self-checking |
| Aug 2026 | **An attempt is a vector.** Direction is what you are trying; signed magnitude is how well it went | One machinery for harm and for action. Failure is the same direction with a negative magnitude |
| Aug 2026 | Direction comes from the **declaration**, magnitude from the **resolution** | Exactly as with a spell: the Channel is what you cast, the magnitude is how it went. The split of effort across Dimensions becomes the tactical choice |
| Aug 2026 | Consequences are **Thresholds declared by things in the world** | Each object declares its own bars, so independently authored content stays consistent — the same move as Channels declaring positions rather than relationships |
| Aug 2026 | **Degree, Cost, outcome ladders, scalarization and Difficulty all deleted** | Degree is the magnitude; Cost is consequences at other Thresholds; Difficulty is a Threshold. Five concepts removed, none added |
| Aug 2026 | Resolved magnitude becomes the **base magnitude** of the vectors the attempt places | The join between resolution and consequence, with Thresholds firing extras on top |
| Aug 2026 | Cooperation and opposition fall out of vector combination | Two helpers combine, bounded by the task's Capacity; an opposed action is two vectors pointing opposite ways |
| Aug 2026 | **Allocation Points** — a player spreads whole points, and direction is the proportion spent | The sum-to-1 rule becomes impossible to violate, because the interface hands out points and the arithmetic does the dividing |
| Aug 2026 | Points buy **precision, not power** | One point all-in is 100%, same as five. More points only buy finer splits — so this progression axis can never inflate damage |
| Aug 2026 | You allocate against bars you cannot see | Which is what makes information worth having. Scouting a lock changes how you spend |
| Aug 2026 | **Participation Capacity** — how many sources may contribute to one thing | A lock worked by one person at a time. Makes cooperation a decision instead of a pile-on |
| Aug 2026 | **Objects take turns.** The default anchor applies to any Entity, not only creatures | Cooperation falls out with no "help action": everyone pins to the lock's turn and it all combines there. Creates a real window — contribute before the object's turn comes round or land on the next one |
| Aug 2026 | ~~Dimension lists are closed and frozen~~ — **corrected.** They are additive-only, like everything else | Dimensions are independent and unspecified defaults to zero, so adding one breaks nothing and folds no Campaign differently. Cost is balance, not correctness: a late Dimension has no coverage in existing Guards |
| Aug 2026 | **Shaping** — ~~three~~ **two** forms: Bonus Points and Baseline | Bonus Points redistribute; a Baseline adds without taking. **Demand retired in the Phase 0 re-attack** — nothing asked for it, forcing a player to spend their own points somewhere is a strange thing to want, and it was the only form that had to be a percentage |
| Aug 2026 | Bonus Points cannot inflate; **Baselines can** | Redistribution is structurally safe. A Baseline raises total effect and therefore needs a ceiling of its own |
| Aug 2026 | Baselines take the **highest, never the sum** | Two sets of lockpicks do not stack. `max` is order-free, so any number of them stays deterministic |
| Aug 2026 | Shaping is snapshot only, never ambient | Direction is fixed at vector creation; keeping it fixed is what makes a placed vector a direction, four numbers and a pin |
| Aug 2026 | **Gear contributes its modifiers automatically, and visibly** | Nobody hunts an inventory for bonuses; every contribution appears as its own step in the animation. Automatic is only acceptable because it is visible |
| Aug 2026 | A Guard covering all Dimensions covers Dimensions invented later | Armour stopping the first 3 of everything keeps working forever. Only a Guard naming specific Dimensions misses a new one, which is correct rather than broken |
| Aug 2026 | Attempt Dimensions stay small by **design discipline**, not by engine rule | They are the interface the player sees. Eight Capacities is a choice; two hundred skills is a spreadsheet. A Component adds a Dimension only for a genuinely new axis of the world |
| Aug 2026 | Capacity is stated as a ceiling on the **total**, where 100% is no enhancement | Reads naturally for content authors: a lock is 100%, a good gun is 250% |
| Aug 2026 | Magnitude is **uncapped**; roughly under 10 / 50 / 100 across a campaign arc | Design guidance for playtesting, not an engine rule. Distinct from Scale, which is the log exponent on an Entity |
| Aug 2026 | Every Ruleset declares a **magnitude reference** | *A competent attempt at an ordinary task is about 5.* Gives content and CI something to check against instead of a silent mismatch |
| Aug 2026 | Attempts run the **whole** assembly pipeline | A *+50% at lockpicking* buff has a home, and the same animation shows a lockpick assembling as shows a fireball |
| Aug 2026 | A Threshold may be declared on the **total magnitude**, not only one Dimension | An outstanding lockpick may reveal what is inside the lock. The declaring object chooses the form |
| Aug 2026 | The **Resolution Record** is Substrate | It is what makes reflection possible without Listeners watching events, and it is where overflow lives and where every *why was it 17* is answered |
| Aug 2026 | Reflected and triggered vectors pin to a **later** Moment, never the current one | Bounds reflection loops by turn structure rather than by an engine limit |
| Aug 2026 | Vectors in a Packet stay distinct rather than merging directions | Same resolved numbers either way, but provenance survives, so rules keyed to a Channel by name remain possible |
| Aug 2026 | **Entry into Ordered time is base Ruleset's decision, not the Substrate's** | Three attempts at a Substrate rule each failed on a real case (strangers, self-targeting, healing an ally). It is a game-design rule wearing an engine costume |
| Aug 2026 | A scheduled vector holds Ordered time open only while it has a non-source anchor | An empty storm anchors to nobody, so it stops holding the table in turn order — falls out of the rule above rather than needing its own |
| Aug 2026 | `destroy` stays in the Verb set | Rare, and means removed from play entirely rather than killed |
| Aug 2026 | States live mostly in Components; the Substrate defines only their shape | Same treatment as Resources. A `max` is an optional field on a State definition |
| **Aug 2026 · Phase 0** | **An attempt's resolved value is `⌊points × magnitude ÷ total points⌋`** — one integer operation | Working the share first and multiplying loses magnitude and tells a different story: 6 points as 3/2/1 on a 12 gives 6/3/1 (total 10) one way and 6/4/2 (total 12) the other. Integer-first is exact, kills the apportionment paradox, and means an attempt's direction is stored as whole point counts rather than decimals |
| **Aug 2026 · Phase 0** | Truncation loss on a spread attempt is **the intended penalty** for attending to many things | Loss is always under `k`, so it is nothing on a big roll and total on a small one. It scales itself and needs no rule |
| **Aug 2026 · Phase 0** | **All-in dominance is answered by authoring, not by arithmetic** | With only `≥` bars, one point all-in is always at least as good as spreading. The authoring tool therefore requires every Threshold set to carry a downside bar; a live GM decides on the fly and is trusted, but the tool offers one by default rather than asking them to invent it. Instrumentation counts how many tasks ship with no downside bar, so playtesting measures this instead of guessing |
| **Aug 2026 · Phase 0** | **Enhancement Capacity clamps percentages. Absolutes are uncapped** | Absolutes cannot run away by stacking — they grow linearly in the number of contributors, and Participation Capacity already bounds contributors. Two directions of failure, two walls that fit them |
| **Aug 2026 · Phase 0** | Enhancement Capacity belongs to the **task or target**, never the source | A source-owned ceiling is shoppable: the party routes every vector through whoever holds the highest. Target-owned, it stays a property of a thing in the world |
| **Aug 2026 · Phase 0** | A **Baseline is a percentage**, so the percentage ceiling already covers it | No second Capacity, no second number on an item. Closes the longest-standing PENDING in Part 2C |
| **Aug 2026 · Phase 0** | **A universal flat Guard subtracts from the packet total and is redistributed**, not applied per Dimension | Per-Dimension subtraction made pure directions land 7 where an even three-way landed 1, at the same magnitude. That would have deleted the interior of every Dimension Space. Redistribution uses the same integer apportionment as Allocation Points — one mechanism, two uses |
| **Aug 2026 · Phase 0** | A **Dimension-named** flat Guard still acts on that Dimension alone | Universal flat Guards are generic toughness; named Guards are specific resistance. Both idioms survive and mean different things |
| **Aug 2026 · Phase 0** | A Guard **reduces toward zero and never past it** | Armour can stop harm; it can never turn harm into its opposite. Needed explicitly now that Dimension values are signed and redistributed |
| **Aug 2026 · Phase 0** | The **fire-elemental stack is a content decision, not a Substrate hole** | An Entity that keeps an aura on itself is a large ability and gets priced per creature. The Substrate reserves **R-780**, unbounded in v1, as insurance — reserving a slot is free, and needing one after Campaigns exist is an Edition break |
| **Aug 2026 · Phase 0** | **Three rounding sites, all truncating toward zero: R-400, R-750, R-1050** | The old claim that two fixed-point numbers are never multiplied was false — a proportional Guard is exactly that. CI fails on a fourth site |
| **Aug 2026 · Phase 0** | **Every truncation is a visible step** in the resolution expansion | Rounding is where a system quietly stops making sense to a player. It is never allowed to happen off-screen |
| **Aug 2026 · Phase 0** | Shaping order is **Bonus Points → Baseline**, permanently | They do not commute: Bonus-first gives 6/3/1, Baseline-first gives 10/3/1 on the same allocation. Arbitrary but declared |
| **Aug 2026 · Phase 0** | **Log-integers are never added** — compare and multiply only | Table lookup is lossy and lossy addition is not associative, which would break the same-Ledger-same-state promise. Sums happen in integers within one Scale |
| **Aug 2026 · Phase 0** | Cross-Scale conversion is `× 10^(source − target)`, truncated, at **R-750** | Ships as a default so the common case is free and nobody flattens the world to Scale 0 to avoid declaring rules |
| **Aug 2026 · Phase 0** | **Scale belongs to the part, not only to the whole** | The conversion rule alone makes a person unable to hurt a rowboat. A Scale-4 airship has Scale-1 doors and rigging; you do not punch the hull, you cut what a person can reach. This is what makes Scale usable instead of a wall |
| **Aug 2026 · Phase 0** | The ruleset is **a book delivered on the website** | Everything therefore has to be explainable in prose, which is a hard size limit on L29 and L4 |
| **Aug 2026 · re-attack** | **A flat Guard acts once per contributing source, not once per Moment** | Everything lands at the start of the target's turn, so one application per packet meant plate absorbed 3 whether one bandit swung or eight — 77 landing instead of 56. Each blow meets the armour, which is what armour does |
| **Aug 2026 · re-attack** | **Cancellation moved to R-1000**, after flat Guards and before proportional ones | Lets armour act per blow while keeping the fire elemental unchanged: a cold bolt of 8 still meets its own aura of 5 and combines to 3 before the temperature-positive Guard is consulted |
| **Aug 2026 · re-attack** | **Flat Guards are per source; proportional Guards act on the combined total** | A flat Guard is armour and meets each blow. A proportional Guard is what you are made of and applies to whatever is left. The split is the meaning |
| **Aug 2026 · re-attack** | **Restoration lands after every Guard and is never reduced by one** | Armour must not reduce healing. It also kills a free exploit — without the rule, delaying a heal one Moment was worth exactly the Guard's value. A deliberate exception; this pipeline earns exceptions by worked cases, not by symmetry |
| **Aug 2026 · re-attack** | *"Armour 3"* means **reduces any incoming packet by 3**, not *immune to 3 or less on any axis* | A poisoned blade that wounds you delivers its poison; heavy armour still stops the rider entirely. Authors need to know which promise they are buying |
| **Aug 2026 · re-attack** | **A consequence is graded by distance from the bar**, never by an absolute value below zero | Otherwise zero is a safe place to be: an axis you ignored would be protected from a bad failure while an axis you tried on and botched would not |
| **Aug 2026 · re-attack** | An attempt with **no points spent anywhere is not legal** | No direction, and nothing to divide by |
| **Aug 2026 · re-attack** | **Absolute modifiers are capped as a fraction of the magnitude reference**, CI-checked | Percentages are the big bounded lever; absolutes are small and pass the ceiling. That division only holds while absolutes stay small, so it is enforced rather than hoped for |
| **Aug 2026 · re-attack** | **One enhancement total, one ceiling, clamp** | 200% Capacity with a Baseline plus two helpers summing past it simply stops at 200%. Nothing to distribute, because the parts were summed before the clamp |
| **Aug 2026 · re-attack** | A **Baseline contributes the increase it caused**, not its face value | Baselining manipulation to 75% when you allocated 25% contributes 50, not 75 — the face value charges you twice for what you paid for yourself |
| **Aug 2026 · re-attack** | **Shaping is expressed in points, never percentages** | Points are what a player actually has. A percentage of 3 points is not always a whole number, and choosing how to round it is choosing an apportionment rule — the thing integer allocation removed |
| **Aug 2026 · re-attack** | **Demand is retired.** Shaping has two forms | Nothing in the design ever asked for it, forcing a player to spend their own points somewhere is a strange thing to want, and it was the only Shaping form that could not be stated in points. A cost belongs in the Budget, or as a Guard or State |
| **Aug 2026 · re-attack** | **Restoration is an ordinary vector resolving at R-1250** — *(amended at L22: it is a **positive direction** on the axis it restores, not a negative magnitude)* | Not an exception — a layer choice. Because it resolves after R-850 and R-1050, no Guard can reach it and it cannot cancel incoming harm, and both of those fall out rather than being written as rules. Which Dimension it uses is an L22 question |
| **Aug 2026 · L21** | **Four Dimension Spaces: physical, mental, social, attempt** | Psychic harm decided it — under three Spaces it has to be `vital`, which is not a body injury, or social pressure, which it is not either. Splitting `mental` out also moved `resolve` off social, which left social cleanly about standing and obligation |
| **Aug 2026 · L21** | **A Space limits a vector, never an ability** | One ability places as many vectors as it needs. A poisoned blade places a physical vector and a mental one; they resolve separately and neither cancels the other, which is right — armour should not blunt a hallucination. This is what makes four Spaces comfortable rather than restrictive |
| **Aug 2026 · L21** | **A vector's Space is decided by what it changes, not by what caused it** | Otherwise *is intimidation mental or social* gets answered differently every time and the whole thing drifts. Intimidating a man makes him afraid (mental) and makes the room see you as dangerous (social) — one action, two vectors |
| **Aug 2026 · L21** | Adding a Space later is **free**; splitting or merging existing ones is an **Edition break** | A new Space is purely additive because nothing existing interacts with it. Splitting stops things cancelling that used to; merging starts things cancelling that never did |
| **Aug 2026 · L21** | **If it is only true in some Settings, it is a Component. If it is true in all of them, it is base Ruleset. If the Substrate cannot function without it, it is a Socket** | Dylan's test, and the sharpest statement of the Substrate line so far. It generalises far beyond Spaces. *(Consciously overridden once, for `mystic` — see the row below)* |
| **Aug 2026 · L21** | **Dimension and Resource are two ends of one pipeline, not alternatives** | Anything that is a Dimension automatically has a Resource, because that is what Landing means. The real question is only whether something has a meaningful *opposite* that should cancel it before it lands — if yes it earns a Dimension and gets the Resource for free |
| **Aug 2026 · L29** | **The attempt Space is two layers: seven Domains, fifteen Dimensions** | A Domain is an *outcome*; its Dimensions are genuinely different *routes* to it. Two characters clear the same FORCE bar, one by `power` and one by `momentum`, without arguing which applies — athletics-versus-acrobatics solved structurally rather than by ruling |
| **Aug 2026 · L29** | **A Domain stores no number** | It is a label on a set of Dimensions. A bar set on a Domain reads the sum of its Dimensions at that moment and the sum is then gone. This forces leaf-first arithmetic rather than leaving it a choice |
| **Aug 2026 · L29** | **The Domain is not the player's choice; the route is** | Scion 2e's structure — the Storyguide sets the arena, the player picks the approach. It is the whole answer to *how does a newcomer know what to roll*: the fiction settles the hard half. FAE-style free choice of axis is the recorded failure mode of every system in this family |
| **Aug 2026 · L29** | At least one point must be spent in the named Domain — or in the named Dimension if the GM names one | The naming *is* the difficulty dial. A Domain bar is forgiving; a Dimension bar is hard, because the player must work out which route the situation wants |
| **Aug 2026 · L29** | **Three ceilings, not two: Enhancement, Attempt, Participant** | They bound different things — amplification, accumulated attention, and headcount. A 200% share budget still admits ten people at 20% each, so a share budget alone does not stop the crowd; only a participant count does. And a participant count alone does not stop three specialists going all-in |
| **Aug 2026 · L29** | **Attempt Capacity is measured in attention, not competence** | A master and a fumbler each consume the same budget at 100%. Space at the keyhole is space at the keyhole |
| **Aug 2026 · L29** | **A Threshold declares how it reads contributors: sum, highest or each** | Effort accumulates on a lock; one person spotting the needle is enough for everyone; a fear aura lands person by person. Without this the arithmetic produces nonsense in the first session |
| **Aug 2026 · L29** | **There is no *lowest* mode** | A weakest-link rule would mean more people makes a party less stealthy, and worse, it would teach players not to participate. Individual jeopardy is **each**, usually with Participant Capacity one |
| **Aug 2026 · L29** | **A Specialisation is a scoped narrowing of one Dimension, granting Bonus Points** | Reuses Shaping, so it cannot inflate. The field says keep such bonuses small and flat — nobody makes a specialisation a multiplier. Pathfinder 2e's rule is the only checkable one: strictly narrower than its Dimension, never a substitute for it |
| **Aug 2026 · L29** | **Magnitude stays open** — *a combination of modifiers and a dice roll* | Deliberately deferred until every list is filled and the real numbers can be seen. The list does not depend on it; every worked example does |
| **Aug 2026 · L21** | **A fifth Space: `mystic`** | Counterspelling decided it, exactly as psychic harm decided `mental` — a counterspell meets a spell and unmakes it, and no axis in the other four can host that. Dispelling, ward-breaking, severing a binding and draining power change neither a body, a mind, nor a standing |
| **Aug 2026 · L21** | **A working's effects live in whatever Space they change; the working's own existence lives in `mystic`** | Magical fire burns you in physical `temperature`, so armour and water help as much as against a torch. The spell taking hold and persisting is the mystic part. Two independent defences against one fireball — dispel it, or survive it — which settings have always had and no system models cleanly |
| **Aug 2026 · L21** | `mystic` **overrides the Component test, deliberately** | The test would make magic a Component, and a hard-science Setting genuinely has none. But an empty Space costs nothing, and if each magic Component published its own Space then a druid's working and a necromancer's could never meet. **The Space is infrastructure; the Channels are content.** Recorded as an override because a test quietly bent once gets bent silently forever after |
| **Aug 2026 · L22** | **Fourteen Dimensions across the four non-attempt Spaces** | physical: temperature, integrity, substance, vitality, vigor, mobility, acuity · mental: composure, clarity, will · social: regard, standing · mystic: working, essence. *(Amended from twelve when the Channel table exposed the sign problem and two missing axes.)* |
| **Aug 2026 · L22** | The test is **a meaningful opposite that cancels before landing** | If yes it earns a Dimension and gets a Resource free, because that is what Landing means. If no it is a Tag, a State, or a Resource moved by Verbs |
| **Aug 2026 · L22** | The anti-test: **a Dimension whose opposite side you cannot describe is not a Dimension** | `piercing` has no opposite — it is a Channel positioned mostly on `integrity`. `holy`'s only opposite is `unholy`, which is the same axis |
| **Aug 2026 · L22** | `vital` negative is **mending in flight**, which is not the same as healing | A regeneration aura meets incoming poison at R-1000; restoration resolves at R-1250. **Wards and regeneration cancel; healing restores.** Settings have always drawn this line without being able to say why |
| **Aug 2026 · L22** | **A social Dimension is broadcast; a per-pair state is a Connection** | `trust` passes the opposite test and is still not a Dimension, because trust is inherently A-toward-B. That discriminator keeps the social Space from absorbing Relationships |
| **Aug 2026 · L22** | `will` is distinct from `clarity` | Being dominated is not being confused — you are perfectly lucid and cannot stop. Afraid, confused and controlled are three different bad nights |
| **Aug 2026 · L22** | These are **expected to move** once items, characters and magic systems are written | Additive-only makes adding free at that point. What stays expensive is discovering one of these was really two, which is why the list is short |
| **Aug 2026 · L22 amend** | **The sign convention: every Dimension is a property of the target; negative means less of it** | The first draft pointed physical axes one way and the rest the other, so `kinetic +5 / clarity −5` was two harms with opposite signs. Now you can read what a Channel does from its signs alone — only 3 of 88 are mixed, and each is a genuine trade |
| **Aug 2026 · L22 amend** | Four axes renamed: `thermal`→**`temperature`**, `kinetic`→**`integrity`**, `corrosive`→**`substance`**, `vital`→**`vitality`** | Each had been named for the harm that arrives rather than the property that is lost. Force *takes* integrity away, so − is the harm direction |
| **Aug 2026 · L22 amend** | Two axes added: **`mobility`** and **`acuity`** | Slow, haste, entangle, root, blind, deafen and numb had no axis at all and would have had to be faked as States. Found by building the Channel table, which is the point of building it |
| **Aug 2026 · L22 amend** | **`temperature` and `working` are bipolar**; the other twelve are signed | Heat and cold both harm; a blessing and a curse both impose a working. Everywhere else, negative is the harm direction |
| **Aug 2026 · L23** | **A Channel positions over every Dimension, not within one Space** | Fatigue tires body and spirit; poison sickens and clouds; a concussion breaks and rattles. None was writable when a Channel lived in one Space |
| **Aug 2026 · L23** | The sum spans all Spaces — **breadth means thin** | The alternative, *100% to every Space it touches*, makes breadth free and every multi-Space Channel strictly better at the same magnitude. Nothing is lost: 50/50 at magnitude 20 equals 100%/100% at magnitude 10, with the doubling visible in the number |
| **Aug 2026 · L23** | **A Channel's components must all land on the same target** | Intimidation frightens *him* and raises *you* in the room — two targets, so one ability placing two vectors, never one Channel |
| **Aug 2026 · L23** | **Positions are integers in hundredths**, summing in absolute value to 100 | No decimals anywhere in a Channel, and "percent" is a word every player already knows |
| **Aug 2026 · L23** | **No two Channels may share a position** — CI rejects it | Identical coordinates mean identical Channels. This is D&D's force-versus-thunder problem made mechanically detectable, which no other system in the field can do |
| **Aug 2026 · L23** | **Every Dimension must be used on both signs** | Otherwise an axis dies because nothing points at it — how one published bestiary ended with a quarter of monsters immune to poison and almost nothing resisting force |
| **Aug 2026 · L23** | **Conditions are not Channels** | Silence, invisibility, aging and knockback are States, Tags, Place and Scale. Five unrelated published systems reached this independently, and mixing them is what produces the dead type |
