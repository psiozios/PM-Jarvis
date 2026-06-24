---
skill: prioritize
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /prioritize

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
| E1 | LNO framework applied | Tasks classified as Leverage, Neutral, or Overhead with clear reasoning |
| E2 | Priority order explicit | Final ranked list with the top priority clearly distinguished |
| E3 | Output path correct | File saved to `outputs/` with date in filename |

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
| E8 | Classification reasoning stated | Each task's L/N/O classification includes a 1-sentence justification |
| E9 | Strategic alignment checked | Priorities connected to current quarterly goals or OKRs |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Time estimates included | Each task has a rough time estimate to assess feasibility |
| E11 | Delegation opportunities flagged | Overhead or Neutral tasks that could be delegated are explicitly called out |
| E12 | What to drop is stated | Explicitly names what gets deprioritized or dropped, not just what to do |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
