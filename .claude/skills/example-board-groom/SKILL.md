---
name: example-board-groom
description: "Example skill. Copy and adapt to your tools. Read-only hygiene pass over a shared board: emits a UI-action checklist grouped by the click the human makes, drafted text inline. Never mutates the board itself."
disable-model-invocation: false
user-invocable: true
---

> **Example skill. Copy and adapt to your tools.** Every `<PLACEHOLDER>` below stands for a concrete tool or id in your own workspace. This is the hygiene half of Pattern 3 (Prep-Then-UI Grooming + Slate-for-Ceremony) from `references/protocols/skill-patterns.md` — read that first for the full pair. The slate-for-ceremony sibling (rank a shortlist for the next planning ceremony) follows the same read-only, live-priority mechanics and is described in the catalog but not separately shipped as an example here.

## Quick Start

**What to provide:** Nothing required.

```
/example-board-groom               → hygiene pass over the default board
```

**What you get:** A checklist grouped by the UI action you'll take (close, reorder, re-allocate, tag, fix description), with drafted replacement text inline wherever a fix is text-based. This skill never touches `<ISSUE_BOARD>` directly — you apply every change by hand from the checklist.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own.

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Issue board | `<ISSUE_BOARD>` (e.g. your kanban/backlog tool) | Full current state: every card, status, description, age, assignee |
| Sibling review outputs | `outputs/`, `<REVIEWS_STORE>` | Cross-check: does a card map to something already flagged elsewhere? |

## Workflow

### 1. Read the full board

Pull every card's current state from `<ISSUE_BOARD>`. This is read-only — nothing in this skill writes back to the board.

### 2. Classify each card by the click it needs

For each card that needs attention, determine which UI action would fix it:
- **Close** — stale, duplicate, or already resolved elsewhere
- **Reorder** — priority doesn't match its position
- **Re-allocate** — assigned to someone who's no longer the right owner
- **Tag** — missing a label that would make it discoverable
- **Fix description** — thin, stale, or unclear enough to cause rework later

### 3. Apply false-positive discipline

Before flagging, check discipline #7 from `skill-patterns.md`: a deliberately terse card is not automatically "thin," a card that's been open a long time by design (a backlog item, not a stuck one) is not automatically "stale." Drop anything that doesn't survive this check.

### 4. Draft the fix inline

For any text-based fix (a rewritten description, a suggested tag), draft the replacement text directly in the checklist — the human should be able to paste it, not compose it from scratch.

### 5. Group and output

Group the checklist by UI action (see Output Format), not by card — this matches how the human will actually work through it.

## Output Format

```markdown
# Board Hygiene Pass — <DATE>

## Close
- [ ] **[<card title>](<link>)** — <why: duplicate of / resolved via / stale since>

## Reorder
- [ ] **[<card title>](<link>)** — currently <position>, suggested <position> because <reason>

## Re-allocate
- [ ] **[<card title>](<link>)** — currently <owner>, suggested <owner> because <reason>

## Tag
- [ ] **[<card title>](<link>)** — add tag: `<suggested-tag>`

## Fix Description
- [ ] **[<card title>](<link>)**
  Current: "<current description, truncated>"
  Suggested: "<drafted replacement, ready to paste>"
```

## Runs as a Routine

This pattern pairs well with a recurring cadence — hygiene between ceremonies, slate before them. See `references/protocols/routines.md` and `setup/routine-setup.md` to schedule it.

## Output Quality Self-Check

- [ ] Board was read, never written to
- [ ] Checklist grouped by UI action, not by card
- [ ] Every text-based fix has drafted replacement text ready to paste
- [ ] Every flagged item survived the false-positive check (not just long-lived, not just deliberately light)
- [ ] Priority judgments made live from current board state, not a cached ranking

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Related:** `references/protocols/skill-patterns.md` (Pattern 3), `references/protocols/routines.md`

## When to Use

- Between planning ceremonies, to keep the board clean without a human combing through every card

## When NOT to Use

- When you need the board actively re-prioritized for an upcoming ceremony — that's the slate-for-ceremony sibling pattern, not this hygiene pass

## Common Mistakes

- Writing directly to the board instead of emitting a checklist
- Grouping the checklist by card instead of by the UI action needed
- Flagging a deliberately terse or deliberately long-lived card as a problem
