---
skill: prd-review-panel
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /prd-review-panel

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
| E1 | All 7 perspectives present | Reviews from: Engineer, Designer, Executive, Legal, UX Researcher, Skeptic, Customer Voice |
| E2 | Distinct voice per reviewer | Each reviewer sounds different and focuses on their domain — no overlapping generic feedback |
| E3 | Synthesis section included | A final synthesis that reconciles conflicting feedback and prioritizes by severity |

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
| E8 | PRD sections cited | Each reviewer references specific PRD sections, not vague praise or criticism |
| E9 | Severity tagged | Findings categorized: Critical Blocker, Important Gap, Enhancement |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Conflicting perspectives flagged | When reviewers disagree, the conflict is explicitly surfaced |
| E11 | Action items extracted | Concrete action items pulled from across all reviews into a prioritized list |
| E12 | Sub-agents spawned in parallel | All 7 reviewers run as parallel sub-agents for clean independent review |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
