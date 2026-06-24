---
skill: code-review
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /code-review

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
| E1 | Dimension-organized review | Review structured by dimension (error handling, security, performance, etc.) not by file |
| E2 | Severity tagged | Every finding has a severity: CRITICAL, HIGH, MEDIUM, or LOW |
| E3 | Output path correct | File saved to `outputs/analyses/code-review-[scope]-[date].md` |

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
| E8 | File:line references | Every finding includes specific file path and line number |
| E9 | Suggested fix included | Each finding includes a concrete suggested fix, not just 'this is wrong' |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Positives acknowledged | At least 2-3 things done well are noted — not just problems |
| E11 | False positives avoided | Each finding verified against actual code context before reporting |
| E12 | Clear recommendation | Final recommendation is PASS / PASS WITH NOTES / FAIL |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
