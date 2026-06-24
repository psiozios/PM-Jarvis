# Memory System

Persistent, file-based memory that carries facts and preferences across conversations.

## How It Works

1. **Memory files** live in this directory, one fact per file with YAML frontmatter
2. **MEMORY.md** is the index, one line per entry
3. The **hook** (`hooks/inject_memory.py`) injects only the universal tier of the index every turn
4. The assistant reads individual memory files on demand when the index suggests relevance
5. The user can review, edit, or delete any memory at any time

## Memory Types and Filename Prefixes

Each memory file must use a type prefix so the hook can determine its injection tier from the index link alone.

| Type | Prefix | Tier | Injected per turn? |
|------|--------|------|-------------------|
| `user` | `user_` | Universal | Yes — who the user is |
| `feedback` | `feedback_` | Universal | Yes — behavioral rules |
| `project` | `project_` | Contextual | No — loaded once per session, then on demand |
| `reference` | `reference_` | Contextual | No — loaded once per session, then on demand |

The `metadata.type` field in the frontmatter is the canonical type and must match the prefix.

## Memory File Format

Each memory is a standalone markdown file with YAML frontmatter:

```markdown
---
name: short-kebab-case-slug
description: one-line summary used to decide relevance in future conversations
metadata:
  type: user | feedback | project | reference
---

The memory content. For feedback and project types, structure as:

The rule or fact.

**Why:** The reason or context behind it.

**How to apply:** When and where this should influence behavior.
```

## What NOT to Save

- Code patterns, architecture, file paths (derive from the codebase)
- Git history (use `git log` / `git blame`)
- Debugging solutions (the fix is in the code)
- Anything already in CLAUDE.md or config files
- Ephemeral task details only useful in the current conversation

## Tiering

**Index-only injection is O(entries), not flat.** Each index line adds ~150 chars to every turn's context budget. Past ~100 entries an untiered index overruns the per-turn size ceiling and loads only partially, silently dropping entries.

**Flatness comes from tiering by type.** The hook injects only `user_` and `feedback_` entries (the universal tier) every turn. `project_` and `reference_` entries (the contextual tier) load once per session via the native MEMORY.md read and are recalled on demand. This keeps per-turn cost bounded by the count of universal entries, which should stay small.

**Keep the universal tier small.** The scaling guarantee depends on `user_` + `feedback_` entries staying well under 100. If you find yourself with dozens of feedback entries, consolidate them.

See `hooks/README.md` for the hook design and installation.

## Index Rules

- `MEMORY.md` is read once per session by Claude (native behavior) and filtered per turn by the hook
- Each entry: one line, under 150 characters
- Lines after 200 may be truncated. Keep the index tight.
- Organize semantically by topic, not chronologically.
- Only `user_` and `feedback_` prefixed entries inject per turn.
- Link related memories with `[[name]]` in the body text.
