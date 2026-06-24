---
skill: editing-assistant
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /editing-assistant

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
| E1 | Edit mode matched | Output matches the requested mode: tighten, restructure, tone-shift, or full rewrite |
| E2 | Changes tracked | Edits are visible — either tracked changes or before/after comparison |
| E3 | Original preserved | Original document referenced, not overwritten without confirmation |

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
| E8 | Edits preserve author voice | Changes maintain the user's writing style, not substitute a generic one |
| E9 | Rationale for major changes | Significant edits include a brief note on why the change improves the document |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Structural issues addressed | If restructuring, the new flow is justified with reasoning |
| E11 | Audience awareness applied | Edits calibrated to the document's target audience |
| E12 | House style applied | Edits conform to config/house-style.md rules if active |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
