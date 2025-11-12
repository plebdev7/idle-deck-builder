# Combat System Specification

**Last Updated:** 2025-11-08  
**Status:** Complete (Session 2.0.3)  
**Parent Document:** [DESIGN.md](../../DESIGN.md)

---

## Overview

The combat system uses **Trimps-style combat-over-time** mechanics where player and enemy exchange damage tick-by-tick until one dies. Player strategy is in deck construction - combat itself is fully automated.

---

## Core Combat Mechanics

### Combat Tick System

**Authoritative Source:** See [`game-data/balance-config.json`](../../game-data/balance-config.json) for exact timing values.

**Tick Rate:** 1.0 second per tick (as of current balance)
- Aligns with card draw rate (1 card/second)
- Simple calculations and predictable pacing
- Combat resolves tick-by-tick until victory or death

**Damage Formulas (Per Tick):**
```
Player Damage Dealt = max(Player_Attack - Enemy_Defense, 0)
Player Damage Taken = max(Enemy_Attack - Player_Defense, 0)

Enemy_Attack = ATK_per_tick × ticks_elapsed
Enemy_Defense = DEF_per_tick × ticks_elapsed

Where ATK_per_tick and DEF_per_tick scale with enemy number
(See progression.md for complete per-tick scaling formulas)
```

**Key Mechanics:**
- No minimum damage (perfect defense = 0 damage taken)
- Cards drawn mid-fight break stalemates naturally
- Flat damage reduction (Attack - Defense)
- Simple, predictable calculations

---

## Player HP System

**Authoritative Source:** See [`game-data/balance-config.json`](../../game-data/balance-config.json) for exact HP values and upgrade costs.

### Starting HP

**Base HP:** 100 HP (as of current balance)

### HP Scaling

**How HP Increases:**
- ✅ Shard upgrades: Spend shards for permanent max HP increases (see HP Upgrade System below)
- ✅ Card mechanics: Cards can temporarily boost max HP, heal, or add HP regen

**What DOESN'T Increase HP:**
- ❌ No automatic HP growth per enemy defeated
- ❌ No automatic HP growth per pack purchased

### HP Recovery

**Healing Rules:**
- ❌ No automatic healing between enemies
- ❌ No healing after victories
- ✅ Full heal only on death/respawn
- ✅ Healing via card mechanics during run (instant heal, HP regen)

### HP Upgrade System (Shard Spending)

**Example progression (as of current balance):**

**Tier 1 (HP 100 → 150):**
- 5 upgrades at 50/75/100/125/150 shards (+10 HP each)
- Total cost: 500 shards
- Total gain: +50 HP

**Tier 2 (HP 150 → 200):**
- 5 upgrades at 175-300 shards (+10 HP each)
- Total cost: ~1,200 shards
- Total gain: +50 HP

**Tier 3 (HP 200 → 300):**
- 10 upgrades at 325-750 shards (+10 HP each)
- Total cost: ~5,000 shards
- Total gain: +100 HP

**Expected Progression:**
- ~600-700 shards by Enemy 50
- Enough for 5-7 upgrades (+50-70 HP)
- Death Loop integration: Spend shards on HP after Loop 1, start Loop 2 with 150-170 HP

### Strategic Implications

- HP is a precious, depleting resource
- No healing between enemies = death spiral gameplay
- Must manage HP across entire run
- Healing cards become strategically valuable
- Death is inevitable without healing strategy

---

## Continuous Deck Cycling

### Card Draw Mechanic

**Timing (as of current balance):**
- Cards draw at **1 card/second** continuously
- When deck exhausts, **1-second reshuffle cooldown**
- After cooldown, deck immediately reshuffles and drawing continues
- Stats accumulate with each cycle (exponential growth)

### Example: 8-Card Deck

```
Cycle 1 (Ticks 0-7):   Draw 8 cards → 0 to 62 ATK
Tick 8:                Reshuffle cooldown (1 second)
Cycle 2 (Ticks 9-16):  Draw 8 cards again → 62 to 124 ATK (+62)
Tick 17:               Reshuffle cooldown
Cycle 3 (Ticks 18-25): Draw 8 cards again → 124 to 186 ATK (+62)
... continues until enemy dies or player dies
```

### Reshuffle Cooldown Benefits

- Small decks: 8 cards + 1s cooldown = 9s cycle (11% downtime)
- Large decks: 15 cards + 1s cooldown = 16s cycle (6% downtime)
- Slightly favors larger decks (less % downtime)

### Deck Size Constraints

**As of current balance:**
- **Minimum:** 8 cards (prevents tiny deck exploit)
- **Maximum:** Determined by active class (varies by rarity)

---

## Stat Accumulation and Reset

### During Enemy Fight

- Cards drawn add to Attack and Defense permanently
- Stats continue accumulating with each deck cycle
- Stats reset only when enemy dies or player dies

### When Enemy Dies

- ✅ Player Attack → **Reset to 0**
- ✅ Player Defense → **Reset to 0**
- ✅ Essence Rate → **PERSISTS** (carries forward)
- ✅ HP → **NO HEAL** (damage carries forward to next enemy)
- ✅ Accumulated Essence → **PERSISTS**
- Next enemy spawns, stats start from 0 again

### When Player Dies

- ✅ Player Attack → Reset to 0
- ✅ Player Defense → Reset to 0
- ✅ Essence Rate → Reset to 0
- ✅ Current HP → **Full heal to max HP**
- ✅ Max HP → Based on permanent shard upgrades only
- ✅ Accumulated Essence → **PERSISTS** (critical for death loop)
- ✅ Enemy Progress → Reset to Enemy 1
- ✅ Card Collection → **PERSISTS**
- ✅ Deck Composition → **PERSISTS**

---

## Combat Flow Example

### Enemy 50: 7,670 HP, 10 ATK (First Attacker)
**Player: 100 HP, 8-card starter deck**

```
CYCLE 1 (Ticks 0-7: Drawing cards)
Tick 0: 0 ATK, 0 DEF
  - Damage dealt: 0 | Damage taken: 10 | Player: 90 HP

Tick 1: 20 ATK, 0 DEF (Arcane Bolt drawn)
  - Damage dealt: 20 | Damage taken: 10 | Player: 80 HP

Tick 2: 20 ATK, 18 DEF (Mystic Shield drawn)
  - Damage dealt: 20 | Damage taken: 0 (defense working!)

Ticks 3-7: Continue drawing, build to 62 ATK, 54 DEF

Tick 8: [RESHUFFLE COOLDOWN - 1 second]
  - Still dealing damage (62/tick), taking 0 damage (defense > attack)

CYCLE 2 (Ticks 9-16)
  - Stats grow: 62 → 124 ATK, 54 → 108 DEF
  - Damage accelerates

CYCLE 3+ (Ticks 17+)
  - Stats continue growing: 186 ATK, 248 ATK, etc.
  - Enemy defeated around Tick 47

Total Time: ~47 seconds
Player HP: ~80/100 (lost 20 HP before defense kicked in)
```

---

## Death System

### Death Condition

**Death Trigger:** HP reaches 0 during combat
- Instant death, no "saving throw"
- Can occur at any tick (during draw or reshuffle)

### Death Screen

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

**Death Screen Tone:**
- Celebratory of progress made (not punishing)
- Shows what you earned this run
- Shows total resources available
- Encourages spending and improving

### Class Switching on Death

- Death screen offers class switch option (if you own other class cards)
- Can switch class before respawning
- Deck adjusts to new class's limits automatically

### Respawn Mechanics

- Stats reset (0 ATK, 0 DEF, 0 Essence/sec)
- HP restored to full (based on permanent max HP)
- Enemy counter resets to Enemy 1
- Accumulated essence and shards persist

**For complete state persistence rules (reshuffle, enemy, death), see:** [conditional-mechanics.md - State Persistence Rules](conditional-mechanics.md#state-persistence-rules)

---

## Strategic Implications

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

- **Early fight:** Vulnerable (low stats)
- **Mid fight:** Ramping (stats accumulating)
- **Late fight:** Overwhelming (massive stats from multiple cycles)
- Longer fights = more cycles = godlike power eventually

### 4. Death Spirals Are Intentional

- Low HP → need to survive longer → need more defense
- Creates tension and "oh no" moments
- Death loop is expected progression mechanic

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

---

## Combat Duration

**Example combat times with starter deck (as of current balance):**

```
Enemy 1 (20 HP):          ~2 seconds
Enemy 10 (1,100 HP):      ~17 seconds
Enemy 25 (2,900 HP):      ~29 seconds
Enemy 50 (7,670 HP):      ~47 seconds (Mini-Boss #1)
Enemy 100 (18,555 HP):    ~90 seconds (Mini-Boss #2, requires Pack 1)
Enemy 150 (38,720 HP):    ~180+ seconds (Major Boss, requires Packs 1-3)
```

**Session Milestones:**
- **~23 minutes:** Enemy 50 reached (Mini-Boss #1 - First Attacker)
- **~30 minutes:** Enemy 60 reached (alternate milestone)
- **~35 minutes:** Enemy 67 - Expected death with starter deck (HP depleted)

---

## Offline Calculation

**Status:** Needs redesign for combat-over-time system

Previous instant-resolution calculation is obsolete.

**To Be Designed:**
- Average combat duration per enemy
- Average essence generation rate with combat duration
- Estimated progression distance for offline time

---

## Superseded Sections

The following sections from Version 1.8 are superseded by this combat redesign:
- Old "Combat Loop (Session 1.2 Decision)" - Replaced with tick-based combat
- Old "Two-Phase System: Charging + Combat" - No longer instant resolution
- Old "Offline Calculation" formula - Needs redesign for combat duration

---

## Document History

**Version 1.0** (2025-11-08) - Split from DESIGN.md Version 1.9  
- Extracted complete Combat System section from Session 2.0.3
- Includes Parts A-D (mechanics, death, balance, documentation)
- Status: Complete and validated

