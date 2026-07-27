---
skill: voice-of-customer
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /voice-of-customer

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Multi-source aggregation | Pulls from multiple feedback channels, not just one (support, reviews, interviews, surveys) |
| E2 | Themes quantified | Each theme includes volume: how many mentions, what percentage of total feedback |
| E3 | Output path correct | File saved to `outputs/research-synthesis/` with date in filename |

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
| E8 | Sentiment tracked | Each theme tagged with sentiment: positive, negative, mixed — with trend direction |
| E9 | Verbatim examples included | At least 1 verbatim customer quote per major theme |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Segment patterns noted | Identifies if certain themes cluster by user segment, plan, or tenure |
| E11 | Trend over time shown | Compares current themes to previous period where data available |
| E12 | Priority recommendations | Themes ranked by business impact, not just volume |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
