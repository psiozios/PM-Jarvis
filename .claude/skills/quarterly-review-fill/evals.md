---
skill: quarterly-review-fill
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /quarterly-review-fill

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
| E1 | Months Rolled Up table present | Lists all three months with rating and link |
| E2 | OKR Progress table present | Grades the quarter against stated objectives from `context-library/strategy/` |
| E3 | Period correctly identified | Output header states the exact quarter (YYYY-QN) being filled |

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
| E8 | Tier-appropriate rollup | The assessment synthesizes the completed monthly entries, not raw weeks or task-tracker activity |
| E9 | Graded against OKRs | The draft explicitly assesses progress against the quarter's stated strategy, not just a recap of activity |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Missing-month handling correct | Any month without a completed entry triggered `monthly-review-fill` rather than being skipped or backfilled from a lower tier |
| E11 | Surgical write | The write to the reviews store was a delta, not a full replace |
| E12 | Forward-create-with-dedupe | Forward-created quarters were checked against existing shells before creation |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
