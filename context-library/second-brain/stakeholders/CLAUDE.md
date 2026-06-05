# stakeholders Focus Area

**What goes here:** Stakeholder profiles, preferences, past decisions, relationship history

## Rules

- `raw/` is immutable. Never modify source files once added.
- `wiki/` is LLM-owned. Create, update, and cross-link pages freely.
- Every factual claim in a wiki page cites its source: `[Source: filename.md]`.
- Every wiki page starts with YAML frontmatter (title, created, last_updated, source_count, status).
- Cross-reference aggressively with `[[page-name]]` links.
- On contradiction: flag both claims, cite both sources, note which is more recent. Never silently overwrite.
- `wiki/index.md` gets updated on every ingest.
- `wiki/log.md` is append-only. Format: `## [YYYY-MM-DD] action | description`.
