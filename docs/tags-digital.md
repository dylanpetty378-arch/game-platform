Harvested ~41 sources. Here is the compilation.

---

# MASTER LIST — machine-readable tags / keywords / properties in digital games

Column key: **Value?** = does the tag carry a number/enum, or is it a bare boolean membership flag.

---

## 1. Material and substance

| Tag name | Carries a value? | Where it comes from | What reads it |
|---|---|---|---|
| `IS_METAL` · `metal` · `sand_metal` · `Metallic` (StuffCategory) | no | Dwarf Fortress, Minecraft Bedrock, Noita, RimWorld | forging recipes, conductivity, sound set |
| `IS_STONE` · `stone` · `Stony` · `rock` · `base_stone_overworld` / `base_stone_nether` | no | DF, MC Bedrock, RimWorld, MC Java | mining, construction legality |
| `IS_GLASS` · `CRYSTAL_GLASSABLE` · `glass` | no | DF | crafting station eligibility, shatter behaviour |
| `IS_GEM` · `IS_CERAMIC` | no | DF | cut/encrust jobs |
| `WOOD` · `logs` · `logs_that_burn` · `planks` · `wood` · `Woody` · `log` | no | DF, MC Java, MC Bedrock, RimWorld | axe mining, burning, plank crafting |
| `LEATHER` · `Leathery` · `ITEMS_LEATHER` · `ArmorMaterialLeather` | no | DF, RimWorld, Skyrim | tanning, apparel construction |
| `THREAD_PLANT` · `YARN` · `SILK` · `Fabric` · `wool` · `wool_carpets` | no | DF, RimWorld, MC Java | weaving, flammability, dye |
| `BONE` · `TOOTH` · `HORN` · `SHELL` · `PEARL` · `HAIR` · `NAIL` · `SCALE` (`ITEMS_SCALED`) | no | DF | butchery products, crafting material class |
| `SOAP` · `ALCOHOL` · `POWDER_MISC_PLANT` · `DEADLY_DUST` | no | DF | hospital cleaning, drink, contaminant spread |
| `material` (free text: leather, wool, cotton, paper) | yes — string | schema.org/Product | product faceting |
| `Steel` · `Plasteel` · `Uranium` · `Silver` · `Gold` · `Jade` · `Obsidian` · `Bioferrite` · `Granite` · `Marble` · `Limestone` · `Sandstone` · `Slate` · `Vacstone` | yes — carries a whole stat-multiplier block | RimWorld "stuff" | every stat on the made item |
| `Cloth` · `Devilstrand` · `Hyperweave` · `Synthread` · `Alpaca/Bison/Megasloth/Muffalo/Sheep/Mastodon/Muskox wool` | yes — stat block | RimWorld | insulation, beauty, flammability |
| `Plainleather` · `Lightleather` · `Patchleather` · `Bearskin` · `Birdskin` · `Bluefur` · `Camelhide` · `Chinchilla fur` · `Dog leather` · `Elephant leather` · `Foxfur` · `Heavy fur` · `Human leather` · `Lizardskin` · `Panthera fur` · `Pigskin` · `Rhinoceros leather` · `Thrumbofur` · `Thrumbomane` · `Wolfskin` · `Dread leather` · `Sealskin` · `Mink fur` | yes — stat block | RimWorld | armour rating, insulation, market value |
| `ArmorMaterialIron/Steel/SteelPlate/Leather/Hide/Studded/Scaled/Elven/ElvenGilded/Glass/Dwarven/Orcish/Ebony/Daedric/Dragonplate/Dragonscale/Falmer/Blades/Forsworn/Stormcloak/ThievesGuild/Penitus/Imperial{Heavy,Light,Studded}` | no | Skyrim KYWD | smithing perks, tempering, matched-set perks |
| `DLC2ArmorMaterial{BonemoldHeavy,BonemoldLight,ChitinHeavy,ChitinLight,NordicHeavy,NordicLight,StalhrimHeavy,StalhrimLight,MoragTong}` · `DLC1ArmorMaterial{Dawnguard,Hunter,Vampire,FalmerHardened,FalmerHeavy}` | no | Skyrim KYWD | same |
| `WeapMaterial{Iron,Steel,Silver,Wood,Imperial,Elven,Glass,Dwarven,Orcish,Ebony,Daedric,Draugr,DraugrHoned,Falmer,FalmerHoned}` · `DLC1WeapMaterialDragonbone` · `DLC2WeaponMaterial{Nordic,Stalhrim}` | no | Skyrim KYWD | smithing, silver-vs-undead bonus |
| `ma_*` (material-swap keyword prefix) | no | Fallout 4 / AWKCR | material swap + crafting menu |
| `dirt` · `sand` · `gravel` · `grass` · `grass_blocks` · `ice` · `snow` · `concrete` · `concrete_powders` · `terracotta` · `glazed_terracotta` · `stone_bricks` · `copper` · `coals` | no | Minecraft Java/Bedrock block+item tags | tool matching, generation, recipes |
| `acacia` · `birch` · `oak` · `dark_oak` · `spruce` · `jungle` · `cherry_logs` · `crimson_stems` · `bamboo_blocks` | no | Minecraft (per-wood-species tags) | recipe substitution |
| Noita substance tags: `water` · `blood` · `acid` · `lava` · `oil`-class via `flammable`, `slime` · `snow` · `ice` · `sand_ground` · `sand_other` · `earth` · `meat` · `plant` · `fungus` · `gold` · `molten_metal` · `rust` · `rust_oxide` · `alchemy` | no | Noita `materials.xml` | reaction table, world sim |

---

## 2. Physical properties

| Tag name | Carries a value? | Where it comes from | What reads it |
|---|---|---|---|
| `Mass` · `weight` · `density` · `SOLID_DENSITY` · `LIQUID_DENSITY` · `MOLAR_MASS` | yes — mass / kg·m⁻³ | RimWorld, schema.org, Unreal `density`, DF, Noita `density` | carry limits, buoyancy, physics mass, throw arcs |
| `Flammability` · `FLAMMABLE` · `burnable` · `burnable_fast` · `flammable` · `logs_that_burn` · `IGNITE_POINT` · `autoignition_temperature` · `fire_hp` | yes (RimWorld ×factor; DF/Noita temperature or HP) | RimWorld, DF, Noita, Minecraft | fire spread, burn-down time |
| `MELTING_POINT` · `BOILING_POINT` · `HEATDAM_POINT` · `COLDDAM_POINT` · `MAT_FIXED_TEMP` · `SPEC_HEAT` | yes — temperature units | Dwarf Fortress | phase change, heat damage, magma-safety |
| `meltable` · `meltable_metal` · `meltable_by_fire` · `meltable_to_water/lava/acid/blood/poison/slime/radioactive/cold` · `molten` · `freezable` · `frozen` · `evaporable` · `evaporable_by_fire` · `vapour` · `soluble` | no (target material implied by tag name) | Noita | material reaction table |
| `IMPACT_YIELD` · `IMPACT_FRACTURE` · `IMPACT_STRAIN_AT_YIELD` | yes — kPa / strain | Dwarf Fortress | blunt combat resolution |
| `COMPRESSIVE_YIELD/FRACTURE/STRAIN_AT_YIELD` · `TENSILE_*` · `SHEAR_*` · `TORSION_*` · `BENDING_*` | yes — kPa / strain | Dwarf Fortress | edged/blunt wound model, item breakage |
| `MAX_EDGE` | yes — integer sharpness | Dwarf Fortress | cutting power of a weapon |
| `Tensile Strength` · `Compression Strength` · `Shear Strength` | yes | Unreal (chaos/destruction physical material) | fracture simulation |
| `durability` · `hp` · `crackability` · `MaxHitPoints` · `Destructible Damage Threshold Scale` | yes — integer | Noita, RimWorld, Unreal | what can dig/break it |
| `hardness` proxies: `needs_stone_tool` · `needs_iron_tool` · `needs_diamond_tool` · `incorrect_for_{wooden,stone,iron,gold,diamond,copper,netherite}_tool` · `diamond_pick_diggable` · `*_tier_destructible` | no | Minecraft Java + Bedrock | drop-vs-no-drop, mining speed |
| `Dynamic Friction` · `Static Friction` · `friction` · `static_friction` · `solid_friction` · `slippery` · `rough` | yes — 0..1 | Unity, Unreal, Godot, Noita | sliding, movement |
| `Bounciness` · `Restitution` · `bounce` · `solid_restitution` | yes — 0..1 | Unity, Unreal, Godot, Noita | rebound |
| `Friction Combine` · `Bounce Combine` (`Average`, `Minimum`, `Maximum`, `Multiply`) · `absorbent` | yes — enum | Unity, Unreal, Godot | pairwise material resolution |
| `Sleep Linear Velocity Threshold` · `Sleep Angular Velocity Threshold` · `Sleep Counter Threshold` · `Raise Mass To Power` | yes | Unreal | solver sleep, mass scaling |
| `electrical_conductivity` · `conductive` (Noita solids class) · `EMP Resistance` | yes / no | Noita, RimWorld | lightning chaining, EMP |
| `ABSORPTION` | yes | Dwarf Fortress | contaminant/liquid soaking |
| `liquid_gravity` · `liquid_viscosity` · `liquid_damping` · `liquid_flow_speed` · `liquid_sticks_to_ceiling` · `liquid_sand` · `liquid_static` · `gas_speed` · `gas_upwards_speed` · `solid_gravity_scale` | yes | Noita | falling-sand simulation |
| `Insulation_Cold` · `Insulation_Heat` · `Minimum/Maximum Comfortable Temperature` · `Survival_ArmorWarm` / `Survival_ArmorCold` | yes — °C | RimWorld, Skyrim SE Survival | temperature comfort |
| `impermeable` · `blockWind` · `blockLight` · `fillPercent` · `passability` · `pathCost` | yes / no | Minecraft, RimWorld ThingDef | pathing, water flow, cover |
| `climbable` · `soul_speed_blocks` · `unstable_bottom_center` · `does_not_block_hoppers` · `one_way_collidable` | no | Minecraft | movement + physics interaction |
| `UNDIGGABLE` · `indestructible` · `dragon_immune` · `wither_immune` · `blocks_wind_charge_explosions` | no | DF, Noita, Minecraft | destruction immunity |
| `ROTS` · `DeteriorationRate` · `Rotting` · `Decayed` · `lifetime` | yes (rate) / no | DF, RimWorld, Noita | spoilage over time |
| `EVAPORATES` · `requires_oxygen` / `requires_air` | no | DF, Noita | ambient state dependence |
| `width` · `height` · `depth` · `size` · `hasMeasurement` | yes | schema.org/Product | display, packing |

---

## 3. Form and construction

| Tag name | Carries a value? | Where it comes from | What reads it |
|---|---|---|---|
| `ITEMS_HARD` · `ITEMS_METAL` · `ITEMS_SOFT` · `ITEMS_BARRED` · `ITEMS_SCALED` · `ITEMS_LEATHER` | no | Dwarf Fortress | which item forms this material may take |
| `ITEMS_WEAPON` · `ITEMS_WEAPON_RANGED` · `ITEMS_ARMOR` · `ITEMS_ANVIL` · `ITEMS_AMMO` · `ITEMS_DIGGER` · `ITEMS_DELICATE` · `ITEMS_SIEGE_ENGINE` · `ITEMS_QUERN` | no | Dwarf Fortress | reaction/job eligibility |
| Minecraft shape tags: `slabs` · `stairs` · `walls` · `fences` · `fence_gates` · `doors` · `trapdoors` · `buttons` · `pressure_plates` · `beds` · `banners` · `signs` · `hanging_signs` · `lanterns` · `candles` · `chains` · `bars` · `rail` · `bundles` · `cushions` | no | Minecraft Java/Bedrock | recipe families, redstone behaviour |
| Wooden-form tags: `wooden_buttons` · `wooden_doors` · `wooden_fences` · `wooden_pressure_plates` · `wooden_slabs` · `wooden_stairs` · `wooden_trapdoors` · `wool_slabs` · `wool_stairs` · `concrete_slabs` · `concrete_stairs` | no | Minecraft | material×form cross product |
| PoE item classes: `One Hand Axes` · `Two Hand Axes` · `One Hand Maces` · `Two Hand Maces` · `One Hand Swords` · `Two Hand Swords` · `Thrusting One Hand Swords` · `Daggers` · `Rune Daggers` · `Claws` · `Bows` · `Wands` · `Sceptres` · `Staves` · `Warstaves` · `Fishing Rods` | no | Path of Exile | which mods can roll; which skills work |
| PoE armour classes: `Body Armours` · `Helmets` · `Gloves` · `Boots` · `Shields` · `Quivers` · `Belts` · `Rings` · `Amulets` · `Jewels` · `Abyss Jewels` · `Life Flasks` · `Mana Flasks` · `Hybrid Flasks` · `Utility Flasks` · `Tinctures` · `Charms` · `Trinkets` · `Relics` | no | Path of Exile | slot legality, mod pool |
| PoE spawn-weight tags: `one_hand_weapon` · `two_hand_weapon` · `weapon` · `armour` · `wand` · `staff` · `dagger` · `sceptre` · `shield` · `ring` · `amulet` · `belt` · `body_armour` · `str_armour` · `dex_armour` · `int_armour` (+ hybrid `str_dex_/str_int_/dex_int_`) · `attack_staff` · `attack_dagger` · `caster_unique_weapon` · `weapon_can_roll_minion_modifiers` · `top_tier_base_item_type` · `default` | yes — an integer spawn weight per tag | Path of Exile mod tables | affix generation weighting |
| `WeapType{Sword,Katana,Rapier,Scimitar,CurvedSword,CurvedGreatsword,Twinblade,Spear,Pike,Halberd,Javelin,Scythe,QuarterStaff,Whip,Claw,Cestus,Gun}` | no | Skyrim KYWD (incl. community) | animation set, perk gating |
| `ArmorHeavy` · `ArmorLight` · `ArmorCuirass` · `ArmorGauntlets` · `ArmorBoots` · `ArmorHelmet` · `ArmorShield` | no | Skyrim KYWD | skill attribution, perk checks |
| Minecraft armour-slot tags: `head_armor` · `chest_armor` · `leg_armor` · `foot_armor` · `harnesses` · `freeze_immune_wearables` | no | Minecraft item tags | equip slot |
| Tool-class tags: `swords` · `axes` · `pickaxes` · `shovels` · `hoes` · `tools` · `is_{hatchet,hoe,mace,pickaxe,shears,shovel,sword}_item_destructible` | no | Minecraft Java + Bedrock | tool matching |
| `bodyPartGroups` · `apparel layers` (`OnSkin`, `Middle`, `Shell`, `Overhead`, `EyeCover`, `Belt`) | yes — enum list | RimWorld ThingDef | apparel stacking legality |
| `_ClothesSlotBelt` · `_ClothesSlotEyewear` · `_ClothesSlot_Ring` · `ap_*` (attach point) · `ap_Melee_Material` · `ap_Gun_Caliber` | no | Fallout 4 / AWKCR | slot conflicts, mod attach points |
| `Colossal` · `Magnetic` · `Starship` · `Location` (card *form* types) | no | Hearthstone | zone legality, attachment |
| `pattern` · `color` · `model` · `sku` · `gtin` | yes — string | schema.org/Product | catalogue identity |

---

## 4. Handling and use

| Tag name | Carries a value? | Where it comes from | What reads it |
|---|---|---|---|
| `mineable/axe` · `mineable/pickaxe` · `mineable/shovel` · `mineable/hoe` · `wood_pick_diggable` · `stone_pick_diggable` · `iron_pick_diggable` · `gold_pick_diggable` · `diamond_pick_diggable` | no | Minecraft Java + Bedrock | tool speed and drop legality |
| `enchantable/armor` · `/bow` · `/crossbow` · `/durability` · `/equippable` · `/fire_aspect` · `/fishing` · `/mace` · `/melee_weapon` · `/mining` · `/mining_loot` · `/sharp_weapon` · `/sweeping` · `/trident` · `/vanishing` · `/weapon` · `/lunge` (+ per-slot variants) | no | Minecraft item tags | which enchantments may apply |
| `repairs_{copper,chain,diamond,gold,iron,leather,netherite}_armor` · `repairs_turtle_helmet` · `repairs_wolf_armor` | no | Minecraft | anvil repair materials |
| `brewing_fuel` · `brewing_potion_inputs` · `beacon_payment_items` · `furnace_minecart_fuel` · `bookshelf_books` · `lectern_books` · `book_cloning_target` · `clonable_maps` · `extendable_maps` · `decorated_pot_ingredients` · `decorated_pot_sherds` · `breaks_decorated_pots` · `cauldron_can_remove_dye` · `dyes` · `creeper_igniters` · `douses_campfires` · `duplicates_allays` | no | Minecraft item tags | station/interaction eligibility |
| `beacon_base_blocks` · `enderman_holdable` · `valid_spawn` · `bee_growables` · `guarded_by_piglins` · `mob_interactable_doors` · `sculk_replaceable` · `replaceable` · `not_feature_replaceable` · `fertilize_area` · `mob_spawner` · `text_sign` | no | Minecraft Java + Bedrock | system-specific behaviour |
| `EQUIPS` · `CANOPENDOORS` · `LOCKPICKER` · `Minimum Handling Skill` · `Equip Delay` | no / yes | Dwarf Fortress, RimWorld | who may use it |
| `MagicDisallowEnchanting` · `weaponTags` · `tradeTags` · `Recipe Filter` (keyword type) | no | Skyrim, RimWorld, Fallout 4 | crafting-menu membership |
| `Timing`-like use windows: `Burst` · `Fast` · `Slow` · `Focus` | no | Legends of Runeterra spell speed | when a card may be played/responded to |
| `Combo` · `Tradeable` · `Forge` · `Echo` · `Twinspell` · `Casts When Drawn` · `Summoned When Drawn` · `Temporary` · `Passive` · `Quickdraw` · `Prepare` · `Rewind` | no | Hearthstone | play-time legality/cost modification |
| `Exhaust` · `Ethereal` · `Innate` · `Retain` · `Unplayable` · `Fleeting` · `Ephemeral` | no | Slay the Spire, Legends of Runeterra | card lifetime in hand/play |
| `Channelling` · `Trigger` · `Vaal` · `Support` · `Blink` · `Stance` · `Reservation` | no | Path of Exile gem tags | how a skill is activated / sustained |
| `Timing`: `own` / `any` / `respond` / `interrupt` analogues — `Secret`, `Battlecry`, `Deathrattle`, `Last Breath`, `Spellburst`, `Outcast`, `Frenzy`, `Honorable Kill`, `Overkill`, `Start of Game`, `Finale`, `Manathirst` | no | Hearthstone, LoR | trigger window |
| `EDIBLE_RAW` · `EDIBLE_COOKED` · `EDIBLE_VERMIN` · `food` · `foodType` · `preferability` · `Nutrition` · `Max Nutrition` · `Raw Nutrition Multiplier` | no / yes | DF, Noita, Minecraft, RimWorld | consumption legality and value |
| Food-target tags: `axolotl_food` · `armadillo_food` · `bee_food` · `camel_food` · `cat_food` · `chicken_food` · `cow_food` · `fox_food` · `frog_food` · `goat_food` · `hoglin_food` · `horse_food` · `llama_food` · `piglin_loved` · `ignored_by_piglin_babies` · `happy_ghast_food` | no | Minecraft item tags | breeding, taming, tempting |
| `WorkToBuild` / `Work To Make` · `Construction Speed (Material Factor)` · `WorkToMake` factor | yes — work units | RimWorld | job duration |
| `Move Speed` · `Carrying Capacity` · `Attack Speed` · `Cooldown Reduction` · `Resource Cost Reduction` | yes | RimWorld, Diablo 4 | action economy |

---

## 5. Condition, quality and durability

| Tag name | Carries a value? | Where it comes from | What reads it |
|---|---|---|---|
| `MaxHitPoints` · `useHitPoints` · `hp` · `Total Armor` · `Armor` | yes | RimWorld, Noita, Diablo 4 | destruction threshold |
| `Quality` · `Item Level` · `Sockets` · `Links` · `Requirements` | yes — integer | Path of Exile | mod tiers, equip legality |
| `Normal` · `Magic` · `Rare` · `Unique` | no — ordinal enum | Path of Exile rarity | affix count, display |
| `Identified` / `Unidentified` · `Corrupted` · `Mirrored` · `Split` | no | Path of Exile | modification legality |
| `Awful` · `Poor` · `Normal` · `Good` · `Excellent` · `Masterwork` · `Legendary` | no — ordinal | RimWorld quality | stat multipliers, beauty |
| `DeteriorationRate` · `Deterioration` · `Decayed` · `Rotting` · `Rotted` · `ROTS` | yes — rate | RimWorld, DF | passive decay tick |
| `Barrier` · `Block` · `Overshield` · `Divine Shield` · `SpellShield` · `Woven Mail` · `Frost Armor` · `Plated Armor` · `Buffer` · `Artifact` · `Intangible` · `Immune` · `Tough` · `Formidable` | yes (most carry a stack count) | StS, Hearthstone, LoR, Destiny 2 | pre-damage mitigation, effect negation |
| `Vulnerable` · `Weak` · `Frail` · `Weakened` · `Sundered` · `Brittle` · `Sap` · `Scorch` · `Shock` · `Chill` | yes — magnitude/stacks | Slay the Spire, PoE, Warframe | damage/defence multipliers |
| `Fortified` · `Fortify` · `Vigor` · `Strength` · `Dexterity` · `Focus` · `Regen` · `Regeneration` · `Restoration` · `Cure` | yes — stacks | Diablo 4, PoE, StS, LoR, Destiny 2 | outgoing/incoming modifiers |
| `Injured` · `Healthy` · `Burning` · `Chilled` · `Frozen` · `Stunned` · `Slowed` · `Immobilized` · `Dazed` · `Feared` · `Taunted` · `Tethered` · `Knockback` · `Crowd Controlled` | no — condition membership | Diablo 4 affix conditions | conditional damage bonuses |
| `Beauty` · `Outdoor Beauty` · `Cleanliness` · `Comfort` · `Style Dominance` · `Filth Rate` · `Filth Multiplier` | yes — signed integer | RimWorld | mood/thought calculation |
| `MarketValue` · `Market Value Ignoring Hitpoints` · `Sell Price Multiplier` · `Honor Value` | yes | RimWorld | trade pricing |
| `stainable` · `liquid_stains` · `stickyness` · `on_fire` | yes / no | Noita | surface state carried on entities |

---

## 6. Detectability and emission

| Tag name | Carries a value? | Where it comes from | What reads it |
|---|---|---|---|
| `LIGHT_GEN` · `gfx_glow` · `gfx_glow_color` · `light emission level` | yes — intensity / colour | DF, Noita, Minecraft block property | lighting, visibility |
| `MAGMA_VISION` · `EXTRAVISION` · `blockLight` · `castEdgeShadows` | no | DF, RimWorld ThingDef | line of sight, shadow casting |
| `vibrations` (56 events) · `warden_can_listen` · `allay_can_listen` · `shrieker_can_listen` · `ignore_vibrations_sneaking` | no | Minecraft `game_event` tags | sculk sensor / Warden detection |
| Individual emission events: `step` · `swim` · `flap` · `hit_ground` · `bounce` · `splash` · `block_place` · `block_destroy` · `block_open` · `block_close` · `block_activate` · `block_deactivate` · `block_attach` · `block_detach` · `block_change` · `container_open` · `container_close` · `drink` · `eat` · `equip` · `unequip` · `shear` · `explode` · `lightning_strike` · `note_block_play` · `instrument_play` · `prime_fuse` · `projectile_shoot` · `projectile_land` · `entity_action` · `entity_damage` · `entity_die` · `entity_place` · `entity_interact` · `entity_mount` · `entity_dismount` · `elytra_glide` · `teleport` · `fluid_pickup` · `fluid_place` · `resonate_1`…`resonate_15` · `shriek` | no — each is an emission kind | Minecraft | detection, note-block resonance |
| `occludes_vibration_signals` · `dampens_vibrations` | no | Minecraft block tags | sound occlusion (wool blocks sound) |
| `audio_physics_material_solid` · `audio_physics_material_wall` · `audio_physics_material_event` · `audio_materialaudio_type` · `audio_is_soft` · `audio_size_multiplier` · `solid_on_collision_splash_power` | yes — enum/scalar | Noita | impact sound selection and loudness |
| `soundImpactStuff` · `Surface Type` (Physical Surface enum) | yes — enum | RimWorld stuffProps, Unreal | footstep/impact sound & VFX |
| `SMELL` · `HEAR` · `SIGHT` (body-part senses) · `Sight` · `Hearing` (capacities) | no / yes % | Dwarf Fortress, RimWorld | perception rolls |
| `BLOOD_MAP_DESCRIPTOR` · `ICHOR_MAP_DESCRIPTOR` · `GOO_MAP_DESCRIPTOR` · `SLIME_MAP_DESCRIPTOR` · `PUS_MAP_DESCRIPTOR` · `SWEAT_MAP_DESCRIPTOR` · `TEARS_MAP_DESCRIPTOR` · `SPIT_MAP_DESCRIPTOR` | no | Dwarf Fortress | contaminant trail naming/tracking |
| `Stealth` · `Elusive` · `Invisibility` · `Blind` · `Sever` · `Suppressed` | no | Hearthstone, LoR, Destiny 2, PoE | targeting legality |
| `danger_radioactive` · `danger_fire` · `danger_water` · `danger_poison` · `radioactive` | no | Noita | AI avoidance / hazard warning |
| `Scout` · `Challenger` · `Taunt` · `Taunted` | no | LoR, Hearthstone, PoE | forced-attention / aggro |

---

## 7. Creature and body descriptors

### 7a. Dwarf Fortress functional body-part tokens (captured in full)

| Tag name | Carries a value? | Where it comes from | What reads it |
|---|---|---|---|
| `UPPERBODY` | no | DF body token | core; destruction blows the creature apart |
| `LOWERBODY` | no | DF | second core; destruction bisects |
| `HEAD` | no | DF | vital; severing kills |
| `GRASP` | no | DF | can hold items, wrestle, lock, choke |
| `STANCE` | no | DF | keeps the creature standing; loss = collapse |
| `SIGHT` | no | DF | vision function |
| `HEAR` | no | DF | hearing function |
| `SMELL` | no | DF | scent function |
| `BREATHE` | no | DF | loss causes suffocation |
| `THOUGHT` | no | DF | required to think; loss = death/incapacity |
| `CIRCULATION` | no | DF | blood movement; damage causes bleeding |
| `NERVOUS` | no | DF | signal conduction; damage paralyses downstream |
| `GUTS` | no | DF | digestive mass; disembowelment |
| `MOUTH` · `THROAT` | no | DF | eating, speech, drowning |
| `LIMB` | no | DF | wrestling-usable appendage |
| `DIGIT` | no | DF | finger/toe class |
| `JOINT` | no | DF | breakable articulation |
| `CONNECTOR` | no | DF | severing detaches children |
| `SOCKET` · `APERTURE` | no | DF | attachment / opening |
| `INTERNAL` | no | DF | organ, invisible until injured |
| `EMBEDDED` | no | DF | inside a parent part |
| `SMALL` | no | DF | reduced hit chance |
| `SKELETON` | no | DF | persists as bone after decay |
| `UNDER_PRESSURE` | no | DF | sprays when opened |
| `PREVENTS_PARENT_COLLAPSE` | no | DF | structural support |
| `TOTEMABLE` | no | DF | can be crafted into a totem |
| `VERMIN_BUTCHER_ITEM` | no | DF | butchery yield |
| `GELDABLE` | no | DF | castration target |
| `FLIER` | no | DF | required for flight; damage grounds |
| `LEFT` · `RIGHT` · `NUMBER` · `INDIVIDUAL_NAME` · `DEFAULT_RELSIZE` · `CON` · `CON_CAT` · `CONTYPE` · `CATEGORY` | yes (NUMBER, RELSIZE) | DF | anatomy graph construction |

### 7b. Other body / creature vocabularies

| Tag name | Carries a value? | Where it comes from | What reads it |
|---|---|---|---|
| Body parts: `Torso` `Neck` `Head` `Skull` `Brain` `Eye` `Ear` `Nose` `Jaw` `Tongue` `Heart` `Lung` `Kidney` `Liver` `Stomach` `Spine` `Ribcage` `Sternum` `Pelvis` `Clavicle` `Shoulder` `Arm` `Humerus` `Radius` `Hand` `Finger` `Leg` `Femur` `Tibia` `Foot` `Toe` `Waist` | no | RimWorld | injury targeting, prosthetics |
| Body part groups: `FullHead` `UpperHead` `Eyes` `Teeth` `Mouth` `Neck` `Torso` `Arms` `Hands` `Shoulders` `Legs` `Feet` `LeftHand` `RightHand` | no | RimWorld | apparel coverage, hit distribution |
| Capacities: `Consciousness` `Sight` `Hearing` `Moving` `Manipulation` `Talking` `Eating` `Breathing` `Blood Filtration` `Blood Pumping` `Digestion` `Metabolism` | yes — % | RimWorld | derived from body-part damage; gates all work |
| `undead` `skeletons` `zombies` `arthropod` `illager` `raiders` `aquatic` `illager_friends` `wither_friends` `beehive_inhabitors` `boat` `arrows` `impact_projectiles` `redirectable_projectile` | no | Minecraft entity_type tags | enchantment bonuses, AI faction |
| `sensitive_to_smite` · `sensitive_to_bane_of_arthropods` · `sensitive_to_impaling` · `immune_to_oozing` · `immune_to_infested` · `inverted_healing_and_harm` · `ignores_poison_and_regen` · `freeze_immune_entity_types` · `freeze_hurts_extra_types` · `fall_damage_immune` · `deflects_projectiles` · `can_breathe_under_water` · `powder_snow_walkable_mobs` · `burn_in_daylight` · `dismounts_underwater` · `non_controlling_rider` · `can_wear_horse_armor` · `can_equip_saddle` · `can_equip_harness` · `no_anger_from_wind_charge` · `not_scary_for_pufferfish` · `not_affected_by_geysers` · `nautilus_hostiles` · `axolotl_hunt_targets` · `axolotl_always_hostiles` · `accepts_iron_golem_gift` · `candidate_for_iron_golem_gift` · `followable_friendly_mobs` · `cannot_be_age_locked` · `cannot_be_pushed_onto_boats` · `cannot_be_dismounted_by_item_usage` | no | Minecraft entity_type tags | per-system special-casing |
| `FLIER` `SWIMS_INNATE` `SWIMS_LEARNED` `AMPHIBIOUS` `AQUATIC` `CANNOT_CLIMB` `CANNOT_JUMP` `IMMOBILE` | no | Dwarf Fortress creature tokens | movement legality |
| `NOBREATHE` `NO_EAT` `NO_DRINK` `NO_SLEEP` `NOPAIN` `NOSTUN` `NOFEAR` `NOEMOTION` `NOTHOUGHT` `NONAUSEA` `NO_DIZZINESS` `NO_FEVERS` `NOEXERT` `NOT_LIVING` `EXTRAVISION` `TRANCES` `OPPOSED_TO_LIFE` | no | Dwarf Fortress | need/vulnerability suppression |
| `FIREIMMUNE` `FIREIMMUNE_SUPER` `WEBIMMUNE` `MAGMA_VISION` | no | Dwarf Fortress | environmental immunity |
| `CARNIVORE` `BONECARN` `GRAZER` `LARGE_PREDATOR` `BENIGN` `CRAZED` `MISCHIEVOUS` `NATURAL` `MEANDERER` `CURIOUSBEAST_EATER` `CURIOUSBEAST_GUZZLER` `CURIOUSBEAST_ITEM` | no / yes (GRAZER) | Dwarf Fortress | AI behaviour selection |
| `INTELLIGENT` `CAN_LEARN` `CAN_SPEAK` `SLOW_LEARNER` `UTTERANCES` `EQUIPS` `CANOPENDOORS` `LOCKPICKER` | no | Dwarf Fortress | agency tier |
| `PET` `PACK_ANIMAL` `MOUNT` `COMMON_DOMESTIC` `MILKABLE` `LAYS_EGGS` `FEMALE` | no / yes | Dwarf Fortress | domestication systems |
| `ActorTypeNPC` `ActorTypeUndead` `ActorTypeAnimal` `ActorTypeDragon` `ActorTypeDwarven` `ActorTypeRobot` `ActorTypeSuperMutant` `ActorTypeGhoul` | no | Skyrim / Fallout 4 KYWD | spell/perk condition checks that replaced hardcoded race checks |
| Tribes: `Beast` `Demon` `Dragon` `Elemental` `Mech` `Murloc` `Naga` `Pirate` `Quilboar` `Totem` `Undead` `Draenei` `All` | no | Hearthstone | synergy/"cluster membership" — one card may hold several |
| Factions: `Grineer` `Corpus` `Infested` `Orokin` `Sentient` `Narmer` `Kuva Grineer` | no | Warframe | faction damage multipliers |
| `Wildness` `Lifespan Factor` `Fertility` `Cancer Rate Factor` `Toxic Resistance` `Toxic Environment Resistance` `Vacuum Resistance` `Psychic Sensitivity` `Pain Shock Threshold` `Mental Break Threshold` `Immunity Gain Speed` `Injury Healing Factor` `Learning Rate Factor` `Rest Rate Multiplier` `Eating Speed` `Carrying Capacity` `Move Speed` `Crawl Speed` | yes | RimWorld pawn stats | pawn simulation |

---

## 8. Origin and provenance

| Tag name | Carries a value? | Where it comes from | What reads it |
|---|---|---|---|
| `Shaper` · `Elder` · `Crusader` · `Redeemer` · `Hunter` · `Warlord` (influence) | no | Path of Exile | which exclusive mod pool the item can access |
| `Synthesised` · `Fractured` · `Veiled` · `Enchanted` · `Replica` · `Relic` · `Eldritch implicit` | no | Path of Exile | crafting legality, mod origin |
| Mod domains: `Item` `Flask` `Monster` `Strongbox` `Area` `Relic` `Crafted` `Jewel` `Abyss Jewel` `Delve Fossil` `Synthesis` `Cluster Jewel` | yes — numeric domain ID | Path of Exile | which entity a mod may attach to |
| Generation types: `Prefix` `Suffix` `Intrinsic` `Corrupted` `Enchantment` `Essence` `Bestiary` `Monster Affliction` | yes — numeric ID | Path of Exile | how a modifier came to exist |
| `countryOfOrigin` · `productionDate` · `purchaseDate` · `releaseDate` · `brand` · `award` | yes | schema.org/Product | provenance display, filtering |
| `techLevel` (`Animal` `Neolithic` `Medieval` `Industrial` `Spacer` `Ultra` `Archotech`) | yes — ordinal | RimWorld ThingDef | faction availability, trade generation |
| `dn_*` (dynamic naming prefix) · `dn_PowerArmor_Helmet` · `dn_HasPAPaint_VIMRed` | no | Fallout 4 / AWKCR | instance naming rules |
| `ccBGSSSE*_` · `DLC1*` · `DLC2*` (content-pack prefixes on keywords) | no | Skyrim SE | which content pack introduced the tag |
| `Vaal` · `Exceptional` · `Prismatic` · `Support` (gem provenance/classes) | no | Path of Exile gem tags | drop pool, gem-quality behaviour |
| `Origin` · `Region` (Bilgewater, Noxus, Demacia, Shadow Isles, …) | no | Legends of Runeterra | deckbuilding legality |
| `component_version` / `edition`-style pins: `manifest`, `datapack format`, `pack_format` | yes | Minecraft datapacks | load-time compatibility |

---

## 9. Effect delivery and damage typing

| Tag name | Carries a value? | Where it comes from | What reads it |
|---|---|---|---|
| `Fire` · `Cold` · `Lightning` · `Chaos` · `Physical` · `Elemental` | no | Path of Exile (gem tags + mod tags) | every scoped modifier ("increased Fire Damage") |
| `Attack` · `Spell` · `Melee` · `Projectile` · `Area`/`AoE` · `Duration` · `Chaining` · `Nova` · `Slam` · `Strike` · `Bow` · `Movement` · `Travel` · `Critical` · `Channelling` | no | Path of Exile gem tags | modifier scoping, support-gem legality |
| `Minion` · `Totem` · `Trap` · `Mine` · `Brand` · `Aura` · `Curse` · `Hex` · `Mark` · `Herald` · `Guard` · `Link` · `Warcry` · `Banner` · `Blessing` · `Golem` · `Orb` · `Arcane` · `Stance` · `Trigger` · `Blink` · `Vaal` · `Support` | no | Path of Exile gem tags | which mods and supports apply |
| PoE mod-tag layer: `Life` `Mana` `Resource` `Caster` `Speed` `Damage` `Defences` `Attribute` `Gem` `Bleed` `Poison` `Ailment` `Drop` | no | Path of Exile mod metadata | Harvest-style targeted crafting |
| Ailments: `Ignite` · `Bleeding` · `Poison` (damaging); `Chill` · `Freeze` · `Shock` · `Scorch` · `Brittle` · `Sap` (non-damaging) | yes — magnitude & duration | Path of Exile | resolution stage after a hit |
| PoE status keywords: `Blind` `Maim` `Hinder` `Stun` `Knockback` `Taunt` `Intimidate` `Unnerve` `Impale` `Withered` `Corrupted Blood` `Fortify` `Onslaught` `Phasing` `Tailwind` `Elusive` `Adrenaline` `Cull` | yes — stacks/duration | Path of Exile | conditional modifiers |
| Warframe physical: `Impact` (→ Knockback) · `Puncture` (→ Weakened) · `Slash` (→ Bleed) | yes — magnitude | Warframe | damage + status roll |
| Warframe elemental: `Heat` (Ignite) · `Cold` (Freeze) · `Electricity` (Tesla Chain) · `Toxin` (Poison) | yes | Warframe | as above |
| Warframe combined: `Blast` (Detonate) · `Corrosive` (Corrosion) · `Gas` (Gas Cloud) · `Magnetic` (Disrupt) · `Radiation` (Confusion) · `Viral` (Virus) — each formed from two primaries | yes | Warframe | combination is itself a rule |
| Warframe special: `Void` (Bullet Attract) · `Tau` (Status Vulnerability) · `True` (no status) | yes | Warframe | bypasses defences |
| Destiny 2: `Kinetic` `Arc` `Solar` `Void` `Stasis` `Strand` | no | Destiny 2 | shield matching, surge mods |
| Destiny 2 verbs — Solar: `Scorch` `Ignite` `Radiant` `Restoration` `Cure` `Firesprite`; Void: `Volatile Rounds` `Weaken` `Suppressed` `Devour` `Invisibility` `Void Overshield` `Void Breach`; Arc: `Amplified` `Blind` `Jolt` `Ionic Trace`; Stasis: `Slow` `Freeze` `Shatter` `Stasis Crystal` `Stasis Shard`; Strand: `Sever` `Suspend` `Unravel` `Tangle` `Threadlings` `Woven Mail` | yes (most stack) | Destiny 2 | subclass keyword system — the exemplar of a published verb vocabulary |
| Diablo 4: `Fire` `Cold` `Lightning` `Poison` `Shadow` `Physical` · `Damage Over Time` · `Overpower` · `Critical Strike` · `Vulnerable` · `Lucky Hit` · `Thorns` | yes — % | Diablo 4 affixes | affix scoping |
| Diablo 4 conditional scopes: `to Close Enemies` `to Distant Enemies` `to Elites` `to Injured` `to Healthy` `to Burning` `to Crowd-Controlled` `to Stunned` `to Slowed` `to Dazed` `to Frozen` `to Chilled` `While Fortified` `While Shapeshifted` | yes — % | Diablo 4 | condition-gated multipliers |
| Minecraft damage types: `in_fire` `on_fire` `campfire` `lava` `hot_floor` `in_wall` `cramming` `drown` `starve` `cactus` `fall` `fly_into_wall` `out_of_world` `outside_border` `generic` `generic_kill` `magic` `indirect_magic` `wither` `wither_skull` `dragon_breath` `dry_out` `sweet_berry_bush` `freeze` `stalagmite` `falling_block` `falling_anvil` `falling_stalactite` `sting` `mob_attack` `mob_attack_no_aggro` `player_attack` `arrow` `spear` `trident` `fireball` `unattributed_fireball` `mob_projectile` `thrown` `explosion` `player_explosion` `fireworks` `sonic_boom` `thorns` `spit` `lightning_bolt` `ender_pearl` `wind_charge` `bad_respawn_point` `mace_smash` | no | Minecraft `damage_type` registry | death message, armour interaction |
| Minecraft damage-type tags: `bypasses_armor` `bypasses_shield` `bypasses_invulnerability` `bypasses_effects` `bypasses_resistance` `bypasses_cooldown` `bypasses_enchantments` `bypasses_wolf_armor` `is_fire` `is_projectile` `is_explosion` `is_fall` `is_drowning` `is_freezing` `is_lightning` `is_player_attack` `no_knockback` `no_anger` `no_impact` `no_wolf_retaliation` `damages_helmet` `always_most_significant_fall` `always_triggers_silverfish` `always_hurts_ender_dragons` `always_kills_armor_stands` `can_break_armor_stand` `burns_armor_stands` `ignites_armor_stands` `avoids_guardian_thorns` `witch_resistant_to` `wither_immune_to` `panic_causes` `panic_environmental_causes` `mace_smash` | no | Minecraft | mitigation-bypass rules, exactly the "guard" layer |
| RimWorld damage defs — Sharp: `Cut` `Stab` `RangedStab` `Bullet` `BulletToxic` `Arrow` `ArrowHighVelocity` `Scratch` `ScratchToxic` `Bite` `BiteToxic` `Bomb` `BombSuper` `Thump` `AcidBurn` `EnergyBolt` `Nerve` `MiningBomb` `TornadoScratch`; Blunt: `Crush` `Blunt` `Poke` `Demolish`; Heat: `Flame` `Burn` `Vaporize` `Beam` `ElectricalBurn` `MechBandShockwave` `NociosphereVaporize`; No armour category: `Frostbite` `Surgical cut` `Execution cut` `EMP` `Stun` `Smoke` `Deterioration` `Rotting` `Mining` `Extinguish` `Decayed` `ToxGas` `Digested` `NerveStun` `Psychic` `DeadlifeDust` `VacuumBurn` | yes — amount | RimWorld | armour category routing |
| RimWorld material multipliers: `SharpDamageMultiplier` `BluntDamageMultiplier` `ArmorRating_Sharp` `ArmorRating_Blunt` `ArmorRating_Heat` `Armor - Material Effect Multiplier` | yes — × | RimWorld stuffProps | weapon/armour derived from material |
| Slay the Spire card types: `Attack` `Skill` `Power` `Status` `Curse` | no | Slay the Spire | targeting rules, "for each Attack played" |
| StS buffs: `Strength` `Dexterity` `Focus` `Artifact` `Buffer` `Intangible` `Plated Armor` `Thorns` `Vigor` `Duplication` `Pen Nib` `Regen` `Ritual` `Draw Card` `Energized` `Mantra` `Barricade` `Berserk` `Brutality` `Combust` `Corruption` `Dark Embrace` `Demon Form` `Double Tap` `Evolve` `Feel No Pain` `Fire Breathing` `Flame Barrier` `Juggernaut` `Metallicize` `Rage` `Rupture` `Accuracy` `After Image` `Blur` `Burst` `Double Damage` `Envenom` `Infinite Blades` `Next Turn Block` `Nightmare` `Noxious Fumes` `Phantasmal` `Thousand Cuts` | yes — stacks | Slay the Spire | almost all are "stack count" tags |
| StS debuffs: `Vulnerable` `Weak` `Frail` `Poison` `Strength Down` `Dexterity Down` `Shackled` `Confusion` `Choked` `Corpse Explosion` `No Draw` `No Block` `Wraith Form` `Bias` `Lock-On` `Block Return` `Fasting` `Mark` `Constricted` `Draw Reduction` `Entangled` `Hex` `Slow` | yes — stacks | Slay the Spire | as above |
| Hearthstone keywords: `Battlecry` `Deathrattle` `Taunt` `Charge` `Rush` `Divine Shield` `Windfury` `Mega-Windfury` `Stealth` `Poisonous` `Lifesteal` `Spell Damage` `Overload` `Combo` `Secret` `Discover` `Inspire` `Silence` `Freeze` `Immune` `Elusive` `Reborn` `Dormant` `Corrupt` `Frenzy` `Tradeable` `Infuse` `Forge` `Titan` `Spellburst` `Outcast` `Questline` `Quest` `Sidequest` `Manathirst` `Finale` `Overheal` `Magnetic` `Echo` `Twinspell` `Adapt` `Recruit` `Colossal` `Honorable Kill` `Overkill` `Start of Game` `Excavate` `Dredge` `Invoke` `Imbue` `Kindred` `Tourist` `Shatter` `Rewind` `Prepare` `Quickdraw` `Gigantify` `Miniaturize` `Fabled` `Herald` `Choose One` | mostly no; some yes (Spell Damage +N, Overload (N)) | Hearthstone | trigger + rules-engine dispatch |
| LoR keywords: `Allegiance` `Attune` `Barrier` `Bond` `Can't Block` `Capture` `Challenger` `Deep` `Double Attack` `Drain` `Elusive` `Enlightened` `Ephemeral` `Fearsome` `Fleeting` `Formidable` `Frostbite` `Fury` `Immobile` `Impact` `Last Breath` `Lifesteal` `Lurk` `Nab` `Nexus Strike` `Obliterate` `Overwhelm` `Plunder` `Quick Attack` `Recall` `Regeneration` `Revive` `Scout` `Silence` `SpellShield` `Strike` `Stun` `Support` `Tough` `Vulnerable` | some yes (Impact N, Tough N) | Legends of Runeterra | combat resolution steps |
| Noita `status_effects` · `on_fire` · `generates_flames` · `temperature_of_fire` · `generates_smoke` · `always_ignites_damagemodel` · `solid_on_break_explode` · `solid_on_collision_explode` · `solid_on_collision_convert` | yes | Noita | material→status propagation |
| `damage_modifier` (per surface type) · `Damage Modifier` | yes — × | Unreal physical materials | surface-specific damage scaling |

---

## 10. Access, rarity and permission

| Tag name | Carries a value? | Where it comes from | What reads it |
|---|---|---|---|
| `Normal` · `Magic` · `Rare` · `Unique` | no — ordinal | Path of Exile | drop table, affix budget |
| `Common` · `Uncommon` · `Rare` · `Epic` · `Legendary` (+ `Free`, `Mythic`) | no — ordinal | Hearthstone, Diablo, Destiny, most F2P economies | crafting cost, drop weight, deck limits |
| `Awful` `Poor` `Normal` `Good` `Excellent` `Masterwork` `Legendary` | no — ordinal | RimWorld quality | separate axis from material |
| `spawn weight` per tag | yes — integer | Path of Exile mod tables | probability, not permission — weight 0 = forbidden |
| `mod level` / `Item Level` / `required level` | yes | Path of Exile, Diablo | gate on tier availability |
| `VendorItemWeapon` `VendorItemArmor` `VendorItemFood` `VendorItemJunk` `VendorItemIngredient` `VendorItemPotion` (`VendorItem*` family) | no | Skyrim / Fallout 4 KYWD | which merchant will buy/sell it |
| `Recipe Filter` (keyword type) · `Mod Association` · `Attach Point` · `Attraction Type` · `Anim Face` | no — keyword *kind* | Fallout 4 Creation Kit | what subsystem may consume the keyword |
| `FeaturedItem` · `FeaturedItem_ExcludeList` · `DPF_FixedBuyPrice` · `DPF_FixedSellPrice` | no / yes | Skyrim SE | price override permission |
| `MagicDisallowEnchanting` · `no_attack_mods` · `no_caster_mods` | no | Skyrim, Path of Exile | negative permission — explicitly forbids a mod class |
| `show_in_creative_mode` · `hax` · `matter_eater_ignore_list` · `sunbaby_ignore_list` | no | Noita | tool/menu exposure, exclusion lists |
| `player_plantable` / `villager_plantable_seeds` · `piglin_loved` · `guarded_by_piglins` | no | Minecraft | NPC permission / reaction |
| `techLevel` · `tradeTags` · `weaponTags` | yes — enum/list | RimWorld ThingDef | which faction may carry or sell it |
| `Delivery` analogue — `Lens`/visibility tags: `INTERNAL` (hidden until injured), `Dormant`, `Unidentified`, `Hidden`, `Fog of war` | no | DF, Hearthstone, PoE | who may see this |
| `offers` · `aggregateRating` · `isConsumableFor` · `isAccessoryOrSparePartFor` · `isSimilarTo` · `isRelatedTo` · `inProductGroupWithID` | yes — relation | schema.org/Product | catalogue-level relations, not physical |
| Cost/economy tags: `Overload (N)` · `Manathirst (N)` · `mana cost` · `Doubloon`-analogues · `Potion Charges` · `Resource Generation` · `Maximum Resource` | yes — integer | Hearthstone, Diablo 4, PoE | payment gating |

---

# NAMES THAT RECUR ACROSS FOUR OR MORE SYSTEMS

- **Fire** (PoE · Minecraft · DF · Noita · Diablo · RimWorld `Flame`/`Burn` · Warframe `Heat` · Destiny `Solar`)
- **Cold / Frost / Freeze** (PoE · Warframe · Destiny `Stasis` · Diablo · Minecraft `freeze`/`is_freezing` · Noita `frozen` · RimWorld `Frostbite` · LoR `Frostbite` · Hearthstone `Freeze`)
- **Lightning / Electricity / Arc** (PoE · Warframe · Diablo · Destiny · Minecraft `lightning_bolt` · Noita `electrical_conductivity` · RimWorld `ElectricalBurn`/`EMP`)
- **Poison / Toxin** (PoE · Warframe · Diablo · Slay the Spire · Hearthstone `Poisonous` · Noita `meltable_to_poison` · RimWorld `ToxGas` · Minecraft `ignores_poison_and_regen`)
- **Physical** (PoE · Diablo · Warframe · RimWorld · Destiny `Kinetic`)
- **Chaos / Shadow / Void / Dark** (PoE `Chaos` · Diablo `Shadow` · Destiny `Void` · Warframe `Void`)
- **Bleed / Bleeding** (PoE · Warframe `Slash`→Bleed · Diablo · DF `CIRCULATION` bleeding · RimWorld)
- **Burn / Burning / Ignite** (PoE `Ignite` · Warframe `Ignite` · Destiny `Ignition`/`Scorch` · Diablo `Burning` · Noita `on_fire` · Minecraft `on_fire`)
- **Stun** (PoE · LoR · Diablo `Stunned` · RimWorld `Stun` · Hearthstone-adjacent · DF `NOSTUN`)
- **Slow** (Slay the Spire · Diablo `Slowed` · Destiny `Slow` · LoR-adjacent · PoE `Hinder`)
- **Vulnerable** (Slay the Spire · Diablo 4 · LoR · Warframe `Tau`/Status Vulnerability)
- **Weak / Weakened** (Slay the Spire `Weak` · Warframe `Weakened` · Destiny `Weaken` · PoE `Unnerve`-adjacent)
- **Blind** (PoE · Destiny 2 · Minecraft blindness · Slay the Spire-adjacent)
- **Silence** (Hearthstone · LoR · PoE conditions discussion · MOBA convention)
- **Lifesteal / Drain** (Hearthstone · LoR `Drain` · PoE leech · Diablo `Life on Kill`)
- **Taunt** (Hearthstone · PoE · LoR `Challenger` · Diablo `Taunted`)
- **Stealth / Invisibility / Elusive** (Hearthstone `Stealth` · LoR `Elusive` · Destiny `Invisibility` · PoE `Elusive`)
- **Immune / Immunity** (Hearthstone · Minecraft `dragon_immune`/`wither_immune_to`/`freeze_immune_entity_types` · DF `FIREIMMUNE` · Noita `indestructible`)
- **Barrier / Shield / Overshield** (LoR `Barrier` · Destiny `Void Overshield` · Diablo `Barrier` · Hearthstone `Divine Shield` · RimWorld `Shield Max Energy`)
- **Armor / Armour** (RimWorld `ArmorRating_*` · Diablo `Armor` · Minecraft `bypasses_armor` · Skyrim `ArmorMaterial*` · Slay the Spire `Plated Armor`)
- **Undead** (Minecraft `undead` · Skyrim `ActorTypeUndead` · Hearthstone `Undead` · DF `NOT_LIVING` · Diablo lineage)
- **Beast / Animal** (Hearthstone `Beast` · Skyrim `ActorTypeAnimal` · RimWorld animal category · DF creature classes)
- **Metal** (DF `IS_METAL` · Minecraft Bedrock `metal` · Noita `meltable_metal` · RimWorld `Metallic` · Skyrim material keywords)
- **Stone** (DF `IS_STONE` · Minecraft `base_stone_*`/`stone` · RimWorld `Stony` · Noita `rock`)
- **Wood** (DF `WOOD` · Minecraft `logs`/`planks`/`wood` · RimWorld `Woody` · Noita solids · Skyrim `WeapMaterialWood`)
- **Leather** (DF `ITEMS_LEATHER` · RimWorld `Leathery` · Skyrim `ArmorMaterialLeather` · Minecraft `repairs_leather_armor` · schema.org `material`)
- **Glass** (DF `IS_GLASS` · Skyrim `ArmorMaterialGlass` · Minecraft · Noita)
- **Steel** (RimWorld · Skyrim `ArmorMaterialSteel`/`WeapMaterialSteel` · Fallout · Minecraft-adjacent `iron`)
- **Water** (Minecraft `water` fluid tag + Bedrock `water` · Noita `water` tag · DF liquid handling · Unity/physics buoyancy)
- **Flammable / Flammability** (DF `FLAMMABLE`/`IGNITE_POINT` · RimWorld `Flammability` · Noita `burnable` · Minecraft `logs_that_burn`)
- **Density** (DF `SOLID_DENSITY` · Noita `density` · Unreal `density` · Unity/PhysX mass · schema.org `weight`)
- **Mass / Weight** (RimWorld `Mass` · Unity Rigidbody · Unreal · schema.org `weight` · DF `MOLAR_MASS`)
- **Friction** (Unity · Unreal · Godot · Noita `solid_friction`/`slippery`)
- **Bounciness / Restitution** (Unity `Bounciness` · Unreal `Restitution` · Godot `bounce` · Noita `solid_restitution`)
- **Melting point / molten** (DF `MELTING_POINT` · Noita `molten`/`meltable` · Minecraft smelting · RimWorld smelting)
- **Durability / Hit Points** (RimWorld `MaxHitPoints` · Noita `durability`/`hp` · Minecraft `enchantable/durability` · Unreal destructible threshold · PoE item integrity)
- **Rarity ladder Common→Legendary** (Hearthstone · Diablo · Destiny · Warframe · RimWorld quality · PoE Normal/Magic/Rare/Unique)
- **Attack** (PoE gem tag · Slay the Spire card type · LoR `Double Attack`/`Quick Attack` · Diablo `Attack Speed` · Minecraft `player_attack`/`mob_attack`)
- **Spell** (PoE gem tag · Hearthstone card type · LoR card type · Diablo skill class)
- **Projectile** (PoE gem tag · Minecraft `is_projectile`/`impact_projectiles` · Warframe · Unity/Unreal collision layers)
- **Melee** (PoE gem tag · Minecraft `enchantable/melee_weapon` · Warframe · Diablo · Skyrim `WeapType*`)
- **Area / AoE / Explosion** (PoE `AoE` · Minecraft `is_explosion` · Diablo · Warframe `Blast` · Noita `solid_on_collision_explode`)
- **Duration** (PoE gem tag · Diablo `Crowd Control Duration` · Hearthstone `Temporary` · Noita `lifetime` · Slay the Spire stack decay)
- **Critical / Critical Strike** (PoE `Critical` · Diablo `Critical Strike Chance/Damage` · Warframe · Destiny precision · RimWorld-adjacent)
- **Movement Speed** (PoE `Movement` · Diablo `Movement Speed` · RimWorld `Move Speed` · Destiny mobility · Minecraft `soul_speed_blocks`)
- **Minion / Summon** (PoE `Minion` · Diablo `Minion Attack Speed`/`Maximum Minion Life` · Hearthstone `minion` · LoR units · RimWorld mechanoids)
- **Curse / Hex** (PoE `Curse`/`Hex` · Slay the Spire `Curse`/`Hex` · Hearthstone-adjacent · Diablo)
- **Aura** (PoE `Aura` · Diablo · RimWorld-adjacent · MOBA convention · Hearthstone ongoing effects)
- **Trigger** (PoE gem tag · Hearthstone trigger keywords · Minecraft `always_triggers_silverfish` · Unreal/Unity trigger volumes)
- **Grasp / Hand / Manipulation** (DF `GRASP` · RimWorld `Manipulation`/`Hands` · Minecraft `enderman_holdable` · Skyrim hand slots)
- **Sight / Vision** (DF `SIGHT`/`EXTRAVISION` · RimWorld `Sight` · Destiny/stealth systems · Minecraft `blockLight`-adjacent)
- **Breathe / Drowning** (DF `BREATHE`/`NOBREATHE` · RimWorld `Breathing` · Minecraft `can_breathe_under_water`/`is_drowning` · Warframe-adjacent)
- **Head** (DF `HEAD` · RimWorld `FullHead`/`UpperHead` · Minecraft `head_armor` · Skyrim helmet slot · Fallout `dn_PowerArmor_Helmet`)
- **Fall / Fall damage** (Minecraft `is_fall`/`fall_damage_immune` · RimWorld · PoE-adjacent · Unity/Unreal physics)
- **Knockback** (Warframe `Impact`→Knockback · Minecraft `no_knockback` · PoE `Knockback` · Diablo `Knockback`)

---

**Sources:** [PoE Gem tag](https://www.poewiki.net/wiki/Gem_tag) · [PoE Item class](https://www.poewiki.net/wiki/Item_class) · [PoE Modifier](https://www.poewiki.net/wiki/Modifier) · [PoE Ailment](https://www.poewiki.net/wiki/Ailment) · [PoE Damage](https://www.poewiki.net/wiki/Damage) · [PoE Influenced item](https://www.poewiki.net/wiki/Influenced_item) · [PoE Item](https://www.poewiki.net/wiki/Item) · [poedb Modifiers](https://poedb.tw/us/Modifiers) · [MC Block tag](https://minecraft.wiki/w/Block_tag_(Java_Edition)) · [MC Item tag](https://minecraft.wiki/w/Item_tag_(Java_Edition)) · [MC Entity type tag](https://minecraft.wiki/w/Entity_type_tag_(Java_Edition)) · [MC Damage type tag](https://minecraft.wiki/w/Damage_type_tag_(Java_Edition)) · [MC Biome tag](https://minecraft.wiki/w/Biome_tag_(Java_Edition)) · [MC Fluid tag](https://minecraft.wiki/w/Fluid_tag_(Java_Edition)) · [MC Game event tag](https://minecraft.wiki/w/Game_event_tag_(Java_Edition)) · [Bedrock Vanilla Block Tags](https://learn.microsoft.com/en-us/minecraft/creator/reference/content/blockreference/examples/vanillablocktags?view=minecraft-bedrock-stable) · [RimWorld Stats](https://rimworldwiki.com/wiki/Stats) · [RimWorld Materials](https://rimworldwiki.com/wiki/Materials) · [RimWorld Damage Types](https://rimworldwiki.com/wiki/Damage_Types) · [RimWorld Body parts](https://rimworldwiki.com/wiki/Body_parts) · [DF Material definition token](https://dwarffortresswiki.org/index.php/Material_definition_token) · [DF Body token](https://dwarffortresswiki.org/index.php/Body_token) · [DF 40d:Body token](https://dwarffortresswiki.org/index.php/40d:Body_token) · [DF Creature token](https://dwarffortresswiki.org/index.php/Creature_token) · [DF Material token](https://dwarffortresswiki.org/index.php/Material_token) · [Skyrim Notable keywords](https://www.nexusmods.com/skyrimspecialedition/articles/11298) · [Fallout 4 CK Keyword](https://falloutck.uesp.net/wiki/Keyword) · [AWKCR](https://www.nexusmods.com/fallout4/mods/6091) · [Warframe Damage](https://wiki.warframe.com/w/Damage) · [Destiny 2 subclass keywords](https://attackofthefanboy.com/guides/all-destiny-2-subclass-keywords-explained-solar-void-arc-stasis-and-strand/) · [Diablo 4 Gear Affixes](https://www.studioloot.com/diablo4/articles/diablo-4-gear-affixes/) · [StS Buffs](https://slaythespire.wiki.gg/wiki/Buffs) · [StS Debuffs](https://slaythespire.wiki.gg/wiki/Debuffs) · [Hearthstone Ability](https://hearthstone.wiki.gg/wiki/Ability) · [LoR keywords](https://www.runeterrafire.com/news/legends-of-runeterra-keywords-list-amp-guide-1) · [Unity Physic Material](https://docs.unity3d.com/Manual/class-PhysicMaterial.html) · [Unreal PhysicalMaterial](https://dev.epicgames.com/documentation/en-us/unreal-engine/python-api/class/PhysicalMaterial?application_version=5.1) · [Noita custom material](https://noita.wiki.gg/wiki/Modding:_Making_a_custom_material) · [Noita list of all tags](https://noita.wiki.gg/wiki/Modding:_List_of_all_tags) · [schema.org/Product](https://schema.org/Product)

**Gaps worth a second pass if wanted:** Godot `PhysicsMaterial` (page returned nav only — properties are `friction`, `rough`, `bounce`, `absorbent`); Fallout 4's actual `ObjectType*`/`ActorType*` keyword enumeration (only `ActorTypeRobot` was confirmed verbatim); DF's `body_default.txt` CATEGORY name list (only the functional token set was retrievable — the anatomical CATEGORY names are in the raws, not on any wiki page I reached).agentId: a3235c53b3c5a790b (use SendMessage with to: 'a3235c53b3c5a790b', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 135304
tool_uses: 68
duration_ms: 718419</usage>