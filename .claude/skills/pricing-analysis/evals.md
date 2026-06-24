---
skill: pricing-analysis
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /pricing-analysis

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
| E1 | Pricing framework applied | Uses a defined framework: value-based, competitive, cost-plus, or hybrid with rationale |
| E2 | Competitive pricing included | At least 3 competitor price points cited with feature comparison |
| E3 | Output path correct | File saved to `outputs/analyses/` with product and date in filename |

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
| E8 | Willingness-to-pay referenced | Cites WTP data or proposes how to gather it if unavailable |
| E9 | Revenue model math shown | Shows the math: price × volume × conversion = projected revenue |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Cannibalization risk assessed | If multiple tiers, addresses risk of customers downgrading |
| E11 | Price sensitivity factors listed | Identifies what would make customers more/less price sensitive |
| E12 | Implementation plan included | Specifies rollout approach: grandfather existing users? migration timeline? |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
