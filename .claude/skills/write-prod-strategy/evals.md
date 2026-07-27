---
skill: write-prod-strategy
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /write-prod-strategy

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | 7-component framework | All 7 strategy components present: Vision, Mission, Goals, Strategy, Tactics, Metrics, Roadmap (or skill-defined equivalent) |
| E2 | Output path correct | File saved to `outputs/strategy/` with descriptive filename |
| E3 | Time horizon stated | Strategy explicitly covers a defined time horizon (quarter, year, multi-year) |

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
| E8 | Market context included | References specific market data, competitor positions, or customer trends |
| E9 | Trade-offs explicit | States what the company will NOT do and why — not just what it will do |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Goals measurable | Every strategic goal has a quantifiable target and timeline |
| E11 | Resource implications noted | Identifies what teams, budget, or capabilities are needed |
| E12 | Alignment chain clear | Shows how this strategy connects to company-level objectives |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
