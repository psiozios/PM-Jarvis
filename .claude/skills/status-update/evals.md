---
skill: status-update
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /status-update

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Status template structure | Contains Progress / Blockers / Next Steps sections |
| E2 | Audience-appropriate depth | Depth matches the stated audience (exec summary vs team detail) |
| E3 | Output path correct | File saved to `outputs/status-updates/` with date-prefixed filename |

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
| E8 | Blockers have owners | Every blocker names a responsible person and proposed resolution path |
| E9 | Progress quantified | Progress described with numbers or percentages, not just 'making good progress' |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Timeline referenced | Current status compared against original timeline or milestones |
| E11 | Risks flagged proactively | At least one forward-looking risk or dependency called out |
| E12 | Ask is explicit | If help is needed, the specific ask and from whom is clearly stated |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
