---
skill: write-prod-strategy
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /write-prod-strategy

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
| E1 | 7-component framework | All 7 strategy components present: Vision, Mission, Goals, Strategy, Tactics, Metrics, Roadmap (or skill-defined equivalent) |
| E2 | Output path correct | File saved to `outputs/strategy/` with descriptive filename |
| E3 | Time horizon stated | Strategy explicitly covers a defined time horizon (quarter, year, multi-year) |

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
| E8 | Market context included | References specific market data, competitor positions, or customer trends |
| E9 | Trade-offs explicit | States what the company will NOT do and why — not just what it will do |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Goals measurable | Every strategic goal has a quantifiable target and timeline |
| E11 | Resource implications noted | Identifies what teams, budget, or capabilities are needed |
| E12 | Alignment chain clear | Shows how this strategy connects to company-level objectives |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
