---
skill: launch-checklist
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /launch-checklist

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
