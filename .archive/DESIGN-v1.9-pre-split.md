# Idle Deck Builder - Game Design Document

## Core Vision

An idle deck building game where strategic deck construction drives passive gameplay. Players build decks that auto-battle, generate resources, and progress through multiple tiers. The primary engagement is deck building strategy, not active combat management.

---

## Theme & Setting

### Theme: Elemental Magic Tower Defense

You are an apprentice mage defending a magical tower from endless waves of invaders. Your deck represents your arsenal of spells and magical abilities. As you master different schools of elemental magic (Fire, Water, Earth, Air, and foundational Arcane magic), you unlock more powerful spells and can defend against increasingly dangerous threats.

**Design Philosophy:** The theme provides context but never obscures gameplay. Familiar fantasy elements reduce cognitive overhead, letting strategic depth dominate. Abstract visuals (color coding + simple shapes) ensure performance and accessibility.

### Element System
- **Arcane (Gray):** Foundational magic underlying all elemental schools
- **Fire (Red):** Aggressive, destructive magic
- **Water (Blue):** Flowing, adaptive magic with healing and control
- **Earth (Green):** Defensive, enduring magic with protection and stability
- **Air (Yellow/White):** Swift, unpredictable magic with speed and tempo

### Currency: Essence
All resources are called "Essence" - magical energy extracted from your spells:
- **Arcane Essence** (base tier)
- **Fire Essence**, **Water Essence**, **Earth Essence**, **Air Essence** (elemental tiers)

Future currencies for prestige/crafting will use different terminology (Prisms, Crystallized Essence, Fragments, etc.) to maintain clarity.

---

## Core Mechanics

### Primary Progression Loop
**Combination Approach:** Multiple interconnected loops:
- Resource accumulation → Buy packs → Improve deck → Faster resource gain
- Combat victories → Unlock new content → New cards/mechanics → More combat options
- Card collecting/upgrading → Better decks → Tackle harder content → Collect more

### Idle Mechanics
**Hybrid Approach:**
- Idle resource generation while away
- Active deck management and strategic choices when playing
- Full passive combat (decks auto-battle)
- Deck building is the primary strategy layer

### Roguelike Elements
**Light Roguelike:**
- Minor run-to-run variance
- Permanent upgrades dominate progression
- Temporary bonuses are secondary to permanent improvements

---

## Tier System

### Tier Structure: Hybrid Cascading Model

**Core Principle:** Tiers unlock linearly, but once unlocked they remain active simultaneously. Lower tiers become "foundational support" rather than obsolete.

#### Arcane Tier (Base/Foundational)
- **Purpose:** Universal starting point, introduces core mechanics
- **Duration:** Full tier (1-2 hours of content)
- **Complexity:** Low - simple card types (Attack, Defense, Utility), basic stats
- **Currency:** Arcane Essence
- **Permanence:** Remains active and useful throughout entire game
  - Continue building Arcane deck
  - Continue earning Arcane Essence
  - Continue buying Arcane packs
  - Arcane Essence always useful (packs, upgrades, cross-tier uses)
- **Unique Feature:** Contains Class Cards (see Class System below)

#### Elemental Tiers (Class-Specific)
- **Tiers:** Fire, Water, Earth, Air (and future expansions)
- **Unlock Method:** Equip a Class Card (obtained from Arcane packs)
- **Progression:** Once unlocked, runs alongside Arcane tier
- **Cross-Tier Synergy:** Elemental tier cards can generate resources for lower tiers
  - Fire cards can generate Arcane Essence
  - Water cards can generate Arcane Essence
  - Higher tier cards can generate multiple Essences
- **Passive Transition:** Previous tiers continue running passively after new tiers unlock
  - Passive tiers: Generate resources automatically, no active deck building/combat
  - Active tiers: Full engagement (deck building, combat, upgrades)

### Tier Count
- **3-5 tiers** per class path (manageable, allows deep interactions)
- Total tiers across all classes: 6-10 unique colored tiers

---

## Class System

### Classes as Collectible Cards

**Core Mechanic:** Classes are not menu choices - they are cards found in packs.

#### Class Card Distribution
- **Common Classes:** Found in Arcane packs (Apprentices)
  - Simple tier paths (2 tiers: Arcane + one element)
  - Examples: Fire Apprentice, Water Apprentice, Earth Apprentice, Air Apprentice
  - **Structure:** Each Apprentice unlocks Arcane → [One Element]
- **Rare Classes:** Found in Arcane packs (rare drops) and elemental tier packs
  - Advanced tier paths (3 tiers: multi-element combinations)
  - Examples: Geomancer (Arcane→Earth→Fire), Frostmage (Arcane→Water→Air)
- **Epic Classes:** Found in elemental tier packs (rare drops)
  - Powerful tier paths (4 tiers: hybrid elements)
  - Examples: Stormlord (Arcane→Air→Water→Lightning), Battlemage (Arcane→Fire→Earth→Magma)
- **Legendary Classes:** Found in special/event packs
  - Complex tier paths (5 tiers: multiple element combinations)
  - Special synergies and bonuses
  - Examples: Primalist (all elements), Void Weaver (forbidden magic)

#### Class Mechanics (Session 1.2 Decision)
- **Activation:** Equip a Class Card to unlock its tier path
- **Single Active Class:** Only one class active at a time
- **Deck Limit Profiles:** Each class defines its own per-tier deck size limits
  - Common classes: Specialist distributions (e.g., 5 Arcane / 10 Fire)
  - Rare classes: Balanced distributions (e.g., 6 Arcane / 7 Earth / 7 Fire)
  - Epic/Legendary: Larger totals and more flexible limits
  - Class choice determines deck-building strategy
- **Switching:** 
  - Classes can ONLY be switched during prestige resets
  - Makes class choice meaningful and strategic
  - Natural prestige incentive (want to try new class? Prestige!)
  - Commit to class for entire run
- **Collection:** Can collect multiple class cards from packs, but only one active per run
- **Strategic Weight:** Class choice affects both tier access AND deck composition constraints

#### Class Path Examples
- **Fire Apprentice (Common):** Arcane → Fire
- **Water Apprentice (Common):** Arcane → Water
- **Earth Apprentice (Common):** Arcane → Earth
- **Air Apprentice (Common):** Arcane → Air
- **Geomancer (Rare):** Arcane → Earth → Fire (stone/metal/lava theme)
- **Frostmage (Rare):** Arcane → Water → Air (ice/mist theme)
- **Stormlord (Epic):** Arcane → Air → Water → Lightning (weather control)
- **Primalist (Legendary):** Arcane → Fire → Water → Earth → Air (all elements)

#### Class-Specific Features
- **Tier Synergy Bonuses:** Classes enhance synergies between their tier paths
  - Fire/Earth combos stronger for Geomancer class
  - Water/Air combos stronger for Frostmage class
- **Passive Tiers:** Tiers outside your class path become passive (auto-generate resources)
- **Cross-Tier Synergies:** Enhanced within class path, present but weaker across classes
- **Progression Incentive:** Higher rarity classes unlock MORE content (more tiers) not just different content

---

## Resource Generation System

### Resource Generation as Deck Building Strategy

**Core Principle:** Specific cards generate resources. Deck composition determines income rate, making resource generation a strategic deck-building decision.

**Critical Economy Model (Sessions 1.2 & 1.3):** Split resource system with distinct purposes:
- **Essence:** Generated by drawing generator cards during combat → Used for packs, conversion, universal upgrades
- **Shards/Fragments:** Dropped by combat victories → Used for card upgrades, deck size increases, permanent upgrades

All Essence generation starts with Arcane Essence. Elemental Essences are created through conversion by generator cards.

#### Resource Generation Mechanics (Session 1.3 Clarification)

**Critical Mechanic:** Generators produce essence **when drawn** during combat, not passively while sitting in deck.

**How It Works:**
- When a generator card is drawn from deck during combat, it adds to your generation rate
- Example: Draw "Arcane Conduit" (+2 Essence/sec) → Generation rate increases by +2/sec
- Draw another generator → Rate accumulates (now +5/sec total)
- Generation rate persists between enemies
- Rate resets only on player death/defeat
- Longer combat sessions = more deck cycles = more generator draws = more essence accumulated

**Strategic Implications:**
- Generators must be in deck AND drawn to produce essence
- Deck cycling speed matters (faster draws = faster essence accumulation)
- Death has meaningful penalty (lose accumulated generation rate)
- Session length matters (playing longer = more draws = more essence)
- Need balance: generators for essence vs combat cards for victory speed

#### Resource Generation Cards

**Arcane Generators (Foundation):**
- **Pure Arcane Generators:** Cards that generate Arcane Essence when drawn
  - Example: "Arcane Conduit" - +2 Arcane Essence/second when drawn
  - These are the foundation of the entire economy
  - Available from Arcane packs
  - Remain valuable throughout entire game

**Elemental Converters (Transformation):**
- **Elemental Generator Cards:** Cards that CONVERT Arcane Essence → Elemental Essence
  - Example: "Flame Transmuter" - Consumes 3 Arcane Essence, generates +2 Fire Essence/second
  - Function as "converters" rather than pure generators
  - Conversion rate is key balance point
  - May have combat stats (Hybrid Converters) or pure conversion (Weak combat, strong conversion)

**Hybrid Cards:** Cards that generate resources AND have combat abilities
  - Example: "Victory Harvest" - +5 Arcane Essence per battle won + combat ability
  - Battle rewards as resource generation
  - Scales with combat performance

**Conditional Generators:** Cards that generate based on game state or combos
  - Example: "Elemental Resonance" - While in deck, each Fire card boosts Arcane generation by +1/second
  - Synergy-based generation
  - Rewards thoughtful deck composition

#### Resource Flow Model (Session 1.3 - Split Resources)

**Essence Flow (Pack Currency):**
```
Draw Generator Cards → Accumulate Essence Generation Rate
                              ↓
                    Generate Arcane Essence (per second)
                              ↓
                    Spend on Arcane Packs
                    OR Spend on Universal Upgrades
                    OR Convert via Elemental Converters
                              ↓
Elemental Converter Cards → Convert Arcane → Elemental Essence
                              ↓
                    Spend on Elemental Packs
                    OR Spend on Tier-Specific Upgrades
```

**Shard Flow (Upgrade Currency):**
```
Combat Victories → Drop Shards/Fragments
                              ↓
                    Spend on Card Upgrades
                    OR Spend on Deck Size Increases
                    OR Spend on Permanent Upgrades
```

**Two Distinct Progression Paths:**
- **Collection Path:** Generators → Essence → Packs → More cards
- **Power Path:** Combat cards → Faster victories → Shards → Stronger cards

#### Scaling Mechanisms
- **Card Leveling:** Upgrade cards to increase generation/conversion rates
- **Card Quantity:** Number of generator cards in deck affects total generation
- **Synergies:** Cross-tier synergies can boost resource generation
- **Conversion Efficiency:** Higher tier/level converters have better conversion rates

#### Strategic Implications
- **Arcane Generators are Critical:** Without them, no resources flow
- **Conversion Rate Decisions:** Spend Arcane on upgrades vs convert to Elemental?
- **Deck Balance:** Must include Arcane generators + Elemental converters + Combat cards
- **Progression Gates:** Can't progress to new tier without efficient conversion
- **Foundation Never Obsolete:** Arcane generation remains valuable forever

#### Resource Generation Rates (To Be Balanced in Session 4)
- **Arcane Generation:** Base rate to be determined (e.g., 1-5 Essence/second early game)
- **Conversion Rates:** To be balanced (e.g., 3:1, 5:2, etc.)
- **Deck Composition:** Optimal ratio of Generators:Converters:Combat to be tested

---

## Deck Building System

### Core Deck Mechanics

#### Deck Constraints (Session 1.2 Decision)

**Multi-Layered Constraint System:**

1. **Total Deck Size (Fixed):**
   - Fixed number of cards in deck (e.g., 15 cards)
   - Varies by class rarity (Common: 15, Rare: 18, Epic: 21, Legendary: 24+)
   - May increase with progression/prestige upgrades
   - Purchased with Arcane Essence or prestige currency
   
2. **Per-Tier Limits (Class-Specific):**
   - **Each class defines its own per-tier limit distribution**
   - Maximum cards from each tier determined by active class
   - Common classes: Specialist focus (5 foundation / 10 primary)
   - Rare classes: Balanced multi-tier (6/7/7 distribution)
   - Epic/Legendary: More total slots and flexible distributions
   - Ensures cross-tier deck building
   - Prevents stacking only highest tier
   - Creates mechanical differentiation between classes
   
3. **Card Copy Limits:**
   - Maximum copies of same card (e.g., 2-3 copies)
   - Prevents dominant single-card strategies
   - May vary by card rarity
   - Encourages diverse deck composition

**Example Deck Constraints by Class:**

**Fire Apprentice (Common):**
```
Total Deck Size:        15 cards
Max Arcane Cards:       5 cards (foundation support)
Max Fire Cards:         10 cards (specialist focus)
Max Copies per Card:    3 copies
```

**Geomancer (Rare, Earth → Fire):**
```
Total Deck Size:        18 cards
Max Arcane Cards:       6 cards (balanced)
Max Earth Cards:        7 cards
Max Fire Cards:         7 cards
Max Copies per Card:    3 copies
```

**Constraint Scaling with Progression:**
- Early game: Common classes, tight specialist limits (5/10)
- Mid game: Rare classes, balanced multi-tier limits (6/7/7)
- Late game: Epic/Legendary classes, flexible high limits (5/8/8/8)
- Prestige: Access to better classes + possible limit upgrades

#### Deck Building Strategy
- **Resource Optimization:** Include generator cards vs combat cards
- **Synergy Building:** Cards that trigger mechanical interactions (not just multipliers)
- **Cross-Tier Composition:** Balance cards from different tiers
- **Meta Progression:** Deck improves through card levels, upgrades, prestige bonuses

### Card Mechanics

#### Card Types
- **Combat Cards:** Primary damage/defense
- **Generator Cards:** Resource generation
- **Synergy Cards:** Trigger combos with other cards
- **Utility Cards:** Special effects and abilities

#### Card Interactions (Mechanical, Not Just Multipliers)
- **Trigger Chains:** Blue card effect triggers Green combo, which triggers Yellow effect
- **Conditional Abilities:** "If you have 3+ Blue cards in play, trigger X"
- **Combo Requirements:** Multiple cards must be present for powerful effects
- **Class Enhancements:** Classes make certain combos more effective

#### No Separate Skills System
- All abilities are card-based
- No separate "skills" menu or system
- Everything players control is through deck composition

---

## Card Collection & Pack System

### Pack Types

#### Arcane Packs
- **Cost:** Arcane Essence
- **Contents:** Arcane cards, Common class cards (Apprentices), Rare class cards (low chance)
- **Always Available:** Arcane packs remain purchasable and valuable throughout game
- **Purpose:** Foundation cards, class acquisition, resource generators

#### Elemental Tier Packs
- **Cost:** Respective elemental Essence (Fire Essence, Water Essence, etc.)
- **Contents:** Cards for that element, Epic class cards (rare), Legendary classes (very rare)
- **Unlock:** Available after unlocking respective tier via class

#### Special Packs
- **Premium Packs:** Higher rarity chances (purchasable with multiple currencies)
- **Event Packs:** Limited-time themes and exclusive cards
- **Milestone Packs:** Rewarded for completing challenges

### Pack Acquisition
- **Purchased:** Buy with earned currency
- **Rewards:** Earned from combat victories, milestones, daily rewards
- **Time-Gated:** Daily free pack options
- **Milestone Rewards:** Special packs for progression achievements

---

## Duplicate Card Handling

### Duplicate Mechanics

#### Experience System
- **Card Leveling:** Each duplicate adds experience to that card
- **Level Benefits:** Higher level = better stats/effects
- **Max Level:** Cards can reach maximum level (cap increases with prestige)

#### Scraps/Crafting System
- **Break Down Duplicates:** Convert excess duplicates to crafting materials
- **Crafting Use:** Upgrade cards, craft missing cards, prestige currency conversion

#### Prestige Integration
- **Maxed Card Breakdown:** Breaking down max-level cards gives prestige currency
- **Prestige Bonuses:** Prestige currency provides permanent upgrades

#### Alternative: Fusion System (Optional)
- Merge duplicates to unlock higher rarities/versions
- Alternative to experience system for certain card types

---

## Prestige System

### Prestige Levels

#### Multiple Prestige Types
1. **Card-Level Prestige:** Reset individual card levels for permanent bonuses
2. **Deck-Level Prestige:** Reset deck composition/progress for deck bonuses
3. **Tier-Level Prestige:** Reset specific tier for tier-specific bonuses
4. **Full Game Prestige:** Reset everything for global bonuses

### Prestige Mechanics

#### Individual Tier Prestige
- **Reset Options:** 
  - Lose cards, deck, progress (start fresh)
  - OR Keep cards but reset levels/progress (to be determined)
- **Benefits:** Permanent bonuses specific to that tier
  - Increased resource generation rates
  - Better pack drop rates
  - Higher stat caps

#### Class Prestige (Optional)
- Reset specific class's tiers
- Gain class-specific permanent bonuses
- Keeps other classes' progress intact

#### Full Game Prestige
- Reset everything
- Keep class cards (permanent unlocks)
- Start fresh with better base stats
- Global bonuses affecting all tiers

#### Prestige Currency
- **Generation:** Earned by breaking down cards, completing tiers, maxing cards
- **Usage:** Purchase permanent upgrades
- **Multiple Types:** May have separate prestige currencies for different prestige levels

---

## Combat System (Session 2.0.3 - Combat-Over-Time Redesign)

**⚠️ DESIGN IN PROGRESS:** Parts A & B complete (mechanics & death system), Parts C & D pending (balance & documentation). See Session Log: `.cursor/log/sessions/session-2-0-3-combat-system-redesign.md`

### Core Combat Mechanics (Trimps-Style Combat-Over-Time)

**Design Philosophy:** Combat is fully automated with tick-based resolution. Player strategy is in deck construction. Combat happens over multiple seconds with HP depletion, creating strategic depth through timing and stat accumulation.

#### Combat Tick System

**Tick Rate:** 1.0 second per tick
- Aligns with card draw rate (1 card/second)
- Simple calculations and predictable pacing
- Combat resolves tick-by-tick until victory or death

**Damage Formulas (Per Tick):**
```
Player Damage Dealt = max(Player_Attack - Enemy_Defense, 0)
Player Damage Taken = max(Enemy_Attack - Player_Defense, 0)
```

**Key Mechanics:**
- No minimum damage (perfect defense = 0 damage taken)
- Cards drawn mid-fight break stalemates naturally
- Flat damage reduction (Attack - Defense)
- Simple, predictable calculations

#### Player HP System

**Starting HP:** 100 HP (fixed baseline)

**HP Scaling:**
- ❌ No automatic HP growth per enemy defeated
- ❌ No automatic HP growth per pack purchased
- ✅ Shard upgrades: Spend shards for permanent max HP increases (see HP Upgrade System below)
- ✅ Card mechanics: Cards can temporarily boost max HP, heal, or add HP regen

**HP Recovery:**
- ❌ No automatic healing between enemies
- ❌ No healing after victories
- ✅ Full heal only on death/respawn
- ✅ Healing via card mechanics during run (instant heal, HP regen)

**HP Upgrade System (Shard Spending):**
- **Tier 1 (HP 100 → 150):** 5 upgrades at 50/75/100/125/150 shards (+10 HP each, 500 total)
- **Tier 2 (HP 150 → 200):** 5 upgrades at 175-300 shards (+10 HP each, ~1,200 total)
- **Tier 3 (HP 200 → 300):** 10 upgrades at 325-750 shards (+10 HP each, ~5,000 total)
- **Expected progression:** ~600-700 shards by Enemy 50, enough for 5-7 upgrades (+50-70 HP)
- **Death Loop integration:** Spend shards on HP after Loop 1, start Loop 2 with 150-170 HP

**Strategic Implications:**
- HP is a precious, depleting resource
- No healing between enemies = death spiral gameplay
- Must manage HP across entire run
- Healing cards become strategically valuable
- Death is inevitable without healing strategy

#### Continuous Deck Cycling

**Card Draw Mechanic:**
- Cards draw at 1 card/second continuously
- When deck exhausts, **1-second reshuffle cooldown**
- After cooldown, deck immediately reshuffles and drawing continues
- Stats accumulate with each cycle (exponential growth)

**Example: 8-Card Deck**
```
Cycle 1 (Ticks 0-7):   Draw 8 cards → 0 to 62 ATK
Tick 8:                Reshuffle cooldown (1 second)
Cycle 2 (Ticks 9-16):  Draw 8 cards again → 62 to 124 ATK (+62)
Tick 17:               Reshuffle cooldown
Cycle 3 (Ticks 18-25): Draw 8 cards again → 124 to 186 ATK (+62)
... continues until enemy dies or player dies
```

**Reshuffle Cooldown Benefits:**
- Small decks: 8 cards + 1s cooldown = 9s cycle (11% downtime)
- Large decks: 15 cards + 1s cooldown = 16s cycle (6% downtime)
- Slightly favors larger decks (less % downtime)

**Deck Size Constraints:**
- **Minimum:** 8 cards (prevents tiny deck exploit)
- **Maximum:** Determined by active class (varies by rarity)

#### Stat Accumulation and Reset

**During Enemy Fight:**
- Cards drawn add to Attack and Defense permanently
- Stats continue accumulating with each deck cycle
- Stats reset only when enemy dies or player dies

**When Enemy Dies:**
- ✅ Player Attack → **Reset to 0**
- ✅ Player Defense → **Reset to 0**
- ✅ Essence Rate → **PERSISTS** (carries forward)
- ✅ HP → **NO HEAL** (damage carries forward to next enemy)
- ✅ Accumulated Essence → **PERSISTS**
- Next enemy spawns, stats start from 0 again

**When Player Dies:**
- ✅ Player Attack → Reset to 0
- ✅ Player Defense → Reset to 0
- ✅ Essence Rate → Reset to 0
- ✅ Current HP → **Full heal to max HP**
- ✅ Max HP → Based on permanent shard upgrades only
- ✅ Accumulated Essence → **PERSISTS** (critical for death loop)
- ✅ Enemy Progress → Reset to Enemy 1
- ✅ Card Collection → **PERSISTS**
- ✅ Deck Composition → **PERSISTS**

#### Combat Flow Example

**Enemy 50: 3,246 HP, 10 ATK (First Attacker)**
**Player: 100 HP, 8-card starter deck**

```
CYCLE 1 (Ticks 0-7: Drawing cards)
Tick 0: 0 ATK, 0 DEF
  - Damage dealt: 0 | Damage taken: 10 | Player: 90 HP

Tick 1: 20 ATK, 0 DEF (Arcane Bolt drawn)
  - Damage dealt: 20 | Damage taken: 10 | Player: 80 HP

Tick 2: 20 ATK, 18 DEF (Mystic Shield drawn)
  - Damage dealt: 20 | Damage taken: 0 (defense working!)

Ticks 3-7: Continue drawing, build to 62 ATK, 54 DEF

Tick 8: [RESHUFFLE COOLDOWN - 1 second]
  - Still dealing damage (62/tick), taking 0 damage (defense > attack)

CYCLE 2 (Ticks 9-16)
  - Stats grow: 62 → 124 ATK, 54 → 108 DEF
  - Damage accelerates

CYCLE 3+ (Ticks 17+)
  - Stats continue growing: 186 ATK, 248 ATK, etc.
  - Enemy defeated around Tick 28-29

Total Time: ~28-29 seconds
Player HP: ~80/100 (lost 20 HP before defense kicked in)
```

#### Death System

**Death Condition:** HP reaches 0 during combat
- Instant death, no "saving throw"
- Can occur at any tick (during draw or reshuffle)

**Death Screen:**
```
═══════════════════════════════════════
         DEFEATED AT ENEMY 47
═══════════════════════════════════════

 Progress: 47/50 to Mini-Boss #1
 
 This Run:
   Essence Earned:     32,450
   Shards Earned:      127
   Time Alive:         14m 23s
   
 Total Resources:
   Total Essence:      68,900
   Total Shards:       283
   
═══════════════════════════════════════
   Your deck grows stronger with
   each attempt. Spend your resources
   and try again!
═══════════════════════════════════════

 [View Collection]  [Spend Shards]  [Continue]
```

**Death Screen Tone:**
- Celebratory of progress made (not punishing)
- Shows what you earned this run
- Shows total resources available
- Encourages spending and improving

**Class Switching on Death:**
- Death screen offers class switch option (if you own other class cards)
- Can switch class before respawning
- Deck adjusts to new class's limits automatically

**Respawn Mechanics:**
- Stats reset (0 ATK, 0 DEF, 0 Essence/sec)
- HP restored to full (based on permanent max HP)
- Enemy counter resets to Enemy 1
- Accumulated essence and shards persist

#### Strategic Implications

**1. HP as Precious Resource**
- No healing between enemies
- Must survive entire run on starting HP (unless healing cards)
- Death is inevitable without healing strategy
- Creates "how far can you go?" gameplay

**2. Defense Becomes Critical**
- Must draw defense cards FAST or take heavy damage
- Defense > Enemy Attack = invulnerable
- Defense < Enemy Attack = death spiral
- Card draw order matters enormously

**3. Combat Ramp-Up Dynamics**
- Early fight: Vulnerable (low stats)
- Mid fight: Ramping (stats accumulating)
- Late fight: Overwhelming (massive stats from multiple cycles)
- Longer fights = more cycles = godlike power eventually

**4. Death Spirals Are Intentional**
- Low HP → need to survive longer → need more defense
- Creates tension and "oh no" moments
- Death loop is expected progression mechanic

**5. Card Design Space Opens Up**
- Instant heal cards (restore X HP)
- HP regen cards (+Y HP per tick for Z seconds)
- Max HP boost cards (temp +50 max HP this run)
- Defense-focused strategies become viable
- "Lifesteal" cards (deal damage, heal for %)
- Shield/barrier cards (temporary defense boost)

**6. Shard Upgrades Gain Value**
- Permanent max HP increases = run further each loop
- Permanent attack/defense boosts = faster kills, less damage
- Each death loop, spend shards to grow stronger

#### Combat Duration (Session 2.0.3 Part C - FINALIZED)

**Combat Times with Starter Deck (62 ATK, 54 DEF):**
```
Enemy 1 (20 HP):          ~2 seconds
Enemy 10 (1,100 HP):      ~17 seconds
Enemy 25 (2,900 HP):      ~29 seconds
Enemy 50 (9,768 HP):      ~47 seconds (Mini-Boss #1)
Enemy 100 (18,555 HP):    ~90 seconds (Mini-Boss #2, requires Pack 1)
Enemy 150 (38,680 HP):    ~180+ seconds (Major Boss, requires Packs 1-3)
```

**Session Milestones:**
- **~23 minutes:** Enemy 50 reached (Mini-Boss #1 - First Attacker)
- **~30 minutes:** Enemy 60 reached (alternate milestone)
- **~35 minutes:** Enemy 67 - Expected death with starter deck (HP depleted)

#### Offline Calculation (To Be Specified)

Needs redesign for combat-over-time system. Previous instant-resolution calculation obsolete.

**To Be Designed in Part C:**
- Average combat duration per enemy
- Average essence generation rate with combat duration
- Estimated progression distance for offline time

---

**⚠️ SUPERSEDED SECTIONS:**
The following sections from Version 1.8 are superseded by this combat redesign:
- Old "Combat Loop (Session 1.2 Decision)" - Replaced with tick-based combat
- Old "Two-Phase System: Charging + Combat" - No longer instant resolution
- Old "Offline Calculation" formula - Needs redesign for combat duration

**⚠️ PENDING DESIGN WORK (Parts C & D):**
- Combat duration validation and balance calculations
- Enemy HP/Attack rebalancing for combat-over-time
- Card stat range adjustments
- Updated first 30 minutes experience
- Pack affordability timing with combat duration
- Complete offline calculation redesign

---

## Combat Progression & Enemy Scaling

### Design Philosophy

The combat progression system is built around a **death-and-retry loop** where players progressively build stronger decks to overcome increasingly difficult enemies and bosses. Death is not punishment but part of the core progression loop - players keep all resources and iterate on their deck between attempts.

### Enemy Health Scaling Formula (Session 2.0.3 Part C - FINALIZED)

**Act-Based Step Function System:**

The HP formula uses a **step function** that increases base HP after each boss, creating clear progression tiers while ensuring post-boss enemies are easier than the boss itself.

**Act 1 (Enemies 1-50): Tutorial Tier**
```
Base HP = 20 + (enemy_number - 1) × 120
Enemy 49:  5,780 HP (regular)
Enemy 50:  9,768 HP (Mini-Boss #1, 1.3× multiplier)
```

**Act 2 (Enemies 51-100): Challenge Tier**
```
Base HP = 6,000 + (enemy_number - 51) × 130
Enemy 51:  6,000 HP (step up from Act 1, but < boss)
Enemy 99:  12,240 HP (regular)
Enemy 100: 18,555 HP (Mini-Boss #2, 1.5× multiplier)
```

**Act 3 (Enemies 101-150): Master Tier**
```
Base HP = 12,500 + (enemy_number - 101) × 140
Enemy 101: 12,500 HP (step up from Act 2, but < boss)
Enemy 149: 19,220 HP (regular)
Enemy 150: 38,680 HP (Major Boss, 2.0× multiplier)
```

**Act 4+ (Enemies 151+): Future Content**
```
Base HP = 38,880 + (enemy_number - 151) × 200
(To be balanced with elemental tier progression)
```

**Design Rationale:**
- **Step functions create clear Acts:** Each boss victory unlocks a new difficulty tier
- **Post-boss breathing room:** Enemy 51 < Boss 50, giving players a moment to stabilize
- **Continuous progression:** Enemy 51 > Enemy 49, ensuring forward momentum
- **Escalating challenge:** HP per enemy increases (120 → 130 → 140) across Acts
- **Boss victories feel rewarding:** Beating a boss unlocks easier content initially, then ramps back up

**Key Milestones:**
- Enemy 1: 20 HP
- Enemy 50: 9,768 HP (Mini-Boss #1 - First Attacker) ← ~23 minutes
- Enemy 100: 18,555 HP (Mini-Boss #2 - First Real Wall) ← ~60-70 minutes
- Enemy 150: 38,680 HP (Major Boss - End of "Act 1" content) ← ~120-180 minutes

### Boss Encounter System

Bosses are **progression checkpoints** that require multiple death loops with deck improvements to overcome. They serve as clear milestones, motivation to purchase packs, and achievement moments.

#### Enemy 50 - Mini-Boss #1 "Defense Tutorial" ("Lieutenant")

**Stats:**
- HP: 9,768 (1.3× regular Enemy 50 = 7,514 × 1.3)
- Attack: **10** (FIRST enemy with attack!)

**Purpose:**
- **First damage dealer** - introduces defense mechanic
- ~23-minute milestone with starter deck
- "Oh no, I'm taking damage!" tutorial moment
- Still survivable (100 HP vs 10 ATK/tick, defense cards block damage)
- Teaches that special enemies are stronger AND more dangerous
- Forces defensive card strategy for first time

**Rewards:**
- 3× regular shard drops (~6-9 shards)
- Achievement: "Survived First Assault"
- Visual celebration

**Expected Outcomes:**
- Most players survive on first loop (if defense cards drawn early)
- Some players die (if poor deck or unlucky draw order)
- Either way: Learns that defense matters now

#### Enemy 100 - Mini-Boss #2 ("Commander")

**Stats:**
- HP: 18,555 (1.5× regular Enemy 100 = 12,370 × 1.5)
- Attack: 30

**Purpose:**
- **First real wall** - bad players fail here on first loop
- Requires Pack 1 purchase OR excellent starter deck play
- Teaches importance of pack purchases and deck optimization
- Soft gate encouraging first death loop

**Rewards:**
- 3× regular shard drops (~12-18 shards)
- Achievement: "Defeated First Commander"

**Expected Outcomes:**
- Bad player (starter deck only): **Fails** - Dies around Enemy 90-100
- Average player (Pack 1): **Beats it** - Continues to ~120-140
- Good player (Pack 1-2): **Beats it** - Continues toward Enemy 150

#### Enemy 150 - Major Boss #1 ("Tower Guardian")

**Stats:**
- HP: 38,680 (2.0× regular Enemy 150 = 19,340 × 2.0)
- Attack: 80

**Purpose:**
- **Major milestone** - End of "Act 1" content
- Requires 2-3 death loops with progressive improvements
- Beating this is major achievement
- May unlock prestige system (to be designed in Session 7)

**Rewards:**
- 5× regular shard drops (~40-60 shards)
- Major achievement: "Defeated Tower Guardian"
- Possible special currency or content unlock
- Celebration sequence

**Expected Outcomes:**
- Loop 1 (starter deck): Fails at Enemy 90-100 (Commander)
- Loop 2 (Packs 1-2): Fails at Enemy 130-140
- Loop 3 (Packs 1-3): Fails at Enemy 150 boss
- Loop 4-5 (optimized): **Beats boss**

**Design Philosophy:**
- Boss is clearly impossible on first 2 loops
- Creates satisfying multi-loop progression arc
- Beating it feels earned, not lucky
- Not a "tutorial death" but a **progression wall** requiring iteration

#### Future Bosses

- **Enemy 300:** Major Boss #2, end of "Act 2"
- **Enemy 450, 600, etc.:** Every 150 enemies
- Elemental tier bosses with unique mechanics (future design)

### Enemy Attack Scaling (Session 2.0.3 - Updated for Combat-Over-Time)

**⚠️ DESIGN IN PROGRESS:** Attack scaling updated in Part A/B. Final values pending Part C balance validation.

**Phase 1: Safe Learning (Enemies 1-49)**
- Attack: **0**
- Purpose: Learn mechanics without death pressure
- HP never depletes
- Pure offense optimization
- 30 minutes of safe learning

**Phase 2: Mini-Boss #1 "Defense Tutorial" (Enemy 50)**
- Attack: **10** (FIRST enemy with attack!)
- Purpose:
  - Teaches defense matters
  - "Oh no, I'm taking damage!" moment
  - Still survivable (100 HP vs 10 ATK/tick)
  - Forces defensive card strategy
  - Natural 30-minute milestone

**Phase 3: Gradual Scaling (Enemies 51-99)**
- Formula: `10 + (enemy_number - 51) × 0.3`
- Enemy 51: 10 ATK → Enemy 99: 24.4 ATK
- Purpose: Progressive difficulty introduction
- Defense becomes increasingly important

**Phase 4: Mini-Boss #2 "First Real Wall" (Enemy 100)**
- Attack: **30** (1.3× regular Enemy 100)
- Purpose: Significant threat, Pack 1 likely needed
- Forces strategic deck building

**Phase 5: Challenge Zone (Enemies 101-149)**
- Formula: `25 + (enemy_number - 101) × 0.6`
- Enemy 101: 25 ATK → Enemy 149: 54 ATK
- Purpose: HP management becomes critical
- Death highly likely without healing strategy

**Phase 6: Major Boss (Enemy 150)**
- Attack: **80** (1.5× regular Enemy 149)
- Purpose: Major milestone, requires multiple death loops
- Expected 3-6 loops to defeat

**Design Rationale (Session 2.0.3):**
- 30 minutes of safe play before first damage = perfect tutorial arc
- Clear "before/after" moment at Mini-Boss #1
- Boss encounters every ~50 enemies = consistent rhythm
- Each boss teaches new lesson (defense, optimization, HP management)

### Death and Respawn System

**CRITICAL DISTINCTION:** Death loop is **NOT prestige**. It's the normal gameplay loop.

#### What Happens on Death

1. **Death Trigger:** Player loses (insufficient defense, can't beat boss, etc.)

2. **Death Screen Shows:**
   - Enemies defeated: "You reached Enemy 94"
   - Essence earned this run
   - Shards earned this run
   - Achievements unlocked
   - Progress indicator: "94/150 to Tower Guardian"

3. **Resources Kept (Everything Persists):**
   - ✅ All cards in collection
   - ✅ All essence (spend on packs)
   - ✅ All shards (spend on upgrades)
   - ✅ Current deck composition
   - ✅ Card levels/upgrades purchased
   - ✅ All progress and unlocks

4. **Player Actions After Death:**
   - Spend essence on new packs
   - Spend shards on card upgrades, deck size increases
   - Rebuild/optimize deck
   - **Swap class** (if you own other class cards)
   - Review achievements

5. **Respawn:** Click "Continue" → Restart at Enemy 1 with improved deck

**This Loop Is Core Gameplay:**
- Fight → Die → Spend resources → Improve deck → Fight again
- Like dying in Rogue Legacy and buying upgrades before next run
- Expected to loop 3-6 times to beat first major boss
- No penalty for death, just natural progression rhythm

#### Death vs Prestige (Clarification)

| Mechanic | Trigger | What Resets | What Persists | Rewards |
|----------|---------|-------------|---------------|---------|
| **Death Loop** | Die to enemy/boss | Enemy progress only | Everything (cards, essence, shards, deck) | None (just retry) |
| **Prestige** | Manual choice (late game) | TBD (Session 7) | TBD (Session 7) | Permanent bonuses |

**Prestige System (To Be Designed):**
- Unlocked after beating first major boss (Enemy 150)?
- Separate advanced mechanic from normal death loop
- Provides permanent bonuses but involves real resets
- Design deferred to Session 7

### Multi-Loop Progression Expectations

#### Loop 1 - Discovery
- Starter deck only, 100 HP
- Reach: Enemy 100-120
- Die to: HP depletion or stronger enemies
- Accumulate: ~300,000 essence, ~600-700 shards
- **Action:** Purchase Pack 1, save shards for HP upgrades

#### Loop 2 - Improvement
- Pack 1 cards + HP upgrades (150-170 HP)
- Reach: Enemy 130-140
- Die to: Approaching Enemy 150 boss or HP depletion
- Accumulate: More essence and shards
- **Action:** Purchase Packs 2-3, more HP upgrades

#### Loop 3 - Approach
- Packs 1-2-3 + HP upgrades (180-200 HP)
- Reach: Enemy 145-150
- Die to: Major Boss first attempts
- Accumulate: More essence/shards
- **Action:** Optimize deck composition, final HP upgrades

#### Loop 4-6 - Victory
- Fully optimized deck with Packs 1-3 + 200+ HP
- Reach: Enemy 150 (Major Boss)
- Close attempts, eventually **BEAT BOSS**
- **Milestone:** Major achievement unlocked

**Total Time to First Boss Victory:**
- Bad players: ~3-4 hours (6-7 loops)
- Average players: ~2-3 hours (4-5 loops)
- Good players: ~1.5-2 hours (3-4 loops)

### Rewards Structure

**Regular Enemy Victories:**
- Shards: 2-3 (early) → 8-12 (late)
- Formula: `base_shards + floor(enemy_number / 50) × 2`
- Essence: From generator cards drawn during combat

**Mini-Boss Victories (50, 100):**
- 3× regular shard drops
- Achievement unlocks
- Visual celebration

**Major Boss Victory (150):**
- 5× regular shard drops
- Major achievement
- Possible special rewards (pack discount, currency, content unlock)
- Narrative moment / celebration sequence

### UI and Player Communication

**Progress Indicators:**
- Display: "Enemy 94 / 150"
- Boss warning at Enemy 149: "Major Boss Ahead"
- Visual milestone markers on progress bar

**Death Screen Tone:**
- Celebratory of progress made (not punishing)
- Shows clear next steps ("Buy packs to grow stronger!")
- Emphasizes iteration and improvement

### Balance Targets for Pack Card Design (Task 2.1)

**Combat Power Requirements:**
- Enemy 100 Mini-Boss: 9,809 HP
  - Pack 1 should provide +15-20% power over starter deck
- Enemy 150 Major Boss: 17,438 HP
  - Packs 1-3 should provide +30-40% total power

**Generator Power Requirements:**
- Pack 1: +4-5 Essence/sec per draw (vs starter +1-2)
- Pack 2: +6-8 Essence/sec per draw
- Pack 3: +10-12 Essence/sec per draw

**Combat Card Stats:**
- Pack 1: 25-35 total stats (vs starter 8-20)
- Pack 2: 40-50 total stats
- Pack 3: 60-80 total stats (Rare/Epic cards)

---

## Progression Flow

### Starting Flow

1. **Begin:** Start with Arcane tier
   - Pre-made starter deck or tutorial-guided deck building
   - Learn core mechanics: pack opening, duplicate handling, upgrades
   - Narrative: You're an apprentice mage learning to defend a tower

2. **Arcane Tier Progress:**
   - Open Arcane packs → Get Arcane spell cards
   - Build/improve deck → Auto-battles generate Arcane Essence
   - Upgrade cards, handle duplicates
   - Resource generation cards become important

3. **Class Acquisition:**
   - Find Class Card in Arcane pack (Common Apprentice or Rare class)
   - Equip Class Card → Unlocks first elemental tier
   - Example: Equip "Fire Apprentice" → Unlocks Fire tier

4. **Elemental Tier Progression:**
   - Build Fire deck → Earn Fire Essence
   - Fire cards can generate both Fire Essence and Arcane Essence
   - Open Fire packs → Get Fire cards and potentially Epic classes
   - If multi-tier class: Unlock next tier in class path

5. **Multi-Tier Engagement:**
   - Arcane tier: Active (building deck, earning Arcane Essence)
   - Fire tier: Active (building deck, earning Fire Essence)
   - Previous tiers become passive (auto-generate resources)
   - Cross-tier synergies activate

6. **Prestige Cycles:**
   - Prestige individual tiers for bonuses (Transcendence)
   - Try new classes (if found new class cards)
   - Full game prestige for global improvements

### Long-Term Progression

- **Collection:** Collect all class cards, try different class paths
- **Optimization:** Find optimal deck compositions for each tier
- **Prestige Loops:** Multiple prestige cycles for exponential growth
- **Content Unlocking:** New tiers, new classes, new mechanics unlock with progression

---

## Key Design Principles

### Deck Building as Core Strategy
- All strategic decisions revolve around deck construction
- Resource generation is a deck-building choice
- Combat effectiveness determined by deck composition
- No separate skill trees or active combat management

### Passive Play with Strategic Engagement
- Combat is fully automated
- Active engagement: deck building, pack purchasing, upgrades
- Idle resource generation while away
- Hybrid idle/active engagement model

### Tiers as Foundation
- Lower tiers remain relevant and useful
- Cross-tier interactions create depth
- Resource generation flows between tiers
- Foundation supports upper tiers rather than being replaced

### Classes as Content
- Classes are collectible content, not menu choices
- Finding new classes creates replayability
- Different class paths offer different experiences
- Class collection becomes long-term goal

### Resource Generation Strategy
- Resource generation cards create strategic deck-building decisions
- Balance combat power vs economy
- Cross-tier generation creates interesting choices
- Scaling through card levels and deck composition

---

## Resolved Design Decisions (Session 1.2)

### Class Switching Mechanics
**Decision:** Classes can only be switched during prestige resets.

**Rationale:**
- Makes class choice meaningful and strategic for each run
- Provides natural prestige incentive (want to try new class? Prestige!)
- Aligns with "light roguelike" design philosophy
- Creates clearer progression arc per class path

**Implications:**
- Players commit to a class for entire run until prestige
- Class collection becomes long-term goal
- Prestige system must be designed to feel rewarding
- Finding new class cards is significant moment

---

### Arcane Tier Combat Role
**Decision:** Arcane cards contribute to elemental tier decks (unified combat system).

**Rationale:**
- Keeps Arcane tier relevant throughout entire game
- Enables deep cross-tier synergies
- Simpler than managing multiple separate battles
- Aligns with "Tiers as Foundation" principle
- Avoids confusion of multiple simultaneous decks

**Implications:**
- Players build one "active" deck mixing Arcane + current elemental cards
- Deck size limits become critical for balance
- Arcane cards must remain competitive with elemental cards
- Cross-tier synergies are primary strategic depth
- Card power must scale appropriately across tiers

---

### Arcane Essence as Universal Currency
**Decision:** Arcane Essence is the universal upgrade currency. Elemental Essences are generated through conversion by generator cards.

**Economy Model:**
- **Arcane Essence:** Used for universal upgrades (card leveling, prestige upgrades, deck size increases, Arcane packs)
- **Elemental Essences:** Used for tier-specific packs and possibly tier-specific upgrades
- **Conversion Mechanic:** Generator cards convert Arcane Essence → Elemental Essence as their primary function

**Critical Design Insight:** Elemental Essences may ONLY be generated through conversion. Direct elemental generation may not exist. This means:
- All economy starts with Arcane Essence generation
- Elemental generator cards function as "converters" (consume Arcane, produce Elemental)
- Resource flow: Generate Arcane → Convert to Elemental → Buy Elemental packs
- Arcane generation remains foundational throughout entire game

**Rationale:**
- Supports "Arcane as foundational magic" theme perfectly
- Arcane Essence always valuable at any stage of game
- Creates strategic choices: spend on upgrades vs convert to elemental
- Unified economy model with clear resource flow
- Generator cards become "conversion specialists" rather than pure generators

**Implications:**
- Arcane generator cards are critically important
- Conversion rates must be carefully balanced
- Resource flow creates natural pacing
- Cross-tier resource generation takes on new meaning
- Economy design (Session 4) must model conversion rates

---

### Deck Size Constraints
**Decision:** Fixed deck size with multiple constraint layers. **Per-tier limits are class-specific.**

**Constraint Types:**
1. **Total Deck Size:** Fixed number (e.g., 15 cards) that may increase with progression
2. **Per-Tier Limits (Class-Specific):** Each class defines its own tier limit distribution
3. **Card Copy Limits:** Maximum copies of same card (e.g., 2-3 per unique card)

**Rationale:**
- Fixed size easiest to balance during design phase
- Multiple constraints create deep strategic choices
- Forces meaningful decisions (can't just stack best cards)
- Traditional card game feel with added complexity
- Prevents dominant strategies
- **Class-specific limits create mechanical differentiation between classes**

**Class-Specific Deck Limit Examples:**

**Fire Apprentice (Common - Fire Specialist):**
```
Total Deck Size: 15 cards
Max Arcane Cards: 5 (foundation support)
Max Fire Cards: 10 (specialist focus)
Max Copies per Card: 3
```
*Strategy:* Fire-focused specialist, relies heavily on elemental power, limited conversion capacity

**Geomancer (Rare - Earth → Fire Multi-Path):**
```
Total Deck Size: 18 cards (higher rarity = more slots)
Max Arcane Cards: 6 (balanced foundation)
Max Earth Cards: 7 (primary element)
Max Fire Cards: 7 (secondary element)
Max Copies per Card: 3
```
*Strategy:* Balanced multi-tier approach, better cross-tier synergies, more flexible deck building

**Stormlord (Epic - Air → Water → Lightning):**
```
Total Deck Size: 21 cards (epic = even more slots)
Max Arcane Cards: 5 (focused foundation)
Max Air Cards: 8
Max Water Cards: 8
Max Lightning Cards: 8
Max Copies per Card: 3
```
*Strategy:* Complex multi-element builds, maximum synergy potential

**Implications:**
- **Class Identity:** Classes feel mechanically different beyond just tier access
- **Strategic Differentiation:** Different classes encourage different deck compositions
- **Prestige Incentive:** Better classes have better/more flexible limit distributions
- **Replayability:** Different classes require different deck-building strategies
- Deck building requires careful balancing across tiers
- Must mix generator cards and combat cards strategically
- Deck constraints scale with class rarity and progression

**Future Progression Mechanics (Not Yet Designed):**
- Class leveling system to increase tier limits
- Tier-specific upgrades (spend resources to expand limits)
- Prestige bonuses for permanent limit increases
- Milestone unlocks for special limit expansions

---

### Combat Timing: Interval-Based with Card Draw
**Decision:** Timed interval combat with continuous card draw charging mechanic.

**Combat Loop Mechanics:**

**Charging Phase (Continuous):**
- Cards drawn from deck at fast intervals (e.g., every 0.5-1 second)
- Each drawn card adds its stats to accumulated Power and Defense
- Drawing continues constantly, building up combat readiness

**Combat Phase (Interval-Based):**
- Enemies arrive on slower intervals (e.g., every 10-15 seconds)
- When enemy arrives, accumulated Power becomes Attack
- Combat triggers: Attack vs Enemy Defense, Enemy Attack vs Player Defense
- Combat continues while cards keep drawing
- Victory/defeat determined, resources awarded
- Brief window before next enemy for continued charging

**Flow Example:**
```
[Charging] Draw cards → Accumulate Power/Defense
[Enemy Arrives] → Combat resolves
[Charging while Fighting] Draw more cards → Power/Defense increase
[Enemy Defeated] → Rewards given
[Charging] Brief recovery period
[Next Enemy Arrives] → Repeat
```

**Rationale:**
- Provides discrete events for feedback and excitement
- Idle-friendly (runs automatically)
- Card draw adds strategic layer (deck cycling matters)
- Interval timing easy to calculate for offline progress
- Can evolve to wave/boss system for special content
- Balances passive idle with engaging combat moments

**Implications:**
- Deck composition affects both power accumulation and combat
- Draw speed becomes potential upgrade path
- Combat interval timing critical for game feel
- Need to design enemy stats and scaling
- Combat simulation (Session 5) must model draw + intervals
- Offline calculation: (cards drawn per second × draw power) + (battles per minute × victory rewards)

**Future Evolution:** Wave-based system for boss battles, milestone events, special challenges while maintaining interval-based core.

---

## First 30 Minutes Experience (Session 1.3 - Part A)

### Starting State: Arcane Student

**Initial Setup:**
- All players start as "Arcane Student" (no class choice yet)
- Pre-built 8-card starter deck (Arcane-only)
- Apprentice class cards (Fire, Water, Earth, Air) pre-owned but locked until first prestige
- No elemental cards accessible before prestige

### Gameplay Phases (Guided Discovery)

**Phase 1: First Contact (Minutes 0-5)**
- Immediate gameplay, no menus or tutorials
- Watch combat loop: cards draw → power builds → enemy appears → victory → essence
- First mechanic: Automatic card draw and combat
- First resource: Arcane Essence starts accumulating from victories and generator draws
- Goal: Understand basic combat loop through observation

**Phase 2: Discovery (Minutes 5-12)**
- Shop unlocks when 50 Essence reached
- First pack purchased and opened (5 cards)
- Collection view unlocks
- Examine card variety (combat, generators, utilities)
- Deck building unlocks after first pack
- Goal: Learn spending resources and collecting cards

**Phase 3: Choice (Minutes 12-20)**
- First deck modification (choose which cards to include)
- See immediate impact in combat
- Passive generation becomes visible if generators included
- Second pack purchased (~50 more Essence)
- Strategic thinking emerges (economy vs combat focus)
- Goal: Experience agency and strategic choice

**Phase 4: Mastery & Glimpse Beyond (Minutes 20-30)**
- Enemy difficulty scales (more health, better rewards)
- Third pack purchased
- Deck optimization (approaching 20-card limit)
- Glimpse of future systems (locked class cards hint at prestige)
- Milestone reached: "Tower Defender I"
- Goal: Feel competent and curious about progression

### Key Milestones

1. **First Blood** (Minute 3): First enemy defeated
2. **Merchant Unlocked** (Minute 6): First pack purchased
3. **Deck Builder** (Minute 13): First deck modification
4. **Generator** (Minute 16): Passive income established
5. **Optimization** (Minute 25): Full 20-card deck built
6. **Glimpse Beyond** (Minute 28): Aware of prestige/class systems

### Progression Gates (Soft, Time-Based)

- **Gate 1** (Minute 5-6): Accumulate 50 Essence → Unlock pack purchasing
- **Gate 2** (Minute 11-12): Own more cards than starter deck → Unlock deck building
- **Gate 3** (Minute 20+): Multiple packs + refinement → Awareness of future systems
- No hard gates: combat continues, resources accumulate, player-driven pacing

### Design Philosophy Applied

**Guided Discovery (No Hand-Holding):**
- Systems reveal themselves through visual feedback
- No tutorial popups or forced explanations
- Complexity expands naturally (observe → explore → act → optimize)
- New UI elements appear when relevant, not forced

**Emotional Arc:**
- Minutes 0-5: Curiosity ("What's happening?")
- Minutes 5-15: Discovery ("I can do things!")
- Minutes 15-25: Mastery ("I'm getting better!")
- Minutes 25-30: Ambition ("What's next?")

### Critical Design Decisions for First 30 Minutes

**Pack Cost Scaling** (Session 1.3):
- Formula: 50 × 1.5^n (50, 75, 110, 165, 245...)
- Creates natural pacing, prevents runaway progression
- Each pack feels earned

**Guaranteed Cards** (Session 1.3):
- First 2 packs have fixed distributions
- Pack 1: 2 generators, 2 combat, 1 utility
- Pack 2: 1 generator, 3 combat, 1 rare synergy
- Pack 3+: Random
- Ensures consistent experience and teaches card variety

**Defense Mechanics** (Session 1.3):
- Defense stat exists on cards
- Early enemies have weak/zero attack
- No failure state during learning phase
- Becomes strategic later

**Class Cards** (Session 1.3):
- All 4 Apprentice classes pre-owned from start
- Grayed out with "Unlocked after first prestige" tooltip
- Creates visible long-term goal
- Unlocked automatically on first prestige

### End State (Minute 30)

**Player Progress:**
- 3-4 packs opened (25-28 cards owned)
- 20-card optimized Arcane deck
- ~5-7 Essence/sec passive generation rate
- Consistent combat victories against scaled enemies
- Aware of prestige and class systems (but not accessible)

**Player Understanding:**
- Combat loop mastery
- Resource economy (essence from generators, shards from victories)
- Deck building strategy (generator/combat balance)
- Progression path (packs → cards → deck → power)
- Long-term goals visible (prestige, classes, elements)

**Player Feeling:**
- Competent with core systems
- Curious about next progression steps
- Satisfied with first session progress
- Motivated to continue playing

### Notes for Parts B & C

**Part B (Baseline Numbers) Must Define:**
- Generator card rates (+X Essence/sec per draw)
- Shard drop amounts per victory
- Pack cost scaling formula implementation (50 × 1.5^n)
- Enemy health/timing for proper pacing
- Deck cycling speed calculations
- Time to reach each milestone with correct economy

**Part C (Starter Cards) Must Define:**
- 8 starter cards with exact stats
- Guaranteed cards for packs 1 & 2
- Card types: generators, combat, utilities
- Validation against 30-minute experience timeline

---

## Baseline Numbers Reference (Session 1.3 - Part B)

### Core Game Timing

**Card Draw & Combat:**
- Card draw speed: 1.0 second per card (60 cards/minute constant)
- Enemy arrival: Every 12 seconds (5 enemies/minute)
- Combat resolution: Instant when enemy arrives

### Generator Card Rates (Essence Generation)

**Mechanic:** Every draw of a generator adds to rate (stacks, even duplicates); rate persists until death.

**Starter Deck:**
- "Arcane Spark": **+1 Essence/sec per draw**
- "Mana Trickle": **+2 Essence/sec per draw**

**Pack 1 Generators:**
- "Arcane Conduit": **+3 Essence/sec per draw**
- "Essence Flow": **+4 Essence/sec per draw**

**Pack 2 Generator:**
- "Greater Conduit": **+5 Essence/sec per draw**

**Random Generators (Pack 3+):**
- Common: **+2 to +4 per draw**
- Rare: **+5 to +7 per draw**
- Epic: **+10+ per draw**

**Expected Rate Progression:**
- Minutes 0-8: 0 → 180 Essence/sec (from ~120 draws)
- Minutes 8-17: 180 → 652 Essence/sec
- Minutes 17-27: 652 → 1,252 Essence/sec
- Minutes 27-30: 1,252 → 1,500 Essence/sec

### Pack Costs (Essence)

**Formula:** 40,000 × 2.5^(n-1)

**Pricing:**
- Pack 1: **40,000 Essence** (minute 8-9)
- Pack 2: **100,000 Essence** (minute 16-17)
- Pack 3: **250,000 Essence** (minute 26-27)
- Pack 4: **625,000 Essence** (minute 32-35, beyond first session)
- Pack 5+: **1,562,500+**

**Pack Contents:**
- 5 cards per pack
- First 2 packs: Guaranteed distributions
- Pack 3+: Random by rarity weights

### Shard System (Combat Rewards)

**Drops per Victory:**
- Early (0-10 min): 2-3 Shards
- Mid (10-20 min): 4-6 Shards
- Late (20-30 min): 8-12 Shards

**Accumulation (Session 2.0.3 Part C - Adjusted for Combat Duration):**
- Total by Enemy 50 (~23 min): ~600-700 Shards
- Total by Enemy 60 (~30 min): ~700-800 Shards

**Usage:**
- **HP upgrades:** 50/75/100/125/150 shards per +10 HP (Tier 1)
- Card upgrades: 50-100+ Shards
- Deck size increase: 200+ Shards
- Permanent upgrades: Variable

### Enemy Stats

**✅ FINALIZED (Session 2.0.3 Part C - Act-Based Scaling)**

See **"Combat Progression & Enemy Scaling"** section for complete specifications.

**Quick Reference - HP Scaling:**
- **Act 1 (1-50):** `HP = 20 + (n-1) × 120`
- **Act 2 (51-100):** `HP = 6,000 + (n-51) × 130`
- **Act 3 (101-150):** `HP = 12,500 + (n-101) × 140`

**Boss HP:**
- Mini-Boss #1 (Enemy 50): 9,768 HP (1.3× multiplier)
- Mini-Boss #2 (Enemy 100): 18,555 HP (1.5× multiplier)
- Major Boss (Enemy 150): 38,680 HP (2.0× multiplier)

**Attack Scaling:**
- Enemies 1-49: 0 attack (safe learning)
- Enemy 50: 10 attack (first attacker)
- Enemies 51-99: 10 + (n-51) × 0.3
- Enemy 100: 30 attack
- Enemies 101-149: 25 + (n-101) × 0.6
- Enemy 150: 80 attack

### Combat Card Stats

**Starter Deck Range:**
- Attack: 4-10
- Defense: 2-10
- Total: 8-15 stat points

**Pack 1 Cards:**
- Attack: 12-18
- Defense: 5-12
- Total: 25-30 stat points

**Pack 2 Cards:**
- Attack: 20-30
- Defense: 8-15
- Total: 35-45 stat points

**Pack 3+ Cards:**
- Rare: 50-80 total stat points
- Epic: 100-150 total stat points

**Power Accumulation:**
- Initial: ~8 Attack/sec
- After Pack 1: 15-25 Attack/sec
- By minute 30: 40-60 Attack/sec

### Deck Composition Guidelines

**Generator Percentage:** Stays constant at 25-35% of deck across all stages

**Starter (8 cards):**
- 2 Generators (25%)
- 5 Combat (62.5%)
- 1 Utility (12.5%)

**Optimized (20 cards):**
- 6-7 Generators (30-35%)
- 12-13 Combat (60-65%)
- 1-2 Utility (5-10%)

### Validated Pacing (Starter Deck Only - "Bad Player" Baseline)

**✅ VALIDATED (Task 2.0 + Session 2.0.3 Part C):**
- ✓ Pack 1 affordable at ~7.0 minutes (40,000 Essence)
- ✓ Pack 2 affordable at ~11.5 minutes (100,000 Essence)
- ✓ Pack 3 affordable at ~18.5 minutes (250,000 Essence)
- ✓ Generation rate scales: 0 → 180 → 382 → 607 Essence/sec (starter deck only)
- ✓ Card draw rate: 60 cards/min (1 card/sec)
- ✓ Enemy 50 reached at ~23 minutes (Mini-Boss #1 - First Attacker)
- ✓ Enemy 60 reached at ~30 minutes (alternate milestone)
- ✓ Player death at Enemy 67 (~35 minutes with starter deck, 100 HP)
- ✓ Combat durations: 2s → 17s → 47s (Enemies 1/10/50)

**✅ FINALIZED (Session 2.0.3 Parts A-D):**
- ✓ Enemy HP scaling: Act-based step function (120/130/140 per enemy by Act)
- ✓ Boss HP: 9,768 / 18,555 / 38,680 (Enemies 50/100/150)
- ✓ Attack scaling: 0 until Enemy 50, then progressive (10/30/80 for bosses)
- ✓ HP upgrade system: 50/75/100/125/150 shards for +10 HP (Tier 1)
- ✓ Death loop progression: 4-6 loops to beat Enemy 150

**STILL NEEDS DESIGN (Task 2.1+):**
- "Good player" progression with Pack 1-3 card improvements
- Target essence rates with optimized decks
- Card stat ranges for Packs 1-3
- Combat card design (healing, HP regen, shields)
- Post-Enemy 150 content and prestige system

---

## Starter Deck Specification (Session 1.3 - Part C)

### The 8 Starter Cards

All players begin as "Arcane Student" with this pre-built 8-card deck. All cards are Arcane tier, Common rarity, with flat values and no complex abilities.

#### Generator Cards (3 cards)

**1. Arcane Conduit** - Rate Generator
- **Generation:** +2 Essence/sec when drawn
- **Attack:** —
- **Defense:** —
- **Flavor:** *"A stable channel of pure arcane energy. Draw upon it to fuel your magic."*
- **Identity:** Pure rate-building. Increases ongoing income permanently (until death).

**2. Essence Burst** - Burst Generator
- **Generation:** +150 Essence when drawn (flat amount)
- **Attack:** —
- **Defense:** —
- **Flavor:** *"A concentrated surge of magical energy, released all at once."*
- **Identity:** Immediate payoff. Doesn't increase rate, but provides instant essence.

**3. Combat Siphon** - Hybrid Generator
- **Generation:** +1 Essence/sec when drawn
- **Attack:** 12
- **Defense:** 6
- **Flavor:** *"Draw power from combat itself, channeling the clash into usable essence."*
- **Identity:** Does both roles. Less efficient at generation, but contributes to combat.

#### Combat Cards (5 cards)

**4. Arcane Bolt** - Pure Offense
- **Attack:** 20
- **Defense:** —
- **Flavor:** *"A focused blast of raw magical force."*
- **Identity:** Glass cannon. Maximum offensive power, no defensive capability.

**5. Mystic Shield** - Pure Defense
- **Attack:** —
- **Defense:** 18
- **Flavor:** *"A shimmering barrier of protective magic."*
- **Identity:** Pure survival. Maximum defensive power, no offensive capability.

**6. Balanced Strike** - Generalist
- **Attack:** 10
- **Defense:** 10
- **Flavor:** *"Harmonious magic balancing offense and defense."*
- **Identity:** Versatile middle ground. Competent at both roles.

**7. Power Strike** - Offense-Leaning
- **Attack:** 15
- **Defense:** 5
- **Flavor:** *"Aggressive magic that prioritizes overwhelming force."*
- **Identity:** Damage-focused but not reckless. Middle option between specialist and generalist.

**8. Stalwart Guard** - Defense-Leaning
- **Attack:** 5
- **Defense:** 15
- **Flavor:** *"Patient, enduring magic that outlasts threats."*
- **Identity:** Survival-focused but not passive. Middle option between specialist and generalist.

### Starter Deck Composition

**Total:** 8 cards
- **Generators:** 3 cards (37.5%) - mix of rate, burst, and hybrid
- **Combat:** 5 cards (62.5%) - mix of specialists and generalists

**Total Stats When All Cards Drawn:**
- Attack: 62 total (20+10+15+5+12)
- Defense: 54 total (18+10+5+15+6)
- Rate Generation: +3 Essence/sec (2+1 from generators)
- Burst Generation: +150 Essence

### Design Philosophy

**All Flat Values:** No conditional effects, utilities, or complex mechanics. Complexity introduced progressively through packs.

**Different, Not Better:** Each card has unique identity and purpose. No strictly superior options:
- Rate vs Burst vs Hybrid generators (different strategies)
- Pure specialist vs generalist vs leaning combat cards (different balance points)

**What Players Learn:**
- Generator diversity (rate building, immediate payoff, hybrid approach)
- Combat variety (specialization, balance, various distributions)
- Deck building foundation (different cards for different strategies)

### Future Progression

**Pack 1:** Introduces conditional bonuses and simple synergies
**Pack 2:** Introduces sequencing effects and multiplier generators
**Pack 3+:** Full complexity (deck manipulation, state-based effects, advanced synergies)

**Future Card Type:** Multiplier generators (e.g., "+(Current rate × 5 seconds) Essence") - scales with accumulated rate, creates natural sequencing strategy.

---

## Outstanding Design Questions (Remaining)

### Still To Be Determined
2. **Secondary Class Slot:** Can prestige unlock passive bonuses from inactive class?
6. **Prestige Reset Details:** What exactly resets (cards, levels, progress, or combinations)?
7. **Card Rarity System:** How many rarities? How do rarities affect stats/abilities?

---

## Notes & Future Considerations

- UI/UX design to follow after core mechanics are solidified
- Balancing will require playtesting and iteration
- Additional systems (events, achievements, etc.) can be added later
- This document serves as the foundational design - details will be refined during development
- Future elements (Lightning, Ice, Shadow, Light, Nature, Magma) can be added as expansion content

---

## Document Changelog

**Version 1.9** (2025-11-07 22:00:00) - Session 2.0.3: Combat System Redesign COMPLETE (Parts A-D)
- **MAJOR REDESIGN:** Combat changed from instant-resolution to Trimps-style combat-over-time
- **ALL PARTS COMPLETE:** Combat mechanics, death system, balance calculations, and documentation finalized
- **Part A - Combat Mechanics:**
  - Combat tick system: 1.0 second per tick
  - Damage formulas: ATK - DEF per tick (no minimum damage)
  - Player HP system: 100 HP starting, shard upgrades only, no auto-healing
  - Continuous deck cycling with 1-second reshuffle cooldown
  - Stat accumulation and reset mechanics (ATK/DEF reset per enemy, essence rate persists)
  - Deck minimum size: 8 cards (prevents tiny deck exploit)
- **Part B - Death & Respawn System:**
  - Death condition: HP = 0 triggers death
  - Respawn: Enemy 1 with full HP, keep all resources (essence, shards, cards, deck)
  - Death screen: Celebratory tone showing progress and resources earned
  - Class switching: Can switch class on death (if own multiple class cards)
  - Death loop is core gameplay, NOT prestige (prestige deferred to Session 7)
- **Part C - Balance & Scaling (FINALIZED):**
  - **NEW Enemy HP Formula: Act-based step function**
    - Act 1 (1-50): `HP = 20 + (n-1) × 120`
    - Act 2 (51-100): `HP = 6,000 + (n-51) × 130`
    - Act 3 (101-150): `HP = 12,500 + (n-101) × 140`
  - **Boss HP values:**
    - Enemy 50: 9,768 HP (1.3× multiplier, ~23-minute milestone)
    - Enemy 100: 18,555 HP (1.5× multiplier)
    - Enemy 150: 38,680 HP (2.0× multiplier)
  - **Step function design:** Post-boss enemies easier than boss but harder than pre-boss
    - Enemy 51 (6,000 HP) < Boss 50 (9,768 HP) but > Enemy 49 (5,780 HP)
    - Creates "breathing room" after boss victories
    - Escalating challenge: HP per enemy increases across Acts (120→130→140)
  - **HP Upgrade System designed:**
    - Tier 1: 50/75/100/125/150 shards for +10 HP each (500 shards for +50 HP)
    - ~600-700 shards earned by Enemy 50
    - Death loop: Upgrade HP between loops for longer runs
  - **Combat duration validation:**
    - Enemy 1: ~2s, Enemy 10: ~17s, Enemy 50: ~47s
    - Enemy 50 at ~23 min (close to 30-min target)
    - Enemy 60 at ~30 min (alternate milestone)
    - Player death at Enemy 67 (~35 min with 100 HP starter deck)
  - **Pack affordability: UNCHANGED** (essence generation independent of combat duration)
- **Part D - Documentation:**
  - Updated "Combat Progression & Enemy Scaling" with act-based formula
  - Updated "Baseline Numbers Reference" with new combat durations
  - Updated multi-loop progression expectations (4-6 loops to beat Enemy 150)
  - Updated "Validated Pacing" with finalized milestones
  - All boss HP values updated throughout document
  - Attack scaling finalized (0 until Enemy 50, progressive scaling after)
- **Strategic implications:**
  - HP management critical (no healing between enemies)
  - Defense essential (first attack at Enemy 50)
  - Combat ramp-up dynamics (exponential stat growth during fight)
  - Death spirals intentional (creates tension)
  - Opens card design space (healing, HP regen, shields, max HP boosts)
  - Shard upgrades provide meaningful progression (HP, attack, defense)
  - Act structure creates clear progression tiers
- **Session Log:** `.cursor/log/sessions/session-2-0-3-combat-system-redesign.md`
- **Balance Calculations:** `.cursor/log/balance/` (part-c-findings.md, part-c-summary.md, final-hp-formula.md)
- **Status:** COMPLETE - Ready for Task 2.0.4 (implementation) and Task 2.1 (pack card design)

**Version 1.8** (2025-11-07) - Task 2.0.1: Combat Progression Design Complete
- Added complete "Combat Progression & Enemy Scaling" section
- Finalized enemy health scaling formula (linear: `20 + (n-1) × 65.8`)
- Designed boss encounter system:
  - Mini-Boss #1 at Enemy 50 (4,220 HP, 1.3× multiplier)
  - Mini-Boss #2 at Enemy 100 (9,809 HP, 1.5× multiplier)
  - Major Boss at Enemy 150 (17,438 HP, ≈2× multiplier)
- Specified death-and-respawn loop (NOT prestige):
  - Keep all resources (cards, essence, shards, deck)
  - Spend resources between loops to grow stronger
  - Can swap class on death (if have class cards)
  - Expected 3-6 loops to beat first major boss
- Clarified death loop vs prestige distinction (prestige to be designed in Session 7)
- Defined multi-loop progression expectations (Loop 1-5 targets)
- Specified rewards structure (regular, mini-boss, major boss)
- Added balance targets for Task 2.1 (Pack card design)
- Updated Baseline Numbers section with finalized enemy stats
- Inspired by "Rogue with the Dead" death-as-progression design philosophy

**Version 1.7** (2025-11-07) - Task 2.0 Corrections: Simulator Results Integrated
- Corrected starter deck total attack (62 not 72)
- Updated enemy scaling section (marked as needing design review)
- Replaced "Validated Pacing" with actual Task 2.0 simulator results
- Distinguished "bad player" baseline (validated) from "good player" targets (needs design)
- Marked combat progression as needing design session (Session 2.X to be added)
- Added note that linear scaling is temporary implementation, not final design decision
- Clarified what's validated vs what still needs design work

**Version 1.6** (2025-11-06) - Session 1.3C: Starter Deck Design Complete
- Added complete 8-card starter deck specification
- 3 generator types: Rate (+2/sec), Burst (+150 flat), Hybrid (+1/sec + 12/6)
- 5 combat cards: Pure specialists, generalists, and various balance points
- All flat values, no complex mechanics in starter deck
- Generator diversity: rate building, immediate payoff, hybrid approach
- Combat variety: offense/defense specialists and various distributions
- Design philosophy: Different strategies, not power levels
- Future progression outlined (Pack 1: conditions, Pack 2: sequencing, Pack 3+: full complexity)
- Identified future card type: Multiplier generators (rate × time)
- Task 1.3 (High-Level Experience) fully complete

**Version 1.5** (2025-11-06) - Session 1.3B: Baseline Numbers FINAL
- **CORRECTED generator mechanic:** Stacking on every draw (including duplicates)
- Generator rates: **+1, +2, +3, +4, +5 Essence/sec per draw** (stacking)
- Pack cost formula: **40,000 × 2.5^(n-1)** (adjusted for stacking accumulation)
- Pack timing: 8-9 min, 16-17 min, 26-27 min (evenly distributed)
- Rate progression: 0 → 180 → 652 → 1,252 → 1,500 Essence/sec
- Validated stacking accumulation math through complete timeline
- Confirmed: 3 packs in 30 minutes with proper pacing
- Clean integer rates for satisfying idle game progression

**Version 1.4** (2025-11-06) - Session 1.3B: Baseline Numbers (SUPERSEDED)
- Initial baseline numbers (non-stacking mechanic, incorrect)
- Corrected in Version 1.5

**Version 1.3** (2025-11-06) - Session 1.3: First 30 Minutes Experience (Part A)
- Added "First 30 Minutes Experience" section with complete minute-by-minute narrative
- Resolved 7 additional design questions:
  - Pack cost scaling (50 × 1.5^n)
  - Guaranteed cards in first packs
  - Arcane-only content before prestige
  - Defense mechanics for early game
  - Deck limit display for Arcane Student
  - Split resource economy (Essence vs Shards)
  - Class card unlock approach (pre-owned, locked until prestige)
- **Major Economy Clarification:** Generators work on DRAW, not passive in deck
  - Generation rate accumulates as cards are drawn
  - Rate persists between enemies, resets on death
  - Critical mechanic for balancing and gameplay feel
- Updated Resource Generation System with draw-based generator mechanics
- Added split resource flow model (Essence for packs, Shards for upgrades)
- Defined starting state (Arcane Student, 8-card starter deck)
- Mapped progression gates and milestones for first 30 minutes
- Applied guided discovery philosophy (no hand-holding tutorials)
- Removed question 8 from outstanding questions (pack pricing resolved)

**Version 1.2** (2025-11-04) - Session 1.2: Critical Design Decisions
- Resolved 5 critical design questions:
  - Class switching (prestige-only)
  - Arcane combat role (unified deck)
  - Arcane Essence economy (universal currency + conversion mechanic)
  - Deck size constraints (fixed with multi-layer limits)
  - Combat timing (interval-based with card draw)
- **Refinement:** Per-tier deck limits are class-specific (creates mechanical class differentiation)
- Updated Resource Generation System with conversion mechanic
- Updated Deck Building System with class-specific constraint specifications
- Updated Combat System with detailed card draw mechanics
- Updated Class System with switching restrictions and deck limit profiles
- Added "Resolved Design Decisions" section
- Removed questions 1, 4, 5, 9, 10 from outstanding questions

**Version 1.1** (2025-11-04) - Theme Integration
- Theme established: Elemental Magic Tower Defense
- Element system defined
- Currency names finalized

**Version 1.0** - Initial Design Document
- Core mechanics established
- Tier and class systems defined
- Initial design questions identified

---

**Document Version:** 1.9  
**Last Updated:** 2025-11-07 22:00:00 (Session 2.0.3 Complete - Combat System Redesign)  
**Status:** Combat system redesign COMPLETE. All parts finalized (A: mechanics, B: death system, C: balance, D: documentation). Ready for Task 2.0.4 (implementation) and Task 2.1 (pack card design). See session log: `.cursor/log/sessions/session-2-0-3-combat-system-redesign.md` and balance calculations: `.cursor/log/balance/`

