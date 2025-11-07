# Document Index - Idle Card Battler

**Purpose:** Quick reference to all project documents and their purposes.  
**Last Updated:** 2025-11-06

---

## Core Project Documents

### CHECKLIST.md
**Purpose:** Granular task tracking with completion status  
**Audience:** You (project owner), AI assistant  
**Update Frequency:** Every task completion  
**Scope:** All sessions, specific tasks and sub-tasks

### ROADMAP.md
**Purpose:** Session structure, deliverables, and methodology  
**Audience:** You (project owner), AI assistant  
**Update Frequency:** Per session or when methodology changes  
**Scope:** Big picture organization and approach

### DESIGN.md
**Purpose:** **Single source of truth** for all game design decisions  
**Audience:** Future developers, AI assistant, design reference  
**Update Frequency:** As design decisions are made  
**Scope:** Complete game design specification  
**Size:** 1260 lines (manageable, may split at 2000+ lines)

**Key Sections:**
- Core Vision & Mechanics
- Theme & Setting (summary)
- Tier & Class Systems
- Resource Generation & Economy
- Deck Building System
- Card Collection & Packs
- Combat System
- Prestige & Progression
- Resolved Design Decisions (Session 1.2)
- First 30 Minutes Experience (Session 1.3A)
- Baseline Numbers Reference (Session 1.3B)
- Starter Deck Specification (Session 1.3C)
- Outstanding Design Questions

### TECH-STACK.md
**Purpose:** Implementation technology decisions and rationale  
**Audience:** Future developers  
**Update Frequency:** Rarely (established decisions)  
**Scope:** Frontend, backend, hosting, tools, workflows

---

## Supporting Documents (docs/)

### docs/theme-specification.md
**Purpose:** Thematic reference for writing flavor text and content  
**Audience:** Content creators, writers  
**Use Case:** Consulted when writing card names, flavor text, class names  
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
**Audience:** AI assistant (for continuity), you (for process review)  
**Update Frequency:** During each work session  
**Scope:** Detailed log of actions, decisions, and reasoning

**Current Logs:**
- `session-1-1-theme-selection.md` - Theme establishment
- `session-1-1A-visual-direction.md` - Visual style guide creation
- `session-1-2-critical-design-decisions.md` - 5 major questions resolved
- `session-1-3-high-level-experience.md` - First 30 minutes design (Part A)
- `session-1-3b-baseline-numbers.md` - Economy numbers and validation (Part B)
- `session-1-3c-starter-cards.md` - 8 starter cards designed (Part C)

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
- `.archive/session-1/economy-model-v1.3.md` - Working document from Session 1.3, now fully integrated into DESIGN.md

**Policy:** See `.archive/README.md` for archive criteria

---

## Document Relationships

### Authoritative Sources (Single Source of Truth)

```
DESIGN.md           ← Game design decisions (authoritative)
TECH-STACK.md       ← Technology decisions (authoritative)
CHECKLIST.md        ← Task status (authoritative)
ROADMAP.md          ← Session structure (authoritative)
```

### Implementation References (Derived from Design)

```
DESIGN.md → docs/theme-specification.md       (thematic subset)
DESIGN.md → docs/visual-style-guide.md        (visual implementation details)
```

### Historical Record (Process Documentation)

```
Session Work → .cursor/log/sessions/*.md      (detailed logs)
             ↓
          DESIGN.md                            (final decisions)
```

---

## Information Flow

### During Design Sessions
```
1. Work performed with decisions made
2. Session log created/updated (detailed record)
3. Main document updated (DESIGN.md, CHECKLIST.md)
4. Supporting docs updated if needed (theme, visual)
```

### Looking Up Information

**"What are the rules for X?"**
→ DESIGN.md (single source of truth)

**"What cards should I design next?"**
→ CHECKLIST.md (task status)

**"What should Pack 3 contain?"**
→ ROADMAP.md (session deliverables) → DESIGN.md (specific requirements)

**"What color should Fire tier borders be?"**
→ docs/visual-style-guide.md (implementation specs)

**"What naming convention for Air cards?"**
→ docs/theme-specification.md (thematic reference)

**"Why did we choose stacking generators?"**
→ .cursor/log/sessions/session-1-3b-baseline-numbers.md (decision rationale)

**"What technology should I use?"**
→ TECH-STACK.md (technology decisions)

---

## Maintenance Guidelines

### When to Update Each Document

**DESIGN.md:**
- Any time a design decision is made or changed
- When new systems are specified
- When outstanding questions are resolved

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

**Session Logs:**
- Timestamped entries (immutable)
- No version numbers (historical record)
- New entries added, old entries never changed

---

## Document Status Summary

| Document | Lines | Status | Next Update |
|----------|-------|--------|-------------|
| CHECKLIST.md | 250 | ✅ Current | Session 2 start |
| ROADMAP.md | 471 | ✅ Current | Session 2 complete |
| DESIGN.md | 1260 | ✅ Current | Session 2 work |
| TECH-STACK.md | 650 | ✅ Current | Implementation phase |
| docs/theme-specification.md | 376 | ✅ Complete | Rarely |
| docs/visual-style-guide.md | 899 | ✅ Complete | Rarely |
| Session logs | ~2000 | ✅ Current | Ongoing |

---

## Future Considerations

### If DESIGN.md Exceeds 2000 Lines

Consider splitting into:
- `DESIGN-CORE.md` - Systems, mechanics, core rules
- `DESIGN-CONTENT.md` - Cards, classes, specific content examples

**Threshold:** Not needed yet, reassess at 1800+ lines

### If Session Logs Become Unwieldy

Consider:
- Creating session summary document
- Archiving very old sessions
- Maintaining "active sessions" vs "completed sessions" directories

**Threshold:** Not needed yet, reassess at 15+ session logs

---

**Document Organization Status:** ✅ Optimized  
**Last Review:** 2025-11-06  
**Next Review:** After Session 4 (mid-project checkpoint)

