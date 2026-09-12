---
skill: prd-review-panel
archetype: Communication-Draft
eval-version: 2
last-updated: 2026-09-11
---

# Evals: /prd-review-panel

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language. **Spot-check the claims against the cited sources**; where a source cannot be reached, score N/A and name it rather than passing on plausibility |
| E8 | PRD sections cited | Each reviewer references specific PRD sections, not vague praise or criticism |
| E9 | Severity tagged | Findings categorized: Critical Blocker, Important Gap, Enhancement |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Conflicting perspectives flagged | When reviewers disagree, the conflict is explicitly surfaced |
| E11 | Action items extracted | Concrete action items pulled from across all reviews into a prioritized list |
| E12 | Sub-agents spawned in parallel | All 7 reviewers run as parallel sub-agents for clean independent review |
| E13 | Blockers confirmed against the PRD | Every Critical Blocker and Important Gap was verified by reading the PRD at the section it names, not accepted from a reviewer's report. FAIL on any blocker traceable only to an agent summary. See `references/capabilities.md` |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
