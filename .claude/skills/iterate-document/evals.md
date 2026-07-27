---
skill: iterate-document
archetype: Document-Writer
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /iterate-document

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Delta-style output | Output shows What Changed / Numeric Targets Validated / Delta Applied, not a full reprint of the doc |
| E2 | Target doc identified | Output header names the specific doc iterated |
| E3 | Doc's own structure honored | The applied delta matches the target doc's existing section conventions |

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
| E8 | Durability | Every restated numeric target is validated against `<METRICS_SOURCE>` before being asserted, with any discrepancy flagged rather than silently trusted. See `references/protocols/freshness-provenance.md`. |
| E9 | Surgical, not wholesale | Only sections affected by the new learning changed; unrelated content is untouched |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Fundamental-rewrite gate honored | If the change was large enough to require a full rewrite, that was proposed and confirmed, not applied silently |
| E11 | Applied to the source | The delta was applied directly to the source doc, not left as a separate untracked draft |
| E12 | Existing phrasing preserved where unaffected | Sections not touched by the update retain their original phrasing, not regenerated wording |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
