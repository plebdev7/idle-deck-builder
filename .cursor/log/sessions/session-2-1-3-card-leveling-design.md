# Task Log: Card Leveling System Design

## Task Information

**Task Reference:** CHECKLIST 2.1.3 | ROADMAP Session 2, Task 2.1.3

**Task Description:** Design complete card leveling and awakening system, including duplicate handling, level-up mechanics, stat scaling formulas, and progression curves.

**Start Time:** 2025-11-09 15:17:36

**Status:** Completed

**End Time:** 2025-11-09 15:32:20

---

## Background Assessment

### Files Read for Context
- [x] CHECKLIST.md (Task 2.1.3 definition and context)
- [x] DESIGN.md (Core design principles and progression)
- [x] ROADMAP.md (Session 2 task structure)
- [x] docs/design-specs/card-system.md (Card rarity system from 2.1.1)
- [x] game-data/balance-config.json (Existing leveling system outline)
- [x] game-data/cards-starter-deck.json (Card structure reference)

### Understanding Summary

Task 2.1.3 follows Task 2.1.1 (rarity system) and 2.1.2 (power curves), building on the preliminary leveling concept that was outlined in 2.1.1. The initial outline included:
- XP-based system with rarity-specific XP values
- Rarity-specific cost multipliers (1.0/1.5/3.0/6.0)
- Rarity-specific stat scaling (20%/25%/30%/35%)
- No level caps

Key constraint identified: **No duplicates until Pack 4+** because Packs 1-3 are deterministic (no random cards). This means leveling is a mid-game mechanic, not early-game.

User's direction emphasized: **Mechanical simplicity with strategic complexity through player decisions.**

### Impact Assessment

**Files to be Modified:**
- `game-data/balance-config.json`: Replace preliminary leveling system with complete design
- `docs/design-specs/card-system.md`: Add complete leveling and awakening specification
- `CHECKLIST.md`: Mark Task 2.1.3 as complete

**Files to be Created:**
- `.cursor/log/sessions/session-2-1-3-card-leveling-design.md`: This task log

**Dependencies Identified:**
- Rarity system (Task 2.1.1) provides foundation
- Pack deterministic/random structure (Tasks 2.1.7-2.1.9) determines when duplicates appear
- Prestige system (Session 7) will interact with level resets
- Card awakening effects will be designed per-card during content creation (Tasks 2.1.7-2.1.9)

---

## Work Log

### Entry 1
**Timestamp:** 2025-11-09 15:17:36

**Action Taken:**
Initiated design discussion with user. Presented proposed discussion structure covering:
1. Math validation (scaling formulas, power curves)
2. Duplicate pipeline definition
3. Practical leveling targets (with Pack 4+ constraint)
4. Level-up UX design
5. Prestige interaction considerations

**Files Impacted:**
- None (discussion phase)

**Rationale:**
Structured approach ensures comprehensive coverage of all leveling aspects while allowing user input on direction and priorities.

**Validation:**
User approved proposed order with specific guidance on each topic.

---

### Entry 2
**Timestamp:** 2025-11-09 15:17:36

**Action Taken:**
Received critical design constraints from user:
1. **No rarity multipliers** - complexity from drop rates, not formulas
2. **Direct duplicate counting** - no XP middleman, count cards directly
3. **Level 10 universal cap** - same for all rarities
4. **Scrap system for awakening** - maxed card duplicates become scraps
5. **Automatic leveling** - no manual confirmation needed
6. **Starter cards treated as Commons** - no special treatment

**Files Impacted:**
- None (design decision phase)

**Rationale:**
User's "mechanically simple/consistent" principle drives all choices. Simplification creates cleaner system with natural difficulty curve from drop rate frequency.

**Validation:**
Explicit user confirmation on all five points.

---

### Entry 3
**Timestamp:** 2025-11-09 15:32:20

**Action Taken:**
Refined awakening system design with user input:
- **Awakening Levels 11-20** with increasing scrap costs (10/20/30/.../100)
- **Level 15: Secondary effect** (utility/synergy additions)
- **Level 20: Transformative effect** (deck-defining mechanics)
- **Total cost to Level 20:** 550 scraps
- **No scrap cross-conversion** (Common scraps ≠ Rare scraps)

Finalized complete leveling system specification.

**Files Impacted:**
- Design specification (ready for documentation)

**Rationale:**
Extended awakening progression (11-20 instead of just stat increases) provides long-term goals spanning multiple prestiges. Level 15/20 effect milestones create meaningful progression beats.

**Validation:**
User confirmation: "let's finalize this design and wrap up 2.1.3"

---

### Entry 4
**Timestamp:** 2025-11-09 15:32:20

**Action Taken:**
Updated `game-data/balance-config.json` with complete leveling system:
- Replaced preliminary XP/rarity multiplier system
- Added universal leveling formula (N-1 duplicates)
- Added awakening system with Level 11-20 progression
- Documented scrap generation and costs
- Added stat multiplier calculations (5.16× at Level 10, 13.74× at Level 20)

**Files Impacted:**
- `game-data/balance-config.json`: Complete rewrite of leveling_system section

**Rationale:**
Game data is authoritative source for all balance values. Leveling system now complete and implementation-ready.

**Validation:**
Values match design decisions: 45 duplicates to Level 10, 550 scraps to Level 20, 20% scaling per level.

---

### Entry 5
**Timestamp:** 2025-11-09 15:32:20

**Action Taken:**
Updated `docs/design-specs/card-system.md` with complete specification:
- Replaced preliminary leveling section with universal system
- Added awakening system documentation
- Updated rarity tier descriptions (removed rarity-specific scaling)
- Added progression timeline (first duplicates at Pack 4+)
- Updated design philosophy with awakening goals
- Added document version history entry (Version 1.2)

**Files Impacted:**
- `docs/design-specs/card-system.md`: Major addition of leveling and awakening systems

**Rationale:**
Design spec documents the system, formulas, and rationale. Provides complete reference for future card content design (Tasks 2.1.7-2.1.9 will design awakening effects per-card).

**Validation:**
Cross-referenced with balance-config.json for consistency.

---

### Entry 6
**Timestamp:** 2025-11-09 15:32:20

**Action Taken:**
Updated `CHECKLIST.md` to mark Task 2.1.3 as complete with all sub-items checked.

**Files Impacted:**
- `CHECKLIST.md`: Marked 2.1.3 complete

**Rationale:**
All task objectives met: duplicate handling defined, level-up mechanics specified, stat scaling formulas designed, progression curve established.

**Validation:**
All CHECKLIST 2.1.3 sub-items addressed in design.

---

### Entry 7
**Timestamp:** 2025-11-09 15:32:20

**Action Taken:**
Created comprehensive task log documenting design session, decisions, and rationale.

**Files Impacted:**
- `.cursor/log/sessions/session-2-1-3-card-leveling-design.md`: Created

**Rationale:**
Complete documentation of design process, user decisions, and system specifications for future reference.

**Validation:**
Log captures all key decisions and design evolution.

---

## Decisions Made

### Decision 1: Universal Leveling Formula
**Timestamp:** 2025-11-09 15:17:36

**Decision:**
All cards use identical leveling formula: **N-1 duplicates** to reach Level N, regardless of rarity.

**Options Considered:**
1. **Rarity-specific multipliers** (preliminary design) - Commons 1×, Rares 1.5×, Epics 3×, Legendaries 6×
   - Pros: Lower rarities level faster with fewer duplicates
   - Cons: Additional complexity, harder to communicate
2. **Universal formula** - Same requirements for all rarities
   - Pros: Simple, consistent, memorable, natural difficulty from drop rates
   - Cons: High rarity cards need same absolute duplicate count

**Chosen Approach:**
Option 2 - Universal formula

**User Confirmation:**
Yes - "let's go mechanically simple/consistent. complexity should come from player decisions"

**Rationale:**
- Drop rate frequency creates natural difficulty curve (Commons 70% vs Legendaries 2%)
- Simpler to understand: "45 duplicates to max any card"
- No special rules or edge cases
- Player choice matters: which cards to focus duplicates on

**Implications:**
- Commons reach max level much faster (high drop rate)
- Legendaries become prestige-spanning goals (low drop rate)
- Clear communication: just show duplicate progress bar
- Applies to awakening system (same scrap costs regardless of rarity)

---

### Decision 2: Direct Duplicate Counting
**Timestamp:** 2025-11-09 15:17:36

**Decision:**
Direct duplicate counting with no XP middleman. Duplicates increment counter directly toward next level.

**Options Considered:**
1. **XP-based system** (preliminary design) - Duplicates grant XP, XP accumulates to level up
   - Pros: Allows weighted XP (Rare dup = 2 XP), more flexible
   - Cons: Additional abstraction layer, harder to communicate
2. **Direct counting** - Duplicates = progress directly
   - Pros: Simpler, clearer, no conversion math
   - Cons: Can't have weighted duplicates

**Chosen Approach:**
Option 2 - Direct counting

**User Confirmation:**
Yes - "i think simplifying it to be 'number of cards to level up' rather than worrying about xp"

**Rationale:**
- Eliminates unnecessary abstraction
- Clear communication: "3/5 duplicates to Level 6"
- Fits with universal formula decision
- Players understand card counting better than XP points

**Implications:**
- UI shows duplicate progress directly
- No XP conversion calculations needed
- Scrap system also uses direct 1:1 conversion

---

### Decision 3: Level 10 Cap with Awakening Extension
**Timestamp:** 2025-11-09 15:17:36

**Decision:**
Universal Level 10 cap for base leveling. Awakening system extends to Level 20 using scrap currency.

**Options Considered:**
1. **No caps** (preliminary design) - Infinite leveling
   - Pros: Never hit ceiling
   - Cons: Balance issues at extreme levels, no natural milestone
2. **Rarity-specific caps** - Different caps by rarity
   - Pros: Graduation effect (max Commons, move to Rares)
   - Cons: Additional complexity, inconsistent experience
3. **Universal Level 10 cap** - Same cap for all rarities
   - Pros: Clear milestone, enables scrap system, simple
   - Cons: Need post-cap progression

**Chosen Approach:**
Option 3 - Universal Level 10 cap with awakening to 20

**User Confirmation:**
Yes - "option B sounds right" (universal cap), "10 is perfect"

**Rationale:**
- 45 duplicates to Level 10 is reasonable long-term goal
- Level 10 = 5.16× stats (strong but not game-breaking)
- Creates natural transition to awakening system
- Memorable milestone ("maxed out at Level 10")

**Implications:**
- First maxed cards appear after ~50-100 packs
- Scrap accumulation begins mid-game
- Awakening becomes ultra-late-game progression layer
- Clear design space for secondary/transformative effects

---

### Decision 4: Hybrid Awakening Progression
**Timestamp:** 2025-11-09 15:32:20

**Decision:**
Awakening Levels 11-20 with **stat increases + effect milestones**:
- Levels 11-14: Stat increases only (10/20/30/40 scraps)
- Level 15: Secondary effect + stat increase (50 scraps)
- Levels 16-19: Stat increases only (60/70/80/90 scraps)
- Level 20: Transformative effect + stat increase (100 scraps)

**Options Considered:**
1. **Stats only** - Just level cap breaking
   - Pros: Simple extension
   - Cons: No mechanical depth
2. **Effects only** - Awakening adds abilities
   - Pros: Mechanical complexity
   - Cons: Need to design for every card
3. **Hybrid** - Stats with effect milestones
   - Pros: Progressive depth, clear goals
   - Cons: More design work per card

**Chosen Approach:**
Option 3 - Hybrid with extended progression

**User Confirmation:**
Yes - "i'd go further to have 11-14 stat increase, 15 secondary effect, 16-19 stat increase, 20 transformative effect"

**Rationale:**
- Provides long-term progression runway (many prestiges)
- Clear milestones at 15 and 20 (celebration moments)
- Stats increases fill gaps between effect milestones
- Transformative Level 20 creates ultimate goals
- 550 total scraps makes this prestige-spanning content

**Implications:**
- Each card needs Level 15 and Level 20 effect designs
- Effect design happens during card content creation (Tasks 2.1.7-2.1.9)
- Creates build-around potential (Level 15 synergies)
- Deck-defining transformations (Level 20 changes strategies)

---

### Decision 5: No Scrap Cross-Conversion
**Timestamp:** 2025-11-09 15:32:20

**Decision:**
Scrap rarities cannot be converted between each other. Common scraps ≠ Rare scraps ≠ Epic scraps ≠ Legendary scraps.

**Options Considered:**
1. **Cross-conversion allowed** - Trade 5 Common → 1 Rare, etc.
   - Pros: More flexibility, Common scraps always useful
   - Cons: Optimal path always converts up, less strategic
2. **No conversion** - Rarity-specific scraps
   - Pros: Strategic choices (which cards to awaken), maintains rarity prestige
   - Cons: Common scraps pile up if all Commons maxed

**Chosen Approach:**
Option 2 - No cross-conversion

**User Confirmation:**
Yes - "assume no for now"

**Rationale:**
- Forces strategic decisions (which cards to awaken in each rarity)
- Maintains rarity prestige (Legendary awakenings are special)
- Prevents "always convert up" optimal strategy
- Each rarity has independent awakening progression

**Implications:**
- Common scraps only awaken Commons (forces choices)
- Can't "shortcut" to Legendary awakenings with Common scraps
- Collection depth matters (need multiple cards in each rarity)
- Future consideration: prestige could enable limited conversion

---

### Decision 6: Universal 20% Stat Scaling
**Timestamp:** 2025-11-09 15:17:36

**Decision:**
All cards gain 20% multiplicative stat increase per level, regardless of rarity. Formula: Base × (1.20)^(level-1)

**Options Considered:**
1. **Rarity-specific scaling** (preliminary design) - 20%/25%/30%/35% by rarity
   - Pros: Higher rarities scale better
   - Cons: Additional complexity, harder to balance
2. **Universal 20% scaling** - Same for all rarities
   - Pros: Simple, predictable, natural power from base stats
   - Cons: Lower rarities can catch up with enough levels

**Chosen Approach:**
Option 2 - Universal 20% scaling

**User Confirmation:**
Implicit in "no rarity multipliers" decision - consistency across all mechanics

**Rationale:**
- Consistent with "mechanically simple" principle
- Power difference comes from base stat budgets (Commons 20-30, Legendaries 90-180)
- Higher rarities still superior (better base × same scaling = better results)
- Easier to communicate and calculate

**Implications:**
- Level 10 Common (25 base) = 129 stats
- Level 10 Legendary (135 base) = 697 stats
- Legendaries always stronger at same level
- But maxed Common (Level 20) competitive with low-level Epic

---

### Decision 7: Automatic Leveling
**Timestamp:** 2025-11-09 15:17:36

**Decision:**
Cards level up automatically when duplicate threshold reached. No manual confirmation required.

**Options Considered:**
1. **Manual leveling** - Player must confirm each level-up
   - Pros: Player agency, celebration moment
   - Cons: Interrupts flow, tedious at scale
2. **Automatic leveling** - Levels up immediately
   - Pros: Smooth flow, idle-friendly
   - Cons: Less player engagement

**Chosen Approach:**
Option 2 - Automatic leveling with pack screen notifications

**User Confirmation:**
Yes - "automatic for sure, but card pack opening screen should note progress"

**Rationale:**
- Fits idle game philosophy (progress happens automatically)
- Reduces tedium (many cards will level over time)
- Pack opening provides natural feedback moment
- Progress bars show advancement without interruption

**Implications:**
- Pack opening screen shows: "⭐ Arcane Bolt reached Level 6!"
- Collection screen shows progress: "3/5 to Level 7"
- No separate "level up" action needed
- Applies to awakening too (auto-awaken with notification)

---

### Decision 8: Starter Cards as Regular Commons
**Timestamp:** 2025-11-09 15:32:20

**Decision:**
Starter deck cards have no special leveling treatment. They are Commons like any other Common cards.

**Options Considered:**
1. **Special starter treatment** - Reduced awakening costs, faster leveling
   - Pros: Rewards player attachment, nostalgia
   - Cons: Arbitrary special case, complicates system
2. **Regular Commons** - No special rules
   - Pros: Consistent, simple, fair
   - Cons: Starter cards not "special"

**Chosen Approach:**
Option 2 - Regular Commons

**User Confirmation:**
Yes - "no, starters are just commons like any other commons"

**Rationale:**
- Maintains system consistency (no special cases)
- Starters already appear in early packs (easy to get duplicates)
- Player can choose which cards to focus on
- Nostalgia shouldn't override mechanical clarity

**Implications:**
- Arcane Bolt levels same as any Pack 1 Common
- No "starter card bonus" mechanic needed
- Simpler codebase (no starter flag checks)
- Design can evolve starters without worrying about special leveling

---

## User Confirmations

### Confirmation 1: Design Direction
**Timestamp:** 2025-11-09 15:17:36

**Question/Issue:**
Presented five-topic discussion structure for leveling design (math, pipeline, targets, UX, prestige).

**User Response:**
"your order seems good to me" with specific notes on each topic

**Action Taken:**
Proceeded with structured approach, incorporating user's specific constraints on each topic.

---

### Confirmation 2: Mechanical Simplicity Principle
**Timestamp:** 2025-11-09 15:17:36

**Question/Issue:**
Should we use rarity-specific multipliers and XP systems, or simplify?

**User Response:**
"let's go mechanically simple/consistent. complexity should come from player decisions"

**Action Taken:**
Removed all rarity-specific formulas, simplified to universal mechanics with natural difficulty from drop rates.

---

### Confirmation 3: Awakening Progression Length
**Timestamp:** 2025-11-09 15:32:20

**Question/Issue:**
Presented three awakening options (stats-only, effects-only, hybrid). Recommended hybrid.

**User Response:**
"yes, hybrid awakening sounds right. i'd go further to have 11-14 stat increase, 15 secondary effect, 16-19 stat increase, 20 transformative effect - gives a lot of design space for much later game progression for late prestiges"

**Action Taken:**
Extended awakening to Level 20 with effect milestones at 15 and 20. Total cost 550 scraps.

---

### Confirmation 4: Design Finalization
**Timestamp:** 2025-11-09 15:32:20

**Question/Issue:**
Reviewed complete system specification with user.

**User Response:**
"let's finalize this design and wrap up 2.1.3"

**Action Taken:**
Documented complete system in balance-config.json and card-system.md, marked task complete.

---

## Validation Status

### Validation Checks Performed

- [x] **Universal formula consistency:** All rarities use N-1 duplicates formula
- [x] **Math validation:** 45 duplicates to Level 10, 550 scraps to Level 20
- [x] **Stat multiplier calculations:** 5.16× at Level 10, 13.74× at Level 20
- [x] **Drop rate analysis:** Commons easier to max (70% vs 2% Legendaries)
- [x] **Timeline validation:** No duplicates until Pack 4+ (deterministic Packs 1-3)
- [x] **Cross-reference with rarity system:** Stat budgets (Task 2.1.1) still valid
- [x] **Design document synchronization:** balance-config.json matches card-system.md
- [x] **Prestige integration:** Level reset tied to pack cost reset (deferred to Session 7)

### Issues Identified

None. Design is internally consistent and aligns with established principles.

### Resolution Status

All objectives met. System is complete and implementation-ready.

---

## Deliverables

### Created Files
- `.cursor/log/sessions/session-2-1-3-card-leveling-design.md`: Complete task log and design documentation

### Modified Files
- `game-data/balance-config.json`: Complete leveling and awakening system specification
  - Replaced preliminary XP-based system with universal duplicate counting
  - Added awakening system with Level 11-20 progression
  - Documented scrap generation and costs
- `docs/design-specs/card-system.md`: Added complete leveling and awakening specification
  - Universal leveling section with formulas
  - Awakening system documentation
  - Updated rarity tier descriptions
  - Updated design philosophy with progression timeline
  - Version 1.2 history entry
- `CHECKLIST.md`: Marked Task 2.1.3 as complete with timestamp

---

## Completion Summary

**Objectives Met:**
- [x] Define duplicate card handling (direct duplicate counting, no XP)
- [x] Specify level-up mechanics (N-1 duplicates, automatic, universal)
- [x] Design stat scaling formulas (20% multiplicative, all rarities)
- [x] Define max level caps (Level 10 base, Level 20 awakening)
- [x] Design awakening system (scrap currency, effect milestones)
- [x] Document complete system (balance-config + card-system.md)
- [x] Validate progression timeline (Pack 4+ constraint)
- [x] Consider prestige interaction (reset tied to pack costs)

**Outstanding Issues:**
None. All design objectives complete.

**Next Steps:**
- Task 2.1.4: Research conditional mechanics (next in Phase 2)
- Tasks 2.1.7-2.1.9: Design card-specific awakening effects (Level 15/20)
- Session 7: Finalize prestige system and level reset behavior

**CHECKLIST.md Update:**
Task 2.1.3 marked complete with all sub-items checked.

**Additional Notes:**

**Key Design Principles Established:**
1. **Universal mechanics** - Same rules for all rarities
2. **Drop rates create difficulty** - Frequency, not formulas
3. **Automatic progression** - Idle-friendly, notification-driven
4. **Long-term goals** - Level 10 mid-game, Level 20 prestige-spanning
5. **Effect milestones** - Level 15/20 provide strategic depth

**Design Space for Future Work:**
- Card-specific Level 15 secondary effects (utility/synergy)
- Card-specific Level 20 transformative effects (deck-defining)
- Prestige bonuses (duplicate drop rates, scrap gains, etc.)
- Achievement system (first Level 10, all starters maxed, etc.)

**Balance Notes:**
- Level 10 Common = ~129 stats (5.16× base 25)
- Level 10 Legendary = ~697 stats (5.16× base 135)
- Level 20 Common = ~344 stats (13.74× base 25)
- Level 20 Legendary = ~1854 stats (13.74× base 135)
- Legendaries always stronger at same level due to higher base budgets

**Math Reference:**
- Duplicates to Level N: N-1 (cumulative: 45 to Level 10)
- Scraps to Level N: 10 × (N-10) (cumulative: 550 to Level 20)
- Stat multiplier: (1.20)^(level-1)
- Pack 4+ timing: ~33 min (first duplicate opportunity)

---

## Cross-References

**Related Log Files:**
- Session 2.1.1 log: Card rarity system design (stat budgets, drop rates)
- Session 2.1.2 log: Power curve and stat point system

**DESIGN.md Sections Referenced:**
- Core Vision: Idle gameplay with strategic depth
- Progression & Scaling: Enemy scaling and pack timing

**Design Spec Files Referenced:**
- `docs/design-specs/card-system.md`: Complete card system specification
- `docs/design-specs/baseline-numbers.md`: Pack timing and progression

**ROADMAP.md Sections Referenced:**
- Session 2, Task 2.1 (Phase 1): Foundation Research

**CHECKLIST.md Items:**
- Task 2.1.1: Card rarity system (foundation)
- Task 2.1.2: Power curve analysis (stat budgets)
- Task 2.1.3: Card leveling concept (this task - COMPLETE)
- Task 2.1.4: Conditional mechanics (next task)

**Game Data Files:**
- `game-data/balance-config.json`: Authoritative source for all leveling values
- `game-data/cards-starter-deck.json`: Card structure reference

---

**Log Created:** 2025-11-09 15:32:20
**Last Updated:** 2025-11-09 15:32:20

