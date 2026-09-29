---
skill: second-brain
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-09-28
---

# Evals: /second-brain

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Wiki page structured | Every page written opens with the YAML frontmatter the skill defines (`title`, `created`, `last_updated`, `source_count`, `status`), then a one-paragraph summary, then the body |
| E2 | Focus area correct | Each page lands in the focus area whose scope fits the source (a source may touch several), and that area's `wiki/index.md` lists it |
| E3 | Output path correct | Pages saved to `context-library/second-brain/{focus}/wiki/` with descriptive kebab-case filenames, and the run's entry appended to that area's `wiki/log.md` |

### Quality & Voice

| ID | Check | Criteria |
|----|-------|----------|
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language. **Spot-check the claims against the cited sources**; where a source cannot be reached, score N/A and name it rather than passing on plausibility |
| E8 | Compounding value | Entry connects to existing wiki entries via explicit cross-references, each resolving to a page on disk |
| E9 | Source attributed | States where the knowledge came from (meeting, article, experience, etc.) |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Search-friendly | Entry uses clear keywords and tags that future searches would match |
| E11 | Actionable framing | Knowledge framed as 'when to use this' not just 'what this is' |
| E12 | Freshness date included | Entry has a date and optional review-by date for time-sensitive knowledge |
| E13 | Surgical update | Every page that existed before the run was updated as a delta: its prior claims, citations, and dated lines survive, and no page shows more deletions than insertions without a stated reason |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
