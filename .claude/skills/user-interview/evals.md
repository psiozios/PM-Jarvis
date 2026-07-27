---
skill: user-interview
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /user-interview

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Interview processed completely | All provided interview data transformed — no sections skipped or summarized away |
| E2 | JTBD format used | Insights framed as Jobs-to-be-Done where applicable: 'When [situation], I want to [motivation], so I can [outcome]' |
| E3 | Output path correct | File saved to `outputs/research/` or `outputs/research-synthesis/` with participant and date |

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
| E8 | Direct quotes extracted | Key participant quotes pulled verbatim with context for how they arose |
| E9 | Surprises highlighted | Unexpected findings or moments that contradicted assumptions explicitly flagged |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Behavioral observations separated from opinions | Distinguishes what participants DID from what they SAID they'd do |
| E11 | Follow-up questions suggested | Proposes 2-3 questions for the next interview based on gaps found |
| E12 | Pattern connections noted | Links findings to patterns from previous interviews or research if available |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
