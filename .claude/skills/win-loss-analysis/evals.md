---
skill: win-loss-analysis
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /win-loss-analysis

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
| E1 | Win/loss structure | Organized by: Win Patterns, Loss Patterns, Competitive Dynamics, Recommendations |
| E2 | Sample described | States number of deals analyzed, time period, and any selection criteria |
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
| E8 | Quotes preserved | Includes verbatim quotes from sales reps or customers for key patterns |
| E9 | Win/loss reasons quantified | Top reasons ranked by frequency with counts, not just listed |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Competitor-specific patterns | Each major competitor has specific win/loss patterns, not generic |
| E11 | Product gaps vs sales gaps | Distinguishes between product capability gaps and sales execution gaps |
| E12 | Actionable recommendations | Each recommendation maps to a specific win/loss pattern and has a proposed owner |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
