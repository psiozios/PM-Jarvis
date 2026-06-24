---
skill: meeting-cleanup
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /meeting-cleanup

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
| E1 | Batch processing applied | Multiple meetings processed in a single run, not one at a time |
| E2 | Consistent format across meetings | All processed meetings use the same output structure |
| E3 | Output path correct | Files saved to `outputs/meeting-notes/` with date and meeting name |

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
