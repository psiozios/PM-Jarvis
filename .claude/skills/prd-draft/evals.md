---
skill: prd-draft
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /prd-draft

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
| E1 | Filename convention | File saved as `outputs/prds/[feature-kebab]-[stage].md` |
| E2 | Stage-appropriate length | Word count falls within stage guidance (Team Kickoff: 300-500, Engineering Handoff: 800-1500) |
| E3 | Required sections present | All sections mandated for the chosen PRD stage are present and non-empty |

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
