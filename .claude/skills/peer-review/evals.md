---
skill: peer-review
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /peer-review

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
