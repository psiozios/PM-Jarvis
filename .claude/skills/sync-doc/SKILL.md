---
name: sync-doc
description: Reconcile a pasted or exported external doc into its local counterpart. Applies only substantive changes, ignores formatting noise, and preserves richer local context the external copy lacks.
user-invocable: true
disable-model-invocation: false
---

## Quick Start

**What to provide:** The external doc's current content (pasted or exported) and the path to its local counterpart.

```
/sync-doc <local file path>
[paste the external doc's current content]
```

**What you get:** A reconciliation showing exactly what substantive changes to apply to the local file — checked-off items, new content, updated facts — with formatting noise ignored and any richer local context preserved.

**Time:** A minute or two, depending on doc size.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own.

## Context Routing

| Source | Location | What to Extract |
|--------|----------|------------------|
| External docs tool | `<DOCS_HUB>` (pasted/exported content) | The doc's current state as the external source of truth for content that originates there |
| Local file | path given by the user | Current local content, including any local-only context to preserve |


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected.

## Workflow

### 1. Diff for substance, not formatting

Compare the external content against the local file's current content. Identify substantive changes only: items checked off, new sections or bullets added, facts or numbers updated, statuses changed. Ignore pure formatting differences — whitespace, heading style, list markers, line wrapping — that carry no content change.

### 2. Preserve richer local context

If the local file has content the external copy doesn't (local annotations, a more detailed breakdown, context added after the last sync), keep it. The sync is additive-and-corrective from the external source, not a wholesale overwrite that would discard local-only richness.

### 3. Reconcile conflicting facts

If the external and local versions disagree on the same fact (a status, a number), treat the external doc as more current for anything that plausibly originates there, but flag the conflict explicitly rather than silently picking a side if it's ambiguous which is newer.

### 4. Present the delta, apply on confirm

Show exactly what would change before writing anything. Apply only on confirmation.

## Output Template

```markdown
# Doc Sync — <local file>

## Substantive Changes to Apply
- <change 1: what's changing and why — e.g. "item X now checked off">
- <change 2>

## Local-Only Context Preserved
- <content that exists locally but not externally, kept as-is>

## Conflicts (need a call)
- <fact that differs between the two, with both values shown>

## Ignored (formatting only)
<one line noting formatting-only differences were skipped, if any>
```

## Runs as a Routine

If the external doc updates on a predictable cadence, this can run as a scheduled routine — see `references/protocols/routines.md` and `setup/routine-setup.md`. Otherwise it's naturally on-demand, triggered right after the external doc changes.

## Output Quality Self-Check

- [ ] Only substantive changes are listed — formatting-only differences are explicitly excluded, not silently merged in
- [ ] Local-only context is identified and preserved, not overwritten
- [ ] Genuine conflicts are flagged, not silently resolved by picking a side
- [ ] Nothing was written to the local file before the delta was confirmed

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it three things: the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/iterate-document` -> when the job is evolving a source-of-truth doc from new learning, not reconciling two copies
- `/editing-assistant` -> after reconciling, when the merged prose needs polish
- `/update-docs` -> when the doc to reconcile is code documentation driven by a git diff

## When to Use

- Whenever an external doc (a shared doc, an exported file) is the source of truth for content that also has a local file, and you need the local copy to catch up without losing local-only additions

## When NOT to Use

- When there's no local counterpart to reconcile against — just import the external content directly instead

## Common Mistakes

- Treating a formatting difference as a substantive change
- Overwriting local-only context that the external copy never had
- Silently picking a side on a genuine conflict instead of flagging it
