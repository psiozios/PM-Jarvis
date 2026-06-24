---
skill: stakeholder-tactics
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /stakeholder-tactics

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
| E1 | Stakeholder profiled | Contains communication style, priorities, known concerns, and influence level |
| E2 | Tactic is situation-specific | Advice tailored to the specific situation described, not generic stakeholder management |
| E3 | Output path correct | File saved to `outputs/` with stakeholder context and date |

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
| E8 | Specific talking points | Provides exact phrases or framings to use, not just 'be persuasive' |
| E9 | Counter-arguments anticipated | Predicts likely objections and provides responses for each |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Stakeholder profile referenced | Uses data from stakeholder profile in context-library if available |
| E11 | Timing recommendation | Suggests when and in what forum to have the conversation |
| E12 | Fallback strategy included | If the primary approach doesn't work, offers an alternative tactic |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
