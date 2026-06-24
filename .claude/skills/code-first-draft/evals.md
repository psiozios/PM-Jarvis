---
skill: code-first-draft
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /code-first-draft

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
| E1 | Codebase conventions followed | Code style, naming, and structure match existing patterns in the project |
| E2 | File placement correct | New files created in the appropriate directory per project structure |
| E3 | No placeholder TODOs | All implementations are complete — no TODO or FIXME stubs left behind |

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
| E8 | PRD requirements mapped | Each requirement from the PRD or spec is addressed in the implementation |
| E9 | Error handling included | Edge cases and error paths handled, not just the happy path |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Tests included | At least basic test coverage for the new code |
| E11 | Dependencies minimal | No unnecessary new dependencies introduced — uses existing libraries where possible |
| E12 | Summary document provided | Brief summary of what was built, how to test it, and any known limitations |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
