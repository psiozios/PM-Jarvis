---
skill: feature-request-analysis
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /feature-request-analysis

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
| E1 | Requests categorized | Feature requests organized into thematic categories, not listed individually |
| E2 | Volume and frequency shown | Each category shows: number of requests, unique requestors, time span |
| E3 | Output path correct | File saved to `outputs/analyses/` with date in filename |

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
| E8 | User segment attached | Each request category maps to specific user segments or personas |
| E9 | Underlying needs extracted | Identifies the 'why behind the ask' — the job-to-be-done, not just the feature requested |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Revenue or retention signal | Notes if requestors are high-value accounts, churned users, or prospects |
| E11 | Existing solution gaps noted | States whether current product partially addresses the need and where it falls short |
| E12 | Prioritization recommendation | Suggests priority order with reasoning tied to strategy, not just volume |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
