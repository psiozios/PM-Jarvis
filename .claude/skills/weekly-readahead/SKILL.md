---
name: weekly-readahead
description: Draft a weekly read-ahead for a recurring cross-team meeting from the week's shipped work, decisions, risks, and metrics, each section carrying a clear so-what rather than an activity dump. Configurable section set. Publishes to the shared docs hub only after you confirm the draft.
user-invocable: true
disable-model-invocation: false
---

## Quick Start

**What to provide:** Which recurring meeting this read-ahead is for, and its section set if this is the first run (subsequent runs reuse the configured set).

```
/weekly-readahead "<meeting name>"               → draft using the configured section set
/weekly-readahead "<meeting name>" --sections "<Section A, Section B, ...>"  → set or override sections
```

**What you get:** A drafted read-ahead pulling from the week's shipped work, decisions, risks, and metrics — each section carrying a clear so-what, not a raw activity dump. Published to the shared docs hub on confirmation.

**Time:** A few minutes.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own. Section set is configurable per meeting — this skill does not hardcode a fixed org structure or a fixed list of sections.

## Context Routing

| Source | Location | What to Extract |
|--------|----------|------------------|
| Task tracker | `<TASK_TRACKER>` | Work shipped this week |
| Decisions | `context-library/decisions/`, `outputs/decisions/` | Decisions made this week |
| Metrics | `<METRICS_SOURCE>` | Movement worth reporting |
| Meeting notes | `outputs/meeting-notes/` | Risks or blockers surfaced this week |
| Docs hub | `<DOCS_HUB>` | Where the read-ahead publishes, and the prior week's read-ahead for continuity |


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected.

## Workflow

### 1. Resolve the section set

If this is the first run for this meeting, ask for the section set (or accept `--sections`). Store it for reuse on subsequent runs so the format stays consistent week over week — this skill does not assume a fixed set of sections across all meetings, since different recurring meetings care about different things.

### 2. Pull the week's substance

For each configured section, pull the relevant material: shipped work from `<TASK_TRACKER>`, decisions from `context-library/decisions/`, metric movement from `<METRICS_SOURCE>`, risks from recent meeting notes.

### 3. Write a so-what per section

Every section leads with why it matters to this specific audience, not a bare list of what happened. A shipped-work bullet without an impact statement is incomplete.

### 4. Draft, then publish on confirm

Show the drafted read-ahead. Publish to `<DOCS_HUB>` only after confirmation — this is content visible to others, so it follows the outward-draft-first discipline even though the destination is a shared doc rather than a message.

## Output Template

```markdown
# Read-Ahead: <meeting name> — Week of <date>

## <Configured Section 1>
<content, with the so-what stated first>

## <Configured Section 2>
<content, with the so-what stated first>

[... remaining configured sections]
```

## Runs as a Routine

A strong weekly-cadence routine candidate, timed to land before the meeting — see `references/protocols/routines.md` and `setup/routine-setup.md`.

## Output Quality Self-Check

- [ ] Section set matches what was configured for this meeting, not a generic default
- [ ] Every section leads with a so-what, not a bare activity list
- [ ] Content is pulled from real sources with specifics — numbers, names, dates — not vague summary language
- [ ] Nothing was published to the docs hub before the draft was confirmed

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it three things: the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/status-update` -> when the audience is a stakeholder inbox rather than a recurring meeting's shared doc
- `/board-deck` -> when the audience is the board and the format needs more weight
- `/weekly-review` -> when the week's substance has not been synthesized yet
- `/meeting-prep` -> when you also need attendee context and talking points for the meeting itself

## When to Use

- Ahead of a recurring cross-team meeting that expects a pre-read

## When NOT to Use

- For a one-off update to a single stakeholder — use `status-update`
- For a board or executive-level presentation — use `board-deck`

## Common Mistakes

- Hardcoding a fixed section set instead of using what this meeting actually needs
- Listing activity without stating why it matters
- Publishing to the shared docs hub before the draft was confirmed
