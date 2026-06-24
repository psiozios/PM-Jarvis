---
skill: interview-feedback
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /interview-feedback

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
| E1 | Structured debrief format | Contains: Performance Assessment, Strengths, Areas for Improvement, Next Steps |
| E2 | Evidence-based feedback | Each assessment point references a specific interview moment, not general impressions |
| E3 | Output path correct | File saved to `outputs/` with interview type and date in filename |

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
| E8 | Behavioral examples cited | Strengths and weaknesses illustrated with what was actually said or done |
| E9 | Improvement actions specific | Each improvement area has a concrete practice action, not just 'do better at X' |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Framework-aware | Evaluates against the framework relevant to the interview type (PM, case, behavioral) |
| E11 | Scoring or rating included | Provides a rating or score on key dimensions for tracking improvement over time |
| E12 | Comparison to target level | Calibrates performance against the expected level for the target role/company |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
