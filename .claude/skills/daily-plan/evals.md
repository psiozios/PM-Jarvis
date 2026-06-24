---
skill: daily-plan
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /daily-plan

## How to Run (automatic on every skill invocation)

1. Original agent completes skill output and runs informal self-check
2. Original agent spawns a separate eval agent (clean context window)
3. Eval agent reads: this file, the skill output, `config/house-style.md`
4. Evaluates each criterion independently → PASS / FAIL / PARTIAL
5. FAILs returned to original agent for revision → re-eval loop
6. Zero FAILs achieved → log results below

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
| E4 | No AI slop | Zero instances of: delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Follows any active rules in `config/house-style.md` |
| E6 | Human-sounding | Varied sentence lengths, contractions used naturally, no formulaic paragraph openings |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | References specific data from context sources — not generic placeholder language |
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
