---
skill: example-board-groom
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /example-board-groom

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
| E1 | Checklist grouped by UI-click | Output grouped by action (close/reorder/re-allocate/tag/fix-description), not by card |
| E2 | Drafted text inline | Every text-based fix includes ready-to-paste replacement text, not just a note that it needs fixing |
| E3 | Deep link per card | Every flagged card links to the actual card, not a generic reference |

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
| E8 | Read-only honored | No evidence the skill wrote to, moved, or edited any card on the board itself |
| E9 | False-positive discipline | No card flagged solely for being long-lived or deliberately terse without a substantive reason given |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Live priority | Judgments reflect the board's current state at run time, not a cached or assumed prior ranking |
| E11 | Full board covered | Every card on the board was considered, not a sampled subset |
| E12 | Reasoning stated per item | Each flagged card states why it needs the proposed action, not just what action |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
