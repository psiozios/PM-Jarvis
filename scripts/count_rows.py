#!/usr/bin/env python3
"""
Count the data rows of every markdown table in a file, optionally by column.

Usage:
  python3 scripts/count_rows.py <file.md> [--by <column header>]

Examples:
  python3 scripts/count_rows.py outputs/ledgers/action-sweep-2026-10-13.md --by Verdict
  python3 scripts/count_rows.py .claude/skills/loose-threads/evals.md

Header and separator rows are not counted, and neither are rows inside fenced
blocks. Prints one summary line to quote verbatim in the output:
  rows: 11 (PROPOSE 6, KILL 4, UNPROVEN 1)
A count in a run's output comes from this line or another command's, never
from recall (references/protocols/freshness-provenance.md rule 6).
Exits 2 on a usage error or when --by names a column no table has.
"""
import sys
from collections import Counter
from pathlib import Path


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_separator(line):
    body = line.strip().strip("|").replace("|", "").replace(":", "").replace("-", "").strip()
    return body == "" and "-" in line


def main(argv):
    if not argv or argv[0].startswith("-"):
        print("usage: count_rows.py <file.md> [--by <column header>]", file=sys.stderr)
        return 2
    path, by = Path(argv[0]), None
    if len(argv) == 3 and argv[1] == "--by":
        by = argv[2]
    elif len(argv) != 1:
        print("usage: count_rows.py <file.md> [--by <column header>]", file=sys.stderr)
        return 2
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        print(f"rows: cannot read {path} ({exc.__class__.__name__})", file=sys.stderr)
        return 2

    total, tally, header, col, in_fence, found_col = 0, Counter(), None, None, False, False
    for i, line in enumerate(lines):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence or not line.lstrip().startswith("|"):
            header = None
            continue
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if header is None and is_separator(nxt):
            header = cells(line)
            col = header.index(by) if by in header else None
            found_col = found_col or col is not None
            continue
        if header is None or is_separator(line):
            continue
        total += 1
        if col is not None:
            row = cells(line)
            tally[row[col].strip("`*") if col < len(row) else ""] += 1

    if by and not found_col:
        print(f"rows: no table in {path} has a column named {by!r}", file=sys.stderr)
        return 2
    detail = ""
    if by:
        detail = " (" + ", ".join(f"{k or '(empty)'} {v}" for k, v in tally.most_common()) + ")"
    print(f"rows: {total}{detail}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
