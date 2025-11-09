# Combat Progression & Enemy Scaling

**Last Updated:** 2025-11-08  
**Status:** Complete (Session 2.0.3 Part C)  
**Parent Document:** [DESIGN.md](../../DESIGN.md)

---

## Design Philosophy

The combat progression system is built around a **death-and-retry loop** where players progressively build stronger decks to overcome increasingly difficult enemies and bosses. Death is not punishment but part of the core progression loop - players keep all resources and iterate on their deck between attempts.

---

## Enemy Health Scaling Formula

### Act-Based Step Function System

The HP formula uses a **step function** that increases base HP after each boss, creating clear progression tiers while ensuring post-boss enemies are easier than the boss itself.

### Act 1 (Enemies 1-50): Tutorial Tier

```
Base HP = 20 + (enemy_number - 1) × 120
Enemy 49:  5,780 HP (regular)
Enemy 50:  7,670 HP (Mini-Boss #1, 1.3× multiplier = 5,900 × 1.3)
```

### Act 2 (Enemies 51-100): Challenge Tier

```
Base HP = 6,000 + (enemy_number - 51) × 130
Enemy 51:  6,000 HP (step up from Act 1, but < boss)
Enemy 99:  12,240 HP (regular)
Enemy 100: 18,555 HP (Mini-Boss #2, 1.5× multiplier)
```

### Act 3 (Enemies 101-150): Master Tier

```
Base HP = 12,500 + (enemy_number - 101) × 140
Enemy 101: 12,500 HP (step up from Act 2, but < boss)
Enemy 149: 19,220 HP (regular)
Enemy 150: 38,720 HP (Major Boss, 2.0× multiplier = 19,360 × 2.0)
```

### Act 4+ (Enemies 151+): Future Content

```
Base HP = 38,880 + (enemy_number - 151) × 200
(To be balanced with elemental tier progression)
```

### Design Rationale

- **Step functions create clear Acts:** Each boss victory unlocks a new difficulty tier
- **Post-boss breathing room:** Enemy 51 < Boss 50, giving players a moment to stabilize
- **Continuous progression:** Enemy 51 > Enemy 49, ensuring forward momentum
- **Escalating challenge:** HP per enemy increases (120 → 130 → 140) across Acts
- **Boss victories feel rewarding:** Beating a boss unlocks easier content initially, then ramps back up

### Key Milestones

- Enemy 1: 20 HP
- Enemy 50: 7,670 HP (Mini-Boss #1 - First Attacker) ← ~23 minutes
- Enemy 100: 18,555 HP (Mini-Boss #2 - First Real Wall) ← ~60-70 minutes
- Enemy 150: 38,720 HP (Major Boss - End of "Act 1" content) ← ~120-180 minutes

---

## Boss Encounter System

Bosses are **progression checkpoints** that require multiple death loops with deck improvements to overcome. They serve as clear milestones, motivation to purchase packs, and achievement moments.

### Enemy 50 - Mini-Boss #1 "Defense Tutorial" ("Lieutenant")

**Stats:**
- HP: 7,670 (1.3× base HP = 5,900 × 1.3)
- Attack: **10** (FIRST enemy with attack!)

**Purpose:**
- **First damage dealer** - introduces defense mechanic
- ~23-minute milestone with starter deck
- "Oh no, I'm taking damage!" tutorial moment
- Still survivable (100 HP vs 10 ATK/tick, defense cards block damage)
- Teaches that special enemies are stronger AND more dangerous
- Forces defensive card strategy for first time

**Rewards:**
- 3× regular shard drops (~6-9 shards)
- Achievement: "Survived First Assault"
- Visual celebration

**Expected Outcomes:**
- Most players survive on first loop (if defense cards drawn early)
- Some players die (if poor deck or unlucky draw order)
- Either way: Learns that defense matters now

### Enemy 100 - Mini-Boss #2 ("Commander")

**Stats:**
- HP: 18,555 (1.5× regular Enemy 100 = 12,370 × 1.5)
- Attack: 30

**Purpose:**
- **First real wall** - bad players fail here on first loop
- Requires Pack 1 purchase OR excellent starter deck play
- Teaches importance of pack purchases and deck optimization
- Soft gate encouraging first death loop

**Rewards:**
- 3× regular shard drops (~12-18 shards)
- Achievement: "Defeated First Commander"

**Expected Outcomes:**
- Bad player (starter deck only): **Fails** - Dies around Enemy 90-100
- Average player (Pack 1): **Beats it** - Continues to ~120-140
- Good player (Pack 1-2): **Beats it** - Continues toward Enemy 150

### Enemy 150 - Major Boss #1 ("Tower Guardian")

**Stats:**
- HP: 38,720 (2.0× base HP = 19,360 × 2.0)
- Attack: 80

**Purpose:**
- **Major milestone** - End of "Act 1" content
- Requires 2-3 death loops with progressive improvements
- Beating this is major achievement
- May unlock prestige system (to be designed in Session 7)

**Rewards:**
- 5× regular shard drops (~40-60 shards)
- Major achievement: "Defeated Tower Guardian"
- Possible special currency or content unlock
- Celebration sequence

**Expected Outcomes:**
- Loop 1 (starter deck): Fails at Enemy 90-100 (Commander)
- Loop 2 (Packs 1-2): Fails at Enemy 130-140
- Loop 3 (Packs 1-3): Fails at Enemy 150 boss
- Loop 4-5 (optimized): **Beats boss**

**Design Philosophy:**
- Boss is clearly impossible on first 2 loops
- Creates satisfying multi-loop progression arc
- Beating it feels earned, not lucky
- Not a "tutorial death" but a **progression wall** requiring iteration

### Future Bosses

- **Enemy 300:** Major Boss #2, end of "Act 2"
- **Enemy 450, 600, etc.:** Every 150 enemies
- Elemental tier bosses with unique mechanics (future design)

---

## Enemy Attack/Defense Scaling (Per-Tick System)

### Design Philosophy

**Dynamic Per-Tick Scaling:** Enemies gain ATK and DEF each combat tick to counter the player's exponential stat growth from deck cycling. This prevents defensive builds from achieving "default invulnerability" and creates strategic tension throughout long fights.

**Key Principle:** Player deck cycling provides ~6.9 ATK/tick and ~6.2 DEF/tick (starter deck). Enemy per-tick rates must scale comparably or faster to remain threatening.

### Per-Tick Scaling Formulas

**Act 1 (Enemies 1-50): Learning Phase**
```
ATK_per_tick = 1.0 + (enemy_number - 1) × 0.05
DEF_per_tick = 0.5 + (enemy_number - 1) × 0.025

Enemy 1:  1.0 ATK/tick, 0.5 DEF/tick
Enemy 25: 2.2 ATK/tick, 1.1 DEF/tick
Enemy 50: 3.45 ATK/tick, 1.73 DEF/tick

Design: Slower than player growth = manageable, teaches mechanics
```

**Act 2 (Enemies 51-100): Challenge Phase**
```
ATK_per_tick = 3.5 + (enemy_number - 51) × 0.08
DEF_per_tick = 1.75 + (enemy_number - 51) × 0.04

Enemy 51:  3.5 ATK/tick, 1.75 DEF/tick
Enemy 75:  5.42 ATK/tick, 2.71 DEF/tick
Enemy 100: 7.42 ATK/tick, 3.71 DEF/tick

Design: Approaches player growth = tense, requires good decks
```

**Act 3 (Enemies 101-150): Master Phase**
```
ATK_per_tick = 7.5 + (enemy_number - 101) × 0.12
DEF_per_tick = 3.75 + (enemy_number - 101) × 0.06

Enemy 101: 7.5 ATK/tick, 3.75 DEF/tick
Enemy 125: 10.38 ATK/tick, 5.19 DEF/tick
Enemy 150: 13.38 ATK/tick, 6.69 DEF/tick

Design: Faster than player growth = intense, requires optimized decks
```

**Bosses (All):**
```
ATK_per_tick = regular_rate × 2.0
DEF_per_tick = regular_rate × 2.0

Enemy 50 Boss:  6.9 ATK/tick, 3.46 DEF/tick (matches player DEF growth!)
Enemy 100 Boss: 14.84 ATK/tick, 7.42 DEF/tick (exceeds player growth!)
Enemy 150 Boss: 26.76 ATK/tick, 13.38 DEF/tick (way exceeds player growth!)

Design: Long boss fights become extremely dangerous
```

### Combat Tick Examples

**Enemy 1 (500 HP suggested, 1.0 ATK/tick, 0.5 DEF/tick):**
```
Tick 0:  1.0 ATK, 0.5 DEF
Tick 5:  6.0 ATK, 3.0 DEF
Tick 10: 11.0 ATK, 5.5 DEF
Tick 15: 16.0 ATK, 8.0 DEF

Fight lasts ~12-15 ticks with starter deck
Player loses ~10-15 HP before defense exceeds enemy ATK
```

**Enemy 50 Regular (7,670 HP, 3.45 ATK/tick, 1.73 DEF/tick):**
```
Tick 0:  3.45 ATK, 1.73 DEF
Tick 10: 37.95 ATK, 19.03 DEF
Tick 20: 72.45 ATK, 36.33 DEF
Tick 47: 165.6 ATK, 82.8 DEF

Starter deck (56 DEF after 8 ticks) can survive
Player DEF outpaces enemy ATK growth = winnable
```

**Enemy 50 Boss (7,670 HP, 6.9 ATK/tick × 2.0, 3.46 DEF/tick):**
```
Tick 0:  6.9 ATK, 3.46 DEF
Tick 10: 75.9 ATK, 38.06 DEF
Tick 20: 144.9 ATK, 72.66 DEF
Tick 47: 331.2 ATK, 165.6 DEF

Enemy ATK growth matches player DEF growth!
Very dangerous, requires excellent defensive play or fast kill
```

**Enemy 150 Boss (38,720 HP, 26.76 ATK/tick, 13.38 DEF/tick):**
```
Tick 0:   26.76 ATK, 13.38 DEF
Tick 30:  830.56 ATK, 415.28 DEF
Tick 60:  1,634.36 ATK, 817.18 DEF
Tick 100: 2,702.76 ATK, 1,351.38 DEF

Starter deck cannot survive this
Requires Packs 1-3 with serious defensive investment OR fast kill strategy
```

### Design Rationale

**No "Safe Tutorial" Phase:** 
- All enemies deal damage from tick 0
- Death has no penalty, players learn by dying
- Removed 30-minute safe period (was artificial)

**No Default Invulnerability:**
- Defense builds require serious investment
- Offensive builds win by killing quickly
- Healing becomes critical for long runs
- Every fight maintains threat

**Strategic Build Diversity:**
- **Glass Cannon:** High ATK, kill before enemy ramps (risky but efficient)
- **Tank:** High DEF investment, survive the ramp (safer, slower)
- **Balanced:** Some of each (middle ground)
- **Healing Focus:** HP regen/healing to sustain (enables long runs)

---

## Death and Respawn System

**CRITICAL DISTINCTION:** Death loop is **NOT prestige**. It's the normal gameplay loop.

### What Happens on Death

**1. Death Trigger:** Player loses (insufficient defense, can't beat boss, etc.)

**2. Death Screen Shows:**
- Enemies defeated: "You reached Enemy 94"
- Essence earned this run
- Shards earned this run
- Achievements unlocked
- Progress indicator: "94/150 to Tower Guardian"

**3. Resources Kept (Everything Persists):**
- ✅ All cards in collection
- ✅ All essence (spend on packs)
- ✅ All shards (spend on upgrades)
- ✅ Current deck composition
- ✅ Card levels/upgrades purchased
- ✅ All progress and unlocks

**4. Player Actions After Death:**
- Spend essence on new packs
- Spend shards on card upgrades, deck size increases
- Rebuild/optimize deck
- **Swap class** (if you own other class cards)
- Review achievements

**5. Respawn:** Click "Continue" → Restart at Enemy 1 with improved deck

### This Loop Is Core Gameplay

- Fight → Die → Spend resources → Improve deck → Fight again
- Like dying in Rogue Legacy and buying upgrades before next run
- Expected to loop 3-6 times to beat first major boss
- No penalty for death, just natural progression rhythm

### Death vs Prestige (Clarification)

| Mechanic | Trigger | What Resets | What Persists | Rewards |
|----------|---------|-------------|---------------|---------|
| **Death Loop** | Die to enemy/boss | Enemy progress only | Everything (cards, essence, shards, deck) | None (just retry) |
| **Prestige** | Manual choice (late game) | TBD (Session 7) | TBD (Session 7) | Permanent bonuses |

**Prestige System (To Be Designed):**
- Unlocked after beating first major boss (Enemy 150)?
- Separate advanced mechanic from normal death loop
- Provides permanent bonuses but involves real resets
- Design deferred to Session 7

---

## Multi-Loop Progression Expectations

### Loop 1 - Discovery

- Starter deck only, 100 HP
- Reach: Enemy 100-120
- Die to: HP depletion or stronger enemies
- Accumulate: ~300,000 essence, ~600-700 shards
- **Action:** Purchase Pack 1, save shards for HP upgrades

### Loop 2 - Improvement

- Pack 1 cards + HP upgrades (150-170 HP)
- Reach: Enemy 130-140
- Die to: Approaching Enemy 150 boss or HP depletion
- Accumulate: More essence and shards
- **Action:** Purchase Packs 2-3, more HP upgrades

### Loop 3 - Approach

- Packs 1-2-3 + HP upgrades (180-200 HP)
- Reach: Enemy 145-150
- Die to: Major Boss first attempts
- Accumulate: More essence/shards
- **Action:** Optimize deck composition, final HP upgrades

### Loop 4-6 - Victory

- Fully optimized deck with Packs 1-3 + 200+ HP
- Reach: Enemy 150 (Major Boss)
- Close attempts, eventually **BEAT BOSS**
- **Milestone:** Major achievement unlocked

### Total Time to First Boss Victory

- Bad players: ~3-4 hours (6-7 loops)
- Average players: ~2-3 hours (4-5 loops)
- Good players: ~1.5-2 hours (3-4 loops)

---

## Rewards Structure

### Regular Enemy Victories

- Shards: 2-3 (early) → 8-12 (late)
- Formula: `base_shards + floor(enemy_number / 50) × 2`
- Essence: From generator cards drawn during combat

### Mini-Boss Victories (50, 100)

- 3× regular shard drops
- Achievement unlocks
- Visual celebration

### Major Boss Victory (150)

- 5× regular shard drops
- Major achievement
- Possible special rewards (pack discount, currency, content unlock)
- Narrative moment / celebration sequence

---

## UI and Player Communication

### Progress Indicators

- Display: "Enemy 94 / 150"
- Boss warning at Enemy 149: "Major Boss Ahead"
- Visual milestone markers on progress bar

### Death Screen Tone

- Celebratory of progress made (not punishing)
- Shows clear next steps ("Buy packs to grow stronger!")
- Emphasizes iteration and improvement

---

## Balance Targets for Pack Card Design (Task 2.1)

### Combat Power Requirements

- Enemy 100 Mini-Boss: 18,555 HP
  - Pack 1 should provide +15-20% power over starter deck
- Enemy 150 Major Boss: 38,720 HP
  - Packs 1-3 should provide +30-40% total power

### Generator Power Requirements

- Pack 1: +4-5 Essence/sec per draw (vs starter +1-2)
- Pack 2: +6-8 Essence/sec per draw
- Pack 3: +10-12 Essence/sec per draw

### Combat Card Stats

- Pack 1: 25-35 total stats (vs starter 8-20)
- Pack 2: 40-50 total stats
- Pack 3: 60-80 total stats (Rare/Epic cards)

---

## Document History

**Version 1.0** (2025-11-08) - Split from DESIGN.md Version 1.9  
- Extracted complete Combat Progression & Enemy Scaling section
- Includes Act-based HP formula (Session 2.0.3 Part C)
- Includes boss encounter system and death loop mechanics
- Status: Complete and validated

