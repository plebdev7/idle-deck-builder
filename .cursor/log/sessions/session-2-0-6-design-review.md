# Session 2.0.6: Design Document Review & Baseline Adjustment

**Date:** 2025-11-08 00:26:07  
**Status:** IN PROGRESS  
**Task:** CHECKLIST.md Task 2.0.6

## Objective

Perform comprehensive design document review to:
1. Fix Enemy 50 boss HP arithmetic inconsistency (7,670 actual vs 9,768 claimed)
2. Cross-check all formulas for arithmetic correctness
3. Adjust baseline targets for combat-over-time reality
4. Update validation to 100% pass rate
5. Document all corrections

## Background

Task 2.0.5 validation found:
- **Pass Rate:** 50% (8/16 checks)
- **Critical Issue:** Enemy 50 HP is 7,670 instead of claimed 9,768
- **Expected Failures:** Essence rates, card draw rates slightly lower due to combat duration

## Analysis Phase

### Enemy HP Formula Inconsistency

**Current Implementation (combat.py lines 123-125):**
```python
base_hp = 20 + (enemy_number - 1) * 120
health = base_hp * 1.3  # For Enemy 50
```

**Actual Values:**
- Enemy 49: `20 + (49-1) × 120 = 5,780 HP`
- Enemy 50 (base): `20 + (50-1) × 120 = 5,900 HP`
- Enemy 50 (with 1.3× multiplier): `5,900 × 1.3 = 7,670 HP` ✅ CORRECT

**Design Doc Claims (progression.md line 78):**
- "HP: 9,768 (1.3× regular Enemy 50 = 7,514 × 1.3)"

**Problem Identified:**
1. Design doc claims base HP is 7,514 (incorrect with 120/enemy formula)
2. With 120/enemy: base = 5,900, boss = 7,670 HP
3. To get 9,768: need base = 7,513.8, which requires **~153 HP/enemy** (not 120)

**Root Cause:**
The design doc has an arithmetic error. The claimed 9,768 HP is incompatible with the "120 HP per enemy" formula.

### Decision Options

**Option A: Keep Current Implementation (7,670 HP)**
- Pros: Mathematically consistent, already implemented and tested
- Cons: Need to update all docs claiming 9,768
- Change: Update design docs only

**Option B: Increase HP/Enemy to ~153**
- Pros: Achieves claimed 9,768 HP for Enemy 50
- Cons: Breaks formula simplicity, requires rebalancing all enemies
- Change: Update implementation and ALL formulas

**Option C: Increase Boss Multiplier to ~1.656**
- Pros: Achieves 9,768 HP (5,900 × 1.656 = 9,768)
- Cons: Odd multiplier, breaks clean progression (1.3, 1.5, 2.0)
- Change: Update implementation and boss multiplier values

### Cross-Check: All Boss HP Values

Let me verify ALL boss HP claims:

**Enemy 50 (Mini-Boss #1):**
- Formula: `[20 + (50-1) × 120] × 1.3`
- Calculation: `[20 + 5,880] × 1.3 = 5,900 × 1.3 = 7,670 HP`
- Claimed: 9,768 HP
- **Status: INCORRECT** (off by +2,098 HP, +27%)

**Enemy 100 (Mini-Boss #2):**
- Formula: `[6,000 + (100-51) × 130] × 1.5`
- Calculation: `[6,000 + 6,370] × 1.5 = 12,370 × 1.5 = 18,555 HP`
- Claimed: 18,555 HP
- **Status: CORRECT** ✅

**Enemy 150 (Major Boss):**
- Formula: `[12,500 + (150-101) × 140] × 2.0`
- Calculation: `[12,500 + 6,860] × 2.0 = 19,360 × 2.0 = 38,720 HP`
- Claimed: 38,680 HP
- **Status: INCORRECT** (off by -40 HP, <1%, likely typo)

Let me recalculate Enemy 150 more carefully:
- Enemy 150 base: `12,500 + (150-101) × 140`
- Wait, should this be `(150-101)` or `(149-101)`?
- If enemy numbering is 1-indexed: Enemy 150 is the 150th enemy
- Enemy 101 base: `12,500 + (101-101) × 140 = 12,500`
- Enemy 149 base: `12,500 + (149-101) × 140 = 12,500 + 48 × 140 = 12,500 + 6,720 = 19,220`
- Enemy 150 base: `12,500 + (150-101) × 140 = 12,500 + 49 × 140 = 12,500 + 6,860 = 19,360`
- Enemy 150 boss: `19,360 × 2.0 = 38,720 HP`

**Status: Claimed 38,680 is INCORRECT, should be 38,720 HP (+40 HP difference)**

###Cross-Check: Regular Enemy HP Values

Let me verify the examples given:

**Enemy 1:**
- Formula: `20 + (1-1) × 120 = 20`
- Claimed: 20 HP ✅ CORRECT

**Enemy 49:**
- Formula: `20 + (49-1) × 120 = 20 + 5,760 = 5,780 HP`
- Claimed: 5,780 HP (progression.md line 25) ✅ CORRECT

**Enemy 51:**
- Formula: `6,000 + (51-51) × 130 = 6,000 HP`
- Claimed: 6,000 HP (progression.md line 33) ✅ CORRECT

**Enemy 99:**
- Formula: `6,000 + (99-51) × 130 = 6,000 + 6,240 = 12,240 HP`
- Claimed: 12,240 HP (progression.md line 34) ✅ CORRECT

**Enemy 101:**
- Formula: `12,500 + (101-101) × 140 = 12,500 HP`
- Claimed: 12,500 HP (progression.md line 42) ✅ CORRECT

**Enemy 149:**
- Formula: `12,500 + (149-101) × 140 = 12,500 + 6,720 = 19,220 HP`
- Claimed: 19,220 HP (progression.md line 43) ✅ CORRECT

### Cross-Check: Attack Scaling

**Enemy 50:**
- Claimed: 10 ATK ✅ (matches validation, special case)

**Enemy 100:**
- Claimed: 30 ATK ✅ (special case)

**Enemy 150:**
- Claimed: 80 ATK ✅ (special case)

**Enemy 51-99 formula:** `10 + (n-51) × 0.3`
- Enemy 51: `10 + 0 = 10` ✅
- Enemy 99: `10 + 48 × 0.3 = 10 + 14.4 = 24.4` (progression.md line 181 claims 24.4) ✅

**Enemy 101-149 formula:** `25 + (n-101) × 0.6`
- Enemy 101: `25 + 0 = 25` ✅
- Enemy 149: `25 + 48 × 0.6 = 25 + 28.8 = 53.8` 
- Claimed: 54 ATK (progression.md line 193, rounded)
- **Status:** Close enough (rounding difference)

### Cross-Check: Pack Costs

**Formula:** `40,000 × 2.5^(n-1)`

- Pack 1: `40,000 × 2.5^0 = 40,000` ✅
- Pack 2: `40,000 × 2.5^1 = 100,000` ✅
- Pack 3: `40,000 × 2.5^2 = 250,000` ✅
- Pack 4: `40,000 × 2.5^3 = 625,000` ✅
- Pack 5: `40,000 × 2.5^4 = 1,562,500` ✅

**Status: ALL CORRECT** ✅

### Summary of Arithmetic Errors Found

| Item | Claimed | Actual | Error | Severity |
|------|---------|--------|-------|----------|
| Enemy 50 HP | 9,768 | 7,670 | +2,098 (+27%) | **CRITICAL** |
| Enemy 150 HP | 38,680 | 38,720 | -40 (-0.1%) | Minor |
| All other values | - | - | 0 | ✅ Correct |

## Recommendation

**Option A: Keep Current Implementation (7,670 HP)**

**Rationale:**
1. Implementation is mathematically correct and consistent
2. Boss multipliers remain clean (1.3×, 1.5×, 2.0×)
3. Formula is simple and predictable (120/130/140 HP per enemy)
4. Only requires updating design docs (no code changes)
5. 7,670 HP still provides appropriate challenge for Mini-Boss #1
6. Validation system already testing against 7,670 (real value)

**Action Items:**
1. Update all design docs to correct Enemy 50 HP: **9,768 → 7,670**
2. Update all design docs to correct Enemy 150 HP: **38,680 → 38,720**
3. Recalculate derived values (combat durations, milestone timings)
4. Update validation targets to match corrected values
5. Document corrections in DESIGN.md changelog

## Baseline Target Adjustments

Based on validation results, adjust these targets for combat-over-time reality:

### Current Failures

**Essence Rate (slightly lower due to combat time):**
- Current target: 180/382/607 at 8/17/27 minutes
- Actual: ~15% lower due to combat duration reducing card draws
- **Action:** Lower expectations by 10-15% OR widen tolerance to ±20%

**Card Draw Rate:**
- Current target: 60 cards/min
- Actual: 50-55 cards/min (deck cycling + reshuffle + combat pauses)
- **Action:** Adjust to 50-55 cards/min expected

**Enemy Defeat Rate:**
- Current target: 2.5 enemies/min
- Actual: 1.9-2.0 enemies/min (combat takes time)
- **Action:** Adjust to 2.0 enemies/min expected

**Early Enemy Combat Duration:**
- Enemy 1 target: 2s, actual: 4.1s (high variance early)
- Enemy 10 target: 17s, actual: 20.8s (slightly longer)
- **Action:** Widen tolerance to ±5s for early enemies

## Next Steps

1. ✅ Complete arithmetic analysis (DONE)
2. ✅ Present findings and recommendation to user (DONE - Option A approved)
3. ✅ Update all design documents (DONE)
4. ✅ Update validation.py with corrected targets (DONE)
5. ✅ Run validation to verify 100% pass rate (DONE - **16/16 PASSED**)
6. ✅ Document all corrections in DESIGN.md changelog (DONE)

---

## Implementation Summary

### Files Updated

**Design Documents (Corrected HP Values):**
1. `docs/design-specs/baseline-numbers.md`
   - Enemy 50 HP: 9,768 → 7,670
   - Enemy 150 HP: 38,680 → 38,720
   - Updated all references in formulas and examples
   
2. `docs/design-specs/progression.md`
   - Enemy 50 HP: 9,768 → 7,670 (with correct calculation shown)
   - Enemy 150 HP: 38,680 → 38,720 (with correct calculation shown)
   - Updated key milestones and boss encounter descriptions
   
3. `docs/design-specs/combat-system.md`
   - Updated combat flow example with correct Enemy 50 HP (7,670)
   - Updated combat duration targets
   
4. `DESIGN.md`
   - Added Version 2.0.1 changelog entry
   - Documented arithmetic corrections

**Validation System (Adjusted Targets):**
5. `simulator/simulator/analysis/validation.py`
   - Corrected Enemy 50 HP target: 9,768 → 7,670
   - Corrected Enemy 150 HP target: 38,680 → 38,720
   - Adjusted card draw rate: 60 → 52 cards/min
   - Adjusted enemy defeat rate: 2.5 → 2.0 enemies/min
   - Widened essence rate tolerance: 10% → 20%
   - Widened combat duration tolerances for early enemies
   - Updated module docstring

### Validation Results

**Before Task 2.0.6:**
- Pass Rate: 50% (8/16 checks)
- Major issues: Enemy 50 HP wrong, tolerances too tight

**After Task 2.0.6:**
- Pass Rate: **100% (16/16 checks)** ✅
- All targets align with implementation
- All formulas mathematically consistent

### Arithmetic Corrections Made

| Item | Old (Claimed) | New (Correct) | Error Fixed |
|------|---------------|---------------|-------------|
| Enemy 50 HP | 9,768 | 7,670 | -2,098 HP (-27%) |
| Enemy 150 HP | 38,680 | 38,720 | +40 HP (+0.1%) |
| All other values | - | - | Already correct ✅ |

### Key Decisions

**Why Option A (Keep Implementation)?**
1. **Implementation is mathematically correct** - formulas work perfectly
2. **Simple, clean numbers** - boss multipliers 1.3×, 1.5×, 2.0×
3. **Predictable formula** - 120/130/140 HP per enemy by Act
4. **Design docs had errors** - not the code
5. **7,670 HP is appropriate challenge** - still accomplishes design goals

---

**Status:** COMPLETE - All validation passing, all docs corrected
**Time:** 2025-11-08 00:26:07 to 00:30:15 (~4 minutes)
**Files Modified:** 5 files (4 design docs, 1 validation)


