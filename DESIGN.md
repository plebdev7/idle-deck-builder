# Idle Deck Builder - Game Design Document

**Version:** 2.0 (Modular Structure)  
**Last Updated:** 2025-11-08  
**Status:** Complete core systems, pack cards pending (Session 2.1)

---

## Document Purpose

This document serves as the **high-level design hub** for the Idle Deck Builder game. Detailed specifications are maintained in focused topic files under `docs/design-specs/`.

**For detailed specifications, see:**
- [Combat System](docs/design-specs/combat-system.md) - Tick-based combat, HP, death mechanics
- [Progression & Scaling](docs/design-specs/progression.md) - Enemy scaling, bosses, death loops
- [Resource Economy](docs/design-specs/resource-economy.md) - Generators, essence, shards
- [Card System](docs/design-specs/card-system.md) - Card types, starter deck, pack cards
- [Tier & Class System](docs/design-specs/tier-class-system.md) - Tiers, classes, deck limits
- [Baseline Numbers](docs/design-specs/baseline-numbers.md) - All formulas, rates, timings
- [First 30 Minutes](docs/design-specs/first-30-minutes.md) - New player experience

---

## Core Vision

An idle deck building game where **strategic deck construction drives passive gameplay**. Players build decks that auto-battle, generate resources, and progress through multiple tiers. The primary engagement is deck building strategy, not active combat management.

**Key Principles:**
- Deck building is the core strategy layer
- Combat is fully automated
- Passive play with strategic engagement
- Tiers remain active (foundation never obsolete)
- Classes are collectible content (found in packs)
- Resource generation is a deck-building decision

---

## Theme & Setting

### Elemental Magic Tower Defense

You are an apprentice mage defending a magical tower from endless waves of invaders. Your deck represents your arsenal of spells and magical abilities. As you master different schools of elemental magic (Fire, Water, Earth, Air, and foundational Arcane magic), you unlock more powerful spells.

**Design Philosophy:** The theme provides context but never obscures gameplay. Familiar fantasy elements reduce cognitive overhead, letting strategic depth dominate.

**Elements:**
- **Arcane (Gray):** Foundational magic underlying all schools
- **Fire (Red):** Aggressive, destructive magic
- **Water (Blue):** Flowing, adaptive magic
- **Earth (Green):** Defensive, enduring magic
- **Air (Yellow/White):** Swift, unpredictable magic

**Currency:** All resources are called "Essence" - magical energy extracted from your spells:
- Arcane Essence (base tier)
- Fire/Water/Earth/Air Essence (elemental tiers)

---

## Core Mechanics Summary

### Primary Progression Loop

Multiple interconnected loops:
- Resource accumulation → Buy packs → Improve deck → Faster resource gain
- Combat victories → Unlock content → New cards/mechanics → More options
- Card collecting/upgrading → Better decks → Tackle harder content → Collect more

### Combat System

**Trimps-Style Combat-Over-Time:**
- Tick-based combat (1.0 second per tick)
- Player HP system (100 HP start, upgradeable with shards)
- Cards drawn continuously (1 card/sec) add to attack and defense
- Stats reset after each enemy (but essence rate persists)
- Death resets enemy progress but keeps all resources

**Death Loop is Core Gameplay:**
- Fight → Die → Spend resources → Improve deck → Fight again
- NOT prestige (which is a separate late-game mechanic)
- Expected 4-6 loops to beat first major boss (Enemy 150)

→ **[Full Combat Specification](docs/design-specs/combat-system.md)**

### Resource Generation

**Two Distinct Resources:**

**1. Essence (Pack Currency):**
- Generated when generator cards are drawn during combat
- Rate accumulates and persists between enemies (resets on death)
- Used for purchasing packs, upgrades, conversions
- All Essence starts as Arcane Essence
- Elemental Essences created through conversion cards

**2. Shards (Upgrade Currency):**
- Dropped by combat victories
- Used for card upgrades, deck size increases, HP upgrades, permanent buffs
- Separate from essence generation

**Critical Mechanic:** Generators work **when drawn**, not passively in deck. Deck cycling speed matters!

→ **[Full Resource Economy Specification](docs/design-specs/resource-economy.md)**

### Tier System

**Hybrid Cascading Model:**
- **Arcane Tier:** Universal starting point, remains active forever
- **Elemental Tiers:** Unlock via class cards, run alongside Arcane tier
- Lower tiers become "foundational support" rather than obsolete
- Cross-tier synergies create strategic depth

**Tier Count:**
- 3-5 tiers per class path
- 6-10 total unique tiers across all classes

→ **[Full Tier & Class Specification](docs/design-specs/tier-class-system.md)**

### Class System

**Classes as Collectible Cards:**
- Classes are NOT menu choices - they're cards found in packs
- Only one class active at a time
- Classes can ONLY be switched during prestige resets (or death)
- Each class defines its own deck size limits and tier path

**Class Rarities:**
- **Common (Apprentices):** 2 tiers (Arcane + one element), 15 cards
- **Rare:** 3 tiers (multi-element), 18 cards, balanced limits
- **Epic:** 4 tiers (hybrid elements), 21 cards, flexible limits
- **Legendary:** 5 tiers (complex paths), 24+ cards

→ **[Full Tier & Class Specification](docs/design-specs/tier-class-system.md)**

### Deck Building

**Multi-Layered Constraints:**
1. **Total Deck Size:** Fixed per class (15-24+ cards by rarity)
2. **Per-Tier Limits:** Each class defines its own tier distribution
3. **Card Copy Limits:** Max 2-3 copies of same card

**Strategic Balance:**
- Generator cards for resources (25-35% of deck)
- Combat cards for attack/defense (60-65% of deck)
- Utility cards for special effects (5-10% of deck)

**Minimum Deck Size:** 8 cards (prevents exploit)

→ **[Full Tier & Class Specification](docs/design-specs/tier-class-system.md)**

---

## Progression & Scaling

### Enemy Scaling (Act-Based Step Function)

**Act 1 (Enemies 1-50):** Tutorial Tier
- Formula: `HP = 20 + (n-1) × 120`
- Enemy 50 (Mini-Boss #1): 9,768 HP, 10 ATK (first attacker!)

**Act 2 (Enemies 51-100):** Challenge Tier
- Formula: `HP = 6,000 + (n-51) × 130`
- Enemy 100 (Mini-Boss #2): 18,555 HP, 30 ATK (first real wall)

**Act 3 (Enemies 101-150):** Master Tier
- Formula: `HP = 12,500 + (n-101) × 140`
- Enemy 150 (Major Boss): 38,680 HP, 80 ATK (requires 4-6 loops)

**Design Rationale:**
- Step functions create clear progression acts
- Post-boss enemies easier than boss (breathing room)
- Continuous forward momentum
- Boss victories unlock new difficulty tiers

→ **[Full Progression Specification](docs/design-specs/progression.md)**

### Boss Encounters

**Enemy 50 - "Defense Tutorial" (Lieutenant):**
- First enemy with attack (10 ATK)
- Teaches defense matters
- ~23 minutes with starter deck

**Enemy 100 - "First Real Wall" (Commander):**
- 30 ATK, requires Pack 1
- Soft gate encouraging death loop
- Bad players fail here

**Enemy 150 - "Major Milestone" (Tower Guardian):**
- 80 ATK, requires multiple loops
- End of "Act 1" content
- Expected 2-3 hours, 4-6 loops to defeat

→ **[Full Progression Specification](docs/design-specs/progression.md)**

---

## Card System

### Card Types

- **Combat Cards:** Attack and/or Defense stats
- **Generator Cards:** Resource generation (rate, burst, hybrid, multiplier, conditional)
- **Synergy Cards:** Trigger combos and mechanical interactions
- **Utility Cards:** Special effects and deck manipulation

### Starter Deck (8 Cards)

**Generators (3):**
- Arcane Conduit (+2 Essence/sec)
- Essence Burst (+150 flat)
- Combat Siphon (+1 Essence/sec + 12/6 stats)

**Combat (5):**
- Arcane Bolt (20 ATK pure offense)
- Mystic Shield (18 DEF pure defense)
- Balanced Strike (10/10)
- Power Strike (15/5)
- Stalwart Guard (5/15)

**Total When Drawn:** 62 ATK, 54 DEF, +3 Essence/sec

→ **[Full Card System Specification](docs/design-specs/card-system.md)**

### Pack Card Progression (To Be Designed in Session 2.1)

- **Pack 1:** Simple synergies, better generators
- **Pack 2:** Sequencing effects, multiplier generators, first Rare
- **Pack 3+:** Full complexity, deck manipulation, Rare/Epic cards

---

## Pack & Collection System

### Pack Types

**Arcane Packs:**
- Cost: Arcane Essence
- Contains: Arcane cards, Common class cards, Rare classes (low chance)
- Always available and valuable

**Elemental Packs:**
- Cost: Respective elemental Essence
- Contains: Element cards, Epic classes (rare), Legendary (very rare)
- Unlock after tier unlocked via class

**Special Packs:**
- Premium packs, event packs, milestone rewards

### Pack Costs

**Formula:** `40,000 × 2.5^(n-1)`

- Pack 1: 40,000 Essence (~7 min)
- Pack 2: 100,000 Essence (~12 min)
- Pack 3: 250,000 Essence (~19 min)
- Pack 4: 625,000 Essence (~33 min)

### Duplicate Handling

**To Be Designed in Session 7:**
- Card leveling (XP system)?
- Scrap/crafting system?
- Prestige currency conversion?

---

## Prestige System

**Status:** To Be Designed in Session 7

**Known Distinctions:**
- **Death Loop ≠ Prestige:** Death loop is normal gameplay
- **Prestige:** Separate late-game mechanic with real resets and permanent bonuses

**Possible Prestige Types:**
- Card-level prestige
- Deck-level prestige
- Tier-level prestige
- Full game prestige

**Unlock Condition:** After beating first major boss (Enemy 150)?

---

## First 30 Minutes Experience

**Starting State:**
- "Arcane Student" class (no choice yet)
- Pre-built 8-card starter deck
- Class cards pre-owned but locked until prestige

**Key Milestones:**
- **Minute 3:** First enemy defeated
- **Minute 7:** Pack 1 affordable
- **Minute 13:** Deck building unlocked
- **Minute 16:** Passive income established
- **Minute 23:** Enemy 50 reached (Mini-Boss #1 - First Attacker)
- **Minute 30:** Enemy 60 reached, 3 packs purchased, optimized deck

**End State:**
- 25-28 cards owned
- 20-card optimized deck
- ~5-7 Essence/sec generation
- Aware of prestige and class systems

→ **[Full First 30 Minutes Specification](docs/design-specs/first-30-minutes.md)**

---

## Baseline Numbers Quick Reference

### Core Timing

- Card draw: **1.0 second per card**
- Enemy spawn: **Every 12 seconds**
- Combat tick: **1.0 second per tick**

### Generator Rates

- Starter: +1, +2 Essence/sec
- Pack 1: +3, +4 Essence/sec
- Pack 2: +5 Essence/sec
- Pack 3+: +2 to +10+ Essence/sec (by rarity)

### Combat Card Stats

- Starter: 8-15 total stats
- Pack 1: 25-30 total stats
- Pack 2: 35-45 total stats
- Pack 3+ Rare: 50-80 total stats
- Pack 3+ Epic: 100-150 total stats

### Shard Drops & Spending

- Drops: 2-3 (early) → 8-12 (late) per victory
- By Enemy 50: ~600-700 shards earned
- HP Tier 1 upgrades: 50/75/100/125/150 shards for +10 HP each

### Combat Duration (Starter Deck)

- Enemy 1: ~2 seconds
- Enemy 10: ~17 seconds
- Enemy 50: ~47 seconds
- Enemy 100: ~90 seconds (requires Pack 1)
- Enemy 150: ~180+ seconds (requires Packs 1-3)

→ **[Full Baseline Numbers Reference](docs/design-specs/baseline-numbers.md)**

---

## Outstanding Design Questions

### High Priority (Session 2.1)

**Question 7: Card Rarity System**
- How many rarities? (Common / Rare / Epic / Legendary?)
- How do rarities affect stats and abilities?
- Stat differences per rarity tier?

### Medium Priority (Session 7)

**Question 2: Secondary Class Slot**
- Can prestige unlock passive bonuses from inactive class?

**Question 6: Prestige Reset Details**
- What exactly resets (cards, levels, progress, or combinations)?
- What persists?
- Different prestige types?

---

## Resolved Design Decisions

### Class Switching (Session 1.2)

**Decision:** Classes can only be switched during prestige resets (or death).

**Rationale:** Makes class choice meaningful for each run, provides prestige incentive.

### Arcane Combat Role (Session 1.2)

**Decision:** Arcane cards contribute to elemental tier decks (unified combat system).

**Rationale:** Keeps Arcane relevant forever, enables deep cross-tier synergies, simpler system.

### Arcane Essence Economy (Session 1.2)

**Decision:** Arcane Essence is universal currency. Elemental Essences generated through conversion.

**Rationale:** Arcane remains foundational, creates strategic conversion decisions, unified economy.

### Deck Size Constraints (Session 1.2)

**Decision:** Fixed deck size with per-tier limits defined by active class.

**Rationale:** Class-specific limits create mechanical differentiation, forces cross-tier building.

### Combat Timing (Session 1.2, Updated 2.0.3)

**Decision:** Tick-based combat-over-time with HP system and death mechanics.

**Rationale:** Creates actual "combat" with tension, enables HP/healing/defense strategy, death spiral gameplay.

### Generator Mechanics (Session 1.3)

**Decision:** Generators work **when drawn**, not passively in deck.

**Rationale:** Deck cycling speed matters, death penalty meaningful, session length relevant.

---

## Development Status

### Complete Sessions

- ✅ **Session 1.1:** Theme Selection (Elemental Magic Tower Defense)
- ✅ **Session 1.1A:** Visual Direction & Style Guide
- ✅ **Session 1.2:** Critical Design Decisions (5 major questions resolved)
- ✅ **Session 1.3A:** First 30 Minutes Experience Design
- ✅ **Session 1.3B:** Baseline Numbers (corrected for stacking)
- ✅ **Session 1.3C:** Starter Deck Design (8 cards)
- ✅ **Task 2.0:** Gameplay Simulator (validates baseline)
- ✅ **Session 2.0.1:** Combat Progression Design (bosses, death loops)
- ✅ **Task 2.0.2:** Live Terminal Simulation View
- ✅ **Session 2.0.3:** Combat System Redesign (combat-over-time, Parts A-D complete)
- ✅ **Task 2.0.4:** Implement New Combat System
- ✅ **Task 2.0.4a/b:** CLI Bug Fixes
- ✅ **Task 2.0.5:** Update Validation System

### In Progress

- 🔄 **Task 2.0.6:** Design Document Review & Baseline Adjustment (pending after restructure)

### Next Up

- **Task 2.1:** Pack Card Design (15-20 cards for Packs 1-3)
- **Session 2.2-2.4:** Card interaction specifications, patterns

---

## Document History

**Version 2.0.1** (2025-11-08) - Task 2.0.6: Arithmetic Corrections
- Fixed Enemy 50 HP: 9,768 → 7,670 (correct per 120 HP/enemy formula)
- Fixed Enemy 150 HP: 38,680 → 38,720 (correct per formula)
- Validated all formulas for arithmetic consistency
- All pack costs, attack scaling, and other values verified correct
- Rationale: Design docs had arithmetic errors; implementation was correct all along

**Version 2.0** (2025-11-08) - Documentation Restructure
- Split monolithic DESIGN.md into modular topic files
- Created lean hub document with summaries and links
- Detailed specs moved to `docs/design-specs/`
- Old Version 1.9 archived to `.archive/DESIGN-v1.9-pre-split.md`

**Version 1.9** (2025-11-07) - Session 2.0.3: Combat System Redesign Complete
- Combat changed to Trimps-style combat-over-time
- HP system, death mechanics, stat resets
- Act-based enemy scaling formula
- Boss HP values finalized

**Version 1.8** (2025-11-07) - Task 2.0.1: Combat Progression Design
- Enemy health scaling, boss encounters, death loop mechanics

**Version 1.7** (2025-11-07) - Task 2.0 Corrections
- Simulator results integrated, baseline validated

**Previous Versions:** See archived document for full history

---

**Document Version:** 2.0.1  
**Last Updated:** 2025-11-08  
**Status:** Core systems complete, arithmetic validated, pack cards pending Task 2.1  
**Archive:** [DESIGN-v1.9-pre-split.md](.archive/DESIGN-v1.9-pre-split.md)

