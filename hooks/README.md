# Hooks

This directory contains hook scripts that extend Claude Code's behavior.

## Available Hooks

### inject_memory.py

**Purpose:** Injects only the *universal* tier of the memory index into every conversation turn so the assistant is aware of persistent facts and preferences without growing per-turn cost.

**How it works:**
1. On every user message, the hook reads `memory/MEMORY.md`
2. It filters index lines by filename prefix: only `user_` and `feedback_` entries are universal
3. It outputs matching entries wrapped in `<memory-context>` tags
4. Claude sees the universal entries and can read individual memory files (any tier) on demand

**Tiering design:**

| Tier | Prefix | Injected when | Per-turn cost |
|------|--------|--------------|---------------|
| Universal | `user_`, `feedback_` | Every turn | Flat: bounded by the count of universal entries only |
| Contextual | `project_`, `reference_` | Once per session (native MEMORY.md read), then on demand | Zero per-turn |

**Why two-axis tiering matters:**

Injecting the whole MEMORY.md index every turn is O(entries), not flat. Each saved memory adds ~150 chars to every turn's context budget. Past ~100 entries the injected block can overrun the per-turn size ceiling and load only partially, silently dropping entries. Tiering by type keeps the per-turn block flat as `project_` and `reference_` entries grow — only the universal tier (who the user is, how to behave) pays per-turn cost.

**Filename prefix convention:**

Memory files must use a type prefix so the hook can determine tier from the index link alone:
- `user_*.md` — universal (injected every turn)
- `feedback_*.md` — universal (injected every turn)
- `project_*.md` — contextual (on demand)
- `reference_*.md` — contextual (on demand)

The `metadata.type` field in each file's frontmatter is the canonical type and must match the prefix.

### user-prompt-submit.sh (deprecated)

Stub pointing to `inject_memory.py`. Safe to delete.

## Installation

1. Copy the settings template to your Claude Code settings:
   ```bash
   cp config/settings-template.json .claude/settings.json
   ```

2. If you already have a `.claude/settings.json`, merge the `hooks` section from `config/settings-template.json` into your existing file.

3. Verify the hook works by starting Claude Code and checking that memory context appears in the conversation.

## Creating Your Own Hooks

Claude Code supports hooks on these events:
- `UserPromptSubmit` - runs when the user sends a message
- `PreToolUse` - runs before a tool executes
- `PostToolUse` - runs after a tool executes
- `Notification` - runs on notifications
- `Stop` - runs when the assistant stops

See Claude Code documentation for the full hook specification.
