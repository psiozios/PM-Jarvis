---
skill: user-interview
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /user-interview

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
| E1 | Interview processed completely | All provided interview data transformed — no sections skipped or summarized away |
| E2 | JTBD format used | Insights framed as Jobs-to-be-Done where applicable: 'When [situation], I want to [motivation], so I can [outcome]' |
| E3 | Output path correct | File saved to `outputs/research/` or `outputs/research-synthesis/` with participant and date |

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
| E8 | Direct quotes extracted | Key participant quotes pulled verbatim with context for how they arose |
| E9 | Surprises highlighted | Unexpected findings or moments that contradicted assumptions explicitly flagged |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Behavioral observations separated from opinions | Distinguishes what participants DID from what they SAID they'd do |
| E11 | Follow-up questions suggested | Proposes 2-3 questions for the next interview based on gaps found |
| E12 | Pattern connections noted | Links findings to patterns from previous interviews or research if available |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
