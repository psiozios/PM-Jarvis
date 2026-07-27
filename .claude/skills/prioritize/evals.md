---
skill: prioritize
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /prioritize

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | LNO framework applied | Tasks classified as Leverage, Neutral, or Overhead with clear reasoning |
| E2 | Priority order explicit | Final ranked list with the top priority clearly distinguished |
| E3 | Output path correct | File saved to `outputs/` with date in filename |

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
| E8 | Classification reasoning stated | Each task's L/N/O classification includes a 1-sentence justification |
| E9 | Strategic alignment checked | Priorities connected to current quarterly goals or OKRs |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Time estimates included | Each task has a rough time estimate to assess feasibility |
| E11 | Delegation opportunities flagged | Overhead or Neutral tasks that could be delegated are explicitly called out |
| E12 | What to drop is stated | Explicitly names what gets deprioritized or dropped, not just what to do |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
