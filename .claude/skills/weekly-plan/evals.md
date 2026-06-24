---
skill: weekly-plan
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /weekly-plan

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
| E1 | Week-level structure | Organized by weekly goals and daily focus areas, not just a task dump |
| E2 | Priority framework applied | Weekly priorities explicitly tied to quarterly OKRs or strategy |
| E3 | Output path correct | File saved to `outputs/weekly-plans/` with week identifier |

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
| E8 | Capacity realistic | Accounts for meeting load and focuses effort on 3-5 key outcomes |
| E9 | Carryover from last week | References what carried over from previous week's plan if available |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Key meetings flagged | High-stakes meetings identified with prep needed |
| E11 | Dependencies tracked | Notes what you're waiting on from others and expected delivery dates |
| E12 | Review checkpoint set | Suggests mid-week check-in point to assess progress |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
