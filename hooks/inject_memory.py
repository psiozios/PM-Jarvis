#!/usr/bin/env python3
"""
UserPromptSubmit hook: inject only the UNIVERSAL tier of memory every turn.

Two tiering axes:
  1. Index vs full file: only the index is injected per turn; full memory files
     are read on demand when a task warrants it.
  2. By type, within the index: only universal entries inject every turn.
       user_     : who the user is
       feedback_ : how to behave everywhere
     Contextual entries (project_, reference_) do NOT inject per turn. They load
     once per session via the native MEMORY.md read and are recalled on demand.

Why both axes: injecting the whole index every turn is O(entries), not flat.
Past ~100 entries it can overrun the per-turn budget and load only partially.
Tiering by type keeps the per-turn block flat as project_/reference_ grow.

Matches MEMORY.md lines of the form:
  - [Title](filename.md) -- one-line description
  - [Title](filename.md): one-line description
"""
import re
import sys
from pathlib import Path

MEMORY_INDEX = Path(__file__).resolve().parent.parent / "memory" / "MEMORY.md"
MAX_DESC_LEN = 110
ENTRY = re.compile(r"^\s*-\s*\[([^\]]+)\]\(([^)]+)\)\s*(?:--|:)\s*(.+)$")


def main() -> int:
    if not MEMORY_INDEX.exists():
        return 0
    try:
        lines = MEMORY_INDEX.read_text(encoding="utf-8").splitlines()
    except Exception:
        return 0  # never break the prompt pipeline

    entries = []
    for line in lines:
        m = ENTRY.match(line)
        if m:
            title, fname, desc = m.groups()
            if len(desc) > MAX_DESC_LEN:
                desc = desc[:MAX_DESC_LEN].rstrip() + "..."
            entries.append((title, fname, desc))
    if not entries:
        return 0

    user = [(t, d) for t, f, d in entries if f.startswith("user_")]
    feedback = [(t, d) for t, f, d in entries if f.startswith("feedback_")]
    injected = len(user) + len(feedback)

    out = ["<memory-context>"]
    out.append(
        f"{injected} of {len(entries)} memory entries inject every turn (universal "
        "rules). The rest are contextual: they load once per session, then on "
        "demand from memory/. Apply these as settled rules, not suggestions."
    )
    if user:
        out.append("\n**User context:**")
        out += [f"- {t}: {d}" for t, d in user]
    if feedback:
        out.append("\n**Behavioral rules:**")
        out += [f"- {t}: {d}" for t, d in feedback]
    out.append("</memory-context>")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
