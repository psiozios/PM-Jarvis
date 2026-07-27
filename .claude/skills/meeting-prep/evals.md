---
skill: meeting-prep
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /meeting-prep

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Per-attendee sections | Every attendee has their own section, not a merged generic summary |
| E2 | All required sections present | Attendees, What's Current, Talking Points, Decisions to Push, Risks all present |
| E3 | Target meeting identified | Output header names the specific meeting and date/time it's prepping for |

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
| E8 | Never a blank agenda | Talking points, decisions, and risks are substantive and specific, not generic filler ("discuss project status") |
| E9 | Recent-call mining evidenced | Output shows evidence that shared calls, not only 1:1 history, were checked |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Priorities tied in | At least one talking point connects to a currently active priority, not just the meeting's stated topic |
| E11 | Honest about gaps | Where context genuinely doesn't exist for a section, that's stated explicitly rather than padded |
| E12 | Cross-skill link offered | Suggests `meeting-agenda` or `meeting-notes` as the natural next step |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
