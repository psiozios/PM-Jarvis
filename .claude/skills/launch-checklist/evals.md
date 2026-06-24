---
skill: launch-checklist
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /launch-checklist

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
| E1 | Checklist format | Items are checkable (done/not done) organized by category: Engineering, Product, Marketing, Support, Legal |
| E2 | Output path correct | File saved to `outputs/launches/` with feature and date in filename |
| E3 | Pre/post launch separated | Clear division between pre-launch gates and post-launch monitoring items |

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
| E8 | Rollback plan included | Specific steps for rolling back if launch goes wrong, with trigger criteria |
| E9 | Monitoring defined | Lists specific metrics to watch post-launch with alert thresholds |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Go/no-go criteria explicit | Binary launch decision criteria — not ambiguous 'should be ready' |
| E11 | Stakeholder sign-offs listed | Names who must approve before launch, with their specific gate |
| E12 | Post-launch review scheduled | Date set for launch retrospective and metrics review |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
