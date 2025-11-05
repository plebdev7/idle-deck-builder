# Task Logging System

This directory contains task-based logs for all work performed on the Idle Card Battler project. The logging system is part of the project's strict methodology for AI agent collaboration.

## Purpose

The logging system serves multiple purposes:
- **Accountability**: Track all work performed with detailed evidence
- **Cross-Referencing**: Link work to CHECKLIST.md and ROADMAP.md items
- **Validation**: Demonstrate that work was completed correctly
- **Historical Record**: Enable reconstruction of design decisions and implementation choices
- **Impact Assessment**: Document which files were affected by which tasks

## Naming Convention

Log files follow this naming pattern:

```
session-X-Y-task-name.md
```

Where:
- `X` = Session number from ROADMAP.md (e.g., 1, 2, 3)
- `Y` = Task number within that session (e.g., 1, 2, 3)
- `task-name` = Brief descriptive kebab-case name

### Examples

- `session-1-1-theme-selection.md` - Session 1, Task 1.1 (Theme Selection)
- `session-1-2-critical-decisions.md` - Session 1, Task 1.2 (Critical Design Decisions)
- `session-2-1-card-system-spec.md` - Session 2, Task 2.1 (Card System Specification)
- `session-3-2-class-system-design.md` - Session 3, Task 3.2 (Class System Design)

## Log File Structure

Every log file MUST use the template provided in `log-template.md`. The template includes:

### Required Sections

1. **Task Information** - Basic metadata about the task
2. **Background Assessment** - Files read and impact analysis
3. **Work Log** - Chronological entries of all actions taken
4. **Decisions Made** - All design and implementation decisions with rationale
5. **User Confirmations** - Record of user approvals and feedback
6. **Validation Status** - How work was validated and checked
7. **Deliverables** - Complete list of files created, modified, or deleted
8. **Completion Summary** - Objectives met and outstanding issues
9. **Cross-References** - Links to related logs and documentation

### Structured Entry Format

Each work log entry must include:
- **Timestamp** (ISO format: YYYY-MM-DD HH:MM:SS)
- **Action Taken** (detailed description)
- **Files Impacted** (complete list with descriptions)
- **Rationale** (why this action was taken)
- **Validation** (how it was checked/verified)

## Usage Guidelines

### Creating a New Log

1. Identify the ROADMAP session and task number
2. Create file with proper naming convention
3. Copy template from `log-template.md`
4. Fill in Task Information section before starting work
5. Complete Background Assessment before making changes

### Maintaining Logs

- Update logs **during** task execution, not after
- Add work entries as actions are performed
- Record decisions when they are made
- Log user confirmations immediately after receiving them
- Keep entries detailed enough to reconstruct work later

### Completing Logs

Before marking a task complete:
1. Fill in End Time and Status
2. Complete Validation Status section
3. List all Deliverables with descriptions
4. Write Completion Summary
5. Update Cross-References section
6. Verify all required sections are filled

## Cross-Referencing

Logs enable cross-referencing in multiple directions:

- **Task → Files**: Which files were affected by a task
- **File → Tasks**: Which tasks modified a specific file
- **Decision → Impact**: How decisions affected implementation
- **Session → Progress**: Track progress through ROADMAP sessions

## Validation

Logs must demonstrate that work was validated:
- Linter checks performed
- Cross-checks with DESIGN.md, ROADMAP.md, CHECKLIST.md
- User confirmations obtained when required
- Issues identified and resolved

## Historical Integrity

- **Never delete** historical log entries
- **Never significantly alter** completed logs
- Add corrections as new entries with timestamps
- Preserve original context even when mistakes are corrected

## Finding Logs

To find relevant logs:
- Look up session/task numbers from ROADMAP.md or CHECKLIST.md
- Use the naming convention to locate files
- Check Cross-References sections in related logs
- Search for file paths within logs to find which tasks affected them

## Example Workflow

1. User assigns Task 1.1 from CHECKLIST.md
2. Agent creates `session-1-1-theme-selection.md`
3. Agent fills in Background Assessment
4. Agent performs work, logging each action
5. Agent records decisions and user confirmations
6. Agent validates work and documents validation
7. Agent completes summary and cross-references
8. Task log serves as proof of completion

## Integration with Rules

This logging system is enforced by `.cursor/rules/02-work-tracking.mdc`. All work must be logged according to these standards.

## Questions?

If you're unsure how to log something:
- Err on the side of more detail rather than less
- Reference `log-template.md` for structure
- Check existing logs for examples
- When in doubt, document it

---

**Remember:** The logging system exists to ensure accountability, enable validation, and maintain a historical record. Detailed, honest logging is essential to the project's methodology.

