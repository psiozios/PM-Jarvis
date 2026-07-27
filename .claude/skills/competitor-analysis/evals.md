---
skill: competitor-analysis
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /competitor-analysis

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Comparison matrix present | Feature/capability comparison matrix with consistent dimensions across all competitors |
| E2 | Competitors profiled | Each competitor has: positioning, target market, pricing, key differentiators |
| E3 | Output path correct | File saved to `outputs/analyses/` with market and date in filename |

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
| E8 | Claims sourced | Every competitive claim cites a specific source (website, pricing page, review) with date |
| E9 | Strengths AND weaknesses for each | Each competitor has both strengths and weaknesses — not just threats |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Strategic implications drawn | Analysis leads to specific 'so what' for product strategy — not just information |
| E11 | Monitoring cadence suggested | Recommends what to track ongoing and how frequently to refresh the analysis |
| E12 | Blind spots acknowledged | States what information was unavailable and how it limits the analysis |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
