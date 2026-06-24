---
skill: okr-planning
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /okr-planning

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
| E1 | OKR format correct | Each Objective has 2-5 Key Results; Key Results are measurable outcomes not tasks |
| E2 | Output path correct | File saved to `outputs/okrs/` with quarter and year in filename |
| E3 | Alignment shown | Each OKR traces to a company or team-level objective |

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
| E8 | Key Results quantified | Every Key Result has a specific number: baseline → target |
| E9 | Ambition calibrated | Mix of committed (70%+ confidence) and aspirational (30-50% confidence) KRs noted |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Anti-metrics included | At least one counter-metric per Objective to prevent gaming |
| E11 | Owner per KR | Each Key Result has a single named owner |
| E12 | Review cadence set | Specifies check-in frequency (weekly, bi-weekly) and scoring method |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
