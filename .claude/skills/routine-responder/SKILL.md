---
name: routine-responder
description: Turn a routine's notification thread into a two-way conversation. Discovers reply threads from active routines, picks up genuine user replies, and continues the underlying skill treating the reply as input.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

**What to provide:** Nothing required. Run it standalone, or wire it as the on-reply continuation for any routine under `routines/`.

```
/routine-responder             → sweep all routine threads for unprocessed user replies
```

**What you get:** Any routine thread with a genuine, unprocessed reply from the user gets picked up, routed to its routine's continuation, and answered in-thread. Threads with nothing new are left untouched — silently.

**Time:** Seconds per thread. Cheap enough to poll frequently.

---

## Purpose

A routine (see `references/protocols/routines.md`) posts a notification and stops. Without this skill, that's a one-way broadcast. `routine-responder` is the receive side: it watches every routine's notification thread for a reply from the user and, when it finds one, continues the conversation — running the routine's skill again with the reply as input, or just answering the question directly.

This skill is example-worthy scaffolding, not a single-purpose tool: any routine that ships an "on-reply continuation" section can be picked up by this responder without a code change here.

---

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|-----------------|
| Routine thread pointers | `routines/*/.thread-pointer.json` | Which threads exist, one per active routine |
| Per-thread reply marker | `routines/*/.last-reply-processed` | The last reply this skill already handled, per thread |
| Routine definition | `routines/<name>/SKILL.md` | The routine's on-reply continuation, if it defines one |
| Notifier config | `config/notifier-example.md` (or your adapter) | Credentials and identity for reading/posting |

---

## Workflow

### 1. Discover threads

Glob `routines/*/.thread-pointer.json`. Each file maps a routine to its live notification thread(s). Build a worklist: one entry per (routine, thread).

### 2. Determine what's actionable

A message in a thread is actionable only if **all** of the following hold:

- It was authored by **the user** — never the bot's own messages (this is the loop-prevention check; a routine reading and reacting to its own posts is the primary failure mode this guards against).
- It is **newer than the bot's last message** in that thread.
- It is **newer than that thread's `.last-reply-processed`** marker.

If no thread has an actionable message: **stop silently.** Send nothing. Write nothing. A sweep that finds nothing to do produces zero output — no "nothing to report" message, no log noise.

### 3. Acknowledge

For each actionable message found, add a "thinking" reaction to it on pickup (signals to the user that it's been seen and is being worked). Swap to a "done" reaction once the reply is posted.

### 4. Route and continue

Identify which routine owns the thread. Check that routine's `SKILL.md` for an on-reply continuation section:

- **If the routine defines a continuation:** run it, treating the user's message as input to that continuation — not as a fresh invocation of the underlying skill from scratch.
- **If it's a plain question with no continuation defined:** answer conversationally, using full workspace and memory context, the same as any direct chat message would.

Inherit the action rules from the routine's own autonomy gate (`references/protocols/routines.md` discipline #7): anything outward-to-others (a message to someone besides the user, an email, a ticket) is draft-only here too — never sent automatically. Anything that would write to the user's own systems runs end-to-end only with unambiguous approval already on record; if approval is ambiguous, ask back in-thread rather than guessing.

### 5. Post and mark

Post the reply in-thread with the notifier's mention token (per `references/protocols/notifications.md` item 4 — this is a material update, so it notifies).

**Only after the send is confirmed:**
1. Advance `.last-reply-processed` for that thread to the message just handled.
2. Swap the reaction from "thinking" to "done."

If the send is not confirmed, leave the marker where it was — the next sweep retries this reply rather than silently dropping it.

### 6. State and cadence

This skill owns exactly one class of file: `.last-reply-processed`, one per thread. It never writes to a routine's own dated output or `.last-run-<period>` pointer — those belong to the routine, not the responder (one owner per file, per `routines.md` discipline #2).

Cadence: cheap to poll frequently (local, read-mostly, idle-cheap when nothing's actionable). Wire it to run on a short local interval, or trigger it manually.

---

## Output Quality Self-Check

Before finishing a sweep, verify:

- [ ] **No self-loop:** the bot's own prior messages were never treated as actionable input
- [ ] **Silent when idle:** if no thread had an actionable reply, nothing was sent and nothing was written
- [ ] **Correct thread routing:** each reply was matched to the routine that actually owns its thread
- [ ] **Outward drafts only:** anything destined for someone other than the user was drafted, not sent
- [ ] **Marker discipline:** `.last-reply-processed` only advanced after a confirmed send

---

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads this file's `evals.md` in a clean context window.

---

## Cross-Skill Links

**Before this:** any routine under `routines/` that has posted at least one notification

**After this:** none — this is the terminal step of a reply cycle

**Related:** `references/protocols/routines.md`, `references/protocols/notifications.md`, `setup/routine-setup.md`

## When to Use

- Any active routine's notification thread might have a user reply worth acting on

## When NOT to Use

- Before any routine has actually posted a notification (nothing to discover yet)

## Common Mistakes

- Treating the bot's own posts as actionable input (loop risk)
- Sending a "nothing found" message on an idle sweep instead of staying silent
- Advancing `.last-reply-processed` before the reply send is confirmed
- Sending an outward message (to someone other than the user) without a draft-and-confirm step
