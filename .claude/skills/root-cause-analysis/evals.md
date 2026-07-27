---
skill: root-cause-analysis
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /root-cause-analysis

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | 5 Whys or Ishikawa applied | Uses a structured root cause framework, not just listing possible causes |
| E2 | Problem statement specific | Problem defined with: who's affected, what's happening, since when, how severe |
| E3 | Output path correct | File saved to `outputs/analyses/` with issue and date in filename |

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
| E8 | Root cause distinguished from symptoms | Clearly separates the root cause from the chain of symptoms |
| E9 | Evidence cited per hypothesis | Each possible cause has supporting or refuting evidence, not just speculation |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Contributing factors mapped | Shows the full causal chain, not just the final root cause |
| E11 | Fix addresses root, not symptom | Proposed solution targets the root cause, not a downstream symptom |
| E12 | Verification plan included | Describes how to confirm the fix actually resolved the issue |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
