---
skill: feature-request-analysis
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /feature-request-analysis

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Requests categorized | Feature requests organized into thematic categories, not listed individually |
| E2 | Volume and frequency shown | Each category shows: number of requests, unique requestors, time span |
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
| E8 | User segment attached | Each request category maps to specific user segments or personas |
| E9 | Underlying needs extracted | Identifies the 'why behind the ask' — the job-to-be-done, not just the feature requested |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Revenue or retention signal | Notes if requestors are high-value accounts, churned users, or prospects |
| E11 | Existing solution gaps noted | States whether current product partially addresses the need and where it falls short |
| E12 | Prioritization recommendation | Suggests priority order with reasoning tied to strategy, not just volume |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
