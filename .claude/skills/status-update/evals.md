---
skill: status-update
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /status-update

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
| E1 | Status template structure | Contains Progress / Blockers / Next Steps sections |
| E2 | Audience-appropriate depth | Depth matches the stated audience (exec summary vs team detail) |
| E3 | Output path correct | File saved to `outputs/status-updates/` with date-prefixed filename |

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
