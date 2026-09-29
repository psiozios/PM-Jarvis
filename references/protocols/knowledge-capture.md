# Knowledge Capture Protocol

**Principle: WRITE ON CONFIRM.**

When a skill produces a durable insight, decision, or learning, propose writing it back to the right location. Never write institutional memory without explicit confirmation.

## How It Works

### 1. Recognize Durable Output

At the end of a skill run, assess whether the output contains something worth persisting:

- A decision and its rationale
- A validated insight from research
- A stakeholder preference or pattern
- A calibration data point (estimate vs actual)
- A process improvement or lesson learned

If yes, propose a write-back.

### 2. Propose a Specific Write-Back

Don't say "want me to save this?" Be specific:

**Good:**
> "This decision about auth architecture could go in `context-library/decisions/auth-approach-2025-q2.md`. Want me to save it?"

**Bad:**
> "Should I save this somewhere?"

### 3. Route to the Right Home

| Learning Type | Destination |
|--------------|-------------|
| Decision + rationale | `context-library/decisions/` |
| User research insight | `context-library/research/` |
| Meeting outcome | `context-library/meetings/` |
| Strategy change | `context-library/strategy/` |
| Launch result | `context-library/launches/` |
| Metric or analysis | `context-library/metrics/` |
| Second-brain material | `context-library/second-brain/{focus-area}/` |
| Behavioral rule or preference | `memory/` (via memory system) |

### 4. Wait for Confirmation

Propose the write-back as a one-tap action. Do not write until the user confirms. This applies to:

- Context library updates
- Memory entries
- Second-brain wiki pages
- Any file outside `outputs/`

### 5. Outward Actions Are Draft-First

When a skill produces something intended for others (a Slack message, a ticket, an email), always produce a draft in `outputs/` first. Never send, post, or publish without explicit confirmation.

**A reply carries new information, or it is not a reply.** Restating what they said, asking them to clarify, and handing their question back all carry nothing — each one moves the work back across the table. Retrieve what the question is about before drafting anything. If the retrieval leaves nothing to say that the reader does not already have, the deliverable is the retrieval — what was looked up and what it showed — rather than a drafted message.

**Test the premise before answering it.** A senior stakeholder's question is not automatically the right question. Where retrieval shows the premise is off, saying so is new information, and it is usually the most useful thing the reply can carry.

### 6. Knowledge-Base Writes Are Surgical

The surgical-edit rule covers every store the assistant writes to: a tracker entry, a source-of-truth doc, a wiki page, a context-library file. It used to name the tracker (the periodic-review cascade in `references/protocols/skill-patterns.md`) and never the wiki, and an ingest fell into the gap: it wrote two existing pages as new and erased their history.

- **Read before writing.** Check on disk whether the target exists, in the directory and not the index. If it does, read it in full and apply only the delta. Never write the page back whole from memory of what it said.
- **Confirm prior content survives.** Re-read the page after the write. Every earlier claim, citation, and dated line is still there, or was struck on purpose with a dated note (`references/protocols/freshness-provenance.md` rule 2).
- **Flag net deletions after a multi-page pass.** Run `git diff --numstat` over what the pass touched and list every file whose deletions exceed its insertions, each with its reason or a restore. An ingest adds; a page that shrank is where history went missing.
- **Every link written resolves on disk, at the right relative depth.** Resolve it from the directory of the file that holds it, not the repo root, and open the target. A `[[page-name]]` link names a page that exists, or one created in the same pass.
- **Strip code spans before a link scan, and never let a fixer edit inside one.** Inline code and fenced blocks are where logs quote old links: a log line, a changelog entry, a correction naming the path it replaced. Those are the record. A scan that counts them reports false breaks, and a fixer that repairs them rewrites history.

## The Governing Boundary

**READ FREELY, WRITE ON CONFIRM.**

- Reading files, MCPs, and tools: do it proactively, in parallel, without asking.
- Writing to context-library, memory, or external systems: always propose, never auto-execute.
- Writing to `outputs/`: permitted (this is the active workspace).

## Anti-Patterns

- Auto-writing to context-library mid-session without asking
- Silently updating stakeholder profiles or decision logs
- Sending a Slack message or creating a ticket without showing a draft first
- Skipping the write-back proposal when durable output was clearly produced
- Writing a page as new without checking whether it already exists (§6)
