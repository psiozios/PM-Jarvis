---
skill: journey-map
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /journey-map

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
| E1 | Journey stages defined | Contains sequential stages: Awareness → Consideration → Onboarding → Usage → Expansion/Churn |
| E2 | Touchpoints mapped | Each stage lists specific user touchpoints with the product |
| E3 | Output path correct | File saved to `outputs/analyses/` or `outputs/research/` with persona in filename |

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
| E8 | Emotions tracked | User emotional state (frustrated, satisfied, confused) noted at each stage |
| E9 | Pain points specific | Each pain point describes a concrete experience, not abstract friction |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Opportunities identified | Each stage has at least one improvement opportunity tied to a pain point |
| E11 | Persona-specific | Journey map reflects a specific persona's experience, not a generic user |
| E12 | Data sources cited | Journey informed by research data, support tickets, or analytics — not assumptions only |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
