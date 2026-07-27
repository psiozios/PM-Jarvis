---
skill: meeting-feedback
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /meeting-feedback

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
