---
skill: refinement-prep
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /refinement-prep

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Theme stated | Output header states the ceremony's theme |
| E2 | Ranked shortlist format | Items numbered in rank order, each with enrichment and unknowns |
| E3 | Cut-list included | A separate section shows items considered but cut, with why |

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
| E8 | Theme asked before board read | The theme was obtained (asked or given) before ranking began, not inferred silently |
| E9 | Read-only honored | No evidence the skill wrote to, moved, or edited any item on the board itself |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Correct ranking order | Ranking demonstrably applied theme-fit first, then live priority, then readiness — not an arbitrary order |
| E11 | Shortlist genuinely capped | The shortlist is smaller than the full filtered candidate set, sized to what a ceremony can cover |
| E12 | Rework-causing unknowns only | Surfaced unknowns are ones that would cause rework if unresolved, not a dump of every open question |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
