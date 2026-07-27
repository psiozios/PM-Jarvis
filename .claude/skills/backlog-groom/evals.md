---
skill: backlog-groom
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /backlog-groom

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Checklist grouped by UI-click | Output grouped by action (Close/Reorder/Re-allocate/Tag/Description-fix), not by item |
| E2 | Drafted text inline | Every text-based fix includes ready-to-paste replacement text |
| E3 | Deep link per item | Every flagged item links to the actual tracker item |

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
| E8 | Read-only honored | No evidence the skill wrote to, moved, closed, or edited any item on the board itself |
| E9 | False-positive discipline | No item flagged solely for being long-lived, terse, or similar-sounding without a substantive reason given |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Live priority | Judgments reflect the board's current state at run time, not a cached or assumed ranking |
| E11 | Full board covered | All triage dimensions (stale, duplicate, ready-to-close, mis-prioritized, wrong-sprint, orphan, thin epic, thin description) were checked across the whole board, not a sampled subset |
| E12 | Reasoning stated per item | Each flagged item states why it needs the proposed action, not just what action |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
