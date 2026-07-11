---
skill: weekly-readahead
archetype: Document-Writer
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /weekly-readahead

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
| E1 | Configured sections used | Output uses the section set configured for this specific meeting, not a generic default |
| E2 | Meeting and week identified | Output header names the target meeting and the week it covers |
| E3 | Consistent with prior read-aheads | Format matches the previously published read-ahead for this meeting, if one exists |

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
