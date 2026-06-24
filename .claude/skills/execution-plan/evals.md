---
skill: execution-plan
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /execution-plan

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
| E1 | Phased structure | Work broken into sequential phases with clear entry/exit criteria per phase |
| E2 | Output path correct | File saved to `outputs/execution-plans/` with date and feature in filename |
| E3 | Timeline realistic | Dates or durations assigned to each phase with buffer for unknowns |

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
