---
skill: action-sweep
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /action-sweep

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Reconciliation table format | Output has separate Proposed New Tasks, Verified-Done, and Drafts tables, not a mixed list |
| E2 | Window stated | Output header states the swept window (since date/timestamp) |
| E3 | Source cited per item | Every row names which source the item came from |

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
| E8 | Both-directions swept | Chat platform and email were swept for both inbound asks and the user's own outbound commitments, not inbound only |
| E9 | Verify-before-surfacing | Every verified-done item cites the specific source where resolution was found, not an assumption |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Dedupe against tracker | Every proposed new task was checked against currently open tracker items before being proposed as new |
| E11 | Execute-only-on-approval | No task was created and no item marked done before the reconciliation table was shown and approved |
| E12 | Outward-draft-only | Any item destined for someone other than the user is a draft, never an auto-sent message |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
