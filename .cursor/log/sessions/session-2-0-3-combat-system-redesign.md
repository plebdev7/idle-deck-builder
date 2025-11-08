# Session 2.0.3 - Combat System Redesign (Parts A & B)

**Date Started:** 2025-11-07 21:29:40  
**Status:** IN PROGRESS (Parts A & B Complete, Parts C & D Pending)  
**Session Type:** Design Session (CRITICAL - Blocks Task 2.1)  
**Related Tasks:** ROADMAP Session 2.0.3, CHECKLIST Task 2.0.3

---

## Session Overview

**Purpose:** Redesign combat from instant-resolution to Trimps-style combat-over-time model with player HP system and death mechanics.

**Problem Identified:** Current combat design accumulates attack/defense that resolves instantly. No actual "combat" occurs - just threshold checks. Every enemy dies in one tick.

**Solution:** Combat-over-time with:
- Attack/Defense as rates (damage per second)
- Combat ticks at 1-second intervals
- Player HP system (can die mid-combat)
- Stats reset per enemy, essence rate persists
- Continuous deck cycling with reshuffle cooldown

---

## Part A: Combat Mechanics Specification ✅ COMPLETE

### Combat Tick System

**Tick Rate:** 1.0 second per tick
- Clean alignment with card draw rate (1 card/sec)
- Simple mental model for players
- Easy damage calculations

**Damage Formulas:**
- Player damage dealt per tick: `max(Player_Attack - Enemy_Defense, 0)`
- Player damage taken per tick: `max(Enemy_Attack - Player_Defense, 0)`
- No minimum damage - perfect defense = 0 damage
- Cards drawn mid-fight break stalemates naturally

**Defense Mechanics:**
- Flat damage reduction (Attack - Defense)
- Defense can completely negate damage (reduces to 0)
- No percentage reduction or complex armor systems

**Design Rationale:**
- Simple, predictable calculations
- Defense directly counters attack
- Strategic depth through timing (when defense cards are drawn)

### Player HP System

**Starting HP:** 100 HP
- Fixed baseline for all players
- Clean round number

**HP Scaling:**
- ❌ No automatic HP growth per enemy
- ❌ No automatic HP growth per pack
- ✅ Shard upgrades: Spend shards for permanent max HP increases
- ✅ Card mechanics: Cards can temporarily boost max HP, heal, or add HP regen

**HP Recovery:**
- ❌ No automatic healing between enemies
- ❌ No healing after victories
- ✅ Full heal only on death/respawn
- ✅ Healing via card mechanics during run (instant heal, HP regen)

**Design Rationale:**
- HP is a precious, depleting resource
- Creates "how far can you go?" tension
- Death is inevitable without healing strategy
- Makes healing cards valuable
- Shard upgrades provide meaningful permanent progression

### Deck Size & Reshuffle Mechanics

**Deck Size Constraints:**
- **Minimum:** 8 cards (prevents tiny deck exploit)
- **Maximum:** Determined by active class (varies by rarity)
- Example: Fire Apprentice = 15 max, Geomancer = 18 max

**Reshuffle Cooldown:**
- **1 second cooldown** after deck exhausts
- Applies to all deck sizes equally
- Creates slight advantage for larger decks:
  - 8-card deck: 8 draw + 1 cooldown = 9s cycle (11% downtime)
  - 15-card deck: 15 draw + 1 cooldown = 16s cycle (6% downtime)

**Continuous Cycling Mechanic:**
- Deck cycles continuously during combat
- Stats accumulate with each cycle
- Example:
  - Cycle 1: 0 → 62 ATK
  - Cycle 2: 62 → 124 ATK (added another 62)
  - Cycle 3: 124 → 186 ATK (added another 62)
  - Power grows exponentially during fight

**Design Rationale:**
- Prevents tiny deck exploit (accelerating stats too fast)
- Encourages larger decks (less downtime %)
- Creates interesting ramp-up dynamics in combat
- Longer fights = more cycles = overwhelming power eventually

### Stat Reset Mechanics

**When Enemy Dies:**
- ✅ Player Attack → Reset to 0
- ✅ Player Defense → Reset to 0
- ✅ Essence Rate → **PERSISTS** (carries forward)
- ✅ HP → **NO HEAL** (damage carries forward)
- ✅ Accumulated Essence → **PERSISTS**

**When Player Dies:**
- ✅ Player Attack → Reset to 0
- ✅ Player Defense → Reset to 0
- ✅ Essence Rate → Reset to 0
- ✅ Current HP → **Full heal to max HP**
- ✅ Max HP → Based on permanent shard upgrades only
- ✅ Accumulated Essence → **PERSISTS** (critical for death loop)
- ✅ Enemy Progress → Reset to Enemy 1
- ✅ Card Collection → **PERSISTS**
- ✅ Deck Composition → **PERSISTS**

**Strategic Implications:**
- Each enemy fight starts from zero combat stats
- Faster card draw = faster stat buildup
- HP depletes across enemies (no healing)
- Death spiral is intentional gameplay
- Death loop is core progression mechanic

---

## Part B: Death & Respawn System ✅ COMPLETE

### Death Conditions

**Primary Condition:** HP reaches 0 during combat
- Can occur at any tick
- Can occur during card draw or reshuffle cooldown
- Instant death, no "saving throw"

**No Timeout Deaths:**
- Combat continues indefinitely until victory or death
- Stalemates shouldn't occur (continuous card draws = always gaining stats)

### Death Consequences

**What Resets on Death:**
1. Combat stats (ATK/DEF) → 0
2. Essence generation rate → 0
3. Current HP → Full heal to max HP
4. Enemy progress → Back to Enemy 1

**What Persists Through Death:**
1. Accumulated essence (KEY for progression)
2. Card collection (all cards owned)
3. Current deck composition
4. Permanent upgrades (shard purchases)
5. Max HP (from permanent shard upgrades)
6. Class selection (but can switch on death)

### Death Screen Design

**Death Screen Shows:**
```
═══════════════════════════════════════
         DEFEATED AT ENEMY 47
═══════════════════════════════════════

 Progress: 47/50 to Mini-Boss #1
 
 This Run:
   Essence Earned:     32,450
   Shards Earned:      127
   Time Alive:         14m 23s
   
 Total Resources:
   Total Essence:      68,900
   Total Shards:       283
   
═══════════════════════════════════════
   Your deck grows stronger with
   each attempt. Spend your resources
   and try again!
═══════════════════════════════════════

 [View Collection]  [Spend Shards]  [Continue]
```

**Tone & Messaging:**
- Celebratory of progress made (not punishing)
- Shows what you earned this run
- Shows total resources available
- Encourages spending and improving
- Positive reinforcement: "Your deck grows stronger"

### Class Switching on Death

**Mechanic:**
- Death screen offers class switch option (if you own other class cards)
- "Switch Class" button opens class selection modal
- Select new class → respawn with that class's deck limits
- Deck composition adjusts to new limits automatically

**UI Flow:**
```
Death Screen 
  → [Switch Class] 
  → Class Selection Modal
  → Select new class 
  → Deck Adjustment Screen (if needed)
  → [Continue] 
  → Respawn at Enemy 1 with new class
```

### Respawn Mechanics

**On Continue:**
1. Stats reset (0 ATK, 0 DEF, 0 Essence/sec)
2. HP restored to full (based on permanent max HP)
3. Enemy counter resets to Enemy 1
4. Combat begins immediately
5. Essence and shards still in inventory (ready to spend)

**Respawn Location:**
- Always Enemy 1
- No checkpoints or mid-run respawns
- Each death = full loop restart

### Integration with Death Loop Design

**Aligns with Session 2.0.1:**

Original death loop (Session 2.0.1):
- Loop 1: Reach Enemy 90-100, die, earn ~50k essence
- Loop 2: Buy Pack 1, reach Enemy 110-130
- Loops 3-5: Iterate until beat Enemy 150

**Updated with new combat system:**
- Loop 1: Reach Enemy 50 (Mini-Boss), die, earn ~40k essence
- Loop 2: Buy Pack 1, reach Enemy 75-85, die
- Loop 3: Buy Packs 2-3, reach Enemy 100 (Mini-Boss #2), die
- Loop 4-5: Optimize deck, reach Enemy 150 (Major Boss)
- Loop 6-7: Iterate, beat Enemy 150

**Progression Incentives:**
1. Spend essence on packs → Get better cards
2. Spend shards on upgrades → Permanent HP increases, attack/defense boosts
3. Switch class (if desired) → Try different strategy
4. Optimize deck composition → Better ATK/DEF balance

**Death as Core Gameplay:**
- Not punishment, but natural rhythm
- Expected and normal
- Core progression loop
- Each death = learn + improve + retry

---

## Strategic Implications of New Combat System

### 1. HP as Precious Resource
- No healing between enemies
- Must survive entire run on starting HP (unless healing cards)
- Death is inevitable without healing strategy
- Creates "how far can you go?" gameplay

### 2. Defense Becomes Critical
- Must draw defense cards FAST or take heavy damage
- Defense > Enemy Attack = invulnerable
- Defense < Enemy Attack = death spiral
- Card draw order matters enormously

### 3. Combat Ramp-Up Dynamics
- Early fight: Vulnerable (low stats)
- Mid fight: Ramping (stats accumulating)
- Late fight: Overwhelming (massive stats from multiple cycles)
- Longer fights = more cycles = godlike power eventually

### 4. Death Spirals Are Intentional
- Low HP → need to survive longer → need more defense
- Might not have enough defense cards
- Creates tension and "oh no" moments
- Death loop is expected progression

### 5. Card Design Space Opens Up
- Instant heal cards (restore X HP)
- HP regen cards (+Y HP per tick for Z seconds)
- Max HP boost cards (temp +50 max HP this run)
- Defense-focused strategies become viable
- "Lifesteal" cards (deal damage, heal for %)
- Shield/barrier cards (temporary defense boost)

### 6. Shard Upgrades Gain Value
- Permanent max HP increases = run further each loop
- Permanent attack/defense boosts = faster kills, less damage
- Each death loop, spend shards to grow stronger
- Long-term progression curve through upgrades

---

## Key Design Decisions Summary

| Topic | Decision | Rationale |
|-------|----------|-----------|
| **Tick Rate** | 1.0 second | Matches card draw, simple calculations |
| **Damage Formula** | ATK - DEF, no minimum | Cards break stalemates, allows perfect defense |
| **Defense Type** | Flat reduction | Simple, predictable, strategic |
| **Starting HP** | 100 HP | Clean number, room for scaling |
| **HP Scaling** | Shard upgrades only | No automatic growth, player-controlled |
| **HP Recovery** | Death only | No healing between enemies, cards provide healing |
| **Deck Minimum** | 8 cards | Prevents tiny deck exploit |
| **Reshuffle Cooldown** | 1 second | Slight bonus for larger decks |
| **Stat Reset** | Per enemy (ATK/DEF), persist (Essence rate) | Strategic separation |
| **Death Penalty** | Reset to Enemy 1, keep resources | Death loop progression |

---

## Combat Flow Example (Complete)

**Enemy 50: 3,246 HP, 10 ATK**
**Player: 100 HP, 8-card starter deck (62 ATK, 54 DEF per cycle)**

```
CYCLE 1 (Ticks 0-7: Drawing cards)
Tick 0: 0 ATK, 0 DEF | Enemy: 3,246 HP | Player: 100 HP
  - Damage dealt: 0 | Damage taken: 10 | Player: 90 HP

Tick 1: 20 ATK, 0 DEF (Arcane Bolt drawn)
  - Damage dealt: 20 | Damage taken: 10 | Player: 80 HP | Enemy: 3,226 HP

Tick 2: 20 ATK, 18 DEF (Mystic Shield drawn)
  - Damage dealt: 20 | Damage taken: 0 (defense working!) | Player: 80 HP | Enemy: 3,206 HP

Tick 3: 20 ATK, 18 DEF (Arcane Conduit - rate gen, no combat stats)
  - Damage dealt: 20 | Damage taken: 0 | Enemy: 3,186 HP

Tick 4: 35 ATK, 23 DEF (Power Strike drawn)
  - Damage dealt: 35 | Damage taken: 0 | Enemy: 3,151 HP

Tick 5: 40 ATK, 38 DEF (Stalwart Guard drawn)
  - Damage dealt: 40 | Damage taken: 0 | Enemy: 3,111 HP

Tick 6: 50 ATK, 38 DEF (Balanced Strike drawn)
  - Damage dealt: 50 | Damage taken: 0 | Enemy: 3,061 HP

Tick 7: 50 ATK, 38 DEF (Essence Burst - burst gen, no combat stats)
  - Damage dealt: 50 | Damage taken: 0 | Enemy: 3,011 HP

Tick 8: 62 ATK, 54 DEF (Combat Siphon drawn - full deck drawn)
  - Damage dealt: 62 | Damage taken: 0 | Enemy: 2,949 HP

After Cycle 1:
  - Stats: 62 ATK, 54 DEF
  - Enemy: 2,949 HP
  - Player: 80 HP (took 20 damage before defense)

Tick 8: [DECK EXHAUSTED - RESHUFFLE COOLDOWN (1 second)]
  - Stats persist: 62 ATK, 54 DEF
  - Damage dealt: 62 | Damage taken: 0
  - Enemy: 2,887 HP

CYCLE 2 (Ticks 9-16: Drawing cards again)
Tick 9: 82 ATK, 54 DEF (Arcane Bolt +20 ATK)
  - Damage: 82 | Enemy: 2,805 HP

Tick 10: 82 ATK, 72 DEF (Mystic Shield +18 DEF)
  - Damage: 82 | Enemy: 2,723 HP

[... cards continue drawing ...]

Tick 16: 124 ATK, 108 DEF (full cycle complete)
  - Enemy: ~2,140 HP
  - Player: 80 HP (stable)

Tick 16: [RESHUFFLE COOLDOWN]
  - Damage: 124 | Enemy: 2,016 HP

CYCLE 3 (Ticks 17-24)
Stats grow to: 186 ATK, 162 DEF
Enemy: ~770 HP after cycle

CYCLE 4 (Ticks 25-29)
Stats grow to: 248+ ATK
Enemy defeated around Tick 28

Total Combat Time: ~28-29 seconds
Final Player HP: 80/100 (survived with 20 HP lost early)
```

**Key Observations:**
- Early vulnerability (first 2 ticks before defense)
- Defense stabilizes quickly
- Damage accelerates with each cycle
- Combat duration reasonable (~30 seconds)
- HP loss only in vulnerable early phase

---

## Updated Progression Structure

### 30-Minute Target: Enemy 50 (TENTATIVE)

With combat-over-time, each enemy takes longer to defeat. Target is **Enemy 50 as 30-minute milestone**, but this is FLEXIBLE pending Part C balance calculations.

### Revised Attack Scaling (BRILLIANT INSIGHT)

**New Design:** Enemy 50 (Mini-Boss #1) is FIRST enemy with attack

**Phase 1: Safe Learning (Enemies 1-49)**
- Attack: **0**
- Purpose: Learn mechanics without death pressure
- HP never depletes
- Pure offense optimization

**Phase 2: Mini-Boss #1 "Defense Tutorial" (Enemy 50)**
- HP: 4,220 (1.3× multiplier)
- Attack: **10** (FIRST damage dealer!)
- Purpose:
  - Teaches defense matters
  - "Oh no, I'm taking damage!" moment
  - Still survivable (100 HP vs 10 ATK)
  - Forces defensive card strategy

**Phase 3: Gradual Scaling (Enemies 51-99)**
- Formula: `10 + (enemy_number - 51) × 0.3`
- Enemy 51: 10 ATK → Enemy 99: ~24 ATK
- Progressive difficulty introduction

**Phase 4: Mini-Boss #2 "First Real Wall" (Enemy 100)**
- HP: 9,809 (1.5× multiplier)
- Attack: **30** (1.3× regular Enemy 100)
- Significant threat, Pack 1 likely needed

**Phase 5: Challenge Zone (Enemies 101-149)**
- Formula: `25 + (enemy_number - 101) × 0.6`
- Enemy 101: 25 ATK → Enemy 149: 54 ATK
- HP management becomes critical

**Phase 6: Major Boss (Enemy 150)**
- HP: 17,438 (≈2× multiplier)
- Attack: **80** (1.5× regular Enemy 149)
- Major milestone, multiple loops expected

**Design Rationale:**
- Natural tutorial arc (30 min safe, then first damage)
- Clear "before/after" moment at Mini-Boss #1
- Boss encounters every ~50 enemies (consistent rhythm)
- Each boss has distinct identity and purpose

---

## Parts C & D: TODO

### Part C: Balance & Scaling (NOT STARTED)

**Topics to Address:**
1. **Combat Duration Targets**
   - Calculate actual combat time per enemy with new system
   - Validate 30-minute target = Enemy 50
   - Adjust if needed (could be Enemy 75 or 100)
   - Account for continuous cycling acceleration

2. **HP Scaling Details**
   - Shard cost for HP upgrades (e.g., 100 shards = +25 max HP?)
   - HP scaling curve (how much HP needed at different stages?)
   - Balance HP vs attack/defense upgrade priorities

3. **Enemy Rebalancing**
   - Validate current HP formula: `20 + (n-1) × 65.8`
   - May need adjustment for combat duration
   - Boss multipliers (1.3×, 1.5×, 2×) still appropriate?
   - Attack scaling formulas finalized

4. **Card Stat Ranges**
   - Validate starter deck (62 ATK, 54 DEF appropriate?)
   - Pack 1-3 card stat ranges
   - Generator card essence rates (still valid?)
   - Balance combat duration vs essence generation tradeoff

5. **Validation Targets**
   - Pack affordability timing with new combat
   - Essence accumulation rates with combat duration
   - Enemy defeat rates (enemies/minute)
   - Death loop progression (how far per loop?)

**Deliverables Needed:**
- Combat duration spreadsheet with calculations
- Enemy scaling validation
- Card stat range guidelines
- Updated baseline numbers
- New validation targets for simulator

### Part D: Documentation (NOT STARTED)

**Topics to Address:**
1. **Update DESIGN.md Combat System Section**
   - Replace instant-resolution with combat-over-time
   - Document stat reset mechanics
   - Specify HP system and death mechanics
   - Version 1.9

2. **Update Baseline Numbers Section**
   - New combat duration expectations
   - Revised enemy scaling if needed
   - Updated card stat ranges
   - Pack affordability timing

3. **Update First 30 Minutes Experience**
   - How death fits into first session
   - Do players die in first 30 minutes?
   - Enemy 50 as milestone instead of 150
   - Tutorial death at Enemy 50 vs survive it

4. **Mark Superseded Sections**
   - Old combat mechanics (Session 1.2)
   - Flag what changed and why
   - Cross-reference to Session 2.0.3
   - Changelog documentation

**Deliverables Needed:**
- Updated DESIGN.md (Version 1.9)
- Changelog documenting combat redesign
- Cross-references to superseded sections
- Updated progression timeline

---

## Critical Questions for Part C

These questions must be answered to complete balance calculations:

1. **Actual Combat Duration:** How long does Enemy 50 REALLY take with continuous cycling?
   - Need to calculate average damage per tick during ramp
   - Account for exponential growth from cycling
   - Validate 30-minute target

2. **HP Upgrade Costs:** What should shard upgrades cost?
   - 100 shards → +25 max HP?
   - 50 shards → +10 max HP?
   - Scaling costs (first upgrade cheap, later expensive)?

3. **Boss Difficulty:** Are boss HP multipliers still appropriate?
   - 1.3× for Mini-Boss #1 (Enemy 50)
   - 1.5× for Mini-Boss #2 (Enemy 100)
   - 2× for Major Boss (Enemy 150)
   - OR do these need adjustment with new combat?

4. **First Death Experience:** Should players die in first 30 minutes?
   - Option A: Survive to Enemy 50, no deaths in session 1
   - Option B: Die before Enemy 50, learn death loop early
   - Option C: Enemy 50 boss kills unprepared players (tutorial death)

5. **Pack Affordability:** Does pack timing change with combat duration?
   - Pack 1 still ~8 minutes?
   - Pack 2 still ~16 minutes?
   - Pack 3 still ~26 minutes?
   - OR does combat duration delay these?

6. **Starter Deck Balance:** Are starter deck stats appropriate?
   - 62 ATK total (after full deck drawn)
   - 54 DEF total
   - OR need adjustment for new combat model?

---

## Implementation Plan (After Parts C & D Complete)

### Task 2.0.4: Implement New Combat System (New Task)

**Scope:**
1. Reimplement `combat.py` with combat-over-time system
2. Add `Player` class with HP system
3. Add death/respawn mechanics
4. Update simulation loop for combat ticks
5. Add reshuffle cooldown tracking
6. Revalidate baseline numbers against new system

**Estimated Time:** 2-3 hours implementation + 1-2 hours validation

### Task 2.0.5: Update Validation System (New Task)

**Scope:**
1. Update validation targets for new combat timing
2. Add HP system validation
3. Add death system validation
4. Test boss encounters with new combat
5. Validate combat duration targets
6. Revalidate all 8 baseline checks

**Estimated Time:** 1-2 hours

### Then: Proceed to Task 2.1 (Pack Card Design)

With new combat system in place, can design pack cards with:
- Appropriate attack/defense ranges
- HP-based utility cards (healing, shields, max HP boosts)
- Combat duration modifiers (attack speed cards?)
- Death prevention mechanics (revive cards?)
- HP regen cards (X HP per tick for Y seconds)

---

## Session Completion Status

**Parts Completed:**
- ✅ Part A: Combat Mechanics Specification (COMPLETE)
- ✅ Part B: Death & Respawn System (COMPLETE)
- ⏳ Part C: Balance & Scaling (NOT STARTED)
- ⏳ Part D: Documentation (NOT STARTED)

**Estimated Time Remaining:**
- Part C: 60-90 minutes (balance calculations, validation)
- Part D: 30-45 minutes (documentation updates)
- Total: 90-135 minutes (~1.5-2 hours)

**Next Steps:**
1. Complete Part C: Balance & Scaling
   - Calculate combat durations with spreadsheet
   - Validate 30-minute target
   - Finalize enemy and card stat ranges
   - Create new validation targets

2. Complete Part D: Documentation
   - Update DESIGN.md (Version 1.9)
   - Update first 30 minutes section
   - Mark superseded sections
   - Document changelog

3. Create Tasks 2.0.4 and 2.0.5 in CHECKLIST.md

4. Implement new combat system in simulator

5. Proceed to Task 2.1 (Pack Card Design)

---

## Files Modified This Session

- None yet (documentation pending Parts C & D completion)

## Files To Be Modified

**Next Session (Parts C & D):**
- `DESIGN.md` (Version 1.8 → 1.9)
- `CHECKLIST.md` (mark 2.0.3 partial progress, add 2.0.4 and 2.0.5)
- `ROADMAP.md` (if timeline changes)
- `.cursor/log/sessions/session-2-0-3-combat-system-redesign.md` (this file, final update)

**Implementation Phase (Tasks 2.0.4 & 2.0.5):**
- `simulator/core/combat.py` (complete rewrite)
- `simulator/core/cards.py` (if needed for reshuffle cooldown)
- `simulator/core/deck.py` (if needed for cycling mechanics)
- `simulator/analysis/validation.py` (new validation targets)
- `tests/test_combat.py` (test new combat system)

---

## Key Insights & Design Philosophy

**New Core Principle Added:**
> "Combat Duration Matters" - Longer fights = more deck cycles = more essence generated, but more risk of HP depletion and death. Balance offense (fast kills) vs defense (survival) vs generators (economy).

**Design Philosophy Reinforced:**
1. **Deck Building as Core Strategy** - Combat mechanics make deck composition critical
2. **Passive Play with Strategic Engagement** - Combat automated, outcomes depend on deck
3. **Death as Progression** - Death feels natural, not punishing; core gameplay loop
4. **Resource Generation Strategy** - Generators vs combat cards creates meaningful tradeoff
5. **HP Management Strategy** - New layer: HP as depleting resource across run

**What Makes This Design Work:**
- Simple mechanics (1-second ticks, ATK - DEF damage)
- Deep strategy (card draw order, deck composition, HP management)
- Clear failure state (HP = 0)
- Natural progression (death loop with resource retention)
- Meaningful choices (offense vs defense vs economy)
- Emergent gameplay (ramp-up dynamics, death spirals, healing strategies)

---

---

## Part C: Balance & Scaling ✅ COMPLETE (2025-11-07 22:00:00)

### Combat Duration Calculations

**Findings:**
- Current HP scaling (65.8 per enemy): Enemy 50 at 16.85 minutes (TOO FAST)
- Target: Enemy 50 at ~30 minutes

**Solution: Act-Based Step Function**

**NEW Enemy HP Formula:**
- **Act 1 (1-50):** `HP = 20 + (n-1) × 120`
- **Act 2 (51-100):** `HP = 6,000 + (n-51) × 130`
- **Act 3 (101-150):** `HP = 12,500 + (n-101) × 140`

**Boss HP:**
- Enemy 50: 9,768 HP (1.3× multiplier, ~23-minute milestone)
- Enemy 100: 18,555 HP (1.5× multiplier)
- Enemy 150: 38,680 HP (2.0× multiplier)

**Step Function Design:**
- Post-boss enemies easier than boss but harder than pre-boss
- Enemy 51 (6,000 HP) < Boss 50 (9,768 HP) but > Enemy 49 (5,780 HP)
- Creates "breathing room" after boss victories
- Escalating challenge: HP per enemy increases (120→130→140)

**HP Upgrade System:**
- Tier 1: 50/75/100/125/150 shards for +10 HP each (500 shards total for +50 HP)
- ~600-700 shards earned by Enemy 50
- Death loop: Upgrade HP between loops for longer runs

**Combat Duration Validation:**
- Enemy 1: ~2s
- Enemy 10: ~17s
- Enemy 50: ~47s (boss)
- Enemy 50 reached at ~23 minutes (close to 30-min target)
- Enemy 60 reached at ~30 minutes (alternate milestone)
- Player death at Enemy 67 (~35 minutes with 100 HP)

**Pack Affordability:** UNCHANGED (essence generation independent of combat duration)

**Balance Documents:**
- `.cursor/log/balance/part-c-findings.md`
- `.cursor/log/balance/part-c-summary.md`
- `.cursor/log/balance/final-hp-formula.md`
- `.cursor/log/balance/combat-duration-calculator.py`

---

## Part D: Documentation ✅ COMPLETE (2025-11-07 22:00:00)

### DESIGN.md Updates

**Sections Updated:**
1. ✅ "Combat Progression & Enemy Scaling" - Act-based HP formula
2. ✅ "Boss Encounter System" - Updated boss HP values (9,768 / 18,555 / 38,680)
3. ✅ "Player HP System" - Added HP Upgrade System details
4. ✅ "Combat Duration" - Finalized combat times and milestones
5. ✅ "Baseline Numbers Reference" - Updated enemy stats, shard accumulation
6. ✅ "Validated Pacing" - Finalized milestones (Enemy 50 at 23 min, Enemy 60 at 30 min)
7. ✅ "Multi-Loop Progression Expectations" - Updated loop targets and total time
8. ✅ "Document Changelog" - Comprehensive Version 1.9 entry

**Version 1.9 Status:** COMPLETE (no longer PARTIAL)

**CHECKLIST.md Updates:**
- ✅ Task 2.0.3 marked complete with all parts A-D finalized
- ✅ Key outcomes documented

---

## Session Completion Summary

**Status:** ✅ **COMPLETE** - All Parts A-D Finalized

**Duration:** 
- Part A & B: 2025-11-07 21:29:40
- Part C & D: 2025-11-07 22:00:00

**What Was Delivered:**

**Part A - Combat Mechanics:**
- Combat tick system (1.0s per tick)
- Player HP system (100 HP start, shard upgrades)
- Continuous deck cycling (1s reshuffle cooldown)
- Stat reset mechanics (ATK/DEF per enemy, essence persists)
- Deck minimum (8 cards)

**Part B - Death & Respawn:**
- Death conditions (HP = 0)
- Respawn mechanics (Enemy 1, full HP, keep resources)
- Death screen design (celebratory tone)
- Class switching on death

**Part C - Balance & Scaling:**
- Act-based HP formula (120/130/140 per enemy)
- Boss HP finalized (9,768 / 18,555 / 38,680)
- HP upgrade system (50-150 shards per +10 HP)
- Combat duration validation (~23 min to Enemy 50)
- Step function design (post-boss breathing room)

**Part D - Documentation:**
- DESIGN.md Version 1.9 finalized
- All combat sections updated
- Baseline numbers updated
- Multi-loop progression updated
- Changelog comprehensive

**Key Design Decisions:**
1. ✅ Act-based step function for enemy HP (approved by user)
2. ✅ Post-boss enemies easier than boss (approved by user)
3. ✅ Enemy 50 at ~23 minutes (close to 30-min target, acceptable)
4. ✅ HP upgrade system designed (shard spending)
5. ✅ Combat duration validated (starter deck baseline)

**Blocking Status:** UNBLOCKED
- Task 2.1 (Pack Card Design) can now proceed
- Task 2.0.4 (Implementation) can proceed

**Next Steps:**
1. Task 2.0.4: Implement new combat system in simulator
2. Task 2.0.5: Update validation system for new mechanics
3. Task 2.1: Design Pack 1-3 cards with new balance parameters

---

**End of Session Log**

**Status:** COMPLETE - Ready for implementation
**Priority:** Cleared - No longer blocking
**Session Log Maintained By:** AI Assistant
**Timestamp:** 2025-11-07 22:00:00

---

## Continuation Guide for Parts C & D (ARCHIVED - COMPLETED)

### Quick Context Refresh

**What We've Decided (Parts A & B):**
1. Combat ticks at 1.0 second intervals
2. Damage = ATK - DEF per tick (no minimum)
3. Player starts with 100 HP, no auto-healing, no auto-scaling
4. HP only heals on death/respawn
5. Shard upgrades for permanent max HP increases
6. Deck cycles continuously with 1s reshuffle cooldown
7. Stats reset per enemy (ATK/DEF), essence rate persists
8. Enemy 50 is first attacker (10 ATK) at ~30-minute mark (tentative)
9. Deck minimum: 8 cards (prevents exploit)
10. Death = respawn at Enemy 1, keep all resources

**What We Haven't Decided (Parts C & D):**
- Exact combat durations with continuous cycling
- Whether Enemy 50 is truly the 30-minute mark (need calculations)
- HP upgrade costs (shards → max HP increases)
- Whether enemy HP formula needs adjustment
- Card stat ranges for new combat model
- Pack affordability timing with combat duration
- Complete baseline numbers update

### Part C: Balance & Scaling - Action Items

**Step 1: Calculate Combat Duration (Critical)**

Build spreadsheet or script to calculate:
- Average damage per tick during stat ramp-up
- Account for continuous cycling (stats grow exponentially)
- Example: 8-card deck cycling every 9 seconds (8 draw + 1 cooldown)

**Formula to test:**
```
Cycle 1: 0 → 62 ATK over 8 ticks
Cycle 2: 62 → 124 ATK over 8 ticks  
Cycle 3: 124 → 186 ATK over 8 ticks
...

Average damage per cycle needs calculation
Total time to defeat enemy = Enemy HP / Average Damage Rate
```

**Step 2: Validate 30-Minute Target**

Calculate total time to reach Enemy 50:
- Sum of combat durations for Enemies 1-50
- Account for faster early enemies, slower late enemies
- Check if it equals ~30 minutes
- If not, adjust target (could be Enemy 40, 60, 75, etc.)

**Step 3: Design HP Upgrade Costs**

Answer:
- Starting max HP: 100 (confirmed)
- First upgrade cost: 50 shards → +25 max HP?
- Scaling: Linear (50, 100, 150...) or exponential (50, 100, 200...)?
- How much HP needed at Enemy 50? Enemy 100? Enemy 150?
- Balance against shard accumulation rate

**Step 4: Rebalance Enemy Stats (If Needed)**

Check if current formulas work:
- HP formula: `20 + (n-1) × 65.8` - Still appropriate?
- Attack scaling: Enemy 50 = 10 ATK - Still appropriate?
- Boss multipliers: 1.3×, 1.5×, 2× - Still appropriate?

Adjust if combat durations don't align with goals.

**Step 5: Update Card Stat Ranges**

Validate:
- Starter deck: 62 ATK, 54 DEF total - Appropriate?
- Does starter deck defeat Enemy 50 in reasonable time?
- Does starter deck survive Enemy 50's 10 ATK?
- Pack 1-3 stat ranges: Need adjustment for new combat?

**Deliverable: Balance Spreadsheet**
- Combat duration per enemy (1-150)
- Cumulative time to reach each enemy
- HP upgrade progression
- Card stat requirements per tier

### Part D: Documentation - Action Items

**Step 1: Update Baseline Numbers Section**

In DESIGN.md, update "Baseline Numbers Reference":
- Combat duration expectations (X seconds per enemy)
- 30-minute target (Enemy X, based on Part C)
- Pack affordability timing (may shift with combat duration)
- Shard accumulation rates
- HP upgrade costs

**Step 2: Update First 30 Minutes Experience**

In DESIGN.md, revise "First 30 Minutes Experience":
- Do players die in first 30 minutes? (Probably not, 0 attack until Enemy 50)
- Milestone: Enemy 50 boss as "first damage" moment
- Does player beat Enemy 50 or die to it?
- Update minute-by-minute timeline if target changes

**Step 3: Update Multi-Loop Progression**

In DESIGN.md, revise death loop expectations:
- Loop 1: Reach Enemy X (based on Part C), die, spend resources
- Loop 2-5: Updated progression targets
- Total time to beat Enemy 150 (recalculate)

**Step 4: Finalize Changelog**

Update Version 1.9 changelog:
- Change from "PARTIAL" to "COMPLETE"
- Add Part C decisions (combat durations, balance)
- Add Part D updates (baseline numbers, progression)
- Update status line

**Step 5: Update Document Version**

At end of DESIGN.md:
- Change "1.9 (PARTIAL)" → "1.9"
- Update status to "Ready for Task 2.0.4 (Implementation)"

**Deliverable: Complete DESIGN.md Version 1.9**
- All combat system specifications finalized
- All affected sections updated
- Ready for implementation

### Key Questions to Answer in Part C

1. **What is the ACTUAL 30-minute target?** (Enemy 40? 50? 60?)
2. **Do combat durations feel right?** (Too fast? Too slow?)
3. **How much HP is needed at each milestone?** (50? 100? 150 enemies)
4. **What should HP upgrades cost?** (Shard costs and HP gains)
5. **Do enemy stats need adjustment?** (HP or attack scaling changes)
6. **Are starter deck stats appropriate?** (Can beat Enemy 50?)

### Tools Needed for Part C

**Option A: Spreadsheet**
- Google Sheets or Excel
- Columns: Enemy #, HP, ATK, Combat Duration, Cumulative Time
- Formulas for damage ramp-up calculation
- Charts showing progression curves

**Option B: Python Script**
- Simulate combat with actual formulas
- Account for deck cycling, stat accumulation
- Output combat duration per enemy
- Validate against 30-minute target

**Option C: Use Existing Simulator**
- Modify Task 2.0 simulator to track combat duration
- Run 30-minute simulation
- See how far starter deck gets
- Extract timing data

**Recommendation:** Option C (use existing simulator) for speed and accuracy.

### Estimated Time for Parts C & D

**Part C: 60-90 minutes**
- 30 min: Calculate combat durations
- 15 min: Validate 30-minute target
- 15 min: Design HP upgrades
- 15 min: Validate enemy stats
- 15 min: Document balance decisions

**Part D: 30-45 minutes**
- 15 min: Update baseline numbers
- 10 min: Update first 30 minutes section
- 10 min: Update multi-loop progression
- 5 min: Finalize changelog and version

**Total: 90-135 minutes (~1.5-2 hours)**

Can be done in one session or split across 2-3 shorter sessions.

### Success Criteria for Completion

Parts C & D are complete when:

1. ✅ Combat duration calculated for all enemies 1-150
2. ✅ 30-minute target validated and finalized (Enemy X)
3. ✅ HP upgrade costs designed (shard cost → HP gain)
4. ✅ Enemy stats validated (HP/ATK formulas appropriate)
5. ✅ Card stat ranges validated (starter deck works)
6. ✅ Baseline numbers section updated in DESIGN.md
7. ✅ First 30 minutes section updated in DESIGN.md
8. ✅ Multi-loop progression updated in DESIGN.md
9. ✅ Changelog finalized (Version 1.9 complete)
10. ✅ Document version updated (no longer "PARTIAL")
11. ✅ Ready to implement (Task 2.0.4)
12. ✅ Ready to design pack cards (Task 2.1)

### Files to Update in Parts C & D

**Part C (Balance Work):**
- Create new file: `.cursor/log/balance/combat-duration-calculations.md` or spreadsheet
- Document balance decisions and rationale

**Part D (Documentation):**
- `DESIGN.md` - Multiple sections (baseline numbers, first 30 min, progression, changelog)
- `CHECKLIST.md` - Mark 2.0.3 complete, unblock 2.1
- `ROADMAP.md` - Update if timeline changes significantly
- `.cursor/log/sessions/session-2-0-3-combat-system-redesign.md` - Final update

### What to Tell Future You

**Key Context:**
- This is a FUNDAMENTAL combat redesign
- Old instant-resolution combat is completely replaced
- All balance numbers from Task 2.0 may need adjustment
- Combat duration adds time to everything (pack timing, enemy progress)
- This enables rich card design space (healing, HP regen, shields)

**Critical Decisions Locked In:**
- 1.0 second ticks (not changing)
- 100 HP start (not changing)
- No auto-healing (not changing)
- Continuous cycling with cooldown (not changing)
- Enemy 50 first attacker (not changing)

**Flexible Decisions:**
- Exact 30-minute target (Enemy 40-60 range)
- HP upgrade costs (tunable)
- Enemy HP formula (can adjust if needed)
- Card stat ranges (can adjust if needed)

**Don't Second-Guess:**
- Combat-over-time was the right call (fixes instant-kill problem)
- HP system opens up card design space
- No healing creates strategic tension
- Continuous cycling creates interesting ramp dynamics
- All these decisions reinforce each other well

---

**Ready to Continue!**

When resuming:
1. Read this continuation guide
2. Start with Part C (balance calculations)
3. Move to Part D (documentation updates)
4. Mark task complete in CHECKLIST.md
5. Proceed to Task 2.0.4 (implementation)

**Session Log Complete**




