# Capabilities

## Parallel Execution

**Instrument the run before you add to it.** Two numbers, recorded for the run as it stands today: time to first delivery, and tool calls. Without them every added stage looks justified on its own merits and nothing shows the total. One pipeline here went from 3 minutes to 74, and from a dozen tool calls to 96, on a sequence whose every step had a reason.

**Cost you moved is not cost you saved.** The 3-minute baseline was not faster — it was deferring the work into the interactive session, where the user paid for it instead. Compare the whole loop against the whole loop: the run plus the conversation it produces. A comparison that stops at the run boundary flatters whichever side of the boundary you are standing on.

**Parallel reads are free; spawned agents are not.** Reading several declared sources at once is one batch and stays the default (`references/protocols/context-acquisition.md`). A spawned agent costs a fresh context window that has to re-derive what this session already knows, and per-item fan-out multiplies that by the length of the list.

**One inline batch by default; spawn only where a false positive is expensive.** Process the items — interviews, competitor profiles, candidates — in a single batched pass, and give a separate agent only to the case where being wrong costs something real. An adversarial fan-out that returned zero kills across four runs and produced only rewording is refinement, not verification: fold it inline and drop the stage.

**Verification does not fix selection.** A per-item check answers "is this claim true". It never answers "was this the right item" or "is this still current" — and those are the two grounds most rejected lists were actually rejected on. Rank first, gate the top N, and **state the ungated count**, so the reader can see what was checked and what only ranked below the line.

## Plan Mode

For complex, multi-step tasks, use Plan Mode:

1. Create a structured plan with steps
2. Get user approval on the plan
3. Execute sequentially, tracking progress

Good candidates for Plan Mode: multi-step PRD creation, testing prompts across models, complex research synthesis, strategic planning with multiple inputs.

## Web Search

Use web search when:

- Researching competitors or recent product launches
- Looking up technical specifications or market data
- Checking current pricing or feature sets
- Gathering context that isn't in workspace files

## Code Execution

Run code when helpful:

- Data analysis on user research or metrics
- Testing AI prompts across multiple APIs
- Generating charts or visualizations
- Processing structured data (CSVs, JSON)

## Context Management

- **Clear context** when switching to a completely different initiative or starting fresh
- **Preserve context** during ongoing work within a single initiative
- If approaching token limits, suggest a new thread and summarize critical carry-over context
- Always preserve critical context (decisions made, constraints identified) when starting new threads
