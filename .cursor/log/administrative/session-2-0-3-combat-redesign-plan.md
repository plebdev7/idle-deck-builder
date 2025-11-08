# Session 2.0.3 - Combat System Redesign Plan

**Date:** 2025-11-07 20:46:02  
**Purpose:** Plan for redesigning combat from instant-resolution to Trimps-style combat-over-time  
**Priority:** CRITICAL - Blocks Task 2.1 (Pack Card Design)  
**Status:** Planning Phase

---

## Executive Summary

**Problem Identified:** Current combat design has accumulated attack/defense resolve instantly against enemies, creating no actual "combat" - just threshold checks. Every enemy dies in one tick after sufficient accumulation.

**Solution Decided:** Redesign combat to **Trimps-style combat-over-time** model with:
- Attack/Defense as **rates** (damage per second)
- Combat happens over **multiple seconds** with HP depletion
- Player has **HP system** (can die mid-combat)
- Stats **reset per enemy** (essence rate persists)
- Card draws add permanently to rates until enemy defeat/death

**Impact:** This is a **fundamental redesign** affecting:
- Combat resolution mechanics
- Player death system implementation
- Card stat interpretation
- Balance validation targets
- Pack card design (Task 2.1 blocked until this is resolved)

---

## Design Session Overview

### Session Goals

1. **Specify complete Trimps-style combat system**
   - Combat tick mechanics (second-by-second resolution)
   - Player HP system and death conditions
   - Stat reset timing and mechanics
   - Card draw effects during combat

2. **Define player progression through combat**
   - HP scaling per enemy
   - Death consequences (essence retention, stat loss)
   - Respawn mechanics
   - Death loop integration with existing design

3. **Balance combat parameters**
   - Starting player HP
   - HP growth per enemy/pack/prestige
   - Attack/defense scaling needs
   - Combat duration targets (seconds per enemy)

4. **Update all affected systems**
   - Enemy scaling formulas (may need adjustment)
   - Card stat ranges (what's "good" attack/defense now?)
   - Generator vs combat card tradeoffs
   - Victory/defeat conditions

5. **Validate against design principles**
   - Death loop system (Session 2.0.1)
   - First 30 minutes experience (Session 1.3)
   - Boss encounter system (mini-bosses, major boss)
   - Progression expectations (3-6 loops to beat first boss)

---

## Key Mechanic Decisions (Pre-Decided)

### Stat Accumulation & Reset ✅

**Confirmed Mechanic:**
- Cards add to attack/defense **permanently within an enemy encounter**
- Stats **reset to 0** when enemy dies OR when player dies
- **Essence rate persists** across enemies (never resets except on death loop)

**Example Flow:**
```
Enemy 1 spawns
  - Your stats: 0 ATK, 0 DEF, 3 Essence/sec
  - Draw card: +20 ATK → Now 20 ATK, 0 DEF
  - Draw card: +10 DEF → Now 20 ATK, 10 DEF
  - Draw card: +2 Essence/sec → Now 20 ATK, 10 DEF, 5 Essence/sec
  - Combat continues...
  - Enemy dies

Enemy 2 spawns
  - Stats RESET: 0 ATK, 0 DEF (fresh start)
  - Essence rate PERSISTS: 5 Essence/sec (carried over)
  - Draw cards again to rebuild attack/defense...
```

**Strategic Implications:**
- Each enemy fight starts from zero combat stats
- Faster card draw = faster stat buildup = faster victories
- Deck cycling speed becomes critical for combat power
- Generators don't reset, so essence accelerates continuously
- Death wipes both combat stats AND essence rate

---

### Player HP System ✅

**Confirmed Mechanic:**
- Player has HP that depletes during combat
- Reaching 0 HP triggers death
- Death = respawn with reset stats (death loop mechanic)

**To Design:**
- Starting HP value
- HP growth mechanics (per enemy? per pack? prestige?)
- HP recovery between enemies (full heal? partial?)
- HP display and feedback

---

### Combat Over Time ✅

**Confirmed Mechanic:**
- Combat ticks at regular intervals (e.g., every 0.1 seconds)
- Each tick: Deal damage, take damage, check for death
- Cards can be drawn **during** combat, affecting ongoing fight

**To Design:**
- Combat tick rate (0.1s? 1.0s?)
- Damage calculation formulas
- Combat duration targets (how long should enemies take?)
- Visual feedback and pacing

---

## Design Session Structure

### Part A: Combat Mechanics Specification (60-90 minutes)

**Topics:**
1. **Combat Tick System**
   - Tick rate and resolution
   - Damage calculation per tick
   - Defense mechanics (flat reduction? percentage? cap?)

2. **Player HP System**
   - Starting HP (e.g., 100 HP? 1000 HP?)
   - HP scaling with progression
   - HP recovery timing (after each enemy? after each wave?)
   - Max HP vs Current HP

3. **Stat Reset Mechanics**
   - Reset triggers (enemy death, player death)
   - What resets (attack, defense)
   - What persists (essence rate, HP?, accumulated essence)

4. **Combat Flow Example**
   - Walk through complete enemy encounter
   - Show stat changes tick-by-tick
   - Demonstrate card draw effects during combat

**Deliverables:**
- Complete combat flow specification
- Damage calculation formulas
- HP system specification
- State transition diagram

---

### Part B: Death & Respawn System (45-60 minutes)

**Topics:**
1. **Death Conditions**
   - HP reaches 0 during combat
   - Stuck against unkillable enemy (timeout?)

2. **Death Consequences**
   - What resets: Combat stats (ATK/DEF), essence rate, HP
   - What persists: Accumulated essence, cards in collection, deck composition
   - Respawn location (Enemy 1)

3. **Death Loop Integration**
   - Aligns with Session 2.0.1 design (death as progression)
   - Spend essence on packs between deaths
   - Class switching on death (if owns class cards)

4. **Death Feedback**
   - Death screen design
   - Progress indicators ("You reached Enemy 47")
   - Encouragement to improve deck

**Deliverables:**
- Death system specification
- Respawn mechanics
- Death screen design
- Integration with existing death loop design

---

### Part C: Balance & Scaling (60-90 minutes)

**Topics:**
1. **Combat Duration Targets**
   - Early enemies: How many seconds to defeat?
   - Boss enemies: How much longer?
   - Pacing goals (fast vs slow combat feel)

2. **Player HP Scaling**
   - Starting HP baseline
   - Growth per enemy defeated
   - Growth per pack purchased
   - Prestige HP bonuses

3. **Enemy Rebalancing**
   - Current HP formulas still valid?
   - Boss HP multipliers still appropriate?
   - Attack scaling needs adjustment?
   - New validation targets

4. **Card Stat Rebalancing**
   - Starter deck: What attack/defense values now?
   - Pack cards: New stat ranges needed?
   - Generators: Still 25-35% of deck?
   - Combat duration vs essence generation tradeoff

**Deliverables:**
- Balanced combat parameters spreadsheet
- Updated enemy scaling formulas
- Card stat range guidelines
- New baseline validation targets

---

### Part D: DESIGN.md Updates & Documentation (30-45 minutes)

**Topics:**
1. **Update Combat System Section**
   - Replace instant resolution with combat-over-time
   - Document stat reset mechanics
   - Specify HP system

2. **Update Baseline Numbers**
   - New combat duration expectations
   - Revised enemy scaling if needed
   - Updated card stat ranges

3. **Update First 30 Minutes Experience**
   - How does death fit into first session?
   - Do players die in first 30 minutes?
   - Tutorial death at Enemy 150 still valid?

4. **Mark Superseded Sections**
   - Old combat mechanics (Session 1.2 decisions)
   - Flag what changed and why

**Deliverables:**
- Updated DESIGN.md (Version 1.9)
- Changelog documenting combat redesign
- Cross-references to superseded sections

---

## Expected Session Duration

**Total Time:** 3-4 hours

- Part A (Combat Mechanics): 60-90 minutes
- Part B (Death System): 45-60 minutes
- Part C (Balance & Scaling): 60-90 minutes
- Part D (Documentation): 30-45 minutes

**Recommended Approach:** Break into multiple work sessions if needed. Can be done over 2-3 days.

---

## Prerequisites

**Before Starting Session:**
- ✅ Current DESIGN.md reviewed
- ✅ Session 2.0.1 combat progression design reviewed
- ✅ Session 1.3 first 30 minutes experience reviewed
- ✅ Trimps combat mechanics researched (if needed)

**Resources Needed:**
- Spreadsheet for balance calculations
- Combat flow diagram tool (or text-based)
- Example combat scenarios for testing

---

## Success Criteria

**Session is complete when:**
1. ✅ Complete combat tick system specified with formulas
2. ✅ Player HP system fully designed (starting HP, scaling, recovery)
3. ✅ Death/respawn mechanics integrated with death loop design
4. ✅ Combat duration targets established (X seconds per enemy)
5. ✅ Enemy scaling validated against new combat model
6. ✅ Card stat ranges updated for new combat mechanics
7. ✅ DESIGN.md updated with all new specifications
8. ✅ Ready to implement in simulator (Task 2.0.4)
9. ✅ Ready to design pack cards against new combat model (Task 2.1)

---

## Downstream Impacts

### Immediate Impacts (Must Address in Session)

1. **Task 2.0 Simulator** - Requires reimplementation
   - Combat resolution logic completely changes
   - Add player HP tracking
   - Add death/respawn system
   - Revalidate baseline numbers

2. **Task 2.1 Pack Card Design** - BLOCKED until this is done
   - Card stat ranges depend on combat mechanics
   - Can't design combat cards without knowing what stats do
   - Generator vs combat tradeoff changes

3. **Validation Targets** - Need recalculation
   - Combat duration adds time to enemy defeats
   - Essence generation timing may change
   - Pack affordability timing may shift

### Future Impacts (Document, Address Later)

4. **Session 5 Combat System** - Already done, but now superseded
   - Old combat simulation model obsolete
   - New session replaces it

5. **Session 8 Multi-Tier** - HP system per tier?
   - Do different tiers have different HP pools?
   - Cross-tier defense synergies?

6. **Prestige System (Session 7)** - HP as prestige benefit
   - Permanent HP increases
   - Max HP bonuses
   - HP recovery upgrades

---

## Design Questions to Answer

### Critical Questions (Must answer in session)

1. **Combat Tick Rate**
   - 0.1 seconds (10 ticks/sec)? Fine-grained but expensive
   - 1.0 seconds (1 tick/sec)? Matches card draw, simpler
   - 0.5 seconds (2 ticks/sec)? Middle ground

2. **Starting Player HP**
   - 100 HP (small numbers, easy to understand)?
   - 1000 HP (room for growth, bigger numbers)?
   - Dynamic based on deck (sum of defense cards × 10)?

3. **HP Recovery Timing**
   - Full heal after each enemy?
   - Partial heal based on victory time?
   - No heal (HP persistent across enemies)?
   - Only heal on pack purchase or special events?

4. **Defense Mechanic**
   - Flat damage reduction (enemy_attack - your_defense)?
   - Percentage reduction (enemy_attack × (1 - defense_percent))?
   - Cap on reduction (max 90% damage reduction)?
   - Armor + HP (two separate systems)?

5. **Combat Duration Targets**
   - Early enemies (1-10): 3-5 seconds each?
   - Mid enemies (50-100): 10-15 seconds each?
   - Boss enemies (50, 100, 150): 30-60 seconds each?
   - Balance fast progression vs strategic combat

6. **Death Penalty**
   - Reset to Enemy 1 (current design)?
   - Reset to last checkpoint (every 10 enemies)?
   - Lose X% of accumulated essence?
   - Just reset stats (keep progress)?

7. **Starter Deck Balance**
   - Do starter deck stats need adjustment?
   - Should players die in first 30 minutes?
   - What's minimum viable combat stats?

8. **Enemy HP Rebalancing**
   - Current HP values assume instant kills
   - With combat duration, do we need higher/lower HP?
   - Does HP scaling formula change?

### Secondary Questions (Can defer if needed)

9. **HP Display**
   - Show actual HP (523/1000)?
   - Show HP bar only?
   - Show HP percentage?

10. **Critical Hits / Variance**
    - Should damage have variance (RNG)?
    - Or deterministic (same fight = same outcome)?
    - Critical hits as card mechanic later?

11. **Armor Penetration**
    - Do we need armor pen as a stat?
    - Or save for advanced cards (Task 2.2+)?

12. **HP Regeneration**
    - Cards that heal HP?
    - Passive HP regen per second?
    - Or only between-enemy healing?

---

## Implementation Plan (After Design Session)

### Task 2.0.4: Implement New Combat System (New Task)

**Scope:**
1. Reimplement `combat.py` with combat-over-time system
2. Add `Player` class with HP system
3. Add death/respawn mechanics
4. Update simulation loop for combat ticks
5. Revalidate baseline numbers against new system

**Estimated Time:** 2-3 hours implementation + 1-2 hours validation

### Task 2.0.5: Update Validation System (New Task)

**Scope:**
1. Update validation targets for new combat timing
2. Add HP system validation
3. Add death system validation
4. Test boss encounters with new combat

**Estimated Time:** 1-2 hours

### Then: Proceed to Task 2.1 (Pack Card Design)

With new combat system in place, can design pack cards with:
- Appropriate attack/defense ranges
- HP-based utility cards (healing, shields)
- Combat duration modifiers (attack speed?)
- Death prevention mechanics (revive cards?)

---

## Session Execution Checklist

**Pre-Session:**
- [ ] Review current DESIGN.md combat sections
- [ ] Review Session 2.0.1 (death loop design)
- [ ] Review Session 1.3 (first 30 minutes)
- [ ] Prepare spreadsheet for balance calculations
- [ ] Have diagram tool ready (or text-based)

**During Session:**
- [ ] Part A: Specify combat tick mechanics
- [ ] Part A: Design player HP system
- [ ] Part A: Document stat reset rules
- [ ] Part B: Design death conditions and consequences
- [ ] Part B: Integrate with death loop system
- [ ] Part C: Calculate combat duration targets
- [ ] Part C: Rebalance enemy HP and attack
- [ ] Part C: Update card stat ranges
- [ ] Part D: Update DESIGN.md with all changes
- [ ] Part D: Document changelog and rationale

**Post-Session:**
- [ ] Create Task 2.0.4 and 2.0.5 in CHECKLIST.md
- [ ] Log session in `.cursor/log/sessions/`
- [ ] Update ROADMAP.md with new task sequence
- [ ] Brief review of session output before implementation

---

## Key Design Philosophy Reminders

**From DESIGN.md Principles:**
1. **Deck Building as Core Strategy** - Combat mechanics should make deck composition matter
2. **Passive Play with Strategic Engagement** - Combat is automated but outcomes depend on deck
3. **Death as Progression** - Death should feel like natural progression, not punishment
4. **Resource Generation Strategy** - Generators vs combat cards creates meaningful tradeoff

**New Principle to Add:**
5. **Combat Duration Matters** - Longer fights = more cards drawn = more essence generated, but more risk of death

---

## Risks & Mitigations

### Risk: Combat too slow/grindy
**Mitigation:** Set aggressive combat duration targets (5-10 seconds early game)

### Risk: Death too punishing
**Mitigation:** Keep essence accumulation, make respawn immediate, celebrate progress made

### Risk: Balance requires massive rework
**Mitigation:** Start with starter deck baseline, adjust enemy HP to match, iterate

### Risk: Session takes too long
**Mitigation:** Can split into multiple shorter sessions, prioritize critical decisions first

### Risk: Changes invalidate prior design work
**Mitigation:** Document what's superseded, keep what works, be transparent about pivots

---

## Next Steps

1. **Schedule design session** - Block 3-4 hours (or split into 2 sessions)
2. **Gather tools** - Spreadsheet, diagram tools, DESIGN.md open
3. **Execute session** - Work through Parts A-D systematically
4. **Document everything** - Update DESIGN.md, create session log
5. **Create new tasks** - Add 2.0.4 and 2.0.5 to CHECKLIST.md
6. **Implement** - Rewrite combat.py with new system
7. **Validate** - Ensure new combat works as designed
8. **Proceed to Task 2.1** - Design pack cards with confidence

---

**Ready to Begin:** Once you give the go-ahead, we'll start with Part A (Combat Mechanics Specification).

**Estimated Completion:** Session can be completed in 1 focused work session or spread across 2-3 shorter sessions.

---

**End of Plan Document**

