---
skill: stakeholder-tactics
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /stakeholder-tactics

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Stakeholder profiled | Contains communication style, priorities, known concerns, and influence level |
| E2 | Tactic is situation-specific | Advice tailored to the specific situation described, not generic stakeholder management |
| E3 | Output path correct | File saved to `outputs/` with stakeholder context and date |

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
| E8 | Specific talking points | Provides exact phrases or framings to use, not just 'be persuasive' |
| E9 | Counter-arguments anticipated | Predicts likely objections and provides responses for each |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Stakeholder profile referenced | Uses data from stakeholder profile in context-library if available |
| E11 | Timing recommendation | Suggests when and in what forum to have the conversation |
| E12 | Fallback strategy included | If the primary approach doesn't work, offers an alternative tactic |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
