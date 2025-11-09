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
- **Scaling:** 20% per level (multiplicative)
- **Leveling Cost:** Linear (cheap to max)
- **Drop Rates:** 70% (Arcane packs), 50% (Elemental packs)

**Rare** - Enhanced cards
- **Stat Budget:** 30-50 stat points (Level 1)
- **Complexity:** Simple conditionals ("If X, then bonus Y")
- **Scaling:** 25% per level
- **Leveling Cost:** Level^1.2 (moderate)
- **Drop Rates:** 20% (Arcane packs), 30% (Elemental packs)

**Epic** - Build-around cards
- **Stat Budget:** 50-90 stat points (Level 1)
- **Complexity:** Multi-effects, combos, sequencing
- **Scaling:** 30% per level
- **Leveling Cost:** Level^1.4 (expensive)
- **Drop Rates:** 8% (Arcane packs), 15% (Elemental packs)

**Legendary** - Deck-defining cards
- **Stat Budget:** 90-180 stat points (Level 1)
- **Complexity:** 3-4 effects, transformative mechanics
- **Scaling:** 35% per level
- **Leveling Cost:** Level^1.6 (very expensive)
- **Drop Rates:** 2% (Arcane packs), 5% (Elemental packs)

### Leveling System

**No Level Caps:** All cards can level indefinitely with exponential cost scaling

**XP-Based System:** Duplicates grant XP toward next level
- Common duplicate: 1 XP
- Rare duplicate: 2 XP
- Epic duplicate: 5 XP
- Legendary duplicate: 10 XP

**Level Requirements:** (N-1) × rarity_cost_multiplier XP to reach level N

### Design Philosophy

**Power + Complexity Hybrid:** Higher rarity = stronger AND more mechanically interesting

**Lower rarities remain useful through:**
- Simplicity and consistency (no setup required)
- Cheaper leveling costs (easier to max out)
- Reliable baseline power
- Deck filler and foundations

**Higher rarities excel through:**
- Raw power (higher base stats)
- Better scaling rates (more growth per level)
- Mechanical complexity (conditional bonuses, combos)
- Deck-defining effects (transform strategies)

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

