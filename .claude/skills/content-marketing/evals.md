---
skill: content-marketing
archetype: Document-Writer
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /content-marketing

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

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
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
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
