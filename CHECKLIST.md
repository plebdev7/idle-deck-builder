# Idle Deck Builder - Task Checklist

**Completed Sessions Archive:** [.archive/CHECKLIST-completed-sessions.md](.archive/CHECKLIST-completed-sessions.md)  
**Archived:** Session 1 (Tasks 1.1 through 1.3C) - Foundational design work

---

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

- [x] **2.0.2** Live Terminal Simulation View
  - [x] Implement live terminal display with Rich library
  - [x] Create event player system (consumes simulation events in real-time)
  - [x] Implement speed controls (1x, 2x, 5x, 10x) via keyboard 1-4
  - [x] Implement pause/resume functionality (Space bar)
  - [x] Implement step-through mode (advance one event at a time when paused)
  - [x] Display zones: card draw highlight, event log, status bars
  - [x] Auto-pause on pack milestones and boss encounters
  - [x] Post-simulation summary screen with replay option
  - [x] Add `sim live` CLI command
  - [x] Test with starter deck simulation (validated with 1-min test)
  - [x] Cross-platform support (Windows via msvcrt, Unix via termios)

- [x] **2.0.3** Combat System Redesign (DESIGN SESSION - CRITICAL) - **COMPLETE** (2025-11-07 22:00:00)
  - **Part A: Combat Mechanics Specification** ✅ COMPLETE
    - [x] Design combat tick system (1.0 second per tick, ATK - DEF damage)
    - [x] Design player HP system (100 HP start, shard upgrades only, no auto-heal)
    - [x] Specify stat reset mechanics (ATK/DEF reset per enemy, essence rate persists)
    - [x] Create combat flow examples (tick-by-tick Enemy 50 walkthrough)
    - [x] Document damage formulas and defense mechanics (flat reduction)
    - [x] Specify deck cycling (continuous with 1s reshuffle cooldown, 8-card minimum)
  - **Part B: Death & Respawn System** ✅ COMPLETE
    - [x] Define death conditions (HP = 0, no timeout)
    - [x] Specify death consequences (stats reset, essence persists)
    - [x] Integrate with death loop system (Session 2.0.1)
    - [x] Design death screen and feedback (celebratory tone, resource display)
    - [x] Document respawn mechanics (Enemy 1, full HP restore, keep resources)
    - [x] Design class switching on death
  - **Part C: Balance & Scaling** ✅ COMPLETE
    - [x] Calculate actual combat durations with continuous cycling
    - [x] Validate 30-minute target = Enemy 50 → ADJUSTED to Enemy 60 (Enemy 50 at ~23 min)
    - [x] Design HP upgrade costs (50/75/100/125/150 shards for +10 HP, Tier 1)
    - [x] Rebalance enemy HP → NEW: Act-based step function (120/130/140 per enemy by Act)
    - [x] Update card stat ranges → Starter deck validated, Pack 1-3 ready for design
    - [x] Validate pack affordability timing → UNCHANGED (essence independent of combat)
    - [x] Create balance spreadsheet → Documented in `.cursor/log/balance/`
  - **Part D: Documentation** ✅ COMPLETE
    - [x] Update DESIGN.md combat system section (Version 1.9)
    - [x] Update enemy attack scaling (Enemy 50 first attacker)
    - [x] Update Mini-Boss #1 specification (defense tutorial)
    - [x] Update baseline numbers section (new HP formula, combat durations)
    - [x] Update first 30 minutes experience (new milestones)
    - [x] Finalize DESIGN.md Version 1.9
    - [x] Document changelog (comprehensive Version 1.9 entry)
    - [x] Mark superseded sections

- [x] **2.0.4** Implement New Combat System - **COMPLETE** (2025-11-07 23:30:00)
  - [x] Reimplement combat.py with combat-over-time mechanics
  - [x] Add Player class with HP system (current HP, max HP, scaling)
  - [x] Add death/respawn system (reset stats, keep essence)
  - [x] Update simulation loop for combat ticks
  - [x] Add combat duration tracking and metrics
  - [x] Test combat resolution with new mechanics
  - [x] Validate stat reset behavior (resets per enemy, essence persists)

- [x] **2.0.4a** Fix CLI Bugs (sim combat, sim live) - **COMPLETE** (2025-11-07 23:02:47)
  - [x] Document bugs found in sim combat and sim live
  - [x] Fix display issues in live viewer
  - [x] Fix error in sim combat command (chart generation KeyError)
  - [x] Fix enemy HP always showing 0 in live viewer
  - [x] Fix desynchronized card draw and combat ticks (combined into single 1s tick)
  - [x] Test both commands thoroughly
  - [x] Validate edge cases (death events, stat resets, HP display)

- [x] **2.0.4b** Live Sim Bug Fixes and Improvements - **COMPLETE** (2025-11-07 23:15:39)
  - [x] Fix enemy health in Recent Activity always showing 0 HP
  - [x] Fix enemy health bar always showing out of 1
  - [x] Add tower mage health bar to match enemy health bar
  - [x] Add deck shuffle indicator in card display and recent activity
  - [x] Test live simulation viewer with all fixes
  - [x] Validate visual consistency and user experience

- [x] **2.0.5** Update Validation System - **COMPLETE** (2025-11-07 23:52:04)
  - [x] Update validation targets for new combat timing
  - [x] Add HP system validation tests
  - [x] Add death system validation tests
  - [x] Test boss encounters with new combat mechanics
  - [x] Validate combat duration targets
  - [x] Revalidate baseline numbers (pack timing may shift)
  - [x] Document new validation expectations
  - **Result:** 50% pass rate (8/16 checks), found boss HP bug and baseline shifts

- [x] **2.0.6** Design Document Review & Baseline Adjustment - **COMPLETE** (2025-11-08 00:30:15)
  - [x] Review DESIGN.md for arithmetic inconsistencies
  - [x] Fix Enemy 50 boss HP issue (7,670 vs 9,768 claimed)
    - [x] Investigate formula vs claimed values
    - [x] Choose fix approach (Option A: update docs to match implementation)
    - [x] Update DESIGN.md with correct values (7,670 HP for Enemy 50)
    - [x] Update validation targets (corrected HP values)
  - [x] Adjust baseline targets for combat-over-time reality
    - [x] Lower essence rate expectations (wider tolerance ±20%)
    - [x] Adjust card draw rate (60 → 52 cards/min)
    - [x] Confirm enemy defeat rate (2.5 → 2.0 enemies/min)
    - [x] Widen combat duration tolerances for early enemies
  - [x] Cross-check all formulas in DESIGN.md
    - [x] Enemy HP scaling (all acts) ✅ Correct
    - [x] Attack scaling progression ✅ Correct
    - [x] Boss multipliers (50, 100, 150) - Fixed Enemy 50/150 HP
    - [x] Shard rewards formulas ✅ Correct
    - [x] Pack cost progression ✅ Correct
  - [x] Validate all claimed milestone timings ✅ Correct
    - [x] Enemy 50 @ 23 min ✅
    - [x] Pack affordability times ✅
    - [x] Combat duration estimates - Widened tolerances
  - [x] Update validation to 100% pass rate ✅ **16/16 PASSED**
  - [x] Document all corrections in DESIGN.md changelog (Version 2.0.1)

- [ ] **2.1** Pack Card Design (15-20 cards for Packs 1-3)
  - **Phase 1: Foundation Research (DESIGN SESSION)**
    - [x] **2.1.1** Define card rarity system (4-tier: Common/Rare/Epic/Legendary) - ✅ COMPLETE
      - [x] Specify rarity stat multipliers and ranges (20%/25%/30%/35% scaling)
      - [x] Define rarity drop rates from packs (Arcane 70/20/8/2, Elemental 50/30/15/5)
      - [x] Document ultra-rare/unique card philosophy (future expansion)
      - [x] Decide: No level caps (infinite leveling with exponential costs)
      - [x] Decide: Power + Complexity hybrid (higher rarity = stronger + more complex)
      - [x] Quick leveling outline (XP-based, duplicates = XP)

    - [x] **2.1.2** Finalize pack card power curve - ✅ COMPLETE (2025-11-09)
      - [x] Create stat point system and card data structure (12-card deck limit)
      - [x] Define conversion rates (ATK/DEF/Essence/Healing)
      - [x] Update Essence Burst (150 → 250) and Mystic Shield (18 → 20)
      - [x] Create JSON schema for cards and balance config

    - [x] **2.1.2A** - ✅ COMPLETE 
      - [x] Identify Enemy that should start dealing damage (Enemy 20 - 4 minute tutorial)
      - [x] Implement card data in simulator (JSON-based)
      - [x] Validate stat ranges per pack and rarity

    - [x] **2.1.2B** - ✅ COMPLETE
      - [x] Evaluate balance issues with enemy ATK value vs. Player DEF value scaling
      - [x] Consider enemy getting ATK/DEF per tick rather than static values
      - [x] Design per-tick scaling formulas (graduated by Act, bosses 2× multiplier)
      - [x] Add enemy_scaling config to balance-config.json
      - [x] Update progression.md with per-tick scaling system
      - [x] Update combat-system.md with per-tick damage formulas

    - [x] **2.1.2C** Update Simulator & Validation for Data Ownership Model - ✅ COMPLETE (2025-11-09)
      - [x] Fix live simulator - not using config scaling
      - [x] UI Tweaks - enemy health bar red, player/enemy ATK/DEF on separate lines
      - [x] Update validation system to check data ownership model
        - [x] Verify simulator loads ALL values from game-data/*.json (no hardcoded values)
        - [x] Validate formulas match design docs (e.g., HP scaling formula)
        - [x] Cross-check game-data values don't contradict design formulas
        - [x] Add validation warnings for missing cross-references (_design_spec fields)
      - [x] Document validation approach for future balance changes
      - [x] Fixed enemy ATK/DEF per-tick scaling display in live viewer

    - [x] **2.1.3** Design card leveling concept - ✅ COMPLETE (2025-11-09)
      - [x] Define duplicate card handling (direct duplicate counting, no XP middleman)
      - [x] Specify level-up mechanics and requirements (N-1 duplicates for Level N)
      - [x] Design stat scaling formulas per level (20% multiplicative, all rarities)
      - [x] Define max level caps and progression curve (Level 10 cap, awakening to 20)
  - **Phase 2: Mechanic Design Research (DESIGN SESSION)**
    - [x] **2.1.4** Research conditional mechanics - ✅ COMPLETE (2025-11-10)
      - [x] Evaluate condition types (timing, composition, state-based)
      - [x] Identify "fun to build around" vs "too random/confusing"
      - [x] Define testable conditions for Pack 1-3
      - [x] Create conditional ability templates
      - [x] Create condition coefficient balancing system
      - [x] Define combat UI tracking requirements
    - [x] **2.1.5** Research sequencing & order-dependent mechanics - ✅ COMPLETE (2025-11-12)
      - [x] Design "next card" and "previous card" tracking
      - [x] Specify combo trigger chains
      - [x] Define state persistence rules (reshuffle, enemy, death)
    - [x] **2.1.6** Create card data structure & text format - ✅ COMPLETE (2025-11-11)
      - [x] Define complete card template (all fields)
      - [x] Specify stat notation format
      - [x] Create ability description templates with keywords
      - [x] Validate text fits card layout (3 lines max, 12px font)
  - **Phase 3: Card Content Design (DESIGN SESSION)**
    - [x] **2.1.7** Design Pack 1 guaranteed cards - ✅ COMPLETE (2025-11-11)
      - [x] Design 5 guaranteed cards (4 Commons + 1 Rare)
      - [x] Introduce tradeoffs (3 cards with negative effects)
      - [x] First conditional card (HP < 50%, coefficient 0.5)
      - [x] First healing card in game
      - [x] Validate all stat budgets per rarity
      - [x] Create game-data/cards-pack1.json
      - [x] Update card-system.md with Pack 1 specifications
    - [ ] **2.1.8** Design Pack 2 guaranteed cards
      - [ ] Design 5 guaranteed cards (3 Commons + 2 Rares)
      - [ ] Introduce sequencing mechanics ("If previous card...")
      - [ ] Add cycle position conditions ("If first 3 cards this cycle")
      - [ ] Validate stat budgets per rarity
      - [ ] Create game-data/cards-pack2.json
      - [ ] Update card-system.md with Pack 2 specifications
    - [ ] **2.1.9** Design Pack 3 guaranteed cards
      - [ ] Design 5 guaranteed cards (2 Commons + 2 Rares + 1 Epic)
      - [ ] Introduce complex conditionals (AND/OR, multiple thresholds)
      - [ ] Validate stat budgets per rarity
      - [ ] Create game-data/cards-pack3.json
      - [ ] Update card-system.md with Pack 3 specifications
  - **Phase 4: Validation & Documentation**
    - [ ] **2.1.10** Validate all cards against design constraints
      - [ ] Check against visual-style-guide.md (layout, text length, stats fit)
      - [ ] Verify power curve progression (Pack 1 < Pack 2 < Pack 3)
      - [ ] Confirm mechanical complexity curve (simple → moderate → complex)
      - [ ] Validate deterministic packs teach core mechanics
    - [ ] **2.1.11** Update DESIGN.md and card-system.md
      - [ ] Add rarity system specification
      - [ ] Add card leveling system design
      - [ ] Document all 15-20 pack cards with full stats
      - [ ] Update pack contents and guaranteed card lists
      - [ ] Add card data structure specification
  - **Phase 5: Implementation (if needed)**
    - [ ] **2.1.12** Implement new card mechanics in simulator
      - [ ] Add conditional trigger system
      - [ ] Add sequencing/order-dependent effect tracking
      - [ ] Add state persistence management
      - [ ] Add deck manipulation mechanics
      - [ ] Add simplified combat UI tracking items
    - [ ] **2.1.13** Create and test all new cards
      - [ ] Test all new pack cards in simulator
      - [ ] Create deck variation for pack 1 cards
      - [ ] Create deck variation for pack 1 + 2 cards
      - [ ] Create several deck variations for pack 1 + 2 + 3 cards
      - [ ] Confirm simulator runs for all variations
    - [ ] **2.1.14** Review and update validation targets
      - [ ] Validate balance and progression targets
      - [ ] Validate "bad player" progression
      - [ ] Define and validate "good player" progression

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

