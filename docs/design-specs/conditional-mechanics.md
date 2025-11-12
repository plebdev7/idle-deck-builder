# Conditional Mechanics Specification

**Last Updated:** 2025-11-10  
**Status:** Complete - Task 2.1.4  
**Parent Document:** [card-system.md](card-system.md)

---

## Overview

Conditional mechanics are the primary design lever for creating strategic depth beyond flat card stats. This document defines all condition types, balancing frameworks, ability templates, and progression through Packs 1-3.

**Core Principle:** Conditions create interesting deck-building decisions and reward strategic composition, without creating untrackable complexity or "feels bad" randomness.

---

## Condition Type Categories

### **TIMING CONDITIONS**

Trigger based on combat phase and deck cycling position.

#### Cycle Position
- `"If drawn in first N cards this cycle"` - Position-based trigger before reshuffle
- `"If drawn after 5+ cards this cycle"` - Late-cycle trigger
- `"If this is the last card before reshuffle"` - Reshuffle setup

#### Reshuffle Count
- `"On first cycle"` (reshuffle_count = 0) - Opening plays
- `"On second cycle"` (reshuffle_count = 1) - Early combat
- `"After 3rd reshuffle"` (reshuffle_count >= 3) - Extended combat
- `"On even/odd reshuffles"` - Alternating pattern

#### Combat Phase (HP-Based)
- `"If enemy HP > 75%"` - Early combat, enemy healthy
- `"If enemy HP < 25%"` - Finishing moves, enemy weakened
- `"If player HP > 75%"` - Confident/healthy state
- `"If player HP < 50%"` - Wounded state
- `"If player HP < 25%"` - Desperate/last stand

**Design Notes:**
- Reshuffle-based timing preferred over seconds/ticks (better game feel)
- HP-based phases are clear and visible on screen
- Position-based conditions scale naturally with deck size

---

### **CARD_COUNT CONDITIONS**

Trigger based on deck composition and cards drawn during combat.

**CRITICAL:** Cards do not stay "in play" - they are drawn, trigger effects, then immediately go to discard. Tracking must be explicit about time window.

#### Cards Drawn This Combat
- `"If 3+ Arcane cards drawn this combat"` - Cumulative since combat start
- `"If 5+ Combat-type cards drawn this combat"` - Type-based counting
- `"If 2+ Generator cards drawn this combat"` - Function-based counting
- `"If 0 Generator cards drawn this combat yet"` - Absence condition

#### Cards Drawn This Cycle
- `"If 3+ same-tier cards drawn this cycle"` - Mono-tier reward
- `"If all cards drawn this cycle are Combat type"` - Purity bonus
- `"If this is the 3rd Generator this cycle"` - Threshold trigger
- `"If 2+ different tiers drawn this cycle"` - Diversity reward

#### Deck Composition
- `"If deck has 3+ Fire cards"` - Deck construction requirement
- `"If deck size > 12"` - Size-based condition
- `"If deck has exactly 8 cards"` - Minimum deck optimization
- `"If deck has 5+ same-tier cards"` - Archetype commitment

**Design Notes:**
- Clear distinction between "this combat", "this cycle", and "in deck"
- Visible counters required for combat/cycle tracking
- Deck composition checkable at any time

---

### **STATE CONDITIONS**

Trigger based on current game values and relationships.

#### Resource State
- `"If essence rate > 5/sec"` - Resource generation threshold
- `"If essence rate = 0"` - Pure combat deck condition
- `"If gained 500+ essence this combat"` - Burst accumulation

#### Stat State
- `"If your ATK > your DEF"` - Offensive build indicator
- `"If your DEF > your ATK"` - Defensive build indicator
- `"If your ATK > enemy current DEF"` - Breakthrough condition
- `"If your total stats > 200"` - Power level threshold

#### HP Relationships
- `"If player HP = enemy HP"` - Mirrored fight
- `"If player HP > enemy HP"` - Winning position
- `"If player HP < enemy HP"` - Underdog position
- `"If at max HP"` - Perfect health

**Design Notes:**
- All states are visible on combat screen
- Stat comparisons encourage build diversity
- HP relationships create dynamic gameplay moments

---

### **SEQUENCE CONDITIONS**

Trigger based on recent card draw history and order.

**CRITICAL:** Requires visual tracking of last N cards drawn (see Combat UI specification).

#### Previous Card
- `"If previous card was Generator type"` - Simple 1-card memory
- `"If previous card was same tier as this"` - Tier chaining
- `"If previous card gave > 15 ATK"` - Power threshold
- `"If previous card gave essence"` - Function-based chain

#### Last N Cards
- `"If last 2 cards were both Combat type"` - Type sequence
- `"If last 3 cards were all different tiers"` - Diversity sequence
- `"If last 2 cards both gave ATK"` - Stat-based pattern

#### Counting Chains
- `"For each Fire card drawn this cycle, +X"` - Scaling per count
- `"For each Generator drawn this combat, +Y"` - Cumulative scaling

#### Reshuffle Triggers
- `"First card after reshuffle"` (position = 0) - Cycle opener
- `"On reshuffle"` (trigger when deck reshuffles) - Cycle-end trigger

**Design Notes:**
- Requires last 3 cards visible with summary info
- Most complex tracking burden on player
- Reserved for Pack 2+ cards
- Creates high-skill combo potential

---

## Pack Progression Framework

### **Pack 1 - Simple Foundations**

**Design Philosophy:** Introduction to conditions without tracking burden. All conditions use visible game state only.

**Allowed Condition Types:**
- Simple timing: "First card this cycle", "After 2nd reshuffle"
- Simple state: "If HP < 50%", "If rate > 3/sec"
- Simple count: "If 3+ Arcane cards drawn this combat"

**Complexity Rules:**
- **Single conditions only** - No AND/OR combinations
- **Always visible state** - HP bars, essence rate, reshuffle counter
- **No sequence tracking** - No "previous card" mechanics
- **Binary bonuses** - All-or-nothing (no scaling)

**Example Cards:**

```
"Desperate Strike"
Common, Arcane, Combat
Base: +15 ATK, +5 DEF
Condition: If player HP < 50%: +15 additional ATK
[Teaches: HP-based timing, introduces conditions]

"Early Essence Burst"
Common, Arcane, Generator
Base: +3 Essence/sec
Condition: If drawn in first 3 cards this cycle: +2 additional Essence/sec
[Teaches: Cycle position, deck ordering matters]

"Mono-Arcane Power"
Rare, Arcane, Combat
Base: +18 ATK, +12 DEF
Condition: If 5+ Arcane cards drawn this combat: +12 ATK, +8 DEF
[Teaches: Deck composition rewards, first multi-card counting]
```

**Stat Budget Notes:**
- Commons: 20-30 base points + conditional bonus (coefficient 0.3-0.5)
- Rares: 30-50 base points + conditional bonus (coefficient 0.3-0.5)

---

### **Pack 2 - Moderate Complexity**

**Design Philosophy:** Introduce sequence tracking and scaling bonuses. Reward deck-building skill and planning.

**Allowed Condition Types:**
- All Pack 1 conditions
- Card count (this cycle): "If 3+ same tier this cycle"
- Simple sequence: "If previous card was Generator"
- Scaling bonuses: "For each X, +Y"
- Threshold tiers: "If 2+: bonus A, if 5+: bonus B"

**Complexity Rules:**
- **Single conditions or intuitive AND pairs** - "If HP < 50% AND enemy HP < 50%"
- **Last 1-2 card tracking** - Previous card effects
- **Visible cycle summary** - Show cards drawn this cycle by tier
- **Scaling allowed** - Linear scaling bonuses

**Example Cards:**

```
"Elemental Harmony"
Rare, Arcane, Combat
Base: +20 ATK, +10 DEF
Condition: For each different tier drawn this cycle, +5 ATK
[Teaches: Multi-tier decks, scaling bonuses]

"Chain Generator"
Rare, Arcane, Generator
Base: +4 Essence/sec
Condition: If previous card was also a Generator: +3 additional Essence/sec
[Teaches: Sequence tracking, deck ordering strategy]

"Growing Power"
Rare, Arcane, Combat
Base: +15 ATK, +15 DEF
Condition: After 2nd reshuffle: +10 ATK, +10 DEF
           After 4th reshuffle: +20 ATK, +20 DEF
[Teaches: Multiple thresholds, long combat scaling]

"Balanced Master"
Epic, Arcane, Combat
Base: +30 ATK, +30 DEF
Condition: If your ATK equals your DEF (within 10%): +25 ATK, +25 DEF
[Teaches: Stat relationships, build-around requirement]
```

**Stat Budget Notes:**
- Rares: 30-50 base points + conditional (coefficient 0.2-0.6 depending on difficulty)
- Epics: 50-90 base points + conditional (coefficient 0.2-0.6)
- Coefficients vary based on deck archetype alignment

---

### **Pack 3 - Full Complexity**

**Design Philosophy:** Unlocks all mechanical depth. Enables advanced combos, deck manipulation, and high-skill play.

**Allowed Condition Types:**
- All Pack 1 & 2 conditions
- Complex sequences: "If last 3 cards were all Combat type"
- Multiple counts: "If 5+ Combat AND 2+ Generator this combat"
- State relationships: "If ATK > DEF AND rate > 5/sec"
- Negative conditions: "Powerful effect BUT take damage if..."

**Complexity Rules:**
- **AND/OR conditions allowed** - Complex boolean logic
- **Last 3 card tracking** - Full sequence visibility required
- **Multiple threshold tiers** - Graduated scaling
- **Retroactive modifications** - Can affect previous card effects
- **Negative conditions** - Anti-synergy or costs

**Example Cards:**

```
"Mastered Arcane Focus"
Epic, Arcane, Combat
Base: +40 ATK, +30 DEF
Condition 1: If 5+ Arcane cards drawn this combat: +30 ATK, +20 DEF
Condition 2: If on 3rd+ reshuffle: +20 ATK, +30 DEF
[Teaches: Multiple independent conditions, both can trigger]

"Reckless Assault"
Rare, Arcane, Combat
Base: +60 ATK
Condition: If your DEF > 50: Take 10 HP damage when drawn
[Teaches: Negative conditions, anti-synergy with defensive decks]

"Sequence Master"
Epic, Arcane, Synergy
Base: +25 ATK, +15 DEF
Condition: If last 3 cards were all different types: +40 ATK, +25 DEF
[Teaches: Complex sequence tracking, huge payoff for skill]

"Desperate Gambit"
Legendary, Arcane, Combat
Base: +50 ATK, +30 DEF
Condition: If player HP < 25% AND enemy HP > 50%: +100 ATK, +50 DEF
[Teaches: Multiple state conditions, clutch comeback mechanic]

"Adaptive Caster"
Legendary, Arcane, Utility
Base: +3 Essence/sec
Condition: If rate > ATK/10: Gain +30 ATK instead of essence this draw
           If ATK > rate×10: Gain +2 Essence/sec instead of ATK this draw
[Teaches: Dynamic adaptation, build flexibility]
```

**Stat Budget Notes:**
- Epics: 50-90 base points + conditional (coefficient 0.1-0.6)
- Legendaries: 90-180 base points + conditional (coefficient 0.1-0.6)
- Complex conditions typically have lower coefficients (harder to trigger)
- Negative conditions reduce base cost (balanced by drawback)

---

## Condition Coefficient System

### Purpose

Balancing framework for conditional bonuses. Conditions reduce the stat point cost based on trigger probability and difficulty.

**Formula:**
```
actual_stat_cost = bonus_value × condition_coefficient
```

**Example:**
```
"+100 ATK if HP < 10%" with coefficient 0.05
Cost = 100 × 0.05 = 5 stat points
```

---

### Coefficient Guidelines

These are **starting points** for design. Each card will be tuned individually based on intended deck archetype and playtesting.

#### Always/Almost Always True (0.8-1.0)
Conditions that are nearly guaranteed in normal gameplay:
- "If deck has 8+ cards" (nearly always true after Pack 1)
- "After 1st reshuffle" (guaranteed in most fights)
- "If player HP < 100" (trivial, essentially unconditional)

**Usage:** Avoid these - too easy to trigger, essentially free bonuses.

---

#### Often True (0.5-0.7)
Conditions that trigger regularly with minimal deck-building:
- "If HP < 75%" (common in challenging fights)
- "If 3+ same tier this cycle" (achievable with 50%+ mono-tier deck)
- "If previous card was Combat type" (60%+ of most decks)
- "After 2nd reshuffle" (common in non-trivial fights)

**Usage:** Pack 1 simple conditionals, teaching mechanics.

---

#### Sometimes True (0.3-0.5)
Conditions requiring deck-building or situational awareness:
- "If first 3 cards this cycle" (30-40% in 8-12 card decks)
- "If previous card was Generator" (depends on 25-35% generator ratio)
- "If 5+ same tier drawn this combat" (requires mono-tier commitment)
- "If ATK > DEF" (requires offensive build focus)
- "After 3rd reshuffle" (longer fights, not guaranteed)

**Usage:** Pack 1-2 build-around conditions, strategic deck choices.

---

#### Rarely True (0.1-0.3)
Conditions requiring specific circumstances or risk:
- "If HP < 25%" (dangerous edge cases)
- "If 5+ same tier AND rate > 5/sec" (requires specific archetype)
- "If last 3 cards all different types" (requires balanced deck + luck)
- "If enemy HP > 75% AND player HP < 50%" (specific combat phase)
- "On 5th+ reshuffle" (very long fights only)

**Usage:** Pack 2-3 high-reward conditionals, clutch moments.

---

#### Very Rarely True (0.01-0.1)
Conditions requiring extreme circumstances or contradictory requirements:
- "If HP < 10%" (edge of death, high risk)
- "If last 3 cards all same tier AND all different types" (contradictory)
- "If total stats > 500" (only in very long fights with large decks)
- "If HP = 1" (edge of death, nearly impossible to maintain)

**Usage:** Pack 3 legendary cards, ultra-high-risk/high-reward.

---

### Per-Card Tuning Process

Rather than rigid formulas, coefficients are adjusted per card based on:

1. **Intended Deck Archetype**
   - Does the card naturally fit decks that trigger its condition?
   - Example: "If rate > 5/sec" on a generator card = higher coefficient (synergistic)
   - Example: "If rate > 5/sec" on a pure combat card = lower coefficient (build-around)

2. **Condition Complexity**
   - Simple state checks = higher coefficient (easy to evaluate)
   - Complex sequences = lower coefficient (skill reward)

3. **Risk/Reward Balance**
   - Low-risk conditions = higher coefficient (predictable trigger)
   - High-risk conditions = lower coefficient (clutch moments)

4. **Playtesting Feedback**
   - Track actual trigger rates in simulator
   - Adjust coefficients based on real gameplay data
   - Balance "feels good" vs "overpowered"

---

### Negative Condition Coefficients

Cards with drawbacks can have negative coefficients, reducing base cost:

**Example:**
```
"Reckless Assault" - +60 ATK, but take 10 damage if DEF > 50
Base cost: 60 points for ATK
Drawback: -15 points (0.3 coefficient on anti-synergy)
Total cost: 45 points (fits in Common budget with drawback)
```

**Guidelines:**
- Drawback coefficient typically 0.2-0.5 (drawbacks are annoying)
- Must be avoidable with deck-building (not pure RNG)
- Clear feedback when drawback triggers
- Reserved for Pack 2+ cards

---

## Ability Text Templates

### Writing Guidelines

1. **Clarity Over Brevity** - Players must understand what triggers the condition
2. **Consistent Format** - Use templates for similar conditions
3. **Visible State Only** - Reference things players can see on screen
4. **Natural Language** - Avoid excessive technical jargon
5. **3-Line Maximum** - Must fit card layout (12px font, 3 lines)

---

### Template Formats

#### Simple Conditional Bonus
```
[Base effect]
If [condition]: [bonus]
```

**Examples:**
- "If player HP < 50%: +15 ATK"
- "If drawn in first 3 cards this cycle: +2 Essence/sec"
- "If 5+ Arcane cards drawn this combat: +10 ATK, +5 DEF"

---

#### Scaling Bonus
```
[Base effect]
For each [counted thing], [scaling bonus]
```

**Examples:**
- "For each Fire card drawn this cycle, +5 ATK"
- "For each Generator drawn this combat, +1 Essence/sec"
- "For each reshuffle this combat, +8 ATK, +8 DEF"

---

#### Multiple Thresholds
```
[Base effect]
If [threshold 1]: [bonus 1]
If [threshold 2]: [bonus 2]
```

**Examples:**
- "After 2nd reshuffle: +10 ATK. After 4th reshuffle: +20 ATK"
- "If 3+ same tier this cycle: +10 ATK. If 6+: +25 ATK"
- "If rate > 3/sec: +15 ATK. If rate > 7/sec: +35 ATK"

---

#### Sequence Condition
```
[Base effect]
If [previous/last N cards were X]: [bonus]
```

**Examples:**
- "If previous card was Generator: +3 Essence/sec"
- "If last 2 cards were both Combat: +20 ATK"
- "If last 3 cards were all different tiers: +30 ATK, +15 DEF"

---

#### Negative Condition
```
[Powerful base effect]
BUT if [anti-condition]: [drawback]
```

**Examples:**
- "+60 ATK. BUT if DEF > 50: Take 10 damage"
- "+50 ATK, +30 DEF. BUT if rate > 5/sec: This card gives +0 essence"
- "+80 ATK. BUT if drawn after 5th card this cycle: -40 ATK"

---

#### Multiple Independent Conditions
```
[Base effect]
• If [condition 1]: [bonus 1]
• If [condition 2]: [bonus 2]
```

**Examples:**
- "• If 5+ Arcane drawn this combat: +20 ATK"
- "• If on 3rd+ reshuffle: +15 DEF"
- (Both can trigger independently)

---

### Keyword Shorthand (Future Enhancement)

For future consideration (not Pack 1-3):

- **Opener:** "First card after reshuffle"
- **Finisher:** "If enemy HP < 25%"
- **Desperate:** "If player HP < 25%"
- **Pure [Tier]:** "If all cards this cycle are [Tier]"
- **Chained:** "If previous card was same tier/type"

**Note:** Don't implement keywords until Pack 4+. Explicit text is clearer for early game.

---

## Combat UI Tracking Requirements

**CRITICAL:** These conditions require specific UI elements to be trackable and fair.

### Required Visual Elements

#### 1. Reshuffle Counter
**Location:** Near deck indicator  
**Format:** "Cycle 3" or "Reshuffle: 2"  
**Updates:** Increment on each deck reshuffle  
**Purpose:** Tracks timing conditions based on reshuffle count

---

#### 2. Cards Drawn This Cycle
**Location:** Near deck indicator or as overlay  
**Format:** Icon summary with counts:
```
Cycle: 5 cards drawn
🔮 Arcane: 3
⚔️ Combat: 4
💎 Generator: 1
```
**Updates:** Real-time as cards drawn, resets on reshuffle  
**Purpose:** Tracks card_count conditions within current cycle

---

#### 3. Last 3 Cards Drawn
**Location:** Below player stats or above combat log  
**Format:** 3 small card summary blocks (most recent on right)

**Each Block Contains:**
- Card name (10px)
- Tier (color border)
- Type icon (Combat/Generator/etc)
- Key stats (ATK/DEF or Essence)

**Example:**
```
┌──────────┐  ┌──────────┐  ┌──────────┐
│ Arcane   │  │ Power    │  │ Essence  │
│ Bolt     │  │ Strike   │  │ Burst    │
│ ⚔️ +20ATK │  │ ⚔️ +15/5 │  │ 💎 +250  │
└──────────┘  └──────────┘  └──────────┘
  (2 ago)       (1 ago)       (current)
```

**Updates:** Slides left when new card drawn (shift+add pattern)  
**Purpose:** Enables sequence condition evaluation

---

#### 4. Cards Drawn This Combat
**Location:** Expandable panel or always-visible counter  
**Format:** Running totals with tier/type breakdown:
```
Combat: 23 cards drawn
🔮 Arcane: 15
🔥 Fire: 5
💧 Water: 3

⚔️ Combat: 18
💎 Generator: 5
```

**Updates:** Real-time throughout combat  
**Resets:** On combat end (new enemy)  
**Purpose:** Tracks cumulative combat conditions

---

#### 5. Current Game State Panel
**Location:** Always visible, center/top of combat area  
**Contains:**
- Player HP bar (with percentage)
- Enemy HP bar (with percentage)
- Current ATK/DEF totals
- Current essence rate (Essence/sec)

**Purpose:** All state-based conditions reference these values

---

### Visual Priority Hierarchy

**Critical (Always Visible):**
1. HP bars (player and enemy)
2. Current stats (ATK/DEF/Rate)
3. Reshuffle counter
4. Last 3 cards drawn

**Important (Visible but Compact):**
5. Cards drawn this cycle (with tier/type breakdown)

**Optional (Expandable/Hover):**
6. Cards drawn this combat (full breakdown)

---

### Mobile/Compact View Considerations

For smaller screens:
- Last 3 cards: Show as icons only (expand on tap)
- Cards drawn this cycle: Show count only (expand for breakdown)
- Prioritize HP bars and current stats
- Reshuffle counter always visible but compact

---

## State Persistence Rules

**CRITICAL:** Understanding what resets and when is essential for designing conditional cards and player strategy. This section consolidates all persistence rules for card designers.

### What Resets and When

#### On Reshuffle (Deck Cycles)

**Resets:**
- Cards drawn this cycle → 0
- Cycle position counter → 0 (starts new cycle)
- Card sequence history (last 3 cards) → clears

**Persists:**
- ATK stat (accumulated from all cards)
- DEF stat (accumulated from all cards)
- Essence rate (accumulated from generator cards)
- Cards drawn this combat counter
- HP (no healing on reshuffle)

**Design Implications:**
- "This cycle" conditions create predictable reset points
- Cycle position conditions enable "opener" and "finisher" cards
- Sequence conditions create short-term memory gameplay

---

#### On New Enemy (Combat End)

**Resets:**
- Cards drawn this combat → 0
- ATK stat → 0 (fresh start for new enemy)
- DEF stat → 0 (fresh start for new enemy)
- Card sequence history → clears
- Reshuffle counter → 0

**Persists:**
- Essence rate (accumulates across all enemies until death)
- HP (no healing between enemies - intentional death spiral)
- Accumulated essence (resource continues growing)
- Deck composition (no forced changes)

**Design Implications:**
- Essence rate is the only combat stat that persists between enemies
- HP management is critical for multi-enemy runs
- "This combat" counters enable escalating bonuses within single enemy fights
- Defense must be re-established each enemy (no carryover protection)

---

#### On Death (Player HP = 0)

**Resets:**
- All combat stats (ATK → 0, DEF → 0, Essence rate → 0)
- Enemy counter → 1 (restart from beginning)
- HP → full restore (based on permanent max HP from shard upgrades)
- All combat tracking counters (this combat, this cycle, sequence history)

**Persists:**
- Accumulated essence (spend on packs)
- Accumulated shards (spend on permanent upgrades)
- Deck composition (all cards remain)
- Permanent upgrades (max HP increases, future class unlocks)

**Design Implications:**
- Death is progression, not punishment (resources persist)
- Each run starts fresh but with better deck/HP
- Conditional abilities based on "enemy number" or "death count" are intentionally avoided (meta-progression would complicate balance)
- Essence rate reset encourages generator-heavy deck strategies for each run

---

### Cross-Document References

**Combat System:** Full combat mechanics and death screen details in [combat-system.md](combat-system.md)  
**Resource Economy:** Essence rate persistence and generation in [resource-economy.md](resource-economy.md)  
**Progression System:** Death loop progression expectations in [progression.md](progression.md)

---

## Validation Checklist

- [x] All four condition type categories defined (Timing, Card_Count, State, Sequence)
- [x] Clear distinction between "this combat", "this cycle", and "in deck" tracking
- [x] Pack 1-3 progression framework with complexity rules
- [x] Example cards for each pack tier
- [x] Condition coefficient system with guidelines (0.01-1.0 scale)
- [x] Coefficient guidelines for trigger probability
- [x] Per-card tuning process documented
- [x] Negative condition coefficients specified
- [x] Ability text templates for all condition types
- [x] Writing guidelines for card text (3-line max)
- [x] Combat UI tracking requirements defined
- [x] Visual mockups for last 3 cards drawn
- [x] Mobile/compact view considerations

---

## Document History

**Version 1.1** (2025-11-12) - Task 2.1.5 Complete
- Added consolidated State Persistence Rules section
- Documented reset behavior for reshuffle, enemy, and death
- Added design implications for each reset type
- Cross-referenced to combat-system.md, resource-economy.md, progression.md

**Version 1.0** (2025-11-10) - Task 2.1.4 Complete
- Created comprehensive conditional mechanics framework
- Defined all four condition type categories
- Established Pack 1-3 progression with complexity rules
- Created condition coefficient system with balancing guidelines
- Documented ability text templates for all condition patterns
- Specified combat UI tracking requirements
- Added visual mockups for card history tracking
- Ready for Pack 1 card design in Phase 3

---

**Document Status:** Complete  
**Next Steps:** Proceed to Task 2.1.6 (Card Data Structure & Text Format)

