---
skill: sprint-planning
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /sprint-planning

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
| E1 | Sprint backlog structured | Items organized by priority with story points or size estimates |
| E2 | Capacity calculated | Team capacity computed based on headcount, time off, and meeting overhead |
| E3 | Output path correct | File saved to `outputs/sprint-plans/` with sprint identifier |

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
| E8 | Acceptance criteria per item | Each sprint item has testable acceptance criteria |
| E9 | Sprint goal defined | Single sprint goal statement that captures the theme or outcome |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Dependencies identified | Cross-team dependencies listed with status: resolved, pending, at-risk |
| E11 | Velocity referenced | Past velocity or throughput data cited to calibrate commitment |
| E12 | Risks and unknowns flagged | Items with high uncertainty explicitly marked with mitigation plans |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
