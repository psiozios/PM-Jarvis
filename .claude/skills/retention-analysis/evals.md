---
skill: retention-analysis
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /retention-analysis

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
| E1 | Cohort table present | Contains a cohort retention table with clearly labeled time periods and percentages |
| E2 | Methodology stated | Analysis method described: which cohort definition, time window, and metric used |
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
| E8 | Benchmark comparison | Retention curves compared against at least one benchmark (industry, prior cohort, or target) |
| E9 | Drop-off points identified | Specific time periods where retention drops most sharply are called out with hypotheses |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Segment breakdown included | Retention analyzed by at least 2 user segments (e.g., plan type, acquisition channel) |
| E11 | Recommendations tied to data | Each recommendation directly references a specific data pattern in the analysis |
| E12 | Leading indicators suggested | Proposes early signals that predict long-term retention for monitoring |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
