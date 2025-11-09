# Task 2.1.2A: Stat Point System & Card Data Structure

**Session:** 2.1.2A - Design Tool and Shared JSON Structure  
**Date:** 2025-11-08 20:01:11  
**Status:** In Progress  
**Related:** CHECKLIST.md Task 2.1.2A, ROADMAP.md Session 2.1

---

## Session Goal

Create a unified stat point system and JSON-based card data structure that can be shared between the Python simulator and the web game implementation. This ensures balance values are centralized and easily tweakable.

---

## Key Decisions Made

### Decision 1: Deck Size for Arcane Student = 12 Cards

**Rationale:**
- Start with 8 cards, Pack 1 adds 5 → 13 total
- Immediately forces cutting 1 card (teaches deck building on Pack 1)
- Perfect tension point for learning
- 12-card deck cycles every 12 seconds (clean timing)
- Later classes can have 15-18-21 cards (feels substantial)

### Decision 2: Starter Cards Are Common Rarity

**Rationale:**
- Pack 1 cards use sidegrade design (not strictly better)
- Starter cards can appear in Pack 4+ random pools
- Starter cards can be leveled
- Adds healing/tradeoff mechanics to avoid power creep

### Decision 3: Essence Burst and Mystic Shield Buffs

**Changes:**
- Essence Burst: 150 → 250 flat Essence (25 stat points, was 15)
- Mystic Shield: 18 → 20 DEF (20 stat points, was 18)

**Rationale:**
- Brings starter cards into proper Common rarity range (20-30 points)
- Essence Burst now competitive with rate generators
- Mystic Shield now symmetrical with Arcane Bolt (both 20)

### Decision 4: Stat Point Conversion Rates

```
1 stat point = 1 ATK
1 stat point = 1 DEF
1 stat point = 10 flat Essence
1 stat point = 0.1 Essence/sec
1 stat point = 0.5 HP heal (instant)
1 stat point = 0.1 HP/sec regen (until next enemy)
```

**Rationale:**
- ATK/DEF 1:1 (both equally valuable)
- Essence/sec expensive (10 points per 0.1/sec) because it accumulates
- Flat Essence cheap (0.1 points per 1 Essence) for burst value
- Healing moderately expensive (survival is valuable)

### Decision 5: Enemy Attack Timing

**Proposed Change:** Enemies start attacking at Enemy 20 (not Enemy 50)

**New Attack Scaling:**
```
Enemy 1-19: 0 ATK (safe tutorial zone)
Enemy 20-39: 2-5 ATK (first deaths without defense/healing)
Enemy 40-49: 6-9 ATK (getting serious)
Enemy 50: 10 ATK (mini-boss, first real wall)
Enemy 51+: Continued scaling
```

**Rationale:**
- Defense and healing matter from Pack 1
- First death at Enemy 25-30 teaches death loop naturally
- Pack 1 purchase motivated by death (not arbitrary milestone)
- Makes sidegrade design space (healing/defense) immediately valuable

**Status:** Proposed, awaiting implementation in Session 2.0.3 update

---

## Files Created

### `game-data/balance-config.json`
Central configuration file containing:
- Stat point conversion rates
- Rarity stat budgets (Common: 20-30, Rare: 30-50, Epic: 50-90, Legendary: 90-180)
- Deck size limits (Arcane Student: 12 cards)
- Rarity drop rates (Arcane: 70/20/8/2, Elemental: 50/30/15/5)
- Leveling system parameters
- Pack costs (Arcane and Elemental)
- Combat timing values
- Player HP system

### `game-data/cards-schema.json`
JSON Schema definition for all card data:
- Card metadata structure
- Effect types and parameters
- Condition system
- Duration types
- Acquisition information

### `game-data/cards-starter-deck.json`
Starter deck card definitions (8 cards):
- All cards in JSON format matching schema
- Stat point budgets included for validation
- Effects properly structured
- All cards validated against Common rarity (20-30 points)

### `game-data/README.md`
Documentation for game-data directory:
- File descriptions
- Usage examples for Python and JavaScript
- Design principles
- Version history

---

## Starter Deck Audit (Stat Points)

| Card | Type | Effects | Stat Points | Status |
|------|------|---------|-------------|--------|
| Arcane Conduit | Generator | +2 Essence/sec | 20 | ✓ |
| Essence Burst | Generator | +250 flat | 25 | ✓ (updated 150→250) |
| Combat Siphon | Hybrid | +1 Ess/sec + 12 ATK + 6 DEF | 28 | ✓ |
| Arcane Bolt | Combat | 20 ATK | 20 | ✓ |
| Mystic Shield | Combat | 20 DEF | 20 | ✓ (updated 18→20) |
| Balanced Strike | Combat | 10 ATK + 10 DEF | 20 | ✓ |
| Power Strike | Combat | 15 ATK + 5 DEF | 20 | ✓ |
| Stalwart Guard | Combat | 5 ATK + 15 DEF | 20 | ✓ |

**Range:** 20-28 stat points (well-balanced within Common rarity 20-30)

---

## Documentation Updates

### `docs/design-specs/card-system.md` - Updated
- Added Card Rarity System section (Session 2.1.1)
- Added Stat Point System section (Session 2.1.2A)
- Updated Essence Burst stats (150 → 250)
- Updated Mystic Shield stats (18 → 20)
- Updated total deck stats (DEF: 54 → 56, Essence: 150 → 250)
- Added starter deck stat point audit

### `CHECKLIST.md` - Updated
- Added Task 2.1.2A as subtask of 2.1.2
- Marked conversion rates as complete
- Marked starter card updates as complete
- Marked JSON schema creation as complete
- Next: Implement JSON loading in simulator

---

## Next Steps

1. **Update Simulator to Load JSON Data**
   - Modify `simulator/core/cards.py` to load from JSON
   - Modify `simulator/core/economy.py` to load balance config
   - Update `simulator/core/deck.py` for 12-card limit
   - Test that simulator still works with JSON data

2. **Validate Enemy Attack Timing Change**
   - Update enemy attack formula in `simulator/core/combat.py`
   - Enemies 20+ start attacking
   - Update validation targets
   - Run sim live to observe first death timing

3. **Design Pack 1 Cards (Task 2.1.2 continuation)**
   - 4 Common + 1 Rare
   - Use sidegrade design (healing, tradeoffs)
   - Validate with stat point system
   - Create `game-data/cards-pack1.json`

---

## Questions for Next Session

1. **Should we implement Enemy 20 attack change now or defer?**
   - Pro: Makes healing/defense relevant immediately
   - Con: Requires revalidation of timing targets

2. **Should Pack 1 cards include healing effects?**
   - Need to decide before designing Pack 1 roster
   - Healing only valuable if enemies attack earlier

3. **Should we add a stat point calculator tool?**
   - Python script to validate card budgets?
   - Help design new cards within budget?

---

**Session Status:** ✅ **PARTIALLY COMPLETE** - JSON structure done, simulator integration pending

**Files Changed:**
- `game-data/balance-config.json` (created)
- `game-data/cards-schema.json` (created)
- `game-data/cards-starter-deck.json` (created)
- `game-data/README.md` (created)
- `docs/design-specs/card-system.md` (updated)
- `CHECKLIST.md` (updated)

**Next Task:** Implement JSON loading in simulator, then return to Task 2.1.2 (Pack 1 design)


