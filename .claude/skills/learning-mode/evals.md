---
skill: learning-mode
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /learning-mode

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
| E1 | Level-appropriate depth | Content matches the selected level: beginner, intermediate, or advanced |
| E2 | Interactive structure | Includes practice exercises or reflection questions, not just explanation |
| E3 | PM-specific framing | Technical concepts explained through the lens of PM work, not generic CS |

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
| E8 | Real examples used | Concepts illustrated with real product or company examples, not abstract ones |
| E9 | Progressive complexity | Builds from simple to complex within the lesson |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Knowledge check included | At least one question or exercise to verify understanding |
| E11 | Practical application suggested | Suggests how to apply the learning in the user's current work |
| E12 | Next topic recommended | Suggests logical next learning topic based on what was covered |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
