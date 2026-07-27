---
skill: okr-planning
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /okr-planning

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | OKR format correct | Each Objective has 2-5 Key Results; Key Results are measurable outcomes not tasks |
| E2 | Output path correct | File saved to `outputs/okrs/` with quarter and year in filename |
| E3 | Alignment shown | Each OKR traces to a company or team-level objective |

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
| E8 | Key Results quantified | Every Key Result has a specific number: baseline → target |
| E9 | Ambition calibrated | Mix of committed (70%+ confidence) and aspirational (30-50% confidence) KRs noted |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Anti-metrics included | At least one counter-metric per Objective to prevent gaming |
| E11 | Owner per KR | Each Key Result has a single named owner |
| E12 | Review cadence set | Specifies check-in frequency (weekly, bi-weekly) and scoring method |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
