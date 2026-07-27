---
skill: win-loss-analysis
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /win-loss-analysis

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Win/loss structure | Organized by: Win Patterns, Loss Patterns, Competitive Dynamics, Recommendations |
| E2 | Sample described | States number of deals analyzed, time period, and any selection criteria |
| E3 | Output path correct | File saved to `outputs/analyses/` with date in filename |

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
| E8 | Quotes preserved | Includes verbatim quotes from sales reps or customers for key patterns |
| E9 | Win/loss reasons quantified | Top reasons ranked by frequency with counts, not just listed |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Competitor-specific patterns | Each major competitor has specific win/loss patterns, not generic |
| E11 | Product gaps vs sales gaps | Distinguishes between product capability gaps and sales execution gaps |
| E12 | Actionable recommendations | Each recommendation maps to a specific win/loss pattern and has a proposed owner |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
