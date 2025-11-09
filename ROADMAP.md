# Idle Deck Builder - Design & Simulation Roadmap

## Overview
This roadmap focuses on creating detailed design specifications and validation tools for the Idle Deck Builder game. Each session produces detailed design documents and simulation tools (spreadsheets, calculators, models) that validate mechanics and system interactions before implementation.

## Approach: Design Specs + Lightweight Simulation

**Strategy:** Create detailed design specifications supported by lightweight simulation tools:
- **Spreadsheets/Calculators**: Model resource generation, combat outcomes, progression curves
- **Component Interaction Diagrams**: Map how systems connect and affect each other
- **Gameplay Simulation Models**: Test game loops and balance without full implementation
- **Detailed Specifications**: Complete enough that implementation is straightforward

---

## Session 1: Design Foundation & Theme

### Goals
- Settle on theme/story that guides all design decisions
- Answer critical outstanding design questions that block core systems
- Establish detailed core game loop specification

### Tasks

#### 1.1 Theme Selection & Story Framework
- Choose theme (fantasy, sci-fi, modern, etc.)
- Define basic narrative framework (why tiers exist, what classes represent)
- Name currencies and tiers with theme-appropriate names
- Create visual/style direction brief

#### 1.2 Critical Design Decisions (Outstanding Questions)
Answer questions 1, 4, 5, 9, 10 from DESIGN.md (most blocking):
- **Question 1: Class Switching Cost:** Free anytime, cost currency, only on prestige, or hybrid?
- **Question 4: Gray Tier Combat Role:** Independent battles, contributes to colored decks, or passive bonuses?
- **Question 5: Gray Points as Universal Currency:** Gray-only, convertible, or global upgrade currency?
- **Question 9: Deck Size Limits:** Fixed size, variable with diminishing returns, or point-based?
- **Question 10: Combat Timing:** Continuous auto-battles, timed intervals, or event-based?

Document decisions in DESIGN.md with rationale and implications for other systems.

#### 1.3 Core Loop Detailed Specification

**Approach:** Work through in three parts for better flow: Experience → Numbers → Content

**Part A: High-Level Experience (Qualitative)**
- Define exact first 30 minutes of gameplay (step-by-step, minute-by-minute narrative)
- Create gameplay flow diagram showing all decision points and branches
- Identify key milestones and progression gates
- Focus on player experience, not exact numbers yet

**Part B: Baseline Numbers (Quantitative)**
- Establish resource generation baseline rates (rough numbers, will be refined in Session 4)
- Define pack pricing model (question 8) with scaling formulas
- Create economy flow model (how Arcane → Elemental conversion works)
- Rough numbers to validate core loop timing

**Part C: Starter Deck (Concrete Content)**
- Design 5-8 simple starter cards (basic examples, Session 2 will expand to 15-20)
- Specify exact starter deck composition (cards, stats, costs)
- Use baseline numbers from Part B
- Validate against first 30 minutes experience from Part A
- Keep cards simple (Session 2 will add complexity and variety)

### Deliverables
- ✅ Theme document (1-2 pages) - Complete (theme-specification.md, visual-style-guide.md)
- ✅ Updated DESIGN.md with resolved questions and detailed rationale - Complete (Version 1.2)
- [ ] Detailed core loop specification document (step-by-step gameplay) - Task 1.3
- [ ] Resource generation baseline spreadsheet/model - Task 1.3
- [ ] Starter deck card designs - Task 1.3

---

## Session 2: Card System Design & Specifications

### Goals
- Build gameplay simulator to validate Session 1.3 designs
- Design concrete card examples that demonstrate all mechanics
- Define complete card data structure and stat systems
- Create card interaction specifications
- Test and balance cards using simulator

### Tasks

#### 2.0 Gameplay Simulator (Foundation)
- Build basic combat simulator
  - Card draw system (1 card per second, deck cycling)
  - Power/Defense accumulation
  - Enemy arrival intervals (12 seconds)
  - Combat resolution (instant when enemy arrives)
- Implement generator mechanics
  - Rate generators (accumulate Essence/sec)
  - Burst generators (flat Essence)
  - Hybrid generators (rate + combat stats)
  - Stacking mechanic (every draw adds, including duplicates)
- Implement combat mechanics
  - Power accumulation from combat cards
  - Enemy health scaling (temporary linear scaling for testing)
  - Victory/defeat conditions
- Validate Session 1.3 baseline numbers
  - Test starter deck (8 cards) against first 30 minutes
  - Establish "bad player" baseline (no pack purchases)
  - Confirm core mechanics work correctly
- Create simulation output/visualization
  - Timeline view (essence over time, enemies defeated, cards drawn)
  - Deck analysis (power accumulation, generation rates)
  - Balance metrics (time to packs, combat power vs enemy health)

#### 2.0.1 Combat Progression Design ✅ COMPLETE
**Purpose:** Resolve combat scaling questions revealed by Task 2.0 simulator

**Completed Deliverables:**
- ✅ Combat scaling formula finalized: Linear `20 + (n-1) × 65.8`
- ✅ Boss encounter system designed:
  - Mini-Boss #1 at Enemy 50 (1.3× HP multiplier, tutorial encounter)
  - Mini-Boss #2 at Enemy 100 (1.5× HP multiplier, first real wall)
  - Major Boss at Enemy 150 (≈2× HP multiplier, requires multiple loops)
- ✅ Death loop mechanics specified (NOT prestige):
  - Keep all resources between deaths
  - Spend essence/shards to improve deck
  - Expected 3-6 loops to beat first boss
- ✅ Multi-loop progression targets defined
- ✅ Death vs prestige distinction clarified (prestige deferred to Session 7)
- ✅ Balance targets for Task 2.1 provided
- ✅ DESIGN.md updated (Version 1.8)

**Key Design Decisions:**
- Linear enemy scaling for predictability and balance
- Boss encounters every 50 enemies (50, 100, 150)
- Death is core game loop, not punishment
- "Rogue with the Dead" inspired death-as-progression model
- Prestige is separate advanced mechanic for late game

#### 2.0.2 Live Terminal Simulation View ✅ COMPLETE
- Create live terminal visualization mode for simulator
- **Display Features:**
  - Real-time card draw display with effects
  - Enemy HP bars and combat status
  - Essence accumulation and rate tracking
  - Event log (recent card draws, enemy spawns, victories)
  - Pack affordability notifications
- **Speed Controls:**
  - Real-time (1x), 2x, 5x, 10x speed multipliers
  - Keyboard shortcuts: 1-4 for speeds
  - Pause/resume functionality (Space)
  - Step-through mode (advance one event at a time)
- **Interaction Features:**
  - Auto-pause on pack milestones and boss encounters
  - Quit early with summary stats
  - Post-simulation summary screen
  - Option to replay or generate charts
- **Purpose:** Understand game flow, pacing, and card interactions during card design work (Tasks 2.1-2.4)

#### 2.0.3 Combat System Redesign (DESIGN SESSION - CRITICAL)
**Purpose:** Redesign combat from instant-resolution to Trimps-style combat-over-time model

**Problem:** Current combat accumulates attack/defense indefinitely, resolving instantly. Every enemy dies in one tick. No actual "combat" occurs.

**Solution:** Combat-over-time with player HP, death mechanics, and stat resets per enemy.

**Part A: Combat Mechanics Specification (60-90 min)**
- Design combat tick system
  - Tick rate decision (0.1s, 1.0s, or other)
  - Damage calculation per tick
  - Defense mechanics (flat reduction, percentage, cap)
- Design player HP system
  - Starting HP value
  - HP scaling with progression (per enemy, per pack, prestige)
  - HP recovery timing (after enemy, after pack, never)
  - Max HP vs Current HP mechanics
- Specify stat reset mechanics
  - Attack/Defense reset to 0 after each enemy
  - Essence rate persists across enemies (only resets on death)
  - Cards drawn during enemy fight add permanently until reset
- Create combat flow examples
  - Tick-by-tick walkthrough of enemy encounter
  - Show stat changes during combat
  - Demonstrate card draw effects mid-combat

**Part B: Death & Respawn System (45-60 min)**
- Define death conditions
  - HP reaches 0 during combat
  - Timeout against unkillable enemy (if applicable)
- Specify death consequences
  - Stats reset: Attack, Defense, Essence Rate, HP
  - Resources retained: Accumulated essence, card collection, deck composition
  - Respawn location: Enemy 1
- Integrate with death loop system (Session 2.0.1)
  - Death as progression mechanic (spend essence between attempts)
  - Class switching on death (if owns class cards)
  - 3-6 death loops expected to beat first boss
- Design death screen feedback
  - Progress indicators ("You reached Enemy 47")
  - Essence/resources earned this run
  - Encouragement to improve deck

**Part C: Balance & Scaling (60-90 min)**
- Establish combat duration targets
  - Early enemies (1-50): Target seconds to defeat
  - Mid enemies (51-100): Target seconds to defeat
  - Late enemies (101-149): Target seconds to defeat
  - Boss enemies (50, 100, 150): Target seconds to defeat
- Design player HP scaling formulas
  - Starting HP baseline
  - Growth per enemy defeated
  - Growth per pack purchased
  - Prestige HP bonuses
- Rebalance enemy HP and attack
  - Current HP formulas still appropriate?
  - Boss multipliers still correct?
  - Attack scaling needs adjustment?
  - New validation targets needed
- Update card stat ranges
  - Starter deck stat rebalancing
  - Pack card stat ranges update
  - Generator vs combat card ratios
  - Combat duration vs essence generation tradeoff

**Part D: Documentation (30-45 min)**
- Update DESIGN.md combat system section
  - Replace instant-resolution with combat-over-time
  - Document stat reset mechanics
  - Specify HP system and death mechanics
  - Version 1.9
- Update baseline numbers section
  - New combat duration expectations
  - Revised enemy scaling if needed
  - Updated card stat ranges
- Update first 30 minutes experience
  - How death fits into first session
  - Do players die in first 30 minutes?
  - Tutorial death at Enemy 150 still valid?
- Document changelog
  - Mark superseded sections (old combat)
  - Explain rationale for redesign
  - Cross-reference to Session 2.0.3

**Key Decision (Pre-Decided):**
- Cards add to attack/defense permanently during enemy fight
- Stats reset to 0 when enemy dies
- Essence rate persists (only resets on death)

**Deliverables:**
- Complete combat tick system specification with formulas
- Player HP system design (starting HP, scaling, recovery)
- Death/respawn mechanics integrated with death loop system
- Combat duration targets established
- Enemy scaling validated against new combat model
- Card stat ranges updated
- DESIGN.md Version 1.9 with combat redesign

**Blocks:** Task 2.1 (Pack Card Design) - Cannot design cards without knowing combat mechanics

#### 2.0.4 Implement New Combat System
**Purpose:** Reimplement simulator with new combat-over-time mechanics

**Implementation Tasks:**
- Reimplement `combat.py` with combat-over-time system
  - Replace instant resolution with tick-based combat
  - Add combat duration tracking
  - Update damage calculation to per-tick model
- Add `Player` class with HP system
  - Current HP and Max HP attributes
  - HP scaling mechanics
  - HP recovery between enemies
  - Death detection (HP = 0)
- Add death/respawn system
  - Reset combat stats (ATK/DEF) on death
  - Reset essence rate on death
  - Keep accumulated essence and collection
  - Respawn at Enemy 1
- Update simulation loop
  - Add combat tick intervals
  - Process combat ticks separately from card draws
  - Handle death and respawn events
- Add combat duration metrics
  - Track time per enemy
  - Track total combat time vs idle time
  - Combat efficiency metrics

**Testing:**
- Validate combat tick mechanics work correctly
- Test HP depletion and death conditions
- Verify stat reset behavior (resets per enemy, essence persists)
- Test boss encounters with new combat
- Ensure death loop works as designed

**Estimated Time:** 2-3 hours implementation

#### 2.0.5 Update Validation System
**Purpose:** Update validation to test new combat mechanics

**Validation Updates:**
- Update validation targets for new combat timing
  - Pack affordability may shift due to combat duration
  - Essence accumulation timing affected by combat
  - Enemy defeat rate changes with combat duration
- Add HP system validation
  - Starting HP correct
  - HP scaling formulas working
  - HP recovery timing correct
  - Death triggers at HP = 0
- Add death system validation
  - Stat reset on death working
  - Essence rate reset on death
  - Accumulated essence retained
  - Respawn at Enemy 1 working
- Test boss encounters with new combat
  - Mini-bosses at 50, 100 defeatable with starter deck
  - Major boss at 150 appropriately challenging
  - Combat duration targets met
- Validate combat duration targets
  - Early enemies defeated in target time
  - Boss enemies take longer as designed
  - Combat feels appropriately paced
- Revalidate baseline numbers
  - All 8 validation checks re-run
  - New tolerances if needed
  - Document any shifts in timing

**Estimated Time:** 1-2 hours

#### 2.1 Pack Card Design (15-20 cards for Packs 1-3)

**Approach:** Research → Design → Implementation (5-phase structured process)

**Phase 1: Foundation Research (DESIGN SESSION, 2-3 hours)**
- **2.1.1 - Card Rarity System**
  - Define 4-tier system (Common/Rare/Epic/Legendary)
  - Specify stat multipliers and ranges per rarity
  - Define drop rates from packs
  - Document ultra-rare/unique card philosophy (future expansion)
- **2.1.2 - Power Curve Analysis**
  - Validate stat ranges per pack and rarity
  - Model essence generation with Pack 1 cards
  - Model combat effectiveness (Enemy 100 feasibility)
  - Validate 4-6 death loop progression expectation
- **2.1.3 - Card Leveling Concept**
  - Define duplicate card handling (XP? Fusion? Scrapping?)
  - Specify level-up mechanics and requirements
  - Design stat scaling formulas per level
  - Define max level caps and progression curve

**Phase 2: Mechanic Design Research (DESIGN SESSION, 2-3 hours)**
- **2.1.4 - Conditional Mechanics Research**
  - Evaluate condition types (timing, composition, state-based)
  - Identify "fun to build around" vs "too random/confusing"
  - Define testable conditions for Pack 1-3
  - Create conditional ability templates
- **2.1.5 - Sequencing & Order-Dependent Mechanics**
  - Design "next card" and "previous card" tracking
  - Specify combo trigger chains
  - Define state persistence rules (reshuffle, enemy, death)
- **2.1.6 - Card Data Structure & Text Format**
  - Define complete card template (all fields)
  - Specify stat notation format
  - Create ability description templates with keywords
  - Validate text fits card layout (3 lines max, 12px font)

**Phase 3: Card Content Design (DESIGN SESSION, 3-4 hours)**
- **2.1.7 - Pack 1 Guaranteed Cards** (5 deterministic cards)
  - 2 generator cards (+3, +4 Essence/sec range)
  - 2 combat cards (25-30 total stats)
  - 1 utility card (introduce first simple conditional)
  - Document design rationale for each card
- **2.1.8 - Pack 2 Guaranteed Cards** (5 deterministic cards)
  - 1 multiplier generator (Current rate × Y seconds)
  - 3 combat cards (35-45 total stats, introduce sequencing)
  - 1 Rare synergy card (first combo mechanic)
  - Document design rationale for each card
- **2.1.9 - Pack 3+ Random Pool** (5-10 cards for Arcane tier)
  - Mix of Common/Rare/Epic cards
  - Deck manipulation ("Draw extra card", "Shuffle deck")
  - State-based effects ("Lasts until reshuffle")
  - Higher power level cards (Rare 50-80, Epic 100-150 stats)
  - Document design rationale for each card

**Phase 4: Validation & Documentation (1-2 hours)**
- **2.1.10 - Validate Cards Against Constraints**
  - Check against visual-style-guide.md
  - Verify power curve progression
  - Confirm mechanical complexity curve
  - Validate deterministic packs teach mechanics
- **2.1.11 - Update Design Documents**
  - Add rarity system to DESIGN.md
  - Add card leveling system design
  - Document all 15-20 pack cards with full stats
  - Update pack contents and guaranteed lists
  - Add card data structure specification
  - Resolve Outstanding Question 7

**Phase 5: Implementation (if needed, 2-4 hours)**
- **2.1.12 - Implement New Mechanics in Simulator**
  - Add conditional trigger system
  - Add sequencing/order-dependent tracking
  - Add state persistence management
  - Add deck manipulation mechanics
  - Test all new pack cards in simulator
  - Validate balance and progression targets

**Key Decisions (Pre-Made):**
- First 2-3 packs are fully deterministic (same cards every time)
- 4-tier rarity system with room for ultra-rare/unique in future
- Conditionals allowed but must be "fun to build around" not "confusing"
- Design first, implementation after (but docs must sync)

#### 2.2 Card Interaction Specifications
- Define trigger chains: exact conditions and effects
- Specify conditional abilities: "If X, then Y" mechanics
- Design combo requirements: card combinations and their effects
- Create interaction matrix showing which cards interact and how
- Specify order-dependent mechanics (sequencing rules)
- Define state management (what persists, what resets, when)
- Implement interactions in simulator to test

#### 2.3 Generator Card Pattern Specifications
- **Rate Generators:** +X Essence/sec when drawn (scales with level)
- **Burst Generators:** +X flat Essence when drawn (scales with level)
- **Hybrid Generators:** +X Essence/sec + combat stats (balanced scaling)
- **Multiplier Generators:** +(Current rate × Y seconds) Essence (scales with accumulated rate)
- **Conditional Generators:** +X Essence/sec if condition met (higher rates, conditional)
- Define generation formulas and scaling with card level
- Test all patterns in simulator

#### 2.4 Combat Card Pattern Specifications
- **Pure Specialists:** High attack OR high defense, no other stats
- **Generalists:** Balanced attack and defense
- **Conditional Combat:** Bonus stats if conditions met ("If drawn early...", "If 3+ cards...")
- **Order-Dependent Combat:** Modifies other cards ("Next card gets +X%", "Previous card triggers...")
- **Combo Combat:** Requires multiple cards for full effect
- Define combat formulas, defense mechanics, and scaling with card level
- Test all patterns in simulator

### Deliverables
- ✅ **Gameplay simulator** (playable, validates Session 1.3 designs)
- ✅ **Combat progression design** (enemy scaling, bosses, death loops)
- ✅ **Live simulation viewer** (terminal-based real-time visualization)
- **Combat system redesign** (Trimps-style combat-over-time, HP system, death mechanics)
- **Updated simulator** (implements new combat system with death/respawn)
- **Updated validation** (tests new combat mechanics and timing)
- Complete card design document with 15-20 Arcane tier pack cards
- Card data structure specification (all fields, types, ranges)
- Card leveling progression spreadsheet (show stat growth curves)
- Card interaction specification document
- Generator and combat pattern reference
- Simulation results showing balance validation

---

## Session 3: Tier & Class System Design

### Goals
- Design complete tier structure and class paths
- Specify cross-tier interactions and synergies
- Create resource flow models

### Tasks

#### 3.1 Tier System Complete Specification
- Finalize tier count per class (3-5 tiers)
- Design 3 starter class paths (Common classes) with full details
- Define exact tier unlock sequence for each class
- Specify tier colors and theme-appropriate names
- Define passive tier mechanics (resource generation rates, conditions)

#### 3.2 Class System Detailed Design
- Define class card structure (stats, abilities, tier unlocks)
- Design 3 starter classes (Warrior, Mage, Ranger) with full specs
- Specify class switching mechanics (costs, conditions, implications)
- Design class-specific bonuses and synergies
- Create class comparison matrix

#### 3.3 Cross-Tier Mechanics Specification
- Design cross-tier resource generation formulas
- Specify cross-tier synergy examples (concrete card combinations)
- Define multi-currency card mechanics
- Create resource flow diagram (which tiers generate which currencies)

### Deliverables
- Complete tier system specification document
- Class system design document (3 starter classes detailed)
- Cross-tier interaction specification
- Resource flow model/diagram
- Tier progression spreadsheet (show unlock requirements)

---

## Session 4: Resource Generation & Economy Design

### Goals
- Design complete resource generation system with formulas
- Create economy balance models
- Specify generator card design patterns

### Tasks

#### 4.1 Resource Generation System Specification
- Design generator card examples (Pure, Hybrid, Conditional) with exact formulas
- Define generation rate formulas (base rate, scaling factors, level multipliers)
- Specify deck composition effects on generation
- Create generation rate calculator/spreadsheet
- Design multi-currency generation cards

#### 4.2 Economy Balance Model
- Create pack cost scaling formulas
- Design resource generation balance model (generators vs combat cards)
- Specify optimal deck composition targets (X% generators, Y% combat)
- Create economy flow model (earn → spend → progress)
- Design idle generation mechanics (offline rates, caps)

#### 4.3 Generator Card Design Patterns
- **Pure Generator:** exact stats, generation rates, scaling
- **Hybrid Generator:** combat stats + generation, balance formulas
- **Conditional Generator:** trigger conditions, generation rates, scaling
- Create generator card examples for each tier

### Deliverables
- Resource generation system specification document
- Economy balance spreadsheet (model resource flow)
- Generator card design pattern document
- Generation rate calculator tool
- Economy flow diagrams

---

## Session 5: Combat System Design & Simulation

### Goals
- Design complete combat system mechanics
- Create combat simulation model
- Specify enemy scaling and difficulty curves

### Tasks

#### 5.1 Combat System Complete Specification
- Define combat mechanics (how cards interact in battle)
- Specify auto-battle resolution (formula-based or simulation-based)
- Design combat timing (continuous, interval-based, event-based)
- Create combat flow diagram

#### 5.2 Combat Simulation Model
- Create spreadsheet calculator for combat outcomes
- Model deck power calculations (how deck composition affects combat)
- Design enemy stat scaling formulas
- Create combat simulation tool (simple calculator or spreadsheet)
- Test different deck compositions against enemy scaling

#### 5.3 Difficulty & Progression Specification
- Define enemy difficulty scaling curves
- Specify victory/defeat conditions
- Design reward formulas (resources per victory)
- Create difficulty progression model

### Deliverables
- Combat system specification document
- Combat simulation spreadsheet/calculator
- Enemy scaling formulas and curves
- Difficulty progression model
- Combat outcome examples (test cases)

---

## Session 6: Deck Building System Design

### Goals
- Design complete deck building constraints and mechanics
- Create deck composition analysis tools
- Specify deck optimization strategies

### Tasks

#### 6.1 Deck Building Constraints Specification
- Define deck size limits (fixed, variable, point-based) with exact rules
- Specify card limits (max copies, rarity restrictions)
- Design deck budget system (if point-based)
- Create deck validation rules

#### 6.2 Deck Composition Analysis
- Create deck composition spreadsheet (analyze generator/combat ratio)
- Design synergy detection/analysis tools
- Specify optimal deck templates for different strategies
- Create deck power calculator

#### 6.3 Deck Building Strategy Documentation
- Document resource optimization strategies
- Specify synergy building patterns
- Design cross-tier composition strategies
- Create deck building decision tree

### Deliverables
- Deck building system specification document
- Deck composition analysis spreadsheet
- Deck power calculator tool
- Deck building strategy guide
- Example deck compositions

---

## Session 7: Prestige & Progression Systems Design

### Goals
- Complete prestige system design with all mechanics
- Define duplicate handling system
- Create progression curve models

### Tasks

#### 7.1 Prestige System Complete Specification
- Answer question 6 (prestige reset details) with exact mechanics
- Define prestige currency types, generation, and usage
- Design prestige upgrade trees (all upgrades, costs, effects)
- Specify what persists across prestige resets (detailed list)
- Create prestige progression model

#### 7.2 Duplicate Card System Design
- Choose system (Experience vs Fusion vs Hybrid) with rationale
- Design card leveling system (if XP): XP requirements, stat growth
- Design scrap/crafting system (if scraps): conversion rates, crafting costs
- Define max level caps and prestige interactions
- Create duplicate handling flow diagram

#### 7.3 Progression Curves & Scaling
- Define difficulty scaling formulas for combat
- Design pack cost scaling (formulas, examples)
- Create resource generation scaling formulas
- Establish prestige bonus magnitude (formulas, examples)
- Create progression curve spreadsheet (show scaling over time)

### Deliverables
- Complete prestige system specification
- Duplicate handling system design document
- Progression curves spreadsheet/model
- Prestige upgrade tree diagram
- Scaling formulas reference

---

## Session 8: Integration Testing & Multi-Tier Validation

### Goals
- Extend simulator to support multi-tier progression
- Test complete game loops across tier transitions
- Validate cross-tier interactions and balance
- Test prestige and class switching mechanics

### Tasks

#### 8.1 Multi-Tier Simulator Extension
- Extend Session 2 simulator to support multiple tiers
  - Arcane → Elemental tier transitions
  - Cross-tier deck building (mixed Arcane + Elemental decks)
  - Elemental essence conversion mechanics
  - Class-specific deck limit profiles
- Implement prestige reset mechanics
  - Reset simulation state
  - Apply prestige bonuses
  - Class switching

#### 8.2 Cross-Tier Interaction Validation
- Test cross-tier synergies in simulation
  - Arcane cards supporting elemental decks
  - Cross-tier generator interactions
  - Multi-tier combo effects
- Validate resource conversion flows
  - Arcane → Elemental essence conversion rates
  - Balance between tier progression
- Test class switching strategies
  - Different class paths (Fire, Water, Earth, Air)
  - Deck composition differences per class

#### 8.3 Full Game Loop Balance Testing
- Simulate progression through Arcane → first elemental tier
  - Time to first prestige
  - Resource accumulation rates across tiers
  - Pack purchasing patterns
- Test deck composition strategies
  - Pure Arcane vs hybrid decks
  - Generator vs combat ratios at different stages
- Validate progression curves
  - Difficulty scaling across tiers
  - Pack cost scaling across tiers
  - Enemy scaling for elemental content
- Identify balance issues and iterate
  - Document required adjustments
  - Test adjustments in simulator
  - Create balance reference document

### Deliverables
- Multi-tier gameplay simulator (extends Session 2 simulator)
- Cross-tier interaction validation report
- Balance testing results and adjustments
- Complete multi-tier gameplay loop documentation
- Final design specifications document with validated numbers

---

## Session 9+: Content Design & Expansion

### Future Sessions
- Design additional classes and tier paths
- Create more card examples for each tier
- Design special packs and events
- Create achievement/milestone systems
- Design tutorial and onboarding flow

---

## Key Principles for Sessions

1. **Design Depth Over Code**: Focus on complete specifications that make implementation straightforward
2. **Simulation Over Prototyping**: Use spreadsheets/calculators to validate mechanics before building
3. **Component Interaction**: Always consider how systems affect each other
4. **Formulas & Numbers**: Specify exact formulas, rates, and scaling rather than vague descriptions
5. **Testable Models**: Create tools that can validate design decisions
6. **Theme Integration**: Theme decisions guide all naming and flavor text

---

## Deliverable Types

### Design Documents
- Detailed specifications (complete enough for implementation)
- System interaction diagrams
- Flow charts and decision trees
- Reference documents

### Simulation Tools
- Spreadsheets (resource generation, combat, progression)
- Calculators (deck power, economy flow)
- Models (gameplay loops, balance testing)
- Test cases and examples

### Updated Documentation
- Updated DESIGN.md with final decisions
- Complete specification documents
- Design reference library

---

## Notes

- Each session produces both design documents AND simulation/validation tools
- Design specs should be detailed enough that implementation is straightforward
- Simulation tools help validate mechanics before building
- Focus on most critical systems first (Gray tier, classes, resource generation)
- Balance between theoretical design and practical simulation

---

**Document Version:** 1.0  
**Last Updated:** Initial Roadmap Creation  
**Status:** Ready for Execution

