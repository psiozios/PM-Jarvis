---
skill: peer-review
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /peer-review

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
| E1 | Cross-model verification format | Each finding from the other AI verified with: CONFIRMED, FALSE POSITIVE, PARTIALLY VALID, or NEEDS INVESTIGATION |
| E2 | Evidence-based verdicts | Each verdict cites specific file:line evidence from the actual codebase |
| E3 | Output path correct | File saved to `outputs/analyses/` with review source and date |

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
| E8 | Credit given for good catches | Confirmed findings acknowledge the original tool's contribution |
| E9 | False positives explained | Each false positive includes why the original tool was wrong with specific evidence |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | New findings added | Notes any issues the original review missed that were discovered during verification |
| E11 | Severity re-assessed | Each finding's severity independently evaluated and adjusted if needed |
| E12 | Summary recommendation | Final verdict: how trustworthy was the original review overall |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
