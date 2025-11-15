# Task 2.1.8: Design Pack 2 Guaranteed Cards

**Task Reference:** CHECKLIST.md Task 2.1.8  
**Session Start:** 2025-11-15 12:41:34  
**Session End:** 2025-11-15 12:45:00  
**Status:** COMPLETE

---

## Objective

Design 5 guaranteed cards for Pack 2 (3 Commons + 2 Rares) that introduce sequencing mechanics and timing-based conditionals while maintaining the "vanilla filler" philosophy for Arcane tier cards.

---

## Design Constraints

### User Requirements (2025-11-15 12:41:34)
1. **Commons should have NO conditions** - continue flat value pattern from Pack 1
2. **Rares should stick to simple conditions** - single conditions only, no AND/OR
3. **Arcane is "vanilla" magic** - filler cards useful in various deck types
4. **Negative effects optional but not required** - use sparingly
5. **Previous card sequencing intuitive** - start with simplest sequence mechanic
6. **No strictly better cards** - every card must have tradeoffs vs same-rarity cards

### Design Philosophy
- Pack 2 timing: ~15-20 minutes, 100,000 Essence (2.5× Pack 1)
- Player state: Owns 18 total cards (8 starter + 5 Pack 1 + 5 Pack 2), 12-card deck limit
- Strategic role: More deck variety without power creep, introduce new mechanics

---

## Design Space Analysis

### What's Covered (Starter + Pack 1)
**Generators:**
- Pure rate: Arcane Conduit (+2/sec)
- Pure burst: Essence Burst (+250)
- Rate+combat balanced: Combat Siphon (+1/sec, +12/6)
- Rate with ATK penalty: Essence Drain (+3/sec, -5 ATK)

**Combat:**
- Full offense/defense spectrum covered
- Penalty extremes covered (Reckless Bolt, Fortified Stance)

**Utility:**
- Burst healing: Minor Restoration (Heal 12 HP)

**Conditionals:**
- State-based: Battle Surge (HP < 50%)

### Gaps to Fill in Pack 2
1. **Burst + combat hybrid** (no card has burst + combat stats)
2. **Generator with defensive penalty** (only ATK penalty exists)
3. **Offensive hybrid generator** (Combat Siphon is balanced, need unbalanced)
4. **Sequence tracking** (previous card mechanic)
5. **Timing-based conditionals** (reshuffle count)

---

## Pack 2 Card Designs

### Card 1: Arcane Reservoir
**Type:** Hybrid (Burst Generator + Combat)  
**Rarity:** Common  
**Stat Budget:** 23 points (200 essence/25 = 8, 15 DEF = 15)

**Stats:**
- +200 Essence (instant burst)
- +15 DEF

**Design Intent:**
- First burst generator with combat stats
- Defensive focus (vs offensive focus options)
- Bridges pure burst (Essence Burst +250) and hybrid rate (Combat Siphon)

**Not Strictly Better Than:**
- Essence Burst: More burst (250 vs 200), no combat stats
- Combat Siphon: Rate generation, more total combat stats

---

### Card 2: Steady Channeling
**Type:** Generator (Rate)  
**Rarity:** Common  
**Stat Budget:** 27 points (3.0 × 10 = 30, -3 DEF = -3)

**Stats:**
- +3 Essence/sec
- -3 DEF

**Design Intent:**
- Completes penalty generator set with Essence Drain
- Essence Drain: +3/sec, -5 ATK (offensive penalty)
- Steady Channeling: +3/sec, -3 DEF (defensive penalty)
- Player chooses which penalty fits their build

**Not Strictly Better Than:**
- Arcane Conduit: Lower rate (2 vs 3), no penalty
- Essence Drain: Same rate, different penalty

**Design Decision (2025-11-15):**
- User approved defensive penalty alternative to "complete the set"
- Creates meaningful choice: offensive builds take Steady Channeling, defensive builds take Essence Drain

---

### Card 3: Offensive Siphon
**Type:** Hybrid (Rate Generator + Combat)  
**Rarity:** Common  
**Stat Budget:** 25 points (1.0 × 10 = 10, 15 ATK = 15)

**Stats:**
- +1 Essence/sec
- +15 ATK

**Design Intent:**
- Attack-focused hybrid generator
- Pure offense (no DEF) vs Combat Siphon's balance
- Same rate as Combat Siphon (+1/sec) but unbalanced stats

**Not Strictly Better Than:**
- Combat Siphon: Same rate, more total combat (18 vs 15), balanced
- Arcane Conduit: Better rate (2 vs 1), no combat

**Design Decision (2025-11-15):**
- **Initial version (+2/sec, +10 ATK) was strictly better than Arcane Conduit**
- User caught this issue
- Fixed to +1/sec, +15 ATK (Option B)
- Now creates clear tradeoff: Arcane Conduit has 2× rate, Offensive Siphon adds ATK

---

### Card 4: Arcane Synergy ⭐
**Type:** Hybrid (All stats + Conditional)  
**Rarity:** Rare  
**Stat Budget:** 43 points (15 ATK + 10 DEF + 1/sec = 35 base, +20 combat @ 0.4 = 8 conditional)

**Stats (Base):**
- +15 ATK
- +10 DEF
- +1 Essence/sec

**Conditional Bonus:**
- If previous card was Generator: +10 ATK, +10 DEF

**Design Intent:**
- **FIRST SEQUENCE-TRACKING CARD IN GAME**
- Teaches "previous card" mechanic (simplest sequence condition)
- Requires visible "last 3 cards drawn" UI element
- Rewards generator-heavy decks (~35% trigger rate in balanced 4/12 generator decks)
- When triggered: 25/20/1 total (strong Rare power level)

**Condition Details:**
- Type: Sequence (previous card)
- Coefficient: 0.4 (Sometimes True, per conditional-mechanics.md)
- Trigger probability: ~30-40% depending on deck composition
- Always visible: Last 3 cards shown with type icons

**Design Decision (2025-11-15):**
- User approved "previous card" as first sequence mechanic (most intuitive)
- Coefficient 0.4 approved as starting point

---

### Card 5: Battle Focus ⭐
**Type:** Combat + Conditional  
**Rarity:** Rare  
**Stat Budget:** 47.5 points (20 ATK + 15 DEF = 35 base, +25 combat @ 0.5 = 12.5 conditional)

**Stats (Base):**
- +20 ATK
- +15 DEF

**Conditional Bonus:**
- After 2nd reshuffle: +15 ATK, +10 DEF

**Design Intent:**
- Teaches reshuffle timing (different from state-based conditions)
- Rewards longer fights (Enemy 50+ naturally reach 2nd reshuffle)
- Short fights: Just base 20/15 (decent)
- Long fights: Full 35/25 stats (strong Rare power level)
- Scales naturally with enemy difficulty

**Condition Details:**
- Type: Timing (reshuffle count)
- Coefficient: 0.5 (Often True, per conditional-mechanics.md)
- Trigger timing: ~18 seconds into 8-card deck combat
- Always visible: Reshuffle counter shown in UI

**Design Decision (2025-11-15):**
- User approved timing-based conditional
- Coefficient 0.5 approved as starting point

---

## Pack 2 Strategic Summary

### Card Distribution
- 2 Generators: Steady Channeling, Offensive Siphon
- 1 Burst+Combat Hybrid: Arcane Reservoir
- 2 Rare Conditionals: Arcane Synergy (sequence), Battle Focus (timing)

### Mechanics Taught
✅ Sequence tracking (previous card type)  
✅ Timing-based conditionals (reshuffle count)  
✅ Generator penalty variety (ATK and DEF penalties)  
✅ Hybrid generator variety (defensive burst, offensive rate)

### Power Curve Impact
- Before Pack 2: 13 cards owned, 12-card deck
- After Pack 2: 18 cards owned, 12-card deck (must cut 6)
- 3 total conditional cards available (Battle Surge, Arcane Synergy, Battle Focus)
- Expected to reach Enemy 100 (Mini-Boss #2) more reliably

### Design Space Reserved for Pack 3
❌ Deck manipulation ("Draw extra card")  
❌ Complex sequences ("Last 3 cards were all X")  
❌ Multiple conditions (AND/OR logic)  
❌ Stat relationship conditionals ("If ATK > DEF")  
❌ Scaling "For each X, +Y" conditionals

---

## Files Modified

### Created
- `game-data/cards-pack2.json` - Authoritative source for Pack 2 card stats

### Updated
- `docs/design-specs/card-system.md` - Added Pack 2 specification section
- `docs/design-specs/card-system.md` - Updated Document History to Version 1.4

---

## Validation

### Design Constraints Met
- ✅ All Commons have flat values (no conditions)
- ✅ All Rares have simple single conditions
- ✅ No strictly better cards (all have tradeoffs)
- ✅ Maintains "vanilla filler" philosophy
- ✅ Introduces sequence tracking (previous card)
- ✅ Introduces timing conditionals (reshuffle count)

### Stat Budget Validation
- Arcane Reservoir: 23 points (Common 20-30) ✅
- Steady Channeling: 27 points (Common 20-30) ✅
- Offensive Siphon: 25 points (Common 20-30) ✅
- Arcane Synergy: 43 points (Rare 30-50) ✅
- Battle Focus: 47.5 points (Rare 30-50) ✅

### "Not Strictly Better" Check
- Arcane Reservoir vs Essence Burst: Less burst (200 vs 250) ✅
- Arcane Reservoir vs Combat Siphon: No rate generation ✅
- Steady Channeling vs Arcane Conduit: Higher rate but has penalty ✅
- Steady Channeling vs Essence Drain: Same rate, different penalty ✅
- Offensive Siphon vs Arcane Conduit: Lower rate (1 vs 2) ✅
- Offensive Siphon vs Combat Siphon: Same rate, less total combat, unbalanced ✅
- Arcane Synergy vs Battle Surge: Different condition types, similar power ✅
- Battle Focus vs Battle Surge: No essence generation, different condition ✅

---

## Key Design Decisions

### Decision 1: Commons Remain Flat Values
**Reasoning:** Maintains simplicity, complexity introduced only through Rares  
**Impact:** Commons are straightforward deck fillers, Rares add strategic depth

### Decision 2: "Previous Card" First Sequence Mechanic
**Reasoning:** Simplest sequence tracking, easiest to understand  
**Impact:** Introduces sequence UI, teaches deck composition awareness

### Decision 3: Defensive Penalty Generator (Steady Channeling)
**Reasoning:** Completes penalty generator set with Essence Drain  
**Impact:** Players choose penalty based on build (offense vs defense)

### Decision 4: Offensive Siphon Rate Reduction
**Original:** +2/sec, +10 ATK (strictly better than Arcane Conduit)  
**Fixed:** +1/sec, +15 ATK (clear tradeoff: rate vs ATK)  
**Reasoning:** User caught strictly-better violation  
**Impact:** Now creates meaningful choice between Arcane Conduit and Offensive Siphon

### Decision 5: Timing-Based Conditional (Battle Focus)
**Reasoning:** Different from state-based (Battle Surge), teaches reshuffle awareness  
**Impact:** Rewards longer fights, scales naturally with difficulty

---

## Next Steps

Per CHECKLIST.md Task 2.1.9:
- Design Pack 3 guaranteed cards (2 Commons + 2 Rares + 1 Epic)
- Introduce complex conditionals (AND/OR, multiple thresholds)
- Validate stat budgets per rarity

---

## Completion Summary

**Task Status:** COMPLETE  
**Completion Time:** 2025-11-15 12:41:34

**Deliverables:**
1. ✅ 5 Pack 2 cards designed (3 Commons, 2 Rares)
2. ✅ Sequence tracking introduced (Arcane Synergy)
3. ✅ Timing conditionals introduced (Battle Focus)
4. ✅ Generator variety expanded (penalty alternatives, hybrid options)
5. ✅ game-data/cards-pack2.json created
6. ✅ docs/design-specs/card-system.md updated with Pack 2 section
7. ✅ All cards validated against design constraints

**Key Achievements:**
- First sequence-tracking card in game (Arcane Synergy)
- First timing-based conditional in game (Battle Focus)
- Completed penalty generator set (ATK and DEF penalties)
- Maintained "vanilla filler" philosophy throughout
- All cards have clear tradeoffs (no strictly better violations)

**User Approvals:**
- ✅ Pack 2 design direction approved
- ✅ "Previous card" as first sequence mechanic approved
- ✅ Commons with flat values approved
- ✅ Rares with simple conditions approved
- ✅ Negative effects for Steady Channeling approved
- ✅ Offensive Siphon fix (+1/sec, +15 ATK) approved
- ✅ Coefficients 0.4 and 0.5 approved as starting points

---

## Final Work Log Entry

**Timestamp:** 2025-11-15 12:45:00

**Action Taken:**
- Completed Pack 2 card design with user approval
- Created game-data/cards-pack2.json with all 5 cards
- Updated docs/design-specs/card-system.md with Pack 2 section (Version 1.4)
- Fixed Offensive Siphon to avoid strictly-better violation
- Created comprehensive task log

**Files Impacted:**
- Created: `game-data/cards-pack2.json` (full card specifications)
- Modified: `docs/design-specs/card-system.md` (added Pack 2 section, updated history)
- Created: `.cursor/log/sessions/session-2-1-8-pack2-design.md` (this log)

**Rationale:**
- Pack 2 needed to introduce sequence tracking and timing conditionals
- Maintained "vanilla filler" philosophy per user requirement
- All Commons kept flat values (no conditions)
- Rares introduced new mechanics with simple single conditions
- Fixed Offensive Siphon after user caught strictly-better violation

**Validation:**
- All stat budgets within rarity ranges (Common 20-30, Rare 30-50)
- No strictly better cards found in final review
- All cards have clear tradeoffs vs existing cards
- No linter errors in JSON or markdown files
- User approved all design decisions and final cards

**User Confirmations:**
- ✅ "Previous card" as first sequence mechanic
- ✅ Commons with no conditions
- ✅ Rares with simple conditions
- ✅ Arcane as "vanilla" filler cards
- ✅ Negative effect for Steady Channeling
- ✅ Offensive Siphon fix (Option B: +1/sec, +15 ATK)
- ✅ Final Pack 2 design approved

**Task Complete:** Ready to proceed to Pack 3 design (Task 2.1.9) when user requests

---

**Task Log Complete**

