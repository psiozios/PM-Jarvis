# Context Acquisition Protocol

**Principle: READ FREELY.**

Before producing output, every skill should acquire the context it needs. This protocol standardizes how.

## How It Works

### 1. Declare Sources

Each skill has a Context Routing Logic table listing the 2-4 live sources that matter for its task. Before running, read those sources in parallel.

Example routing table (from a skill's SKILL.md):

| Source | Location | What to Extract |
|--------|----------|-----------------|
| Strategy docs | `context-library/strategy/*.md` | Strategic pillar alignment |
| Related PRDs | `context-library/prds/*.md` | Related features, dependencies |
| User research | `context-library/research/*.md` | Pain points, quotes, validation |

### 2. Fan Out Reads

Read all declared sources in parallel. Do not read sequentially. Do not read the entire context library. Only read what the routing table specifies.

### 3. Synthesize

Combine what you found into a working context for the task. Note gaps and contradictions.

### 4. Ask Only for What Tools Cannot Supply

If a source is empty or a file doesn't exist, note it and proceed with what you have. Only ask the user for information that cannot be found in any file, MCP, or tool.

### 5. Verify Live State

When reporting status of anything (a metric, a decision, a task), verify against the current source. Don't rely on cached or remembered state.

## Graceful Degradation

- **MCP unavailable:** Fall back to `context-library/` files for the same data type.
- **File empty or missing:** Proceed without it. Note what's missing in your output.
- **Multiple sources conflict:** Flag the conflict. Cite both sources. Use the more recent one unless the user says otherwise.

## Anti-Patterns

- Reading every file in `context-library/` before starting (firehose)
- Asking the user for information that's already in a file (lazy)
- Skipping context reads entirely and producing generic output (careless)
- Reading files sequentially when parallel reads are possible (slow)
