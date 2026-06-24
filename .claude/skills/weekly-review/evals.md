---
skill: weekly-review
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /weekly-review

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
| E1 | Plan vs actual structure | Compares planned priorities to what actually happened |
| E2 | Workspace data scanned | Pulls from recent outputs, meeting notes, and PRD changes in the workspace |
| E3 | Output path correct | File saved to `outputs/weekly-reviews/` with week identifier |

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
| E8 | Wins and misses explicit | Clearly states what went well and what didn't — not just a summary |
| E9 | Learnings extracted | At least 1 actionable learning for next week, not just observations |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | PRD progress tracked | Active PRDs categorized: Advanced / Active / Stalled / New |
| E11 | Stakeholder pulse noted | Notes any stakeholder sentiment shifts or relationship changes |
| E12 | Feeds into weekly-plan | Explicitly sets up context for next week's planning |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
