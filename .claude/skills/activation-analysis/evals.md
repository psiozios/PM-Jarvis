---
skill: activation-analysis
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /activation-analysis

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
| E1 | Activation funnel present | Contains Setup → Aha Moment → Habit stages with conversion rates between each |
| E2 | Aha moment defined | Explicitly defines what the 'aha moment' is with the specific user action |
| E3 | Output path correct | File saved to `outputs/analyses/` with product and date in filename |

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
| E8 | Drop-off quantified per step | Each funnel step shows conversion rate and absolute user counts |
| E9 | Time-to-value measured | States median time from signup to aha moment and to habit formation |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Segment comparison | Activation rates compared across at least 2 user segments |
| E11 | Intervention points identified | Specific points in the funnel where product changes could improve conversion |
| E12 | Benchmark or target stated | Each funnel step has a target conversion rate or industry benchmark |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
