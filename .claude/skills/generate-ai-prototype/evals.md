---
skill: generate-ai-prototype
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /generate-ai-prototype

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
| E1 | Platform-specific prompt | Prompt tailored to the target platform: v0.dev, Lovable, or Bolt.new |
| E2 | Requirements translated | PRD requirements translated into prompt-friendly instructions |
| E3 | Output path correct | Prompt saved to `outputs/prototypes/` with platform and feature name |

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
| E8 | UI components specified | Key UI components and layout described specifically enough for generation |
| E9 | Interaction flows described | User interactions described step-by-step, not just static layouts |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Design constraints included | Brand colors, typography, or design system constraints included in prompt |
| E11 | Iteration guidance included | Suggests follow-up prompts for refining the generated output |
| E12 | Expected output described | States what the generated prototype should look like and do |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
