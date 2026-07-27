---
skill: sales-battlecard
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /sales-battlecard

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Battlecard format | Structured as: Overview, Key Differentiators, Objection Handling, Win Themes, Competitive Traps |
| E2 | Sales-ready language | Written in language sales reps can use directly with prospects — not PM jargon |
| E3 | Output path correct | File saved to `outputs/sales/` or `outputs/analyses/` with competitor name |

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
| E8 | Objection responses scripted | Each objection has a specific response script, not just talking points |
| E9 | Proof points included | Claims backed by specific customer wins, metrics, or third-party validation |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Competitor weaknesses actionable | Each competitor weakness maps to a specific question reps should ask prospects |
| E11 | Pricing comparison clear | Pricing positioning explained with specific scenarios (not just 'we're competitive') |
| E12 | Updated signals included | Notes what triggers a refresh: competitor launch, pricing change, feature release |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
