---
skill: analytics-instrumentation
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /analytics-instrumentation

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Tracking plan structured | Events organized by user action or funnel stage, not randomly listed |
| E2 | Event schema complete | Each event has: name, trigger, properties with types, and sample values |
| E3 | Output path correct | File saved to `outputs/analytics/` or `outputs/analyses/` with feature name |

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
| E8 | Naming convention consistent | Event and property names follow a stated naming convention (snake_case, etc.) |
| E9 | Properties include context | Each event includes relevant context properties (user segment, plan, source) |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Key metrics derivable | Shows how the tracked events map to the success metrics from the PRD |
| E11 | Implementation notes included | Specifies where in the code each event should fire |
| E12 | Privacy considerations noted | Flags any PII or sensitive data in event properties |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
