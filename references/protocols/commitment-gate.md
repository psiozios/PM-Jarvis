# Commitment Gate

A pre-takeoff checklist that fires at expensive, hard-to-reverse commitment moments — not on ideas, discussion, or quick capture.

## When It Fires

You define the triggers. Generic examples:
- Creating an epic or set of implementation tickets
- Moving work into a sprint commitment
- Signing off on a scope that a cross-functional team will execute against

The gate does **not** fire on: brainstorms, PRD Lite proposals, backlog grooming, exploratory research, or any artifact that is cheap to revise.

## The Five Checks

Run these in order. Each takes one sentence to answer.

1. **Problem before solution.** State the problem and its current cost in one sentence, with a number. Name no solution.
2. **Capability delta.** Confirm what already exists by trying it or asking the owner — don't assert a gap from memory. Write down the real delta between what exists and what's needed.
3. **"Done" defined by the gating function.** For anything a compliance, legal, risk, or finance function touches, that function confirms the requirement and what "complete" looks like, in writing, before scoping begins.
4. **Every touched layer saw the shape.** Each implementing and reviewing function sees the design before committed work exists. No surprises at review time.
5. **Open questions triaged.** Sort unknowns into two bins:
   - *Shape-changing* — blocks the commitment; must be resolved first.
   - *Resolvable-in-flight* — does not block; track and resolve during execution.

## Why This Is Faster, Not Slower

Skipping the gate feels fast. It buys rework: re-scoped sprints, late-stage compliance blockers, engineering that builds the wrong thing because the problem wasn't stated clearly. Five one-sentence checks take five minutes. A mis-scoped sprint costs a week.

## Enforcement

The gate is a habit, not a hard block. Three reinforcement points:

1. **Skill pointers.** The skills that produce committed work (`/create-tickets`, `/sprint-planning`, `/prd-draft`, `/prioritize`, `/prd-lite`) include a one-line pointer to this protocol. The assistant surfaces the checklist when those skills produce commitment-level output.
2. **feedback_ memory entry (optional).** Save a `feedback_` memory entry like *"Run the commitment-gate checklist before creating tickets or committing work to a sprint"* to make the gate fire automatically via the per-turn hook. See `memory/feedback_example.md` for the format.
3. **Pre-takeoff framing.** Treat the five checks like a pilot's pre-takeoff checklist: quick, sequential, non-negotiable at the commitment moment, invisible the rest of the time.
