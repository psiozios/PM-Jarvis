---
skill: retention-analysis
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /retention-analysis

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Cohort table present | Contains a cohort retention table with clearly labeled time periods and percentages |
| E2 | Methodology stated | Analysis method described: which cohort definition, time window, and metric used |
| E3 | Output path correct | File saved to `outputs/analyses/` with date in filename |

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
| E8 | Benchmark comparison | Retention curves compared against at least one benchmark (industry, prior cohort, or target) |
| E9 | Drop-off points identified | Specific time periods where retention drops most sharply are called out with hypotheses |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Segment breakdown included | Retention analyzed by at least 2 user segments (e.g., plan type, acquisition channel) |
| E11 | Recommendations tied to data | Each recommendation directly references a specific data pattern in the analysis |
| E12 | Leading indicators suggested | Proposes early signals that predict long-term retention for monitoring |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
