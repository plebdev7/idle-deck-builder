# Task 2.1.1: Card Rarity System Research

**Session:** 2.1.1 - Card Rarity System Design (Phase 1: Foundation Research)  
**Date:** 2025-11-08  
**Status:** In Progress - Research & Discussion  
**Related:** CHECKLIST.md Task 2.1.1, ROADMAP.md Session 2.1

---

## Session Goal

Define the 4-tier card rarity system (Common/Rare/Epic/Legendary) including:
- Stat multipliers and power scaling
- Drop rates from packs
- Relationship between rarity and card leveling
- Mechanical complexity vs raw power
- Pack distribution strategies
- Elemental tier interactions

---

## Pre-Session Context

### Established Constraints

**From Existing Systems:**
- Card leveling system exists (duplicates used for something - XP? Fusion?)
- 4-tier rarity system decided: Common / Rare / Epic / Legendary
- Ultra-rare/unique cards deferred to future (post-online support)
- First 2-3 packs are deterministic (same cards every time)
- Arcane tier is foundational and remains active forever

**From Baseline Numbers:**
- Starter deck: 8-15 total stats per card (all Common)
- Pack 1 target: 25-30 total stats
- Pack 2 target: 35-45 total stats
- Pack 3+ Rare: 50-80 total stats
- Pack 3+ Epic: 100-150 total stats

**Pack Costs:**
- Pack 1: 40,000 Essence (~7 min)
- Pack 2: 100,000 Essence (~12 min)
- Pack 3: 250,000 Essence (~19 min)
- Pack 4: 625,000 Essence (2.5× scaling)

---

## Research Questions

### Question 1: Leveling vs Rarity Progression

**Core Question:** Should a Common card at Level 10 be stronger than a Rare card at Level 1?

#### Option A: Rarity Dominates (Rare L1 > Common L10)

**How it works:**
- Rarity determines base power tier
- Leveling provides incremental improvements within tier
- Higher rarity cards are always stronger baseline
- Example: Common L10 = 30 stats, Rare L1 = 35 stats

**Pros:**
- Finding a higher rarity card always feels good (immediate upgrade)
- Rarity hierarchy is clear and consistent
- Encourages pursuing higher rarity cards
- Simpler to balance (rarities are distinct power tiers)

**Cons:**
- Common cards become obsolete once Rare cards drop
- Leveling feels less impactful
- Effort invested in leveling Commons feels wasted
- Lower deck diversity late game (everyone uses highest rarity)

**Appropriate for games with:**
- Heavy RNG card acquisition
- Short progression cycles
- Focus on collection completeness
- Frequent card replacement

#### Option B: Leveling Can Surpass Rarity (Common L10 > Rare L1)

**How it works:**
- Rarity determines starting power and scaling rate
- Leveling provides significant improvements
- Investment in any card can pay off long-term
- Example: Common L10 = 40 stats, Rare L1 = 35 stats, Rare L10 = 70 stats

**Pros:**
- Cards you invest in remain relevant
- Leveling feels impactful and rewarding
- Early cards don't become useless
- More strategic decisions (level existing vs acquire new)
- Supports "main deck" concept (investment in favorites)

**Cons:**
- Finding higher rarity cards feels less exciting if existing cards leveled
- More complex to balance (intersection points matter)
- Players might "over-invest" in suboptimal cards
- Harder to communicate power levels at a glance

**Appropriate for games with:**
- Deterministic progression
- Long-term investment systems
- "Main deck" or "signature build" emphasis
- Strategic resource allocation

#### Analysis for Our Game

**Factors Favoring Option B (Leveling Can Surpass):**
1. **Deterministic Packs 1-3:** Players get same cards, can plan investments
2. **Death Loop Core Gameplay:** Investment and iteration are central themes
3. **Long Progression:** 4-6 loops to beat first boss means long-term deck building
4. **Arcane Forever:** Foundation tier needs to remain relevant with elemental tiers
5. **Strategic Depth:** More interesting if players must decide between leveling vs replacing

**Factors Favoring Option A (Rarity Dominates):**
1. **Pack Cost Scaling (2.5×):** Higher packs need to feel valuable
2. **Rarity Excitement:** Finding Epic/Legendary needs to feel special
3. **Progression Clarity:** Easier to understand "bigger number = better"
4. **Collection Incentive:** Encourages opening packs for upgrades

**Hybrid Approach - Staged Dominance:**
- Common L10 ≈ Rare L1 (similar power, different mechanics)
- Rare L10 >> Common L10 (clear endgame winner)
- Each rarity has "competitive range" where they overlap
- Leveling matters, but diminishing returns vs next rarity tier

**Example Stat Scaling (Hybrid):**
```
Common: 25 → 30 → 35 → 40 → 45 (L1 → L10, 20% growth per level)
Rare:   35 → 42 → 49 → 56 → 63 (L1 → L10, 20% growth per level)
Epic:   55 → 70 → 85 → 100 → 115 (L1 → L10, 20% growth per level)
Legend: 85 → 110 → 135 → 160 → 185 (L1 → L10, 20% growth per level)

Overlap zones:
- Common L10 (45) ≈ Rare L4 (47)
- Rare L10 (63) ≈ Epic L3 (61)
- Epic L10 (115) ≈ Legend L3 (110)
```

**Recommendation:** **Hybrid Approach - Staged Dominance**

**Rationale:**
- Leveling feels meaningful (20% growth = significant)
- Rarity upgrades still exciting (30-40% base power jump)
- Common cards useful early/mid game, Rare+ dominate endgame
- Supports both "invest in favorites" AND "chase new cards"
- Aligns with death loop progression (gradual improvements)

---

### Question 2: What Do "Ranges" Mean?

**Context:** Checklist mentions "Specify rarity stat multipliers and ranges per rarity"

#### Interpretation A: Stat Value Ranges (Randomness)

**Description:** Cards have stat ranges rather than fixed values
- Common card might be 25-30 stats
- Each copy of same card rolled independently
- Creates variety but also RNG frustration

**Verdict:** ❌ **NOT RECOMMENDED**
- Adds frustration without strategic depth
- Conflicts with deterministic Pack 1-3 philosophy
- Complicates leveling system
- Players want consistency

#### Interpretation B: Level Cap Ranges

**Description:** Different rarities have different max levels
- Common: Max Level 10
- Rare: Max Level 15
- Epic: Max Level 20
- Legendary: Max Level 25 (or unlimited?)

**Pros:**
- Clear rarity differentiation
- Higher rarity = more growth potential
- Creates upgrade path (Common → Rare unlocks more levels)
- Supports long-term progression

**Cons:**
- Complexity in communication
- Why can't I level my favorite Common to 20?
- Requires careful balance (don't make caps feel arbitrary)

**Verdict:** ✅ **CONSIDER** - Good differentiation mechanic

#### Interpretation C: Rarity-Based Stat Ranges (Design Space)

**Description:** Rarity determines which stat budgets designers can use
- Commons: 20-50 total stats
- Rares: 40-80 total stats
- Epics: 70-150 total stats
- Legendaries: 120-300 total stats

**Purpose:** Design guideline, not player-facing mechanic
- Ensures power curve consistency
- Allows variance within tier
- Some Commons can be "budget Rares"

**Verdict:** ✅ **ESSENTIAL** - This is what "ranges" should mean

#### Interpretation D: Copy Limits for Prestige/Rank-Up

**Description:** Number of copies needed varies by rarity
- Common: 10 copies to max out
- Rare: 20 copies to max out
- Epic: 50 copies to max out
- Legendary: 100 copies to max out

**Purpose:** Higher rarity = more investment to max
**Problem:** Conflicts with deterministic packs and scarcity

**Verdict:** ❌ **NOT RECOMMENDED** - Makes Legendaries feel bad

**Recommendation:** **Interpretation C (Design Space) + Optional Interpretation B (Level Caps)**

**Proposed System:**
- "Ranges" = design budget guidelines (stat totals per rarity)
- Level caps differentiate rarities (Common L10, Rare L15, Epic L20, Legend L25)
- Stats are fixed per card (no RNG rolls)
- Copy requirements for leveling can be tuned per rarity

---

### Question 3: Strictly Better vs Mechanically Unique

**Core Question:** Should rarity determine raw power or mechanical complexity?

#### Option A: Strictly Better (Power Creep by Design)

**Description:** Higher rarity = same effect, bigger numbers
- Common: +3 Essence/sec
- Rare: +6 Essence/sec (same mechanic, double power)
- Epic: +12 Essence/sec
- Legendary: +24 Essence/sec

**Pros:**
- Simple to understand
- Clear upgrade path
- Easy to balance (just scale numbers)

**Cons:**
- Lower rarities become obsolete
- Boring card design
- No build diversity
- "Solved" optimal decks

**Verdict:** ❌ **AVOID** - Leads to stale meta

#### Option B: Mechanically Unique (Complexity = Rarity)

**Description:** Higher rarity = more complex/interesting mechanics
- Common: +3 Essence/sec (simple rate generator)
- Rare: +3 Essence/sec + 10 ATK if drawn in first 10 seconds (conditional)
- Epic: +(Current rate × 5 seconds) Essence (multiplier generator)
- Legendary: +5 Essence/sec + Draw an extra card + All generators gain +1 (complex combo)

**Pros:**
- Every rarity has a role
- Build diversity
- Interesting deck building decisions
- Higher rarity = more options, not just bigger numbers

**Cons:**
- Harder to balance
- Power level less obvious
- New players might struggle with complex cards
- Risk of power creep through mechanics

**Verdict:** ✅ **STRONGLY RECOMMENDED** - Core to good card game design

#### Option C: Hybrid (Power + Complexity)

**Description:** Higher rarity = more powerful AND more complex
- Common: +3 Essence/sec, 25 total stats
- Rare: +5 Essence/sec + 15 ATK, 40 total stats (conditional bonus)
- Epic: +(Rate × 5s) Essence + 20/20 stats, 70 total stats (multiplier)
- Legendary: Complex multi-effect card, 120+ total stats

**Pros:**
- Best of both worlds
- Clear power progression
- Complexity rewards skill
- Casual players can use simple commons, experts can leverage complex legendaries

**Cons:**
- Risk of high rarity being "strictly better" in all cases
- Must carefully balance to avoid obsolescence

**Verdict:** ✅ **BEST APPROACH** - Power + Complexity scaling together

**Proposed Design Philosophy:**

**Common Rarity:**
- **Role:** Foundational, simple, always useful
- **Power:** 20-50 total stats
- **Complexity:** Flat values, no conditions
- **Examples:** Rate generators, pure attack/defense cards
- **Design Goal:** Reliable, straightforward, deck building blocks

**Rare Rarity:**
- **Role:** Enhanced versions with conditionals
- **Power:** 40-80 total stats (1.5-2× Common)
- **Complexity:** Simple conditionals ("If X, then bonus Y")
- **Examples:** Conditional generators, situational combat cards
- **Design Goal:** Rewards timing and deck composition choices

**Epic Rarity:**
- **Role:** Build-around cards, combo enablers
- **Power:** 70-150 total stats (2-3× Common)
- **Complexity:** Multiple effects, sequencing, state-based
- **Examples:** Multiplier generators, combo triggers, deck manipulation
- **Design Goal:** Enables new strategies and deck archetypes

**Legendary Rarity:**
- **Role:** Deck-defining powerhouse cards
- **Power:** 120-300 total stats (4-6× Common)
- **Complexity:** Complex multi-effects, transformation effects
- **Examples:** "Draw 2 extra cards + generators gain +2 rate + 30/30 stats"
- **Design Goal:** Exciting, memorable, changes how you play

**Key Principle:** **Lower rarity cards remain useful even when you own higher rarities**
- Commons excellent for consistent baseline power
- Rares offer situational power spikes
- Epics enable specific strategies
- Legendaries are explosive but require setup

---

### Question 4: Pack Rarity Distribution

**Core Question:** Should all packs have the same rarity distribution, or should different pack types/editions have different rates?

#### Current Pack Types (from DESIGN.md)

**Arcane Packs:**
- Cost: Arcane Essence
- Contains: Arcane cards, Common class cards, Rare classes (low chance)
- Always available

**Elemental Packs:**
- Cost: Elemental Essence
- Contains: Element cards, Epic classes (rare), Legendary (very rare)
- Unlock after tier unlocked via class

**Special Packs:**
- Premium packs, event packs, milestone rewards

#### Option A: Uniform Rarity Distribution

**Description:** All pack types use same rarity weights
- Example: 70% Common, 20% Rare, 8% Epic, 2% Legendary
- Applies to Arcane packs, Elemental packs, Special packs

**Pros:**
- Simple to understand
- Predictable expectations
- Fair across all pack types

**Cons:**
- No differentiation between pack types
- No sense of progression in pack "quality"
- Elemental packs feel the same as Arcane packs

**Verdict:** ❌ **TOO SIMPLE** - Misses opportunity

#### Option B: Tiered Pack Quality

**Description:** Different pack types have different rarity distributions

**Example Distribution:**
```
Arcane Packs (Entry-level):
- 70% Common, 20% Rare, 8% Epic, 2% Legendary
- Focus: Build foundational deck

Elemental Packs (Mid-tier):
- 50% Common, 30% Rare, 15% Epic, 5% Legendary
- Focus: Better rarity rates, elemental cards

Special/Premium Packs (High-tier):
- 30% Common, 35% Rare, 25% Epic, 10% Legendary
- Focus: Chase high-rarity cards
```

**Pros:**
- Clear progression in pack value
- Elemental packs feel special
- Incentivizes advancing to elemental tiers
- Creates "luxury" pack options

**Cons:**
- More complex to balance
- Risk of Arcane packs feeling "bad"
- Could invalidate Arcane tier

**Verdict:** ✅ **RECOMMENDED** - With careful balance

#### Option C: Edition-Based (Same Rarity, Different Cards)

**Description:** All packs have same rarity distribution, but different card pools
- Arcane Pack: Arcane tier cards only
- Fire Pack: Fire tier cards only
- Water Pack: Water tier cards only
- Each pool has all rarities represented

**Pros:**
- Fair rarity rates across all packs
- Differentiation through card content, not rates
- No "worse" pack types
- Supports tier diversity

**Cons:**
- Less excitement differentiation
- All packs feel similar

**Verdict:** ✅ **SOLID BASELINE** - Can combine with Option B

**Proposed System: Hybrid Tiered + Edition-Based**

**Arcane Packs (Foundation Tier):**
- Cost: 40,000 × 2.5^(n-1) Arcane Essence
- Rarity: 70% Common, 20% Rare, 8% Epic, 2% Legendary
- Contents: Arcane tier cards + Common class cards
- Packs 1-3: Deterministic (specific cards)
- Pack 4+: Random from Arcane pool

**Elemental Packs (Specialized Tier):**
- Cost: 50,000 × 2.5^(n-1) Elemental Essence (slightly more expensive)
- Rarity: 50% Common, 30% Rare, 15% Epic, 5% Legendary (better rates!)
- Contents: Specific element cards + Rare/Epic class cards
- All packs: Random from element pool

**Premium Packs (Special):**
- Cost: Shards or special currency
- Rarity: 20% Common, 30% Rare, 35% Epic, 15% Legendary (best rates!)
- Contents: Cross-tier cards, special cards
- Acquisition: Milestones, achievements, shop

**Progression Incentive:**
- Arcane packs accessible early, build foundation
- Elemental packs better rates, but require elemental essence (conversion)
- Premium packs chase high-rarity, limited acquisition

---

### Question 5: Elemental Cards and Rarity

**Core Question:** Should all elements appear at all rarities, or should some elements be rarity-gated?

#### Background Context

**5 Elements:**
- Arcane (Gray) - Foundation
- Fire (Red) - Aggressive
- Water (Blue) - Adaptive
- Earth (Green) - Defensive
- Air (Yellow) - Swift

**Future Expansion Possibility:** Additional elements/hybrids
- Lightning, Ice, Shadow, Light, etc.

#### Option A: All Elements, All Rarities

**Description:** Every element has Common, Rare, Epic, Legendary cards

**Example:**
```
Fire Element:
- Common: Flame Strike (basic attack)
- Rare: Inferno Burst (conditional high attack)
- Epic: Wildfire Cascade (attack + DoT combo)
- Legendary: Phoenix Rebirth (complex resurrection effect)
```

**Pros:**
- Complete card pools for each element
- Supports all deck archetypes at any rarity
- Easier to balance (all elements equal)
- Flexibility in deck building

**Cons:**
- Huge card pool to design
- Less differentiation between elements
- No sense of "advanced" vs "basic" elements

**Verdict:** ✅ **BEST FOR CORE 5 ELEMENTS**

#### Option B: Rarity-Gated Elements (Basic vs Advanced)

**Description:** Basic elements (Fire, Water, Earth, Air) have all rarities. Advanced elements (Lightning, Shadow, etc.) only appear at Rare+

**Example:**
```
Basic Elements (All Rarities):
- Fire, Water, Earth, Air: Common → Legendary
- Arcane: Common → Legendary (foundation)

Advanced Elements (Rare+ Only):
- Lightning: Rare → Legendary
- Shadow: Epic → Legendary
- Prismatic: Legendary only
```

**Pros:**
- Creates sense of progression
- Advanced elements feel special
- Smaller core card pool (easier to balance)
- Room for expansion

**Cons:**
- Confusing (why no common Lightning cards?)
- Limits deck building options
- Could feel arbitrary

**Verdict:** ✅ **GOOD FOR FUTURE EXPANSION ELEMENTS**

#### Option C: Hybrid Element Complexity

**Description:** All elements have all rarities, but advanced elements skew toward higher rarity

**Example:**
```
Basic Elements (Even Distribution):
- 35% Common, 30% Rare, 25% Epic, 10% Legendary

Advanced Elements (High-Rarity Skew):
- 10% Common, 25% Rare, 40% Epic, 25% Legendary
```

**Pros:**
- All elements accessible to all players
- Advanced elements naturally appear less often at low levels
- Organic progression feeling
- Room for expansion

**Cons:**
- More complex to balance
- Pack contents less predictable

**Verdict:** ✅ **INTERESTING OPTION** - Natural progression through rarity

**Proposed Approach:**

**Phase 1 (Current - Arcane Tier + 4 Elements):**
- **All 5 elements (Arcane, Fire, Water, Earth, Air) have all rarities**
- Even distribution of rarities within each element
- Complete card pools for core elements

**Phase 2 (Future - Advanced Elements):**
- **Advanced elements (Lightning, Shadow, Ice, Light, etc.) start at Rare+**
- No common versions of advanced elements
- Creates clear "basic" vs "advanced" element distinction
- Rewards progression with access to complex elements

**Rationale:**
- Core 5 elements should be fully accessible (matches tier system)
- Future advanced elements can be prestige rewards / late-game content
- Arcane remains foundation (always relevant, all rarities)
- Clean design now, room for expansion later

---

## Summary of Recommendations

### 1. Leveling vs Rarity
**Decision:** **Hybrid - Staged Dominance**
- Leveling provides meaningful growth (20% per level)
- Rarity provides 30-40% base power jump
- Common L10 ≈ Rare L4 (overlap zones exist)
- Higher rarity dominates at max level

### 2. Stat Ranges
**Decision:** **Design Budget Guidelines + Level Caps**
- Ranges = design space (stat totals per rarity, not randomness)
- Level caps: Common L10, Rare L15, Epic L20, Legendary L25
- Fixed stats per card (no RNG rolls)

### 3. Rarity Design Philosophy
**Decision:** **Power + Complexity Hybrid**
- Commons: Simple, reliable, 20-50 stats
- Rares: Conditional effects, 40-80 stats
- Epics: Build-around mechanics, 70-150 stats
- Legendaries: Deck-defining, 120-300 stats
- Lower rarities remain useful through simplicity

### 4. Pack Rarity Distribution
**Decision:** **Tiered Pack Quality**
- Arcane Packs: 70/20/8/2 (Common/Rare/Epic/Legendary)
- Elemental Packs: 50/30/15/5 (better rates, requires elemental essence)
- Premium Packs: 20/30/35/15 (best rates, special acquisition)

### 5. Elemental Cards and Rarity
**Decision:** **All Core Elements at All Rarities**
- Arcane, Fire, Water, Earth, Air: Common → Legendary
- Future advanced elements: Rare+ only
- Even distribution within core elements

---

## Next Steps

1. **Create detailed stat scaling tables** (Common L1-L10, Rare L1-L15, etc.)
2. **Define rarity drop rates precisely** (guaranteed vs random slots)
3. **Document in DESIGN.md** (update Outstanding Questions, add Rarity System section)
4. **Proceed to Task 2.1.2** (Power Curve Analysis with these numbers)

---

## User Decisions (2025-11-08 15:15:00)

### 1. Level Caps → NO CAPS (APPROVED ALTERNATIVE)

**Decision:** No level caps at all, just increasingly expensive to level up

**Rationale:**
- Gives value to duplicates forever (continuous pack opening incentive)
- Rarity differentiation sufficient through base stats and complexity
- Simpler system (no arbitrary caps)
- Better for long-term progression loop

**Implication:** 
- All rarities can level indefinitely
- Cost scaling ensures diminishing returns naturally
- Rare/Epic/Legend still dominate through higher base stats and better scaling rates

**Updated Recommendation:**
```
Leveling Cost Scaling (per rarity):
Common: Base cost × level (linear)
Rare: Base cost × level^1.2 (slight exponential)
Epic: Base cost × level^1.4 (moderate exponential)
Legendary: Base cost × level^1.6 (steep exponential)

Example (if base cost = 5 duplicates):
Common L10: 50 dupes total
Rare L10: ~80 dupes total
Epic L10: ~150 dupes total
Legend L10: ~300 dupes total
```

### 2. Stat Overlap Zones (APPROVED)

**Decision:** Common L10 ≈ Rare L4 balance point approved

**Note:** Balance will be refined through testing, but this starting point is solid.

### 3. Elemental Pack Costs (CLARIFIED)

**Decision:** Elemental packs cost **elemental essence** (not arcane), with their own scaling

**Implication:**
- Arcane Packs: Cost Arcane Essence (40K, 100K, 250K, 625K...)
- Fire Packs: Cost Fire Essence (own scaling, e.g., 50K, 125K, 315K...)
- Water Packs: Cost Water Essence (own scaling)
- Each element has independent pack economy

**Questions to Resolve in Task 2.1.2:**
- Should all elemental packs cost the same? (Fire = Water = Earth = Air?)
- Should elemental packs be more/less expensive than Arcane packs?
- Same 2.5× scaling or different?

### 4. Legendary Complexity (APPROVED)

**Decision:** Legendaries with 3-4 effects per card are fine

**Example Design Space:**
- "Draw 2 extra cards + All generators +2 rate + 30/30 stats + Once per reshuffle"
- Multi-layered effects that change how deck operates
- Not worried about overwhelming new players (Legendaries appear late)

### 5. Leveling System Outline (APPROVED FOR NOW)

**Decision:** Quick sketch now, full design in Task 2.1.3

---

## Finalized Rarity System Design

### Core Stats by Rarity (Level 1 Baseline)

**Common (Foundation):**
- Base Stats: 20-50 total
- Scaling: 20% per level (multiplicative)
- Complexity: Flat values only
- Level Cost: Linear (cheap to max)
- Example L1: 25 stats → L10: 45 stats (1.8× growth)

**Rare (Enhanced):**
- Base Stats: 40-80 total (1.5-2× Common)
- Scaling: 25% per level
- Complexity: Simple conditionals
- Level Cost: Level^1.2 (moderate)
- Example L1: 35 stats → L10: 72 stats (2.06× growth)

**Epic (Build-Around):**
- Base Stats: 70-150 total (2-3× Common)
- Scaling: 30% per level
- Complexity: Multi-effects, combos
- Level Cost: Level^1.4 (expensive)
- Example L1: 55 stats → L10: 156 stats (2.84× growth)

**Legendary (Deck-Defining):**
- Base Stats: 120-300 total (4-6× Common)
- Scaling: 35% per level
- Complexity: 3-4 effects, transformative
- Level Cost: Level^1.6 (very expensive)
- Example L1: 85 stats → L10: 270 stats (3.18× growth)

### Pack Rarity Distribution

**Arcane Packs (Foundation):**
- Cost: Arcane Essence (40K × 2.5^(n-1))
- Distribution: 70% Common, 20% Rare, 8% Epic, 2% Legendary
- Contents: Arcane tier cards + Common class cards
- Packs 1-3: Deterministic (same cards every time)

**Elemental Packs (Specialized):**
- Cost: Respective Elemental Essence (TBD in Task 2.1.2)
- Distribution: 50% Common, 30% Rare, 15% Epic, 5% Legendary
- Contents: Element-specific cards + Rare/Epic class cards
- All packs: Random from element pool
- Better rarity rates than Arcane packs

**Premium Packs (Special):**
- Cost: Shards or special currency
- Distribution: 20% Common, 30% Rare, 35% Epic, 15% Legendary
- Contents: Cross-tier, special edition cards
- Acquisition: Milestones, achievements, limited

### Elemental Rarity Coverage

**Core Elements (All Rarities Available):**
- Arcane, Fire, Water, Earth, Air
- Full Common → Legendary card pools
- Even distribution within each element
- Supports all deck archetypes at any rarity

**Future Advanced Elements (Rare+ Only):**
- Lightning, Shadow, Ice, Light, Hybrid elements
- No Common versions
- Prestige/late-game content
- Creates "basic" vs "advanced" distinction

### Design Philosophy Summary

**Lower rarities remain useful through:**
- Simplicity and consistency (no setup required)
- Cheaper leveling costs (easier to max out)
- Reliable baseline power
- Deck filler and foundations

**Higher rarities excel through:**
- Raw power (higher base stats)
- Better scaling rates (more growth per level)
- Mechanical complexity (conditional bonuses, combos)
- Deck-defining effects (transform strategies)

**Key Principle:** You can level anything indefinitely, but diminishing returns naturally guide you toward higher rarities for endgame optimization.

---

## Quick Leveling System Outline

### Duplicate Card Handling

**System:** XP-Based Leveling (Duplicates = XP)

**How It Works:**
1. Drawing a duplicate card grants XP to that card
2. Each level requires increasing XP (based on rarity)
3. No level caps - can level indefinitely
4. XP requirements scale exponentially with rarity

**XP Values:**
- Common duplicate: 1 XP
- Rare duplicate: 2 XP
- Epic duplicate: 5 XP
- Legendary duplicate: 10 XP

**Level Requirements (XP to next level):**
```
Level 2: 1 × rarity_cost_multiplier
Level 3: 2 × rarity_cost_multiplier
Level 4: 3 × rarity_cost_multiplier
...
Level N: (N-1) × rarity_cost_multiplier

Total XP to Level 10:
Common (1×): 1+2+3+4+5+6+7+8+9 = 45 XP = 45 duplicates
Rare (1.5×): 68 XP = 34 duplicates
Epic (3×): 135 XP = 27 duplicates
Legend (6×): 270 XP = 27 duplicates
```

**Design Note:** Epic/Legend require fewer duplicates due to higher XP per duplicate, but they're much rarer to acquire.

### Alternative: Fusion System (Noted, Not Selected)

**How It Works:**
- Combine N copies of same card to level up
- Level 2 requires 2 copies total (consume 1 duplicate)
- Level 3 requires 3 copies total (consume 2 more)
- Exponential scaling per rarity

**Why Not Selected:** Less flexible, can't mix duplicate values across rarities.

### Full Design Deferred to Task 2.1.3

Questions for later:
- Can you convert duplicates to generic XP?
- Can you scrap unwanted cards for XP?
- Are there alternative level-up methods? (Shards, prestige currency?)
- Does leveling affect card evolution/transformation?

---

**Session Status:** ✅ **COMPLETE** - Ready to proceed to Task 2.1.2 (Power Curve Analysis)

