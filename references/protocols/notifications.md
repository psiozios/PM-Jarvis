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

### 3. Per-period anchor rotation

Each routine posts in its own thread. The anchor message for that thread rotates **per period** — there is no single permanent anchor a routine reuses forever.

- **Daily routines:** thread pointer is keyed `<period>|<anchor-id>`. The first checkpoint of a given day mints a fresh anchor and saves it under that day's key. Any later checkpoint the same day reuses the saved anchor.
- **Weekly / monthly / quarterly routines:** mint a fresh anchor every run — there is no "later checkpoint, same period" case for these cadences under normal use.

The anchor's own text carries the period's date, so the thread is self-describing even out of context (e.g. "Daily Digest — 2026-07-11").

### 4. Notify semantics

A threaded reply by itself may not trigger a notification on every platform. A main-surface broadcast is too noisy for routine, low-signal updates. Use a targeted **mention token** in the reply body when it should notify, and omit it when it shouldn't:

- **Notify (tag):** a run summary worth seeing, a blocking ask, a deliverable that was applied, an approval that resolved.
- **Silent (no tag):** a no-op run, an FYI with nothing actionable.

### 5. Per-checkpoint markers

A routine that pings more than once per period (e.g. a morning check and an afternoon follow-up on the same day) writes a **per-checkpoint marker** after each confirmed delivery — not just one marker for the whole period. This lets it notify multiple times in a period without either duplicating a checkpoint it already sent or skipping one it hasn't.

### 6. Self-heal

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
