---
skill: design-direction
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /design-direction

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
| E1 | Direction options presented | At least 2-3 distinct design directions with pros/cons for each |
| E2 | Visual or verbal moodboard | Each direction described with enough specificity to differentiate them |
| E3 | Output path correct | File saved to `outputs/design/` with feature in filename |

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
| E8 | User needs anchored | Each direction tied back to specific user needs or research findings |
| E9 | Technical feasibility noted | Each direction includes a feasibility assessment from engineering perspective |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Brand alignment checked | Directions evaluated against brand guidelines or design system |
| E11 | Recommendation stated | A clear recommendation for which direction to pursue with reasoning |
| E12 | Decision criteria provided | Framework for evaluating which direction to choose if more input needed |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
