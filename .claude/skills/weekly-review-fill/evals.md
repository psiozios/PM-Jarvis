---
skill: weekly-review-fill
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /weekly-review-fill

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
| E1 | Auto-vs-asked table present | Shown before the full draft, clearly separating auto-filled from asked items |
| E2 | Period correctly identified | Output header states the exact week (YYYY-Www) being filled |
| E3 | Forward-created periods listed | Output states which future week shells were created |

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
