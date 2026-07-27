---
skill: business-model-canvas
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /business-model-canvas

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Canvas format complete | All 9 BMC sections present: Key Partners, Activities, Resources, Value Props, Customer Relationships, Channels, Segments, Cost Structure, Revenue Streams |
| E2 | Output path correct | File saved to `outputs/analyses/` with company/product in filename |
| E3 | Concise per section | Each canvas section is 3-5 bullet points — not paragraphs |

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
| E8 | Revenue model specific | Revenue streams name specific pricing models with numbers where available |
| E9 | Customer segments defined | Segments described with specific characteristics, not generic labels |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Value props differentiated | Value propositions state what's unique vs competitors, not just features |
| E11 | Cost drivers identified | Cost structure names the top 3-5 cost drivers with relative magnitude |
| E12 | Hypotheses flagged | Assumptions that need validation are explicitly marked as hypotheses |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
