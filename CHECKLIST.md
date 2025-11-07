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
  - [x] Define baseline numbers (Part B: generator rates, shard drops, pack costs, enemy stats) - CORRECTED for stacking
  - [x] Design starter deck (Part C: 8 starter cards with concrete stats) - COMPLETE

- [x] **1.3B** Baseline Numbers (COMPLETE - Corrected for Stacking)
  - [x] Establish resource generation baseline rates (generator cards, shard drops)
  - [x] Define pack pricing model with scaling formulas (40,000 × 2.5^n)
  - [x] Create economy flow model (Essence from generators, Shards from victories)
  - [x] Calculate timing and pacing for first 30 minutes
  - [x] Define enemy health scaling and attack values
  - [x] Establish combat card stat ranges
  - [x] CORRECTED: Generator stacking mechanic (every draw adds, including duplicates)
  - [x] Validated complete 30-minute timeline with stacking accumulation

- [x] **1.3C**: Starter Deck (COMPLETE)
  - [x] Design 8 simple starter cards (using baseline numbers from 1.3B)
  - [x] Specify exact starter deck composition (cards, stats, costs)
  - [x] All flat values, no complex mechanics
  - [x] 3 generator types: Rate (+2/sec), Burst (+150 flat), Hybrid (+1/sec + 12/6)
  - [x] 5 combat cards: Pure specialists, generalists, various balance points
  - [x] Design philosophy: Different strategies, not power levels
  - [x] Guaranteed cards for first 2 packs (deferred to Session 2)
  - [x] Validate deck against first 30 minutes experience (conceptual validation done, math validation awaits simulator)

## Session 2: Card System Design & Specifications

- [x] **2.0** Gameplay Simulator (Foundation)
  - [x] Build basic combat simulator (card draw, power accumulation, enemy intervals)
  - [x] Implement generator mechanics (rate, burst, hybrid, stacking)
  - [x] Implement combat mechanics (power accumulation, enemy scaling, victory/defeat)
  - [x] Validate baseline mechanics ("bad player" baseline with starter deck only)
  - [x] Create simulation output/visualization (timeline, deck analysis, balance metrics)

- [x] **2.0.1** Combat Progression Design (DESIGN SESSION - Added post-Task 2.0)
  - [x] Resolve enemy health scaling formula (linear: `20 + (n-1) × 65.8`)
  - [x] Design boss encounter system (mini-bosses at 50, 100; major boss at 150)
  - [x] Define death loop mechanics (keep resources, respawn, iterate)
  - [x] Define multi-loop progression expectations (3-6 loops to beat first boss)
  - [x] Clarify death loop vs prestige distinction (prestige deferred to Session 7)
  - [x] Update DESIGN.md with finalized combat progression system (Version 1.8)

- [ ] **2.0.2** Live Terminal Simulation View
  - [ ] Implement live terminal display with Rich library
  - [ ] Create event player system (consumes simulation events in real-time)
  - [ ] Implement speed controls (1x, 2x, 5x, 10x) via keyboard 1-4
  - [ ] Implement pause/resume functionality (Space bar)
  - [ ] Implement step-through mode (advance one event at a time when paused)
  - [ ] Display zones: card draw highlight, event log, status bars
  - [ ] Auto-pause on pack milestones and boss encounters
  - [ ] Post-simulation summary screen with replay option
  - [ ] Add `sim live` or `sim combat --live` CLI command
  - [ ] Test with starter deck simulation (30 minutes)

- [ ] **2.1** Pack Card Design (15-20 cards for Packs 1-3)
  - [ ] Define card rarity levels (answer question 7) with stat differences
  - [ ] Design Pack 1 guaranteed cards (5 cards: 2 generators, 2 combat, 1 utility)
    - [ ] Introduce conditional bonuses ("If drawn in first 5 seconds...")
    - [ ] Simple synergies ("If you have 3+ Arcane cards...")
    - [ ] Better generators (+3, +4 Essence/sec)
  - [ ] Design Pack 2 guaranteed cards (5 cards: 1 generator, 3 combat, 1 rare synergy)
    - [ ] Introduce multiplier generator (Current rate × Y seconds)
    - [ ] Order-dependent effects ("Next card gets +50%")
    - [ ] First Rare card with combo mechanics
  - [ ] Design 5-10 Pack 3+ random pool cards for Arcane tier
    - [ ] Deck manipulation ("Draw extra card", "Shuffle deck")
    - [ ] State-based effects ("Lasts until reshuffle")
    - [ ] Higher power level cards (Rare/Epic)
  - [ ] Create complete card template/stats structure
  - [ ] Define card leveling progression curves
  - [ ] Specify card text format and ability descriptions
  - [ ] Validate card examples against visual-style-guide.md (layout, text length, stats fit)

- [ ] **2.2** Card Interaction Specifications
  - [ ] Define trigger chains (exact conditions and effects)
  - [ ] Specify conditional abilities ("If X, then Y" mechanics)
  - [ ] Design combo requirements (card combinations and effects)
  - [ ] Create interaction matrix (which cards interact and how)
  - [ ] Specify order-dependent mechanics (sequencing rules)
  - [ ] Define state management (what persists, what resets)

- [ ] **2.3** Generator Card Pattern Specifications
  - [ ] Rate Generators: +X Essence/sec when drawn (scales with level)
  - [ ] Burst Generators: +X flat Essence when drawn (scales with level)
  - [ ] Hybrid Generators: +X Essence/sec + combat stats (balanced scaling)
  - [ ] Multiplier Generators: +(Current rate × Y seconds) Essence (scales with accumulated rate)
  - [ ] Conditional Generators: +X Essence/sec if condition met (higher rates, conditional)
  - [ ] Define generation formulas and scaling with card level

- [ ] **2.4** Combat Card Pattern Specifications
  - [ ] Pure Specialists: High attack OR high defense, no other stats
  - [ ] Generalists: Balanced attack and defense
  - [ ] Conditional Combat: Bonus stats if conditions met ("If drawn early...", "If 3+ cards...")
  - [ ] Order-Dependent Combat: Modifies other cards ("Next card gets +X%", "Previous card triggers...")
  - [ ] Combo Combat: Requires multiple cards for full effect
  - [ ] Define combat formulas, defense mechanics, and scaling with card level

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

## Session 8: Integration Testing & Multi-Tier Validation

- [ ] **8.1** Multi-Tier Simulator Extension
  - [ ] Extend Session 2 simulator to support multiple tiers
  - [ ] Implement Arcane → Elemental tier transitions
  - [ ] Implement cross-tier deck building (mixed Arcane + Elemental)
  - [ ] Implement elemental essence conversion mechanics
  - [ ] Implement class-specific deck limit profiles
  - [ ] Implement prestige reset mechanics and class switching

- [ ] **8.2** Cross-Tier Interaction Validation
  - [ ] Test cross-tier synergies (Arcane + Elemental)
  - [ ] Validate resource conversion flows (Arcane → Elemental)
  - [ ] Test class switching strategies (Fire, Water, Earth, Air paths)
  - [ ] Validate balance between tier progression

- [ ] **8.3** Full Game Loop Balance Testing
  - [ ] Simulate progression through Arcane → first elemental tier
  - [ ] Test deck composition strategies (pure vs hybrid, ratios)
  - [ ] Validate progression curves (difficulty, packs, enemies across tiers)
  - [ ] Identify balance issues and iterate
  - [ ] Document adjustments and create balance reference

## Session 9+: Content Design & Expansion

- [ ] Design additional classes and tier paths
- [ ] Create more card examples for each tier
- [ ] Design special packs and events
- [ ] Create achievement/milestone systems
- [ ] Design tutorial and onboarding flow

---

**Usage:** Check off items as you complete them. Each numbered item (1.1, 1.2, etc.) corresponds to a major task in ROADMAP.md.

