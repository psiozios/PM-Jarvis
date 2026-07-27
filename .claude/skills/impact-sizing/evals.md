---
skill: impact-sizing
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /impact-sizing

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
