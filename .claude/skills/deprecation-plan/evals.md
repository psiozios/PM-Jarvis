---
skill: deprecation-plan
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /deprecation-plan

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
| E1 | Deprecation phases defined | Plan includes: Announce → Migrate → Sunset → Remove phases with dates |
| E2 | Output path correct | File saved to `outputs/deprecation-plans/` with feature name in filename |
| E3 | User impact quantified | States how many users/accounts are affected and their migration options |

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
| E8 | Communication plan detailed | Specifies who gets notified, when, through which channels, with what messaging |
| E9 | Migration path clear | Step-by-step migration guide for affected users — not just 'switch to X' |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Rollback criteria defined | Conditions under which deprecation would be paused or reversed |
| E11 | Legal/compliance checked | Notes any contractual or compliance implications of removal |
| E12 | Success metrics for deprecation | Defines what 'done' looks like — migration rate target and timeline |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
