---
skill: design-direction
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /design-direction

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
