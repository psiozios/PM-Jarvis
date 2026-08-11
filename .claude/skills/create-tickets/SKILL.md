---
name: create-tickets
description: Break a PRD, spec, or list of action items into engineering tickets — one per domain change, shaped by issue type, every behavioral claim sourced. Creates them in the issue tracker when one is connected, otherwise gives copy-paste text. Does not size or schedule work; engineering does that. Commits a team to work, so a commitment gate runs first.
user-invocable: true
disable-model-invocation: false
---

Turn a PRD, spec, or action-item list into tickets engineering can pick up. The skill decides ticket boundaries, fills the section set for each issue type, and sources every claim it makes about how the product behaves.

## Quick Start

**What to provide:** A source — a PRD path, a spec, meeting action items, or a description of the work. Say which tracker and project if one is connected.

```
/create-tickets outputs/prds/checkout-redesign.md
/create-tickets --quick "Login button broken on mobile Safari"
/create-tickets --stories
```

**What you get:** Tickets created in the tracker, or copy-paste text saved to `outputs/analyses/[feature]-tickets.md`.

**Commitment gate:** Creating tickets commits a team to work. Run the five checks in `references/protocols/commitment-gate.md` before anything is created.

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own.

**Ticket shape comes from a corpus, not from taste.** Before setting or revising the shape of a ticket here, mine the team's existing tickets into `references/tickets-corpus.md` — the ones engineers actually picked up without asking questions, and the ones that generated a thread of clarifications. Every shape rule traces to a quote in it (`config/house-style.md` §9, template at `templates/corpus-template.md`). The section sets in this skill's `references/ticket-templates.md` are a starting shape and lose to the corpus wherever the two disagree.

**One ticket per domain change, not one per surface.** A single change to how something behaves is one ticket, even when landing it touches the schema, an endpoint, and a screen. Splitting by surface manufactures dependency chains, spreads one "done" across three tickets so none of them is independently shippable, and leaves nobody owning the behavior. Split when the *domain* splits — two changes that could ship in either order, or ship separately and still make sense.

**Never prescribe implementation.** Say what must be true when it is done and what constrains it. Do not name the table, the endpoint, the library, or the pattern. Engineering owns how, and a PM's guess at it reads as a requirement.

**Every behavioral claim carries its source.** Any assertion about how the product behaves, what users do, or what was decided carries an inline pointer — PRD section, dated thread, ticket ID, research quote, metrics query. Unsourced behavioral claims are the expensive defect: engineering builds against them and nobody can check them later.

**No acceptance-criteria floor.** No minimum count, and no requirement that a ticket have criteria at all. Write them where the "done" boundary is genuinely unclear; leave them out where the summary settles it. Padding to a count produces criteria that restate the title.

**No estimating, no sprint assignment.** Do not attach t-shirt sizes, story points, day ranges, or a sprint — not in the body, not in tracker fields, not as a suggestion. **Engineering sizes its own work.** A PM-supplied estimate either gets treated as a commitment nobody made, or gets silently corrected and teaches everyone to ignore the field. Flag a ticket that looks too large to be one ticket by saying it may cover more than one domain change, which is a scope observation rather than a size.

## When to Use

- Breaking a PRD or spec into work engineering can pick up
- Turning meeting action items into tracked tickets
- Capturing a bug or request mid-flow (`--quick`)

## When NOT to Use

- To size or schedule work — that is `/sprint-planning`, with the engineers in the room
- To clean up an existing board — that is `/backlog-groom`
- When there is no spec yet — run `/prd-lite` or `/prd-draft` first

## Context Routing

| Source | Location | What to extract |
|--------|----------|-----------------|
| Source spec | The named PRD, `context-library/prds/` | Requirements, non-goals, open questions, and the section IDs to cite as sources |
| Ticket corpus | `references/tickets-corpus.md` | The team's real ticket shape; overrides the starting templates |
| Existing tracker state | `<TASK_TRACKER>` | Open epics and project structure; existing tickets covering the same domain change |
| Related in-flight work | `context-library/prds/`, `outputs/prds/` | Domain changes elsewhere that this one depends on or duplicates |
| Metrics and research | `<METRICS_SOURCE>`, `context-library/research/` | The evidence behind any behavioral or impact claim a ticket makes |

For live tool data, route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected.

## Workflow

### 1. Read the source to resolution

Read the whole spec, not the requirements list. Non-goals and open questions determine ticket boundaries as much as requirements do.

### 2. Cut by domain change

List the distinct changes in behavior. Each one is a candidate ticket. Resist the surface split — if the schema, the endpoint, and the screen all move so that one behavior changes, that is one ticket. Then check each candidate against the tracker: a domain change already covered by an open ticket is not a new ticket.

### 3. Pick the type, then fill its section set

Bug, behavior change, chore, or spike — each has its own sections. Read `references/ticket-templates.md` for the four section sets, the type-selection table, and the rules that bind all of them.

### 4. Source every claim as you write it

Attach the pointer at the moment you write the sentence. Sourcing afterward is where invented citations come from. Where the source is genuinely a person's recollection, say so and name them rather than dressing it as a spec reference.

### 5. Name the open questions

Every ambiguity the spec did not settle goes into the ticket's Open questions with **who can answer it**. These are the writeback targets below, and a ticket that hides its ambiguities relocates them into a thread nobody will find later.

### 6. Create or emit

Read `references/modes-and-integration.md` for tracker creation, field-mapping cautions, dependency reporting, and the `--quick` and `--stories` modes. Nothing is created until the user approves the batch.

## The Writeback Loop

**An answer that resolves a ticket's ambiguity lands in the ticket before the thread that produced it closes.**

Ambiguities in tickets get resolved somewhere else — a chat thread, a hallway answer, a design review, a comment on a different ticket. The answer arrives, everyone present understands it, the thread goes quiet, and the ticket still says `[TBD]`. Whoever picks the work up later finds the question and not the answer, and asks it again.

The loop:

1. A ticket ships with an Open question naming who can answer it.
2. When that question gets answered anywhere, **edit the ticket description first** — before replying in the thread, before closing it, before moving on.
3. Write the answer into the description as a resolved statement with its source: who answered, where, and when. Do not leave it as a comment; comments are not read by whoever picks up the ticket.
4. Only then close the thread.

The ordering is the whole rule. Reply-then-update becomes reply-and-forget within one context switch, and the thread — which is the only remaining copy of the answer — is exactly the thing that gets archived.

When this skill runs and finds a ticket whose Open question was answered in a source it has read, it proposes the description edit as part of its output. Per `references/protocols/knowledge-capture.md` the edit is proposed and never written unprompted, since a ticket is a shared system other people are acting on.

## Output Quality Self-Check

- [ ] **Cut by domain change** — no ticket exists only because a change touched another surface
- [ ] **Type chosen and its section set used** — not a universal body across all four types
- [ ] **Every behavioral claim sourced** — inline pointer to PRD section, thread, ticket, research, or query
- [ ] **No implementation prescribed** — outcomes and constraints, never tables, endpoints, or libraries
- [ ] **No estimate, no story points, no sprint** — in the body or in any tracker field
- [ ] **Acceptance criteria only where "done" is ambiguous** — none padded to hit a count
- [ ] **Open questions carry an owner** — each names who can answer it
- [ ] **Dependencies stated where real** — with no duration attached to the chain
- [ ] **Nothing created before approval** — the commitment gate ran and the user said go

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it three things: the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Common Mistakes

- Splitting one behavior across `[Frontend]` / `[API]` / `[DB]` tickets, then reporting the dependency chain it created as if it were a finding
- Writing "users expect X" with nothing behind it
- Specifying the schema or the endpoint shape, which reads as a requirement engineering has to argue out of
- Filling in a sizing field because the tracker marks it required
- Generating three acceptance criteria that restate the title
- Leaving `[TBD]` in a ticket after the answer arrived in a thread

## Cross-Skill Links

- `/prd-draft` or `/prd-lite` -> before ticketing, when there is no spec to break down
- `/execution-plan` -> before ticketing, when the work needs phasing first
- `/sprint-planning` -> after ticketing, when the tickets need sizing and committing with the engineers
- `/backlog-groom` -> when the board is cluttered enough that new tickets will get lost
- `/meeting-notes` -> when the tickets come from meeting action items, or when a meeting answered a ticket's open question
- `/code-review` -> when the tickets originate from confirmed review findings
