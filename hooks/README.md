# Hooks

This directory contains hook scripts that extend Claude Code's behavior.

## Available Hooks

### user-prompt-submit.sh

**Purpose:** Injects the memory index into every conversation turn so the assistant is aware of persistent facts and preferences.

**How it works:**
1. On every user message, the hook checks if `memory/MEMORY.md` exists
2. If yes, it outputs the index contents wrapped in `<memory-context>` tags
3. Claude sees the index and can read individual memory files on demand

**Tiering design:**

| Tier | What's injected | When | Cost |
|------|----------------|------|------|
| Universal (Tier 1) | `MEMORY.md` index | Every turn | Flat: O(entries x ~150 chars) |
| Contextual (Tier 2) | Individual memory files | On demand, when Claude reads them | Per-read: only when relevant |

**Why tiering matters:** Without tiering, every saved memory gets injected into every turn. At small scale this is invisible. At 50+ memories it burns significant context budget on every interaction, whether the memories are relevant or not. The index-only approach keeps per-turn cost flat as memory grows. Claude reads full memory files only when the task warrants it.

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
