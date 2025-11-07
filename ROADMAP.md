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

#### 2.0.2 Live Terminal Simulation View
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

#### 2.1 Pack Card Design (15-20 cards for Packs 1-3)
- Define card rarity levels (answer question 7) with stat differences
- **Pack 1 Guaranteed Cards** (5 cards: 2 generators, 2 combat, 1 utility)
  - Introduce conditional bonuses ("If drawn in first 5 seconds...")
  - Simple synergies ("If you have 3+ Arcane cards...")
  - Better generators (+3, +4 Essence/sec)
  - Test in simulator to validate balance
- **Pack 2 Guaranteed Cards** (5 cards: 1 generator, 3 combat, 1 rare synergy)
  - Introduce multiplier generator (Current rate × Y seconds)
  - Order-dependent effects ("Next card gets +50%")
  - First Rare card with combo mechanics
  - Test in simulator to validate sequencing mechanics
- **Pack 3+ Random Pool** (5-10 cards for Arcane tier)
  - Deck manipulation ("Draw extra card", "Shuffle deck")
  - State-based effects ("Lasts until reshuffle")
  - Higher power level cards (Rare/Epic)
  - Test in simulator for balance and interactions
- Create complete card template/stats structure (all fields, ranges, formulas)
- Define card leveling progression curves (formulas, examples per level)
- Specify card text format and ability descriptions
- Validate card examples against visual-style-guide.md (layout, text length, stats fit)

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
- **Live simulation viewer** (terminal-based real-time visualization)
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

