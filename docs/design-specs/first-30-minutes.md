# First 30 Minutes Experience

**Last Updated:** 2025-11-08  
**Status:** Complete (Session 1.3A)  
**Parent Document:** [DESIGN.md](../../DESIGN.md)

---

## Starting State: Arcane Student

### Initial Setup

- All players start as "Arcane Student" (no class choice yet)
- Pre-built 8-card starter deck (Arcane-only)
- Apprentice class cards (Fire, Water, Earth, Air) pre-owned but locked until first prestige
- No elemental cards accessible before prestige

---

## Gameplay Phases (Guided Discovery)

### Phase 1: First Contact (Minutes 0-5)

**Experience:**
- Immediate gameplay, no menus or tutorials
- Watch combat loop: cards draw → power builds → enemy appears → victory → essence
- First mechanic: Automatic card draw and combat
- First resource: Arcane Essence starts accumulating from victories and generator draws

**Goal:** Understand basic combat loop through observation

**What Players See:**
- Cards drawing one by one from deck (1 card/second)
- Attack and Defense stats building up with each card
- **Deck reshuffles and cycles continuously** - stats keep accumulating
- Enemies spawning every 12 seconds
- Combat resolves tick-by-tick (not instant) - enemies take damage gradually
- Enemies attack back immediately from tick 0 (player HP decreases)
- Essence counter increasing
- Generator cards adding to Essence/sec rate

**Milestone:** First Blood (Minute 3) - First enemy defeated

### Phase 2: Discovery (Minutes 5-12)

**Experience:**
- Shop unlocks when 50 Essence reached
- First pack purchased and opened (5 cards)
- Collection view unlocks
- Examine card variety (combat, generators, utilities)
- Deck building unlocks after first pack
  
**Goal:** Learn spending resources and collecting cards

**What Players Learn:**
- Essence is spent on packs
- Packs contain random cards
- Cards have different types (generators, combat, utilities)
- Collection grows with pack purchases
- Deck building is possible

**Milestones:**
- **Merchant Unlocked (Minute 6):** First pack purchased
- **Deck Builder (Minute 13):** First deck modification

### Phase 3: Choice (Minutes 12-20)

**Experience:**
- First deck modification (choose which cards to include)
- See immediate impact in combat
- Passive generation becomes visible if generators included
- Second pack purchased (~50 more Essence)
- Strategic thinking emerges (economy vs combat focus)

**Goal:** Experience agency and strategic choice

**What Players Experiment With:**
- Swapping cards in/out of deck
- Balancing generators vs combat cards
- Seeing how deck changes affect power accumulation
- Understanding that more generators = more essence

**Milestone:** Generator (Minute 16) - Passive income established

### Phase 4: Mastery & Glimpse Beyond (Minutes 20-30)

**Experience:**
- Enemy difficulty scales (more health, better rewards)
- Third pack purchased
- Deck optimization (approaching 20-card limit)
- Glimpse of future systems (locked class cards hint at prestige)
- Milestone reached: "Tower Defender I"

**Goal:** Feel competent and curious about progression

**What Players Notice:**
- Combat getting longer (enemies have more HP)
- Strategy matters (deck composition affects success)
- More packs available to purchase
- Hints of future content (class cards grayed out)
- Clear progression path emerging

**Milestones:**
- **Optimization (Minute 25):** Full 20-card deck built
- **Glimpse Beyond (Minute 28):** Aware of prestige/class systems

---

## Key Milestones Summary

1. **First Blood** (Minute 3): First enemy defeated
2. **Merchant Unlocked** (Minute 6): First pack purchased
3. **Deck Builder** (Minute 13): First deck modification
4. **Generator** (Minute 16): Passive income established
5. **Optimization** (Minute 25): Full 20-card deck built
6. **Glimpse Beyond** (Minute 28): Aware of prestige/class systems

---

## Progression Gates (Soft, Time-Based)

### Gate 1 (Minute 5-6)

**Condition:** Accumulate 50 Essence  
**Unlock:** Pack purchasing

**Experience:**
- Natural accumulation from generator draws
- No forced waiting - just playing the game
- Shop button appears when affordable

### Gate 2 (Minute 11-12)

**Condition:** Own more cards than starter deck  
**Unlock:** Deck building

**Experience:**
- Happens automatically after first pack
- Collection naturally exceeds 8 cards
- Deck management UI appears

### Gate 3 (Minute 20+)

**Condition:** Multiple packs + refinement  
**Unlock:** Awareness of future systems

**Experience:**
- Locked class cards visible in collection
- Tooltips hint at prestige system
- Player naturally curious about next steps

**No Hard Gates:**
- Combat continues regardless
- Resources accumulate automatically
- Player-driven pacing throughout

---

## Design Philosophy Applied

### Guided Discovery (No Hand-Holding)

**Systems reveal themselves through visual feedback:**
- No tutorial popups or forced explanations
- Complexity expands naturally (observe → explore → act → optimize)
- New UI elements appear when relevant, not forced
- Player discovers mechanics through gameplay

**Example:**
- Deck building doesn't appear until you have enough cards to make choices meaningful
- Shop doesn't appear until you can afford something
- No explanations - UI is self-evident

### Emotional Arc

**Minutes 0-5:** Curiosity ("What's happening?")
- Watching unfamiliar systems
- Figuring out what cards do
- Understanding combat flow

**Minutes 5-15:** Discovery ("I can do things!")
- Opening first pack
- Seeing new cards
- Making first deck changes

**Minutes 15-25:** Mastery ("I'm getting better!")
- Optimizing deck composition
- Seeing strategy pay off
- Building stronger essence generation

**Minutes 25-30:** Ambition ("What's next?")
- Hints of deeper systems
- Locked content tantalizing
- Clear progression path ahead

---

## End State (Minute 30)

### Player Progress

- 3-4 packs opened (25-28 cards owned)
- 20-card optimized Arcane deck
- ~5-7 Essence/sec passive generation rate
- Consistent combat victories against scaled enemies
- Aware of prestige and class systems (but not accessible)
- Reached Enemy 60 (~30 minute mark)

### Player Understanding

- **Combat loop mastery:** Cards draw → stats accumulate → **deck cycles continuously** → exponential power growth
- **Continuous cycling:** Deck reshuffles every 9 seconds (8 cards + 1s cooldown), stats stack indefinitely
- **Resource economy:** Essence from generators, shards from victories
- **Deck building strategy:** Generator/combat balance matters
- **Progression path:** Packs → cards → deck → power
- **Long-term goals visible:** Prestige, classes, elements

### Player Feeling

- **Competent** with core systems
- **Curious** about next progression steps
- **Satisfied** with first session progress
- **Motivated** to continue playing

---

## Critical Design Decisions for First 30 Minutes

### Pack Cost Scaling (Session 1.3)

**Formula:** `50 × 1.5^n` → Later adjusted to `40,000 × 2.5^(n-1)`

**Why:** Creates natural pacing, prevents runaway progression  
**Effect:** Each pack feels earned

### Guaranteed Cards (Session 1.3)

**First 2 packs have fixed distributions:**
- **Pack 1:** 2 generators, 2 combat, 1 utility
- **Pack 2:** 1 generator, 3 combat, 1 rare synergy
- **Pack 3+:** Random

**Why:** Ensures consistent experience and teaches card variety  
**Effect:** All players see generator types and combat variety

### Defense Mechanics (Session 1.3, Updated 2.1.2B)

- Defense stat exists on cards
- **All enemies attack from tick 0** (immediate combat threat)
- Defense reduces damage taken each tick
- No safe tutorial phase - learning through death is acceptable
- Strategy critical from first enemy

**Why:** Death is part of the core loop, no penalty for dying early  
**Effect:** Players learn combat mechanics through experience

### Class Cards (Session 1.3)

- All 4 Apprentice classes pre-owned from start
- Grayed out with "Unlocked after first prestige" tooltip
- Creates visible long-term goal
- Unlocked automatically on first prestige

**Why:** Shows progression path without overwhelming  
**Effect:** Curious about future content

---

## Pacing Validation

See [baseline-numbers.md](baseline-numbers.md) for detailed timing validation.

**Validated Milestones (Task 2.0):**
- Pack 1: ~7 minutes (40,000 Essence)
- Pack 2: ~12 minutes (100,000 Essence)
- Pack 3: ~19 minutes (250,000 Essence)
- Enemy 50: ~23 minutes (Mini-Boss #1)
- Enemy 60: ~30 minutes (session milestone)

---

## Notes for Implementation

### Visual Feedback Requirements

- Clear essence counter with rate display
- Card draw animation (fast but visible)
- Enemy spawn notification
- Victory celebration (brief)
- Pack opening excitement (medium)

### UI Reveal Timing

- **Minute 0:** Combat view only
- **Minute 6:** Shop button appears
- **Minute 12:** Deck building UI appears
- **Minute 20+:** Collection filters and sorting

### Accessibility

- No time pressure
- Can pause/resume
- All information visible
- No hidden mechanics
- Clear visual hierarchy

---

## Document History

**Version 1.1** (2025-11-09) - Synchronization Update
- Updated defense mechanics to reflect per-tick enemy attack system (all enemies attack from tick 0)
- Added continuous deck cycling clarifications
- Updated combat description (tick-by-tick resolution)
- Aligned with Session 2.1.2B design decisions

**Version 1.0** (2025-11-08) - Split from DESIGN.md Version 1.9  
- Extracted First 30 Minutes Experience section (Session 1.3A)
- Includes gameplay phases, milestones, and emotional arc
- Status: Complete specification for new player experience

