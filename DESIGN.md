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

## Combat System

### Fully Passive Combat with Card Draw Mechanic

**Core Principle:** Combat is fully automated. Player strategy is in deck construction, not combat management.

#### Combat Loop (Session 1.2 Decision)

**Two-Phase System: Charging + Combat**

**Phase 1: Charging (Continuous)**
- Cards drawn from deck at fast intervals (e.g., every 0.5-1 second)
- Each drawn card adds its stats to accumulated Power and Defense
- Drawing continues constantly, building combat readiness
- Deck cycles and reshuffles when exhausted
- Power/Defense accumulate over time

**Phase 2: Combat (Interval-Based)**
- Enemies arrive at regular intervals (e.g., every 10-15 seconds)
- When enemy arrives:
  - Accumulated Power becomes Attack value
  - Player Defense vs Enemy Attack
  - Player Attack vs Enemy Defense
  - Victory/defeat determined
  - Rewards granted on victory
- Card drawing continues during combat
- Brief recovery period after enemy defeat before next enemy

**Combat Flow Example:**
```
Time 0-10s:   [CHARGING] Draw cards continuously, Power/Defense build up
Time 10s:     [ENEMY ARRIVES] Combat resolves with accumulated stats
Time 10-25s:  [FIGHTING + CHARGING] Combat ongoing, cards still drawing
Time 25s:     [ENEMY DEFEATED] Rewards granted
Time 25-35s:  [CHARGING] Brief recovery, power accumulates
Time 35s:     [NEXT ENEMY] Cycle repeats
```

#### Combat Mechanics
- **Auto-Battles:** Fully automated, no player input during combat
- **Card Draw Strategy:** Deck composition and draw order matter
- **Stat Accumulation:** Cards drawn = power built
- **Deck Cycling:** Fast draw means deck cycles multiple times per enemy
- **Results:** Victories earn resources, unlock content, progress milestones

#### Combat Triggers
- **Interval-Based Battles:** Enemies arrive at regular intervals
- **Milestone Battles:** Special boss/challenge battles (different intervals/mechanics)
- **Event Battles:** Periodic special encounters
- **Wave System (Future):** Boss waves, escalating challenges

#### Combat Progression
- **Difficulty Scaling:** Enemy stats scale with player progression
- **Victory Rewards:** Resources (primarily Arcane Essence), pack unlocks, milestone progress
- **Defeat Consequences:** May slow progression, but no permanent loss (light roguelike)
- **Draw Speed Upgrades:** Potential progression path (draw cards faster)
- **Interval Tuning:** Enemy arrival intervals may change with progression

#### Offline Calculation
Offline progress calculated as:
```
Cards Drawn = (Draw Rate × Time Away)
Power Accumulated = Sum of drawn card stats
Battles Fought = (Time Away / Battle Interval)
Estimated Victories = Battle Win Rate × Battles Fought
Resources Earned = Victories × Reward per Victory
```

#### Strategic Implications
- **Deck Cycling Speed:** Smaller decks cycle faster, larger decks cycle slower
- **Card Draw Order Matters:** For draw mechanic to be meaningful, order must affect outcomes
- **Generator Cards in Draw:** Drawing generator cards may trigger generation effects
- **Combat Power Curve:** Deck must accumulate power faster than enemy difficulty scales
- **Balanced Deck Required:** Need both generators (economy) and combat cards (power)

#### Order-Dependent Card Effects (To Be Designed in Session 5)

**Critical Design Note:** Card draw order must create meaningful variance, otherwise draw mechanic is unnecessary.

**Potential Order-Dependent Mechanics:**
- **Multipliers:** "Next 3 cards deal +50% damage"
- **Modifiers:** "Next card's attack is doubled"
- **Combo Chains:** Card A enhances Card B if drawn in sequence
- **Temporary Buffs:** "For next 5 cards drawn, +10 power"
- **Conditional Effects:** "If previous card was Fire, trigger X"
- **Persistent State:** Some effects last until deck reshuffle
- **Reset Triggers:** Effects may reset on enemy defeat, deck cycle, or time intervals

**State Management Considerations:**
- What persists across enemy defeats?
- What resets on deck reshuffle?
- How do effects stack or override each other?
- Timing of effect application vs resolution

**Design Goal:** Draw order creates strategic variance without making combat unpredictable or unbalanced.

**To Be Specified:** Session 5 will design concrete card effect types, timing rules, and state management.

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

## Outstanding Design Questions (Remaining)

### Still To Be Determined
2. **Secondary Class Slot:** Can prestige unlock passive bonuses from inactive class?
3. **Resource Generation Balance:** Low rate (many cards needed) vs high rate (few needed)?
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

**Document Version:** 1.3  
**Last Updated:** 2025-11-06 19:51:18 (Session 1.3 - First 30 Minutes Experience)  
**Status:** First 30 Minutes Defined (Part A Complete), Ready for Baseline Numbers (Part B) and Starter Cards (Part C)

