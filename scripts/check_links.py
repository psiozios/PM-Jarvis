#!/usr/bin/env python3
"""
Link check: every local link in the given markdown files resolves on disk.

Usage:
  python3 scripts/check_links.py <file-or-dir> [<file-or-dir> ...]

Checks two link shapes, after stripping fenced blocks and inline code spans
(logged old links are the record, never a break to fix):
  [text](relative/path.md#anchor)  resolved from the directory of the file
                                   that holds it, not the repo root
  [[page-name]] / [[page|alias]]   resolved to page-name.md anywhere under the
                                   nearest ancestor directory named `wiki`
                                   (or the file's own directory if none)

URLs (http, https, mailto) and same-page anchors are skipped: a URL is checked
by fetching it before it is written, not by this script.

Prints one line per broken link, then a summary line to quote verbatim:
  link-check: <files> files, <links> links, <broken> broken
Exits 1 when anything is broken, 2 on a usage error, 0 otherwise. A gate that
runs this reads the exit code, never a count typed from memory
(references/protocols/freshness-provenance.md rule 6).
"""
import re
import sys
from pathlib import Path

FENCE = re.compile(r"^(\s*)(```|~~~)")
INLINE_CODE = re.compile(r"`+[^`\n]*`+")
MD_LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
WIKI_LINK = re.compile(r"\[\[([^\]\n]+)\]\]")
SKIP = ("http://", "https://", "mailto:", "#")


def prose_lines(text):
    """Yield (line_no, line) outside fenced blocks, with code spans removed."""
    in_fence = None
    for no, line in enumerate(text.splitlines(), 1):
        m = FENCE.match(line)
        if m:
            marker = m.group(2)
            if in_fence is None:
                in_fence = marker
            elif in_fence == marker:
                in_fence = None
            continue
        if in_fence is None:
            yield no, INLINE_CODE.sub("", line)


def wiki_root(path):
    for parent in path.parents:
        if parent.name == "wiki":
            return parent
    return path.parent


def check_file(path):
    broken, count = [], 0
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return [f"{path}: unreadable ({exc.__class__.__name__})"], 0
    for no, line in prose_lines(text):
        for target in MD_LINK.findall(line):
            if target.startswith(SKIP):
                continue
            count += 1
            rel = target.split("#", 1)[0]
            if rel and not (path.parent / rel).exists():
                broken.append(f"{path}:{no}: [..]({target}) does not resolve")
        for inner in WIKI_LINK.findall(line):
            count += 1
            name = inner.split("|", 1)[0].split("#", 1)[0].strip()
            if not name:
                continue
            root = wiki_root(path)
            if not any(root.rglob(f"{name}.md")):
                broken.append(f"{path}:{no}: [[{inner}]] names no page under {root}")
    return broken, count


def main(argv):
    if not argv:
        print("usage: check_links.py <file-or-dir> [<file-or-dir> ...]", file=sys.stderr)
        return 2
    files = []
    for arg in argv:
        p = Path(arg)
        if p.is_dir():
            files += sorted(p.rglob("*.md"))
        elif p.suffix == ".md" and p.exists():
            files.append(p)
        else:
            print(f"link-check: no such markdown file or directory: {arg}", file=sys.stderr)
            return 2
    broken, links = [], 0
    for f in files:
        b, n = check_file(f)
        broken += b
        links += n
    for line in broken:
        print(line)
    print(f"link-check: {len(files)} files, {links} links, {len(broken)} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
