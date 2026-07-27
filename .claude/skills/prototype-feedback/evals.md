---
skill: prototype-feedback
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /prototype-feedback

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
