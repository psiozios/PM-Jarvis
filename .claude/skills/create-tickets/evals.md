---
skill: create-tickets
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /create-tickets

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
| E1 | Ticket structure complete | Each ticket has: title, description, acceptance criteria, and size estimate |
| E2 | Acceptance criteria testable | Each acceptance criterion can be verified as done or not done — no ambiguity |
| E3 | Priority assigned | Each ticket has a priority level with brief justification |

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
