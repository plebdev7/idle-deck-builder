# Tier & Class System Specification

**Last Updated:** 2025-11-08  
**Status:** Complete (Sessions 1.1, 1.2)  
**Parent Document:** [DESIGN.md](../../DESIGN.md)

---

## Tier System

### Tier Structure: Hybrid Cascading Model

**Core Principle:** Tiers unlock linearly, but once unlocked they remain active simultaneously. Lower tiers become "foundational support" rather than obsolete.

---

## Arcane Tier (Base/Foundational)

### Purpose

Universal starting point, introduces core mechanics

### Duration

Full tier (1-2 hours of content)

### Complexity

Low - simple card types (Attack, Defense, Utility), basic stats

### Currency

Arcane Essence

### Permanence

Remains active and useful throughout entire game:
- Continue building Arcane deck
- Continue earning Arcane Essence
- Continue buying Arcane packs
- Arcane Essence always useful (packs, upgrades, cross-tier uses)

### Unique Feature

Contains Class Cards (see Class System below)

---

## Elemental Tiers (Class-Specific)

### Tiers

Fire, Water, Earth, Air (and future expansions)

### Unlock Method

Equip a Class Card (obtained from Arcane packs)

### Progression

Once unlocked, runs alongside Arcane tier

### Cross-Tier Synergy

Elemental tier cards can generate resources for lower tiers:
- Fire cards can generate Arcane Essence
- Water cards can generate Arcane Essence
- Higher tier cards can generate multiple Essences

### Passive Transition

Previous tiers continue running passively after new tiers unlock:
- **Passive tiers:** Generate resources automatically, no active deck building/combat
- **Active tiers:** Full engagement (deck building, combat, upgrades)

---

## Tier Count

- **3-5 tiers** per class path (manageable, allows deep interactions)
- Total tiers across all classes: 6-10 unique colored tiers

---

## Element System

### Arcane (Gray)

Foundational magic underlying all elemental schools

### Fire (Red)

Aggressive, destructive magic

### Water (Blue)

Flowing, adaptive magic with healing and control

### Earth (Green)

Defensive, enduring magic with protection and stability

### Air (Yellow/White)

Swift, unpredictable magic with speed and tempo

---

## Class System

### Classes as Collectible Cards

**Core Mechanic:** Classes are not menu choices - they are cards found in packs.

---

## Class Card Distribution

### Common Classes (Apprentices)

**Found in:** Arcane packs
**Structure:** Simple tier paths (2 tiers: Arcane + one element)

**Examples:**
- Fire Apprentice: Arcane → Fire
- Water Apprentice: Arcane → Water
- Earth Apprentice: Arcane → Earth
- Air Apprentice: Arcane → Air

### Rare Classes

**Found in:** Arcane packs (rare drops) and elemental tier packs
**Structure:** Advanced tier paths (3 tiers: multi-element combinations)

**Examples:**
- Geomancer: Arcane → Earth → Fire
- Frostmage: Arcane → Water → Air

### Epic Classes

**Found in:** Elemental tier packs (rare drops)
**Structure:** Powerful tier paths (4 tiers: hybrid elements)

**Examples:**
- Stormlord: Arcane → Air → Water → Lightning
- Battlemage: Arcane → Fire → Earth → Magma

### Legendary Classes

**Found in:** Special/event packs
**Structure:** Complex tier paths (5 tiers: multiple element combinations)

**Examples:**
- Primalist: All elements (Arcane → Fire → Water → Earth → Air)
- Void Weaver: Forbidden magic path

---

## Class Mechanics (Session 1.2 Decision)

### Activation

Equip a Class Card to unlock its tier path

### Single Active Class

Only one class active at a time

### Deck Limit Profiles

Each class defines its own per-tier deck size limits:

- **Common classes:** Specialist distributions (e.g., 5 Arcane / 10 Fire)
- **Rare classes:** Balanced distributions (e.g., 6 Arcane / 7 Earth / 7 Fire)
- **Epic/Legendary:** Larger totals and more flexible limits
- Class choice determines deck-building strategy

### Class Switching

- Classes can ONLY be switched during prestige resets
- Makes class choice meaningful and strategic
- Natural prestige incentive (want to try new class? Prestige!)
- Commit to class for entire run

### Collection

Can collect multiple class cards from packs, but only one active per run

### Strategic Weight

Class choice affects both tier access AND deck composition constraints

---

## Deck Limit Examples

**Note:** These are example configurations to illustrate the system. Actual deck limits defined in game-data when classes are implemented.

### Fire Apprentice (Common)

```
Total Deck Size:        15 cards
Max Arcane Cards:       5 cards (foundation support)
Max Fire Cards:         10 cards (specialist focus)
Max Copies per Card:    3 copies
```

**Strategy:** Fire-focused specialist, relies heavily on elemental power, limited conversion capacity

### Geomancer (Rare, Earth → Fire)

```
Total Deck Size:        18 cards
Max Arcane Cards:       6 cards (balanced)
Max Earth Cards:        7 cards
Max Fire Cards:         7 cards
Max Copies per Card:    3 copies
```

**Strategy:** Balanced multi-tier approach, better cross-tier synergies, more flexible deck building

### Stormlord (Epic, Air → Water → Lightning)

```
Total Deck Size:        21 cards
Max Arcane Cards:       5 cards (focused foundation)
Max Air Cards:          8
Max Water Cards:        8
Max Lightning Cards:    8
Max Copies per Card:    3 copies
```

**Strategy:** Complex multi-element builds, maximum synergy potential

---

## Class Path Examples

- **Fire Apprentice (Common):** Arcane → Fire
- **Water Apprentice (Common):** Arcane → Water
- **Earth Apprentice (Common):** Arcane → Earth
- **Air Apprentice (Common):** Arcane → Air
- **Geomancer (Rare):** Arcane → Earth → Fire (stone/metal/lava theme)
- **Frostmage (Rare):** Arcane → Water → Air (ice/mist theme)
- **Stormlord (Epic):** Arcane → Air → Water → Lightning (weather control)
- **Primalist (Legendary):** Arcane → Fire → Water → Earth → Air (all elements)

---

## Class-Specific Features

### Tier Synergy Bonuses

Classes enhance synergies between their tier paths:
- Fire/Earth combos stronger for Geomancer class
- Water/Air combos stronger for Frostmage class

### Passive Tiers

Tiers outside your class path become passive (auto-generate resources)

### Cross-Tier Synergies

Enhanced within class path, present but weaker across classes

### Progression Incentive

Higher rarity classes unlock MORE content (more tiers) not just different content

---

## Deck Building Constraints (Session 1.2 Decision)

### Multi-Layered Constraint System

**1. Total Deck Size (Fixed):**
- Fixed number of cards in deck
- Varies by class rarity (example: Common: 15, Rare: 18, Epic: 21, Legendary: 24+)
- May increase with progression/prestige upgrades
- Purchased with Arcane Essence or prestige currency

**2. Per-Tier Limits (Class-Specific):**
- **Each class defines its own per-tier limit distribution**
- Maximum cards from each tier determined by active class
- Common classes: Specialist focus (5 foundation / 10 primary)
- Rare classes: Balanced multi-tier (6/7/7 distribution)
- Epic/Legendary: More total slots and flexible distributions
- Ensures cross-tier deck building
- Prevents stacking only highest tier
- Creates mechanical differentiation between classes

**3. Card Copy Limits:**
- Maximum copies of same card (e.g., 2-3 copies)
- Prevents dominant single-card strategies
- May vary by card rarity
- Encourages diverse deck composition

### Constraint Scaling with Progression

- **Early game:** Common classes, tight specialist limits (5/10)
- **Mid game:** Rare classes, balanced multi-tier limits (6/7/7)
- **Late game:** Epic/Legendary classes, flexible high limits (5/8/8/8)
- **Prestige:** Access to better classes + possible limit upgrades

---

## Deck Building Strategy

### Resource Optimization

Include generator cards vs combat cards

### Synergy Building

Cards that trigger mechanical interactions (not just multipliers)

### Cross-Tier Composition

Balance cards from different tiers

### Meta Progression

Deck improves through card levels, upgrades, prestige bonuses

---

## Future Progression Mechanics (Not Yet Designed)

- Class leveling system to increase tier limits
- Tier-specific upgrades (spend resources to expand limits)
- Prestige bonuses for permanent limit increases
- Milestone unlocks for special limit expansions

---

## Document History

**Version 1.0** (2025-11-08) - Split from DESIGN.md Version 1.9  
- Extracted Tier System and Class System sections
- Includes Session 1.2 decisions (class switching, deck limits)
- Status: Complete, progression mechanics pending Session 7

