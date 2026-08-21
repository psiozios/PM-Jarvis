---
name: action-sweep
description: Sweep every connected source for the user's open action items since the last sweep, reconcile against the task tracker, and either execute internal-tool items end-to-end or propose the rest.
user-invocable: true
disable-model-invocation: false
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

## Context Routing

| Source | Location | What to Extract |
|--------|----------|------------------|
| Meeting notes | `outputs/meeting-notes/`, `context-library/meetings/` | Action items assigned to the user since last sweep |
| Chat platform | `<CHAT_PLATFORM>` | Both directions: asks directed at the user, and commitments the user made |
| Email | `<EMAIL_SOURCE>` | Threads where the user owes a reply or a deliverable |
| Calendar | `<CALENDAR>` | Meetings that likely produced commitments (cross-check against notes) |
| Issue tracker | `<TASK_TRACKER>` | Current open tasks, for dedupe and mark-done matching |
| Call-transcript source | `<CALL_TRANSCRIPT_SOURCE>` | Action items surfaced in calls not yet in meeting notes |
| Sweep state | `.last-sweep` (this skill's own state file) | Window start for "since last sweep" |


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected.

## Workflow

### 1. Determine the window

Read `.last-sweep`. If present, sweep from that timestamp to now. If absent (first run, or first run of the day with no prior timestamp), fall back to yesterday + today so nothing from an unswept prior day is silently missed.

### 2. Sweep every source, both directions

Pull candidate action items from every source in the routing table. For the chat platform and email specifically, sweep **both directions**: things asked of the user, and things the user committed to doing. Read every candidate thread to resolution — a search hit is a pointer, not an answer (see `references/protocols/skill-patterns.md` discipline #1).

### 3. Apply exclusions, on the record

Open the log and the ledger now, before any candidate is dropped — one appended line per lookup as it returns, one ledger row per candidate carrying its own targeted lookup, verbatim evidence, and verdict (`references/protocols/evidence-ledger.md`). FYI-only mentions, items explicitly delegated away, and items closed out in the same thread are `KILL` rows **with the evidence that killed them**. Anything you believe is excluded but cannot show is `UNPROVEN`, and an unproven kill is not a kill — it ships as a one-line question, since the run cannot show the item is live either.

### 4. Verify live state

For each remaining candidate, check whether it's already been handled since it arose — cross-reference the task tracker, later messages in the same thread, and calendar follow-ups. An item resolved after the fact is marked **verified-done**, not surfaced as still-open (see `skill-patterns.md` discipline #2 — verify before surfacing).

### 5. Dedupe against the task tracker

Fuzzy-match each remaining candidate against currently open tasks in `<TASK_TRACKER>` by title/description similarity. A near-match is treated as the same item, not a duplicate proposal. Fuzzy-matching is a pointer, not a verdict: record the matched task in the ledger row as the evidence, and where the match is only plausible, the row is `UNPROVEN` rather than `KILL`.

### 6. Deliver the questions, then the reconciliation table

Send the questions the moment they exist — they are what the user, and only the user, can answer, and they should not wait on the verification still running (`references/protocols/skill-patterns.md` discipline #10). Then show proposed new tasks and verified-done items as one numbered table (see Output Template). Nothing is written until that table is approved.

### 7. Execute on approval

- **New tasks:** create in `<TASK_TRACKER>`.
- **Verified-done:** mark done in `<TASK_TRACKER>`.
- **Fully internal-tool-doable items** (the fix is entirely within a tool the user has authorized end-to-end use of): carry out the action, then mark done.
- **Outward-to-others** (a message, an email, a ticket reply, an invite): produce a draft only. Never send automatically.

### 8. Stamp

After the reconciliation is applied (or explicitly declined), write `.last-sweep` to the current timestamp — not before, so a partial or aborted run retries the same window next time.

## Output Template

```markdown
# Action Sweep — <DATE> (since <WINDOW START>)

## Questions (shipped first — each is one line, and the run is blocked on nothing else)
- <the `UNPROVEN` item, as a question only the user can answer>

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
- [ ] Lookup log appended as each lookup returned, and every evidence cell joined back to a query in it
- [ ] Dedupe checked against currently open tracker items before proposing anything new
- [ ] Questions shipped ahead of the table, and no item appears in two sections
- [ ] Nothing was created or marked done without the reconciliation table being approved first
- [ ] Outward-to-others items are drafts, not sent messages
- [ ] `.last-sweep` only advanced after the run completed or was explicitly declined

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it three things: the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/loose-threads` -> when a swept item is a stalled conversation rather than an action; dedupe against its output before flagging either
- `/create-tickets` -> when a swept item needs to become a tracked ticket rather than a reply
- `/meeting-notes` -> when the sweep surfaces meeting commitments that were never written up
- `/daily-plan` -> when the surviving items need sequencing into today

## When to Use

- Daily or every few days, to catch action items scattered across sources before they slip

## When NOT to Use

- For a one-off "what did I commit to in this meeting" — use `meeting-notes` directly, it's cheaper for a single meeting

## Common Mistakes

- Sweeping only inbound asks and missing the user's own outbound commitments
- Surfacing an item as open when it was already resolved elsewhere
- Creating tasks or marking items done before the reconciliation table was approved
- Sending an outward message automatically instead of drafting it
