---
skill: post-mortem
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /post-mortem

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Post-mortem template | Contains: Timeline, Impact, Root Cause, Contributing Factors, Action Items sections |
| E2 | Output path correct | File saved to `outputs/post-mortems/` with incident and date in filename |
| E3 | Blameless tone | Focuses on systems and processes, not individual blame — no finger-pointing language |

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
| E8 | Timeline specific | Incident timeline includes specific times, not just 'then we noticed' |
| E9 | Root cause distinguished from symptoms | Clearly separates the root cause from the symptoms and contributing factors |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Action items owned and dated | Every action item has a named owner, priority, and due date |
| E11 | Impact quantified | User impact stated in numbers: users affected, duration, revenue impact if applicable |
| E12 | Prevention measures concrete | States what systemic change prevents recurrence — not just 'be more careful' |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
