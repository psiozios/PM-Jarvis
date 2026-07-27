---
skill: chat-ingest
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /chat-ingest

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Preview table format | Every candidate thread shown with signal type, routing target, and reasoning before any write |
| E2 | Mode correctly identified | Output header states which mode ran (daily catch-all / channel / topic / catch-up / dm-threads) |
| E3 | Confirmation prompt present | Output ends with an explicit ask for which candidates to ingest |

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
| E8 | Durability | Any status-like claim proposed for ingestion is either dated or routed to `second-brain`'s citation convention — not asserted as timeless fact. See `references/protocols/freshness-provenance.md`. |
| E9 | Signal-filtering correctness | Low-signal candidates (acks, small talk, one-liners) were excluded from the preview, not just deprioritized |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Correct focus-area routing | Each candidate's proposed focus area is defensible from its content, and unclear fits are flagged rather than forced |
| E11 | Write-on-confirm honored | No thread was ingested into the second brain before the user confirmed |
| E12 | dm-threads mapping correct | In `dm-threads` mode, partners were matched against existing `stakeholders` profiles, not left unmapped when a profile exists |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
