---
skill: metrics-framework
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /metrics-framework

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
| E1 | Framework structure complete | Contains: North Star, Leading Indicators, Lagging Indicators, Health Metrics sections |
| E2 | Metric hierarchy clear | Shows how individual metrics ladder up to the North Star metric |
| E3 | Output path correct | File saved to `outputs/analyses/` with date in filename |

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
| E8 | Each metric operationally defined | Every metric has: name, formula, data source, owner, and review frequency |
| E9 | Input vs output metrics distinguished | Separates metrics the team can directly influence from outcome metrics |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Alert thresholds set | Key metrics have defined thresholds that trigger investigation |
| E11 | Metric relationships mapped | Shows which leading indicators predict which lagging outcomes |
| E12 | Gaming risks identified | For each key metric, notes how it could be gamed and the counter-metric |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
