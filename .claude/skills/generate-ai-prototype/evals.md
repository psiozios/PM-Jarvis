---
skill: generate-ai-prototype
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /generate-ai-prototype

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
