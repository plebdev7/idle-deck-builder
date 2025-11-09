# Card System Specification

**Last Updated:** 2025-11-08  
**Status:** Starter deck complete (Session 1.3C), Pack cards pending (Session 2.1)  
**Parent Document:** [DESIGN.md](../../DESIGN.md)

---

## Overview

All abilities in this game are card-based. There is no separate "skills" menu or system. Everything players control is through deck composition.

---

## Card Types

### Combat Cards

Primary damage/defense cards

- Pure offense (high attack, no defense)
- Pure defense (high defense, no attack)
- Balanced (equal attack and defense)
- Hybrid distributions (various balances)

### Generator Cards

Resource generation cards

- See [resource-economy.md](resource-economy.md) for detailed generator mechanics
- Rate generators (+X Essence/sec)
- Burst generators (+X flat Essence)
- Hybrid generators (rate + combat stats)
- Multiplier generators (rate × time)
- Conditional generators (if condition, +X Essence/sec)

### Synergy Cards

Cards that trigger mechanical interactions (not just multipliers)

- Trigger chains: Card A effect triggers Card B combo, which triggers Card C effect
- Conditional abilities: "If you have 3+ Blue cards in play, trigger X"
- Combo requirements: Multiple cards must be present for powerful effects

### Utility Cards

Special effects and abilities

- Deck manipulation ("Draw extra card", "Shuffle deck")
- State-based effects ("Lasts until reshuffle")
- Temporary buffs/debuffs

---

## Card Interactions (Mechanical, Not Just Multipliers)

### Trigger Chains

Blue card effect triggers Green combo, which triggers Yellow effect

### Conditional Abilities

"If you have 3+ Blue cards in play, trigger X"

### Combo Requirements

Multiple cards must be present for powerful effects

### Class Enhancements

Classes make certain combos more effective

---

## Starter Deck Specification (Session 1.3C)

All players begin as "Arcane Student" with this pre-built 8-card deck. All cards are Arcane tier, Common rarity, with flat values and no complex abilities.

**Authoritative Source:** See [`game-data/cards-starter-deck.json`](../../game-data/cards-starter-deck.json) for exact card stats, effects, and implementations.

### Design Philosophy

**All Flat Values:** No conditional effects, utilities, or complex mechanics. Complexity introduced progressively through packs.

**Different, Not Better:** Each card has unique identity and purpose. No strictly superior options:
- Rate vs Burst vs Hybrid generators (different strategies)
- Pure specialist vs generalist vs leaning combat cards (different balance points)

### Starter Deck Composition

**Total:** 8 cards
- **Generators:** 3 cards (37.5%) - mix of rate, burst, and hybrid
- **Combat:** 5 cards (62.5%) - mix of specialists and generalists

**Total Stats When All Cards Drawn:**
- Attack: 62 total
- Defense: 56 total
- Rate Generation: +3 Essence/sec
- Burst Generation: +250 Essence

**Note:** Stats accumulate with each deck cycle (9 seconds for 8-card deck). See [combat-system.md](combat-system.md) for deck cycling mechanics.

### Card Roles

**Generator Cards (3):**
1. **Arcane Conduit** - Rate Generator (pure rate-building, +2 Essence/sec)
2. **Essence Burst** - Burst Generator (immediate payoff, +250 flat Essence)
3. **Combat Siphon** - Hybrid Generator (both roles, +1 Essence/sec + combat stats)

**Combat Cards (5):**
4. **Arcane Bolt** - Pure Offense (glass cannon, maximum ATK)
5. **Mystic Shield** - Pure Defense (pure survival, maximum DEF)
6. **Balanced Strike** - Generalist (versatile middle ground, equal ATK/DEF)
7. **Power Strike** - Offense-Leaning (damage-focused but not reckless)
8. **Stalwart Guard** - Defense-Leaning (survival-focused but not passive)

### What Players Learn

- Generator diversity (rate building, immediate payoff, hybrid approach)
- Combat variety (specialization, balance, various distributions)
- Deck building foundation (different cards for different strategies)

---

## Pack Card Progression (To Be Designed in Session 2.1)

### Pack 1: Simple Synergies

Introduces conditional bonuses and simple synergies
- Conditional bonuses ("If drawn in first 5 seconds...")
- Simple synergies ("If you have 3+ Arcane cards...")
- Better generators (+3, +4 Essence/sec)

### Pack 2: Sequencing Effects

Introduces sequencing effects and multiplier generators
- Multiplier generator (Current rate × Y seconds)
- Order-dependent effects ("Next card gets +50%")
- First Rare card with combo mechanics

### Pack 3+: Full Complexity

Full complexity (deck manipulation, state-based effects, advanced synergies)
- Deck manipulation ("Draw extra card", "Shuffle deck")
- State-based effects ("Lasts until reshuffle")
- Higher power level cards (Rare/Epic)

---

## Card Rarity System (Session 2.1.1 - COMPLETE)

### Rarity Tiers

**Common** - Foundation cards
- **Stat Budget:** 20-30 stat points (Level 1)
- **Complexity:** Flat values, no conditions
- **Drop Rates:** 70% (Arcane packs), 50% (Elemental packs)
- **Leveling:** Same as all rarities (45 duplicates to Level 10)
- **Awakening:** Easier to achieve (high drop rates)

**Rare** - Enhanced cards
- **Stat Budget:** 30-50 stat points (Level 1)
- **Complexity:** Simple conditionals ("If X, then bonus Y")
- **Drop Rates:** 20% (Arcane packs), 30% (Elemental packs)
- **Leveling:** Same as all rarities (45 duplicates to Level 10)
- **Awakening:** Moderate difficulty

**Epic** - Build-around cards
- **Stat Budget:** 50-90 stat points (Level 1)
- **Complexity:** Multi-effects, combos, sequencing
- **Drop Rates:** 8% (Arcane packs), 15% (Elemental packs)
- **Leveling:** Same as all rarities (45 duplicates to Level 10)
- **Awakening:** Long-term goal (low drop rates)

**Legendary** - Deck-defining cards
- **Stat Budget:** 90-180 stat points (Level 1)
- **Complexity:** 3-4 effects, transformative mechanics
- **Drop Rates:** 2% (Arcane packs), 5% (Elemental packs)
- **Leveling:** Same as all rarities (45 duplicates to Level 10)
- **Awakening:** Prestige-spanning goal (very low drop rates)

### Leveling System (Session 2.1.3 - COMPLETE)

**Universal Mechanics:** All cards use identical leveling formulas regardless of rarity

**Duplicate-Based System:** Direct duplicate counting, no XP middleman
- **Duplicates needed for Level N:** `N - 1`
  - Level 1 → 2: 1 duplicate
  - Level 2 → 3: 2 duplicates
  - Level 3 → 4: 3 duplicates
  - Level 10: Total of 45 duplicates (1+2+3+...+9)

**Stat Scaling:** 20% multiplicative growth per level (all rarities)
- Formula: Base stats × (1.20)^(level-1)
- Level 1: 100% base stats
- Level 5: 207% base stats (2.07× multiplier)
- Level 10: 516% base stats (5.16× multiplier)

**Level Cap:** Level 10 (base leveling system)
- Opens awakening system at Level 10
- All cards follow same progression
- Natural difficulty from drop rate frequency

### Awakening System (Session 2.1.3 - COMPLETE)

**Individual Card Prestige:** Post-Level-10 progression layer for maxed cards

#### Scrap Generation
- **Maxed card duplicates (Level 10)** convert to scraps
- 1 duplicate = 1 scrap (rarity-specific)
- Common duplicate → Common Scrap
- Rare duplicate → Rare Scrap
- Epic duplicate → Epic Scrap
- Legendary duplicate → Legendary Scrap
- **No cross-conversion** between scrap rarities

#### Awakening Progression
**Level 11-20:** Extended progression with increasing scrap costs
- **Levels 11-14:** Stat increases (10/20/30/40 scraps)
- **Level 15:** Secondary effect unlocked (50 scraps) + stat increase
- **Levels 16-19:** Stat increases (60/70/80/90 scraps)
- **Level 20:** Transformative effect unlocked (100 scraps) + stat increase

**Total Cost:** 550 scraps to reach Level 20
**Stat Multiplier at Level 20:** 13.74× base stats

#### Awakening Effect Types

**Secondary Effects (Level 15):** Card-specific utility or synergy
- Examples: "+5% ATK to next card", "+1 HP regen per tick", "Draw +1 card on reshuffle"
- Adds build-around potential without overwhelming power
- Designed per-card during content creation

**Transformative Effects (Level 20):** Deck-defining mechanical changes
- Examples: "Triggers twice per draw", "Affects all cards in hand", "Permanent effect until death"
- Major strategic decisions
- Ultra-late-game goals (prestige-spanning)
- Designed per-card during content creation

### Design Philosophy

**Power + Complexity Hybrid:** Higher rarity = stronger AND more mechanically interesting

**Lower rarities remain useful through:**
- Simplicity and consistency (no setup required)
- **Higher drop rates** (easier to max out and awaken)
- Reliable baseline power
- Deck filler and foundations
- First cards to reach awakening levels

**Higher rarities excel through:**
- Raw power (higher base stats)
- Mechanical complexity (conditional bonuses, combos)
- Deck-defining effects (transform strategies)
- **Harder to max** (scarcity creates prestige goals)

**Leveling creates long-term goals:**
- First 30 min: No duplicates (Packs 1-3 deterministic)
- Enemy 50-100: Early leveling begins (Pack 4+)
- Enemy 100-150: Commons reach Level 5-7
- Multiple loops: First Level 10 cards, scraps accumulate
- Post-prestige: Awakening progression begins

---

## Card Data Structure (To Be Designed in Session 2.1)

**To Be Specified:**
- All card fields (name, type, stats, abilities, flavor text, rarity, tier, cost)
- Stat ranges per rarity and tier
- Ability description format
- Card leveling progression curves

---

## Card Text Format (To Be Designed in Session 2.1)

**To Be Specified:**
- Ability description templates
- Keywords and formatting rules
- Flavor text length limits
- Visual layout validation against visual-style-guide.md

---

## Stat Point System (Session 2.1.2 - ADDED)

### Conversion Rates

**Purpose:** Unified balancing system for all card effects. All values are configurable.

**Authoritative Source:** See [`game-data/balance-config.json`](../../game-data/balance-config.json) for exact conversion rates and rarity budgets.

**System Overview:**
- Each card effect type has a stat point cost
- Cards are balanced by total stat point budget
- Rarity determines stat point budget ranges
- Provides consistent power scaling across all cards

### Rarity Stat Budgets (Level 1)

- **Common:** 20-30 stat points
- **Rare:** 30-50 stat points
- **Epic:** 50-90 stat points
- **Legendary:** 90-180 stat points

### Starter Deck Validation

All starter deck cards fall within the Common rarity range (20-30 stat points). See [`game-data/cards-starter-deck.json`](../../game-data/cards-starter-deck.json) for exact stat point budgets per card.

---

## Document History

**Version 1.2** (2025-11-09) - Task 2.1.3 Complete
- **Added complete leveling and awakening system**
- Universal leveling formula: N-1 duplicates for Level N (all rarities)
- Level 10 cap for base leveling (45 total duplicates)
- 20% multiplicative stat scaling per level (all rarities)
- Awakening system: Levels 11-20 using scrap currency
- Scrap generation from maxed card duplicates (rarity-specific)
- Secondary effects at Level 15, transformative effects at Level 20
- Total 550 scraps needed for Level 20 awakening
- Removed rarity-specific leveling multipliers (simplified)
- Updated design philosophy with awakening progression timeline

**Version 1.1** (2025-11-08) - Task 2.1.2 Updates
- Added Card Rarity System (Session 2.1.1)
- Added Stat Point System (Session 2.1.2)
- Updated Essence Burst: 150 → 250 flat Essence
- Updated Mystic Shield: 18 → 20 DEF
- Starter deck rebalanced to stat point system

**Version 1.0** (2025-11-08) - Split from DESIGN.md Version 1.9  
- Extracted Card Mechanics, Card Types, and Starter Deck sections
- Starter deck complete (Session 1.3C)
- Pack card design pending (Session 2.1)
- Status: Partial - awaits Task 2.1 for pack card specifications

