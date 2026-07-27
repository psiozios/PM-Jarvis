---
skill: expansion-strategy
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /expansion-strategy

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Growth lever framework | Organized by expansion levers: upsell, cross-sell, seat expansion, usage expansion |
| E2 | Output path correct | File saved to `outputs/strategy/` or `outputs/analyses/` with date |
| E3 | Revenue model grounded | Strategy tied to actual pricing/packaging structure from business context |

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
| E8 | Segment-specific tactics | Different expansion tactics per customer segment, not one-size-fits-all |
| E9 | Trigger events identified | Specific user behaviors or milestones that signal expansion readiness |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Revenue impact estimated | Each expansion lever has a rough revenue impact estimate |
| E11 | Competitive context included | Notes how expansion pricing compares to competitive alternatives |
| E12 | Implementation sequenced | Tactics ordered by expected impact and implementation difficulty |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
