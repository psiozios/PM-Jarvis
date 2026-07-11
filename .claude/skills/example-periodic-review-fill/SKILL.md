---
name: example-periodic-review-fill
description: "Example skill. Copy and adapt to your tools. Pre-fills a periodic review (week/month/quarter) from existing sources, asking only for genuine judgment calls, and forward-creates the next cycle with dedupe."
disable-model-invocation: false
user-invocable: true
---

> **Example skill. Copy and adapt to your tools.** Every `<PLACEHOLDER>` below stands for a concrete tool or id in your own workspace. This is Pattern 2 (Periodic-Review Assisted-Fill Cascade) from `references/protocols/skill-patterns.md` — read that first for the mechanics this skill instantiates.

## Quick Start

**What to provide:** Nothing required. State the tier if not obvious from context.

```
/example-periodic-review-fill week      → pre-fill this week's review
/example-periodic-review-fill month     → pre-fill this month's review, rolling up completed weeks
/example-periodic-review-fill quarter   → pre-fill this quarter's review, rolling up completed months
```

**What you get:** A pre-filled draft review with an explicit "auto-filled vs. asked" table, plus the next N periods forward-created (deduped against anything already scheduled). You edit the draft in one pass instead of starting from a blank template.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own.

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Reviews store | `<REVIEWS_STORE>` (e.g. your notes tool or tracker) | Prior period's review, current period's raw activity |
| Task tracker | `<TASK_TRACKER>` | Completed/carried items for the period, to auto-fill "what shipped" |
| Lower-tier reviews | `<REVIEWS_STORE>` | For month/quarter tiers: the completed reviews of the tier below, to roll up |
| Calendar | `<CALENDAR>` | Period boundaries, forward periods to create |

## Workflow

### 1. Determine tier and boundaries

Resolve the period (week/month/quarter) and its start/end dates from `<CALENDAR>`, computed in local time.

### 2. Auto-fill everything derivable

Pull from `<TASK_TRACKER>` and `<REVIEWS_STORE>`: what shipped, what's still open, what got reprioritized. For month/quarter tiers, roll up and synthesize the completed reviews of the tier below rather than re-deriving from raw activity (a quarter review reads the quarter's three month reviews, not twelve weeks of raw tickets).

### 3. Identify genuine judgment calls

Anything that isn't derivable — a qualitative read on how the period went, a call on what to change next period, a prioritization tradeoff — goes in the "asked" column. Never leave these blank; ask them directly, but never auto-fill a guess either.

### 4. Present the auto-vs-asked table

Show the user exactly what was inferred and what needs their input before drafting the rest of the review (see Output Format).

### 5. Surgical write

Once the user answers the judgment-call questions, fetch the current state of `<REVIEWS_STORE>` for this period, compute the delta between current state and the completed draft, and write only the delta — never replace the whole document (discipline: surgical writes, not wholesale replacement).

### 6. Forward-create next N periods

Create the next N periods' review shells in `<REVIEWS_STORE>`, deduped against anything already scheduled there. This runs only on confirm, same as the write in step 5.

## Output Format

```markdown
# <Tier> Review — <period label>

## Auto-Filled vs. Asked

| Item | Source | Auto-filled or Asked |
|---|---|---|
| Shipped this period | `<TASK_TRACKER>` | Auto-filled |
| What changed vs. plan | — | Asked |
| Carry-over items | `<TASK_TRACKER>` | Auto-filled |
| Next period's focus | — | Asked |

## Draft Review

<pre-filled sections, judgment-call answers inserted where the user provided them>

## Forward-Created

- <period N+1> shell created in `<REVIEWS_STORE>`
- <period N+2> shell created in `<REVIEWS_STORE>`
```

## Runs as a Routine

This pattern is a natural candidate for a scheduled routine (fire at the start of each period to pre-fill the draft before the user sits down to write it). See `references/protocols/routines.md` and `setup/routine-setup.md`.

## Output Quality Self-Check

- [ ] Nothing derivable was left in the "asked" column
- [ ] Nothing genuinely judgment-based was auto-filled with a guess
- [ ] Higher tiers rolled up from the tier below, not re-derived from raw activity
- [ ] The write to `<REVIEWS_STORE>` was a delta, not a wholesale replace
- [ ] Forward-created periods were deduped against what already existed

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Related:** `references/protocols/skill-patterns.md` (Pattern 2), `references/protocols/routines.md`

## When to Use

- At the start of a week/month/quarter review ritual

## When NOT to Use

- For a one-off retrospective with no recurring cadence — use `/post-mortem` or `/weekly-review` directly instead

## Common Mistakes

- Handing over a blank template instead of a pre-filled draft
- Guessing at a judgment call instead of asking
- Replacing the whole review document instead of writing only the delta
- Re-deriving a quarter review from raw tickets instead of rolling up the month reviews
