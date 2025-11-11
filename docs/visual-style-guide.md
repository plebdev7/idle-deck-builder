# Visual Direction & Style Guide

**Document Version:** 1.0  
**Date:** 2025-11-04  
**Status:** Complete - Ready for Implementation  
**Related:** CHECKLIST.md Task 1.1A

---

## Core Philosophy

### Design Principles
1. **Minimalist First:** Geometric simplicity over detailed illustration
2. **Text-Focused:** Stats and mechanics are the visual focus, not decoration
3. **Color-Coded Clarity:** Instant tier recognition via color accents on neutral base
4. **AI-Friendly Assets:** All icons describable in one sentence for AI generation
5. **Fast Iteration:** Adding new cards takes minutes, not hours
6. **Performance Priority:** Tiny assets, CSS-only animations, no heavy graphics

### 80/20 Split Philosophy
- **80% of time:** Designing card mechanics, abilities, interactions
- **20% of time:** Visual implementation (color assignment, icon selection)

---

## Color Palettes

### Base UI (Neutral Foundation)

All UI elements use this neutral palette as the foundation. Tier colors are applied as **accents only** (borders, icons, glows).

```
Background Dark:    #1a1a1a (near-black, main background, easy on eyes)
Background Medium:  #2d2d2d (card backgrounds, panels, elevated surfaces)
Background Light:   #404040 (hover states, elevated elements, headers)
Text Primary:       #f0f0f0 (main text, high contrast)
Text Secondary:     #a0a0a0 (labels, less important info, hints)
Border Base:        #4a4a4a (default borders, dividers)
```

**Usage Guidelines:**
- Main screen background: Background Dark (#1a1a1a)
- Card backgrounds: Background Medium (#2d2d2d)
- Panel/modal backgrounds: Background Medium with slight elevation
- Hover states: Background Light (#404040)
- All text defaults to Text Primary (#f0f0f0)
- Labels, tier names, metadata: Text Secondary (#a0a0a0)

---

### Tier Color Palettes (Accent Colors)

Each tier has a 4-color palette: Primary (main accent), Light (highlights), Dark (shadows), Icon (icon fills).

#### Arcane (Gray/Purple)
```
Primary:   #8b7ab8 (mystical purple-gray, borders, accents)
Light:     #b8a8e0 (highlights, glows, hover effects)
Dark:      #5a4a7a (shadows, depth, pressed states)
Icon:      #a090c8 (icon fill color)
```

**Theme:** Mystical, foundational magic, neutral but magical

#### Fire (Red/Orange)
```
Primary:   #e74c3c (vibrant red, borders, accents)
Light:     #ff6b5a (flame highlights, glows, hover effects)
Dark:      #c0392b (ember shadows, depth, pressed states)
Icon:      #ff5744 (icon fill color)
```

**Theme:** Aggressive, destructive, energetic

#### Water (Blue/Cyan)
```
Primary:   #3498db (clear blue, borders, accents)
Light:     #5dade2 (water shimmer, glows, hover effects)
Dark:      #2471a3 (deep water, depth, pressed states)
Icon:      #4fa8d5 (icon fill color)
```

**Theme:** Flowing, adaptive, calm but powerful

#### Earth (Green/Brown)
```
Primary:   #27ae60 (forest green, borders, accents)
Light:     #52c77a (foliage light, glows, hover effects)
Dark:      #1e8449 (deep earth, depth, pressed states)
Icon:      #3fb56e (icon fill color)
```

**Theme:** Defensive, enduring, stable, grounded

#### Air (Yellow/White)
```
Primary:   #f4d03f (bright yellow, borders, accents)
Light:     #f9e79f (sky highlight, glows, hover effects)
Dark:      #d4a017 (golden shadow, depth, pressed states)
Icon:      #f7dc6f (icon fill color)
```

**Theme:** Swift, unpredictable, energetic, free

---

### Color Application Rules

**Cards:**
- Background: Always #2d2d2d (neutral)
- Border: Tier Primary color (3px solid)
- Border glow (hover): Tier Light color (2px blur)
- Icon: Tier Icon color
- Text: #f0f0f0 (white) for readability

**UI Elements:**
- Buttons: Background Medium with tier Primary color border
- Active tier indicator: Tier Primary color background (20% opacity)
- Resource counters: Tier Icon color for the icon, white text
- Progress bars: Tier Primary color fill

**Accessibility:**
- All tier colors have 4.5:1+ contrast ratio against #2d2d2d background
- Text always uses #f0f0f0 (white) for maximum readability
- Never place tier-colored text on tier-colored backgrounds

---

## Icon & Symbol Style

### Design Rules

**Technical Specs:**
- Format: SVG (scalable, tiny file size)
- Design size: 24×24px to 48×48px artboard
- Complexity: Single shape with 2-3 color variations maximum
- Geometric basis: Circles, triangles, flowing curves
- No fine details: Must be recognizable at 16px size
- Transparent background
- Max 2 gradients per icon

**Style Guidelines:**
- Clean geometric shapes
- Minimal line work
- No drop shadows or complex effects
- Solid fills with optional gradient (tier color light → dark)
- 2px stroke maximum if outlines needed

---

### Element Symbols (Core Set)

#### Arcane
**Description:** Overlapping circles forming mystical pattern  
**AI Generation Prompt:**
```
Simple SVG icon: three overlapping circles forming a mystical symbol 
in a triangular arrangement, purple-gray gradient from #b8a8e0 to #5a4a7a, 
minimalist geometric style, transparent background, 32x32px
```

**Shape Concept:** ◯ ◯ ◯ (three circles, mystical intersection)

---

#### Fire
**Description:** Stylized flame from curved triangles  
**AI Generation Prompt:**
```
Simple SVG icon: stylized flame shape made of three curved triangular 
points stacked vertically, red-orange gradient from #ff6b5a to #c0392b, 
minimalist geometric style, transparent background, 32x32px
```

**Shape Concept:** 🔥 (angular flame, three points)

---

#### Water
**Description:** Three flowing waves in circular pattern  
**AI Generation Prompt:**
```
Simple SVG icon: three flowing wave curves arranged in a circular 
pattern suggesting movement, blue gradient from #5dade2 to #2471a3, 
minimalist geometric style, transparent background, 32x32px
```

**Shape Concept:** 〰️ 〰️ 〰️ (three waves, circular flow)

---

#### Earth
**Description:** Angular mountain/crystal formation  
**AI Generation Prompt:**
```
Simple SVG icon: angular geometric crystal or mountain shape with 
three peaks, green-brown gradient from #52c77a to #1e8449, 
minimalist geometric style, transparent background, 32x32px
```

**Shape Concept:** ▲ ▲ ▲ (three peaks, solid and stable)

---

#### Air
**Description:** Swirling spiral wind shape  
**AI Generation Prompt:**
```
Simple SVG icon: swirling spiral or wind gust with three curved lines 
suggesting motion, yellow-white gradient from #f9e79f to #d4a017, 
minimalist geometric style, transparent background, 32x32px
```

**Shape Concept:** 〜〜〜 (swirling motion, three curves)

---

### Card Type Icons (Secondary Set)

**Attack** - Simple upward-pointing sword or arrow
```
Minimalist sword silhouette pointing up, single color #e74c3c, 24x24px
```

**Defense** - Simple shield or bracket shape
```
Minimalist shield outline or angular bracket, single color #3498db, 24x24px
```

**Generator** - Coin/gem or circular arrow
```
Minimalist coin with sparkle or circular refresh arrow, single color #f4d03f, 24x24px
```

**Utility** - Star or gear shape
```
Minimalist four-point star or simple gear, single color #8b7ab8, 24x24px
```

---

### Rarity Icons (Optional - Can Use Text Instead)

**Common** - Single dot
**Rare** - Two dots
**Epic** - Three dots  
**Legendary** - Four-point star

These can be text labels instead of icons for MVP.

---

## Card Layout Specification

### Standard Card (Full Detail View)

**Dimensions:** 200px wide × 280px tall (standard trading card ratio ~5:7)

**Structure:**
```
┌─────────────────────────────┐
│ ╔═══════════════════════╗   │ ← Tier Primary color border (3px solid)
│ ║                       ║   │
│ ║   [ICON]   Card Name  ║   │ ← Icon (32px) left, Name (18px bold) right
│ ║          Level 5      ║   │ ← Level (12px, secondary text color)
│ ║                       ║   │
│ ║   ─────────────────   ║   │ ← Divider line (1px, border base color)
│ ║                       ║   │
│ ║   ATK  12    DEF  8   ║   │ ← Stats grid (14px medium)
│ ║   GEN  2 Fire/sec     ║   │ ← Generator stat (only if applicable)
│ ║                       ║   │
│ ║   ─────────────────   ║   │ ← Divider line
│ ║                       ║   │
│ ║   Ability text that   ║   │ ← Ability description (12px regular)
│ ║   describes the card  ║   │ ← Max 3 lines, wrap text
│ ║   effect clearly      ║   │
│ ║                       ║   │
│ ║   ─────────────────   ║   │ ← Divider line
│ ║                       ║   │
│ ║   Arcane    [Common]  ║   │ ← Tier name + Rarity (10px, secondary text)
│ ║                       ║   │
│ ╚═══════════════════════╝   │
└─────────────────────────────┘
```

**Color Specifications:**
- Outer card background: #2d2d2d
- Border: Tier Primary color (3px solid)
- Inner card background: Same #2d2d2d (no gradient)
- Divider lines: #4a4a4a (border base)
- Text: #f0f0f0 (primary text)
- Secondary text (level, tier, rarity): #a0a0a0
- Icon: Tier Icon color

**Padding & Spacing:**
- Outer padding: 8px
- Inner padding: 16px
- Spacing between sections: 8px
- Line height: 1.4 for ability text

---

### Compact Card (Deck List / Grid View)

**Dimensions:** 150px wide × 60px tall

**Structure:**
```
┌─────────────────────────┐
│ [ICON]  Card Name       │ ← Icon (20px) + Name (14px bold)
│ ─────────────────────── │ ← Divider
│  ATK 12  │  DEF 8  │+2  │ ← Stats inline (12px, compact)
└─────────────────────────┘
```

**Usage:** Deck composition view, card selection lists, inventory

**Color Specifications:**
- Background: #2d2d2d
- Left border accent: Tier Primary color (4px solid, left side only)
- Text: #f0f0f0
- Icons: Tier Icon color

---

### Minimal Card (Mobile / Small Screen)

**Dimensions:** 120px wide × 40px tall

**Structure:**
```
┌──────────────────┐
│ [I] Name    12/8 │ ← Icon (16px) + Name + ATK/DEF compact
└──────────────────┘
```

**Usage:** Mobile deck view, very small screens

---

## Typography Specification

### Font Family
**Primary:** System font stack for performance
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 
             'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 
             'Fira Sans', 'Droid Sans', 'Helvetica Neue', 
             sans-serif;
```

**Alternative (Web Font):** Inter or Roboto (load only if needed)

### Font Sizes & Weights

```
Headings (H1):         32px bold    (page titles)
Headings (H2):         24px bold    (section headers)
Headings (H3):         18px bold    (card names, subsections)

Body Large:            16px regular (main UI text)
Body Medium:           14px medium  (card stats, labels)
Body Regular:          12px regular (card abilities, descriptions)
Body Small:            10px regular (metadata, hints)

Labels:                10px uppercase (tier names, categories)
```

### Line Heights
```
Headings:              1.2
Body text:             1.4
Compact lists:         1.2
```

### Font Colors
```
Primary text:          #f0f0f0 (used 90% of the time)
Secondary text:        #a0a0a0 (labels, hints, metadata)
Tier accent text:      Tier Primary color (sparingly, headings only)
```

---

## UI Layout Principles

### Spacing System (8px Base Unit)

All spacing uses multiples of 8px for consistency:
```
4px   - Micro spacing (icon padding)
8px   - Tight spacing (between related elements)
16px  - Standard spacing (section padding, card internal padding)
24px  - Comfortable spacing (between sections)
32px  - Large spacing (major section breaks)
48px  - Extra large spacing (page sections)
```

### Grid System

**12-Column Responsive Grid:**
- Desktop (1200px+): 12 columns, 24px gutters
- Tablet (768-1199px): 8 columns, 16px gutters  
- Mobile (<768px): 4 columns, 16px gutters

**Card Grid:**
- Desktop: 4 cards per row (with 24px gap)
- Tablet: 3 cards per row (with 16px gap)
- Mobile: 1-2 cards per row (with 16px gap)

### Container Widths
```
Max content width:     1400px (centered)
Card width:            200px (standard)
Compact card:          150px
Mobile card:           120px minimum
```

### Padding Standards
```
Page padding:          32px (desktop), 16px (mobile)
Panel padding:         24px (desktop), 16px (mobile)
Card padding:          16px (internal)
Button padding:        12px 24px (vertical horizontal)
```

---

## Interaction States

### Card States

**Default:**
```
Background: #2d2d2d
Border: 3px solid Tier Primary color
Shadow: none
Transform: none
```

**Hover:**
```
Background: #2d2d2d (unchanged)
Border: 3px solid Tier Primary color
Box shadow: 0 0 8px Tier Light color (glow effect)
Transform: scale(1.02)
Transition: all 150ms ease-in-out
```

**Active/Pressed:**
```
Background: Tier Primary color at 10% opacity
Border: 3px solid Tier Primary color
Transform: scale(0.98)
Transition: all 100ms ease-in-out
```

**Selected:**
```
Background: Tier Primary color at 15% opacity
Border: 4px solid Tier Primary color (thicker)
Box shadow: 0 0 12px Tier Light color (stronger glow)
```

**Disabled:**
```
Opacity: 0.5
Filter: grayscale(100%)
Cursor: not-allowed
Pointer-events: none
```

### Button States

**Default:**
```
Background: #404040
Border: 2px solid #4a4a4a
Text: #f0f0f0
```

**Hover:**
```
Background: #4a4a4a
Border: 2px solid #606060
Box shadow: 0 2px 8px rgba(0,0,0,0.3)
```

**Primary Button (with tier context):**
```
Background: Tier Primary color at 20% opacity
Border: 2px solid Tier Primary color
Text: #f0f0f0
Hover: Tier Primary color at 30% opacity
```

---

## Animation Specifications

### Philosophy
- **CSS-only animations** for performance
- **Subtle and fast** - never block user interaction
- **Optional** - can disable for performance/accessibility
- **Meaningful** - animations indicate state changes, not decoration

### Card Animations

**Hover Effect:**
```css
transition: all 150ms ease-in-out;
transform: scale(1.02);
box-shadow: 0 0 8px [Tier Light color];
```

**Click/Select:**
```css
/* Press down */
transition: transform 100ms ease-in-out;
transform: scale(0.98);

/* Release */
transition: transform 100ms ease-in-out;
transform: scale(1.0);
```

**Card Draw/Add to Deck:**
```css
@keyframes slideInFromTop {
  from {
    transform: translateY(-100px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

animation: slideInFromTop 300ms ease-out;
```

**Card Remove:**
```css
@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}

animation: fadeOut 200ms ease-out;
```

### Resource Generation Feedback (Optional)

**Floating Text (+X Essence):**
```css
@keyframes floatUp {
  from {
    transform: translateY(0);
    opacity: 1;
  }
  to {
    transform: translateY(-40px);
    opacity: 0;
  }
}

animation: floatUp 1000ms ease-out;
color: [Tier Icon color];
font-size: 14px;
font-weight: bold;
```

**Usage:** Small text appears above resource counter, floats up and fades

### Pack Opening Animation

**Card Flip/Reveal:**
```css
@keyframes flipReveal {
  0% {
    transform: rotateY(0deg);
  }
  50% {
    transform: rotateY(90deg);
  }
  100% {
    transform: rotateY(0deg);
  }
}

animation: flipReveal 600ms ease-in-out;
```

**Rarity-Based Timing:**
- Common: 400ms (fast flip)
- Rare: 600ms (standard flip)
- Epic: 800ms (slow flip)
- Legendary: 1200ms (dramatic flip + glow pulse)

---

## Particle Effects (Post-MVP)

### Defer to Phase 2

**If implementing later:**
- Use lightweight library (particles.js or tsparticles)
- Maximum 10-20 particles on screen
- Tier-colored dots floating slowly
- Only on main menu screen, not during gameplay
- Performance budget: <5ms per frame

**Recommendation:** Skip particles entirely for MVP. CSS animations are sufficient.

---

## Basic Asset List

### Must-Have for MVP

**Element Icons (SVG):**
```
icons/elements/
├── arcane.svg       (mystical overlapping circles)
├── fire.svg         (stylized flame)
├── water.svg        (flowing waves)
├── earth.svg        (crystal/mountain)
└── air.svg          (swirling wind)
```

**Card Type Icons (SVG):**
```
icons/card-types/
├── attack.svg       (sword/arrow up)
├── defense.svg      (shield)
├── generator.svg    (coin/gem)
└── utility.svg      (star/gear)
```

**UI Icons (SVG):**
```
icons/ui/
├── pack.svg         (card pack/chest)
├── deck.svg         (stacked cards)
├── settings.svg     (gear)
├── info.svg         (information circle)
└── close.svg        (X button)
```

**Total: ~15 simple SVG icons**

### Nice-to-Have (Post-MVP)

**Rarity Icons:**
```
icons/rarities/
├── common.svg       (single dot)
├── rare.svg         (two dots)
├── epic.svg         (three dots)
└── legendary.svg    (star)
```

**Class-Specific Icons:**
```
icons/classes/
└── (individual class icons as designed)
```

### Assets NOT Needed

- ❌ No background images
- ❌ No card illustrations/artwork
- ❌ No character portraits
- ❌ No texture files
- ❌ No sprite sheets
- ❌ Everything is color + geometric shape + text

---

## Implementation Workflow

### Adding a New Card (Example)

**1. Design Mechanics (80% of time):**
```typescript
const newCard = {
  name: "Flame Strike",
  tier: "fire",
  attack: 12,
  defense: 8,
  essenceGeneration: { type: "fire", amount: 2 },
  ability: "Deal 5 damage to all enemies when played",
  rarity: "rare",
  level: 1
}
```

**2. Visual Implementation (20% of time):**
- Tier = "fire" → Automatically applies fire color palette (#e74c3c border, etc.)
- Icon = "fire" → Uses existing fire.svg icon
- Rarity = "rare" → Applies rare styling if implemented

**3. Result:**
- No new assets needed
- Color scheme handled by tier
- Icon reused from existing set
- Card ready to implement in minutes

### Creating New Tier (Future)

**Steps:**
1. Define 4-color palette (Primary, Light, Dark, Icon)
2. Generate 1 SVG icon (one AI prompt)
3. Add palette to CSS variables
4. Done - all cards automatically styled

**Time estimate:** 30 minutes

---

## CSS Variable Structure (Implementation Reference)

```css
:root {
  /* Base UI */
  --bg-dark: #1a1a1a;
  --bg-medium: #2d2d2d;
  --bg-light: #404040;
  --text-primary: #f0f0f0;
  --text-secondary: #a0a0a0;
  --border-base: #4a4a4a;
  
  /* Arcane */
  --arcane-primary: #8b7ab8;
  --arcane-light: #b8a8e0;
  --arcane-dark: #5a4a7a;
  --arcane-icon: #a090c8;
  
  /* Fire */
  --fire-primary: #e74c3c;
  --fire-light: #ff6b5a;
  --fire-dark: #c0392b;
  --fire-icon: #ff5744;
  
  /* Water */
  --water-primary: #3498db;
  --water-light: #5dade2;
  --water-dark: #2471a3;
  --water-icon: #4fa8d5;
  
  /* Earth */
  --earth-primary: #27ae60;
  --earth-light: #52c77a;
  --earth-dark: #1e8449;
  --earth-icon: #3fb56e;
  
  /* Air */
  --air-primary: #f4d03f;
  --air-light: #f9e79f;
  --air-dark: #d4a017;
  --air-icon: #f7dc6f;
  
  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-2xl: 48px;
  
  /* Card Dimensions */
  --card-width: 200px;
  --card-height: 280px;
  --card-compact-width: 150px;
  --card-compact-height: 60px;
}
```

---

## Combat UI Specification

### Overview

Combat UI must support conditional card mechanics by displaying game state and card history. All tracking elements must be visible and updateable in real-time.

**Related Spec:** [conditional-mechanics.md](design-specs/conditional-mechanics.md)

---

### Required Tracking Elements

#### 1. Reshuffle Counter

**Purpose:** Tracks cycle-based timing conditions  
**Location:** Near deck indicator (top-right recommended)  
**Format:** `"Cycle 3"` or `"Reshuffle: 2"`

**Visual Specs:**
```
Font: 14px medium
Color: #f0f0f0 (primary text)
Icon: Circular arrow (16px) in #8b7ab8 (arcane color)
Layout: [Icon] Cycle 3
```

**Behavior:**
- Starts at 0 (first cycle)
- Increments on each deck reshuffle
- Resets on new enemy

---

#### 2. Cards Drawn This Cycle

**Purpose:** Track card counts within current cycle  
**Location:** Near deck indicator or expandable overlay  
**Format:** Compact icon summary with counts

**Visual Specs - Compact View:**
```
┌─────────────────────┐
│ This Cycle: 5 cards │
│ 🔮3  ⚔️4  💎1      │
└─────────────────────┘

Legend:
🔮 = Arcane tier count
⚔️ = Combat type count
💎 = Generator type count
```

**Visual Specs - Expanded View (Hover/Click):**
```
┌─────────────────────────┐
│ Cards Drawn This Cycle  │
├─────────────────────────┤
│ By Tier:                │
│ 🔮 Arcane: 3            │
│ 🔥 Fire: 1              │
│ 💧 Water: 1             │
├─────────────────────────┤
│ By Type:                │
│ ⚔️ Combat: 4            │
│ 💎 Generator: 1         │
└─────────────────────────┘
```

**Styling:**
```
Background: #2d2d2d
Border: 2px solid #4a4a4a
Padding: 12px
Font: 12px regular
Icons: 16px, tier colors
```

**Behavior:**
- Updates real-time as cards drawn
- Resets to 0 on reshuffle
- Highlights when conditions trigger (pulse tier color)

---

#### 3. Last 3 Cards Drawn

**Purpose:** Enable sequence condition evaluation  
**Location:** Below player stats or above combat log (horizontal row)  
**Format:** 3 card summary blocks, most recent on right

**Visual Specs - Standard View:**
```
┌──────────┐  ┌──────────┐  ┌──────────┐
│ Arcane   │  │ Power    │  │ Essence  │
│ Bolt     │  │ Strike   │  │ Burst    │
│ ⚔️ +20   │  │ ⚔️ +15/5 │  │ 💎 +250  │
└──────────┘  └──────────┘  └──────────┘
  (2 ago)       (1 ago)       (current)
```

**Card Block Specs:**
```
Dimensions: 80px wide × 60px tall
Background: #2d2d2d
Border: 2px solid [Tier Primary color]
Padding: 6px
Text: 10px regular

Content:
- Card name (truncate if needed)
- Type icon (14px)
- Key stat (ATK/DEF or Essence)
- Tier color border
```

**Behavior:**
- Slides left when new card drawn (shift animation)
- Oldest card fades out
- New card fades in from right
- Animation: 150ms ease-in-out
- Cleared on new enemy

**Mobile/Compact:**
```
Show icons only: [🔮][⚔️][💎]
Tap to expand full card summary
```

---

#### 4. Cards Drawn This Combat

**Purpose:** Track cumulative combat conditions  
**Location:** Expandable panel (click/tap to show)  
**Format:** Running totals with tier/type breakdown

**Visual Specs:**
```
┌─────────────────────────────┐
│ Combat Stats: 23 cards      │
├─────────────────────────────┤
│ By Tier:                    │
│ 🔮 Arcane: 15               │
│ 🔥 Fire: 5                  │
│ 💧 Water: 3                 │
├─────────────────────────────┤
│ By Type:                    │
│ ⚔️ Combat: 18               │
│ 💎 Generator: 5             │
└─────────────────────────────┘
```

**Styling:**
```
Panel: 240px wide (right sidebar)
Background: #2d2d2d
Border: 2px solid #4a4a4a
Header: 14px medium, #a0a0a0
Counts: 14px regular, #f0f0f0
Icons: 16px, tier colors
Padding: 16px
```

**Behavior:**
- Updates real-time throughout combat
- Resets on new enemy
- Can be collapsed (show just total count)
- Expandable on hover or click

---

#### 5. Current Game State Panel

**Purpose:** Display all state-based condition values  
**Location:** Center/top of combat area (always visible)  
**Format:** Clean horizontal layout with all key stats

**Visual Layout:**
```
┌──────────────────────────────────────────────────┐
│                  ENEMY #15                       │
│  ██████████████████░░░░░░░░░  1,234 / 2,000 HP  │
├──────────────────────────────────────────────────┤
│                    PLAYER                        │
│  ████████████████████████████░░  85 / 100 HP    │
│                                                  │
│  ATK: 124    DEF: 98    Rate: 5.2/sec          │
└──────────────────────────────────────────────────┘
```

**Styling:**
```
Panel width: 500px (centered)
Background: #2d2d2d
Border: 2px solid #4a4a4a
Padding: 16px

HP Bars:
- Height: 20px
- Enemy bar: #e74c3c (fire red)
- Player bar: #3498db (water blue)
- Background: #1a1a1a
- Border: 1px solid #4a4a4a

Stats:
- Font: 16px medium
- Color: #f0f0f0
- Spacing: 24px between stats
- Labels uppercase, 10px
```

**Percentage Indicators:**
```
Show HP percentages in parentheses:
"85 / 100 HP (85%)"

Color coding:
> 75%: #52c77a (green)
50-75%: #f9e79f (yellow)
25-50%: #ff6b5a (orange)
< 25%: #e74c3c (red)
```

---

### Visual Priority & Responsive Behavior

#### Desktop (1200px+)
**Always Visible:**
- Current game state panel (center)
- Reshuffle counter (top-right)
- Last 3 cards drawn (below player stats)
- Cards drawn this cycle (compact, top-right)

**Expandable:**
- Cards drawn this combat (panel/sidebar)

---

#### Tablet (768-1199px)
**Always Visible:**
- Current game state panel (shrink to 400px)
- Reshuffle counter
- Last 3 cards (smaller blocks, 60px wide)

**Compact:**
- Cards drawn this cycle (icon counts only)

**Hidden/Expandable:**
- Cards drawn this combat (tap to overlay)

---

#### Mobile (<768px)
**Always Visible:**
- HP bars only (full width)
- Current stats (below HP)
- Reshuffle counter (compact)

**Icon-Only:**
- Last 3 cards (tap to expand)
- Cards this cycle (tap to expand)

**Overlay:**
- All detailed breakdowns accessible via tap

---

### Condition Trigger Feedback

When a card's condition triggers, provide visual feedback:

**Success Trigger:**
```
- Card border pulses with tier color (2× glow intensity)
- "+X bonus!" text floats up from card (1s fade)
- Color: Tier Light color
- Font: 14px bold
- Animation: floatUp 1000ms ease-out
```

**Failed Condition (Optional):**
```
- Dim the condition text slightly (70% opacity)
- Show why it failed on hover
- No intrusive feedback
```

---

### Animation Specifications

**Card History Slide (New Card Drawn):**
```css
@keyframes slideLeft {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(-90px); /* card width + gap */
  }
}

/* Oldest card */
animation: slideLeft 150ms ease-in-out, fadeOut 150ms ease-out;

/* New card enters */
@keyframes slideIn {
  from {
    transform: translateX(90px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

animation: slideIn 150ms ease-in-out;
```

**Counter Increment:**
```css
/* Number changes */
@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.2); color: [Tier Light color]; }
  100% { transform: scale(1); }
}

animation: pulse 200ms ease-out;
```

**Reshuffle Counter Update:**
```css
/* On reshuffle increment */
@keyframes highlight {
  0% { 
    background: transparent; 
  }
  50% { 
    background: [Tier Primary color] at 20% opacity;
    box-shadow: 0 0 8px [Tier Light color];
  }
  100% { 
    background: transparent; 
  }
}

animation: highlight 400ms ease-in-out;
```

---

### Accessibility Considerations

**Screen Reader Announcements:**
- Announce reshuffle count changes
- Announce when cards drawn exceed thresholds (3+, 5+, etc.)
- Announce condition triggers ("Bonus activated: +15 ATK")
- Provide text descriptions for all icons

**Keyboard Navigation:**
- Tab through expandable panels
- Arrow keys to navigate card history
- Enter/Space to expand collapsed panels

**Color Independence:**
- All tier indicators have icons + text labels
- HP percentages shown as text (not just color)
- Card type icons distinct shapes (not just colors)

---

### Implementation Notes

**Performance:**
- Use CSS transforms for animations (GPU-accelerated)
- Throttle counter updates (max 60 FPS)
- Virtual scrolling for combat history if > 100 cards
- Minimize DOM reflows (batch updates)

**State Management:**
- Track all counters in game state object
- Update UI reactively (React/Vue patterns)
- Reset logic on enemy/combat transitions
- Persist reshuffle count between enemies (resets on death)

**Testing:**
- Validate all counters with simulator
- Test responsive breakpoints
- Verify animations don't block interaction
- Check accessibility with screen readers

---

### Contrast Ratios
- All text (#f0f0f0) on backgrounds (#2d2d2d, #1a1a1a): **WCAG AAA** (>7:1)
- Tier colors on backgrounds: **WCAG AA** minimum (>4.5:1)
- Never use tier-colored text on tier-colored backgrounds

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Screen Reader Considerations
- All icons have `aria-label` attributes
- Card stats have semantic HTML structure
- Interactive elements have proper focus states
- Tier information available to screen readers

### Colorblind Modes (Future Enhancement)
- Consider adding icon shapes in addition to colors
- Each tier already has unique icon shape for distinction
- Text labels always present as backup to color

---

## Design Constraints & Requirements

### Performance Budget
- Initial SVG icon load: <50KB total (all 15 icons combined)
- CSS file: <20KB (including Tailwind purged output)
- Font loading: Use system fonts (0KB) or single web font (<30KB)
- Total visual asset budget: <100KB

### Browser Support
- Modern browsers only (Chrome, Firefox, Safari, Edge - last 2 versions)
- SVG support required
- CSS Grid and Flexbox support required
- CSS custom properties (variables) required

### Responsive Breakpoints
```
Mobile:        < 768px (1-2 cards per row)
Tablet:        768px - 1199px (3 cards per row)
Desktop:       1200px+ (4 cards per row)
Large Desktop: 1600px+ (5 cards per row, optional)
```

---

## Future Enhancements (Not MVP)

### Potential Additions
1. **Animated backgrounds** - Subtle particle effects on main screen
2. **Card shine effects** - Holographic effect on legendary cards
3. **Sound effects** - Card flip, pack open, essence gain sounds
4. **Alternative card layouts** - Players can choose compact/detailed view
5. **Custom themes** - Dark/light mode toggle
6. **Seasonal themes** - Holiday color palette swaps

### Do NOT Implement Yet
- Any of the above
- Complex animations
- Multiple theme options
- Illustrated card variants
- 3D card effects

---

## Quick Reference Summary

**Card Dimensions:** 200×280px (standard), 150×60px (compact)  
**Colors:** Neutral backgrounds (#2d2d2d), tier color accents only  
**Icons:** 15 simple SVG icons, AI-generated, reusable  
**Typography:** System fonts, 10px-32px range, #f0f0f0 text  
**Spacing:** 8px base unit (multiples of 8)  
**Animations:** CSS only, subtle, fast (<300ms)  
**Asset Budget:** <100KB total

**Adding New Card:** 80% mechanics design, 20% visual (auto-styled by tier)  
**Adding New Tier:** 30 minutes (4-color palette + 1 icon)

---

## Validation Checklist

Before marking 1.1A complete, confirm:
- [x] Color palettes defined with exact hex codes for all 5 tiers
- [x] Base UI neutral palette defined
- [x] Icon style guidelines specified
- [x] AI generation prompts created for 5 element icons
- [x] Card layout mockup (wireframe) documented
- [x] Compact card layout specified
- [x] UI color scheme principles established
- [x] Layout principles (spacing, grid, typography) defined
- [x] Animation style specified (CSS-only, minimal)
- [x] Basic asset list created (15 SVG icons)
- [x] Implementation workflow documented
- [x] 80/20 design philosophy maintained

---

**Document Status:** Complete  
**Ready For:** Implementation (Session 9+ or after all design sessions complete)  
**Next Steps:** Proceed to Task 1.2 (Critical Design Decisions)

---

**Approved By:** User  
**Date:** 2025-11-04  
**Session:** 1.1A Visual Direction & Style Guide

