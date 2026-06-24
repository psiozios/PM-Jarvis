---
skill: post-mortem
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /post-mortem

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
| E1 | Post-mortem template | Contains: Timeline, Impact, Root Cause, Contributing Factors, Action Items sections |
| E2 | Output path correct | File saved to `outputs/post-mortems/` with incident and date in filename |
| E3 | Blameless tone | Focuses on systems and processes, not individual blame — no finger-pointing language |

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
| E8 | Timeline specific | Incident timeline includes specific times, not just 'then we noticed' |
| E9 | Root cause distinguished from symptoms | Clearly separates the root cause from the symptoms and contributing factors |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Action items owned and dated | Every action item has a named owner, priority, and due date |
| E11 | Impact quantified | User impact stated in numbers: users affected, duration, revenue impact if applicable |
| E12 | Prevention measures concrete | States what systemic change prevents recurrence — not just 'be more careful' |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
