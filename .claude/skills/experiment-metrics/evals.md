---
skill: experiment-metrics
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /experiment-metrics

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
