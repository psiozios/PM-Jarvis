---
skill: autoresearch
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /autoresearch

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
| E1 | Research loop documented | Shows the iterative research path: question → search → finding → next question |
| E2 | Sources cited per finding | Every finding attributes its source with URL or reference |
| E3 | Output path correct | File saved to `outputs/research/` with topic and date |

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
| E8 | Contradictions flagged | When sources disagree, both perspectives presented with assessment |
| E9 | Research question refined | Shows how the research question evolved as findings emerged |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Confidence rated per finding | Each finding rated: confirmed by multiple sources, single source, or inference |
| E11 | Gaps identified | States what couldn't be found and suggests alternative research approaches |
| E12 | Summary actionable | Final summary answers the original question with specific, usable information |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
