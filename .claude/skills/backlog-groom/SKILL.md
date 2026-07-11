---
name: backlog-groom
description: Whole-board hygiene pass over the issue tracker, strictly read-only. Triages stale, duplicate, ready-to-close, mis-prioritized, wrong-sprint, orphan, and thin items with hard false-positive discipline. Output is a UI-action checklist the user applies by hand.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

**What to provide:** Nothing required.

```
/backlog-groom               → whole-board hygiene pass
```

**What you get:** A checklist grouped by the click you'll make in the tracker UI — Close, Reorder, Re-allocate, Tag, Description-fix — with drafted replacement text inline. This skill never touches the board itself.

**Time:** A few minutes for a full board sweep.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own.

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Issue tracker | `<TASK_TRACKER>` | Full current board state: every item, status, description, age, assignee, sprint, epic/parent |
| Sprint context | `<TASK_TRACKER>` sprint field | Current sprint boundaries, for wrong-sprint detection |

## Workflow

### 1. Read the full board — never mutate it

Pull every item's current state from `<TASK_TRACKER>`. Strictly read-only: nothing in this skill writes back to the tracker (see `references/protocols/skill-patterns.md` discipline #8).

### 2. Triage each item across all dimensions

For every item, check each triage dimension:

- **Stale** — no activity in a long window, not just "old"
- **Duplicate** — genuinely overlapping scope with another open item
- **Ready-to-close** — already resolved, superseded, or no longer relevant
- **Mis-prioritized / mis-ordered** — priority or position doesn't match current reality
- **Wrong-sprint** — assigned to a sprint that's already closed, or clearly doesn't fit the current one
- **Orphan / mis-parented** — missing an epic/parent it should have, or parented under the wrong one
- **Thin epic** — an epic with no meaningfully scoped children
- **Thin description** — too vague to action without asking the author

### 3. Establish priority live

Judge priority and ordering from the board's current state at run time — never from a stale doc or an assumed prior ranking.

### 4. Apply hard false-positive discipline

Before flagging: a long-lived item is not automatically stale (check for a design reason it's meant to sit), a deliberately terse item is not automatically thin (check whether terseness was intentional for that item type), a similar-sounding item is not automatically a duplicate (check scope, not just title) — see discipline #7. Drop or downgrade anything that doesn't survive this check.

### 5. Draft the fix inline

For any text-based fix (a rewritten description, a suggested tag, a suggested parent), draft the replacement text directly in the checklist — ready to paste, not a note that it needs fixing.

### 6. Group by UI action

Group the output by the click the user will actually make, not by item — this matches how they'll work through it.

## Output Format

```markdown
# Backlog Hygiene Pass — <DATE>

## Close
- [ ] **[<item>](<link>)** — <why: duplicate of / resolved via / stale since>

## Reorder
- [ ] **[<item>](<link>)** — currently <position>, suggested <position> because <reason>

## Re-allocate
- [ ] **[<item>](<link>)** — currently <sprint/owner>, suggested <sprint/owner> because <reason>

## Tag / Re-parent
- [ ] **[<item>](<link>)** — add tag: `<tag>` / re-parent under: `<epic>`

## Fix Description
- [ ] **[<item>](<link>)**
  Current: "<current description, truncated>"
  Suggested: "<drafted replacement, ready to paste>"
```

## Runs as a Routine

Pairs naturally with `refinement-prep` on a recurring cadence — hygiene between ceremonies, slate before them. See `references/protocols/routines.md` and `setup/routine-setup.md`.

## Output Quality Self-Check

- [ ] Board was read, never written to
- [ ] Checklist grouped by UI action, not by item
- [ ] Every text-based fix has drafted replacement text ready to paste
- [ ] Every flagged item survived the false-positive check
- [ ] Priority judgments reflect the board's current live state, not a cached ranking

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Pairs with:** `refinement-prep` (runs off the cleaned board this skill produces)

**Related:** `sprint-planning` (`--groom` mode covers per-ticket INVEST readiness; this skill covers whole-board hygiene — run this first, then `sprint-planning --groom` for the tickets headed into the next sprint)

## When to Use

- Between planning ceremonies, to keep the board clean without a human combing through every item

## When NOT to Use

- When you need the board actively re-prioritized for an upcoming ceremony — that's `refinement-prep`

## Common Mistakes

- Writing directly to the tracker instead of emitting a checklist
- Grouping the checklist by item instead of by the UI action needed
- Flagging a deliberately terse or deliberately long-lived item as a problem without checking why it's that way
