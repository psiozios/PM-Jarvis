---
name: weekly-review-fill
description: Fill in the week's entry in a standing review tracker — pre-filled from work you actually completed, asking only the genuine judgment questions, never handing over a blank questionnaire. Base tier of the periodic-review cascade; forward-creates upcoming week shells with dedupe. For a free-form week retrospective, use weekly-review.
user-invocable: true
disable-model-invocation: false
---

## Quick Start

**What to provide:** Nothing required — defaults to the current week.

```
/weekly-review-fill               → pre-fill this week's review entry
/weekly-review-fill --week 2026-W15  → target a specific week
```

**What you get:** The week's entry drafted straight into your reviews store, with only its empty fields filled, the next N week shells created (deduped), and a reply that links the page, shows the auto-filled-vs-asked table, and asks only the judgment questions. The write mode is a per-surface setting in `config/write-surfaces.md`; set the store to `propose` and you get a preview first instead.

**Time:** A couple minutes to review the draft; the fill itself is automatic.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own. This is the base tier of a nested cascade — see `monthly-review-fill` and `quarterly-review-fill`, which roll this tier up rather than re-deriving from raw activity.

## Context Routing

| Source | Location | What to Extract |
|--------|----------|------------------|
| Reviews store | `<REVIEWS_STORE>` | This week's existing entry (if any), the prior week's entry for continuity |
| Task tracker | `<TASK_TRACKER>` | Tasks resolved within the week's date range, filtered on resolved date and never created date, for candidate accomplishments |
| Calendar | `<CALENDAR>` | Week boundaries, computed in local time |


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected. A source that is connected but fails — an expired credential, a revoked scope, an OAuth refresh with no browser — is reported unavailable by name with its reason and never listed among the sources swept (`references/protocols/source-preflight.md`).

## Workflow

### 1. Resolve the period

Compute the target week's start/end dates from `<CALENDAR>` in local time. Check `<REVIEWS_STORE>` for an existing entry for this week.

**That check is a dedupe-before-write, not an already-ran guard.** It answers "does an entry exist to update" so the write stays surgical. It never answers "did this run already" — when this skill is wrapped as a routine, that question is answered from the routine's own confirmed-delivery marker and from nothing downstream (`references/protocols/routines.md` disciplines #2 and #3). Reading the store as an already-ran signal means a user who deletes an entry gets no rerun, and a store that fails auth gets a duplicate.

### 2. Create the period entry from template

If no entry exists, create it from the store's standing template. Set every derivable field immediately: date range, links to the prior and next week entries, and a rating.

**The rating needs a stated arithmetic, and the store's baseline needs to be read, not assumed.** Read the baseline the store actually defines, write down which operation you applied, and put both in the auto-filled column — a rating that rolls up two more tiers cannot be audited if the base unit is undefined. Where the store defines no baseline, say so and leave the rating for the user rather than inventing a scale (`references/protocols/tracker-writes.md` §§1-2: the anchors are fixed and written down, and a computed field is never typed by hand).

### 3. Pull completed work

Query `<TASK_TRACKER>` for everything completed within the week's date range. These are the candidate accomplishments — draft them into the accomplishments section directly, not as a prompt for the user to fill in themselves.

### 4. Ask only genuine judgment questions

Everything derivable from step 2-3 is auto-filled. The only questions asked are things no source can answer: how the week actually felt, what should change, what's the honest read on a stalled item. Never leave a derivable field blank waiting on the user, and never guess at a judgment call.

### 5. Read the surface's write mode

Read the `<REVIEWS_STORE>` row in `config/write-surfaces.md`. Under `draft-in-place`, steps 6-7 run now and step 8 reports them. Under `propose`, step 8's table and draft come first, and steps 6-7 run on confirm.

### 6. Write the draft into the entry

Fetch the entry live immediately before writing and fill **only the fields that are empty**. A field with anything in it is the user's: never overwrite it, and put a different derivation in the reply as a proposal. Never replace the whole entry. Goal, project, and status changes are proposals in the reply, never writes. The user's answers to the judgment questions go into their fields as given.

### 7. Forward-create next N periods

Create shells for the next N weeks in `<REVIEWS_STORE>`, deduped against the live store immediately before each create.

### 8. Reply with the link, the table, and the questions

Open with the link to the entry. Then the auto-vs-asked table (see Output Template), what was filled and what was left alone, any proposals, and the judgment questions.

## Output Template

```markdown
# Week <YYYY-Www> Review — [open the entry](<link>)

## Auto-Filled vs. Asked
| Item | Source | Auto-filled or Asked |
|---|---|---|
| Date range | `<CALENDAR>` | Auto-filled |
| Completed work | `<TASK_TRACKER>` | Auto-filled |
| Rating | Computed from completion count | Auto-filled |
| How the week felt | — | Asked |
| What to change next week | — | Asked |

## Written in Place
<fields filled, each one previously empty> · **Left alone:** <fields that already had content>

## Proposals
<goal, project, or status changes, and any different derivation for a filled field; omit when none>

## Questions
<the judgment questions only the user can answer>

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
- [ ] Writes followed the store's mode in `config/write-surfaces.md`: only empty fields filled, the page linked, goals, projects, and statuses only proposed

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it the output (or its absolute path), this skill's `evals.md`, `config/house-style.md`, and the sources the output cites — E7 cannot be scored without them, and scoring it from plausibility is a vacuous PASS. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/monthly-review-fill` -> when four weeks are filled and the month can be rolled up
- `/weekly-review` -> when you want the fuller reflective narrative rather than the structured entry
- `/weekly-plan` -> when this week's entry should shape next week's priorities

## When to Use

- At the start or close of every week, to keep the reviews store current with minimal manual entry

## When NOT to Use

- When you want the full narrative synthesis (patterns, learnings, stakeholder pulse) — that's `weekly-review`, which can read this skill's filled entry as a starting point

## Common Mistakes

- Handing over a blank entry instead of a pre-filled draft, or a preview in chat when the store is set to `draft-in-place`
- Guessing at a judgment question instead of asking
- Replacing the whole entry, or overwriting a field the user already filled
- Forward-creating a week that already has a shell, producing a duplicate
