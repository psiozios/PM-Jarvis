---
skill: warehouse-brief
archetype: Analysis
eval-version: 1
last-updated: 2026-10-13
---

# Evals: /warehouse-brief

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, `config/house-style.md`, and the sources the output cites, and the loop runs until zero FAILs. Without the sources, E7 is **N/A with the reason named** — never PASS.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Brief structure | Coverage lines, then three to five insights, a Cut list, Run Quality where required, and a query appendix |
| E2 | Four-part insight | Each insight is written as numbered facts, logic, falsifiers, and next steps in the user's lane |
| E3 | Output path correct | Saved to `outputs/briefs/warehouse-brief-<DATE>.md`, with its ledger at `outputs/ledgers/warehouse-brief-<DATE>.md` |

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
| E8 | Durability | Every figure carries the date of the query that produced it. No figure is asserted as standing fact. See `references/protocols/freshness-provenance.md` |
| E9 | Source coverage declared | The output names which sources answered and, separately, any source that was unavailable with its reason. See `references/protocols/source-preflight.md` |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Landed on a live decision | Every insight names an open decision, its owner, and where it lives. FAIL on "this is interesting" with no decision |
| E11 | Next steps in the user's lane | Every next step is something the user can do in their role, never "the team should" |
| E12 | Ranked on two stated factors | How far it moves the decision × when the decision is made, both stated per insight |

### Category 5: Warehouse Discipline

| ID | Check | Criteria |
|----|-------|----------|
| E13 | No warehouse, no brief | The warehouse answered its preflight and the map was filled in. Where either failed, the output is one line naming which and what repairs it. FAIL on a brief built from dashboards, exports, or recall |
| E14 | Map read first | The lookup log shows the map read before the first query, and no query contradicts a grain, join key, or trap the map records |
| E15 | Read-only | Every query in the appendix is a `SELECT`. FAIL on any write, temp table in a shared schema, or scheduled query |
| E16 | Computed, not looked up | Every insight is a join, a cohort split, or an unrun trend. FAIL on a figure the user's own dashboards already show |
| E17 | Reconciled a second way | Each headline figure appears twice, by independent paths, both queries in the appendix and within the map's tolerance. FAIL on a single-path figure |
| E18 | Kills what the user already sees | Every candidate was checked against the user's dashboards, plan, review, and the last two briefs and scans, and every match is a `KILL` row naming where (`references/protocols/skill-patterns.md` Pattern 4) |
| E19 | Ledger-derived list | A ledger exists at `outputs/ledgers/warehouse-brief-<DATE>.md`, written before the list. Every candidate has a row, cuts and kills are reported beside the list, and nothing past the cap was dropped unreported (`references/protocols/evidence-ledger.md`) |
| E20 | Figures from query results | Every figure in a fact matches its query's output in the appendix, and every count was taken from a command, never typed (`references/protocols/freshness-provenance.md` rule 6) |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!--
Append after each run. Keep last 5. Notes must be legible enough to show
what broke and what fixed it — not just a pass/fail count. Include: which
check IDs failed, what remediation was applied, and the re-check result.
See references/protocols/skill-evals.md, "Legible Eval Results Log" for a
worked example row.
-->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
