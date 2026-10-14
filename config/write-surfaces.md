# Write Surfaces

**Principle: A DRAFT GOES WHERE THE USER EDITS IT, ON THE SURFACES THEY HAVE SAID SO, AND NOWHERE ELSE.**

Per-surface write mode for stores the user owns. Read the surface's row before a skill or routine writes to it. A surface with no row is `propose`. Changing a row is the user's call; a run never edits this file.

## The two modes

- **`propose`** (default): show the batch, write nothing until the user approves it (`references/protocols/knowledge-capture.md` §4, `references/protocols/skill-patterns.md` disciplines #4-5).
- **`draft-in-place`**: write the draft straight into the user's own entry on that surface, within the row's limits, and reply with a link to it. A preview-first reply costs a round trip before the user sees the page, and the page is where they edit anyway.

`draft-in-place` covers the user's own entries only. Anything other people read or act on (a shared doc, a ticket, a message) stays draft-first whatever its row says (`references/protocols/knowledge-capture.md` §5).

## How a `draft-in-place` write runs

1. **Fetch live.** Read the entry as it stands immediately before writing, never from earlier in the run.
2. **Fill only empty fields.** A field with anything in it belongs to the user and is not overwritten. Where the run would have written something different, that goes in the reply as a proposal.
3. **Dedupe creates.** Check the live store for the entry, or the forward shell, before creating it.
4. **Link the page.** The reply opens with the link, then lists what was filled, what was left alone, and the judgment questions.
5. **Proposals stay proposals.** Each row names what it never writes in place.

## Surfaces

| Surface | Mode | Written in place | Stays a proposal |
|---------|------|------------------|------------------|
| `<REVIEWS_STORE>`, the user's own review entries (week, month, quarter) | `draft-in-place` | Empty fields of the period's entry; deduped forward shells; links between entries | Goal, project, and status changes; any field already filled |
| `<TASK_TRACKER>` | `propose` | — | Every create, edit, and close |
| `<DOCS_HUB>` | `propose` | — | Every write |
| `context-library/`, `memory/` | `propose` | — | Every write |

To change a surface, edit its Mode cell, and name the limits in the next two cells. A row set to `draft-in-place` is also the standing approval an unattended routine needs to write that surface (`references/protocols/routines.md` discipline #7).
