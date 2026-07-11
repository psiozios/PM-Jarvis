---
skill: meeting-prep
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /meeting-prep

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
| E1 | Per-attendee sections | Every attendee has their own section, not a merged generic summary |
| E2 | All required sections present | Attendees, What's Current, Talking Points, Decisions to Push, Risks all present |
| E3 | Target meeting identified | Output header names the specific meeting and date/time it's prepping for |

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
