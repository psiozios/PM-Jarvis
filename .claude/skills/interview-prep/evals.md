---
skill: interview-prep
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /interview-prep

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Company research included | Contains company context: product, market, recent news, challenges |
| E2 | Role-specific prep | Preparation tailored to the specific PM role type (platform, growth, B2B, etc.) |
| E3 | Output path correct | File saved to `outputs/` with company and date in filename |

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
| E8 | Practice questions provided | At least 5 likely interview questions with suggested answer frameworks |
| E9 | STAR stories mapped | User's experience mapped to relevant stories for behavioral questions |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Product sense exercises included | At least 1 product critique or improvement exercise for the company's product |
| E11 | Questions to ask prepared | 3-5 thoughtful questions for the interviewer that demonstrate research |
| E12 | Weak spots identified | Honestly flags areas where the user's background may be challenged and how to address them |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
