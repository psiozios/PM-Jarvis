---
skill: second-brain
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /second-brain

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
| E1 | Wiki entry structured | Each entry follows a consistent structure: Title, Summary, Details, Sources, Related |
| E2 | Topic correctly categorized | Entry placed in the right second-brain category (frameworks, people, processes, etc.) |
| E3 | Output path correct | File saved to `context-library/second-brain/` with descriptive filename |

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
| E8 | Compounding value | Entry connects to existing wiki entries via explicit cross-references |
| E9 | Source attributed | States where the knowledge came from (meeting, article, experience, etc.) |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Search-friendly | Entry uses clear keywords and tags that future searches would match |
| E11 | Actionable framing | Knowledge framed as 'when to use this' not just 'what this is' |
| E12 | Freshness date included | Entry has a date and optional review-by date for time-sensitive knowledge |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
