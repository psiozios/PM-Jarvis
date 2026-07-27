---
skill: board-deck
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /board-deck

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Executive structure | Follows executive presentation flow: Summary → Metrics → Strategy → Ask |
| E2 | Slide-ready format | Each section is concise enough for a single slide — no section exceeds 5 bullet points |
| E3 | Output path correct | File saved to `outputs/presentations/` with date and audience in filename |

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
| E8 | Metrics with trend | Every metric includes current value, trend direction, and comparison period |
| E9 | Strategic narrative coherent | Story arc connects metrics → insight → action in a logical flow |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Ask is specific | If requesting resources or decisions, the ask is quantified and time-bound |
| E11 | Risk section balanced | Risks presented alongside mitigations — not just a list of problems |
| E12 | Appendix referenced | Supporting detail pushed to appendix, not crammed into main sections |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
