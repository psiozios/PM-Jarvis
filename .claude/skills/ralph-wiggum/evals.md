---
skill: ralph-wiggum
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /ralph-wiggum

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Devil's advocate framing | Criticism is delivered in the skill's distinctive irreverent voice |
| E2 | Real issues found | Identifies genuine weaknesses, not manufactured objections |
| E3 | Feedback is specific | Each criticism points to a specific section or claim, not vague complaints |

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
| E8 | Assumptions challenged | Calls out at least 2 unstated assumptions in the document |
| E9 | Alternative perspectives offered | For each criticism, suggests what would make it stronger |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Severity distinguished | Separates fatal flaws from nice-to-fix issues |
| E11 | Constructive underneath the humor | Every humorous jab contains an actionable improvement suggestion |
| E12 | Document scope respected | Critiques the document for what it is, not what it isn't (e.g., doesn't fault a PRD Lite for lacking detail) |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
