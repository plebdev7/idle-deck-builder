# Task 2.1.2A Continuation: Enemy Attack Timing & JSON Implementation

**Session:** 2.1.2A (Continuation)  
**Date:** 2025-11-08 23:07:46  
**Status:** Complete  
**Related:** CHECKLIST.md Task 2.1.2A, ROADMAP.md Session 2.1

---

## Session Goal

Complete Task 2.1.2A by:
1. Deciding on enemy attack timing (when enemies start dealing damage)
2. Implementing JSON loading in simulator
3. Validating the changes work

---

## Key Decision Made

### Decision: Enemy Attack Starts at Enemy 20 (4-minute tutorial)

**User Approval:** 2025-11-08 23:07:46

**Rationale:**
- **4-minute safe learning period** (Enemies 1-19, ~20 enemies × 12 seconds)
- First damage taken at Enemy 20 (~minute 4)
- First death expected at Enemy 25-30 (5-7 minutes) - **after Pack 1 purchase at 7 min**
- Defense/healing cards become immediately valuable from Pack 1
- Natural motivation: "I just died, need better cards!"

**Attack Scaling:**
```
Enemies 1-19:  0 ATK (safe tutorial zone)
Enemies 20-49: 2-9 ATK (gradual combat introduction, linear scaling)
Enemy 50:      10 ATK (first boss)
```

**Advantages over Enemy 50 timing:**
- Healing/defense relevant from Pack 1 (instead of 23 minutes later)
- Death loop mechanics taught naturally (first death around minute 5-7)
- Pack 1 purchase motivated by survival need
- Sidegrade design space (healing vs damage) is meaningful

---

## Implementation Work

### 1. Updated Combat System (combat.py) ✅

**Changes Made:**
- Modified `Enemy.spawn()` attack scaling
- Enemies 1-19: 0 ATK
- Enemies 20-49: 2-9 ATK (linear scaling: `int(2 + (n-20) * 0.23)`)
- Enemy 50: 10 ATK (first boss)
- Updated docstrings to reflect new timing

**Lines Changed:**
- combat.py lines 151-161 (attack scaling logic)
- combat.py line 91 (docstring update)

### 2. Implemented JSON Loading (cards.py) ✅

**New Functions Added:**
- `load_cards_from_json(json_path)` - Load cards from JSON file
- `_convert_json_to_card_format(json_card)` - Convert JSON format to Card model
- `_determine_generator_type(effects)` - Infer generator subtype from effects
- `get_game_data_path()` - Get path to game-data directory
- `load_starter_deck_from_json()` - Load starter deck with fallback
- `load_balance_config()` - Load balance configuration JSON

**JSON Format Conversion:**
- JSON uses `"type": "Generator"` → converted to `card_type` and `generator_type`
- JSON uses `"effects": [...]` array → converted to flat `attack`, `defense`, `essence_rate`, `essence_burst` fields
- Handles effect types: `add_attack`, `add_defense`, `essence_per_sec`, `essence_flat`

**Lines Added:**
- cards.py lines 176-332 (JSON loading functions)

### 3. Updated Economy Module (economy.py) ✅

**New Functions Added:**
- `load_pack_costs_from_config(config)` - Extract pack costs from balance config

**Lines Changed:**
- economy.py lines 1-35 (added JSON loading support)

### 4. Updated Deck Validation (deck.py) ✅

**Changes Made:**
- Added `max_size` field (default: 12 for Arcane Student)
- Added `validate_deck_size()` model validator
- Validates minimum 8 cards, maximum 12 cards (configurable)

**Lines Changed:**
- deck.py lines 1-42 (added validation and max_size field)

### 5. Updated Design Documentation (DESIGN.md) ✅

**Changes Made:**
- Updated "Act 1 (Enemies 1-50)" section with new attack timing
- Updated "Key Milestones" with Minute 4 milestone
- Added clarity: "Enemy 20 reached (first damage taken, combat becomes real)"
- Updated "Enemy 50" description from "First Attacker" to "First Boss Fight"

**Lines Changed:**
- DESIGN.md lines 156-160 (enemy scaling section)
- DESIGN.md lines 294-301 (key milestones section)

---

## Validation & Testing

### Test Results ✅

**Test Script:** `simulator/test_json_loading.py` (temporary, deleted after validation)

**Test 1: JSON Loading**
- ✅ Loaded 8 cards from `game-data/cards-starter-deck.json`
- ✅ All card stats correctly parsed:
  - Arcane Conduit: +2.0/sec
  - Essence Burst: +250 (buffed value)
  - Combat Siphon: ATK:12 DEF:6 +1.0/sec
  - Arcane Bolt: ATK:20
  - Mystic Shield: DEF:20 (buffed value)
  - Balanced Strike: ATK:10 DEF:10
  - Power Strike: ATK:15 DEF:5
  - Stalwart Guard: ATK:5 DEF:15

**Test 2: Balance Config Loading**
- ✅ Loaded balance-config.json v1.0.0
- ✅ Deck limit: 12 cards
- ✅ Pack 1 cost: 40,000

**Test 3: Deck Creation**
- ✅ Created deck with 8 cards (max: 12)
- ✅ Total stats: ATK:62 DEF:56 Rate:3.0/sec

**Test 4: Enemy Attack Timing**
```
Enemy  1: HP=    20, ATK=  0  ← Safe
Enemy 10: HP= 1,100, ATK=  0  ← Safe
Enemy 19: HP= 2,180, ATK=  0  ← Safe (last safe enemy)
Enemy 20: HP= 2,300, ATK=  2  ← FIRST ATTACK! ✅
Enemy 25: HP= 2,900, ATK=  3  ← Expected first death zone
Enemy 30: HP= 3,500, ATK=  4
Enemy 49: HP= 5,780, ATK=  8
Enemy 50: HP= 7,670, ATK= 10  ← Boss
```

**Test 5: Simulation**
- ✅ 30-second simulation ran successfully
- ✅ Defeated 3 enemies
- ✅ Drew 25 cards
- ✅ Final essence: 1,135
- ✅ Player HP: 100/100
- ✅ Deaths: 0

---

## Files Modified

### Created
- `game-data/balance-config.json` (Session 2.1.2A earlier)
- `game-data/cards-schema.json` (Session 2.1.2A earlier)
- `game-data/cards-starter-deck.json` (Session 2.1.2A earlier)
- `game-data/README.md` (Session 2.1.2A earlier)

### Modified
- `simulator/simulator/core/combat.py` - Enemy attack timing (Enemy 20)
- `simulator/simulator/core/cards.py` - JSON loading, buffed starter cards, converters
- `simulator/simulator/core/economy.py` - Config loading support
- `simulator/simulator/core/deck.py` - 12-card limit validation
- `DESIGN.md` - Enemy attack timing documentation
- `docs/design-specs/card-system.md` (Session 2.1.2A earlier)

### Next Files to Update
- `CHECKLIST.md` - Mark Task 2.1.2A items complete
- `.cursor/log/sessions/session-2-1-2a-stat-point-system.md` - Update with continuation work

---

## Completion Status

### Task 2.1.2A Checklist

- [x] ~~Identify Enemy that should start dealing damage~~ → **Enemy 20 (4-min tutorial)**
- [x] ~~Implement card data in simulator (JSON-based)~~
  - [x] JSON loading functions in cards.py
  - [x] JSON format converter (effects array → flat stats)
  - [x] Balance config loading in economy.py
  - [x] Deck size validation (12-card limit)
- [x] ~~Validate stat ranges per pack and rarity~~ → Validated via test script

**Status:** ✅ **COMPLETE**

---

## Next Steps (Task 2.1.2B)

### Now Ready For:

**Task 2.1.2B - Design Pack 1+2 Cards:**
1. Create Pack 1 cards (4 Common + 1 Rare)
   - Use stat point system (Common: 20-30, Rare: 30-50)
   - Include healing/defense options (now valuable from Enemy 20)
   - Sidegrade design (not strictly better than starter)
2. Create Pack 2 cards
3. Model essence generation with Pack 1+2 cards
4. Model combat effectiveness (Enemy 100 feasibility)
5. Validate 4-6 death loop progression expectation

### Critical Design Context for Pack 1

**Timing:**
- Pack 1 affordable: ~7 minutes (40,000 Essence)
- Enemy 20 reached: ~4 minutes (first damage)
- Expected first death: 5-7 minutes (just before or during Pack 1 purchase)

**Design Implications:**
- **Healing cards NOW valuable** (enemies attacking from Enemy 20+)
- **Defense cards NOW relevant** (not waiting until minute 23)
- **Sidegrade space works:** Can trade damage for survival
- **Teaching moment:** Death → see Pack 1 → buy defensive options → survive longer

**Pack 1 Should Include:**
- At least 1-2 defensive/healing options
- Higher damage options for aggressive players
- Clear tradeoffs (survival vs. speed)

---

## Design Philosophy Reinforced

### Death Loop as Core Mechanic

**This change makes death loop work better:**
- Players experience death early (minute 5-7, not minute 23)
- Death happens with resources available (Pack 1 just affordable)
- Clear upgrade path: die → earn essence → buy cards → try again
- Multiple deaths to Enemy 50 now makes sense (was overkill before)

### Sidegrade Design Validation

**Now feasible because:**
- Defense matters from Pack 1 (Enemy 20+ attacking)
- Healing cards useful immediately
- Can't just stack damage - need survival
- Creates meaningful choice: speed vs. safety

---

## Decisions Documented

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Enemy 20 attack start | 4-min tutorial, death before Pack 1, defense relevant early | ✅ Better death loop, meaningful Pack 1 choices |
| JSON loading implementation | Centralized balance, shared data between simulator and web game | ✅ Single source of truth |
| 12-card deck limit | Forces choices at Pack 1 (8 starter + 5 pack 1 = 13, must cut 1) | ✅ Teaches deck building immediately |
| Effect converter | JSON uses array format, simulator uses flat stats | ✅ Flexible data format for web game |

---

## Session Complete

**Date Completed:** 2025-11-08 23:15:00  
**Time Spent:** ~45 minutes  
**Tasks Completed:** 6/6

✅ Enemy attack timing decision made (Enemy 20)  
✅ Combat system updated  
✅ JSON loading implemented  
✅ Deck validation updated (12-card limit)  
✅ DESIGN.md updated  
✅ All changes validated via test script

**Ready for:** Task 2.1.2B - Pack 1+2 Card Design

