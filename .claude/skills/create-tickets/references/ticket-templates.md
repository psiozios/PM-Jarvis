# Ticket Templates — One Section Set Per Issue Type

Four issue types, four section sets. **Use the set that matches the type; do not merge them into one universal body.** A bug and a spike need different things on the page, and a single template forces empty ceremony into three of the four.

**These are starting shapes, not the standard.** The standard is your team's own corpus — mine `references/tickets-corpus.md` first (`config/house-style.md` §9) and reshape these sections to match what your engineers actually read and write. Ship whichever sections the corpus supports and delete the rest.

## Rules that bind every type

**Never prescribe implementation.** State what must be true when the work is done, and what constraints hold. Do not name the table, the endpoint shape, the library, the file, or the pattern. Engineering owns how. Where a technical fact is a genuine *constraint* rather than a preference — a contract another team already ships against, a compliance requirement — state it as a constraint and cite where it came from.

**Every behavioral claim carries its source.** Any sentence asserting how the product currently behaves, what a user does, or what was decided carries an inline pointer to where that came from: a PRD section, a dated thread, a ticket ID, a research quote, a metrics query. A behavioral claim with no source is the ticket's most expensive defect, because engineering builds against it and nobody can check it later.

**No acceptance-criteria floor.** There is no minimum count and no requirement that a ticket have criteria at all. Write them where the "done" boundary is genuinely unclear, and leave them out where the summary already settles it. Padding to a count produces criteria that restate the title, which trains everyone to stop reading them.

**No sizing, no sprint.** Nothing in these templates carries an estimate, a story point, a t-shirt size, or a sprint. Engineering sizes its own work.

## Type: Bug

```markdown
## What happens
[Observed behavior. Source: where it was reported, with a date or link.]

## What should happen
[Expected behavior. Source: the PRD section, spec, or decision that establishes it.]

## Reproduction
[Steps, environment, and how consistently it reproduces. Say so if it is intermittent.]

## Impact
[Who hits this, how often, and what it costs them. Source the frequency claim.]

## Scope
[What this ticket does and does not cover — particularly nearby broken things it is not.]
```

## Type: Behavior change (feature, story, enhancement)

```markdown
## The change
[One paragraph: what will be different for the user when this ships.]

## Why now
[The reason this is being built at this point. Source: PRD, decision doc, or thread.]

## Behavior
[What the product must do. Each claim carries its source. Describe outcomes, not mechanisms.]

## Out of scope
[Explicitly excluded, so scope questions resolve on the page instead of in a thread.]

## Acceptance criteria
[Only where "done" is genuinely ambiguous. Delete this section otherwise.]

## Open questions
[Unresolved ambiguities, each with who can answer it. These are the writeback targets.]
```

## Type: Chore / infrastructure

```markdown
## Current state
[What exists now. Source it.]

## Desired state
[What must be true afterward — the property, not the implementation.]

## Why now
[What makes this worth doing at this point rather than later.]

## Constraints
[What must not break, what must keep working, any external contract that binds. Source each.]
```

## Type: Spike

```markdown
## Question to answer
[One question, phrased so an answer can settle it.]

## What is blocked without it
[The decision or the work that cannot proceed. Name it.]

## Timebox
[How long before we stop and decide with what we have.]

## What a usable answer looks like
[The form the output takes — a recommendation, a number, a working sample.]
```

A spike carries no acceptance criteria by construction. If you can write criteria for it, it is not a spike.

## Choosing the type

| The work is… | Type |
|---|---|
| Something behaves differently than it should | Bug |
| Something should behave differently than it does today | Behavior change |
| No user-visible behavior changes | Chore / infrastructure |
| We cannot specify the work until a question is answered | Spike |

When a bug and a behavior change are genuinely tangled, split them: the bug restores the documented behavior, the behavior change alters what is documented.
