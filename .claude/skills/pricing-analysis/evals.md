---
skill: pricing-analysis
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /pricing-analysis

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Pricing framework applied | Uses a defined framework: value-based, competitive, cost-plus, or hybrid with rationale |
| E2 | Competitive pricing included | At least 3 competitor price points cited with feature comparison |
| E3 | Output path correct | File saved to `outputs/analyses/` with product and date in filename |

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
| E8 | Willingness-to-pay referenced | Cites WTP data or proposes how to gather it if unavailable |
| E9 | Revenue model math shown | Shows the math: price × volume × conversion = projected revenue |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Cannibalization risk assessed | If multiple tiers, addresses risk of customers downgrading |
| E11 | Price sensitivity factors listed | Identifies what would make customers more/less price sensitive |
| E12 | Implementation plan included | Specifies rollout approach: grandfather existing users? migration timeline? |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
