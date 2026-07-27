---
skill: sprint-planning
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /sprint-planning

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Sprint backlog structured | Items organized by priority with story points or size estimates |
| E2 | Capacity calculated | Team capacity computed based on headcount, time off, and meeting overhead |
| E3 | Output path correct | File saved to `outputs/sprint-plans/` with sprint identifier |

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
| E8 | Acceptance criteria per item | Each sprint item has testable acceptance criteria |
| E9 | Sprint goal defined | Single sprint goal statement that captures the theme or outcome |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Dependencies identified | Cross-team dependencies listed with status: resolved, pending, at-risk |
| E11 | Velocity referenced | Past velocity or throughput data cited to calibrate commitment |
| E12 | Risks and unknowns flagged | Items with high uncertainty explicitly marked with mitigation plans |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
