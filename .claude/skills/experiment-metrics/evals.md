---
skill: experiment-metrics
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /experiment-metrics

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
| E1 | STEDII framework applied | Uses Sample, Trigger, Enrollment, Duration, Inference, Iteration framework |
| E2 | Primary metric defined | Single primary metric identified with clear measurement definition |
| E3 | Output path correct | File saved to `outputs/analyses/` with experiment name and date |

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
| E8 | Sample size calculated | Minimum sample size stated with power analysis parameters (MDE, significance, power) |
| E9 | Guardrail metrics listed | At least 2 guardrail metrics that must not degrade |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Duration justified | Experiment duration based on traffic volume and minimum detectable effect, not arbitrary |
| E11 | Decision criteria pre-registered | States upfront: what result leads to ship, iterate, or kill |
| E12 | Novelty and seasonal effects addressed | Acknowledges potential confounds and how they'll be controlled |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
