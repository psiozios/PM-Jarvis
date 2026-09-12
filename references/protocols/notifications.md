# Notifications Protocol

**Principle: NOTIFICATIONS ARE OUTPUT, ADDRESSED TO A NOTIFIER INTERFACE — NEVER A HARDCODED PLATFORM CALL.**

Routines (see `references/protocols/routines.md`) report back through notifications. This protocol defines the provider-agnostic contract every notifier adapter must satisfy, plus one labeled reference implementation for Slack. Nothing in `routines/` or the core template should call a platform API directly — it calls the interface below, and the adapter underneath can be swapped without touching a single routine.

## The Contract

### 1. Identity

Post from a **bot identity** to the **user's own surface** — a self-notification. Never use a "send as the user" API, and never post to a shared or public surface unless the routine explicitly exists to do that (rare; state it if so).

Credentials, the user's id, and the target channel/surface come from config or environment variables — never hardcoded into a routine prompt, never printed to logs or chat output.

### 2. Idempotent single send

Compose once, send once. Confirm delivery by reading the transport's success signal **defensively from the raw response bytes** — many transports echo the message text back in the response, and a parse hiccup on that echoed field is not the same thing as a failed send. Distinguish the two before deciding to resend.

Resend at most once, and only on a genuine failure signal (non-2xx status, explicit error field, connection failure) — never on an ambiguous parse. Two confirmed sends for one intended notification is a bug, not a safety margin.

### 3. Render before you post

**The reader's own copy has to exist before the notification pointing at it does.** A tool call completes before your prose does, so posting first means the notification lands — often on a phone — while the conversation still shows nothing. The reader arrives to an empty room.

Order every checkpoint: finish the work, write the dated output, **render the summary in the conversation**, then make the outbound call, then stamp the marker on confirmation. Each step exists before the thing that announces it.

This holds per checkpoint, not per run. A routine that pings twice in a period renders the second summary before posting the second reply, the same as the first.

### 4. Per-period anchor rotation

Each routine posts in its own thread. The anchor message for that thread rotates **per period** — there is no single permanent anchor a routine reuses forever.

- **Daily routines:** thread pointer is keyed `<period>|<anchor-id>`. The first checkpoint of a given day mints a fresh anchor and saves it under that day's key. Any later checkpoint the same day reuses the saved anchor.
- **Weekly / monthly / quarterly routines:** mint a fresh anchor every run — there is no "later checkpoint, same period" case for these cadences under normal use.

The anchor's own text carries the period's date, so the thread is self-describing even out of context (e.g. "Daily Digest — 2026-07-11").

### 5. Notify semantics

A threaded reply by itself may not trigger a notification on every platform. A main-surface broadcast is too noisy for routine, low-signal updates. Use a targeted **mention token** in the reply body when it should notify, and omit it when it shouldn't:

- **Notify (tag):** a run summary worth seeing, a blocking ask, a deliverable that was applied, an approval that resolved.
- **Silent (no tag):** a no-op run, an FYI with nothing actionable.

### 6. Per-checkpoint markers

A routine that pings more than once per period (e.g. a morning check and an afternoon follow-up on the same day) writes a **per-checkpoint marker** after each confirmed delivery — not just one marker for the whole period. This lets it notify multiple times in a period without either duplicating a checkpoint it already sent or skipping one it hasn't.

**The marker is written on the transport's confirmation and on nothing else.** Not when the body is composed, not when the output file lands, not when the send is issued — when the transport says it arrived, read defensively per item 2. Anything earlier means a run can die between the write and the delivery and answer already-ran forever, with silence as the only symptom (`references/protocols/routines.md` discipline #2).

`.claude/skills/routine-responder/` is the worked instance: one marker class, one per thread, advanced only after the reply send is confirmed, left where it was on any failure.

### 7. Prune the thread pointer against its source, behind a count gate

The thread pointer is a **copy-only snapshot**: every entry is a local note about a thread the platform owns. It gains one key per period and nothing ever removes one, so a daily routine accumulates a few hundred dead keys a year, and `routine-responder` globs all of them on every sweep.

Prune it, but only against the source and only when the source is believable:

1. **List the routine's live threads from the platform.**
2. **Gate on the count.** If the listing is empty, or implausibly smaller than the number of keys held, **skip the prune entirely and say so.** A source that just failed auth returns few or no threads, and a prune run against that answer deletes every pointer the routine has — a self-inflicted total loss that looks exactly like a successful cleanup. Preflight state feeds this gate directly: a source that is `bad` or `missing` never authorizes a prune (`references/protocols/source-preflight.md`).
3. **Remove only keys whose thread the source confirms is gone**, and only for periods already closed. Never touch the current period's key.

Deleting a key that should have stayed costs the thread's history. Keeping one that should have gone costs a line in a file. Prune conservatively.

### 8. Self-heal

If the anchor message or thread is gone (deleted, expired, "not found" on send): re-post a fresh anchor, overwrite the thread pointer with the new one, and retry the reply exactly once against the new anchor. Do not loop indefinitely on a self-heal retry.

## Reference Implementation: Slack

**This is a reference implementation. Swap it for your own platform's adapter — nothing in the core template is Slack-specific.**

| Contract item | Slack mapping |
|---|---|
| Post message + threaded reply | `chat.postMessage` (new anchor) / `chat.postMessage` with `thread_ts` set to the anchor's `ts` (threaded reply) |
| Add reaction | `reactions.add` with the anchor or reply's `channel` + `timestamp` |
| Thread-id field | Slack's `ts` (timestamp string) doubles as the thread identifier — store it verbatim in the thread pointer |
| Success signal from raw bytes | Parse the top-level `"ok": true/false` field from the raw JSON body; do not fail the send solely because the echoed `"text"` field differs from what was sent (formatting/escaping differences are expected, not failures) |
| Bot token from env | Read from the environment variable named in `config/notifier-example.md`, never inline in a prompt or committed file |
| User-id-as-channel | A Slack user id used directly as the `channel` parameter opens/reuses that user's DM with the bot — this is the self-notification surface |
| Mention token | `<@USER_ID>` inside the message body triggers Slack's native notification for that user |

## Configuration

Notifier identity and credentials live in `config/notifier-example.md` (a separate labeled stub, not `config/settings-template.json` — that file is strict JSON with no room for inline documentation). Copy it, fill in the placeholders, and point your adapter at it.

## Cross-Reference

- `references/protocols/routines.md` — the scheduling discipline that calls this contract's `send` interface from its SENDING/THREADING blocks
- `routines/example-daily-digest/SKILL.md` — a worked example calling the interface described here
- `setup/routine-setup.md` — guided setup that wires notifier config into a new routine
