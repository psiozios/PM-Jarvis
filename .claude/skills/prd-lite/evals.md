---
skill: prd-lite
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /prd-lite

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
| E1 | Lightweight format | Output is 1 page or less — no full PRD structure, just the essential sections |
| E2 | Problem-first framing | Opens with the user problem and current cost, not the solution |
| E3 | Output path correct | File saved to `outputs/prds/` with appropriate naming |

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
| E8 | Specific user segment | Names the specific user segment affected with approximate count or percentage |
| E9 | Success criteria measurable | At least 2 success criteria that are quantifiable and time-bound |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Scope boundaries clear | What's in and what's out are explicitly stated |
| E11 | Next steps defined | Clear next actions with owners listed |
| E12 | Cross-skill link offered | Suggests logical next skill (e.g., /prd-draft for full spec, /impact-sizing for sizing) |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
