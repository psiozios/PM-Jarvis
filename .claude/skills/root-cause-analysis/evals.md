---
skill: root-cause-analysis
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /root-cause-analysis

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
| E1 | 5 Whys or Ishikawa applied | Uses a structured root cause framework, not just listing possible causes |
| E2 | Problem statement specific | Problem defined with: who's affected, what's happening, since when, how severe |
| E3 | Output path correct | File saved to `outputs/analyses/` with issue and date in filename |

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
| E8 | Root cause distinguished from symptoms | Clearly separates the root cause from the chain of symptoms |
| E9 | Evidence cited per hypothesis | Each possible cause has supporting or refuting evidence, not just speculation |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Contributing factors mapped | Shows the full causal chain, not just the final root cause |
| E11 | Fix addresses root, not symptom | Proposed solution targets the root cause, not a downstream symptom |
| E12 | Verification plan included | Describes how to confirm the fix actually resolved the issue |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
