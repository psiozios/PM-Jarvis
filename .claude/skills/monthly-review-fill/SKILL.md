---
name: monthly-review-fill
description: Middle tier of the periodic-review cascade. Links and rolls up the month's completed weekly-review-fill entries into a synthesized monthly assessment — never re-derives from raw task activity. Pre-fills, asks only judgment questions, forward-creates.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

**What to provide:** Nothing required — defaults to the current month.

```
/monthly-review-fill                → pre-fill this month's review, rolling up its completed weeks
/monthly-review-fill --month 2026-07  → target a specific month
```

**What you get:** A pre-filled monthly entry whose assessment is synthesized from the month's `weekly-review-fill` entries — not re-derived from raw tickets. Same auto-vs-asked discipline, same preview-first, same forward-create with dedupe as the weekly tier.

**Time:** A couple minutes to review; the rollup itself is automatic once the weeks exist.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own. This is the middle tier of a nested cascade — see `weekly-review-fill` (the tier it rolls up) and `quarterly-review-fill` (the tier that rolls this one up in turn).

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Reviews store | `<REVIEWS_STORE>` | This month's existing entry, and every `weekly-review-fill` entry whose date range falls inside the month |
| Task tracker | `<TASK_TRACKER>` | Only used as a fallback for a week with no filled entry yet — see step 2 |
| Calendar | `<CALENDAR>` | Month boundaries, computed in local time |

## Workflow

### 1. Resolve the period and its weeks

Compute the target month's boundaries from `<CALENDAR>`. Identify every week whose range falls inside the month.

### 2. Require the lower tier, don't bypass it

For each week in range, check `<REVIEWS_STORE>` for a completed `weekly-review-fill` entry. If one is missing, that's the trigger to run `weekly-review-fill` for that week first — **never** fall back to re-deriving the month's accomplishments straight from raw `<TASK_TRACKER>` activity. The nesting is the point: a month reads its weeks, a quarter reads its months.

### 3. Roll up and synthesize

Read the completed weekly entries and synthesize the month's assessment block from them: what compounded across weeks, which weeks were strong or weak and why, what carried over more than once. This is a synthesis pass, not a concatenation — don't just paste four weeks back to back.

### 4. Create the period entry from template

Set derivable fields immediately: date range, links to every week entry rolled up, links to the prior/next month entries, and a rating computed from the weeks' own ratings.

### 5. Ask only genuine judgment questions

Everything derivable from the rolled-up weeks is auto-filled. Only ask what the weeks themselves don't answer — a monthly-scale judgment the weekly entries wouldn't have surfaced individually.

### 6. Auto-vs-asked table, preview-first, surgical write, forward-create

Same discipline as `weekly-review-fill` steps 5-8: table before the draft, nothing written until confirmed, delta-only write, next N months forward-created with dedupe.

## Output Format

```markdown
# Month <YYYY-MM> Review Draft

## Weeks Rolled Up
| Week | Rating | Link |
|---|---|---|
| <YYYY-Www> | <rating> | `<REVIEWS_STORE>` entry |

## Auto-Filled vs. Asked
| Item | Source | Auto-filled or Asked |
|---|---|---|
| Date range | `<CALENDAR>` | Auto-filled |
| Weekly rollup | Completed week entries | Auto-filled |
| Monthly rating | Computed from weekly ratings | Auto-filled |
| Monthly-scale judgment call | — | Asked |

## Draft Entry
<synthesized assessment, not a concatenation of the four weeks>

## Forward-Created
- Month <N+1> shell created in `<REVIEWS_STORE>`
```

## Runs as a Routine

A natural monthly-cadence routine — see `references/protocols/routines.md` and `setup/routine-setup.md`.

## Output Quality Self-Check

- [ ] Every week in range was checked for a completed entry before rolling up
- [ ] Missing weeks triggered `weekly-review-fill`, not a raw-activity fallback
- [ ] The assessment is a genuine synthesis, not four weeks pasted back to back
- [ ] Nothing derivable from the weekly entries was left in "asked"
- [ ] The write was a delta, and forward-created months were deduped

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Rolls up:** `weekly-review-fill` (required lower tier)

**Rolled up by:** `quarterly-review-fill`

**Related:** `weekly-review` (deeper weekly narrative, feeds this tier indirectly via its own second-brain filing)

## When to Use

- At the start or close of every month, once the month's weekly entries are filled

## When NOT to Use

- Before any of the month's weeks have a filled entry — run `weekly-review-fill` for those first

## Common Mistakes

- Re-deriving the month's accomplishments from raw tickets instead of rolling up the weeks
- Concatenating the weekly entries instead of synthesizing them
- Skipping a week with no entry instead of triggering its fill first
