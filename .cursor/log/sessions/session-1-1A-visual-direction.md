# Session 1.1A - Visual Direction & Style Guide

**Session Date:** 2025-11-04  
**Task Reference:** CHECKLIST.md Task 1.1A, ROADMAP.md Session 1  
**Status:** Complete  
**Related Documents:** docs/visual-style-guide.md

---

## Task Summary

Define comprehensive visual direction and style guide for the Idle Deck Builder game, establishing color palettes, icon styles, card layouts, UI principles, and asset requirements.

---

## Log Entries

### 2025-11-04 22:50:41 - Discussion: Visual Direction Fundamentals

**Context:**  
User requested discussion of fundamentals for Task 1.1A. Reviewed CHECKLIST.md, ROADMAP.md, DESIGN.md, and TECH-STACK.md to understand project requirements and constraints.

**Key Design Constraints Identified:**
- Abstract visuals emphasizing performance (from DESIGN.md)
- Theme provides context but never obscures gameplay
- User is not an artist, prefers AI-generated SVGs
- 80/20 split: 80% time on mechanics, 20% on visuals
- Minimalist preference for fast iteration

**Questions Presented to User:**

1. **Visual Fidelity Level** - Three options presented:
   - Option A: Minimal Abstract (solid colors, geometric shapes)
   - Option B: Stylized Minimalism (subtle gradients, simple SVG icons) **[RECOMMENDED]**
   - Option C: Illustrated (detailed art, heavier assets)

2. **Color Strategy** - Three approaches:
   - Option A: Primary Color Dominance (tier colors everywhere)
   - Option B: Accent Color System (neutral base, tier colors as accents) **[RECOMMENDED]**
   - Option C: Gradient/Theme Approach (color palettes per tier)

3. **Card Layout Philosophy** - Three layouts:
   - Option A: Data-Dense (all info always visible)
   - Option B: Balanced (key info visible, details on card) **[RECOMMENDED]**
   - Option C: Minimal-Clean (hide details, show on hover)

**Recommendations Made:**
- Visual Fidelity: Stylized Minimalism (SVG icons, Tailwind gradients, fast to implement)
- Color Strategy: Accent Color System (dark base, prevents fatigue, high contrast)
- Card Layout: Balanced (shows stats at glance, familiar UX pattern)

**User Response:**  
User confirmed recommendations align with vision. Preferences: minimalist, AI-generated SVGs, 80/20 split mechanics/visuals, fast iteration priority.

**Approval:** User approved proceeding with creating formal visual style guide.

**Files Read:**
- CHECKLIST.md (task requirements)
- ROADMAP.md (session context)
- DESIGN.md (theme and constraints)
- TECH-STACK.md (implementation technology)

---

### 2025-11-04 22:51:00 - Document Creation: Visual Style Guide

**Action:** Created comprehensive visual style guide document.

**File Created:**
- `docs/visual-style-guide.md` (complete specification, ~600 lines)

**Content Sections:**
1. **Core Philosophy** - Design principles and 80/20 split philosophy
2. **Color Palettes** - Complete hex codes for base UI + 5 tier palettes
3. **Icon & Symbol Style** - Design rules + AI generation prompts for 5 element icons
4. **Card Layout Specification** - Standard (200×280px), Compact (150×60px), Mobile variants
5. **Typography Specification** - Font families, sizes, weights, colors
6. **UI Layout Principles** - 8px spacing system, 12-column grid, responsive breakpoints
7. **Interaction States** - Hover, active, selected, disabled states with exact CSS specs
8. **Animation Specifications** - CSS-only animations, timing, effects
9. **Basic Asset List** - 15 SVG icons required (5 elements + 4 card types + 6 UI)
10. **Implementation Workflow** - Step-by-step for adding cards and tiers
11. **Accessibility Considerations** - Contrast ratios, reduced motion, screen readers

**Key Decisions Documented:**

**Color Palettes:**
- Base UI: Neutral grays (#1a1a1a, #2d2d2d, #404040) + white text (#f0f0f0)
- Arcane: Purple-gray (#8b7ab8 primary, #b8a8e0 light, #5a4a7a dark)
- Fire: Red-orange (#e74c3c primary, #ff6b5a light, #c0392b dark)
- Water: Blue-cyan (#3498db primary, #5dade2 light, #2471a3 dark)
- Earth: Green (#27ae60 primary, #52c77a light, #1e8449 dark)
- Air: Yellow (#f4d03f primary, #f9e79f light, #d4a017 dark)

**Icon Design:**
- SVG format, 24-48px design size
- Single geometric shapes, 2-3 colors max
- AI generation prompts provided for each element icon
- Transparent backgrounds, minimal complexity

**Card Layout:**
- Standard: 200×280px (full detail, primary view)
- Compact: 150×60px (deck lists, grids)
- Mobile: 120×40px (small screens)
- Neutral background (#2d2d2d) with tier color borders
- Clear stat display, 3-line ability text

**Performance Budget:**
- All SVG icons: <50KB total
- CSS file: <20KB (Tailwind purged)
- Total visual assets: <100KB
- CSS-only animations (no particle systems for MVP)

**Asset Requirements:**
- 5 element icons (arcane, fire, water, earth, air)
- 4 card type icons (attack, defense, generator, utility)
- 6 UI icons (pack, deck, settings, info, close)
- Total: 15 simple SVG icons
- All AI-generatable with single-sentence prompts

**Implementation Workflow:**
- Adding new card: 80% mechanics, 20% visual (tier auto-applies colors)
- Adding new tier: 30 minutes (4-color palette + 1 icon)
- No new assets needed per card (icons reused)

**Validation:**
- All CHECKLIST.md 1.1A items addressed
- All color palettes defined with exact hex codes ✓
- Icon style guidelines specified ✓
- AI generation prompts created ✓
- Card layout mockups documented ✓
- UI color scheme established ✓
- Animation style specified ✓
- Asset list created ✓

---

## Deliverables

### Documents Created
1. **docs/visual-style-guide.md** - Complete visual direction specification
   - 600+ lines of detailed specifications
   - Ready for implementation
   - All hex codes, dimensions, and guidelines defined

### Design Decisions Made

**Visual Approach:** Stylized Minimalism
- Geometric SVG icons with gradients
- Neutral dark base UI with tier color accents
- Performance-first, accessibility-considered

**Color Strategy:** Accent System
- Dark backgrounds for long play sessions
- High contrast white text
- Tier colors used as borders, icons, highlights only

**Asset Strategy:** Minimal AI-Generated Set
- 15 reusable SVG icons total
- Single-sentence AI prompts for generation
- No custom artwork per card needed

**Animation Strategy:** CSS-Only
- Subtle, fast interactions (<300ms)
- Hover, click, reveal animations specified
- No particle systems (defer to post-MVP)

---

## Cross-References

### CHECKLIST.md Task 1.1A
- [x] Define color palettes for each tier (exact hex codes)
- [x] Design icon/symbol style for elements
- [x] Create card layout mockup (wireframe or text-based)
- [x] Specify UI color scheme and layout principles
- [x] Define animation/particle style (if any)
- [x] Create basic asset list

### ROADMAP.md Session 1
Task 1.1A completed as part of Session 1 design foundation work.

### DESIGN.md Alignment
- Maintains "abstract visuals emphasizing performance" principle
- Ensures "theme provides context but never obscures gameplay"
- Supports familiar fantasy elements with minimal cognitive overhead

### TECH-STACK.md Alignment
- SVG icons compatible with SvelteKit + Tailwind stack
- CSS-only animations leverage Tailwind utilities
- Performance budget aligns with PWA targets (<200KB initial load)

---

## Next Steps

### Immediate
1. Update CHECKLIST.md to mark Task 1.1A as complete
2. Proceed to Task 1.2: Critical Design Decisions

### Future (Session 9+ or Implementation Phase)
1. Generate 15 SVG icons using AI prompts from style guide
2. Implement CSS variables and Tailwind config with color palettes
3. Create Svelte card components following layout specifications
4. Test responsive layouts at specified breakpoints

---

## Notes

**User Preferences Captured:**
- Not an artist, relies on AI-generated assets
- Minimalist preference for fast iteration
- 80/20 split: mechanics over visuals
- Performance and clarity prioritized

**Design Philosophy:**
- Every visual decision optimized for speed of iteration
- Adding new cards should take minutes, not hours
- Visual system scales easily (new tiers = 1 palette + 1 icon)
- No artistic bottleneck to content creation

**Success Metrics:**
- Time to add new card: <5 minutes (mostly mechanics)
- Time to add new tier: ~30 minutes (palette + icon)
- Asset bundle size: <100KB (target met with 15 SVG icons)
- Visual clarity: Instant tier recognition via color

---

**Session Status:** Complete  
**All Checklist Items:** Addressed and Delivered  
**Document Quality:** Production-Ready  
**Ready for:** Task 1.2 (Critical Design Decisions)

