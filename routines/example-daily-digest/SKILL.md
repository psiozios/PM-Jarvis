---
name: example-daily-digest
description: "Example routine. Copy and adapt to your tools. Chains meeting-prep, action-sweep, and loose-threads on a daily schedule and reports one digest back through a notifier."
disable-model-invocation: true
user-invocable: false
---

<!--
EXAMPLE ROUTINE. Copy this directory to `routines/<your-routine>/`, rename this
file's frontmatter `name`, and fill in every remaining <PLACEHOLDER> (notifier
identity and cron schedule are still workspace-specific). The three skills
below are real, shipped skills — this routine is runnable as-is once your
notifier config and tool placeholders in those skills are filled in.

This skeleton implements all eight disciplines from
`references/protocols/routines.md`. Read that file first; the comments below
point at which discipline each block satisfies but do not restate it.

State files this routine owns (discipline #2 — one owner per file):
  routines/example-daily-digest/outputs/YYYY-MM-DD-digest.md   (dated output)
  routines/example-daily-digest/.last-run-<period>              (already-ran guard)
  routines/example-daily-digest/.thread-pointer.json             (notification thread — see notifications.md)
-->

## What This Routine Does

A morning digest that chains three real skills in sequence — prep for the day's meetings, reconcile action items, then check for stalled threads — and reports one consolidated summary back through the notifier instead of three separate ones.

Orchestrates, in order (cite each skill — do not restate its internals here; see discipline #1 in `references/protocols/routines.md`):
1. `.claude/skills/meeting-prep/SKILL.md` — prep for the day's next meeting
2. `.claude/skills/action-sweep/SKILL.md` — reconcile open action items since the last sweep
3. `.claude/skills/loose-threads/SKILL.md` — open-loop radar for stalled conversations

## Schedule

- **Period:** <daily | weekly | monthly | quarterly | custom cron>
- **Host:** <cloud (default) | local — state which and why, per discipline #5>
- **Cron expression:** `<CRON_EXPRESSION>` — verify the scheduler's *computed* next-run time, not its label (discipline #6)
- **Timezone:** machine-local, computed at run time — never hardcoded (discipline #8)

## Step Skeleton

Every run executes these steps in order. Do not reorder; do not skip the guard.

### 1. Bind rules

Read `references/protocols/routines.md` and `references/protocols/notifications.md` into context. Read `config/notifier-example` (or your real notifier config) for credentials and identity — never print secret values.

### 2. Guard (idempotency check — discipline #3)

Compute today's period key in local time (discipline #8). Check `.last-run-<period>` against that key.

- If the key matches an already-recorded run for this period: STOP. Do not re-run. Do not consult chat history, prior notifications, or downstream tool state to make this decision — local state only.
- If the key is missing, older than the current period, or was cleared: proceed. This also covers catch-up-on-wake (discipline #4) — a missed period runs on next wake, keyed to the period it was owed for, not the day the routine happens to wake up.

### 3. Gather

Each of the three skills reads its own context per its own Context Routing Logic table. Do not duplicate those tables here — read them from the skills.

### 4. Decide (run the chain in order)

Run `meeting-prep` per its definition. Then run `action-sweep` per its definition. Then run `loose-threads` per its definition. Capture each skill's output section — this routine does not reimplement any of their internal logic, it just sequences them and combines what they produce into one digest body.

If `meeting-prep` finds no upcoming meeting today, note that plainly and continue to `action-sweep` — a skipped section is not a failed run.

### 5. Execute

If any skill's output implies a write to the user's own systems (their own tracker, their own draft folder — e.g. `action-sweep`'s task creation/mark-done step), apply the autonomy gate (discipline #7):

- Standing approval already granted for this specific routine → apply the write.
- No standing approval → list the proposed write and stop. Do not guess.
- Under no circumstances call a write-to-others tool (message to anyone but <USER_ID>, email, ticket, shared doc edit, calendar invite) unattended. That class of call is blocked at the tool layer regardless of what this prompt says.

### 6. Deliver (see SENDING block below)

### 7. Stamp

Only after the notification send is CONFIRMED (per `notifications.md` item 2):

1. Write the dated output file.
2. Advance `.last-run-<period>` to the current period key.

If the send is not confirmed, do not write either file — next wake retries this period from scratch (discipline #2).

## SENDING

<!--
Calls the notifier INTERFACE, not a platform API directly. See
references/protocols/notifications.md for the full contract. Swap in your
adapter (Slack reference adapter provided) without touching this routine.
-->

```
notifier.send(
  identity   = <BOT_IDENTITY>,          # bot identity, never "send as the user"
  target     = <USER_ID>,               # the user's own surface — self-notification only
  thread_key = "<period>|<anchor-id>",  # per-period anchor rotation — see notifications.md item 3
  body       = <meeting-prep summary> + <action-sweep summary> + <loose-threads summary>,  # one digest, three sections
  notify     = <true if any section has a material update / blocking ask, false only if all three were no-ops — item 4>,
)
```

Read the transport's success signal defensively from the raw response bytes before treating the send as confirmed (item 2). A parse error on an echoed field is not a send failure.

## THREADING

<!--
Anchor rotation: mint a fresh anchor at the first checkpoint of each period;
later checkpoints in the same period reuse it. Daily → new anchor every day.
Weekly/monthly/quarterly → new anchor every run (item 3).
-->

```
if .thread-pointer.json has no entry for current period key:
    anchor = notifier.post_new_thread(target=<USER_ID>, title="<period date>")
    save .thread-pointer.json[period_key] = anchor.thread_id
else:
    anchor = load .thread-pointer.json[period_key]

notifier.reply_in_thread(anchor.thread_id, body, notify=<see SENDING>)
```

If the anchor was deleted (thread/message not found on send), re-post per `notifications.md` item 6: mint a new anchor, overwrite the pointer, retry the reply once.

## Formal Eval

This is a routine wrapper, not a skill — it has no `evals.md` of its own. Each orchestrated skill (`meeting-prep`, `action-sweep`, `loose-threads`) carries its own eval pass per `references/protocols/skill-evals.md`, run when that skill executes as part of this chain. The routine wrapper itself is not separately evaluated.

## Cross-Skill Links

- **Orchestrates:** `meeting-prep`, `action-sweep`, `loose-threads` — in that order
- **Setup:** `setup/routine-setup.md` walks through copying and adapting this routine
- **Reply handling:** `.claude/skills/routine-responder/` turns this routine's notification thread into a two-way conversation
- **Protocol:** `references/protocols/routines.md` (scheduling discipline), `references/protocols/notifications.md` (notifier contract)
