---
name: weekly-review-fill
description: Base tier of the periodic-review cascade. Pre-fills the week's review entry from completed work, asks only genuine judgment questions, and forward-creates upcoming weeks with dedupe. Never hands over a blank questionnaire.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

**What to provide:** Nothing required — defaults to the current week.

```
/weekly-review-fill               → pre-fill this week's review entry
/weekly-review-fill --week 2026-W15  → target a specific week
```

**What you get:** A pre-filled draft of the week's review with an explicit auto-filled-vs-asked table, ready for a single edit pass — never a blank template. On confirm, the next N weeks get forward-created shells (deduped), and the delta is written to the reviews store.

**Time:** A couple minutes to review the draft; the fill itself is automatic.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own. This is the base tier of a nested cascade — see `monthly-review-fill` and `quarterly-review-fill`, which roll this tier up rather than re-deriving from raw activity.

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Reviews store | `<REVIEWS_STORE>` | This week's existing entry (if any), the prior week's entry for continuity |
| Task tracker | `<TASK_TRACKER>` | Tasks completed within the week's date range, for candidate accomplishments |
| Calendar | `<CALENDAR>` | Week boundaries, computed in local time |

## Workflow

### 1. Resolve the period

Compute the target week's start/end dates from `<CALENDAR>` in local time. Check `<REVIEWS_STORE>` for an existing entry for this week.

### 2. Create the period entry from template

If no entry exists, create it from the store's standing template. Set every derivable field immediately: date range, links to the prior and next week entries, and a rating computed from the completed-work count against whatever baseline the store defines.

### 3. Pull completed work

Query `<TASK_TRACKER>` for everything completed within the week's date range. These are the candidate accomplishments — draft them into the accomplishments section directly, not as a prompt for the user to fill in themselves.

### 4. Ask only genuine judgment questions

Everything derivable from step 2-3 is auto-filled. The only questions asked are things no source can answer: how the week actually felt, what should change, what's the honest read on a stalled item. Never leave a derivable field blank waiting on the user, and never guess at a judgment call.

### 5. Present the auto-vs-asked table, then the draft

Show exactly what was inferred versus what needs input (see Output Format) before the full draft — so the user's one edit pass is informed, not a cold read.

### 6. Preview-first, write on confirm

Nothing is written to `<REVIEWS_STORE>` until the user confirms the draft (including their answers to the judgment questions).

### 7. Surgical write

Fetch the entry's current state in `<REVIEWS_STORE>` immediately before writing, compute the delta against the confirmed draft, and write only that delta. Never replace the whole entry — a user's own prior edits to this week's entry survive.

### 8. Forward-create next N periods

Create shells for the next N weeks in `<REVIEWS_STORE>`, deduped against anything already scheduled there. This also runs only on confirm.

## Output Format

```markdown
# Week <YYYY-Www> Review Draft

## Auto-Filled vs. Asked
| Item | Source | Auto-filled or Asked |
|---|---|---|
| Date range | `<CALENDAR>` | Auto-filled |
| Completed work | `<TASK_TRACKER>` | Auto-filled |
| Rating | Computed from completion count | Auto-filled |
| How the week felt | — | Asked |
| What to change next week | — | Asked |

## Draft Entry
<pre-filled sections with judgment-question answers inserted where provided>

## Forward-Created
- Week <N+1> shell created in `<REVIEWS_STORE>`
```

## Runs as a Routine

A natural weekly-cadence routine — fire at the start (or end) of each week to have the draft ready before the user sits down. See `references/protocols/routines.md` and `setup/routine-setup.md`.

## Output Quality Self-Check

- [ ] Nothing derivable from the task tracker or calendar was left in "asked"
- [ ] Nothing genuinely judgment-based was auto-filled with a guess
- [ ] The write was a delta against current state, not a wholesale replace
- [ ] Forward-created weeks were deduped against existing entries
- [ ] Nothing was written before the draft was confirmed

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Rolled up by:** `monthly-review-fill` (synthesizes completed weeks into the month's assessment)

**Related:** `weekly-review` (deeper narrative synthesis — this skill fills the structured entry fast; `weekly-review` is the fuller reflective pass)

## When to Use

- At the start or close of every week, to keep the reviews store current with minimal manual entry

## When NOT to Use

- When you want the full narrative synthesis (patterns, learnings, stakeholder pulse) — that's `weekly-review`, which can read this skill's filled entry as a starting point

## Common Mistakes

- Handing over a blank entry instead of a pre-filled draft
- Guessing at a judgment question instead of asking
- Replacing the whole entry instead of writing only the delta
- Forward-creating a week that already has a shell, producing a duplicate
