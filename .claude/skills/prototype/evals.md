---
skill: prototype
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /prototype

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
| E1 | Working prototype delivered | Output is a functional prototype, not just a description or wireframe |
| E2 | Technology appropriate | Prototyping tool matches the need: HTML/CSS for web, Figma for design, code for interactive |
| E3 | Core flow covered | The primary user flow is fully interactive, not just the first screen |

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
| E8 | Real content used | Prototype uses realistic content and data, not lorem ipsum |
| E9 | Interaction patterns standard | UI patterns follow platform conventions (web, iOS, Android) |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Edge states shown | Empty states, error states, and loading states represented |
| E11 | Feedback points marked | Areas where user feedback is especially wanted are highlighted |
| E12 | Handoff notes included | Notes for developers on what's approximate vs what's exact in the prototype |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
