---
skill: metrics-framework
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /metrics-framework

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Framework structure complete | Contains: North Star, Leading Indicators, Lagging Indicators, Health Metrics sections |
| E2 | Metric hierarchy clear | Shows how individual metrics ladder up to the North Star metric |
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
| E8 | Each metric operationally defined | Every metric has: name, formula, data source, owner, and review frequency |
| E9 | Input vs output metrics distinguished | Separates metrics the team can directly influence from outcome metrics |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Alert thresholds set | Key metrics have defined thresholds that trigger investigation |
| E11 | Metric relationships mapped | Shows which leading indicators predict which lagging outcomes |
| E12 | Gaming risks identified | For each key metric, notes how it could be gamed and the counter-metric |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
