---
skill: chat-ingest
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /chat-ingest

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
| E1 | Preview table format | Every candidate thread shown with signal type, routing target, and reasoning before any write |
| E2 | Mode correctly identified | Output header states which mode ran (daily catch-all / channel / topic / catch-up / dm-threads) |
| E3 | Confirmation prompt present | Output ends with an explicit ask for which candidates to ingest |

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
