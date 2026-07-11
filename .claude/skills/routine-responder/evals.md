---
skill: routine-responder
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-07-11
---

# Evals: /routine-responder

## How to Run (automatic on every skill invocation)

1. Original agent completes skill output and runs informal self-check
2. Original agent spawns a separate eval agent (clean context window)
3. Eval agent reads: this file, the skill output (or the sweep's log of what it did/didn't do), `config/house-style.md`
4. Evaluates each criterion independently → PASS / FAIL / PARTIAL
5. FAILs returned to original agent for revision → re-eval loop
6. Zero FAILs achieved → log results below

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
| E4 | No AI slop | Zero instances of: delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Follows any active rules in `config/house-style.md` |
| E6 | Human-sounding | Varied sentence lengths, contractions used naturally, no formulaic paragraph openings |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | References specific data from context sources — not generic placeholder language |
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
