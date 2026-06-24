---
skill: napkin-sketch
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /napkin-sketch

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
| E1 | ASCII wireframe rendered | Clean ASCII wireframe with consistent box-drawing characters |
| E2 | Layout communicates hierarchy | Visual hierarchy (size, position, emphasis) matches the UX priority |
| E3 | Annotations included | Key elements labeled with their function or destination |

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
| E8 | Interactive elements marked | Buttons, links, and inputs clearly distinguishable from static content |
| E9 | Screen flow shown | If multi-screen, shows how screens connect with labeled transitions |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Responsive considerations noted | Notes how layout adapts for mobile/desktop if applicable |
| E11 | Data requirements visible | Dynamic data fields show what data populates each area |
| E12 | Browser capture option offered | Offers to render as HTML for cleaner visual if needed |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
