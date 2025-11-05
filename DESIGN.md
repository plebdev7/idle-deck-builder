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

#### Class Mechanics
- **Activation:** Equip a Class Card to unlock its tier path
- **Single Active Class:** Only one class active at a time
- **Switching:** 
  - Unequip current class → Equip new class
  - May require prestige or cost (to be determined)
- **Collection:** Can collect multiple class cards, choose which to use

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

#### Resource Generation Cards
- **Pure Generators:** Cards that primarily generate resources (weaker combat stats)
  - Example: "Arcane Conduit" - Generates +2 Arcane Essence/second while in deck
- **Hybrid Cards:** Cards that generate resources AND have combat abilities
  - Example: "Victory Harvest" - +5 Arcane Essence per battle won + combat ability
- **Conditional Generators:** Cards that generate based on game state or combos
  - Example: "Elemental Resonance" - While in deck, each Fire card generates +1 Fire Essence/second

#### Scaling Mechanisms
- **Card Leveling:** Upgrade cards to increase their resource generation rate
- **Card Quantity:** Number of generator cards in deck affects total generation
- **Synergies:** Cross-tier synergies can boost resource generation

#### Cross-Tier Resource Generation
- **Multi-Currency Cards:** Higher tier cards can generate multiple currencies
  - Fire card might generate both Fire Essence and Arcane Essence
  - Advanced elemental cards might generate multiple Essences
- **Foundation Support:** Arcane tier cards can generate resources for elemental tiers (less efficient)
- **Strategic Balance:** Players balance combat power vs resource generation in deck composition

#### Resource Generation Rates
- **Scaling with Card Level:** Upgrade cards to increase generation
- **Deck Composition Matters:** More generator cards = faster economy, but weaker combat
- **Balanced Strategy:** Optimal decks balance generators and combat cards

---

## Deck Building System

### Core Deck Mechanics

#### Deck Constraints
- **Size Limits:** Fixed deck size OR variable with diminishing returns
- **Point/Cost System:** Each card has a cost; deck budget increases with progression
- **Type Restrictions:** Max copies per card, minimum/maximum of certain types
- **Synergy Bonuses:** Matching sets or factions provide bonuses

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

### Fully Passive Combat

**Core Principle:** Combat is fully automated. Player strategy is in deck construction, not combat management.

#### Combat Mechanics
- **Auto-Battles:** Decks battle automatically against NPCs
- **No Active Input:** No clicking or manual skill usage during combat
- **Performance Based on Deck:** Deck composition determines combat effectiveness
- **Results:** Victories earn resources, unlock content, progress story/milestones

#### Combat Triggers
- **Continuous Battles:** Auto-battles run continuously based on deck power
- **Milestone Battles:** Special boss/challenge battles (may have different mechanics)
- **Event Battles:** Periodic special encounters

#### Combat Progression
- **Difficulty Scaling:** Enemies scale with player progression
- **Victory Rewards:** Resources, pack unlocks, milestone progress
- **Defeat Consequences:** May slow progression, but no permanent loss (light roguelike)

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

## Outstanding Design Questions

### To Be Determined
1. **Class Switching Cost:** Free anytime, cost currency, only on prestige, or hybrid?
2. **Secondary Class Slot:** Can prestige unlock passive bonuses from inactive class?
3. **Resource Generation Balance:** Low rate (many cards needed) vs high rate (few needed)?
4. **Gray Tier Combat Role:** Independent battles, contributes to colored decks, or passive bonuses?
5. **Gray Points as Universal Currency:** Gray-only, convertible, or global upgrade currency?
6. **Prestige Reset Details:** What exactly resets (cards, levels, progress, or combinations)?
7. **Card Rarity System:** How many rarities? How do rarities affect stats/abilities?
8. **Pack Pricing:** How do pack costs scale? Fixed or dynamic pricing?
9. **Deck Size Limits:** Fixed size, variable with diminishing returns, or point-based?
10. **Combat Timing:** Continuous auto-battles, timed intervals, or event-based?

---

## Notes & Future Considerations

- UI/UX design to follow after core mechanics are solidified
- Balancing will require playtesting and iteration
- Additional systems (events, achievements, etc.) can be added later
- This document serves as the foundational design - details will be refined during development
- Future elements (Lightning, Ice, Shadow, Light, Nature, Magma) can be added as expansion content

---

**Document Version:** 1.1  
**Last Updated:** 2025-11-04 (Theme Integration)  
**Status:** Core Mechanics Established + Theme Defined, Implementation Details Pending

