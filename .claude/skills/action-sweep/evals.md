---
skill: action-sweep
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /action-sweep

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
| E1 | Reconciliation table format | Output has separate Proposed New Tasks, Verified-Done, and Drafts tables, not a mixed list |
| E2 | Window stated | Output header states the swept window (since date/timestamp) |
| E3 | Source cited per item | Every row names which source the item came from |

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
