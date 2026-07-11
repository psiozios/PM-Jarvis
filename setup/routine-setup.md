# Routine Setup

Guided walkthrough from "I want a recurring X" to a registered, notifying routine.

## Overview

This is the routine analog of `first-session-checklist.md` — it doesn't build a routine for you, it walks you through parameterizing the shipped example (`routines/example-daily-digest/`) the same way the first-session checklist walks you through the context-library templates.

This doc does not restate the underlying rules — it cites them. Read `references/protocols/routines.md` (scheduling discipline) and `references/protocols/notifications.md` (notifier contract) before or during this walkthrough; each step below points at the relevant section instead of repeating it.

**Time needed:** 20-30 minutes for the first routine.

---

## Step 1: Prerequisites

**What we're checking:** The automation layer is present and your notifier is configured.

```bash
ls references/protocols/routines.md references/protocols/notifications.md
ls config/notifier-example.md
ls routines/example-daily-digest/SKILL.md
```

All four should exist. Then confirm notifier credentials are set, per `setup/environment-keys.md` and `config/notifier-example.md`:

```bash
echo $<BOT_TOKEN_ENV_VAR_NAME>   # should print something — never share the output
```

Never print secret values into chat or commit them to a file. Confirming the variable is *set* (non-empty) is enough — don't echo it into a shared transcript.

✅ **Mark complete when:** all four files exist and your notifier's bot-token env var, user id, and channel are filled into your copy of `config/notifier-example.md`.

---

## Step 2: Pick what to schedule

**What we're deciding:** Which skill (or short chain of 2-3 skills) this routine orchestrates.

State the job in one line: "Every [period], run [skill] and tell me [what]." For example: "Every weekday morning, run the daily-plan skill and post the summary."

This reinforces the thin-wrapper rule (`references/protocols/routines.md` discipline #1) — the routine's job is scheduling and reporting, not reimplementing the skill. If the one-line job description starts describing *how* the skill works internally, that's a sign the routine is about to restate instead of cite.

✅ **Mark complete when:** you can state the routine's job in one sentence naming a specific existing skill.

---

## Step 3: Cadence and host

**What we're deciding:** How often it fires, and whether it runs in the cloud or locally.

- **Period:** daily, weekly, monthly, quarterly, or a custom cron.
- **Host:** cloud (default) or local. Local is the interim option only for work-hours sub-hourly cadence or in-session back-and-forth — see `references/protocols/routines.md` discipline #5.
- **Cron:** write the expression, apply the day-of-week guard from discipline #6 (prefer daily cron + in-prompt day-skip over unreliable day-of-week lists), and verify the scheduler's *computed* next-run time — not its display label. If this is a one-time fire-at task, remember it will not self-re-arm; use a recurring cron if it needs to repeat.
- **Timezone:** confirm the schedule computes in the machine's local timezone (discipline #8), not a hardcoded zone.

✅ **Mark complete when:** you've written down the period, host choice (with a one-line "why"), and cron expression, and verified the next-run time the scheduler actually computed.

---

## Step 4: Copy and fill the template

**What we're doing:** Turning the example into your routine.

```bash
cp -r routines/example-daily-digest routines/<your-routine>
```

Or start from the blank `templates/routine-template.md` if you'd rather build from an unfilled skeleton than adapt the worked example.

Fill in:
- The ordered step skeleton (bind rules → guard → gather → decide → execute → deliver → stamp)
- The skill citation from Step 2
- State files this routine owns: dated output path, `.last-*` guard file(s), thread pointer — one owner per file (discipline #2)
- The SENDING and THREADING blocks (see Step 5)
- Replace every `<USER_ID>` placeholder with your real target

✅ **Mark complete when:** `routines/<your-routine>/SKILL.md` has no placeholder text left and cites a real skill by name.

---

## Step 5: Wire the notification

**What we're doing:** Connecting the routine to your notifier.

- **Identity:** bot identity posting to the user's own surface — self-notification, never "send as the user" (`notifications.md` item 1).
- **Anchor rotation:** confirm the thread-pointer logic mints a fresh anchor per period and reuses it for same-period checkpoints (item 3).
- **Notify semantics:** material updates get the mention token; no-ops stay silent (item 4).

✅ **Mark complete when:** the SENDING/THREADING blocks in your routine's `SKILL.md` reference your real notifier config, not the example placeholders.

---

## Step 6: Register the schedule

**What we're doing:** Making the routine actually fire.

Register the cron with your scheduler — a cloud-routine scheduling UI if hosting in the cloud, or your local cron/scheduler if hosting locally. This template does not hardcode a specific platform here; use whatever scheduling mechanism your environment provides.

Verify the next-run time the scheduler reports, the same way you verified it in Step 3 — schedulers sometimes compute a different next-run than their label implies.

✅ **Mark complete when:** the schedule is registered and you've independently verified its computed next-run time.

---

## Step 7: First-fire verification

**What we're testing:** The routine actually behaves per the eight disciplines on a real run.

Trigger the routine once (manually, or wait for its first scheduled fire) and confirm:

- [ ] The self-notification lands in the expected thread
- [ ] The dated output file and `.last-*` pointer were written **only after** the notification was confirmed delivered — not before
- [ ] If run headless/unattended, any write-to-others call (message to someone besides you, ticket, shared doc edit) was blocked and stopped rather than sent
- [ ] Catch-up-on-wake works: clear the `.last-*` pointer, re-run, and confirm it produces a fresh run for the owed period rather than skipping

✅ **Mark complete when:** all four checks pass on a real trigger.

---

## Step 8 (Optional): Make it two-way

**What we're doing:** Letting you reply to the routine's notification and get a response.

Wire `.claude/skills/routine-responder/` to poll your new routine's thread. See that skill's `SKILL.md` for what counts as an actionable reply and how it routes back to your routine's continuation.

✅ **Mark complete when:** a test reply in the routine's thread gets picked up and answered.

---

## Next Steps

- Add another routine by repeating from Step 2
- If a routine's reporting cadence needs to change, revisit Step 3 — don't hand-edit the `.last-*` guard files directly
- See `references/protocols/skill-patterns.md` — several of the reusable skill archetypes there are natural routine candidates
