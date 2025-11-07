# Rule Enhancement: Design Document Synchronization

**Date:** 2025-11-07 12:59:31  
**Reason:** Address Task 2.0 issues where design changes occurred without user approval or DESIGN.md updates

---

## Problem Statement

During Task 2.0 (Gameplay Simulator), several design changes were made without proper approval or documentation:
1. Enemy scaling formula changed from exponential to linear (without user approval)
2. Baseline validation targets changed significantly (without updating DESIGN.md)
3. "Tutorial death" boss concept added (new design not in DESIGN.md)
4. DESIGN.md errors discovered but not corrected

Current rules didn't explicitly prevent these issues.

---

## Rule Enhancements

### Rule 01: Background Assessment - Added "Design Document Integrity Check"

**New Section:** Design Document Integrity Check

**Purpose:** Require checking design documents for errors BEFORE implementation begins

**Key Requirements:**
- Check for mathematical/arithmetic correctness
- Check for internal contradictions
- Check for missing critical information
- STOP and present errors to user before implementing
- Never begin implementation knowing design docs contain errors

---

### Rule 02: Work Tracking - Added "Design Document Synchronization"

**New Section:** Design Document Synchronization

**Purpose:** Treat DESIGN.md as source of truth that must stay synchronized with implementation

**Key Requirements:**
- Implementation must match DESIGN.md specifications
- If deviation needed: STOP and seek approval
- After approval: Update DESIGN.md IMMEDIATELY (before or concurrent with implementation)
- Task completion checklist includes design/implementation synchronization check
- Never leave docs out of sync or defer updates to "later"

---

### Rule 03: Decision Validation - Enhanced and Added Protocol

**Enhanced:** User Confirmation Requirements (expanded significant decisions list)

**Added Items:**
- Changing any formulas, numbers, or calculations in DESIGN.md
- Discovering DESIGN.md contains unworkable/broken design elements
- Changing baseline numbers or validation targets
- Substituting alternative mechanics
- Adding design concepts not present in DESIGN.md

**New Section:** Design Document Change Protocol

**Purpose:** Explicit protocol for handling design document problems discovered during implementation

**Key Requirements:**
- STOP immediately when discovering design bugs/contradictions
- Present to user: Problem, Evidence, Options, Recommendation, Impact
- After approval: Update DESIGN.md FIRST, then implement
- Never continue with known design bugs or change design without updating docs

---

### Rule 05: Realistic Partnership - Added "Design Document Stewardship"

**New Section:** Design Document Stewardship

**Purpose:** Make design document accuracy and synchronization part of accountability

**Key Requirements:**
- Treat DESIGN.md as contract between sessions
- Speak up immediately when finding design problems
- Hold yourself accountable: verify work matches DESIGN.md
- Hold user accountable: request doc updates when decisions change
- Design doc errors are blocking issues

---

## How These Prevent Task 2.0 Issues

### Issue: Enemy scaling formula changed without approval
**Prevention:** 
- Rule 03 "Design Document Change Protocol" requires STOP and user presentation
- Rule 03 expanded "Significant Decisions" explicitly includes "changing formulas in DESIGN.md"

### Issue: Baseline numbers changed without updating DESIGN.md
**Prevention:**
- Rule 02 "Design Document Synchronization" requires updating DESIGN.md immediately
- Task completion checklist includes sync verification

### Issue: DESIGN.md errors discovered but not fixed
**Prevention:**
- Rule 01 "Design Document Integrity Check" requires reporting errors during background assessment
- Rule 05 "Design Document Stewardship" treats errors as blocking issues

### Issue: New design concepts added (tutorial boss) without approval
**Prevention:**
- Rule 03 expanded "Significant Decisions" includes "Adding design concepts not present in DESIGN.md"

---

## Key Principles Established

1. **DESIGN.md is the Contract:** Between design sessions and implementation sessions
2. **Design Problems are Blocking:** Cannot proceed with known design bugs
3. **Synchronization is Mandatory:** Implementation and DESIGN.md must match
4. **Design Changes Need Approval:** Even "obvious" fixes require user confirmation
5. **Update Docs First:** DESIGN.md updated before or concurrent with implementation

---

## Files Modified

- `.cursor/rules/01-background-assessment.mdc` - Added Design Document Integrity Check
- `.cursor/rules/02-work-tracking.mdc` - Added Design Document Synchronization  
- `.cursor/rules/03-decision-validation.mdc` - Enhanced list, added Change Protocol
- `.cursor/rules/05-realistic-partner.mdc` - Added Design Document Stewardship

---

## Next Steps

These enhanced rules will apply to all future work. For Task 2.1 and beyond:
- Check DESIGN.md for errors during background assessment
- Report any design problems before implementing
- Update DESIGN.md when design changes are approved
- Verify synchronization before marking tasks complete

---

**Status:** Rules Enhanced and Active  
**Applied Starting:** Immediately (next task begins with enhanced rules)

