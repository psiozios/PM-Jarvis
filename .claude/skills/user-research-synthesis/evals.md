---
skill: user-research-synthesis
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /user-research-synthesis

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
| E1 | Themes by pattern | Insights organized by behavioral pattern, not by interview chronology or question order |
| E2 | Sample described | States number of participants, segments, recruitment method, and interview dates |
| E3 | Output path correct | File saved to `outputs/research-synthesis/` with topic and date in filename |

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
| E8 | Verbatim quotes preserved | At least 2 verbatim participant quotes per theme — not paraphrased |
| E9 | Contradictions surfaced | Contradictory findings explicitly called out with participant counts on each side |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Confidence levels assigned | Each insight rated by evidence strength: strong (5+ participants), moderate (3-4), preliminary (1-2) |
| E11 | Gaps identified | Explicitly states what questions remain unanswered and what research would fill them |
| E12 | Actionable recommendations | Each theme maps to a specific product recommendation, not just 'consider this' |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
