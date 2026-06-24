---
skill: update-docs
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /update-docs

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
| E1 | Changed files identified | Lists all documentation files that need updating based on code changes |
| E2 | Changes match code diff | Documentation updates accurately reflect what changed in the code |
| E3 | No stale references | Updated docs don't reference old function names, paths, or behaviors |

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
| E8 | Examples updated | Code examples in documentation reflect the new implementation |
| E9 | Migration notes included | If breaking changes, includes migration guide for users |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | API documentation current | Function signatures, parameters, and return types match current code |
| E11 | Changelog entry drafted | Suggests a changelog entry summarizing what changed and why |
| E12 | Cross-references checked | Other docs that reference the changed code are identified for update |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
