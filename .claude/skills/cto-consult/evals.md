---
skill: cto-consult
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /cto-consult

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | CTO voice authentic | Response sounds like a technical executive, not a generic advisor |
| E2 | Technical pushback specific | Objections reference specific technical constraints, not vague 'it's complex' |
| E3 | Output structured | Contains: Technical Assessment, Concerns, Alternative Approaches, Recommendation |

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
| E8 | Architecture implications noted | Identifies specific architectural impacts of the proposed feature |
| E9 | Effort estimate provided | Rough engineering effort estimate with what drives the complexity |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Trade-offs explicit | States what you gain and what you give up with each approach |
| E11 | Phasing suggested | If the ask is large, suggests a phased approach with the minimal viable slice |
| E12 | Questions for the PM | Asks clarifying questions that a real CTO would need answered |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
