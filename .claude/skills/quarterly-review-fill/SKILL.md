---
name: quarterly-review-fill
description: Top tier of the periodic-review cascade. Links and rolls up the quarter's completed monthly-review-fill entries into a synthesized quarterly assessment — never re-derives from raw weeks or task activity. Pre-fills, asks only judgment questions, forward-creates.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

**What to provide:** Nothing required — defaults to the current quarter.

```
/quarterly-review-fill                → pre-fill this quarter's review, rolling up its completed months
/quarterly-review-fill --quarter 2026-Q3  → target a specific quarter
```

**What you get:** A pre-filled quarterly entry whose assessment is synthesized from the quarter's three `monthly-review-fill` entries — not re-derived from twelve weeks or raw tickets. Same discipline as the two tiers below it.

**Time:** A couple minutes to review; the rollup is automatic once the months exist.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own. This is the top tier of a nested cascade — see `monthly-review-fill` (the tier it rolls up) and `weekly-review-fill` (the base tier two levels down).

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Reviews store | `<REVIEWS_STORE>` | This quarter's existing entry, and every `monthly-review-fill` entry inside it |
| Strategy | `context-library/strategy/` | The quarter's stated OKRs/goals, for grading the quarter against intent, not just activity |
| Calendar | `<CALENDAR>` | Quarter boundaries, computed in local time |

## Workflow

### 1. Resolve the period and its months

Compute the target quarter's boundaries from `<CALENDAR>`. Identify the three months inside it.

### 2. Require the lower tier, don't bypass it

For each month, check `<REVIEWS_STORE>` for a completed `monthly-review-fill` entry. If missing, that's the trigger to run `monthly-review-fill` for that month — **never** skip two tiers and re-derive the quarter from raw weeks or tickets.

### 3. Roll up and synthesize against strategy

Read the three monthly entries and synthesize the quarter's assessment: trajectory across the three months, whether the quarter's OKRs (from `context-library/strategy/`) were actually advanced, and what the quarter's throughline was. Grade against stated intent, not just a list of what happened.

### 4. Create the period entry from template

Set derivable fields: date range, links to all three month entries, links to prior/next quarter entries, and a rating computed from the months' own ratings and OKR progress.

### 5. Ask only genuine judgment questions

Only quarterly-scale calls the months themselves don't resolve — a strategic read, a call on next quarter's focus.

### 6. Auto-vs-asked table, preview-first, surgical write, forward-create

Same discipline as the two tiers below: table before the draft, nothing written until confirmed, delta-only write, next N quarters forward-created with dedupe.

## Output Format

```markdown
# Quarter <YYYY-QN> Review Draft

## Months Rolled Up
| Month | Rating | Link |
|---|---|---|
| <YYYY-MM> | <rating> | `<REVIEWS_STORE>` entry |

## OKR Progress (from context-library/strategy/)
| Objective | Status |
|---|---|

## Auto-Filled vs. Asked
| Item | Source | Auto-filled or Asked |
|---|---|---|
| Date range | `<CALENDAR>` | Auto-filled |
| Monthly rollup | Completed month entries | Auto-filled |
| OKR progress | `context-library/strategy/` + monthly rollups | Auto-filled |
| Quarterly-scale judgment call | — | Asked |

## Draft Entry
<synthesized assessment graded against stated OKRs, not a concatenation of three months>

## Forward-Created
- Quarter <N+1> shell created in `<REVIEWS_STORE>`
```

## Runs as a Routine

A natural quarterly-cadence routine — see `references/protocols/routines.md` and `setup/routine-setup.md`.

## Output Quality Self-Check

- [ ] Every month in the quarter was checked for a completed entry before rolling up
- [ ] Missing months triggered `monthly-review-fill`, not a raw-activity or raw-week fallback
- [ ] The assessment is graded against stated OKRs, not just a recap of activity
- [ ] Nothing derivable from the monthly entries was left in "asked"
- [ ] The write was a delta, and forward-created quarters were deduped

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Rolls up:** `monthly-review-fill` (required lower tier)

**Related:** `okr-planning` (next quarter's OKRs, informed by this review), `board-deck` (quarterly assessment feeds the QBR narrative)

## When to Use

- At quarter close, once all three months have filled entries

## When NOT to Use

- Before the quarter's months have filled entries — run `monthly-review-fill` for those first

## Common Mistakes

- Re-deriving the quarter from raw weeks or tickets instead of rolling up the months
- Reporting activity without grading it against the quarter's stated OKRs
- Skipping a month with no entry instead of triggering its fill first
