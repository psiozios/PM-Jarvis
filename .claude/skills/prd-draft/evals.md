---
skill: prd-draft
archetype: Document-Writer
eval-version: 4
last-updated: 2026-10-30
---

# Evals: /prd-draft

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Filename convention | File saved as `outputs/prds/[feature-kebab]-[stage].md` |
| E2 | Stage-appropriate length | Body word count, appendix excluded, against the stage target in the SKILL's length table: up to 250 words over the top of the range is PASS, 251-500 over is PARTIAL, more is FAIL. FAIL as well if the user's own text was cut to hit the number |
| E3 | Themes, in order, every stage | Overview, Problem (hypothesis, current implementation gaps), Business metrics and goals, Legal compliance and risk constraints, Solution (approach, high-level design), Rollout plan, Open questions, collapsible Appendix with the design-decisions table. No section named for a team. Business metrics and constraints present at every stage, as "None identified" plus what was checked where empty |

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
| E8 | Testable hypothesis | Contains explicit 'If we... then... because...' with specific user behavior prediction |
| E9 | Metrics with baselines | Every success metric has current baseline, target number, and timeline — not just 'increase X' |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | "What it is not" with rationale | Each non-goal in the Overview states WHY it's excluded, not just what it is |
| E11 | Kill criteria actionable | Kill criteria specify a threshold the team would act on, with a named owner. In `--retro` mode this is N/A, never PASS: the review trigger is scored under E19 |
| E12 | Open questions assigned | Every open question has a named stakeholder owner |

### Category 5: Graded Evidence

| ID | Check | Criteria |
|----|-------|----------|
| E13 | Code read before drafting | With a codebase connected, Current implementation gaps names the file or function each gap was read from, graded "inferred from the code" with its confirming engineer in Open questions. N/A with the reason where no codebase is connected |
| E14 | Why now is external | Why now cites a market, competitor, regulation, or client-research source. FAIL where it rests on an internal metric, which belongs under Business metrics and goals |
| E15 | Versions and comments | Every contract, policy, or spec cited names its version, and the run shows its comments were read, resolved ones included |
| E16 | Summaries keep the grade | No overview, TL;DR, or announcement line states as fact what its section grades as inferred, estimated, or unsourced, and none speaks in the first person for the user |

### Category 6: Retro Mode (N/A unless the run is `--retro`)

| ID | Check | Criteria |
|----|-------|----------|
| E17 | Intent from the user | Intended behavior is attributed to the user and was asked before the sources were read; none of it is reconstructed from the code |
| E18 | Four-way cross-check | Each behavior is read against code, contract (with version), sales and ops material (with dates), and ticket acceptance criteria. Every disagreement is a gap with its sources on each side and an owner in Open questions |
| E19 | Retro shape | Past tense, no rollout plan section, a review trigger with a threshold and an owner in place of kill criteria, every status claim dated or linked live |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
