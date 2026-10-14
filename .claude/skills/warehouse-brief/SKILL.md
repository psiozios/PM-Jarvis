---
name: warehouse-brief
description: Weekly inside-out brief of 3 to 5 insights computed from the org's own warehouse — a join, a cohort split, or a trend nobody has run — each landed on a live decision and its owner, reconciled a second way, query in an appendix. Read-only. Reads the warehouse map first; no warehouse, no brief. Kills what you already see.
user-invocable: true
disable-model-invocation: false
---

The inside-out half of the upside scan. `/proactive-gaps` reads what other institutions have written down; this skill reads what the org's own data says that nobody has looked at yet, and lands each finding on a decision someone is about to make.

## Quick Start

**What to provide:** Nothing required. A connected warehouse and a filled-in warehouse map are preconditions, not inputs.

```
/warehouse-brief                    → this week's brief
/warehouse-brief --focus activation → bias candidates toward one area's live decisions
```

**What you get:** Three to five insights, each written as numbered facts, logic, falsifiers, and next steps in your lane, each landed on a named live decision and its owner. A Cut list beside them, and every query in an appendix. Read-only: nothing is written but the brief and its ledger.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own. Realizes Pattern 5 (Inside-Out Warehouse Brief) from `references/protocols/skill-patterns.md` — read that first for the mechanics this skill instantiates.

**No warehouse, no brief.** Two preconditions, checked before anything else: `<WAREHOUSE>` answers its preflight (`references/protocols/source-preflight.md`), and `context-library/metrics/warehouse-map.md` is filled in, its Status line no longer reading `template`. If either fails, the run stops with one line naming which, and what repairs it. Dashboards, exports, and recall are not a substitute; they are what the user already sees.

**Read the warehouse map before the first query.** Its grains, join keys, traps, control totals, and cost limits bind every query. A table the map does not list is a gap to report, never a license to guess its grain.

**Read-only.** `SELECT` only. No writes, no tables or views in shared schemas, no scheduled queries, no dashboards. Stay inside the map's cost limits.

**Each insight is computed, not looked up.** One of three kinds: a **join** across tables nobody joins, a **cohort split** a top-line average hides, or an **unrun trend**, a metric over a window or cut no dashboard shows. A number already on a dashboard the user sees is not an insight.

**Landed on a live decision and its owner.** A decision still open, in the tracker, `context-library/decisions/`, this week's plan, the OKRs, or an upcoming meeting, named with its owner and where it lives. No live decision, no insight: cut it as "changes no live decision".

**Reconciled a second way.** Compute the headline figure by an independent path before it ships: a different table, a different grain rolled up, or a control total from the map. Both figures go in the insight. Where they disagree beyond the map's tolerance, the insight is cut with both shown.

**Kill what the user already sees** (`references/protocols/skill-patterns.md` Pattern 4). A match is a `KILL` row naming where they see it.

**Three to five, never padded, never silently cut.** Fewer than three that clear the bars ships fewer, with Run Quality saying what blocked the rest. Past five, the rest are reported in Cut with their rank (`references/protocols/evidence-ledger.md` §4).

**Every figure comes from a query result**, quoted from its output, never typed (`references/protocols/freshness-provenance.md` rule 6).

## Context Routing

| Source | Location | What to Extract |
|--------|----------|------------------|
| Warehouse | `<WAREHOUSE>` | Query results, read-only |
| Warehouse map | `context-library/metrics/warehouse-map.md` | Tables, grains, join keys, traps, control totals, tolerance, cost limits. Read before the first query |
| Live decisions | `<TASK_TRACKER>`, `context-library/decisions/`, the latest `outputs/weekly-plans/`, `context-library/strategy/` OKRs, `<CALENDAR>` for the next two weeks | Open decisions, each with its owner and where it lives |
| What the user already sees | dashboards the user owns or follows in `<METRICS_SOURCE>`, the latest weekly plan and review, the last two `outputs/briefs/warehouse-brief-*.md` and `outputs/briefs/proactive-gaps-*.md`, `outputs/state/rulings-warehouse-brief.md` | The kill list |

For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected, except the warehouse: without it there is no brief. A source that is connected but fails — an expired credential, a revoked scope, an OAuth refresh with no browser — is reported unavailable by name with its reason and never listed among the sources swept (`references/protocols/source-preflight.md`).

## Workflow

### 1. Preflight and the map

Check `<WAREHOUSE>` and every other source. Read the warehouse map in full. Either precondition failing ends the run here, in one line.

### 2. Build the kill list, then the decision list

Before any query, write down what the user already sees, and the live decisions with their owners. Candidates come from decisions, not from tables: a finding with no decision attached is noise, however interesting.

### 3. Generate candidates against decisions

For each live decision, ask which join, cohort split, or unrun trend would move it. One decision may yield several candidates, and each candidate gets a ledger row (`references/protocols/evidence-ledger.md`).

### 4. Query, logging as you go

Check the map's traps for every table a query touches before sending it. Append each query and its row count to the lookup log the moment it returns. Copy the SQL verbatim into the appendix.

### 5. Reconcile a second way

Recompute each surviving headline figure by an independent path. Record both paths and both figures in the ledger row.

### 6. Kill, cut, rank, cap

`KILL` what the user already sees, naming where. Cut what changes no live decision, what did not reconcile, and what turned out to be a lookup rather than a computation. Rank the rest on how far the figure would move the decision × how soon the decision is made, and state both factors. Ship three to five.

### 7. Write each insight in four parts

Numbered facts (each from a named query in the appendix), the logic from the facts to the decision, the falsifiers, and next steps the user can take in their own lane. Save to `outputs/briefs/warehouse-brief-<DATE>.md`.

## Output Template

Brief shape, the four-part insight, and the query appendix: `references/brief-template.md` — read before writing the first insight.

## Runs as a Routine

Weekly, by design — `references/protocols/routines.md`, `setup/routine-setup.md`. Register the warehouse's preflight check first (`setup/routine-setup.md`), since an unattended run with no warehouse ends at step 1.

## Output Quality Self-Check

- [ ] The warehouse answered and the map was read before the first query, or the run stopped at step 1 saying which precondition failed
- [ ] Every query was `SELECT`-only and inside the map's cost limits
- [ ] Every insight is a join, a cohort split, or an unrun trend, not a number from a dashboard
- [ ] Every insight names a live decision, its owner, and where it lives
- [ ] Every headline figure was reconciled a second way, with both paths and both figures shown
- [ ] Every candidate was checked against what the user already sees, and the matches are `KILL` rows naming where
- [ ] Three to five shipped, and the rest are in Cut with their reason or rank
- [ ] Every figure is quoted from a query result in the appendix

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it the output (or its absolute path), this skill's `evals.md`, `config/house-style.md`, and the sources the output cites — E7 cannot be scored without them, and scoring it from plausibility is a vacuous PASS. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/proactive-gaps` -> when a candidate's evidence is another institution's text rather than the org's own data
- `/decision-doc` -> when an insight moves a live decision enough to write the decision down
- `/root-cause-analysis` -> when an insight is a drop that needs diagnosing before anyone acts
- `/retention-analysis` -> when a cohort split points at where users stop coming back

## When to Use

- Weekly, to put what the org's own data says in front of the decisions about to be made

## When NOT to Use

- To answer one specific metric question — query it directly, or use `/root-cause-analysis` for a known drop
- When no warehouse is connected — set one up with `/connect-mcps` and fill in the warehouse map first

## Common Mistakes

- **Querying before reading the map.** A grain guessed wrong doubles a count, and the number looks fine
- **Reporting what a dashboard already shows.** The user dismisses it as known, and the next brief gets read less
- **An insight with no decision.** Interesting is not the bar; changing a live decision is
- **One path to the number.** An unreconciled figure is a hypothesis presented as a fact
- Typing a figure instead of quoting the query result
