---
skill: daily-plan
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /daily-plan

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Time-blocked structure | Plan structured with time blocks, not just a bullet list of tasks |
| E2 | Priority framework applied | Top 3 priorities clearly ranked with reasoning tied to weekly/quarterly goals |
| E3 | Output path correct | File saved to `outputs/` with today's date in filename |

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
| E8 | Meeting context included | Each meeting has attendee names and 1-line context on what to prepare |
| E9 | Realistic capacity | Total planned work fits within available hours after meetings |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Calendar data used | MCP calendar data included, or graceful degradation noted if unavailable |
| E11 | Heads-up section present | Flags upcoming deadlines, risks, or stakeholder needs for the day |
| E12 | Cross-skill link offered | Suggests relevant next skill (e.g., /meeting-agenda for prep, /status-update if due) |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
