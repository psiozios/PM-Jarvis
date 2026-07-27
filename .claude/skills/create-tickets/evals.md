---
skill: create-tickets
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /create-tickets

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Ticket structure complete | Each ticket has: title, description, acceptance criteria, and size estimate |
| E2 | Acceptance criteria testable | Each acceptance criterion can be verified as done or not done — no ambiguity |
| E3 | Priority assigned | Each ticket has a priority level with brief justification |

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
| E8 | Dependencies noted | Cross-ticket dependencies explicitly listed with blocking/blocked relationships |
| E9 | Scope right-sized | Each ticket is completable in 1-3 days of work — large items broken down |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | PRD traceability | Each ticket traces back to a specific requirement or user story |
| E11 | Edge cases included | Non-obvious edge cases listed in the description or acceptance criteria |
| E12 | Output to correct system | Tickets created via Linear/Jira MCP or saved to `outputs/tickets/` as markdown |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
