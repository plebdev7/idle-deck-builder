# Session 2.0.5 Findings: Design Document Inconsistencies

**Date:** 2025-11-07 23:52:04  
**Discovered During:** Validation system testing

## Critical Finding: Boss HP Arithmetic Error

### The Issue

**DESIGN.md Claims:**
- Enemy HP formula: `HP = 20 + (n-1) × 120` for Act 1
- Enemy 50 Boss HP: 9,768 HP with 1.3× multiplier

**Reality:**
- Implementation correctly follows: `base = 20 + 49 × 120 = 5,900`
- With 1.3× multiplier: `5,900 × 1.3 = 7,670 HP` ✓
- **THESE VALUES ARE MUTUALLY INCOMPATIBLE**

### The Math

To get 9,768 HP with 1.3× multiplier:
- Required base: `9,768 ÷ 1.3 = 7,513.85 HP`
- Required formula: `20 + 49 × 153 = 7,517 HP`
- **But DESIGN.md says 120 HP/enemy, not 153**

### Possible Origins

This likely stems from the Session 2.0.3 balance redesign when we moved from:
- **OLD:** Linear `20 + (n-1) × 65.8` → Enemy 50: 3,244 HP
- **NEW:** Act-based `20 + (n-1) × 120` → Enemy 50: 5,900 HP

Someone may have:
1. Calculated 9,768 HP for a different formula
2. Applied it to the wrong formula
3. Didn't verify the arithmetic

## Additional Concerns

### Likely Issues to Investigate

Based on this finding, Task 2.0.6 should check:

1. **Enemy 100 Boss HP:**
   - Claimed: 18,555 HP with 1.5× multiplier
   - Formula: `base = 6,000 + 49 × 130 = 12,370`
   - With 1.5×: `12,370 × 1.5 = 18,555 HP` ✓ **CORRECT**

2. **Enemy 150 Boss HP:**
   - Claimed: 38,680 HP with 2.0× multiplier
   - Formula: `base = 12,500 + 49 × 140 = 19,360`
   - With 2.0×: `19,360 × 2.0 = 38,720 HP`
   - **DISCREPANCY: Off by 40 HP** (19,340 × 2.0 = 38,680)

3. **Attack Scaling:**
   - Need to verify all attack progression claims
   - Check boss attack multipliers

4. **Combat Duration Claims:**
   - DESIGN.md: "Enemy 50 at ~23 min"
   - Validation: 23.15 min ✓ **CORRECT**
   - Other milestones may need checking

5. **Essence Rate Progression:**
   - DESIGN.md claims: 180 → 382 → 607 Essence/sec
   - Validation shows: 153 → 334 → 516 Essence/sec
   - ~15% lower due to combat time (expected)

## Implications

### For Task 2.0.6

**Must Do:**
1. Full arithmetic audit of DESIGN.md
2. Verify every formula produces claimed values
3. Check all three boss encounters
4. Validate milestone timings
5. Update all inconsistent values

**Decide:**
- Accept lower baseline values (combat takes time now)?
- Adjust formulas to match claims?
- Update claims to match formulas?

### For Task 2.1+ (Pack Design)

Cannot design cards without accurate baseline:
- Need correct enemy HP values for power scaling
- Need correct combat durations for pacing
- Need correct essence rates for economy

**Block:** Task 2.1 blocked until 2.0.6 completes

## Resolution Strategy

### Recommended Approach

1. **Phase 1: Find All Errors** (30-60 min)
   - Systematic review of DESIGN.md formulas
   - Calculate vs claimed values for all key numbers
   - Document all discrepancies

2. **Phase 2: Decide Fixes** (15-30 min)
   - For each discrepancy, choose: fix formula or fix claim
   - Prefer minimal code changes where possible
   - Maintain design intent where clear

3. **Phase 3: Implement** (30-60 min)
   - Update combat.py formulas if needed
   - Update DESIGN.md values if needed
   - Update validation.py targets
   - Re-run validation to 100%

4. **Phase 4: Document** (15-30 min)
   - Comprehensive DESIGN.md changelog
   - Mark superseded values
   - Document rationale for all changes

**Total Estimated Time:** 2-3 hours

## Validation Pass Rate Impact

**Current:** 50% (8/16 checks)

**After 2.0.6 (Expected):**
- Fix boss HP: +2 checks (Enemy 50 HP + possibly others)
- Adjust baselines: +6 checks (essence rates, card draw, enemy defeat, combat durations)
- **Target:** 100% (16/16 checks) ✓

## Lessons Learned

1. **Always validate arithmetic** in design documents
2. **Cross-check formulas** against claimed examples
3. **Test-driven design** catches errors early
4. **Validation systems are valuable** - caught a real bug!

---

**Status:** Documented - Ready for Task 2.0.6

