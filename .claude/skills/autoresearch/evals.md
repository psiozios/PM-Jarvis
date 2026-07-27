---
skill: autoresearch
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /autoresearch

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
