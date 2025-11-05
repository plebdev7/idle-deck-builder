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
- Design concrete card examples that demonstrate all mechanics
- Define complete card data structure and stat systems
- Create card interaction specifications

### Tasks

#### 2.1 Card System Complete Specification
- Define card rarity levels (answer question 7) with stat differences
- Design 15-20 example cards for Gray tier (covering all card types)
- Create complete card template/stats structure (all fields, ranges, formulas)
- Define card leveling progression curves (formulas, examples per level)
- Specify card text format and ability descriptions

#### 2.2 Card Interaction Specifications
- Define trigger chains: exact conditions and effects
- Specify conditional abilities: "If X, then Y" mechanics
- Design combo requirements: card combinations and their effects
- Create interaction matrix showing which cards interact and how

#### 2.3 Card Type Specifications
- **Combat Cards:** damage formulas, defense mechanics, scaling
- **Generator Cards:** generation formulas, scaling with level/deck composition
- **Synergy Cards:** trigger conditions, effect magnitudes
- **Utility Cards:** special effects, edge cases

### Deliverables
- Complete card design document with 15-20 Gray tier examples
- Card data structure specification (all fields, types, ranges)
- Card leveling progression spreadsheet (show stat growth curves)
- Card interaction specification document
- Card type mechanics reference

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

## Session 8: Gameplay Simulation & Integration Testing

### Goals
- Create integrated gameplay simulation
- Test complete game loops
- Validate system interactions and balance

### Tasks

#### 8.1 Integrated Gameplay Simulation
- Create comprehensive gameplay simulator (spreadsheet or simple tool)
- Model complete game loop: pack opening → deck building → combat → resource generation
- Simulate progression through Gray tier and first colored tier
- Test resource flow and economy balance

#### 8.2 System Interaction Validation
- Test cross-tier interactions in simulation
- Validate resource generation vs combat balance
- Test deck composition strategies
- Validate progression curves (time to unlock tiers, classes)

#### 8.3 Balance Testing & Iteration
- Identify balance issues through simulation
- Iterate on formulas and rates
- Document required adjustments
- Create balance reference document

### Deliverables
- Integrated gameplay simulation tool
- System interaction validation report
- Balance testing results and adjustments
- Complete gameplay loop documentation
- Final design specifications document

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

