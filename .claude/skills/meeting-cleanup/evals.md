---
skill: meeting-cleanup
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /meeting-cleanup

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Batch processing applied | Multiple meetings processed in a single run, not one at a time |
| E2 | Consistent format across meetings | All processed meetings use the same output structure |
| E3 | Output path correct | Files saved to `outputs/meeting-notes/` with date and meeting name |

### Quality & Voice

| ID | Check | Criteria |
|----|-------|----------|
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
| E8 | Key decisions extracted | Decisions pulled from each meeting into a clear list, not buried in notes |
| E9 | Action items with owners | Every action item has a named owner and due date |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Cross-meeting connections noted | Links between meetings flagged (e.g., a decision in one affects another) |
| E11 | Source transcript preserved | Original transcript or notes available for reference, not overwritten |
| E12 | Priority meetings flagged | Meetings ranked by urgency of follow-up needed |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
