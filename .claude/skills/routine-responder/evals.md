---
skill: routine-responder
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /routine-responder

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Thread discovery correct | Every `.thread-pointer.json` under `routines/*/` was checked, not a hardcoded subset |
| E2 | State file scoped correctly | Only `.last-reply-processed` files were written; no routine's own dated output or `.last-run-*` pointer was touched |
| E3 | Reaction lifecycle correct | "Thinking" reaction applied on pickup, swapped to "done" only after the reply send was confirmed |

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
| E8 | Loop-safety | The bot's own prior messages in a thread were never classified as actionable input |
| E9 | Correct actionable detection | A message was treated as actionable only if authored by the user, newer than the bot's last message, and newer than `.last-reply-processed` — all three, not a subset |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Silent stop on no replies | If no thread had an actionable message, nothing was sent and nothing was written — no "nothing found" filler message |
| E11 | Outward-draft-only | Any content destined for someone other than the user was produced as a draft, never sent automatically |
| E12 | Marker advanced only after confirmed send | `.last-reply-processed` only moved forward once the reply's delivery was confirmed by the notifier, not optimistically before |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
