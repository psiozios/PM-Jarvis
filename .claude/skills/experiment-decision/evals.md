---
skill: experiment-decision
archetype: Analysis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /experiment-decision

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Ship-or-test decision clear | Explicitly recommends: A/B test, phased rollout, or just ship — with reasoning |
| E2 | Decision framework applied | Uses a structured framework (reversibility, blast radius, confidence) not just gut feel |
| E3 | Output path correct | File saved to `outputs/analyses/` or `outputs/decisions/` with date |

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
| E8 | Risk assessment specific | Quantifies downside risk: what happens if the change is wrong? |
| E9 | Cost of testing vs shipping | Compares the cost of running an experiment (time, complexity) vs shipping directly |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Confidence level stated | Rates pre-experiment confidence in the hypothesis (high/medium/low) with reasoning |
| E11 | Past precedent referenced | Cites similar past decisions or experiments for calibration |
| E12 | Recommendation is binary | Final recommendation is a clear action, not 'it depends' or 'consider testing' |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
