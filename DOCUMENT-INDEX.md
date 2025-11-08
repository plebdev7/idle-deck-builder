# Document Index - Idle Card Battler

**Purpose:** Quick reference to all project documents and their purposes.  
**Last Updated:** 2025-11-08 (Version 2.0 - Documentation Restructure)

---

## Core Project Documents

### DESIGN.md

**Purpose:** **High-level design hub** with summaries and links to detailed specifications  
**Audience:** Project owners, AI assistants, quick reference  
**Update Frequency:** When major systems change or new systems added  
**Scope:** Vision, system summaries, quick reference  
**Size:** ~400 lines (lean and navigable)

**What's Here:**
- Core vision and principles
- System summaries (2-3 sentences each)
- Key design decisions
- Links to detailed specifications
- Quick reference tables
- Outstanding questions

**What's NOT Here:**
- Detailed formulas (→ baseline-numbers.md)
- Combat mechanics (→ combat-system.md)
- Card specifications (→ card-system.md)
- Complete progression curves (→ progression.md)

### CHECKLIST.md

**Purpose:** Granular task tracking with completion status  
**Audience:** Project owners, AI assistants  
**Update Frequency:** Every task completion  
**Scope:** All sessions, specific tasks and sub-tasks  
**Size:** 365 lines (manageable)

### ROADMAP.md

**Purpose:** Session structure, deliverables, and methodology  
**Audience:** Project owners, AI assistants  
**Update Frequency:** Per session or when methodology changes  
**Scope:** Big picture organization and approach  
**Size:** 690 lines (stable)

### TECH-STACK.md

**Purpose:** Implementation technology decisions and rationale  
**Audience:** Future developers  
**Update Frequency:** Rarely (established decisions)  
**Scope:** Frontend, backend, hosting, tools, workflows  
**Size:** 650 lines (stable)

---

## Detailed Design Specifications (docs/design-specs/)

**NEW in Version 2.0:** Detailed specifications split into focused topic files.

### combat-system.md

**Purpose:** Complete combat mechanics specification  
**Size:** ~400 lines  
**Status:** Complete (Session 2.0.3)

**Contains:**
- Tick-based combat system (1.0s per tick)
- Player HP system (starting, scaling, upgrades)
- Continuous deck cycling mechanics
- Stat accumulation and reset rules
- Death system and respawn mechanics
- Combat flow examples
- Strategic implications

**When to Use:** Implementing combat, balancing cards for combat, understanding death mechanics

### progression.md

**Purpose:** Enemy scaling, bosses, and death loop system  
**Size:** ~350 lines  
**Status:** Complete (Session 2.0.3 Part C)

**Contains:**
- Act-based enemy HP scaling formulas
- Attack scaling by enemy number
- Boss encounter specifications (50, 100, 150)
- Death and respawn system details
- Multi-loop progression expectations
- Rewards structure
- Balance targets for pack card design

**When to Use:** Balancing enemies, designing bosses, understanding progression pacing

### resource-economy.md

**Purpose:** Complete resource generation and economy specification  
**Size:** ~250 lines  
**Status:** Complete (Sessions 1.2, 1.3)

**Contains:**
- Split resource system (Essence vs Shards)
- Draw-based generator mechanics
- Arcane Essence as universal currency
- Elemental conversion system
- Resource flow models
- Strategic implications

**When to Use:** Designing generator cards, balancing economy, understanding resource flow

### card-system.md

**Purpose:** Card types, patterns, and specifications  
**Size:** ~300 lines  
**Status:** Starter deck complete, Pack cards pending (Task 2.1)

**Contains:**
- Card type definitions (Combat, Generator, Synergy, Utility)
- Card interaction patterns
- Complete starter deck specification (8 cards)
- Pack card progression roadmap
- Card rarity system (pending)

**When to Use:** Designing new cards, understanding card mechanics, implementing card system

### tier-class-system.md

**Purpose:** Tier structure and class system specification  
**Size:** ~350 lines  
**Status:** Complete (Sessions 1.1, 1.2)

**Contains:**
- Hybrid cascading tier model
- Arcane tier (foundational, permanent)
- Elemental tiers (class-specific)
- Class card distribution (Common/Rare/Epic/Legendary)
- Class mechanics (activation, switching, deck limits)
- Deck building constraints (multi-layered)
- Class-specific deck limit examples

**When to Use:** Designing classes, understanding tier progression, implementing deck constraints

### baseline-numbers.md

**Purpose:** All formulas, rates, timings, and validation targets  
**Size:** ~400 lines  
**Status:** Complete baseline, Pack targets pending (Task 2.1)

**Contains:**
- Core game timing (card draw, combat ticks)
- Generator card rates (all tiers)
- Pack costs and scaling formulas
- Shard drops and spending
- Enemy HP and Attack formulas
- Combat card stat ranges
- Validated pacing milestones
- Combat duration targets
- All major formulas in quick reference format

**When to Use:** Balancing anything, validating timings, reference for all numbers

### first-30-minutes.md

**Purpose:** New player experience specification  
**Size:** ~350 lines  
**Status:** Complete (Session 1.3A)

**Contains:**
- Starting state (Arcane Student)
- Gameplay phases (minute-by-minute)
- Key milestones (6 major milestones)
- Progression gates (soft, time-based)
- Emotional arc
- End state expectations
- Critical design decisions
- Pacing validation

**When to Use:** Designing onboarding, understanding player journey, tuning early game

---

## Supporting Documents (docs/)

### docs/theme-specification.md

**Purpose:** Thematic reference for writing flavor text and content  
**Audience:** Content creators, writers  
**Use Case:** Consulted when writing card names, flavor text, class names  
**Size:** 376 lines  
**Why Separate:** Design decisions vs thematic consistency reference

**Contains:**
- Element descriptions and themes
- Currency naming conventions
- Class naming patterns
- Card naming conventions
- Narrative context (minimal)

### docs/visual-style-guide.md

**Purpose:** UI/UX implementation guide with exact specifications  
**Audience:** Frontend developers, UI implementers  
**Use Case:** Consulted during frontend implementation  
**Size:** 899 lines  
**Why Separate:** Design decisions vs implementation specifications

**Contains:**
- Exact hex color codes (all tiers)
- Card layout specifications (pixel-perfect)
- Typography specs (fonts, sizes, weights)
- Icon style guide with AI generation prompts
- CSS variable structure
- Animation specifications
- Accessibility considerations

---

## Session Logs (.cursor/log/sessions/)

**Purpose:** Historical record of work performed with timestamps and rationale  
**Audience:** AI assistants (for continuity), project owners (for process review)  
**Update Frequency:** During each work session  
**Scope:** Detailed log of actions, decisions, and reasoning

**Current Logs:**
- `session-1-1-theme-selection.md` - Theme establishment
- `session-1-1A-visual-direction.md` - Visual style guide creation
- `session-1-2-critical-design-decisions.md` - 5 major questions resolved
- `session-1-3-high-level-experience.md` - First 30 minutes design (Part A)
- `session-1-3b-baseline-numbers.md` - Economy numbers and validation (Part B)
- `session-1-3c-starter-cards.md` - 8 starter cards designed (Part C)
- `session-2-0-1-combat-progression.md` - Combat scaling, bosses, death loops
- `session-2-0-2-live-sim-viewer.md` - Live terminal visualization
- `session-2-0-3-combat-system-redesign.md` - Combat-over-time redesign (Parts A-D)
- `session-2-0-4-cli-fixes.md` - Bug fixes and improvements

**Why Keep:**
- Shows decision-making process (not just final decisions)
- Preserves rationale and alternatives considered
- Workspace rules require detailed logging
- Different purpose than main docs (process vs product)

---

## Administrative (.cursor/log/)

### .cursor/log/administrative/ (if created)

**Purpose:** Planning, meta-discussions, project organization  
**Scope:** Non-session work (like this document organization review)

### .cursor/log/setup/ (if created)

**Purpose:** Setup and configuration work  
**Scope:** Repository setup, tool configuration, initial scaffolding

---

## Archive (.archive/)

**Purpose:** Superseded documents with historical value  
**When Used:** Document served purpose but now creates confusion or redundancy

**Current Archive:**
- `.archive/session-1/economy-model-v1.3.md` - Working document from Session 1.3, fully integrated into design specs
- `.archive/DESIGN-v1.9-pre-split.md` - Monolithic DESIGN.md before Version 2.0 restructure (1,867 lines)

**Policy:** See `.archive/README.md` for archive criteria

---

## Document Relationships

### Authoritative Sources (Single Source of Truth)

```
DESIGN.md (v2.0)       ← High-level hub (summaries + links)
├── docs/design-specs/ ← Detailed specifications (authoritative)
│   ├── combat-system.md
│   ├── progression.md
│   ├── resource-economy.md
│   ├── card-system.md
│   ├── tier-class-system.md
│   ├── baseline-numbers.md
│   └── first-30-minutes.md

TECH-STACK.md       ← Technology decisions (authoritative)
CHECKLIST.md        ← Task status (authoritative)
ROADMAP.md          ← Session structure (authoritative)
```

### Implementation References (Derived from Design)

```
design-specs/*.md → docs/theme-specification.md       (thematic subset)
design-specs/*.md → docs/visual-style-guide.md        (visual implementation)
```

### Historical Record (Process Documentation)

```
Session Work → .cursor/log/sessions/*.md      (detailed logs)
             ↓
     design-specs/*.md                         (final decisions)
             ↓
          DESIGN.md                            (summaries + links)
```

---

## Information Flow

### During Design Sessions

```
1. Work performed with decisions made
2. Session log created/updated (detailed record)
3. Detailed spec updated (design-specs/*.md)
4. Main hub updated if needed (DESIGN.md - summaries/links)
5. Supporting docs updated if needed (theme, visual)
```

### Looking Up Information

**"What are the rules for combat?"**  
→ DESIGN.md (summary) → [combat-system.md](docs/design-specs/combat-system.md) (complete spec)

**"What cards should I design next?"**  
→ CHECKLIST.md (task status)

**"What is the enemy HP formula?"**  
→ [baseline-numbers.md](docs/design-specs/baseline-numbers.md) (all formulas)

**"How does the death loop work?"**  
→ [progression.md](docs/design-specs/progression.md) (complete death system)

**"What generator rates should Pack 1 have?"**  
→ [baseline-numbers.md](docs/design-specs/baseline-numbers.md) (generator rates by pack)

**"What color should Fire tier borders be?"**  
→ docs/visual-style-guide.md (implementation specs)

**"What naming convention for Air cards?"**  
→ docs/theme-specification.md (thematic reference)

**"Why did we choose combat-over-time?"**  
→ .cursor/log/sessions/session-2-0-3-combat-system-redesign.md (decision rationale)

**"What technology should I use?"**  
→ TECH-STACK.md (technology decisions)

---

## Maintenance Guidelines

### When to Update Each Document

**DESIGN.md:**
- When adding new major systems
- When system summaries change significantly
- Rarely for details (those go in design-specs/)

**design-specs/*.md:**
- Any time detailed specifications change
- When formulas are finalized
- When new mechanics are added
- When balance numbers update

**CHECKLIST.md:**
- Mark tasks complete as finished
- Add new tasks if scope changes

**ROADMAP.md:**
- Rarely - only if session structure changes
- Document session completion status

**docs/theme-specification.md:**
- When adding new tiers/elements
- When expanding thematic context
- Rarely after initial establishment

**docs/visual-style-guide.md:**
- When adding new UI components
- When establishing new visual patterns
- Rarely after initial establishment

**Session Logs:**
- Create new log for each major task
- Update throughout work session
- Finalize when task complete

### Version Control Strategy

**Main Documents:**
- Version info in document header
- Update version on significant changes
- Changelog section at bottom

**Design Specs:**
- Version info in document header
- Status field (Complete, Partial, Pending)
- Document history at bottom

**Session Logs:**
- Timestamped entries (immutable)
- No version numbers (historical record)
- New entries added, old entries never changed

---

## Document Status Summary

| Document | Lines | Status | Next Update |
|----------|-------|--------|-------------|
| **DESIGN.md** | 400 | ✅ Hub Complete | Session 2.1+ (minor) |
| **design-specs/combat-system.md** | 400 | ✅ Complete | Rarely |
| **design-specs/progression.md** | 350 | ✅ Complete | Rarely |
| **design-specs/resource-economy.md** | 250 | ✅ Complete | Session 4 (rates) |
| **design-specs/card-system.md** | 300 | 🔄 Partial | Session 2.1 (packs) |
| **design-specs/tier-class-system.md** | 350 | ✅ Complete | Session 7 (prestige) |
| **design-specs/baseline-numbers.md** | 400 | 🔄 Baseline Complete | Session 2.1 (pack targets) |
| **design-specs/first-30-minutes.md** | 350 | ✅ Complete | Rarely |
| CHECKLIST.md | 365 | ✅ Current | Task 2.0.6+ |
| ROADMAP.md | 690 | ✅ Current | Session 3+ |
| TECH-STACK.md | 650 | ✅ Current | Implementation |
| docs/theme-specification.md | 376 | ✅ Complete | Rarely |
| docs/visual-style-guide.md | 899 | ✅ Complete | Rarely |
| Session logs | ~3000 | ✅ Current | Ongoing |

---

## Benefits of Version 2.0 Structure

### For AI Agents

1. **Focused Context:** Each spec file is 250-400 lines, easily fits in context
2. **Clear Boundaries:** Each system has its own authoritative document
3. **Easier Updates:** Update only the relevant spec file
4. **Better Navigation:** DESIGN.md hub provides clear entry points

### For Human Readers

1. **Quick Reference:** DESIGN.md provides summaries and links
2. **Deep Dives:** Detailed specs available when needed
3. **Logical Organization:** Related content grouped together
4. **Easier Review:** Can review one system at a time

### For Project Management

1. **Better Collaboration:** Multiple people can work on different specs
2. **Clear Ownership:** Each spec has clear scope and status
3. **Version Control:** Easier to track changes per system
4. **Scalability:** Can add new spec files as game expands

---

## Future Considerations

### If Design Specs Grow Too Large

Consider splitting further:
- `combat-system.md` → `combat-mechanics.md` + `death-system.md`
- `tier-class-system.md` → `tier-system.md` + `class-system.md`

**Threshold:** Individual files exceeding 600 lines

### When Adding New Systems

Create new spec files following the pattern:
- Clear purpose and scope
- Status and completion tracking
- Parent document link (DESIGN.md)
- Document history section
- 250-400 line target

---

**Document Organization Status:** ✅ Version 2.0 Complete  
**Last Review:** 2025-11-08 (Documentation Restructure)  
**Next Review:** After Session 4 (mid-project checkpoint)
