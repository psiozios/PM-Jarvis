---
skill: design-audit
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /design-audit

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Audit dimensions covered | Reviews: consistency, accessibility, usability, visual hierarchy, responsiveness |
| E2 | Severity-tagged findings | Each issue rated by severity: critical, major, minor, suggestion |
| E3 | Output path correct | File saved to `outputs/analyses/` with product area and date |

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
| E8 | Specific screenshots or elements cited | Each finding references a specific screen, component, or interaction |
| E9 | Accessibility standards referenced | WCAG or platform guidelines cited for accessibility findings |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Patterns vs one-offs distinguished | Systemic issues separated from one-off problems |
| E11 | Fix recommendations included | Each finding includes a specific fix suggestion |
| E12 | Positive patterns noted | Design strengths explicitly called out alongside issues |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
