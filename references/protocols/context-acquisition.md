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

**A `Search Terms` column is a list of queries, not one query.** Forty-five skills carry a routing table with a comma-separated term list. Each term is sent on its own, and a term containing a space is sent again word by word if it comes back empty — the combining behaviour belongs to the tool, and most of them AND. See `references/protocols/evidence-ledger.md` for the rule and `references/mcp-routing.md` for what each tool was verified to do.

### 3. Synthesize

Combine what you found into a working context for the task. Note gaps and contradictions.

### 4. Ask Only for What Tools Cannot Supply

If a source is empty or a file doesn't exist, note it and proceed with what you have. Only ask the user for information that cannot be found in any file, MCP, or tool.

### 5. Verify Live State

When reporting status of anything (a metric, a decision, a task), verify against the current source. Don't rely on cached or remembered state.

### 6. An absence claim needs its own read

"No page exists", "nobody asked", and "never recorded" are assertions about a whole store. Each one needs a read aimed at the thing said to be missing, done this run: search the store on that thing's own nouns (`references/protocols/evidence-ledger.md` §1-2), and open the directory rather than the index. Only then write the claim.

**A prior run's gap flag is a lead to re-check, never a finding.** One run repeated last week's missing-page flag about a page created the same day that flag was raised. The flag had been carried forward, and nobody had looked.

**A partial read supports "I found X", never "there is no X".** An index, the first page of results, a search stopped once it had enough, a single export: each tells you what it holds, not what the store lacks. One artifact is one source. An absence claim resting on one file, thread, or index is scoped to what was read ("not in `wiki/index.md` as of `<DATE>`"), or it is not made.

**Strike a wrong claim in place and name its cause.** The reader may already have acted on it, so it stays visible, struck through, with a dated line beside it saying what produced it (an index-only read, a stopped search, a carried flag) and what the fresh read found. A silent deletion hides the defect, and a quiet rewrite hides the fix. This is the dated-append correction of `references/protocols/freshness-provenance.md` rule 2, applied to a claim that was wrong rather than one that aged. It is not the ledger's strike rule, under which a claim about a lookup that never ran is removed before anything ships (`references/protocols/evidence-ledger.md` §1).

## Graceful Degradation

- **Live source failed** (a credential expired, a scope was revoked, an OAuth refresh needs a browser the run doesn't have): fall back, and **report it unavailable by name with the reason it gave**. It does not appear in any list of sources the run covered. See `references/protocols/source-preflight.md` — a failed source and a source with nothing to say look identical in the data and mean opposite things.
- **MCP not connected at all:** Fall back to `context-library/` files for the same data type, and say once that you did.
- **File empty or missing:** Proceed without it. Note what's missing in your output.
- **Multiple sources conflict:** Flag the conflict. Cite both sources. Use the more recent one unless the user says otherwise.

**Degradation is disclosed, not silent.** Reading around a dead source is fine; letting the output imply that source was consulted is not.

## Anti-Patterns

- Reading every file in `context-library/` before starting (firehose)
- Asking the user for information that's already in a file (lazy)
- Skipping context reads entirely and producing generic output (careless)
- Reading files sequentially when parallel reads are possible (slow)
- Listing a source as covered when it never answered (dishonest, and the defect is invisible from outside the run)
- Saying a page, ask, or record is missing on the strength of an index, a stopped search, or last run's flag (§6)
