---
skill: competitor-analysis
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /competitor-analysis

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
| E1 | Comparison matrix present | Feature/capability comparison matrix with consistent dimensions across all competitors |
| E2 | Competitors profiled | Each competitor has: positioning, target market, pricing, key differentiators |
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
| E8 | Claims sourced | Every competitive claim cites a specific source (website, pricing page, review) with date |
| E9 | Strengths AND weaknesses for each | Each competitor has both strengths and weaknesses — not just threats |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Strategic implications drawn | Analysis leads to specific 'so what' for product strategy — not just information |
| E11 | Monitoring cadence suggested | Recommends what to track ongoing and how frequently to refresh the analysis |
| E12 | Blind spots acknowledged | States what information was unavailable and how it limits the analysis |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
