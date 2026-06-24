---
skill: impact-sizing
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /impact-sizing

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
| E1 | Driver tree present | Contains a driver tree with labeled nodes showing how feature maps to business metric |
| E2 | 4-step framework followed | Covers: Addressable Users → Adoption Rate → Behavior Change → Business Impact |
| E3 | Output path correct | File saved to `outputs/analyses/` with feature name and date in filename |

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
| E8 | Confidence levels on assumptions | Every assumption has an explicit confidence level (high/medium/low) with reasoning |
| E9 | Sensitivity analysis present | Shows how the estimate changes when top 2-3 assumptions are wrong by 2x |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Range not point estimate | Final impact is a range (conservative/expected/optimistic), not a single number |
| E11 | Comparable precedent cited | References at least one similar feature or industry benchmark for calibration |
| E12 | De-risk actions specific | Lists concrete actions to validate the highest-uncertainty assumptions |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
