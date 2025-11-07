# Idle Deck Builder - Task Checklist

## Session 1: Design Foundation & Theme

- [x] **1.1** Theme Selection & Story Framework
  - [x] Choose theme (Elemental Magic Tower Defense)
  - [x] Define basic narrative framework (Apprentice mage defending tower from invaders)
  - [x] Name currencies and tiers (Essence system: Arcane, Fire, Water, Earth, Air)
  - [x] Create visual/style direction brief (completed in 1.1A)

- [x] **1.1A** Visual Direction & Style Guide
  - [x] Define color palettes for each tier (exact hex codes)
  - [x] Design icon/symbol style for elements
  - [x] Create card layout mockup (wireframe or text-based)
  - [x] Specify UI color scheme and layout principles
  - [x] Define animation/particle style (if any)
  - [x] Create basic asset list

- [x] **1.2** Critical Design Decisions (Outstanding Questions)
  - [x] Answer Question 1: Class Switching Cost → Prestige-only
  - [x] Answer Question 4: Arcane Tier Combat Role → Unified deck (contributes to colored decks)
  - [x] Answer Question 5: Arcane Essence Currency Model → Universal currency with conversion mechanic
  - [x] Answer Question 9: Deck Size Limits → Fixed with multi-layer constraints (per-tier, per-card)
  - [x] Answer Question 10: Combat Timing → Interval-based with continuous card draw
  - [x] Document decisions in DESIGN.md with rationale

- [x] **1.3** High-Level Experience
  - [x] Define exact first 30 minutes of gameplay (step-by-step, minute-by-minute narrative)
  - [x] Create gameplay flow diagram showing decision points and branches
  - [x] Identify key milestones and progression gates
  - [x] Resolve 7 critical design questions (pack costs, guaranteed cards, defense, economy model, etc.)
  - [ ] Define baseline numbers (Part B: generator rates, shard drops, pack costs, enemy stats)
  - [ ] Design starter deck (Part C: 8 starter cards with concrete stats)

- [ ] **1.3B** Baseline Numbers
  - [ ] Establish resource generation baseline rates (generator cards, shard drops)
  - [ ] Define pack pricing model with scaling formulas (50 × 1.5^n)
  - [ ] Create economy flow model (Essence from generators, Shards from victories)
  - [ ] Calculate timing and pacing for first 30 minutes

- [ ] **1.3C**: Starter Deck
  - [ ] Design 8 simple starter cards (using baseline numbers from 1.3B)
  - [ ] Specify exact starter deck composition (cards, stats, costs)
  - [ ] Design guaranteed cards for first 2 packs
  - [ ] Validate deck against first 30 minutes experience from 1.3

## Session 2: Card System Design & Specifications

- [ ] **2.1** Card System Complete Specification
  - [ ] Define card rarity levels (answer question 7) with stat differences
  - [ ] Design 15-20 example cards for Gray tier
  - [ ] Create complete card template/stats structure
  - [ ] Define card leveling progression curves
  - [ ] Specify card text format and ability descriptions
  - [ ] Validate card examples against visual-style-guide.md (layout, text length, stats fit)

- [ ] **2.2** Card Interaction Specifications
  - [ ] Define trigger chains (exact conditions and effects)
  - [ ] Specify conditional abilities ("If X, then Y" mechanics)
  - [ ] Design combo requirements (card combinations and effects)
  - [ ] Create interaction matrix (which cards interact and how)

- [ ] **2.3** Card Type Specifications
  - [ ] Combat Cards: damage formulas, defense mechanics, scaling
  - [ ] Generator Cards: generation formulas, scaling
  - [ ] Synergy Cards: trigger conditions, effect magnitudes
  - [ ] Utility Cards: special effects, edge cases

## Session 3: Tier & Class System Design

- [ ] **3.1** Tier System Complete Specification
  - [ ] Finalize tier count per class (3-5 tiers)
  - [ ] Design 3 starter class paths (Common classes) with full details
  - [ ] Define exact tier unlock sequence for each class
  - [ ] Specify tier colors and theme-appropriate names
  - [ ] Define passive tier mechanics

- [ ] **3.2** Class System Detailed Design
  - [ ] Define class card structure (stats, abilities, tier unlocks)
  - [ ] Design 3 starter classes (Warrior, Mage, Ranger) with full specs
  - [ ] Specify class switching mechanics
  - [ ] Design class-specific bonuses and synergies
  - [ ] Create class comparison matrix

- [ ] **3.3** Cross-Tier Mechanics Specification
  - [ ] Design cross-tier resource generation formulas
  - [ ] Specify cross-tier synergy examples (concrete card combinations)
  - [ ] Define multi-currency card mechanics
  - [ ] Create resource flow diagram

## Session 4: Resource Generation & Economy Design

- [ ] **4.1** Resource Generation System Specification
  - [ ] Design generator card examples (Pure, Hybrid, Conditional) with exact formulas
  - [ ] Define generation rate formulas (base rate, scaling factors, level multipliers)
  - [ ] Specify deck composition effects on generation
  - [ ] Create generation rate calculator/spreadsheet
  - [ ] Design multi-currency generation cards

- [ ] **4.2** Economy Balance Model
  - [ ] Create pack cost scaling formulas
  - [ ] Design resource generation balance model (generators vs combat cards)
  - [ ] Specify optimal deck composition targets
  - [ ] Create economy flow model (earn → spend → progress)
  - [ ] Design idle generation mechanics (offline rates, caps)

- [ ] **4.3** Generator Card Design Patterns
  - [ ] Pure Generator: exact stats, generation rates, scaling
  - [ ] Hybrid Generator: combat stats + generation, balance formulas
  - [ ] Conditional Generator: trigger conditions, generation rates, scaling
  - [ ] Create generator card examples for each tier

## Session 5: Combat System Design & Simulation

- [ ] **5.1** Combat System Complete Specification
  - [ ] Define combat mechanics (how cards interact in battle)
  - [ ] Specify auto-battle resolution (formula-based or simulation-based)
  - [ ] Design combat timing (continuous, interval-based, event-based)
  - [ ] Create combat flow diagram

- [ ] **5.2** Combat Simulation Model
  - [ ] Create spreadsheet calculator for combat outcomes
  - [ ] Model deck power calculations (how deck composition affects combat)
  - [ ] Design enemy stat scaling formulas
  - [ ] Create combat simulation tool
  - [ ] Test different deck compositions against enemy scaling

- [ ] **5.3** Difficulty & Progression Specification
  - [ ] Define enemy difficulty scaling curves
  - [ ] Specify victory/defeat conditions
  - [ ] Design reward formulas (resources per victory)
  - [ ] Create difficulty progression model

## Session 6: Deck Building System Design

- [ ] **6.1** Deck Building Constraints Specification
  - [ ] Define deck size limits (fixed, variable, point-based) with exact rules
  - [ ] Specify card limits (max copies, rarity restrictions)
  - [ ] Design deck budget system (if point-based)
  - [ ] Create deck validation rules

- [ ] **6.2** Deck Composition Analysis
  - [ ] Create deck composition spreadsheet (analyze generator/combat ratio)
  - [ ] Design synergy detection/analysis tools
  - [ ] Specify optimal deck templates for different strategies
  - [ ] Create deck power calculator

- [ ] **6.3** Deck Building Strategy Documentation
  - [ ] Document resource optimization strategies
  - [ ] Specify synergy building patterns
  - [ ] Design cross-tier composition strategies
  - [ ] Create deck building decision tree

## Session 7: Prestige & Progression Systems Design

- [ ] **7.1** Prestige System Complete Specification
  - [ ] Answer question 6 (prestige reset details) with exact mechanics
  - [ ] Define prestige currency types, generation, and usage
  - [ ] Design prestige upgrade trees (all upgrades, costs, effects)
  - [ ] Specify what persists across prestige resets (detailed list)
  - [ ] Create prestige progression model

- [ ] **7.2** Duplicate Card System Design
  - [ ] Choose system (Experience vs Fusion vs Hybrid) with rationale
  - [ ] Design card leveling system (if XP): XP requirements, stat growth
  - [ ] Design scrap/crafting system (if scraps): conversion rates, crafting costs
  - [ ] Define max level caps and prestige interactions
  - [ ] Create duplicate handling flow diagram

- [ ] **7.3** Progression Curves & Scaling
  - [ ] Define difficulty scaling formulas for combat
  - [ ] Design pack cost scaling (formulas, examples)
  - [ ] Create resource generation scaling formulas
  - [ ] Establish prestige bonus magnitude (formulas, examples)
  - [ ] Create progression curve spreadsheet

## Session 8: Gameplay Simulation & Integration Testing

- [ ] **8.1** Integrated Gameplay Simulation
  - [ ] Create comprehensive gameplay simulator (spreadsheet or simple tool)
  - [ ] Model complete game loop: pack opening → deck building → combat → resource generation
  - [ ] Simulate progression through Gray tier and first colored tier
  - [ ] Test resource flow and economy balance

- [ ] **8.2** System Interaction Validation
  - [ ] Test cross-tier interactions in simulation
  - [ ] Validate resource generation vs combat balance
  - [ ] Test deck composition strategies
  - [ ] Validate progression curves (time to unlock tiers, classes)

- [ ] **8.3** Balance Testing & Iteration
  - [ ] Identify balance issues through simulation
  - [ ] Iterate on formulas and rates
  - [ ] Document required adjustments
  - [ ] Create balance reference document

## Session 9+: Content Design & Expansion

- [ ] Design additional classes and tier paths
- [ ] Create more card examples for each tier
- [ ] Design special packs and events
- [ ] Create achievement/milestone systems
- [ ] Design tutorial and onboarding flow

---

**Usage:** Check off items as you complete them. Each numbered item (1.1, 1.2, etc.) corresponds to a major task in ROADMAP.md.

