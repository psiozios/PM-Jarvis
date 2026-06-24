---
skill: content-marketing
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /content-marketing

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
| E1 | Content type matched | Output format matches the requested content type (blog post, changelog, case study, etc.) |
| E2 | SEO-aware structure | Includes headline, subheadings, and meta description where applicable |
| E3 | Output path correct | File saved to `outputs/content/` with descriptive filename |

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
| E8 | Product-led narrative | Content ties back to a specific product capability or user outcome |
| E9 | Audience-specific language | Vocabulary and examples match the target reader persona, not generic marketing speak |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | CTA present and clear | Includes a specific call-to-action appropriate to the content type |
| E11 | Claims backed by evidence | Every product claim references a specific feature, metric, or customer result |
| E12 | Distribution channel noted | Suggests where/how to publish with channel-specific formatting notes |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
