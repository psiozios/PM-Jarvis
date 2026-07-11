---
name: refinement-prep
description: Slate for the next refinement ceremony, run off a cleaned issue tracker. Asks the period's theme first, ranks a capped shortlist by theme-fit then live priority then readiness, drafts each item's enrichment, and surfaces the unknowns that would cause rework. Read-only.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

**What to provide:** The period's theme (the "big rock") — if not given, this skill asks first.

```
/refinement-prep               → asks for the theme, then builds the slate
/refinement-prep "<theme>"     → builds the slate directly against a stated theme
```

**What you get:** A capped shortlist ranked for the next refinement ceremony, each item's enrichment drafted, and the 1-2 genuine unknowns that would cause rework if the item entered the ceremony raw. Strictly read-only — a staged brief the user applies in the tracker UI.

**Time:** A few minutes, most of it after `backlog-groom` has already cleaned the board.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own.

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Issue tracker | `<TASK_TRACKER>` | Full current board state, post-`backlog-groom` if it's been run recently |
| Strategy | `context-library/strategy/` | Current priorities, for theme-fit ranking |
| Prioritize method | `.claude/skills/prioritize/SKILL.md` (if present) | The LNO-style ranking method, if the user wants live priority scored consistently with how they prioritize elsewhere |

## Workflow

### 1. Ask the theme first

Before touching the board, ask the user what this ceremony's theme is — the one big rock this refinement session should be organized around. Don't infer it silently; a wrong assumed theme produces a shortlist for the wrong ceremony.

### 2. Read the board — never mutate it

Pull the current board state from `<TASK_TRACKER>`. Strictly read-only, same as `backlog-groom` (see `references/protocols/skill-patterns.md` discipline #8).

### 3. Rank by theme-fit, then live priority, then readiness

Filter to items that plausibly fit the stated theme. Within that set, rank by live priority — using the `prioritize` skill's method if it's present in the workspace, so ranking stays consistent with how the user prioritizes elsewhere; otherwise rank by the tracker's own priority field, judged live rather than from a stale doc. Break remaining ties by readiness (how close the item already is to refinement-ready).

### 4. Cap the shortlist

A refinement ceremony has limited time. Cap the shortlist to what the ceremony can realistically cover — don't hand over the whole filtered set.

### 5. Draft each item's enrichment

For each shortlisted item, draft what it needs to enter refinement ready: a clearer description, acceptance criteria, a sizing note — whatever's missing, drafted inline and ready to paste.

### 6. Surface the unknowns

For each shortlisted item, identify the 1-2 genuine unknowns that would cause rework if the item entered the ceremony raw and got refined on a wrong assumption. Not every open question — only the ones that would actually cause backtracking.

## Output Format

```markdown
# Refinement Slate — <DATE>
**Theme:** <stated theme>

## Shortlist (ranked)
1. **[<item>](<link>)** — theme-fit: <why> | priority: <live rank> | readiness: <ready / needs enrichment>
   **Enrichment drafted:** <description / AC / sizing note, ready to paste>
   **Unknowns that would cause rework:** <1-2 items, or "none identified">

2. ...

## Cut From Shortlist (theme-fit too weak)
- <item> — <why it didn't make the cap>
```

## Runs as a Routine

Pairs with `backlog-groom` on a recurring cadence — hygiene between ceremonies, this slate right before one. See `references/protocols/routines.md` and `setup/routine-setup.md`.

## Output Quality Self-Check

- [ ] Theme was asked (or explicitly given) before the board was read
- [ ] Board was read, never written to
- [ ] Ranking used theme-fit first, then live priority, then readiness — in that order
- [ ] Shortlist is genuinely capped, not the full filtered set
- [ ] Every shortlisted item has drafted enrichment ready to paste
- [ ] Unknowns surfaced are ones that would actually cause rework, not every open question

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Before this:** `backlog-groom` (the cleaned board this slate runs off of)

**Related:** `prioritize` (ranking method, when present), `sprint-planning` (the ceremony this slate feeds into)

## When to Use

- Right before a refinement ceremony, once the board has recently been groomed

## When NOT to Use

- For whole-board hygiene — that's `backlog-groom`, which this skill assumes has already run

## Common Mistakes

- Building the shortlist before asking what the theme is
- Handing over an uncapped list instead of what the ceremony can realistically cover
- Surfacing every open question instead of just the ones that would cause rework
- Writing directly to the tracker instead of staging a brief
