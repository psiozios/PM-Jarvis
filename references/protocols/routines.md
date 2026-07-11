# Routines Protocol

**Principle: A ROUTINE IS A SCHEDULE WRAPPED AROUND A SKILL, NOT A NEW SKILL.**

A routine turns an existing skill (or short chain of skills) into something that fires on a schedule, checks its own state, and reports back through a notification. This protocol is the discipline every routine follows, regardless of what it schedules or how often it fires.

See `references/protocols/notifications.md` for the outbound-notification contract routines use to report back, and `setup/routine-setup.md` for the guided walkthrough that turns this protocol into a working routine.

## The Eight Disciplines

### 1. Thin wrapper

A routine's prompt is an ordered sequence of steps — bind rules, guard, gather, decide, execute, deliver, stamp. Those steps ORCHESTRATE existing skills; they never restate a skill's internals.

The routine owns the scheduling contract (when it runs, what state it checks, how it reports). The skill owns the method (how the work actually gets done). Cite the skill — "run `/example-skill` per its definition" — and stop there. Restating a skill's steps inside a routine prompt is the anti-pattern: it wastes tokens on every fire and drifts out of sync the moment the skill changes.

### 2. State-file discipline

Each routine owns its own state, and only its own state:

- A dated output (the artifact the run produced)
- One or more `.last-*` pointer files (what "already ran" means)
- A thread pointer (where its notifications live — see `notifications.md`)

One owner per file. Never let two routines write the same state file.

Write the dated output and advance the `.last-*` pointer **only after a confirmed notification send**. This ordering matters in both directions: a missed stamp (notification failed) cannot cause a false "already ran," so the routine retries next wake instead of silently going dark. And a cleared state directory (user wants a fresh start) always produces a fresh run, because there is nothing local telling the routine otherwise.

### 3. Idempotency from local state only

"Did this already run?" is answered from local state files — never from chat history, a prior bot message, a reply the user sent, or the contents of a downstream tool (calendar, tracker, inbox).

The notification surface is OUTPUT. It is never INPUT to the idempotency check. If a run's notification is visible in the chat thread but the local `.last-*` pointer was cleared or never written, the routine runs fresh and — if the content is unchanged — sends a duplicate-looking notification rather than silently skipping. That's the correct failure mode: a duplicate notification is recoverable (the user ignores it); a silently skipped run is not (the user has no way to know it didn't happen).

### 4. Catch-up on wake

A routine that missed its scheduled fire (laptop closed, process restarted, cron didn't trigger) runs its missed occurrence the next time it wakes — but keyed to the intended PERIOD, not the fire date.

Guard by the period's dated output, not by day-of-week. A daily routine that should have fired Tuesday but wakes Wednesday morning still owes Tuesday's output if Tuesday's dated file doesn't exist yet — it does not silently skip to today and pretend Tuesday never happened.

### 5. Cloud default, local interim

Two hosting choices, stated explicitly for every routine — never left implicit:

- **Cloud** (server-side scheduling) is the default. It fires even when the local machine is closed, and its minimum practical interval is roughly an hour.
- **Local** (a cron or scheduler on the user's own machine, or an in-session interval) is the interim option for two cases only: work-hours sub-hourly cadence, or in-session back-and-forth where the user is actively present.

State which one a given routine uses and why. Don't default silently — an unstated hosting choice is how routines quietly stop firing when a laptop sleeps.

### 6. Cron gotchas

Day-of-week ranges and lists (`MON-FRI`, `MON,WED,FRI`) are unreliable across some schedulers. Prefer a **daily cron plus an in-prompt day-skip guard** for anything except a contiguous weekday range that the target scheduler is verified to support.

Always verify the scheduler's **computed next-run time**, not the human-readable label it displays — labels lie more often than computed timestamps. One-time "fire-at" tasks auto-disable after firing and do not self-re-arm; if a routine needs to recur, it must use a recurring cron, not a chain of one-time fires.

### 7. Autonomy gate

Headless (unattended) routines get broad read access and local shell access by default. Write-to-others tools — messages to anyone but the user, email sends, ticket creation, edits to shared docs, calendar invites — are **not** on the unattended autonomy allowlist. Calling one blocks and prompts, every time, run headless or not.

The only permitted outbound action for an unattended routine is its own self-notification (see `notifications.md`). Writes to the user's own systems (their own task list, their own draft folder) run end-to-end only when the user has given explicit standing approval for that specific routine. Absent that approval, an unattended run lists the proposed writes and stops — it does not guess that silence means yes.

This is enforced at the tool layer, not by the routine's prompt. A routine prompt that says "don't message anyone" is a suggestion; a tool-layer allowlist is a guarantee.

### 8. Timezone-portable

Compute ALL time in the machine's local timezone — never a hardcoded zone. This covers every time-sensitive decision a routine makes: the day-key used for the dated output filename, the already-ran guard, the weekday/weekend skip, period boundaries (start/end of day, week, month, quarter), read windows ("last 24 hours"), and any timestamp displayed to the user.

A routine hardcoded to UTC (or to the timezone of whoever wrote it) silently misfires for a user in a different timezone — it fires at the wrong wall-clock hour, or worse, computes the wrong day-key entirely near midnight.

## Worked Example

`routines/example-daily-digest/SKILL.md` is a fully commented skeleton implementing all eight disciplines. Copy it as the starting point for a new routine — see `setup/routine-setup.md` for the guided walkthrough.

## Durable Enforcement

Five of the disciplines above are easy to silently regress on once a routine has shipped: cloud-default, catch-up-on-wake, thin-wrapper, notify-by-mention (see `notifications.md`), and local-timezone. Each may optionally be mirrored as a `feedback_` memory entry via the format in `memory/feedback_example.md`, so the per-turn memory hook reinforces it even outside an active routine-authoring session.

This protocol seeds no real `feedback_` entry — that would assert a rule before the user has a routine to apply it to. When the user's first routine goes live, propose the relevant mirrors per the knowledge-capture protocol (propose, don't auto-write).
