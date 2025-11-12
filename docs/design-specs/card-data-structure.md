# Card Data Structure & Text Format Specification

**Document Version:** 1.0  
**Date:** 2025-11-11  
**Status:** Complete  
**Related Tasks:** CHECKLIST.md Task 2.1.6

---

## Document Purpose

This document specifies the complete card data structure and text formatting rules for the Idle Deck Builder game. It defines:
1. All card data fields (JSON schema fields explained)
2. Stat notation format for display text
3. Ability description templates with keyword system
4. Text length validation rules (3-line maximum constraint)

**Cross-References:**
- **Card System:** `docs/design-specs/card-system.md` (card types, stat budgets)
- **Conditional Mechanics:** `docs/design-specs/conditional-mechanics.md` (condition types, templates)
- **Visual Style:** `docs/visual-style-guide.md` (card layout, typography)
- **JSON Schema:** `game-data/cards-schema.json` (technical schema)

---

## Card Data Structure

### Complete Field Specification

Every card must have the following fields in its JSON definition:

#### Core Identity Fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | string | ✅ | Unique identifier (snake_case) | `"arcane_conduit"` |
| `name` | string | ✅ | Display name (Title Case) | `"Arcane Conduit"` |
| `tier` | enum | ✅ | Elemental tier | `"Arcane"`, `"Fire"`, `"Water"`, `"Earth"`, `"Air"` |
| `rarity` | enum | ✅ | Card rarity | `"Common"`, `"Rare"`, `"Epic"`, `"Legendary"` |
| `type` | enum | ✅ | Primary card type | `"Generator"`, `"Combat"`, `"Hybrid"`, `"Utility"`, `"Synergy"` |

#### Balance & Effects Fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `stat_point_budget` | number | ✅ | Total stat points for validation | `20` |
| `effects` | array | ✅ | List of effect objects | `[{effect_type: "add_attack", value: 12}]` |
| `ability_text` | string | ✅ | Human-readable description | `"+12 ATK"` |
| `ability_text_short` | string | ⚪ | Compact version for mobile | `"+12 ATK"` |

#### Metadata Fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `flavor_text` | string | ⚪ | Lore/flavor description | `"A stable channel of pure arcane energy."` |
| `acquisition` | object | ✅ | How to obtain this card | `{source: "starter"}` |
| `_design_notes` | string | ⚪ | Internal notes (not loaded by game) | `"Designed for Pack 1 teaching"` |

---

### Effect Object Structure

Each item in the `effects` array must have:

```json
{
  "effect_type": "add_attack",
  "value": 12,
  "duration": "until_enemy_defeated",
  "condition": {
    "type": "card_count",
    "parameters": {
      "threshold": 5,
      "tier": "Arcane",
      "scope": "this_combat"
    },
    "coefficient": 0.4
  }
}
```

#### Effect Type Enum

| Effect Type | Value Type | Description | Example |
|-------------|-----------|-------------|---------|
| `add_attack` | number | Flat ATK bonus | `12` |
| `add_defense` | number | Flat DEF bonus | `8` |
| `essence_flat` | number | One-time essence burst | `250` |
| `essence_per_sec` | number | Ongoing essence rate | `2.0` |
| `heal_flat` | number | One-time HP restoration | `15` |
| `heal_regen` | number | HP per second until duration ends | `2.0` |
| `conditional` | varies | Condition-dependent effect | See condition object |
| `draw_card` | number | Draw N extra cards | `1` |
| `modify_next_card` | object | Affect next card drawn | `{stat: "attack", multiplier: 1.5}` |
| `modify_previous_card` | object | Retroactively affect previous card | `{stat: "defense", bonus: 10}` |
| `deck_manipulation` | object | Shuffle, exile, etc. | `{action: "reshuffle"}` |

#### Duration Enum

| Duration | Description | Reset Trigger |
|----------|-------------|---------------|
| `instant` | One-time effect | Immediate |
| `until_reshuffle` | Lasts until deck reshuffles | Reshuffle |
| `until_enemy_defeated` | Lasts until current enemy dies | New enemy |
| `until_death` | Lasts until player dies | Player death |
| `permanent` | Never resets | None |

---

### Acquisition Object Structure

```json
{
  "source": "pack1_guaranteed",
  "pack_type": "Arcane",
  "position": 2
}
```

| Field | Type | Required | Description | Values |
|-------|------|----------|-------------|--------|
| `source` | enum | ✅ | Acquisition method | `"starter"`, `"pack1_guaranteed"`, `"pack2_guaranteed"`, `"pack3_guaranteed"`, `"random_pool"` |
| `pack_type` | enum | ⚪ | Which pack (if from packs) | `"Arcane"`, `"Fire"`, `"Water"`, `"Earth"`, `"Air"` |
| `position` | number | ⚪ | Position in guaranteed pack | `1-5` |

---

## Stat Notation Format

### Display Text Conventions

When displaying card stats in `ability_text`, use these standardized formats:

#### Base Stats

| Stat | Notation | Examples |
|------|----------|----------|
| Attack | `+X ATK` | `+12 ATK`, `+35 ATK` |
| Defense | `+X DEF` | `+8 DEF`, `+20 DEF` |
| Both | `+X ATK, +Y DEF` | `+12 ATK, +8 DEF` |

#### Essence Generation

| Type | Notation | Examples |
|------|----------|----------|
| Rate | `+X Essence/sec` | `+2 Essence/sec`, `+4.5 Essence/sec` |
| Burst | `+X Essence` | `+250 Essence`, `+1000 Essence` |
| Both | `+X Essence, +Y/sec` | `+100 Essence, +1/sec` |

**Formatting Rules:**
- Rates with decimals: Show one decimal place if non-zero (`2.0` → `2 Essence/sec`, `2.5` → `2.5 Essence/sec`)
- Large values: Use comma separators for 1000+ (`+1,250 Essence`)
- Zero values: Omit entirely (don't show `+0 ATK`)

#### Healing

| Type | Notation | Examples |
|------|----------|----------|
| Flat | `Heal X HP` | `Heal 15 HP` |
| Regen | `+X HP/sec` | `+2 HP/sec until reshuffle` |

#### Conditional Effects

**Pattern:** `[Base effect]. If [condition]: [bonus]`

Examples:
- `+12 ATK. If HP < 50%: +15 ATK`
- `+2 Essence/sec. If 5+ Arcane drawn: +1 Essence/sec`

---

### Abbreviations & Keywords

#### Standard Abbreviations

| Term | Abbreviation | Usage |
|------|--------------|-------|
| Attack | ATK | Always abbreviated |
| Defense | DEF | Always abbreviated |
| Essence | Essence | Never abbreviated |
| Hit Points | HP | Always abbreviated |
| Per Second | /sec | Always abbreviated |

#### Tier Names

| Tier | Full Name | Short | In Text |
|------|-----------|-------|---------|
| Arcane | Arcane | Arc | "Arcane" (always full) |
| Fire | Fire | Fire | "Fire" (always full) |
| Water | Water | Wat | "Water" (always full) |
| Earth | Earth | Ear | "Earth" (always full) |
| Air | Air | Air | "Air" (always full) |

**Rule:** Never abbreviate tier names in ability text. Always use full names.

#### Card Type Keywords

| Type | In Text | Usage |
|------|---------|-------|
| Generator | "Generator" | "If previous card was Generator" |
| Combat | "Combat card" | "For each Combat card drawn" |
| Hybrid | Use effect type | Don't reference Hybrid directly |
| Utility | "Utility" | "If last 2 cards were Utility" |
| Synergy | "Synergy card" | "If Synergy card in last 3" |

---

### Scope Keywords

When referencing counting windows:

| Scope | Notation | Example |
|-------|----------|---------|
| This cycle | "this cycle" | "If 5+ Arcane drawn this cycle" |
| This combat | "this combat" | "For each reshuffle this combat" |
| In deck | "in deck" | "If 8+ Generators in deck" |
| Right now | "currently" or omit | "If rate > 5/sec" |

---

## Ability Text Templates

### Base Template Structure

All ability text follows this structure:

```
[Base Effect]
[Optional Conditional Bonus 1]
[Optional Conditional Bonus 2]
```

**Line Limit:** 3 lines maximum at 12px font, 168px effective width (~40-45 characters per line)

---

### Template 1: Flat Bonus (No Conditions)

**Format:**
```
+X ATK, +Y DEF
```

**Examples:**
```
+12 ATK, +8 DEF
+20 ATK
+15 DEF
+2 Essence/sec
+250 Essence
```

**Character Count:** 10-25 chars (always 1 line)

---

### Template 2: Simple Conditional

**Format:**
```
+X ATK [, +Y DEF]
If [condition]: [bonus]
```

**Examples:**
```
+12 ATK
If HP < 50%: +15 ATK
```
```
+2 Essence/sec
If 5+ Arcane this combat: +1/sec
```
```
+20 ATK, +10 DEF
If first 3 cards: +10 ATK
```

**Character Count:** 30-70 chars (2 lines)

---

### Template 3: Scaling Bonus

**Format:**
```
+X ATK [, +Y DEF]
For each [thing], [bonus]
```

**Examples:**
```
+8 ATK
For each Fire card this cycle, +4 ATK
```
```
+10 ATK, +10 DEF
For each reshuffle, +5 ATK, +5 DEF
```
```
+1 Essence/sec
For each Generator drawn, +0.5/sec
```

**Character Count:** 35-80 chars (2 lines)

---

### Template 4: Multiple Thresholds

**Format:**
```
+X ATK [, +Y DEF]
If [threshold 1]: [bonus 1]
If [threshold 2]: [bonus 2]
```

**Examples:**
```
+10 ATK
After 2nd reshuffle: +10 ATK
After 4th reshuffle: +20 ATK
```
```
+2 Essence/sec
If rate > 3/sec: +1 Essence/sec
If rate > 7/sec: +2 Essence/sec
```

**Character Count:** 60-120 chars (3 lines)

---

### Template 5: Sequence Condition

**Format:**
```
+X ATK [, +Y DEF]
If [previous/last N cards]: [bonus]
```

**Examples:**
```
+15 ATK, +10 DEF
If previous card was Generator: +2/sec
```
```
+20 ATK
If last 2 cards were Combat: +20 ATK
```
```
+30 ATK, +15 DEF
If last 3 all different tiers: +15 ATK
```

**Character Count:** 45-90 chars (2-3 lines)

---

### Template 6: Negative Condition

**Format:**
```
+X ATK [, +Y DEF]
BUT if [anti-condition]: [drawback]
```

**Examples:**
```
+60 ATK
BUT if DEF > 50: Take 10 damage
```
```
+50 ATK, +30 DEF
BUT if rate > 5/sec: +0 Essence
```
```
+80 ATK
BUT if drawn 6th+ card: -40 ATK
```

**Character Count:** 40-85 chars (2-3 lines)

---

### Template 7: Multiple Independent Conditions

**Format:**
```
+X ATK [, +Y DEF]
• If [condition 1]: [bonus 1]
• If [condition 2]: [bonus 2]
```

**Examples:**
```
+10 ATK, +5 DEF
• If 5+ Arcane: +15 ATK
• If 3rd+ reshuffle: +10 DEF
```

**Character Count:** 55-100 chars (3 lines)

**Note:** Use bullet points (•) to clearly separate independent conditions.

---

## Text Length Validation

### Card Layout Constraints

From `docs/visual-style-guide.md`:

**Font:** 12px regular, system font  
**Line Height:** 1.4  
**Available Width:** 168px (200px card - 32px padding)  
**Max Lines:** 3

**Calculated Character Limits:**
- **Average character width:** ~4px at 12px font
- **Characters per line:** ~42 characters
- **Total characters (3 lines):** ~126 characters maximum

---

### Validation Rules

#### Rule 1: 3-Line Maximum
- **Strict limit:** No card can exceed 3 lines of ability text
- **Test method:** Render text at 12px with 168px width container
- **Failure mode:** If wraps to 4th line, text must be shortened

#### Rule 2: Character Count Guidelines

| Lines | Character Range | Template Types |
|-------|-----------------|----------------|
| 1 line | 0-42 chars | Flat bonus only |
| 2 lines | 43-84 chars | Simple conditional, scaling bonus |
| 3 lines | 85-126 chars | Multiple thresholds, complex conditionals |

**Note:** These are guidelines. Actual wrapping depends on word length and hyphenation.

---

### Text Compression Techniques

When text is too long, apply these techniques **in order**:

#### 1. Use Standard Abbreviations
```
Before: "+12 Attack, +8 Defense"
After:  "+12 ATK, +8 DEF"
Saved:  10 characters
```

#### 2. Remove Redundant Words
```
Before: "If you have drawn 5 or more Arcane cards this combat"
After:  "If 5+ Arcane drawn this combat"
Saved:  23 characters
```

#### 3. Use Scope Shortcuts
```
Before: "this cycle" → "this cycle" (keep full)
Before: "during this combat" → "this combat"
Saved:  7 characters
```

#### 4. Consolidate Stats
```
Before: "+12 ATK. Also +8 DEF"
After:  "+12 ATK, +8 DEF"
Saved:  5 characters
```

#### 5. Use Symbols (Sparingly)
```
Before: "greater than or equal to 5"
After:  "≥5" or "5+"
Saved:  20+ characters
```

**Limit:** Only use `<`, `>`, `≤`, `≥` when absolutely necessary. Prefer `5+` over `≥5`.

#### 6. Simplify Condition Phrasing
```
Before: "If the previous card that was drawn was a Generator card"
After:  "If previous card was Generator"
Saved:  30+ characters
```

---

### Validation Checklist

Before finalizing any card's `ability_text`:

- [ ] Text renders in 3 lines or fewer at 12px font, 168px width
- [ ] All abbreviations follow standard notation (ATK, DEF, HP, /sec)
- [ ] Tier names spelled out fully (not abbreviated)
- [ ] Scope keywords used correctly ("this cycle" vs "this combat")
- [ ] Numbers formatted consistently (decimals only when needed)
- [ ] Conditional format follows template structure
- [ ] Text is clear and unambiguous (ask: "Can a new player understand this?")
- [ ] No orphaned words (single word on last line if avoidable)

---

## Keyword System (Future Enhancement)

For Pack 4+ cards, we may introduce keyword shortcuts:

| Keyword | Full Text | Characters Saved |
|---------|-----------|------------------|
| **Opener** | "If first card after reshuffle" | 23 |
| **Finisher** | "If enemy HP < 25%" | 11 |
| **Desperate** | "If player HP < 25%" | 12 |
| **Pure [Tier]** | "If all cards this cycle are [Tier]" | 25+ |
| **Chained** | "If previous card was same tier" | 24 |
| **Burst** | "When drawn, gain X once" | 17 |
| **Aura** | "+X/sec until reshuffle" | 15 |

**Status:** NOT IMPLEMENTED for Pack 1-3. Use full text for clarity during learning phase.

---

## Compact Text (Mobile View)

For compact card layouts (150px × 60px), use `ability_text_short`:

### Shortening Rules

1. **Remove conditions entirely** - Show only base effect
2. **Use minimal stat notation** - `+12/8` instead of `+12 ATK, +8 DEF`
3. **Single line only** - Max ~30 characters

### Examples

| Full Text | Compact Text |
|-----------|--------------|
| `+12 ATK, +8 DEF` | `+12/8` |
| `+2 Essence/sec. If 5+ Arcane: +1/sec` | `+2/sec` |
| `+20 ATK. For each Fire card, +5 ATK` | `+20 ATK` |
| `+250 Essence` | `+250` |

**Rule:** Compact text should show the **guaranteed base effect only**. Omit all conditional bonuses.

---

## JSON Example

Complete card with all fields populated:

```json
{
  "id": "arcane_surge",
  "name": "Arcane Surge",
  "tier": "Arcane",
  "rarity": "Rare",
  "type": "Generator",
  "stat_point_budget": 35,
  "effects": [
    {
      "effect_type": "essence_per_sec",
      "value": 3.0,
      "duration": "until_death"
    },
    {
      "effect_type": "conditional",
      "condition": {
        "type": "card_count",
        "parameters": {
          "threshold": 5,
          "tier": "Arcane",
          "scope": "this_combat"
        },
        "coefficient": 0.4
      },
      "bonus_effect": {
        "effect_type": "essence_per_sec",
        "value": 1.5
      }
    }
  ],
  "ability_text": "+3 Essence/sec\nIf 5+ Arcane drawn this combat: +1.5/sec",
  "ability_text_short": "+3/sec",
  "flavor_text": "The more you channel, the stronger the flow becomes.",
  "acquisition": {
    "source": "pack2_guaranteed",
    "pack_type": "Arcane",
    "position": 3
  },
  "_design_notes": "Teaches cumulative card_count tracking"
}
```

**Notes:**
- `\n` represents line breaks in `ability_text`
- `ability_text` must match the effects mechanically
- `ability_text_short` omits conditional bonus

---

## Design Process Workflow

When creating a new card:

### Step 1: Design Mechanics
1. Choose card type (Generator, Combat, Hybrid, etc.)
2. Define base effects (ATK, DEF, Essence, etc.)
3. Add conditional effects if appropriate
4. Calculate stat point budget

### Step 2: Write Ability Text
1. Start with appropriate template
2. Write base effect using stat notation
3. Add conditional clauses if any
4. Check character count (~126 char max)

### Step 3: Validate Text Length
1. Paste text into 168px width container at 12px font
2. Verify ≤ 3 lines
3. If too long, apply compression techniques
4. Repeat until valid

### Step 4: Create JSON Entry
1. Populate all required fields
2. Create `effects` array matching ability text
3. Add `ability_text` (full) and `ability_text_short` (compact)
4. Add acquisition and metadata

### Step 5: Validate Consistency
1. Verify `ability_text` accurately describes `effects`
2. Check stat budget matches effects
3. Validate rarity and type alignment
4. Cross-check against design specs

---

## Version History

### Version 1.0 (2025-11-11)
- Initial specification created for Task 2.1.6
- Defined complete card data structure
- Specified stat notation format
- Created text templates with character count guidelines
- Established text length validation rules
- Added JSON examples and workflow

---

## Next Steps

**After Task 2.1.6:**
1. Task 2.1.7: Design Pack 1 cards using these templates
2. Task 2.1.8: Design Pack 2 cards with more complex conditionals
3. Task 2.1.9: Design Pack 3 cards with full conditional system
4. Implementation: Update simulator to parse and validate ability text
5. UI Implementation: Render ability text with proper formatting

---

## Cross-References

- **Card System Spec:** `docs/design-specs/card-system.md`
- **Conditional Mechanics:** `docs/design-specs/conditional-mechanics.md`
- **Visual Style Guide:** `docs/visual-style-guide.md`
- **Balance Config:** `game-data/balance-config.json`
- **Cards Schema:** `game-data/cards-schema.json`
- **Starter Deck:** `game-data/cards-starter-deck.json`

---

**Document Status:** ✅ Complete  
**Ready For:** Pack 1-3 card design (Tasks 2.1.7-2.1.9)

