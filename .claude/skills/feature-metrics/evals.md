---
skill: feature-metrics
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /feature-metrics

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | STEDII framework applied | Uses the STEDII framework for metric selection |
| E2 | Leading and lagging separated | Clearly distinguishes leading indicators from lagging outcomes |
| E3 | Output path correct | File saved to `outputs/analyses/` with feature name in filename |

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
| E8 | Each metric has measurement plan | Every metric specifies: data source, calculation method, and reporting frequency |
| E9 | Targets with timelines | Every metric has a baseline, target, and timeline — not just 'improve X' |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Counter-metrics included | At least one metric that guards against unintended consequences |
| E11 | Dashboard-ready format | Metrics organized in a format that could be directly implemented in a dashboard |
| E12 | Review cadence defined | States when metrics will be reviewed and what triggers a deeper investigation |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
