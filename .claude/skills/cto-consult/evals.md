---
skill: cto-consult
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /cto-consult

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
| E1 | CTO voice authentic | Response sounds like a technical executive, not a generic advisor |
| E2 | Technical pushback specific | Objections reference specific technical constraints, not vague 'it's complex' |
| E3 | Output structured | Contains: Technical Assessment, Concerns, Alternative Approaches, Recommendation |

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
| E8 | Architecture implications noted | Identifies specific architectural impacts of the proposed feature |
| E9 | Effort estimate provided | Rough engineering effort estimate with what drives the complexity |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Trade-offs explicit | States what you gain and what you give up with each approach |
| E11 | Phasing suggested | If the ask is large, suggests a phased approach with the minimal viable slice |
| E12 | Questions for the PM | Asks clarifying questions that a real CTO would need answered |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
