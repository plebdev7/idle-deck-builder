# Design Document Synchronization: Task 2.0 Results

**Date:** 2025-11-07 13:07:56  
**Reason:** Update DESIGN.md to reflect Task 2.0 simulator findings and add combat progression design session

---

## Context

Task 2.0 (Gameplay Simulator) revealed several design issues:
1. Original exponential enemy scaling formula produces unworkable numbers
2. Baseline numbers from Session 1.3B were theoretical, not validated
3. Distinction between "bad player" (no packs) and "good player" (optimal play) not clear
4. Combat progression beyond first 30 minutes not designed

User clarified the pivot:
- Originally intended to design Pack 1-3 cards before Session 2
- Realized numbers couldn't be evaluated without simulator
- Pivoted during Session 1.3 to: starter cards → simulator (Task 2.0) → pack cards (Task 2.1)
- Both "bad player" and "good player" baselines are valuable

---

## DESIGN.md Updates (Version 1.7)

### Fixed Errors
1. **Starter deck attack total:** 72 → 62 (correct arithmetic)
2. **Enemy scaling formula:** Marked as "needs design review"
3. **Pack timing/essence rates:** Replaced theoretical with actual Task 2.0 results
4. **Validation status:** Distinguished validated vs needs-design

### Added Clarity
1. **"Validated Pacing" section:** Now explicitly "Starter Deck Only - Bad Player Baseline"
2. **What's validated:** Simulator confirms core mechanics work
3. **What needs design:** Combat progression, boss encounters, "good player" targets
4. **Status markers:** Clear indicators of temporary vs finalized design decisions

### Design Document Changes
- Line 1133: Attack total corrected (62 not 72)
- Lines 998-1010: Enemy scaling marked as needing design review
- Lines 1052-1071: Replaced with actual validated results + needs-design list
- Lines 1266-1268: Updated version and status
- Lines 1192-1199: Added changelog entry

---

## ROADMAP.md Updates

### Added Task 2.0.1: Combat Progression Design

**Type:** Design session (not implementation)

**Purpose:** Resolve combat scaling questions before designing Pack 1-3 cards

**Key Questions:**
1. Enemy health scaling formula (linear? exponential? hybrid?)
2. Boss encounter design (tutorial death concept? frequency? mechanics?)
3. "Good player" progression targets (what should Pack 1-3 cards achieve?)
4. Long-term progression (beyond 30 min, pre/post prestige)
5. Pack timing balance (bad player baseline vs good player targets)

**Why Before Task 2.1:**
- Pack card design needs clear targets to hit
- Can't design "good player" cards without defining "good player" progression
- Combat scaling affects card power level requirements

**Deliverables:**
- Combat scaling formula specification with rationale
- Boss encounter design document
- "Good player" progression targets
- Updated DESIGN.md with finalized combat system
- Validation targets for pack card design

---

## CHECKLIST.md Updates

### Task 2.0 Marked Complete
- Changed status from pending to complete
- Updated subtask descriptions to reflect actual work done
- Noted validation is "bad player baseline" not full intended experience

### Task 2.0.1 Added
- New design session task between 2.0 and 2.1
- 5 subtasks covering combat progression design questions
- Blocks Task 2.1 (can't design pack cards without progression targets)

---

## Current State Summary

**Validated (Task 2.0):**
- ✓ Core mechanics work (card draw, generators, combat)
- ✓ Starter deck balance confirmed
- ✓ "Bad player" baseline established (7, 11.5, 18.5 min pack timing)
- ✓ Simulation tools ready for testing pack card designs

**Needs Design (Task 2.0.1):**
- Enemy scaling formula
- Boss encounter system
- "Good player" progression targets
- Long-term combat progression
- Final pack timing/essence rate targets

**Ready for Implementation (after 2.0.1):**
- Task 2.1: Pack card design (with clear targets from 2.0.1)
- Task 2.2+: Card interactions, patterns, specifications

---

## Design Process Clarification

**Session 1 Pivot:**
- Original plan: Session 1 → design packs → Session 2
- Problem: Can't evaluate numbers without simulator
- Solution: Session 1 → design starter cards → Task 2.0 (simulator) → Task 2.0.1 (design session) → Task 2.1 (pack cards)

**Why This Works:**
1. Starter cards + simulator validates core mechanics
2. Simulator provides data for design decisions
3. Design session (2.0.1) uses simulator data to finalize progression
4. Pack card design (2.1) has clear targets and can test in simulator

**Both Baselines Valuable:**
- "Bad player" baseline: Minimum viable progression (do nothing)
- "Good player" baseline: Intended experience (buy packs, optimize)
- Testing range: Game must work for both extremes

---

## Next Steps

### Immediate
User decides when to tackle Task 2.0.1 (combat progression design)

### After Task 2.0.1
- Clear "good player" targets established
- Pack card design (Task 2.1) can proceed with concrete goals
- Simulator can validate both "bad" and "good" player progressions

---

**Status:** DESIGN.md synchronized with Task 2.0 results  
**New Task:** 2.0.1 added to ROADMAP and CHECKLIST  
**Ready For:** User decision on Task 2.0.1 timing

