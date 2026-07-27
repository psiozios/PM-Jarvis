---
skill: define-north-star
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /define-north-star

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | North Star metric defined | Single metric identified with clear name, formula, and measurement method |
| E2 | Criteria for selection stated | Explains why this metric was chosen over alternatives using selection criteria |
| E3 | Output path correct | File saved to `outputs/analyses/` or `outputs/strategy/` with date |

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
| E8 | Alternatives considered | At least 2 alternative metrics evaluated and rejected with reasoning |
| E9 | Input metrics mapped | Shows 3-5 input metrics that teams can directly influence to move the North Star |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Current baseline stated | Includes current value of the metric and recent trend |
| E11 | Target set with rationale | North Star target has both a number and reasoning for why that number |
| E12 | Anti-gaming measure included | At least one guardrail metric to prevent optimizing the North Star at the expense of user value |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
