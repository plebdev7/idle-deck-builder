# Log

Maintain task logs according to the project's logging methodology.

## Purpose

This command ensures proper task logging throughout the development process. All work must be documented in structured log files that provide accountability, enable validation, and create a historical record of decisions and implementations.

## When Invoked

When this command is called, perform the following actions:

### 1. Identify Current Task

- Determine which ROADMAP.md session and CHECKLIST.md item is being worked on
- If unclear, ask the user to specify the current task
- Session/task logs go in `.cursor/log/sessions/`
- Setup/configuration logs go in `.cursor/log/setup/`
- Planning/meta work logs go in `.cursor/log/administrative/`

### 2. Find or Create Log File

**For Session/Task Work:**
- Use naming convention: `sessions/session-X-Y-task-name.md`
  - X = Session number from ROADMAP.md
  - Y = Task number within session
  - task-name = Brief descriptive kebab-case name
- Example: `sessions/session-1-1-theme-selection.md`

**For Setup/Administrative Work:**
- Use descriptive names: `setup/tooling-setup.md` or `administrative/planning-discussion.md`

**Creating New Logs:**
- Copy the structure from `.cursor/log/log-template.md`
- Fill in Task Information section immediately
- Complete Background Assessment before making any changes

### 3. Add Work Log Entry

Create a new entry in the Work Log section with:

**Timestamp:** Use `get_timestamp()` MCP tool (returns YYYY-MM-DD HH:MM:SS format)

**Action Taken:**
- Detailed description of what was done
- Be specific about implementation details

**Files Impacted:**
- Complete list of files read, modified, created, or deleted
- Describe what changed in each file

**Rationale:**
- Explain WHY this action was taken
- Link to design decisions or requirements

**Validation:**
- How was this work validated or checked?
- Include linter results, tests run, or manual verification

### 4. Record Decisions

If any decisions were made during the work:

**Decision:**
- What was decided

**Options Considered:**
- List alternatives with pros/cons

**Chosen Approach:**
- Which option was selected and why

**User Confirmation:**
- Did the user approve? When and how?

**Rationale:**
- Detailed reasoning

**Implications:**
- What this affects (immediate and long-term)

### 5. Update Status and Cross-References

- Update task status (In Progress / Completed / Blocked)
- Update End Time if task is complete
- Fill in Validation Status section
- Update Cross-References to link with DESIGN.md, ROADMAP.md, CHECKLIST.md
- List related log files

### 6. Ensure Completeness

Before finishing, verify:
- [ ] Timestamps are present and accurate (use `get_timestamp()`)
- [ ] All files impacted are documented
- [ ] Decisions include rationale
- [ ] User confirmations are recorded
- [ ] Validation checks are documented
- [ ] Cross-references are complete
- [ ] Log follows template structure

## Key Reminders

- **Log DURING work**, not after completion
- **Use `get_timestamp()` MCP tool** for all timestamps (format: YYYY-MM-DD HH:MM:SS)
- **Never delete** historical log entries
- **Be detailed** - logs must enable reconstruction of work
- **Cross-reference** with CHECKLIST.md and ROADMAP.md
- **Record user confirmations** immediately when received
- **Document validation** - how was correctness verified?

## Template Location

The complete log template is available at `.cursor/log/log-template.md`

## Directory Structure

```
.cursor/log/
├── sessions/        # Session/task logs (session-X-Y-task-name.md)
├── setup/          # Setup and configuration logs
├── administrative/ # Planning and meta work logs
├── README.md       # Logging system documentation
└── log-template.md # Template for all logs
```

## Integration with Methodology

Logging is a core requirement of the project's AI collaboration methodology. See `.cursor/log/README.md` and workspace rules for complete details.

---

**Action Required:** When `/log` is invoked, actively create or update the appropriate log file with a new entry using the current timestamp and following the structure above.

