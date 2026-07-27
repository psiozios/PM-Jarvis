---
skill: napkin-sketch
archetype: Code-Technical
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /napkin-sketch

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
