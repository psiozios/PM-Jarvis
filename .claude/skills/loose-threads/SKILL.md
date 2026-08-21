---
name: loose-threads
description: Open-loop radar. Finds stalled two-way conversations the user may be dropping — across threads they're in and their own posts awaiting reply — verified before flagging, bucketed by age, framed as triage not a scorecard.
user-invocable: true
disable-model-invocation: false
---

## Quick Start

**What to provide:** Nothing required — sweeps a default window.

```
/loose-threads               → full re-sweep of the default window (14 days) across scoped channels
/loose-threads --window 30d  → widen the sweep
```

**What you get:** Open loops bucketed by age, each with a whose-court call, a `Checked:` line, and a real deep link. A follow-up task is proposed only where the next move is genuinely the user's.

**Time:** A few minutes — most of it reading threads to resolution, not scanning titles.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own.

## Context Routing

| Source | Location | What to Extract |
|--------|----------|------------------|
| Chat platform | `<CHAT_PLATFORM>` | Every thread/DM the user participated in within the window |
| Task tracker | `<TASK_TRACKER>` | Cross-check: is a loop already tracked as a ticket? |
| Email | `<EMAIL_SOURCE>` | Threads awaiting the user's reply or awaiting someone else's |
| Calendar | `<CALENDAR>` | Cross-check: did a loop resolve in a meeting instead of in-thread? |
| Sibling sweep | `action-sweep` output | Dedupe — don't re-flag something `action-sweep` already surfaced as an action item |


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected.

## Workflow

### 1. Full-window, from-scratch sweep

Re-sweep the entire window every run. Prior-run state marks items new-vs-carried for the user's benefit only — it never narrows what gets swept (see `references/protocols/skill-patterns.md` discipline #3).

### 2. Sweep both directions

- **Inbound:** someone asked the user something or mentioned them, no reply yet.
- **Outbound:** the user posted a question or ask, no reply received yet.

### 3. Classify whose court

For each candidate: **yours** (the user owes the next move), **theirs** (someone else owes it), or **no owner** (ambiguous — flag as low-confidence rather than force a call).

### 4. Verify before flagging

Open every candidate and read to resolution — a search hit is a pointer, not an answer (discipline #1). Cross-check the task tracker, calendar, and other threads: a thread with no in-channel reply but a resolved ticket, or a decision made live in a meeting, is not stalled. Emit a `Checked:` line per item naming what was cross-referenced (discipline #2). That line is a join, not a summary: it names a query the lookup log already carries, and where the log holds nothing for this item the line stands empty rather than being written from recall (`references/protocols/evidence-ledger.md`).

### 5. False-positive pass

A long-running thread with a healthy back-and-forth cadence is not automatically stalled just because it's old (discipline #7). Drop or downgrade anything that doesn't survive this check.

### 6. Dedupe against action-sweep

If `action-sweep` already surfaced the same item as an action item, don't re-flag it here — cross-reference its most recent output before finalizing the list.

### 7. Bucket by age

Fresh (0-2 days) / This week (3-7 days) / Aging (8-13 days) / Stale (14+ days).

### 8. Propose follow-ups

For "yours" items only, propose a task in `<TASK_TRACKER>` as a numbered list awaiting confirmation — never auto-created (discipline #4).

## Output Template

```markdown
# Loose Threads — <DATE>

## Fresh (0-2 days)
- **[<thread title>](<deep link>)** — <whose court>: <one line on what's owed>
  Checked: <cross-reference>

## This Week (3-7 days)
...

## Aging (8-13 days)
...

## Stale (14+ days)
...

## Proposed Follow-Ups
| Item | Next Move | Proposed Task |
|---|---|---|
| <thread> | Yours | <task title, ready on confirm> |
```

## Runs as a Routine

Natural fit for a scheduled routine — see `references/protocols/routines.md` and `setup/routine-setup.md`. `routines/example-daily-digest/SKILL.md` chains this skill last, after `meeting-prep` and `action-sweep`.

## Output Quality Self-Check

- [ ] Full window re-swept, not narrowed by prior-run state
- [ ] Both directions covered — inbound and the user's own outbound posts
- [ ] Every item has a real `Checked:` line joined to a logged query, not a placeholder
- [ ] No item duplicated from `action-sweep`'s most recent output
- [ ] Framing is non-accusatory — triage, not a scorecard
- [ ] Follow-ups proposed only for "yours" items, and only as a numbered list

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it three things: the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/action-sweep` -> when a thread carries an action item; dedupe against its output before flagging either
- `/daily-plan` -> when the surviving threads need sequencing into today
- `/chat-ingest` -> when a thread carries durable knowledge worth filing, not just a reply owed
- `/slack-message` -> when the next move on a thread is drafting the reply

## When to Use

- Periodically, to catch conversations the user might be unintentionally dropping

## When NOT to Use

- As a substitute for checking a single thread you already know needs a reply — this is for the ones you don't know about
- When `action-sweep` already covers today's need — the two overlap by design and dedupe against each other, but running both back to back on the same window is redundant

## Common Mistakes

- Flagging a thread as stalled without cross-checking whether it resolved elsewhere
- Narrowing the sweep window based on what a previous run already found
- Auto-creating follow-up tasks instead of proposing them
- Re-flagging something `action-sweep` already surfaced
