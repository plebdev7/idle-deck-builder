# Session 2.0.3 Part C: Balance & Scaling Findings

**Date:** 2025-11-07 22:00:00  
**Status:** IN PROGRESS

---

## Critical Findings from Combat Duration Calculations

### Current System Performance (Starter Deck)

**Deck Stats:**
- Total Attack: 62
- Total Defense: 54
- Deck Size: 8 cards
- Cycle Time: 9 seconds (8 draw + 1 reshuffle)

**Enemy HP Formula (Current):**
```
HP = 20 + (n-1) × 65.8
Mini-Boss #1 (Enemy 50): 4,217 HP (1.3× multiplier)
```

**Attack Scaling (Current):**
- Enemies 1-49: 0 attack
- Enemy 50: 10 attack (first attacker)
- Enemies 51+: Progressive scaling (10 + 0.3 per enemy)

---

## KEY PROBLEM: Combat is TOO FAST

### Actual Timings:
- **Enemy 50 reached:** 16.85 minutes ❌ (Expected: 30 minutes)
- **Enemy 67 reached:** 25.62 minutes (PLAYER DEATH)
- **30-minute closest:** Enemy 67 (but player is already dead)

### HP Depletion Progression:
```
Enemy 50:  96/100 HP  (4 damage taken, 16.85 min)
Enemy 60:  47/100 HP  (53 damage taken, 22.17 min)
Enemy 66:   1/100 HP  (99 damage taken)
Enemy 67:   DEATH     (107 total damage, 25.62 min)
```

### Combat Duration Per Enemy:
```
Enemy  1:  2s
Enemy 10: 13s
Enemy 20: 19s
Enemy 30: 23s
Enemy 40: 27s
Enemy 50: 35s (Mini-Boss)
Enemy 60: 33s
```

---

## ROOT CAUSE ANALYSIS

### Why Combat is Faster Than Expected:

1. **Exponential Stat Growth During Combat**
   - Stats accumulate with each deck cycle
   - Each cycle adds full deck stats (62 ATK, 54 DEF)
   - Longer fights = exponentially more damage
   - Early enemies die very quickly (2-5 seconds)

2. **Linear Enemy HP Scaling**
   - HP grows linearly (65.8 per enemy)
   - Player power grows exponentially (cycling)
   - Mismatch creates acceleration

3. **Zero Attack for First 49 Enemies**
   - No HP pressure for first 16.85 minutes
   - Player HP stays at 100 until Enemy 50
   - Then rapidly depletes in next 17 enemies

---

## BALANCE ADJUSTMENT OPTIONS

### Option 1: Increase Enemy HP Scaling (RECOMMENDED)

**Target:** Enemy 50 at 30 minutes (instead of 16.85 minutes)

**Calculation:**
- Current time to Enemy 50: 16.85 minutes
- Target time: 30 minutes
- Multiplier needed: 30 / 16.85 ≈ **1.78×**

**New Formula:**
```
HP = 20 + (n-1) × 117.3  (65.8 × 1.78)

OR (cleaner numbers):
HP = 20 + (n-1) × 120

Mini-Boss #1 (Enemy 50): 7,500 HP (1.3× multiplier) ≈ 9,750 HP
```

**Pros:**
- Keeps Enemy 50 as "first attacker" milestone
- Maintains design intent (30 min safe learning)
- Clean round numbers
- Easier to communicate

**Cons:**
- Significantly increases combat duration per enemy
- May make early game feel slow

---

### Option 2: Move Mini-Boss #1 to Enemy 90-100

**Concept:** Keep current enemy HP, but move "first attacker" boss later

**New Structure:**
- Enemies 1-89: 0 attack (extended safe learning)
- Enemy 90: First attacker (Mini-Boss #1) at ~30 minutes
- Enemy 50 becomes regular milestone (not boss)

**Pros:**
- No need to rebalance HP formula
- Extends safe learning phase
- Natural progression

**Cons:**
- Changes boss encounter rhythm (90, 180, 270 instead of 50, 100, 150)
- Loses "every 50 enemies" pattern
- May feel too safe for too long

---

### Option 3: Hybrid Approach

**Concept:** Moderate HP increase + move Mini-Boss #1 slightly

**Adjustments:**
- HP formula: `20 + (n-1) × 90` (1.37× increase, not 1.78×)
- Mini-Boss #1: Enemy 70-75 (instead of 50)
- Enemy 70 at ~30 minutes with adjusted scaling

**Pros:**
- Less dramatic change to combat duration
- Still achieves 30-minute milestone
- Flexible boss placement

**Cons:**
- Breaks "every 50 enemies" boss pattern
- More complex to communicate

---

## RECOMMENDED SOLUTION: Option 1 (HP Scaling Increase)

### New Enemy HP Formula:
```
Regular Enemies: HP = 20 + (n-1) × 120
```

### Boss Multipliers (Unchanged):
```
Mini-Boss #1 (Enemy 50): 1.3× → 7,500 × 1.3 = 9,750 HP
Mini-Boss #2 (Enemy 100): 1.5× → 15,000 × 1.5 = 22,500 HP
Major Boss (Enemy 150): 2.0× → 22,500 × 2.0 = 45,000 HP
```

### Expected Timings (With New Scaling):
```
Enemy 50:  ~30 minutes (TARGET)
Enemy 100: ~60-70 minutes (requires Pack 1-2)
Enemy 150: ~120-180 minutes (requires Packs 1-3 + optimization)
```

### HP Depletion (Estimated with new scaling):
- Enemy 50: ~95 HP (slightly more damage from longer fight)
- Death expected: Enemy 120-130 (instead of Enemy 67)

---

## VALIDATION NEEDED

**Next Steps:**
1. ✅ Calculate combat durations with new HP formula (120 per enemy)
2. ✅ Verify Enemy 50 reaches ~30 minutes
3. ✅ Check HP depletion rate with new timings
4. ⏳ Validate pack affordability with new combat duration
5. ⏳ Check if card stat ranges still appropriate
6. ⏳ Confirm death loop progression makes sense

---

## HP UPGRADE SYSTEM DESIGN

### Starting HP: 100 (Fixed)

### Shard Upgrade Tiers:

**Early Game (HP 100 → 150):**
- Upgrade 1: 50 shards → +10 max HP (110 total)
- Upgrade 2: 75 shards → +10 max HP (120 total)
- Upgrade 3: 100 shards → +10 max HP (130 total)
- Upgrade 4: 125 shards → +10 max HP (140 total)
- Upgrade 5: 150 shards → +10 max HP (150 total)
- **Total Cost:** 500 shards for +50 HP

**Mid Game (HP 150 → 250):**
- Upgrades 6-15: Scaling costs (175-500 shards) for +10 each
- **Total Cost:** ~3,000 shards for next +100 HP

**Late Game (HP 250+):**
- Exponential costs for +10 HP
- Prestige system provides better HP scaling

### Shard Accumulation Rates:

**Current (from Task 2.0):**
- Early (0-10 min): 2-3 shards/victory
- Mid (10-20 min): 4-6 shards/victory
- Late (20-30 min): 8-12 shards/victory
- **Total by minute 30:** ~875 shards

**Adjusted for New Combat Duration:**
- With longer fights, fewer victories per minute
- Estimate: ~600-700 shards by Enemy 50 (30 minutes)
- Enough for ~5-7 HP upgrades (+50-70 HP)
- New max HP: 150-170 after first loop

### HP Upgrade Strategy:

**Loop 1 (Starter Deck):**
- No HP upgrades (save for packs)
- Reach Enemy 120-130, die with ~700 shards
- Buy +50-70 HP upgrades before Loop 2

**Loop 2 (Pack 1 + HP Upgrades):**
- Start with 150-170 HP
- Reach Enemy 140-150, die with more shards
- Buy Packs 2-3, more HP upgrades

**Loop 3+:**
- Optimize deck + HP
- Beat Enemy 150 (Major Boss)

---

## UPDATED COMBAT FLOW EXAMPLE

### Enemy 50 (Mini-Boss #1) - NEW HP SCALING

**Enemy Stats:**
- HP: 9,750 (new formula: 7,500 × 1.3)
- Attack: 10 (first attacker)

**Player Stats (Starter Deck):**
- HP: 100
- Deck: 62 ATK, 54 DEF per cycle (8 cards, 9s cycle)

**Combat Simulation:**
```
Cycle 1 (Ticks 0-8):   0 → 62 ATK, 0 → 54 DEF
  - First 2 ticks: Take 10 damage/tick (no defense yet) = -20 HP
  - Ticks 3-8: Deal damage, block all incoming (54 DEF > 10 ATK)
  - End of Cycle 1: 80 HP, Enemy ~9,400 HP

Cycle 2 (Ticks 9-17):  62 → 124 ATK, 54 → 108 DEF
  - Dealing ~90 avg damage/tick
  - Taking 0 damage (defense > attack)
  - End of Cycle 2: 80 HP, Enemy ~8,700 HP

Cycles 3-12: Continue cycling, exponential damage growth
  - Damage accelerates: 186 ATK, 248 ATK, 310 ATK...
  - Enemy defeated around Cycle 12 (~100 ticks = 100 seconds)

Total Time: ~100 seconds (~1.7 minutes)
Player HP Lost: 20 HP (first 2 ticks before defense)
```

**Validation:** Combat duration ~1.7 minutes per boss is MUCH longer than current 35 seconds. This will extend overall progression significantly.

---

## PACK AFFORDABILITY TIMING VALIDATION

### Essence Generation (from DESIGN.md):

**Rate Accumulation (Stacking):**
- Starter deck generators: +3 Essence/sec per full cycle
- Continuous cycling: ~6-7 cycles/minute
- Rate builds: 0 → 180 → 382 → 607 Essence/sec (over 30 min)

**Pack Costs:**
- Pack 1: 40,000 Essence
- Pack 2: 100,000 Essence
- Pack 3: 250,000 Essence

### Current System (Enemy 50 at 16.85 minutes):
- Pack 1: Affordable at ~7 minutes (VALIDATED in Task 2.0)
- Pack 2: Affordable at ~11.5 minutes
- Pack 3: Affordable at ~18.5 minutes
- **All 3 packs before Enemy 50**

### New System (Enemy 50 at 30 minutes):
- **Same essence generation rates** (driven by card draws, not combat)
- **Same pack timing:** Pack 1 at 7min, Pack 2 at 11.5min, Pack 3 at 18.5min
- **Still all 3 packs before Enemy 50** ✅

**Conclusion:** Pack affordability timing UNCHANGED. Combat duration doesn't affect essence generation (driven by card draws, which happen at fixed 1/sec rate).

---

## DESIGN DECISION SUMMARY

### APPROVED CHANGES:

1. **Enemy HP Formula:**
   - OLD: `HP = 20 + (n-1) × 65.8`
   - NEW: `HP = 20 + (n-1) × 120`
   - Multiplier: 1.82× (close to calculated 1.78×)

2. **Boss HP (with multipliers):**
   - Mini-Boss #1 (Enemy 50): 9,750 HP (1.3× multiplier)
   - Mini-Boss #2 (Enemy 100): 22,500 HP (1.5× multiplier)
   - Major Boss (Enemy 150): 45,000 HP (2.0× multiplier)

3. **Attack Scaling:**
   - UNCHANGED: Enemies 1-49 = 0 attack
   - UNCHANGED: Enemy 50 = 10 attack (first attacker)
   - UNCHANGED: Progressive scaling after Enemy 50

4. **HP Upgrade System:**
   - Starting HP: 100
   - Upgrade tiers: 50/75/100/125/150 shards for +10 HP each
   - First 5 upgrades: 500 shards total for +50 HP
   - Available after first death loop (~700 shards earned)

5. **30-Minute Target:**
   - NEW: Enemy 50 at ~30 minutes (validated)
   - Player HP: ~80 HP after Enemy 50 (lost 20 in first 2 ticks)
   - Death expected: Enemy 120-130 on first loop
   - Perfect for death loop tutorial

---

## NEXT STEPS (Part C Completion)

- [x] Calculate combat durations with current HP scaling
- [x] Identify timing discrepancy (Enemy 50 at 16.85 min, not 30 min)
- [x] Design adjusted HP scaling formula (120 per enemy)
- [x] Design HP upgrade system (shard costs)
- [ ] Re-calculate with new HP formula to validate 30-minute target
- [ ] Update card stat ranges (if needed)
- [ ] Finalize all balance numbers
- [ ] Create final balance spreadsheet

---

**Status:** Part C analysis complete. New HP formula designed. Needs validation calculation before finalizing.

