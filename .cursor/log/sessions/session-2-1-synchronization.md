# Task 2.1: Design Document Synchronization

**Session:** 2.1 - Design/Implementation Synchronization  
**Date:** 2025-11-09  
**Status:** ✅ COMPLETE  
**Related:** CHECKLIST.md Task 2.1, ROADMAP.md Session 2.1

---

## Session Goal

Synchronize primary design documents (DESIGN.md, spec files) and simulator implementation with design decisions made in Sessions 2.1.1, 2.1.2A, and 2.1.2B.

**Critical Problem Identified:** Agents consistently confused by:
1. Stale enemy attack information (mix of "Enemy 20 first attack" and "all enemies attack from tick 0")
2. **Misunderstanding of continuous deck cycling** - agents think deck draws once and stops, missing that stats accumulate indefinitely through repeated cycles

---

## User Decisions Confirmed

### Decision 1: All Enemies Attack from Tick 0
**Chosen:** Session 2.1.2B per-tick scaling system  
**Rejected:** Session 2.1.2A "Enemy 20 first attack" approach

**Rationale:**
- No "safe tutorial" - death has no penalty, players learn by dying
- Per-tick scaling counters player deck cycling (prevents "default invulnerability")
- Creates build diversity (glass cannon vs tank vs balanced)

### Decision 2: Keep Original Stat Budget Ranges
**Chosen:** Common 20-30, Rare 30-50, Epic 50-90, Legendary 90-180  
**Rejected:** Adjusted ranges (Common 30-40) from Session 2.1.2B

**Rationale:**
- Original ranges are adequate for per-tick combat
- Can adjust individual cards as needed during Pack 1 design
- Cleaner starting point

---

## Files Updated

### Primary Documents

**1. DESIGN.md (Version 2.0.1 → 2.0.2)**
- ✅ Replaced enemy attack section with per-tick scaling formulas
- ✅ Updated boss ATK descriptions (6.9/14.84/26.76 ATK/tick)
- ✅ Fixed starter deck stats (Essence Burst 250, Mystic Shield 20)
- ✅ **Added prominent deck cycling clarification** - stats accumulate through repeated cycles
- ✅ Updated first 30 minutes milestones (combat starts immediately at tick 0)
- ✅ Added design rationale for per-tick scaling
- ✅ Updated document version history

**Changes:**
```
Lines 156-183: Per-tick enemy scaling system
Lines 73-77: Continuous deck cycling clarification (CRITICAL)
Lines 104-107: Deck cycling mechanics emphasized
Lines 228-241: Starter deck stats corrected
Lines 313-320: First 30 minutes milestones updated
Lines 467-509: Version history (2.0.2 added)
```

**2. docs/design-specs/first-30-minutes.md (Version 1.0 → 1.1)**
- ✅ Updated defense mechanics (all enemies attack from tick 0)
- ✅ Added continuous deck cycling clarifications
- ✅ Updated combat description (tick-by-tick, not instant)
- ✅ Updated player understanding section (continuous cycling emphasis)
- ✅ Changed design rationale (death is part of core loop)

**3. docs/design-specs/baseline-numbers.md**
- ✅ Replaced static attack scaling with per-tick formulas
- ✅ Added Act 1/2/3 per-tick rate formulas
- ✅ Added boss 2× multiplier documentation

**4. docs/design-specs/progression.md**
- ✅ Already updated in Session 2.1.2B (no changes needed)

**5. docs/design-specs/combat-system.md**
- ✅ Already has continuous cycling documentation (no changes needed)

### Simulator Implementation

**6. simulator/simulator/core/combat.py**

**Major Changes:**
- ✅ `Enemy` class restructured for per-tick scaling:
  - Added `atk_per_tick`, `def_per_tick`, `is_boss`, `combat_ticks_elapsed` fields
  - Removed static `attack` and `defense` fields
  - Added `current_attack()` and `current_defense()` methods
  - Added `tick()` method to increment combat tick counter
  - Updated `spawn()` to calculate per-tick rates using Session 2.1.2B formulas

- ✅ `_combat_tick()` updated:
  - Calls `enemy.tick()` at start of each combat tick
  - Uses `enemy.current_attack()` and `enemy.current_defense()` for damage calculation
  - Adds `enemy_attack`, `enemy_defense`, `ticks_elapsed` to combat_tick events

- ✅ `_spawn_enemy()` updated:
  - Records `atk_per_tick`, `def_per_tick`, `is_boss` in enemy_spawn events

- ✅ File header updated:
  - References DESIGN.md Version 2.0.2
  - Documents per-tick scaling system
  - Emphasizes continuous deck cycling

**Per-Tick Formulas Implemented:**
```python
Act 1 (Enemies 1-50):
atk_per_tick = 1.0 + (n-1) * 0.05
def_per_tick = 0.5 + (n-1) * 0.025

Act 2 (Enemies 51-100):
atk_per_tick = 3.5 + (n-51) * 0.08
def_per_tick = 1.75 + (n-51) * 0.04

Act 3 (Enemies 101-150):
atk_per_tick = 7.5 + (n-101) * 0.12
def_per_tick = 3.75 + (n-101) * 0.06

Bosses: All rates × 2.0
```

---

## Validation Results

### Simulator Testing

**Test 1: Basic Functionality**
- ✅ 1-minute simulation completed successfully
- ✅ 6 enemies defeated, 92/100 HP remaining
- ✅ No errors, charts generated

**Test 2: Per-Tick Scaling Verification**
```
Enemy 1:
- HP: 20
- ATK/tick: 1.0 ✅ (expected: 1.0)
- DEF/tick: 0.5 ✅ (expected: 0.5)
- Attacks from tick 0 ✅

Enemy 50 Boss:
- HP: 7,670 ✅ (expected: 7,670)
- ATK/tick: 6.9 ✅ (expected: 3.45 × 2 = 6.9)
- DEF/tick: 3.45 ✅ (expected: 1.73 × 2 = 3.46)
- Boss multiplier working ✅
```

**Test 3: Continuous Cycling**
- ✅ Deck cycles multiple times in 1 minute
- ✅ Stats accumulate properly
- ✅ 52 cards drawn in 60 seconds (deck cycles ~6 times)

---

## Critical Documentation Improvements

### Issue 1: Deck Cycling Misunderstanding

**Problem:** Agents consistently think:
- "Deck draws 8 cards and stops"
- "Stats = 62 ATK, 56 DEF (total)"
- Missing that deck cycles continuously

**Solution:** Added prominent clarifications in multiple locations:

**DESIGN.md line 73-77:**
```markdown
- **Cards drawn continuously (1 card/sec) and deck CYCLES INDEFINITELY**
  - **CRITICAL:** Stats accumulate through repeated deck cycling, not just one draw
  - 8-card deck cycles every 9 seconds (8 draws + 1s reshuffle cooldown)
  - Each cycle adds stats again: Cycle 1 = 62 ATK, Cycle 2 = 124 ATK, Cycle 3 = 186 ATK, etc.
  - This exponential growth is why enemies must scale per-tick
```

**DESIGN.md line 104-107:**
```markdown
**Critical Mechanics:** 
- Generators work **when drawn**, not passively in deck. Deck cycling speed matters!
- **Deck cycles continuously** - stats accumulate through repeated cycles, not just first draw
- Small decks cycle faster (8 cards = 9s/cycle) vs large decks (15 cards = 16s/cycle)
```

**DESIGN.md line 240-241:**
```markdown
**Total Per Cycle:** 62 ATK, 56 DEF, +3 Essence/sec
- **Note:** These stats accumulate with each deck cycle (9 seconds for 8-card deck)
```

### Issue 2: Enemy Attack Timing Confusion

**Problem:** Mixed messages:
- Session 2.1.2A docs: "Enemy 20 first attack"
- Session 2.1.2B docs: "All enemies attack from tick 0"
- DESIGN.md: "Enemies 1-19: 0 ATK"

**Solution:**
- ✅ Removed all references to "Enemy 20 first attack"
- ✅ Removed all references to "safe tutorial"
- ✅ Consistent messaging: "All enemies attack from tick 0"
- ✅ Updated all affected documents

---

## Synchronization Checklist

### Design Documents
- [x] DESIGN.md updated with per-tick scaling
- [x] DESIGN.md starter deck stats corrected
- [x] DESIGN.md deck cycling clarified (CRITICAL)
- [x] first-30-minutes.md updated (attack timing, deck cycling)
- [x] baseline-numbers.md updated (per-tick formulas)
- [x] progression.md verified (already correct from 2.1.2B)
- [x] combat-system.md verified (already has cycling docs)

### Simulator Implementation
- [x] Enemy class restructured for per-tick scaling
- [x] Combat tick method updated
- [x] Spawn method updated
- [x] File header updated
- [x] Tested and validated

### Cross-References
- [x] CHECKLIST.md updated (marked Session 2.1.2B complete)
- [x] ROADMAP.md verified (no updates needed)
- [x] Document version numbers incremented

---

## Remaining Work

### Not Part of This Session (Deferred)
- ❌ Synchronization checklist tool (user requested deferral)
- ❌ Pack 1 card design (Task 2.1.2C)
- ❌ Card leveling system design (Task 2.1.3)

---

## Lessons Learned

### For Future Sessions

**1. Design Decision Conflicts Must Be Resolved Immediately**
- Session 2.1.2A and 2.1.2B made conflicting decisions (Enemy 20 vs all enemies)
- This created confusion for future agents
- **Fix:** Always check for conflicts before marking session complete

**2. Critical Mechanics Need Prominent Documentation**
- Continuous deck cycling is fundamental but was understated
- Agents consistently missed this detail
- **Fix:** Add **CRITICAL** markers and multiple clarifications for foundational mechanics

**3. Implementation Should Follow Immediately**
- Simulator was 2 sessions behind design decisions
- Created "design drift" where docs didn't match reality
- **Fix:** Implement in same session as design approval, or mark as "pending implementation"

**4. Document Synchronization is Not Optional**
- Multiple documents can have conflicting information
- "Hub" documents (DESIGN.md) must stay synchronized with spec files
- **Fix:** Check all related documents when making design changes

---

## Files Changed Summary

### Created
- `.cursor/log/sessions/session-2-1-synchronization.md` (this file)

### Modified
- `DESIGN.md` (lines 73-77, 104-107, 156-183, 185-204, 228-241, 313-320, 467-509)
- `docs/design-specs/first-30-minutes.md` (lines 32-40, 209-216, 246-255, 309-320)
- `docs/design-specs/baseline-numbers.md` (lines 119-139)
- `simulator/simulator/core/combat.py` (major restructure: lines 1-19, 72-234, 478-565)

### Verified (No Changes Needed)
- `docs/design-specs/progression.md` (already correct from 2.1.2B)
- `docs/design-specs/combat-system.md` (already has cycling documentation)
- `game-data/balance-config.json` (already correct from 2.1.2B)

---

## Session Timeline

**Total Time:** ~1.5 hours

- 00:00-00:15: Review session logs and identify issues
- 00:15-00:45: Update DESIGN.md (per-tick scaling, deck cycling, starter stats)
- 00:45-01:00: Update spec files (first-30-minutes, baseline-numbers)
- 01:00-01:15: Implement per-tick scaling in simulator
- 01:15-01:25: Test and validate simulator
- 01:25-01:30: Create session log (this file)

---

**Session Status:** ✅ **COMPLETE**  
**Completion Date:** 2025-11-09 00:30:00  
**Ready for:** Task 2.1.2C - Pack 1+2 Card Design (with correct combat system)


