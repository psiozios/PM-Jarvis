---
skill: user-research-synthesis
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /user-research-synthesis

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Themes by pattern | Insights organized by behavioral pattern, not by interview chronology or question order |
| E2 | Sample described | States number of participants, segments, recruitment method, and interview dates |
| E3 | Output path correct | File saved to `outputs/research-synthesis/` with topic and date in filename |

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
| E8 | Verbatim quotes preserved | At least 2 verbatim participant quotes per theme — not paraphrased |
| E9 | Contradictions surfaced | Contradictory findings explicitly called out with participant counts on each side |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Confidence levels assigned | Each insight rated by evidence strength: strong (5+ participants), moderate (3-4), preliminary (1-2) |
| E11 | Gaps identified | Explicitly states what questions remain unanswered and what research would fill them |
| E12 | Actionable recommendations | Each theme maps to a specific product recommendation, not just 'consider this' |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
