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

### Generator Cards (3 cards)

**1. Arcane Conduit** - Rate Generator
- **Generation:** +2 Essence/sec when drawn
- **Attack:** —
- **Defense:** —
- **Flavor:** *"A stable channel of pure arcane energy. Draw upon it to fuel your magic."*
- **Identity:** Pure rate-building. Increases ongoing income permanently (until death).

**2. Essence Burst** - Burst Generator
- **Generation:** +250 Essence when drawn (flat amount)
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

### Combat Cards (5 cards)

**4. Arcane Bolt** - Pure Offense
- **Attack:** 20
- **Defense:** —
- **Flavor:** *"A focused blast of raw magical force."*
- **Identity:** Glass cannon. Maximum offensive power, no defensive capability.

**5. Mystic Shield** - Pure Defense
- **Attack:** —
- **Defense:** 20
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
- Defense: 56 total (20+10+5+15+6)
- Rate Generation: +3 Essence/sec (2+1 from generators)
- Burst Generation: +250 Essence

### Design Philosophy

**All Flat Values:** No conditional effects, utilities, or complex mechanics. Complexity introduced progressively through packs.

**Different, Not Better:** Each card has unique identity and purpose. No strictly superior options:
- Rate vs Burst vs Hybrid generators (different strategies)
- Pure specialist vs generalist vs leaning combat cards (different balance points)

**What Players Learn:**
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

```
1 stat point = 1 ATK
1 stat point = 1 DEF
1 stat point = 10 flat Essence
1 stat point = 0.1 Essence/sec
1 stat point = 0.5 HP heal (instant)
1 stat point = 0.1 HP/sec regen (until next enemy)
```

### Rarity Stat Budgets (Level 1)

```
Common:     20-30 stat points
Rare:       30-50 stat points
Epic:       50-90 stat points
Legendary:  90-180 stat points
```

### Starter Deck Audit (All Common Rarity)

**Arcane Conduit:** +2 Essence/sec = 20 stat points ✓
**Essence Burst:** +250 flat Essence = 25 stat points ✓
**Combat Siphon:** +1 Essence/sec + 12 ATK + 6 DEF = 28 stat points ✓
**Arcane Bolt:** 20 ATK = 20 stat points ✓
**Mystic Shield:** 20 DEF = 20 stat points ✓
**Balanced Strike:** 10 ATK + 10 DEF = 20 stat points ✓
**Power Strike:** 15 ATK + 5 DEF = 20 stat points ✓
**Stalwart Guard:** 5 ATK + 15 DEF = 20 stat points ✓

**Starter deck range:** 20-28 stat points (well-balanced within Common rarity)

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

