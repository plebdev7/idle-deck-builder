# Game Data Directory

**Purpose:** Centralized JSON data files for all game content and balance values. These files are the **authoritative source of truth** for specific values, implementations, and configurations used by both the Python simulator and the web game.

---

## Data Ownership Model

### Game Data Owns: INSTANCES, SPECIFIC VALUES, IMPLEMENTATIONS
- **What:** Actual card stats, exact costs, specific configurations, conversion rates
- **Why:** Single source of truth for what the game actually uses
- **Examples:** The exact stats of "Arcane Bolt", pack cost of 40,000 Essence, conversion rate of 1.0 for ATK

### Design Docs Own: SYSTEMS, FORMULAS, RATIONALE
- **What:** Game mechanics, scaling formulas, design principles, the "why" behind decisions
- **Why:** Explains the design thinking and mathematical models
- **Examples:** Enemy HP scaling by act formula, boss multiplier system, resource generation mechanics

### Cross-Reference Requirements
- Game data files include `_design_spec` fields linking to the design documents that define their system
- Design docs reference specific game-data files for implementation details
- Changes to formulas in design docs → must regenerate/validate game-data
- Changes to specific values in game-data → may not need design doc updates (unless formula changes)

---

## Files

### `balance-config.json`
**Central configuration for all game balance values**

Contains:
- Stat point conversion rates (ATK/DEF/Essence/Healing)
- Rarity stat budgets (Common: 20-30, Rare: 30-50, Epic: 50-90, Legendary: 90-180)
- Deck size limits per class
- Rarity drop rates for pack types
- Leveling system parameters
- Pack costs and formulas
- Combat timing values
- Player HP system

**Usage:**
- Load this file to get all tunable balance parameters
- Modify conversion rates here to rebalance the entire game
- Both simulator and web game read from this single source

---

### `cards-schema.json`
**JSON Schema definition for all card data**

Defines the structure for card definitions including:
- Card metadata (id, name, tier, rarity, type)
- Stat point budget (for balance validation)
- Effects array (all card effects)
- Effect types (attack, defense, essence, healing, conditionals, etc.)
- Condition system (timing, card count, state, sequence)
- Duration types (instant, until_enemy_defeated, until_death, etc.)
- Acquisition information (starter, guaranteed packs, random pools)

**Usage:**
- Validate all card JSON files against this schema
- Reference when creating new cards
- Ensures consistency across all card definitions

---

### `cards-starter-deck.json`
**Starter deck cards (8 cards for Arcane Student class)**

Contains all 8 starter cards:
- **Generators (3):** Arcane Conduit, Essence Burst, Combat Siphon
- **Combat (5):** Arcane Bolt, Mystic Shield, Balanced Strike, Power Strike, Stalwart Guard

**Stat Point Audit:**
- All cards: 20-28 stat points (within Common rarity 20-30 range)
- Total when drawn: 62 ATK, 56 DEF, +3 Essence/sec, +250 flat Essence

---

## Future Files

### `cards-pack1.json` (To Be Created)
Pack 1 guaranteed cards (4 Common + 1 Rare)

### `cards-pack2.json` (To Be Created)
Pack 2 guaranteed cards (4 Common + 1 Rare)

### `cards-pack3.json` (To Be Created)
Pack 3 guaranteed cards (4 Common + 1 Epic)

### `cards-random-pool.json` (To Be Created)
Random card pool for Pack 4+ (5-10 cards per tier)

---

## Design Principles

### 1. Single Source of Truth
- All balance values in `balance-config.json`
- All card stats in respective card JSON files
- No hardcoded values in simulator or web game code

### 2. Easy Rebalancing
- Change conversion rates in one place
- Automatically affects all card evaluations
- Stat point budgets validate card power levels

### 3. Shared Between Implementations
- Python simulator loads JSON for testing
- Web game loads JSON for gameplay
- Guaranteed consistency between environments

### 4. Validation
- All cards include `stat_point_budget` field
- Can validate cards match their rarity budget
- Can audit power creep across packs

---

## Implementation Notes

### For Simulator
```python
import json

# Load balance config
with open('game-data/balance-config.json') as f:
    balance = json.load(f)

# Load starter deck
with open('game-data/cards-starter-deck.json') as f:
    starter_cards = json.load(f)

# Use conversion rates
conversion = balance['stat_point_system']['conversion_rates']
atk_cost = conversion['ATK']['value']  # 1.0
```

### For Web Game
```javascript
// Load balance config
const balance = await fetch('game-data/balance-config.json').then(r => r.json());

// Load starter deck
const starterDeck = await fetch('game-data/cards-starter-deck.json').then(r => r.json());

// Use conversion rates
const conversion = balance.stat_point_system.conversion_rates;
const atkCost = conversion.ATK.value; // 1.0
```

---

## Version History

**Version 1.1.0** (2025-11-09) - Data Ownership Model (Task Pre-2.1)
- **Added Data Ownership Model** documentation
- Added `_design_spec` cross-reference fields to JSON files
- Established game-data as authoritative source for specific values
- Updated descriptions to clarify role as implementation truth
- Design docs now reference game-data for exact values
- Rationale: Prevent divergence between design and implementation

**Version 1.0.0** (2025-11-08) - Initial Creation (Task 2.1.2A)
- Created balance-config.json with stat point system
- Created cards-schema.json for card structure
- Created cards-starter-deck.json with 8 starter cards
- Updated Essence Burst (150 → 250) and Mystic Shield (18 → 20)
- Established 12-card deck limit for Arcane Student class

---

**Last Updated:** 2025-11-09  
**Status:** Foundation complete with ownership model, Pack 1-3 cards pending Task 2.1

