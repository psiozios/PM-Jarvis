---
skill: expansion-strategy
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /expansion-strategy

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
| E1 | Growth lever framework | Organized by expansion levers: upsell, cross-sell, seat expansion, usage expansion |
| E2 | Output path correct | File saved to `outputs/strategy/` or `outputs/analyses/` with date |
| E3 | Revenue model grounded | Strategy tied to actual pricing/packaging structure from business context |

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
| E8 | Segment-specific tactics | Different expansion tactics per customer segment, not one-size-fits-all |
| E9 | Trigger events identified | Specific user behaviors or milestones that signal expansion readiness |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Revenue impact estimated | Each expansion lever has a rough revenue impact estimate |
| E11 | Competitive context included | Notes how expansion pricing compares to competitive alternatives |
| E12 | Implementation sequenced | Tactics ordered by expected impact and implementation difficulty |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
