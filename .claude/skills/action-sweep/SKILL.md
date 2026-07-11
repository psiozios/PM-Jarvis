---
name: action-sweep
description: Sweep every connected source for the user's open action items since the last sweep, reconcile against the task tracker, and either execute internal-tool items end-to-end or propose the rest.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

**What to provide:** Nothing required — it sweeps since the last run by default.

```
/action-sweep               → sweep since .last-sweep, reconcile against the task tracker
/action-sweep --since 3d    → override the window
```

**What you get:** A numbered table of proposed new tasks and verified-done items. On approval, new tasks are created and done items are marked done in the task tracker end-to-end; anything outward-to-others stays a draft you send yourself.

**Time:** A few minutes, most of it reading sources in parallel.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own.

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Meeting notes | `outputs/meeting-notes/`, `context-library/meetings/` | Action items assigned to the user since last sweep |
| Chat platform | `<CHAT_PLATFORM>` | Both directions: asks directed at the user, and commitments the user made |
| Email | `<EMAIL_SOURCE>` | Threads where the user owes a reply or a deliverable |
| Calendar | `<CALENDAR>` | Meetings that likely produced commitments (cross-check against notes) |
| Issue tracker | `<TASK_TRACKER>` | Current open tasks, for dedupe and mark-done matching |
| Call-transcript source | `<CALL_TRANSCRIPT_SOURCE>` | Action items surfaced in calls not yet in meeting notes |
| Sweep state | `.last-sweep` (this skill's own state file) | Window start for "since last sweep" |

## Workflow

### 1. Determine the window

Read `.last-sweep`. If present, sweep from that timestamp to now. If absent (first run, or first run of the day with no prior timestamp), fall back to yesterday + today so nothing from an unswept prior day is silently missed.

### 2. Sweep every source, both directions

Pull candidate action items from every source in the routing table. For the chat platform and email specifically, sweep **both directions**: things asked of the user, and things the user committed to doing. Read every candidate thread to resolution — a search hit is a pointer, not an answer (see `references/protocols/skill-patterns.md` discipline #1).

### 3. Apply exclusions

Drop anything that's clearly not the user's action: FYI-only mentions, items explicitly delegated away, items already closed out in the same thread.

### 4. Verify live state

For each remaining candidate, check whether it's already been handled since it arose — cross-reference the task tracker, later messages in the same thread, and calendar follow-ups. An item resolved after the fact is marked **verified-done**, not surfaced as still-open (see `skill-patterns.md` discipline #2 — verify before surfacing).

### 5. Dedupe against the task tracker

Fuzzy-match each remaining candidate against currently open tasks in `<TASK_TRACKER>` by title/description similarity. A near-match is treated as the same item, not a duplicate proposal.

### 6. Present the reconciliation table

Show proposed new tasks and verified-done items as one numbered table (see Output Format). Nothing is written until this is approved.

### 7. Execute on approval

- **New tasks:** create in `<TASK_TRACKER>`.
- **Verified-done:** mark done in `<TASK_TRACKER>`.
- **Fully internal-tool-doable items** (the fix is entirely within a tool the user has authorized end-to-end use of): carry out the action, then mark done.
- **Outward-to-others** (a message, an email, a ticket reply, an invite): produce a draft only. Never send automatically.

### 8. Stamp

After the reconciliation is applied (or explicitly declined), write `.last-sweep` to the current timestamp — not before, so a partial or aborted run retries the same window next time.

## Output Format

```markdown
# Action Sweep — <DATE> (since <WINDOW START>)

## Proposed New Tasks
| # | Item | Source | Checked | Proposed Task |
|---|---|---|---|---|
| 1 | <what's owed> | <meeting notes / chat / email / call> | <cross-ref confirming it's still open> | <task title> |

## Verified-Done (no longer open)
| # | Item | Source | Resolved Via |
|---|---|---|---|
| 1 | <item> | <original source> | <where the resolution was found> |

## Drafts (outward-to-others — review before sending)
- <draft 1, ready to copy/send manually or via confirm>
```

## Runs as a Routine

This is a strong candidate for a scheduled routine — see `references/protocols/routines.md` and `setup/routine-setup.md`. `routines/example-daily-digest/SKILL.md` chains this skill after `meeting-prep`.

## Output Quality Self-Check

- [ ] Window correctly resolved from `.last-sweep`, with the first-run-of-day fallback applied when relevant
- [ ] Both directions swept on the chat platform and email, not just inbound
- [ ] Every verified-done item cites where the resolution was found
- [ ] Dedupe checked against currently open tracker items before proposing anything new
- [ ] Nothing was created or marked done without the reconciliation table being approved first
- [ ] Outward-to-others items are drafts, not sent messages
- [ ] `.last-sweep` only advanced after the run completed or was explicitly declined

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Related:** `daily-plan`, `loose-threads` (sibling radar — dedupe against its output), `meeting-notes`, `create-tickets`

## When to Use

- Daily or every few days, to catch action items scattered across sources before they slip

## When NOT to Use

- For a one-off "what did I commit to in this meeting" — use `meeting-notes` directly, it's cheaper for a single meeting

## Common Mistakes

- Sweeping only inbound asks and missing the user's own outbound commitments
- Surfacing an item as open when it was already resolved elsewhere
- Creating tasks or marking items done before the reconciliation table was approved
- Sending an outward message automatically instead of drafting it
