---
name: chat-ingest
description: Pull high-signal threads from the chat platform into the second-brain knowledge base. Filters for signal, previews before writing, routes each thread to the right focus area. Modes for channel sweep, topic search, catch-up ranking, DM-to-stakeholder mapping, and daily catch-all.
user-invocable: true
disable-model-invocation: false
---

## Quick Start

**What to provide:** A mode, or let it default to a daily catch-all.

```
/chat-ingest                        → daily catch-all: sweep since last ingest, filter for signal
/chat-ingest channel <name>         → sweep one channel fully
/chat-ingest topic "<search term>"  → pull everything matching a topic
/chat-ingest catch-up               → ranked history for catching up after time away
/chat-ingest dm-threads             → map DM threads to stakeholder profiles
```

**What you get:** A preview of high-signal threads and where each would file in the second brain — nothing is written until you confirm.

**Time:** A few minutes depending on mode and window.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own. Integrates with `second-brain` — this skill is the chat-platform-specific ingestion path into it. Signal-filtering drops candidates, so discipline #9 of `references/protocols/skill-patterns.md` binds: ledger first, discarded threads carry their evidence, and an unproven discard is not a discard.

## Context Routing

| Source | Location | What to Extract |
|--------|----------|------------------|
| Chat platform | `<CHAT_PLATFORM>` | Threads matching the selected mode's scope |
| Second brain | `context-library/second-brain/*/wiki/index.md` | Existing pages, to avoid re-ingesting the same content twice |
| Stakeholder profiles | `context-library/second-brain/stakeholders/` | For `dm-threads` mode: mapping a DM partner to their existing profile |
| Ingest state | `.last-ingest` (this skill's own state file) | Window start for the daily catch-all mode |


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected.

## Workflow

### 1. Resolve scope from mode

- **Daily catch-all:** sweep since `.last-ingest`, all scoped channels.
- **Channel sweep:** full history of one named channel (bounded by a reasonable lookback if the channel is large).
- **Topic search:** search across all scoped channels for the given term.
- **Catch-up:** rank recent activity by signal so returning from time away starts with what matters, not chronological scroll.
- **DM-threads:** sweep DM threads and match each partner to a `stakeholders` profile.

### 2. Filter for signal

Not every thread is worth ingesting. Filter on: thread length (a real discussion, not a one-line ack), decision language ("let's go with," "we decided," "the plan is"), and substance (concrete claims, not small talk). Discard low-signal matches before they ever reach the preview.

### 3. Preview before writing

Show the filtered candidates and, for each, which second-brain focus area it would route to and why. Nothing is ingested until the user confirms — this mirrors `second-brain`'s own ingest discipline (propose, don't auto-write).

### 4. Route to the right focus area

Match each confirmed thread's content to the most relevant existing focus area under `context-library/second-brain/`. If none fits, flag it rather than forcing it into the wrong wiki.

### 5. Ingest on confirm

Hand off confirmed threads to `second-brain`'s own `ingest` mode, one at a time per its own discipline (discuss takeaways, don't batch blindly) — see the `second-brain` skill for the full ingest workflow this triggers.

### 6. Stamp

After a daily catch-all run completes (or is explicitly declined), write `.last-ingest` to the current timestamp.

## Output Template

```markdown
# Chat Ingest Preview — <mode>, <DATE>

| # | Thread | Signal | Routes To | Why |
|---|---|---|---|---|
| 1 | <deep link> | <decision / substantive discussion> | `<focus-area>` | <one line> |

Confirm which to ingest (all / by number / none).
```

## Runs as a Routine

The daily catch-all mode is a natural routine candidate — see `references/protocols/routines.md` and `setup/routine-setup.md`. On-demand for the other modes.

## Output Quality Self-Check

- [ ] Low-signal threads (acks, small talk) were filtered out before the preview
- [ ] Every candidate shows its proposed focus-area routing and why
- [ ] Nothing was ingested before the user confirmed
- [ ] `dm-threads` mode correctly matched partners to existing stakeholder profiles where one exists
- [ ] `.last-ingest` only advanced after the daily catch-all run completed or was declined

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it three things: the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/second-brain` -> hands off here; its `ingest` mode does the actual wiki write
- `/loose-threads` -> when a thread is an open loop awaiting your reply, not knowledge to capture
- `/action-sweep` -> when a thread carries an action item rather than durable signal
- `/meeting-prep` -> when the ingested context is needed for a specific upcoming meeting

## When to Use

- Regularly, to keep the second brain current with what's actually being discussed on the chat platform

## When NOT to Use

- For finding action items or stalled replies — use `action-sweep` or `loose-threads`, which read the same platform for a different purpose

## Common Mistakes

- Ingesting low-signal threads (small talk, one-line acks) that add noise to the wiki
- Writing to the second brain before the preview was confirmed
- Forcing a thread into a focus area it doesn't actually fit instead of flagging it
