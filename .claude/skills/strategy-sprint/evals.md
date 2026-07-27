---
skill: strategy-sprint
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /strategy-sprint

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Sprint duration matched | Workflow matches the chosen duration: 1 day, 1 week, or 1 month sprint |
| E2 | Phased deliverables clear | Each phase has a specific deliverable with definition of done |
| E3 | Output path correct | File saved to `outputs/strategy/` with sprint duration and date |

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
| E8 | Stakeholder input planned | Identifies who to consult and when during the sprint |
| E9 | Decision points scheduled | Key decision moments built into the sprint timeline |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Research vs synthesis balanced | Sprint allocates time for both gathering input and synthesizing output |
| E11 | Final deliverable defined | States exactly what artifact comes out of the sprint and for whom |
| E12 | Cross-skill integration | Links to specific skills needed at each phase (/competitor-analysis, /write-prod-strategy, etc.) |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
