---
skill: weekly-review-fill
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /weekly-review-fill

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Auto-vs-asked table present | Shown before the full draft, clearly separating auto-filled from asked items |
| E2 | Period correctly identified | Output header states the exact week (YYYY-Www) being filled |
| E3 | Forward-created periods listed | Output states which future week shells were created |

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
| E8 | Auto-vs-asked correctness | Nothing derivable from the task tracker or calendar was placed in "asked"; no judgment item was auto-filled with an unconfirmed guess |
| E9 | Never-blank-questionnaire | Every section of the draft has real content to react to, not an empty field |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Forward-create-with-dedupe | Forward-created weeks were checked against existing shells before creation |
| E11 | Surgical write | The write to the reviews store was a delta against current state, not a full replace |
| E12 | Preview-first | Nothing was written until the draft (including judgment-question answers) was confirmed |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
