---
skill: prototype
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /prototype

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
