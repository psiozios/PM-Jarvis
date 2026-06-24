---
skill: ralph-wiggum
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /ralph-wiggum

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
| E1 | Devil's advocate framing | Criticism is delivered in the skill's distinctive irreverent voice |
| E2 | Real issues found | Identifies genuine weaknesses, not manufactured objections |
| E3 | Feedback is specific | Each criticism points to a specific section or claim, not vague complaints |

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
| E8 | Assumptions challenged | Calls out at least 2 unstated assumptions in the document |
| E9 | Alternative perspectives offered | For each criticism, suggests what would make it stronger |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Severity distinguished | Separates fatal flaws from nice-to-fix issues |
| E11 | Constructive underneath the humor | Every humorous jab contains an actionable improvement suggestion |
| E12 | Document scope respected | Critiques the document for what it is, not what it isn't (e.g., doesn't fault a PRD Lite for lacking detail) |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
