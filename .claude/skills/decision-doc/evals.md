---
skill: decision-doc
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /decision-doc

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Decision template structure | Contains: Context, Options Considered, Decision, Rationale, Consequences sections |
| E2 | Output path correct | File saved to `outputs/decisions/` with date-prefixed filename |
| E3 | Options compared fairly | At least 2 options presented with pros/cons for each — not just the chosen option |

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
| E8 | Reversibility stated | Explicitly states whether the decision is reversible or irreversible and the cost of reversal |
| E9 | Stakeholder input documented | Names who was consulted and what they recommended |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Dissent captured | If disagreement existed, it's documented with the dissenter's reasoning |
| E11 | Review date set | Includes a specific date or trigger for revisiting the decision |
| E12 | Consequences specific | Lists concrete downstream effects, not vague 'this will impact the team' |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
