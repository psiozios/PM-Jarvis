---
skill: strategy-sprint
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /strategy-sprint

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
| E1 | Sprint duration matched | Workflow matches the chosen duration: 1 day, 1 week, or 1 month sprint |
| E2 | Phased deliverables clear | Each phase has a specific deliverable with definition of done |
| E3 | Output path correct | File saved to `outputs/strategy/` with sprint duration and date |

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
| E8 | Stakeholder input planned | Identifies who to consult and when during the sprint |
| E9 | Decision points scheduled | Key decision moments built into the sprint timeline |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Research vs synthesis balanced | Sprint allocates time for both gathering input and synthesizing output |
| E11 | Final deliverable defined | States exactly what artifact comes out of the sprint and for whom |
| E12 | Cross-skill integration | Links to specific skills needed at each phase (/competitor-analysis, /write-prod-strategy, etc.) |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
