# Task 2.1.5 - Research Sequencing & Order-Dependent Mechanics

**Task Reference:** CHECKLIST.md Task 2.1.5  
**Start Time:** 2025-11-12 22:30:00  
**Completion Time:** 2025-11-12 22:35:00  
**Status:** ✅ COMPLETE

---

## Objective

Research and document sequencing and order-dependent mechanics for card design, including "next card" and "previous card" tracking, combo trigger chains, and state persistence rules.

---

## Context & Background Assessment

### Pre-Task State
- Task 2.1.4 completed (conditional mechanics framework)
- Sequence conditions already documented in conditional-mechanics.md
- "Previous card" and "last N cards" tracking already specified
- Combo trigger chains already documented with Pack 1-3 progression
- State persistence rules scattered across multiple documents

### User Request
User asked to review 2.1.4 work to verify if 2.1.5 was already complete. Assessment found:
- ✅ "Next card" and "previous card" tracking: **100% complete** in conditional-mechanics.md
- ✅ Combo trigger chains: **100% complete** with Pack 1-3 progression
- ⚠️ State persistence rules: **95% complete**, but scattered across documents

**Decision:** User chose Option B - consolidate state persistence rules into single reference section in conditional-mechanics.md with cross-references.

---

## Work Performed

### 1. Added State Persistence Rules Section
**File:** `docs/design-specs/conditional-mechanics.md`

**New Section Added (lines 641-719):**
- "State Persistence Rules" comprehensive section
- Three subsections: On Reshuffle, On New Enemy, On Death
- Each subsection documents:
  - What resets
  - What persists
  - Design implications for card designers
- Cross-document references to combat-system.md, resource-economy.md, progression.md

**Design Decisions:**
- Organized by trigger event (reshuffle, enemy, death) for clarity
- Emphasized design implications to guide card designers
- Explicit about what counters reset vs persist
- Clear that meta-progression conditions (enemy count, death count) are intentionally avoided

---

### 2. Added Cross-Reference in Combat System
**File:** `docs/design-specs/combat-system.md`

**Change:** Added reference note after "Respawn Mechanics" section (line 261):
```markdown
**For complete state persistence rules (reshuffle, enemy, death), see:** 
[conditional-mechanics.md - State Persistence Rules](conditional-mechanics.md#state-persistence-rules)
```

**Rationale:**
- Prevents duplication of persistence rules
- Points combat system readers to consolidated reference
- Maintains single source of truth for state persistence

---

### 3. Updated Document History
**File:** `docs/design-specs/conditional-mechanics.md`

**Changes:**
- Added Version 1.1 (2025-11-12) changelog entry
- Updated "Next Steps" to point to Task 2.1.6
- Documented state persistence consolidation work

---

### 4. Updated Checklist
**File:** `CHECKLIST.md`

**Changes:**
- Marked Task 2.1.5 as ✅ COMPLETE (2025-11-12)
- Checked off all three sub-tasks:
  - Design "next card" and "previous card" tracking
  - Specify combo trigger chains
  - Define state persistence rules

---

## Design Decisions Made

### State Persistence Organization
**Decision:** Consolidate all persistence rules in conditional-mechanics.md

**Rationale:**
- Card designers are primary audience for persistence rules
- Conditional card design depends heavily on understanding reset timing
- Single reference section easier to maintain than scattered documentation
- Cross-references prevent navigation confusion

---

### Persistence Categories
**Decision:** Three categories - Reshuffle, Enemy, Death

**Rationale:**
- These are the three distinct reset triggers in the game
- Each has different implications for card design
- Clear boundaries between short-term (reshuffle), medium-term (enemy), and long-term (death) state

---

### Design Implications Focus
**Decision:** Include "Design Implications" subsection for each persistence category

**Rationale:**
- Helps card designers understand WHY persistence matters
- Guides strategic card design ("this cycle" vs "this combat" conditions)
- Highlights intentional design decisions (no meta-progression conditions)
- Connects mechanics to player experience

---

## Files Created/Modified

**Created:**
- `.cursor/log/sessions/session-2-1-5-sequencing-mechanics.md` (this file)

**Modified:**
- `docs/design-specs/conditional-mechanics.md` (added State Persistence Rules section)
- `docs/design-specs/combat-system.md` (added cross-reference)
- `CHECKLIST.md` (marked Task 2.1.5 complete)

---

## Validation Performed

### Completeness Check
- [x] "Next card" and "previous card" tracking documented
- [x] Combo trigger chains specified (Pack 1-3 progression)
- [x] State persistence rules consolidated
- [x] Cross-references added between documents
- [x] Design implications documented

### Documentation Quality
- [x] Clear organization by trigger event
- [x] Comprehensive lists of what resets/persists
- [x] Design implications for each category
- [x] Cross-document references maintain navigation
- [x] Single source of truth established

### Task Requirements Met
- [x] All CHECKLIST.md sub-tasks addressed
- [x] Sequencing mechanics fully documented (from 2.1.4)
- [x] Order-dependent mechanics fully specified (from 2.1.4)
- [x] State persistence rules consolidated (2.1.5)

---

## Assessment Summary

**Task 2.1.5 Completion:**
- 95% of work was completed in Task 2.1.4 (sequencing, combo chains)
- 5% of work done in Task 2.1.5 (consolidate persistence rules)
- All three checklist requirements met

**Key Insight:**
The original task breakdown anticipated more work for sequencing mechanics, but the comprehensive conditional mechanics framework in Task 2.1.4 already covered sequence tracking and combo chains thoroughly. Task 2.1.5 primarily added documentation consolidation for card designers.

---

## Outstanding Questions

None. All sequencing mechanics and state persistence rules are fully documented.

---

## Next Steps

**Immediate:**
1. Task 2.1.6: Create card data structure & text format
   - Define complete card template (all fields)
   - Specify stat notation format
   - Create ability description templates with keywords
   - Validate text fits card layout (3 lines max, 12px font)

**Future:**
1. Task 2.1.7-2.1.9: Design Pack 1-3 cards using frameworks from 2.1.1-2.1.5
2. Implementation: Add sequence tracking to simulator
3. UI Implementation: Build last 3 cards history display

---

## Notes

**Efficient Task Completion:**
This task demonstrates the value of comprehensive design work. Task 2.1.4's thorough conditional mechanics specification meant Task 2.1.5 was mostly verification and documentation consolidation rather than new design work.

**Documentation Consolidation Value:**
The consolidated State Persistence Rules section provides card designers with a single reference for all reset timing. This will be invaluable during Pack 1-3 card design phases (Tasks 2.1.7-2.1.9).

**Sequence Tracking Coverage:**
All sequence-dependent mechanics are fully specified:
- Previous card tracking (1 card lookback)
- Last N cards tracking (up to 3 cards)
- Counting chains ("For each X, +Y")
- Reshuffle triggers
- Visual UI requirements (last 3 cards always visible)

---

**Log Status:** Complete  
**Task Status:** ✅ COMPLETE (2025-11-12)  
**Ready for:** Task 2.1.6 (Card Data Structure & Text Format)

