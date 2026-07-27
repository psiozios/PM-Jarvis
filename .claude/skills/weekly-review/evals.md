---
skill: weekly-review
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /weekly-review

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
