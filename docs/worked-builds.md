# Twenty things, built from the model

*August 2026, at the close of Phase 1. Every build below uses only the eight universal fields, the nine Categories and the four Noun kinds. Nothing is invented along the way.*

**These exist to be attacked.** A data model looks complete until you put something in it, so the way to find out whether this one is sufficient is to build things and watch for four failures:

| Signal | What it means |
|---|---|
| A build needs a field that isn't there | incomplete — **additive**, cheap to fix |
| A build hides something in `facets` that another Component must read | **wrong** — a Noun slot is missing |
| Two builds express one idea differently | **ambiguous** — content will diverge |
| A build needs a shape the Verb set can't produce | **structural** — expensive, window closes at launch |

`—` means the field is genuinely absent, which under rule 8b is not zero and not empty-by-default but explicitly nothing.

---

## People, ships, factions

### 1 · Kira Vance — a person

```
id           #4471
category     Creature
tags         living · sapient · humanoid · tangible · portable
scale        1
links        member_of #3300 (Ashfall Company) · member_of #4102 (Bren's party)
             carried_by — · inside #7702 (The Drowned Crow)
capacities   power 3 · momentum 1 · control 5 · timing 2 · agility 4 · pace 2
             senses 2 · study 1 · appeal 1 · pressure 3 · bargain 2
             stealth 4 · deceit 2 · grit 3 · focus 2
tracks       vitality 18/22 · vigor 9/11 · mobility 6/6 · acuity 5/5
             composure 7/9 · clarity 8/8 · will 6/7 · temperature 0 (temperate)
             integrity 12/12 · substance 10/10 · doubloons 44/60
facets       { progression, place, inventory }
```

**No initiative, no carrying capacity, no movement speed, no level.** Those are the four person-assumptions that leak into every generic system; each is a Capacity, a Tag magnitude, or a Component's Facet.

**She is in two groups at once**, which is what `links` exists for. Composition would not allow it; membership does.

### 2 · The Gull — a ship, with parts

```
THE GULL                              THE GULL'S HELM DOOR
id      #9012                         id      #9014
category Item · Place                 category Item
tags    manufactured · tangible       tags    manufactured · tangible · portal
        vehicle · container           scale   1        ← ITS OWN, copied at creation
scale   4                             links   part_of #9012   ← the link lives HERE
capacities power 6 · pace 5           tags    locked
tracks  integrity 40/40               tracks  integrity 8/8
        substance 40/40 · temperature 0       substance 6/6
```

**This is the build that tests rule 18.** A person-scale attack on the door resolves entirely at Scale 1 and never touches the ship's Scale-4 integrity. No published system has a rule for this; here it falls out of two fields.

**The Gull carries `Item` and `Place` and `Creature`-less Capacities** — it can attempt (power, pace) without being a Creature, because nothing gates attempting. Add `Creature` only if it should act on its own.

### 3 · The Crimson Hand — a faction

```
id           #3300
category     Group · Creature
tags         organisation
scale        3                        ← Tier. Not tangible. Still scaled.
capacities   pressure 4 · bargain 5 · deceit 3
tracks       standing 6/9 · vitality 8/10 (cohesion)
facets       { place: { turf: [zone-3, zone-9] } }
```

**Proof that `scale` is not gated on tangibility.** No `tangible` Tag, a location that is a list of turf, and a Scale that means influence. Blades and Fate both do exactly this.

---

## The four-way test cases

### 4 · "The Duke poisoned his brother" — a rumour

```
id #7781 · category Notion · tags claim · scale — (genuinely absent)
links part_of #7780 (a larger body of lore)
tracks standing 3/10 (how widely believed)
```

### 5 · The postern lock

```
id #9016 · category Item · tags manufactured · tangible · mechanism · locked
scale 1 · links part_of #9014 (the door, which is part of the ship)
capacities grit 6        ← its Threshold for being picked
tracks integrity 3/3
```

A three-deep chain — lock in door in ship — and the Fold derives ancestry from three `part_of` links.

### 6 · The storm off Cape Mor

```
id #5522 · category Phenomenon · tags tangible · weather · scale 5
tracks vigor 14/14 (how long it can last)
facets { place: { covers: [zone-14, zone-15] }, emits: standing vector }
```

No mass, no `portable`. Targetable, and it has Scale.

---

## The hard cases

### 7 · A ghost that materialises

```
BEFORE  tags  spirit                AFTER   tags  spirit · tangible
```

**This is the case that killed `Tangible` as a Category.** A Category is permanent under rule 6; a Tag is added and removed by a Verb. One field write instead of two Entities and a hand-off.

### 8 · A hole in the hull

```
id #9021 · category Place · tags breach     ← NOT tangible; it is an absence
scale 1 · links part_of #9012
```

BFO calls this a *site*: immaterial and fully located. It works **only because `location` is not gated on tangibility** — which was the decisive argument against the Category.

### 9 · A crowd, and the constraint it exposes

```
THE MOB                    A PERSON IN IT
id #4800                   links  member_of #4800  ← MEMBERSHIP, not composition
category Group · Creature         member_of #3300  ← and she can be in both
tags organisation · tangible
scale 3
```

**Under the old `part_of`-only model this was impossible** — one whole per part. `links` is exactly why: a door is *part of* a ship, a person is *member of* a mob, and those are different relations with different cardinality.

### 10 · A fire

```
id #5600 · category Phenomenon · tags tangible · hazard · scale 2
links part_of #4900 (the building it burns in)
tracks vigor 12/12 (its fuel) · temperature +6
facets { emits: standing vector — temperature +6, scope: this Place }
```

**It works because standing vectors already exist.** A curse, a plague and a blizzard are the same shape. This was flagged as a possible Substrate finding and is not one.

### 11 · Kira's regard for Bren

```
id #6120 · category Relationship
connections [ { holder #4471, about #6199, tracks: { regard 7/9 } } ]
```

**One Connection, Kira's stance only.** Bren's is a separate Connection with its own value, and neither can be inferred from the other. If Bren dies, Kira's Connection survives and still names him — people remember the dead.

### 12 · A pending arrow

```
category Vector · direction pierce · magnitude 14 · target #4471
pin turn start(#4471, round 12) · layer R-700 · class Direct
```

Targetable while pending — which is what makes `interrupt` work, and what made `pending` unnecessary as a timing.

### 13 · A shattered sword, and a retracted one

```
SHATTERED — a band on a Track       RETRACTED — no Entity at all
id #8800 · category Item            the creation Record is retracted;
tracks integrity 0/12  (ruined)     the Fold never produces it.
                                    No field, no default, no predicate.
```

**The two behave completely differently, which is the point.** A Listener watching `integrity` in the *ruined* band fires for the first and cannot fire for the second, because there is nothing to watch.

### 14 · A vase, and why it cannot be frightened

```
id #7400 · category Item · tags mineral · tangible · portable
tracks integrity 4/4 · substance 4/4 · temperature 0
```

**No `composure`, no `will`, no `clarity`.** Throw fear at it: the vector resolves perfectly normally, the magnitude is real, and Landing has nowhere to put it. **The data not being there *is* the immunity.**

And a Channel at `integrity −70 / composure −30` lands seventy and drops thirty — so a broad Channel is naturally weaker against a narrow target, and nothing had to say so.

---

## Six more, compressed

| | The build |
|---|---|
| **15 · A room** | `Place` · `tags enclosure · tangible` · `scale 2` · `part_of` the building · `tracks temperature` |
| **16 · A debt** | `Notion` · `tags obligation` · no scale · `tracks standing` · plus a `Relationship` naming creditor and debtor |
| **17 · A law of the city** | `Notion` · `tags statute` · a Listener declared in its Facet · no scale, no harm pipeline |
| **18 · A trade route** | `Relationship` with two Connections, each holding its own view of the terms |
| **19 · A disease** | `Phenomenon` · `part_of` its host · `tracks vigor` (virulence) · a standing vector, like the fire |
| **20 · A GM's pending ruling** | `Proposal` · decider `Person` · Moment = end of round · default = the safer outcome |

---

## What twenty builds say

**No build needed a field that does not exist.** The three that looked most dangerous going in — the ghost, the hole, the fire — all worked, and each worked because of a decision made for a *different* reason: Tags being mutable, `location` not being gated on matter, and standing vectors already existing.

**Where it is thin, honestly:**

1. **`links` cardinality will be argued about.** `part_of` is exclusive and cascades; `member_of` is not. The first time an author wants a thing structurally inside two wholes, the answer is *one of those is a Relationship* — and that answer will need saying repeatedly.
2. **Standing vectors are load-bearing and barely tested.** Builds 10 and 19 both lean on them. If one needs a field outside the uniform Verb shape, that is a structural finding and everything stops.
3. **`facets` is where the model can rot.** Anything a Component puts there that another Component must read is a missing Noun slot in disguise. Watch for it in every review.
4. **Nine Categories may be too few or too many**, and playtest is what will say. The six Ruleset ones are versionable; only `Vector`, `Proposal` and `Relationship` are frozen.
