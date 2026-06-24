---
skill: meeting-notes
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /meeting-notes

## How to Run (automatic on every skill invocation)

1. Original agent completes skill output and runs informal self-check
2. Original agent spawns a separate eval agent (clean context window)
3. Eval agent reads: this file, the skill output, `config/house-style.md`
4. Evaluates each criterion independently → PASS / FAIL / PARTIAL
5. FAILs returned to original agent for revision → re-eval loop
6. Zero FAILs achieved → log results below

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
| E4 | No AI slop | Zero instances of: delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Follows any active rules in `config/house-style.md` |
| E6 | Human-sounding | Varied sentence lengths, contractions used naturally, no formulaic paragraph openings |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | References specific data from context sources — not generic placeholder language |
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
