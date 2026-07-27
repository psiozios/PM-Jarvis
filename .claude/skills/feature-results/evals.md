---
skill: feature-results
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /feature-results

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Results template followed | Contains: Hypothesis Recap, Results, Analysis, Learnings, Next Steps sections |
| E2 | Pre/post comparison | Shows metrics before and after launch with the same measurement methodology |
| E3 | Output path correct | File saved to `outputs/analyses/` with feature and date in filename |

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
| E8 | Hypothesis verdict explicit | States clearly: confirmed, partially confirmed, or rejected — with evidence |
| E9 | Unintended effects noted | Documents any unexpected positive or negative side effects observed |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Statistical confidence noted | States whether sample size is sufficient and if results are statistically significant |
| E11 | Goal vs actual compared | Every pre-launch metric target compared against actual result |
| E12 | Next steps concrete | States: iterate, scale, pivot, or kill — with specific reasoning |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
