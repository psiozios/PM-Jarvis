---
skill: survey-builder
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /survey-builder

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
| E1 | Survey structure logical | Questions flow from general to specific, grouped by topic |
| E2 | Research objective stated | Opens with what decision the survey data will inform |
| E3 | Output path correct | File saved to `outputs/research/` with topic in filename |

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
| E8 | Question types appropriate | Mix of question types (Likert, multiple choice, open-ended) matched to what each question needs to learn |
| E9 | Bias minimized | No double-barreled questions, no leading phrasing, response options balanced |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Survey length reasonable | Total estimated completion time stated and under 10 minutes |
| E11 | Analysis plan included | States how each question will be analyzed and what actionable thresholds look like |
| E12 | Sample requirements defined | Specifies target sample size, segments to include, and distribution method |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
