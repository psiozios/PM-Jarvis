---
skill: prototype-feedback
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /prototype-feedback

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
| E1 | Build-review-iterate structure | Follows the full loop: current state → feedback → changes → next iteration |
| E2 | Feedback actionable | Each feedback item is specific enough to implement, not vague |
| E3 | Screenshot or reference used | Feedback references specific screens or elements in the prototype |

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
| E8 | Usability issues prioritized | Issues ranked by user impact: critical flow blockers vs polish items |
| E9 | User perspective centered | Feedback framed from the user's perspective, not developer convenience |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Positive patterns noted | What's working well is explicitly called out to preserve in iterations |
| E11 | Iteration scope defined | Specific changes for the next iteration are scoped and prioritized |
| E12 | Testing suggestions included | Suggests what to test with users and what questions to ask |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
