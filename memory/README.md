# Memory System

Persistent, file-based memory that carries facts and preferences across conversations.

## How It Works

1. **Memory files** live in this directory, one fact per file with YAML frontmatter
2. **MEMORY.md** is the index, one line per entry, injected every turn via hook
3. The assistant reads individual memory files on demand when the index suggests relevance
4. The user can review, edit, or delete any memory at any time

## Memory Types

| Type | What it stores | When to save |
|------|---------------|-------------|
| `user` | Role, goals, expertise, preferences | When you learn about the user's background or perspective |
| `feedback` | Behavioral guidance (corrections and confirmations) | When the user corrects your approach or confirms something non-obvious |
| `project` | Ongoing work, goals, deadlines, decisions | When you learn about project context not derivable from code/git |
| `reference` | Pointers to external resources | When you learn where information lives in external systems |

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

The hook injects only `MEMORY.md` (the index) every turn. Individual memory files are read on demand. This keeps per-turn cost flat as memory grows. See `hooks/README.md` for the design rationale.

## Index Rules

- `MEMORY.md` is injected into every conversation turn. Keep it concise.
- Each entry: one line, under 150 characters
- Lines after 200 may be truncated. Keep the index tight.
- Organize semantically by topic, not chronologically.
- Link related memories with `[[name]]` in the body text.
