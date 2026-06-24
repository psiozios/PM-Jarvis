---
skill: interview-guide
archetype: Research-Synthesis
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /interview-guide

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
| E1 | JTBD structure | Questions structured around Jobs-to-be-Done framework: situation, motivation, outcome |
| E2 | Research objective stated | Opens with clear research objective: what decision this research will inform |
| E3 | Output path correct | File saved to `outputs/research/` with topic in filename |

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
| E8 | Open-ended questions only | Zero yes/no questions in the guide — all questions invite narrative responses |
| E9 | Leading questions flagged | No questions that suggest a 'right' answer or reveal the hypothesis |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Warm-up and cool-down included | Guide starts with rapport-building questions and ends with open floor |
| E11 | Probing prompts included | Follow-up probes listed for each main question (e.g., 'Tell me more about...', 'What happened next?') |
| E12 | Estimated timing per section | Time allocation suggested per section to keep interviews on track |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
