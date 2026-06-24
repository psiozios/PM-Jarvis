---
skill: board-deck
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /board-deck

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
| E1 | Executive structure | Follows executive presentation flow: Summary → Metrics → Strategy → Ask |
| E2 | Slide-ready format | Each section is concise enough for a single slide — no section exceeds 5 bullet points |
| E3 | Output path correct | File saved to `outputs/presentations/` with date and audience in filename |

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
