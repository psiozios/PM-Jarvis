---
skill: opportunity-sizing
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /opportunity-sizing

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
| E1 | TAM/SAM/SOM breakdown | Contains Total Addressable, Serviceable Addressable, and Serviceable Obtainable Market estimates |
| E2 | Top-down and bottom-up | Uses both top-down (market data) and bottom-up (unit economics) approaches |
| E3 | Output path correct | File saved to `outputs/analyses/` with market and date in filename |

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
| E8 | Market data sourced | Every market size claim cites a source with date — no unsourced round numbers |
| E9 | Growth rate included | Market growth rate estimated with basis (historical trend, analyst forecast, or assumption) |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Competitive share estimated | Acknowledges incumbent share and what % is realistically capturable |
| E11 | Timeline to penetration | Estimates time to reach SOM with quarterly or annual milestones |
| E12 | Key assumptions listed separately | Top 5 assumptions that drive the estimate isolated for easy challenge |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
