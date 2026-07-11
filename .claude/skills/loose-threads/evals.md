---
skill: loose-threads
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /loose-threads

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
| E1 | Bucketed by age | Output grouped Fresh / This Week / Aging / Stale, not a flat list |
| E2 | Real deep link per item | Every flagged item links to the actual source thread/post |
| E3 | Proposed follow-ups separated | Follow-up proposals are a distinct table, not mixed into the bucket lists |

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
| E8 | Verify-before-flag | Every item carries a real `Checked:` line naming a cross-referenced source |
| E9 | Comprehensive-not-delta | The full sweep window was re-examined this run, not narrowed to new-since-last-run items |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Correct whose-court classification | Each item's court call is defensible from the thread content, not guessed |
| E11 | Propose-not-auto-create | No task was created in the tracker without an explicit confirmation step |
| E12 | Deduped against action-sweep | No item duplicates something already surfaced in `action-sweep`'s most recent output |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
