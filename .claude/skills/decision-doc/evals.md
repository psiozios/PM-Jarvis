---
skill: decision-doc
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /decision-doc

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
| E1 | Decision template structure | Contains: Context, Options Considered, Decision, Rationale, Consequences sections |
| E2 | Output path correct | File saved to `outputs/decisions/` with date-prefixed filename |
| E3 | Options compared fairly | At least 2 options presented with pros/cons for each — not just the chosen option |

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
| E8 | Reversibility stated | Explicitly states whether the decision is reversible or irreversible and the cost of reversal |
| E9 | Stakeholder input documented | Names who was consulted and what they recommended |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Dissent captured | If disagreement existed, it's documented with the dissenter's reasoning |
| E11 | Review date set | Includes a specific date or trigger for revisiting the decision |
| E12 | Consequences specific | Lists concrete downstream effects, not vague 'this will impact the team' |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
