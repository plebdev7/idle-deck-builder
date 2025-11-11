# Task 2.1.4 - Research Conditional Mechanics

**Task Reference:** CHECKLIST.md Task 2.1.4  
**Start Time:** 2025-11-10 23:01:54  
**Completion Time:** 2025-11-10 23:15:00  
**Status:** ✅ COMPLETE

---

## Objective

Research and define conditional mechanics for card design. Establish the foundational "levers" for card design space beyond flat stats, including condition types, balancing framework, ability templates, and UI tracking requirements.

---

## Context & Background Assessment

### Pre-Task State
- Starter deck complete with 8 flat-value cards (Session 1.3C)
- Card rarity system defined (Session 2.1.1)
- Stat point balancing system established (Session 2.1.2)
- Card leveling system designed (Session 2.1.3)
- Pack 1-3 progression framework outlined in CHECKLIST
- cards-schema.json has placeholder condition types but no specification

### Design Constraints Clarified
**User Clarifications:**
1. **No "in play" concept** - Cards are drawn, trigger, discard immediately
2. **No meta-progression conditions** - No boss-specific, enemy count, or death loop tracking
3. **Reshuffle cycles > time/ticks** - Better game feel for timing conditions
4. **Single conditions primary** - AND/OR only for intuitive pairs
5. **Complex tracking OK if visible** - Show last 3 cards with summary blocks
6. **Condition coefficient per-card tuning** - Flexible balancing, not rigid formulas
7. **Negative effects are fine** - Future design space

---

## Work Performed

### 1. Created Conditional Mechanics Specification
**File:** `docs/design-specs/conditional-mechanics.md`

**Content Sections:**
- Overview and core principles
- Four condition type categories:
  - **TIMING:** Cycle position, reshuffle count, HP-based phases
  - **CARD_COUNT:** Cards drawn (combat/cycle/deck), tier/type counting
  - **STATE:** Resource state, stat relationships, HP comparisons
  - **SEQUENCE:** Previous card, last N cards, counting chains
- Pack 1-3 progression framework with complexity rules
- Example cards for each pack tier
- Condition coefficient balancing system (0.01-1.0 scale)
- Coefficient guidelines by trigger probability
- Per-card tuning process
- Negative condition coefficients
- Ability text templates (7 template types)
- Writing guidelines for card text
- Combat UI tracking requirements (detailed)

**Design Decisions:**
- Avoided boss-specific and meta-progression conditions (user feedback)
- Emphasized reshuffle-based timing over seconds/ticks (better game feel)
- Clear distinction between "this combat", "this cycle", and "in deck" tracking
- Pack 1: Simple, visible state only (binary bonuses)
- Pack 2: Moderate complexity with sequence tracking (scaling allowed)
- Pack 3: Full complexity with AND/OR, negative conditions, retroactive effects

---

### 2. Updated Visual Style Guide
**File:** `docs/visual-style-guide.md`

**Added Combat UI Specification Section:**
- 5 required tracking elements with full visual specs:
  1. Reshuffle counter (cycle tracking)
  2. Cards drawn this cycle (tier/type breakdown)
  3. Last 3 cards drawn (sequence history)
  4. Cards drawn this combat (cumulative totals)
  5. Current game state panel (HP, stats, rate)
- Visual priority and responsive behavior (Desktop/Tablet/Mobile)
- Condition trigger feedback animations
- Animation specifications (slideLeft, pulse, highlight)
- Accessibility considerations (screen reader, keyboard, color independence)
- Implementation notes (performance, state management, testing)

**Design Decisions:**
- Last 3 cards always visible (desktop) or expandable (mobile)
- Reshuffle counter prominent (top-right recommended)
- HP percentage color coding (green > yellow > orange > red)
- All animations < 200ms (non-blocking)
- Card history slides left with fade animation (150ms)

---

### 3. Updated Card System Documentation
**File:** `docs/design-specs/card-system.md`

**Changes:**
- Added "Conditional Abilities (Session 2.1.4 - COMPLETE)" section
- Listed all four condition types with examples
- Referenced full specification in conditional-mechanics.md
- Marked trigger chains and combo requirements as "To be designed in Task 2.1.5"

---

### 4. Updated Checklist
**File:** `CHECKLIST.md`

**Changes:**
- Marked Task 2.1.4 as ✅ COMPLETE (2025-11-10)
- Checked off all sub-tasks
- Added completion notes:
  - Create condition coefficient balancing system
  - Define combat UI tracking requirements

---

## Design Decisions Made

### Condition Type Framework
**Decision:** Four categories - Timing, Card_Count, State, Sequence

**Rationale:**
- Covers all trackable game mechanics
- Clear boundaries between categories
- Each category has distinct UI requirements
- Enables progressive complexity (Pack 1 → 3)

---

### Tracking Clarity
**Decision:** Explicit time windows - "this combat" vs "this cycle" vs "in deck"

**Rationale:**
- Cards don't stay "in play" (immediate discard)
- Players need clear understanding of tracking scope
- Prevents "feels bad" confusion about why conditions didn't trigger
- Aligns with combat system (cycle-based draw pattern)

---

### Pack Progression Complexity
**Decision:** Pack 1 simple (visible only), Pack 2 moderate (sequence), Pack 3 full (AND/OR)

**Rationale:**
- Teaches conditions gradually
- Pack 1 requires no memory burden (all visible state)
- Pack 2 introduces last 1-2 card tracking (manageable)
- Pack 3 unlocks full design space (high-skill players)
- Prevents overwhelming new players

---

### Condition Coefficient System
**Decision:** Flexible per-card tuning with guidelines, not rigid formulas

**Rationale:**
- Different deck archetypes trigger conditions at different rates
- Design space needs flexibility for interesting cards
- Guidelines provide starting points
- Playtesting will refine actual values
- Simulator can track actual trigger rates

**Coefficient Ranges:**
- 0.8-1.0: Always/almost always (avoid these)
- 0.5-0.7: Often true (Pack 1 teaching)
- 0.3-0.5: Sometimes true (Pack 1-2 build-around)
- 0.1-0.3: Rarely true (Pack 2-3 high-reward)
- 0.01-0.1: Very rarely true (Pack 3 legendary edge cases)

---

### Combat UI Requirements
**Decision:** Last 3 cards visible, reshuffle counter always shown, expandable detail panels

**Rationale:**
- Last 3 cards enables all sequence conditions
- Reshuffle counter critical for timing conditions
- Expandable panels reduce visual clutter while maintaining access
- Mobile: Icon-only with tap-to-expand (performance + screen space)
- All condition-relevant state visible or accessible in 1 tap

---

### Negative Conditions
**Decision:** Allow negative conditions in Pack 2+, reduce base cost with negative coefficient

**Rationale:**
- Creates interesting deck-building constraints
- High-risk/high-reward gameplay moments
- Must be avoidable with deck construction (not pure RNG)
- Clear feedback when drawback triggers
- Expands design space significantly

---

## Files Created/Modified

**Created:**
- `docs/design-specs/conditional-mechanics.md` (complete specification, 550+ lines)
- `.cursor/log/sessions/session-2-1-4-conditional-mechanics.md` (this file)

**Modified:**
- `docs/visual-style-guide.md` (added Combat UI Specification section)
- `docs/design-specs/card-system.md` (added conditional abilities section, references)
- `CHECKLIST.md` (marked Task 2.1.4 complete)

---

## Validation Performed

### Specification Completeness
- [x] All four condition types defined with examples
- [x] Pack 1-3 progression with complexity rules
- [x] Example cards for each pack tier
- [x] Condition coefficient system with guidelines
- [x] Ability text templates for all patterns
- [x] Combat UI tracking requirements with mockups
- [x] Responsive design considerations (Desktop/Tablet/Mobile)

### Design Constraints Met
- [x] No "in play" tracking (clarified as "drawn this combat/cycle")
- [x] No boss-specific or meta-progression conditions
- [x] Reshuffle-based timing preferred over seconds/ticks
- [x] Last 3 cards visible for sequence tracking
- [x] Coefficient system allows per-card tuning
- [x] Negative conditions supported

### Documentation Quality
- [x] Cross-references between documents
- [x] Clear section organization
- [x] Examples for all concepts
- [x] Visual mockups for UI elements
- [x] Animation specifications (CSS)
- [x] Accessibility considerations

---

## Outstanding Questions

None. All design questions from Task 2.1.4 checklist resolved.

---

## Next Steps

**Immediate:**
1. Task 2.1.5: Research sequencing & order-dependent mechanics (likely skip - covered in 2.1.4)
2. Task 2.1.6: Create card data structure & text format (ready to proceed)

**Future:**
1. Task 2.1.7-2.1.9: Design Pack 1-3 cards using conditional framework
2. Implementation: Add conditional logic to simulator
3. UI Implementation: Build combat tracking elements

---

## User Feedback

**User approval:** "Check back to 2.1.4, I think we've done a pretty good job here."

**Confirmed complete:** User directed to move to documentation (coefficient table, ability templates, visual tracking).

---

## Notes

**Condition Coefficient System:**
The coefficient system is a flexible balancing tool, not a rigid formula. Each card will need individual tuning based on:
1. Intended deck archetype (mono-tier vs multi-tier, generator-heavy vs combat-focused)
2. Condition complexity (simple state vs complex sequence)
3. Risk/reward balance (safe conditions vs edge-case clutch moments)
4. Playtesting feedback (simulator can track actual trigger rates)

**Sequencing Mechanics:**
Task 2.1.5 (sequencing & order-dependent) appears largely covered by Task 2.1.4. Sequence conditions (previous card, last N cards) are fully specified. May be able to skip or merge with 2.1.6.

**Combat UI Implementation:**
Visual tracking requirements are comprehensive but will need iterative refinement during implementation. Key priorities:
1. Reshuffle counter (critical for timing)
2. Last 3 cards (critical for sequence)
3. Current state panel (critical for state conditions)
4. Expandable detail panels (nice-to-have, can defer)

---

**Log Status:** Complete  
**Task Status:** ✅ COMPLETE (2025-11-10)  
**Ready for:** Task 2.1.6 or skip to Task 2.1.7 (Pack 1 card design)

