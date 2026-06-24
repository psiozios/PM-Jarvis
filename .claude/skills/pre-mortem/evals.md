---
skill: pre-mortem
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /pre-mortem

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
| E1 | Pre-mortem structure | Contains: Scenario, Risk Categories, Likelihood/Impact Matrix, Mitigations sections |
| E2 | Output path correct | File saved to `outputs/pre-mortems/` with project and date in filename |
| E3 | Future tense framing | Risks framed as 'what could go wrong' scenarios, not current problems |

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
| E8 | Risks categorized | Risks organized by type: technical, organizational, market, execution |
| E9 | Likelihood and impact rated | Each risk has explicit likelihood (high/med/low) and impact rating |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Mitigations actionable | Each high-priority risk has a specific mitigation action, not 'monitor closely' |
| E11 | Trigger signals defined | Early warning signs identified for top risks — how would we know it's happening? |
| E12 | Owner per mitigation | Each mitigation action has a named owner and timeline |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
