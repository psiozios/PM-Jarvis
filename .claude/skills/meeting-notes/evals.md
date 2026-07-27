---
skill: meeting-notes
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /meeting-notes

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Structured template used | Contains: Attendees, Decisions, Action Items, Discussion Summary, Open Items |
| E2 | Action items are first-class | Action items prominent and easy to scan — not buried in paragraphs |
| E3 | Output path correct | File saved to `outputs/meeting-notes/` with date and meeting topic |

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
| E8 | Decisions documented with context | Each decision includes the rationale and who made it |
| E9 | Owner on every action | Every action item has a named owner and due date or 'ASAP' |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Attendee list complete | All participants listed, including those who joined late or left early |
| E11 | Open items tracked | Unresolved questions listed with owners for follow-up |
| E12 | Follow-up meeting noted | If a follow-up is needed, date/time suggested or flagged for scheduling |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
