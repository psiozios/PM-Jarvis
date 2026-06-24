---
skill: define-north-star
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /define-north-star

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
| E1 | North Star metric defined | Single metric identified with clear name, formula, and measurement method |
| E2 | Criteria for selection stated | Explains why this metric was chosen over alternatives using selection criteria |
| E3 | Output path correct | File saved to `outputs/analyses/` or `outputs/strategy/` with date |

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
