---
skill: create-tickets
archetype: Code-Technical
eval-version: 2
last-updated: 2026-08-10
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
| E3 | Priority assigned | Each ticket has a priority level with brief justification |

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
| E8 | Dependencies noted | Cross-ticket dependencies explicitly listed with blocking/blocked relationships, and no duration attached to the chain |
| E9 | Cut by domain change | No ticket exists only because one behavior change touched an extra surface. FAIL on a `[Frontend]`/`[API]`/`[DB]` split of a single behavior |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | PRD traceability | Each ticket traces back to a specific requirement or user story |
| E11 | Edge cases included | Non-obvious edge cases listed in the description or acceptance criteria |
| E12 | Output to correct system | Tickets created via the connected tracker or saved to `outputs/analyses/[feature]-tickets.md` |
| E13 | Behavioral claims sourced | Every assertion about how the product behaves, what users do, or what was decided carries an inline source. FAIL on any unsourced behavioral claim |
| E14 | No implementation prescribed | No table, endpoint shape, library, or pattern is specified. Genuine external constraints are allowed **only** when stated as constraints and sourced |
| E15 | No sizing or scheduling | No t-shirt size, story points, day range, or sprint appears in any body or tracker field. A required tracker field was escalated to the user, not filled in |
| E16 | Open questions own their answer | Each open question names who can answer it, and any question answered in a source the run read is proposed as a description edit |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
