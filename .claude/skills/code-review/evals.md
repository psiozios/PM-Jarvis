---
skill: code-review
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /code-review

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
