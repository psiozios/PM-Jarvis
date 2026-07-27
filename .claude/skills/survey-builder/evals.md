---
skill: survey-builder
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /survey-builder

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Survey structure logical | Questions flow from general to specific, grouped by topic |
| E2 | Research objective stated | Opens with what decision the survey data will inform |
| E3 | Output path correct | File saved to `outputs/research/` with topic in filename |

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
| E8 | Question types appropriate | Mix of question types (Likert, multiple choice, open-ended) matched to what each question needs to learn |
| E9 | Bias minimized | No double-barreled questions, no leading phrasing, response options balanced |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Survey length reasonable | Total estimated completion time stated and under 10 minutes |
| E11 | Analysis plan included | States how each question will be analyzed and what actionable thresholds look like |
| E12 | Sample requirements defined | Specifies target sample size, segments to include, and distribution method |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
