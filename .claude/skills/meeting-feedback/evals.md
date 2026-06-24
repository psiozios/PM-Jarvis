---
skill: meeting-feedback
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /meeting-feedback

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
| E1 | Feedback structure used | Contains: Effectiveness Rating, What Worked, What to Improve, Recommendations |
| E2 | Meeting-type-aware | Feedback calibrated to the meeting type (standup, planning, 1:1, exec review) |
| E3 | Output path correct | File saved to `outputs/` with meeting type and date |

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
| E8 | Specific observations cited | Each feedback point references a specific moment or behavior, not generalities |
| E9 | Improvement is actionable | Each 'what to improve' item has a concrete suggestion for next time |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Facilitation assessed | Evaluates whether the facilitator managed time, participation, and decisions well |
| E11 | Outcome vs purpose compared | Checks whether the meeting achieved its stated purpose |
| E12 | Pattern tracking suggested | Recommends tracking recurring meeting issues over time |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
