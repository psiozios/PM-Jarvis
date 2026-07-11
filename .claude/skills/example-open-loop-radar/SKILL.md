---
name: example-open-loop-radar
description: "Example skill. Copy and adapt to your tools. Sweeps conversations and the user's own posts for two-way loops that may have stalled, verifies before flagging, and proposes follow-ups for items in the user's court."
disable-model-invocation: false
user-invocable: true
---

> **Example skill. Copy and adapt to your tools.** Every `<PLACEHOLDER>` below stands for a concrete tool or id in your own workspace. This is Pattern 1 (Open-Loop Radar) from `references/protocols/skill-patterns.md` — read that first for the mechanics this skill instantiates.

## Quick Start

**What to provide:** Nothing required — it sweeps a defined window by default.

```
/example-open-loop-radar               → sweep the default window (last 14 days) across configured channels
/example-open-loop-radar --window 30d  → widen the sweep window
```

**What you get:** A bucketed list of open loops — conversations or posts where a reply is owed, grouped by age, each with a `Checked:` line and a deep link. Items where the next move is genuinely the user's get a proposed follow-up task; nothing is created without confirmation.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own.

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Chat platform | `<CHAT_PLATFORM>` (e.g. your team chat tool) | Threads/DMs the user participated in within the sweep window |
| Task tracker | `<TASK_TRACKER>` (e.g. your issue tracker) | Cross-reference: does an existing ticket already cover this loop? |
| Sibling skill outputs | `outputs/` (prior radar runs, meeting notes) | Dedupe against items already surfaced (discipline #6) |
| User identity | `<USER_ID>` | Which messages/mentions count as "the user's" for inbound/outbound classification |

## Workflow

### 1. Sweep (comprehensive, not delta)

Query `<CHAT_PLATFORM>` for every thread or DM the user (`<USER_ID>`) participated in within the window (default 14 days). Re-sweep the **full** window every run — do not narrow based on what a prior run already surfaced (discipline #3).

### 2. Classify direction

For each thread, determine whose court the next move is in:
- **Inbound:** someone asked the user something or mentioned them, and the user hasn't replied.
- **Outbound:** the user posted something (a question, a request) and hasn't received a reply.

### 3. Verify before flagging

For each candidate loop, open it and read to resolution (discipline #1 — a search hit is a pointer, not an answer). Cross-check against `<TASK_TRACKER>`: is there already a ticket tracking this? Emit a `Checked: <what was cross-referenced>` line per item (discipline #2). A thread with no reply in-channel but a resolved ticket is not stalled — it moved elsewhere.

### 4. False-positive pass

Before including an item, apply the skeptic check (discipline #7): a long-running thread with a healthy back-and-forth cadence is not automatically stalled just because it's old. Drop or downgrade-to-low-confidence anything that doesn't survive this pass.

### 5. Bucket by age

Fresh (0-2 days) / This week (3-7 days) / Aging (8-13 days) / Stale (14+ days).

### 6. Propose follow-ups

For items where the next move is the user's, propose a task in `<TASK_TRACKER>` — as a numbered list, not an auto-create (discipline #4). Skip items sitting in someone else's court; those aren't the user's action item yet.

## Output Format

```markdown
# Open-Loop Radar — <DATE>

## Fresh (0-2 days)
- **[<Thread title>](<deep link>)** — <one line: what's owed, by whom>
  Checked: <tracker/other source cross-referenced>

## This Week (3-7 days)
...

## Aging (8-13 days)
...

## Stale (14+ days)
...

## Proposed Follow-Ups
| Item | Next Move | Proposed Task |
|---|---|---|
| <thread> | User's | <task title, ready to create on confirm> |
```

## Runs as a Routine

This pattern is a natural candidate for a scheduled routine (a standing radar). See `references/protocols/routines.md` and `setup/routine-setup.md` to wire this skill into a recurring, self-notifying routine instead of running it on demand.

## Output Quality Self-Check

- [ ] Full window re-swept, not narrowed by prior-run state
- [ ] Every item has a `Checked:` line naming a real cross-reference
- [ ] Every item has one real deep link
- [ ] Framing is non-accusatory (triage, not a scorecard)
- [ ] Follow-ups proposed only for items in the user's court, and only as a numbered list awaiting confirmation

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Related:** `references/protocols/skill-patterns.md` (Pattern 1), `references/protocols/routines.md`

## When to Use

- Periodically, to catch conversations the user might be unintentionally dropping

## When NOT to Use

- As a substitute for reading a single thread you already know needs a reply — this is for the ones you don't know about

## Common Mistakes

- Flagging a thread as stalled without cross-checking whether it resolved elsewhere
- Narrowing the sweep window based on what a previous run already found
- Auto-creating follow-up tasks instead of proposing them
