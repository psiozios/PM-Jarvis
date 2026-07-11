---
skill: sync-doc
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /sync-doc

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
| E1 | Four-section output | Substantive Changes, Local-Only Context Preserved, Conflicts, and Ignored sections all present (Ignored may be a one-liner if empty) |
| E2 | Target file identified | Output header names the local file being synced |
| E3 | Confirmation gate visible | Output makes clear nothing is applied until confirmed |

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
| E8 | Formatting-noise correctly excluded | No formatting-only difference (whitespace, list markers, heading style) appears in the Substantive Changes list |
| E9 | Local-only content preserved | Content present locally but absent externally is explicitly called out as preserved, not silently dropped |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Conflicts flagged, not resolved silently | Any genuinely ambiguous conflicting fact is surfaced with both values, not silently picked |
| E11 | Write-on-confirm honored | No evidence the local file was modified before the delta was presented and confirmed |
| E12 | Every substantive change is specific | Each listed change names the actual content that changed, not a vague "content updated" |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
