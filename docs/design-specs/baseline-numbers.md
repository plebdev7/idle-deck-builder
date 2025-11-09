# Baseline Numbers Reference

**Last Updated:** 2025-11-08  
**Status:** Complete (Session 1.3B, Task 2.0, Session 2.0.3)  
**Parent Document:** [DESIGN.md](../../DESIGN.md)

---

## Core Game Timing

**Authoritative Source:** See [`game-data/balance-config.json`](../../game-data/balance-config.json) for exact timing values used by the simulator and game.

### Card Draw & Combat

- **Card draw speed:** 1.0 second per card (60 cards/minute constant)
- **Enemy arrival:** Every 12 seconds (5 enemies/minute)
- **Combat resolution:** Tick-based (1.0 second per tick)
- **Deck reshuffle cooldown:** 1 second

---

## Generator Card Rates (Essence Generation)

**Authoritative Source:** See [`game-data/cards-starter-deck.json`](../../game-data/cards-starter-deck.json) for starter deck generators. Pack card generators to be defined in future game-data files.

### Mechanic

Every draw of a generator adds to rate (stacks, even duplicates); rate persists until death.

### Starter Deck Generators

See starter deck data file for exact values. Starter deck provides +3 Essence/sec total when all generators drawn.

### Pack Generators (To Be Designed)

Target ranges for pack card generators:
- **Pack 1:** +3 to +4 Essence/sec per draw
- **Pack 2:** +5 Essence/sec per draw
- **Pack 3+ Common:** +2 to +4 per draw
- **Pack 3+ Rare:** +5 to +7 per draw
- **Pack 3+ Epic:** +10+ per draw

### Expected Rate Progression

With starter deck only:
- **Minutes 0-8:** 0 → 180 Essence/sec (from ~120 draws)
- **Minutes 8-17:** 180 → 652 Essence/sec
- **Minutes 17-27:** 652 → 1,252 Essence/sec
- **Minutes 27-30:** 1,252 → 1,500 Essence/sec

---

## Pack Costs (Essence)

**Authoritative Source:** See [`game-data/balance-config.json`](../../game-data/balance-config.json) for exact pack costs and formulas.

### Formula

`40,000 × 2.5^(n-1)`

### Pricing (as of current balance)

- **Pack 1:** 40,000 Essence (minute 8-9)
- **Pack 2:** 100,000 Essence (minute 16-17)
- **Pack 3:** 250,000 Essence (minute 26-27)
- **Pack 4:** 625,000 Essence (minute 32-35, beyond first session)
- **Pack 5+:** 1,562,500+

### Pack Contents

- 5 cards per pack
- First 2 packs: Guaranteed distributions
- Pack 3+: Random by rarity weights

---

## Shard System (Combat Rewards)

**Authoritative Source:** See [`game-data/balance-config.json`](../../game-data/balance-config.json) for exact shard drop rates and upgrade costs.

### Drops per Victory

- **Early (0-10 min):** 2-3 Shards
- **Mid (10-20 min):** 4-6 Shards
- **Late (20-30 min):** 8-12 Shards

### Accumulation

**(Session 2.0.3 Part C - Adjusted for Combat Duration)**

- **Total by Enemy 50 (~23 min):** ~600-700 Shards
- **Total by Enemy 60 (~30 min):** ~700-800 Shards

### Usage Examples (Current Balance)

- **HP upgrades:** 50/75/100/125/150 shards per +10 HP (Tier 1)
- **Card upgrades:** 50-100+ Shards
- **Deck size increase:** 200+ Shards
- **Permanent upgrades:** Variable

---

## Enemy Stats

### ✅ FINALIZED (Session 2.0.3 Part C - Act-Based Scaling)

See [progression.md](progression.md) for complete specifications.

### Quick Reference - HP Scaling

- **Act 1 (1-50):** `HP = 20 + (n-1) × 120`
- **Act 2 (51-100):** `HP = 6,000 + (n-51) × 130`
- **Act 3 (101-150):** `HP = 12,500 + (n-101) × 140`

### Boss HP

- **Mini-Boss #1 (Enemy 50):** 7,670 HP (1.3× multiplier)
- **Mini-Boss #2 (Enemy 100):** 18,555 HP (1.5× multiplier)
- **Major Boss (Enemy 150):** 38,720 HP (2.0× multiplier)

### Attack/Defense Scaling (Per-Tick System)

**Design Philosophy:** Enemies scale per-tick to counter player deck cycling

**Act 1 (Enemies 1-50):**
- ATK per tick: `1.0 + (n-1) × 0.05`
- DEF per tick: `0.5 + (n-1) × 0.025`
- Example: Enemy 1 = 1.0 ATK/tick, Enemy 50 = 3.45 ATK/tick

**Act 2 (Enemies 51-100):**
- ATK per tick: `3.5 + (n-51) × 0.08`
- DEF per tick: `1.75 + (n-51) × 0.04`

**Act 3 (Enemies 101-150):**
- ATK per tick: `7.5 + (n-101) × 0.12`
- DEF per tick: `3.75 + (n-101) × 0.06`

**Bosses:**
- 2× multiplier on per-tick rates

---

## Combat Card Stats

**Authoritative Source:** See [`game-data/cards-starter-deck.json`](../../game-data/cards-starter-deck.json) for exact starter deck stats. Pack card stats to be defined in future game-data files.

### Starter Deck Range

- **Total:** 20-28 stat points (Common rarity range)
- Provides 62 ATK, 56 DEF when all cards drawn

### Pack Cards (To Be Designed)

Target stat point budgets:
- **Pack 1 Cards:** 25-30 stat points
- **Pack 2 Cards:** 35-45 stat points
- **Pack 3+ Rare:** 50-80 total stat points
- **Pack 3+ Epic:** 100-150 total stat points

### Power Accumulation Targets

- **Initial (starter deck):** ~6.9 ATK/tick, ~6.2 DEF/tick
- **After Pack 1:** 10-15 ATK/tick
- **By minute 30:** 20-30 ATK/tick

---

## Deck Composition Guidelines

### Generator Percentage

Stays constant at 25-35% of deck across all stages

### Starter (8 cards)

- **2 Generators (25%)**
- **5 Combat (62.5%)**
- **1 Utility (12.5%)**

### Optimized (20 cards)

- **6-7 Generators (30-35%)**
- **12-13 Combat (60-65%)**
- **1-2 Utility (5-10%)**

---

## Validated Pacing (Starter Deck Only - "Bad Player" Baseline)

### ✅ VALIDATED (Task 2.0 + Session 2.0.3 Part C)

- ✓ Pack 1 affordable at ~7.0 minutes (40,000 Essence)
- ✓ Pack 2 affordable at ~11.5 minutes (100,000 Essence)
- ✓ Pack 3 affordable at ~18.5 minutes (250,000 Essence)
- ✓ Generation rate scales: 0 → 180 → 382 → 607 Essence/sec (starter deck only)
- ✓ Card draw rate: 60 cards/min (1 card/sec)
- ✓ Enemy 50 reached at ~23 minutes (Mini-Boss #1 - First Attacker)
- ✓ Enemy 60 reached at ~30 minutes (alternate milestone)
- ✓ Player death at Enemy 67 (~35 minutes with starter deck, 100 HP)
- ✓ Combat durations: 2s → 17s → 47s (Enemies 1/10/50)

### ✅ FINALIZED (Session 2.0.3 Parts A-D)

- ✓ Enemy HP scaling: Act-based step function (120/130/140 per enemy by Act)
- ✓ Boss HP: 7,670 / 18,555 / 38,720 (Enemies 50/100/150)
- ✓ Attack scaling: 0 until Enemy 50, then progressive (10/30/80 for bosses)
- ✓ HP upgrade system: 50/75/100/125/150 shards for +10 HP (Tier 1)
- ✓ Death loop progression: 4-6 loops to beat Enemy 150

### STILL NEEDS DESIGN (Task 2.1+)

- "Good player" progression with Pack 1-3 card improvements
- Target essence rates with optimized decks
- Card stat ranges for Packs 1-3
- Combat card design (healing, HP regen, shields)
- Post-Enemy 150 content and prestige system

---

## Session Milestones

### First 30 Minutes (Starter Deck Only)

- **~7 minutes:** Pack 1 affordable (40,000 Essence)
- **~12 minutes:** Pack 2 affordable (100,000 Essence)
- **~19 minutes:** Pack 3 affordable (250,000 Essence)
- **~23 minutes:** Enemy 50 reached (Mini-Boss #1 - First Attacker)
- **~30 minutes:** Enemy 60 reached (alternate milestone)
- **~35 minutes:** Expected death at Enemy 67 (HP depleted, 100 HP starter)

### Multi-Loop Progression (With Pack Purchases)

- **Loop 1:** Enemy 100-120 reached, ~300K essence, ~600-700 shards earned
- **Loop 2:** Enemy 130-140 reached (with Pack 1 + HP upgrades)
- **Loop 3:** Enemy 145-150 reached (with Packs 1-2-3 + HP upgrades)
- **Loop 4-6:** Enemy 150 defeated (fully optimized deck)

### Total Time to First Boss Victory

- **Bad players:** ~3-4 hours (6-7 loops)
- **Average players:** ~2-3 hours (4-5 loops)
- **Good players:** ~1.5-2 hours (3-4 loops)

---

## Combat Duration Targets

### With Starter Deck (62 ATK, 54 DEF)

```
Enemy 1 (20 HP):          ~2 seconds
Enemy 10 (1,100 HP):      ~17 seconds
Enemy 25 (2,900 HP):      ~29 seconds
Enemy 50 (7,670 HP):      ~47 seconds (Mini-Boss #1)
Enemy 100 (18,555 HP):    ~90 seconds (Mini-Boss #2, requires Pack 1)
Enemy 150 (38,720 HP):    ~180+ seconds (Major Boss, requires Packs 1-3)
```

---

## Formulas Summary

### Enemy HP Scaling (Act-Based)

```
Act 1 (1-50):    HP = 20 + (n-1) × 120
Act 2 (51-100):  HP = 6,000 + (n-51) × 130
Act 3 (101-150): HP = 12,500 + (n-101) × 140
Boss Multipliers: 1.3× (Enemy 50 = 7,670), 1.5× (Enemy 100 = 18,555), 2.0× (Enemy 150 = 38,720)
```

### Enemy Attack Scaling

```
Enemies 1-49:   0 attack
Enemy 50:       10 attack
Enemies 51-99:  10 + (n-51) × 0.3
Enemy 100:      30 attack
Enemies 101-149: 25 + (n-101) × 0.6
Enemy 150:      80 attack
```

### Pack Cost Scaling

```
Cost = 40,000 × 2.5^(n-1)
Pack 1: 40,000
Pack 2: 100,000
Pack 3: 250,000
Pack 4: 625,000
Pack 5: 1,562,500
```

### Shard Drops

```
Base_Shards = 2-3 (early) to 8-12 (late)
Formula: base_shards + floor(enemy_number / 50) × 2
Boss Multipliers: 3× (mini-bosses), 5× (major bosses)
```

### HP Upgrade Costs (Tier 1)

```
Upgrade 1 (+10 HP): 50 shards   (100 → 110 HP)
Upgrade 2 (+10 HP): 75 shards   (110 → 120 HP)
Upgrade 3 (+10 HP): 100 shards  (120 → 130 HP)
Upgrade 4 (+10 HP): 125 shards  (130 → 140 HP)
Upgrade 5 (+10 HP): 150 shards  (140 → 150 HP)
Total Cost: 500 shards for +50 HP
```

---

## Document History

**Version 1.0** (2025-11-08) - Split from DESIGN.md Version 1.9  
- Extracted Baseline Numbers Reference section
- Includes Session 1.3B baseline values
- Includes Task 2.0 validation results
- Includes Session 2.0.3 combat system updates
- Status: Complete baseline, pack card targets pending Task 2.1

