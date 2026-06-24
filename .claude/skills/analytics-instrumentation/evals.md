---
skill: analytics-instrumentation
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /analytics-instrumentation

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
| E1 | Tracking plan structured | Events organized by user action or funnel stage, not randomly listed |
| E2 | Event schema complete | Each event has: name, trigger, properties with types, and sample values |
| E3 | Output path correct | File saved to `outputs/analytics/` or `outputs/analyses/` with feature name |

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
