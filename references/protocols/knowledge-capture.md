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
