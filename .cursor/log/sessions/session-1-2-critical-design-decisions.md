# Task Log: Session 1.2 - Critical Design Decisions

**Task Reference:** CHECKLIST.md Task 1.2, ROADMAP.md Session 1  
**Status:** In Progress  
**Started:** 2025-11-04 23:00:20

---

## Task Objectives

Answer 5 critical design questions that are blocking other system designs:
1. Class Switching Cost (Question 1)
2. Arcane Tier Combat Role (Question 4)
3. Arcane Essence Currency Model (Question 5)
4. Deck Size Limits (Question 9)
5. Combat Timing (Question 10)

Document all decisions in DESIGN.md with rationale.

---

## Files Impacted

- **Read:** DESIGN.md, ROADMAP.md, CHECKLIST.md, theme-specification.md, visual-style-guide.md
- **Modified:** DESIGN.md (will update with decisions and remove "Outstanding Design Questions" section)
- **Created:** This log file

---

## Background Assessment

### Current Project State
- Theme established: Elemental Magic Tower Defense
- Visual direction complete: Color palettes, card layouts, icon style defined
- Task 1.1 and 1.1A are complete and approved
- Ready to make critical design decisions that will inform all subsequent design work

### Context for Decisions
- Game is hybrid idle/active deck builder
- Classes are collectible cards, not menu choices
- Tiers unlock linearly but remain active simultaneously
- Lower tiers provide foundational support
- Combat is fully passive (auto-battle)
- Resource generation is deck-building strategy

---

## Log Entries

### 2025-11-04 23:00:20 - Task Initiated

**Actions Taken:**
- Read all relevant design documents
- Identified the 5 outstanding questions
- Created this log file
- Prepared to present questions to user for decision-making

**Next Steps:**
- Present each question with options, pros/cons, and recommendation
- Get user confirmation for each decision
- Document decisions in DESIGN.md
- Update CHECKLIST.md to mark task complete

---

## Decision Log

### Question 1: Class Switching Cost
**Status:** DECIDED - Option C (Only on Prestige)
**Timestamp:** 2025-11-04 23:00:20
**Decision:** Classes can only be switched when performing a prestige reset.
**Rationale:** 
- Makes class choice meaningful for each run
- Natural prestige incentive
- Clearer progression arc per class path
- Aligns with "light roguelike" design philosophy

### Question 4: Arcane Tier Combat Role
**Status:** DECIDED - Option B (Contributes to Colored Decks)
**Timestamp:** 2025-11-04 23:00:20
**Decision:** Arcane cards can be included in elemental tier decks; unified combat system.
**Rationale:**
- Keeps Arcane tier relevant throughout game
- Enables cross-tier synergies
- Simpler than managing multiple separate battles
- Aligns with "Tiers as Foundation" design principle
**User Note:** "Having multiple decks is just going to be confusing"

### Question 5: Arcane Essence Currency Model
**Status:** DECIDED - Option C (Global Upgrade Currency) with Conversion Mechanic
**Timestamp:** 2025-11-04 23:00:20
**Decision:** Arcane Essence used for universal upgrades (card leveling, prestige upgrades, deck size increases). Elemental Essences primarily generated through generator card conversion.
**Rationale:**
- Arcane Essence always valuable throughout game
- Supports "foundational magic" theme
- Creates strategic choices between packs and upgrades
**Important Design Nuance:** Potentially the ONLY way to get elemental essence is through conversion as part of generator cards. This means:
- Elemental generator cards convert Arcane Essence → Elemental Essence
- Direct elemental generation doesn't exist
- Arcane generation becomes foundation of entire economy
**User Note:** "I see there being some conversion via cards being played as well. Potentially the only way to get other elemental essence is by conversion as part of the generation cards"

### Question 9: Deck Size Limits
**Status:** DECIDED - Option A (Fixed Size) with Additional Constraints
**Timestamp:** 2025-11-04 23:00:20
**Decision:** Start with fixed deck size, add multiple constraint types.
**Rationale:**
- Easiest to balance during design phase
- Forces meaningful deck-building choices
- Traditional card game feel
**Additional Complexity (User Request):**
- Limits per element/tier (e.g., max X Fire cards, max Y Arcane cards)
- Individual card copy limits (e.g., max 2-3 copies of same card)
- Multiple constraint layers create deeper deck-building strategy
**User Note:** "I think I'd want to go further to have specific limits per element/tier, counts for individual cards, etc."

### Question 10: Combat Timing
**Status:** DECIDED - Option B (Timed Intervals) with Card Draw Mechanic
**Timestamp:** 2025-11-04 23:00:20
**Decision:** Interval-based combat with continuous card draw charging system.
**Detailed Mechanic (User Design):**
- Cards drawn continuously at fast intervals (charging phase)
- Drawing cards charges up power/defense values
- Enemies arrive on slower intervals (combat phase)
- Attack/defend triggers occur when enemy present
- Combat continues while drawing cards
- Time between enemy arrivals for preparation
**Rationale:**
- Provides feedback and discrete events
- Idle-friendly but engaging
- Card draw adds strategic layer
- Can evolve to wave system (Option C) for bosses/events
**User Note:** "maybe cards are drawn continuously (faster interval than monsters) to 'charge up' power/defense, and then the enemy arrives and attack/defend occur on the interval. attack/defend can then continue to trigger on the monster(s) while drawing cards and giving some time before the next monster arrives"

---

## Validation

- [x] All 5 questions answered
- [x] Decisions documented in DESIGN.md with rationale
- [x] "Outstanding Design Questions" section updated (5 resolved, 5 remain)
- [x] Decisions cross-referenced with affected systems
- [x] User confirmation received for all decisions
- [x] CHECKLIST.md updated

---

---

### 2025-11-04 23:05:00 - Task Complete

**Actions Taken:**
- Updated DESIGN.md with all 5 resolved design decisions
- Added detailed "Resolved Design Decisions" section to DESIGN.md
- Updated Resource Generation System section with conversion mechanic
- Updated Deck Building System section with multi-layer constraints
- Updated Combat System section with card draw mechanics
- Updated Class System section with prestige-only switching
- Removed resolved questions from "Outstanding Design Questions" section
- Added document changelog to DESIGN.md
- Updated document version to 1.2

**Files Modified:**
- DESIGN.md (major updates, version 1.2)
- .cursor/log/sessions/session-1-2-critical-design-decisions.md (this file)

**Validation Status:**
- ✅ All 5 questions answered with user confirmation
- ✅ Decisions documented in DESIGN.md with detailed rationale
- ✅ "Outstanding Design Questions" section updated (5 questions resolved, 5 remaining)
- ✅ Decisions cross-referenced with affected systems
- ✅ User confirmation received for all decisions
- ✅ Implications documented for each decision

**Key Decisions Summary:**
1. **Class Switching:** Prestige-only (meaningful commitment)
2. **Arcane Combat:** Unified deck system (cross-tier building)
3. **Arcane Essence:** Universal currency with conversion mechanic
4. **Deck Size:** Fixed with per-tier and per-card limits
5. **Combat Timing:** Interval-based with continuous card draw

**Next Task:** 1.3 Core Loop Detailed Specification

---

---

### 2025-11-04 23:10:00 - Design Refinement: Class-Specific Deck Limits

**User Insight:** Per-tier deck limits should be determined by class choice, not universal.

**Actions Taken:**
- Updated "Deck Size Constraints" decision with class-specific limit profiles
- Added detailed examples: Fire Apprentice (5/10), Geomancer (6/7/7), Stormlord (5/8/8/8)
- Updated Class Mechanics section with deck limit profile descriptions
- Updated Deck Building System section in main body
- Added future progression mechanics notes (class leveling, tier upgrades)
- Updated document changelog

**Rationale:**
- Creates mechanical differentiation between classes (not just thematic)
- Common classes = specialist (tight limits), Rare+ = balanced (flexible)
- Higher rarity classes have more total deck slots
- Makes class choice strategically meaningful beyond tier access
- Adds prestige incentive (better classes = better deck limits)

**Examples Added:**
- Fire Apprentice: 15 cards (5 Arcane / 10 Fire) - specialist
- Geomancer: 18 cards (6 Arcane / 7 Earth / 7 Fire) - balanced
- Stormlord: 21 cards (5 Arcane / 8 Air / 8 Water / 8 Lightning) - flexible

**Future Considerations (Noted, Not Designed):**
- Class leveling to increase limits
- Tier-specific upgrades
- Prestige bonuses
- Milestone unlocks

**Files Modified:**
- DESIGN.md (Deck Size Constraints, Class Mechanics, Deck Building System sections)
- .cursor/log/sessions/session-1-2-critical-design-decisions.md (this file)

---

---

### 2025-11-04 23:15:00 - Design Note: Order-Dependent Card Effects

**User Insight:** Card draw order must create meaningful variance, otherwise there's no reason to have a draw mechanic at all.

**Discussion Points:**
- If cards just accumulate stats, draw order is irrelevant
- Need order-dependent effects: multipliers, modifiers, "next X cards" effects
- State management: what persists vs resets (enemy defeat, deck reshuffle, time)
- Combat will be more complex than simple stat accumulation

**Actions Taken:**
- Added "Order-Dependent Card Effects" section to Combat System in DESIGN.md
- Listed potential mechanics: multipliers, modifiers, combo chains, temporary buffs, conditional effects
- Added state management considerations (persistence, reset triggers, stacking)
- Flagged for detailed design in Session 5 (Combat System Design & Simulation)

**Design Note:**
This adds significant complexity to combat simulation but is necessary for draw mechanic to be meaningful. Session 5 will need to:
- Design concrete card effect types
- Specify timing rules for effect application
- Define state management (what persists, what resets, when)
- Balance predictability vs variance

**Rationale:**
- Draw order creates strategic depth
- Different card sequences produce different outcomes
- Deck composition becomes more nuanced (card order matters)
- Adds replayability and skill expression

**Files Modified:**
- DESIGN.md (Combat System section, added order-dependent effects note)
- .cursor/log/sessions/session-1-2-critical-design-decisions.md (this file)

---

**Log Status:** Complete (with refinements and design notes)  
**Task Duration:** ~20 minutes (including refinements and design notes)  
**Deliverables:** 
- Updated DESIGN.md with 5 critical design decisions resolved
- Class-specific deck limit refinement
- Order-dependent card effects design note for Session 5

