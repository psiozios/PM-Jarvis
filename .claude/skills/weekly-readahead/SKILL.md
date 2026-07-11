---
name: weekly-readahead
description: Draft a weekly read-ahead for a recurring cross-team meeting and publish it to the shared docs hub. Configurable section set, pulled from the week's shipped work, decisions, risks, and metrics, with a clear so-what per section.
disable-model-invocation: false
user-invocable: true
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

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Task tracker | `<TASK_TRACKER>` | Work shipped this week |
| Decisions | `context-library/decisions/`, `outputs/decisions/` | Decisions made this week |
| Metrics | `<METRICS_SOURCE>` | Movement worth reporting |
| Meeting notes | `outputs/meeting-notes/` | Risks or blockers surfaced this week |
| Docs hub | `<DOCS_HUB>` | Where the read-ahead publishes, and the prior week's read-ahead for continuity |

## Workflow

### 1. Resolve the section set

If this is the first run for this meeting, ask for the section set (or accept `--sections`). Store it for reuse on subsequent runs so the format stays consistent week over week — this skill does not assume a fixed set of sections across all meetings, since different recurring meetings care about different things.

### 2. Pull the week's substance

For each configured section, pull the relevant material: shipped work from `<TASK_TRACKER>`, decisions from `context-library/decisions/`, metric movement from `<METRICS_SOURCE>`, risks from recent meeting notes.

### 3. Write a so-what per section

Every section leads with why it matters to this specific audience, not a bare list of what happened. A shipped-work bullet without an impact statement is incomplete.

### 4. Draft, then publish on confirm

Show the drafted read-ahead. Publish to `<DOCS_HUB>` only after confirmation — this is content visible to others, so it follows the outward-draft-first discipline even though the destination is a shared doc rather than a message.

## Output Format

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

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Related:** `status-update` (similar substance, different destination — this skill is specifically for a recurring cross-team meeting's shared read-ahead), `board-deck` (heavier-weight version for board/exec audiences)

## When to Use

- Ahead of a recurring cross-team meeting that expects a pre-read

## When NOT to Use

- For a one-off update to a single stakeholder — use `status-update`
- For a board or executive-level presentation — use `board-deck`

## Common Mistakes

- Hardcoding a fixed section set instead of using what this meeting actually needs
- Listing activity without stating why it matters
- Publishing to the shared docs hub before the draft was confirmed
