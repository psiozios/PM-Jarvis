---
skill: business-model-canvas
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /business-model-canvas

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
| E1 | Canvas format complete | All 9 BMC sections present: Key Partners, Activities, Resources, Value Props, Customer Relationships, Channels, Segments, Cost Structure, Revenue Streams |
| E2 | Output path correct | File saved to `outputs/analyses/` with company/product in filename |
| E3 | Concise per section | Each canvas section is 3-5 bullet points — not paragraphs |

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
