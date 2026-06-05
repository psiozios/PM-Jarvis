#!/bin/bash
# UserPromptSubmit hook: injects memory index into every turn.
#
# TIERING STRATEGY:
# - Tier 1 (every turn): MEMORY.md index only. One line per entry, bounded cost.
# - Tier 2 (on demand): Individual memory files. Claude reads these when
#   the index suggests relevance. Not injected per-turn.
#
# WHY TIERING MATTERS:
# Without tiering, every saved memory is injected into every turn.
# At 10 memories that's fine. At 100 it burns context on every interaction.
# The index-only approach keeps per-turn cost flat: O(entries * ~150 chars).
# Claude reads full memory files on demand when the task warrants it.
#
# INSTALL:
# Copy config/settings-template.json to .claude/settings.json
# Or add the UserPromptSubmit hook from that template to your existing settings.

if [ -f memory/MEMORY.md ]; then
  echo "<memory-context>"
  cat memory/MEMORY.md
  echo "</memory-context>"
fi
