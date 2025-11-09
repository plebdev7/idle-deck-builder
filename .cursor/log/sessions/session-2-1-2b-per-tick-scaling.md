# Task 2.1.2B: Per-Tick Enemy Scaling System

**Task Reference:** CHECKLIST.md Task 2.1.2B  
**Session:** 2.1 (Pack Card Design - Foundation Research)  
**Status:** ✅ COMPLETE  
**Date:** 2025-11-08 23:43:00

---

## Objective

Evaluate and resolve balance issues between enemy ATK (static) vs Player DEF (exponentially growing through deck cycling), and implement dynamic per-tick enemy scaling system.

---

## Problem Statement

### The Scaling Issue

**Player DEF scaling (Dynamic - grows continuously):**
- Starter deck provides 56 total DEF when all cards drawn
- Continuous deck cycling = exponential growth
- Cycle 1: 56 DEF, Cycle 2: 112 DEF, Cycle 3: 168 DEF, etc.
- Average growth: ~6.9 ATK/tick, ~6.2 DEF/tick (8-card starter deck)

**Enemy ATK scaling (Static - OLD SYSTEM):**
- Enemy 50: 10 ATK (fixed)
- Enemy 100: 30 ATK (fixed)
- Enemy 150: 80 ATK (fixed)

**Result:**
- First ~10-20 seconds: Player vulnerable (building DEF)
- After 2-3 cycles: DEF >> ATK permanently
- No sustained threat in long fights
- Defense builds achieve "default invulnerability" with minimal investment
- HP becomes meaningless after defense threshold

---

## User Requirements

1. **No Default Invulnerability:** Late invulnerability shouldn't be default; defensive builds should require investment
2. **Per-Tick Scaling:** Enemy ATK/DEF should grow each tick
3. **All Enemies Get Attack:** Even Enemy 1 should have attack from tick 0
4. **Graduated Scaling:** Per-tick rates should scale with enemy number (like HP formulas)
5. **Bosses Scale Faster:** Boss fights should become more dangerous over time
6. **Remove Safe Tutorial:** No penalty for death, players learn by dying

---

## Solution: Per-Tick Enemy Scaling System

### Core Mechanic

```
Enemy ATK at tick N = ATK_per_tick × N
Enemy DEF at tick N = DEF_per_tick × N

Where ATK_per_tick and DEF_per_tick scale with enemy number
```

### Per-Tick Rate Formulas

**Act 1 (Enemies 1-50): Learning Phase**
```
ATK_per_tick = 1.0 + (n - 1) × 0.05
DEF_per_tick = 0.5 + (n - 1) × 0.025

Enemy 1:  1.0 ATK/tick, 0.5 DEF/tick
Enemy 25: 2.2 ATK/tick, 1.1 DEF/tick
Enemy 50: 3.45 ATK/tick, 1.73 DEF/tick

Design: Slower than player growth = manageable
```

**Act 2 (Enemies 51-100): Challenge Phase**
```
ATK_per_tick = 3.5 + (n - 51) × 0.08
DEF_per_tick = 1.75 + (n - 51) × 0.04

Enemy 51:  3.5 ATK/tick, 1.75 DEF/tick
Enemy 75:  5.42 ATK/tick, 2.71 DEF/tick
Enemy 100: 7.42 ATK/tick, 3.71 DEF/tick

Design: Approaches player growth = tense
```

**Act 3 (Enemies 101-150): Master Phase**
```
ATK_per_tick = 7.5 + (n - 101) × 0.12
DEF_per_tick = 3.75 + (n - 101) × 0.06

Enemy 101: 7.5 ATK/tick, 3.75 DEF/tick
Enemy 125: 10.38 ATK/tick, 5.19 DEF/tick
Enemy 150: 13.38 ATK/tick, 6.69 DEF/tick

Design: Faster than player growth = intense
```

**Bosses (All):**
```
ATK_per_tick = regular_rate × 2.0
DEF_per_tick = regular_rate × 2.0

Enemy 50 Boss:  6.9 ATK/tick (matches player DEF growth!)
Enemy 100 Boss: 14.84 ATK/tick (exceeds player growth!)
Enemy 150 Boss: 26.76 ATK/tick (way exceeds player growth!)
```

---

## Files Modified

### 1. game-data/balance-config.json

**Added:** Complete `enemy_scaling` configuration section

**Key Additions:**
- `hp_formulas`: Act-based HP formulas for all enemy ranges
- `boss_multipliers`: HP multipliers (1.3×, 1.5×, 2.0×) and per-tick rate multiplier (2.0×)
- `per_tick_scaling`: Graduated scaling rates for Acts 1-3
  - `atk_base`, `atk_growth_per_enemy`: Base rate and growth coefficient
  - `def_base`, `def_growth_per_enemy`: Base rate and growth coefficient
  - Formulas documented for each Act
- `design_rationale`: Explains per-tick system, no default invulnerability, graduated scaling
- `balance_targets`: Expected per-tick rates for key enemies (1, 50, 100, 150) with design notes

**Configuration Structure:**
```json
"enemy_scaling": {
  "per_tick_scaling": {
    "act_1": {
      "atk_base": 1.0,
      "atk_growth_per_enemy": 0.05,
      "def_base": 0.5,
      "def_growth_per_enemy": 0.025,
      "formula_atk": "1.0 + (n - 1) * 0.05",
      "formula_def": "0.5 + (n - 1) * 0.025"
    }
    // ... act_2, act_3
  },
  "boss_multipliers": {
    "per_tick_rates": {
      "multiplier": 2.0
    }
  }
}
```

### 2. docs/design-specs/progression.md

**Replaced:** Entire "Enemy Attack Scaling" section with "Enemy Attack/Defense Scaling (Per-Tick System)"

**Key Changes:**
- Removed static ATK values and "safe learning phase" (Enemies 1-49 with 0 ATK)
- Added graduated per-tick scaling formulas for Acts 1-3
- Added boss per-tick multiplier (2.0×)
- Added combat tick examples for Enemy 1, 50 (regular & boss), 150 boss
- Added design rationale explaining no safe phase, no default invulnerability
- Added strategic build diversity section (Glass Cannon, Tank, Balanced, Healing Focus)

**New Section Headers:**
- Design Philosophy
- Per-Tick Scaling Formulas
- Combat Tick Examples
- Design Rationale

### 3. docs/design-specs/combat-system.md

**Updated:** Damage formulas to include per-tick enemy stat calculation

**Changes:**
```
Added:
Enemy_Attack = ATK_per_tick × ticks_elapsed
Enemy_Defense = DEF_per_tick × ticks_elapsed

Where ATK_per_tick and DEF_per_tick scale with enemy number
(See progression.md for complete per-tick scaling formulas)
```

### 4. CHECKLIST.md

**Marked Complete:** Task 2.1.2B with completion timestamp and deliverables

---

## Strategic Implications

### Build Diversity Created

**Glass Cannon (High ATK, Low DEF):**
- Kill enemies quickly before they ramp
- Risky but efficient
- Lower HP requirements
- Fast progression

**Tank Build (Low ATK, High DEF):**
- Survive enemy ramping with serious DEF investment
- Safer but slower kills
- Requires more HP and healing
- Steady progression

**Balanced Build:**
- Moderate ATK and DEF
- Middle ground between risk and safety
- Most flexible

**Healing Focus:**
- HP regen/healing cards critical
- Enables long runs and boss attempts
- Sustains through dangerous late-fight phases

### Card Design Impact (Task 2.1+)

**Higher stat budgets needed:**
- Combat is more dangerous now
- Pack cards must provide meaningful power increases
- Healing/HP regen cards gain strategic value

**Suggested adjustments:**
- Common: 30-40 stat points (was 20-30)
- Rare: 50-70 stat points (was 30-50)  
- Epic: 80-120 stat points (was 50-90)

**New card types enabled:**
- Instant heal cards
- HP regen cards (per tick until next enemy)
- Max HP boost cards (temporary)
- Lifesteal cards (damage → healing)
- Shield/barrier cards

---

## Balance Targets

### Enemy 1
- **ATK per tick:** 1.0
- **DEF per tick:** 0.5
- **Player vs Enemy:** Player outpaces (6.9 vs 1.0 ATK/tick)
- **Result:** Manageable learning experience

### Enemy 50 Boss
- **ATK per tick:** 6.9 (2× regular rate of 3.45)
- **DEF per tick:** 3.46
- **Player vs Enemy:** Matched rates (6.2 vs 6.9 DEF/tick)
- **Result:** Very dangerous, requires good play or Pack 1

### Enemy 100 Boss
- **ATK per tick:** 14.84
- **DEF per tick:** 7.42
- **Player vs Enemy:** Enemy faster than player
- **Result:** Requires Pack 1 with strong defensive investment

### Enemy 150 Boss
- **ATK per tick:** 26.76
- **DEF per tick:** 13.38
- **Player vs Enemy:** Enemy much faster than player
- **Result:** Requires Packs 1-3 and optimized defensive or fast-kill strategy

---

## Design Decisions

### Decision 1: Remove Safe Tutorial Phase
**Rationale:** Death has no penalty. Players learn by dying. Artificial "safe zone" not needed.

### Decision 2: Per-Tick Scaling from Tick 0
**Rationale:** First tick values = per-tick rate (no offset exceptions). Consistency in formulas.

### Decision 3: Graduated Scaling Rates
**Rationale:** Per-tick rates grow with enemy number, matching HP formula approach. Creates smooth difficulty curve.

### Decision 4: Boss 2× Multiplier
**Rationale:** Long boss fights become extremely dangerous. Encourages fast-kill strategies or serious defensive investment.

### Decision 5: All Configuration in balance-config.json
**Rationale:** Coefficients (0.05, 0.08, 0.12) and base values controllable. Easy to tune and test.

---

## Next Steps

### Immediate (Task 2.1.2C)
- Create Pack 1+2 cards with adjusted stat budgets
- Model essence generation with new cards
- Test combat effectiveness against per-tick scaling
- Validate Enemy 100 boss feasibility with Pack 1

### Implementation (Future Task)
- Update simulator combat.py to implement per-tick enemy scaling
- Read from balance-config.json enemy_scaling section
- Test all formulas and validate balance targets
- Update validation system for new combat dynamics

### Documentation
- ✅ balance-config.json updated
- ✅ progression.md updated
- ✅ combat-system.md updated
- ✅ CHECKLIST.md marked complete

---

## Cross-References

**Related Tasks:**
- Task 2.1.2A: Stat point system and card data structure (prerequisite)
- Task 2.1.2C: Pack 1+2 card design (next step, uses per-tick scaling targets)
- Task 2.1.3: Card leveling concept (affected by new difficulty)

**Related Documents:**
- DESIGN.md: Main design hub (references progression.md and combat-system.md)
- docs/design-specs/progression.md: Complete per-tick scaling specification
- docs/design-specs/combat-system.md: Tick-based combat with per-tick damage
- docs/design-specs/baseline-numbers.md: Will need updates for new combat timing
- game-data/balance-config.json: Source of truth for all enemy scaling values

---

## Validation Required

**After Implementation:**
1. Test Enemy 1 with starter deck (should lose ~10-15 HP)
2. Test Enemy 50 boss with starter deck (should be very dangerous)
3. Test Enemy 100 boss with Pack 1 (should be beatable)
4. Test Enemy 150 boss with Packs 1-3 (should require optimization)
5. Verify defensive builds require serious DEF investment
6. Verify glass cannon builds can win by killing fast
7. Confirm no "default invulnerability" with basic defense

---

**Task Status:** ✅ COMPLETE  
**Completion Date:** 2025-11-08 23:43:00  
**User Approval:** Confirmed design approach and configuration structure  
**Ready for Implementation:** Yes (future task)

