---
name: example-daily-digest
description: "Example skeleton. Copy and adapt to your tools. Runs a chosen skill on a schedule and reports back through a notifier."
disable-model-invocation: true
user-invocable: false
---

<!--
EXAMPLE ROUTINE. Copy this directory to `routines/<your-routine>/`, rename this
file's frontmatter `name`, and fill in every <PLACEHOLDER>. Do not run this
skeleton as-is — it has no real skill wired in.

This skeleton implements all eight disciplines from
`references/protocols/routines.md`. Read that file first; the comments below
point at which discipline each block satisfies but do not restate it.

State files this routine owns (discipline #2 — one owner per file):
  routines/<your-routine>/outputs/YYYY-MM-DD-<slug>.md   (dated output)
  routines/<your-routine>/.last-run-<period>              (already-ran guard)
  routines/<your-routine>/.thread-pointer.json             (notification thread — see notifications.md)
-->

## What This Routine Does

<ONE LINE: what skill or short chain this orchestrates, and why it runs on a schedule instead of on demand.>

Orchestrates: `/example-skill` (cite the skill — do not restate its internals here; see discipline #1 in `references/protocols/routines.md`).

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

Read whatever context the orchestrated skill's own Context Routing Logic table specifies. Do not duplicate that table here — read it from the skill.

### 4. Decide

Run `/example-skill` per its definition, passing the gathered context. Capture its output.

### 5. Execute

If the skill's output implies a write to the user's own systems (their own tracker, their own draft folder), apply the autonomy gate (discipline #7):

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
  body       = <rendered output summary>,
  notify     = <true if material update / blocking ask, false if no-op — item 4>,
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

This is an example skeleton, not a shipped skill — it has no `evals.md`. When you copy this into a real routine, give the *underlying skill* (`/example-skill` above) its own eval pass per `references/protocols/skill-evals.md`; the routine wrapper itself is not separately evaluated.

## Cross-Skill Links

- **Setup:** `setup/routine-setup.md` walks through copying and filling this skeleton
- **Reply handling:** `.claude/skills/routine-responder/` turns this routine's notification thread into a two-way conversation
- **Protocol:** `references/protocols/routines.md` (scheduling discipline), `references/protocols/notifications.md` (notifier contract)
