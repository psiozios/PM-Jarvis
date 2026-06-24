---
skill: feature-metrics
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /feature-metrics

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
| E1 | STEDII framework applied | Uses the STEDII framework for metric selection |
| E2 | Leading and lagging separated | Clearly distinguishes leading indicators from lagging outcomes |
| E3 | Output path correct | File saved to `outputs/analyses/` with feature name in filename |

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
| E8 | Each metric has measurement plan | Every metric specifies: data source, calculation method, and reporting frequency |
| E9 | Targets with timelines | Every metric has a baseline, target, and timeline — not just 'improve X' |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Counter-metrics included | At least one metric that guards against unintended consequences |
| E11 | Dashboard-ready format | Metrics organized in a format that could be directly implemented in a dashboard |
| E12 | Review cadence defined | States when metrics will be reviewed and what triggers a deeper investigation |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
