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

### Combat Cards (5 cards)

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

## Card Rarity System (To Be Designed in Session 2.1)

**Question 7 from DESIGN.md Outstanding Questions:**
- How many rarities?
- How do rarities affect stats/abilities?
- Stat differences per rarity?

**To Be Determined:**
- Common / Rare / Epic / Legendary system?
- Rarity affects stat totals or ability complexity?
- Drop rates from packs?

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

## Document History

**Version 1.0** (2025-11-08) - Split from DESIGN.md Version 1.9  
- Extracted Card Mechanics, Card Types, and Starter Deck sections
- Starter deck complete (Session 1.3C)
- Pack card design pending (Session 2.1)
- Status: Partial - awaits Task 2.1 for pack card specifications

