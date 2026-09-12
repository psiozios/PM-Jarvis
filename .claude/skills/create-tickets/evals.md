---
skill: create-tickets
archetype: Code-Technical
eval-version: 2
last-updated: 2026-09-11
---

# Evals: /create-tickets

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Type-matched section set | Each ticket uses the section set for its issue type per `references/ticket-templates.md` — not one universal body across all four types |
| E2 | Acceptance criteria earn their place | Criteria appear only where the "done" boundary is genuinely ambiguous, and none restates the title. Absent criteria are correct, not a gap — **there is no floor** |
| E3 | Priority set at creation, on a frozen scale | Every ticket carries a priority, set from factors written into the tracker's own fields against anchors that hold across the whole board — not against this batch. No computed field was typed by hand, and an unassessed factor was left empty rather than guessed. See `references/protocols/tracker-writes.md` |

### Quality & Voice

| ID | Check | Criteria |
|----|-------|----------|
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language. **Spot-check the claims against the cited sources**; where a source cannot be reached, score N/A and name it rather than passing on plausibility |
| E8 | Dependencies noted | Cross-ticket dependencies explicitly listed with blocking/blocked relationships, and no duration attached to the chain |
| E9 | Cut by domain change | No ticket exists only because one behavior change touched an extra surface. FAIL on a `[Frontend]`/`[API]`/`[DB]` split of a single behavior |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | PRD traceability | Each ticket traces back to a specific requirement or user story |
| E11 | Edge cases where they exist | Non-obvious edge cases appear in the body where the type's section set has a place for them. Their absence is not a gap — the section set is a menu, and an empty section is deleted with its header, not padded (`references/protocols/tracker-writes.md` §6) |
| E12 | Output to correct system | Tickets created via the connected tracker or saved to `outputs/analyses/[feature]-tickets.md` |
| E13 | Behavioral claims sourced | Every assertion about how the product behaves, what users do, or what was decided carries an inline source. FAIL on any unsourced behavioral claim |
| E14 | No implementation prescribed | No table, endpoint shape, library, or pattern is specified. Genuine external constraints are allowed **only** when stated as constraints and sourced |
| E15 | No sizing or scheduling | No t-shirt size, story points, day range, or sprint appears in any body or tracker field. A required tracker field was escalated to the user, not filled in |
| E16 | Open questions own their answer | Each open question names who can answer it, and any question answered in a source the run read is proposed as a description edit |
| E17 | Body within the corpus-median budget | Body length measured against the median in `references/tickets-corpus.md`, not an assumed number. No header stands over an empty section |
| E18 | Approved from a table, not from bodies | The chat carried one row per ticket with its factors and score, and one line per ticket after creation. FAIL on a full ticket body rendered in the conversation (`references/protocols/tracker-writes.md` §7) |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
