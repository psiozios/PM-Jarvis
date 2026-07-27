---
skill: pre-mortem
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /pre-mortem

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Pre-mortem structure | Contains: Scenario, Risk Categories, Likelihood/Impact Matrix, Mitigations sections |
| E2 | Output path correct | File saved to `outputs/pre-mortems/` with project and date in filename |
| E3 | Future tense framing | Risks framed as 'what could go wrong' scenarios, not current problems |

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
| E8 | Risks categorized | Risks organized by type: technical, organizational, market, execution |
| E9 | Likelihood and impact rated | Each risk has explicit likelihood (high/med/low) and impact rating |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Mitigations actionable | Each high-priority risk has a specific mitigation action, not 'monitor closely' |
| E11 | Trigger signals defined | Early warning signs identified for top risks — how would we know it's happening? |
| E12 | Owner per mitigation | Each mitigation action has a named owner and timeline |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
