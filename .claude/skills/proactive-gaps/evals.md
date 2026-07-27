---
skill: proactive-gaps
archetype: Analysis
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /proactive-gaps

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Two-horizon structure | Output separates Present-State Alpha, Forward Alpha, and a Contrarian Read — not a merged list |
| E2 | Ranked and capped | Items within each horizon are ranked by impact and the list is tight, not exhaustive |
| E3 | "Your lane" stated per item | Every item explicitly states what the user can do with it |

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
| E8 | Durability | Evidence cited for each item is either dated or points to a live source, never asserted as an unchanging fact. See `references/protocols/freshness-provenance.md`. |
| E9 | Evidence-backed, not speculative | Every item cites a real workspace source; nothing is included on pure inference with no evidence trail |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Elevated-posture-but-landed | Every item connects a broad/elevated observation back to something concrete in the user's actual IC lane |
| E11 | Contrarian pass grounded | The over-indexing claim is backed by actual recent-meeting evidence, not a generic assertion |
| E12 | Surface-only honored | No task was created, no message drafted for sending, nothing written beyond the scan output itself |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
