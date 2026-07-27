---
skill: execution-plan
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /execution-plan

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Phased structure | Work broken into sequential phases with clear entry/exit criteria per phase |
| E2 | Output path correct | File saved to `outputs/execution-plans/` with date and feature in filename |
| E3 | Timeline realistic | Dates or durations assigned to each phase with buffer for unknowns |

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
| E8 | Dependencies mapped | Cross-team and technical dependencies explicitly listed with owners |
| E9 | Milestones checkable | Each milestone is a binary yes/no — not 'mostly done' |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Risk mitigations included | Top 3 risks identified with specific mitigation actions |
| E11 | RACI or owners assigned | Every workstream has a named owner, not just 'the team' |
| E12 | Communication plan included | States when and how stakeholders will be updated on progress |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
