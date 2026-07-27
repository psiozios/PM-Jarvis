---
skill: weekly-readahead
archetype: Document-Writer
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /weekly-readahead

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Configured sections used | Output uses the section set configured for this specific meeting, not a generic default |
| E2 | Meeting and week identified | Output header names the target meeting and the week it covers |
| E3 | Consistent with prior read-aheads | Format matches the previously published read-ahead for this meeting, if one exists |

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
| E8 | Durability | No point-in-time status is asserted as a standing fact without a date; metric values state their as-of date. See `references/protocols/freshness-provenance.md`. |
| E9 | So-what per section | Every section leads with why it matters, not a bare activity list |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | All configured sections filled | No configured section is silently dropped for lack of content — a true no-update section says so explicitly |
| E11 | Publish-on-confirm honored | No evidence the read-ahead was published to the docs hub before the draft was confirmed |
| E12 | Specificity throughout | Numbers, names, and dates are used instead of vague summary language |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
