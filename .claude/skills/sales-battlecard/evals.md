---
skill: sales-battlecard
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /sales-battlecard

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
| E1 | Battlecard format | Structured as: Overview, Key Differentiators, Objection Handling, Win Themes, Competitive Traps |
| E2 | Sales-ready language | Written in language sales reps can use directly with prospects — not PM jargon |
| E3 | Output path correct | File saved to `outputs/sales/` or `outputs/analyses/` with competitor name |

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
| E8 | Objection responses scripted | Each objection has a specific response script, not just talking points |
| E9 | Proof points included | Claims backed by specific customer wins, metrics, or third-party validation |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Competitor weaknesses actionable | Each competitor weakness maps to a specific question reps should ask prospects |
| E11 | Pricing comparison clear | Pricing positioning explained with specific scenarios (not just 'we're competitive') |
| E12 | Updated signals included | Notes what triggers a refresh: competitor launch, pricing change, feature release |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
