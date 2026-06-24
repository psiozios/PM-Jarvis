---
skill: feature-results
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /feature-results

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
| E1 | Results template followed | Contains: Hypothesis Recap, Results, Analysis, Learnings, Next Steps sections |
| E2 | Pre/post comparison | Shows metrics before and after launch with the same measurement methodology |
| E3 | Output path correct | File saved to `outputs/analyses/` with feature and date in filename |

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
| E8 | Hypothesis verdict explicit | States clearly: confirmed, partially confirmed, or rejected — with evidence |
| E9 | Unintended effects noted | Documents any unexpected positive or negative side effects observed |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Statistical confidence noted | States whether sample size is sufficient and if results are statistically significant |
| E11 | Goal vs actual compared | Every pre-launch metric target compared against actual result |
| E12 | Next steps concrete | States: iterate, scale, pivot, or kill — with specific reasoning |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
