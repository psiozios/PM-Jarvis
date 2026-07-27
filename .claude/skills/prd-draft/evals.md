---
skill: prd-draft
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /prd-draft

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Filename convention | File saved as `outputs/prds/[feature-kebab]-[stage].md` |
| E2 | Stage-appropriate length | Word count falls within stage guidance (Team Kickoff: 300-500, Engineering Handoff: 800-1500) |
| E3 | Required sections present | All sections mandated for the chosen PRD stage are present and non-empty |

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
| E8 | Testable hypothesis | Contains explicit 'If we... then... because...' with specific user behavior prediction |
| E9 | Metrics with baselines | Every success metric has current baseline, target number, and timeline — not just 'increase X' |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Non-goals with rationale | Each non-goal states WHY it's excluded, not just what it is |
| E11 | Kill criteria actionable | Kill criteria specify a threshold the team would act on, with a named owner |
| E12 | Open questions assigned | Every open question has a named stakeholder owner |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
