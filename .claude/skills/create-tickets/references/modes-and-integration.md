# Modes and Tracker Integration

Bulk reference for `/create-tickets`. Read when running a mode or writing to a tracker.

## Mode: --quick (fast issue capture)

Capture a bug or request mid-development without the full ceremony. You are in the zone and thought of something; log it and get back to work.

```
/create-tickets --quick
/create-tickets --quick "Login button broken on mobile Safari"
```

**Time:** Under 60 seconds. Total interaction: 1-2 messages.

Captures five fields: title, one-or-two-sentence summary, current vs expected, files involved (auto-detected from the working context where possible, max 3), and priority (default Medium).

**How it behaves:** ask only what is missing — a one-liner like "login broken on mobile" earns one or two targeted follow-ups, never a checklist. Skip everything else; a quick capture is not a specification.

**Output.** With a tracker connected, creates the ticket with a `triage` label. Otherwise appends to `outputs/analyses/quick-issues-[date].md`:

```markdown
### [Title]
**Type:** Bug / Behavior change / Chore
**Priority:** Medium
**Summary:** [1-2 sentences]
**Current:** [What happens now]
**Expected:** [What should happen]
**Source:** [Where this came from — thread, session, report]
**Logged:** [timestamp]
```

**What --quick does not do:** no acceptance criteria, no sizing, no dependency mapping. The `triage` label is the signal that the ticket needs a real pass before anyone works it.

## Mode: --stories (user story format)

Generate tickets as user stories focused on outcomes.

```
/create-tickets --stories
```

Ask for: the feature or epic, the user types involved, and the job they are trying to get done.

```markdown
## Story: [Title in action format]

**As a** [specific user type],
**I want** [capability],
**So that** [outcome].

**Behavior:** [What must be true. Each claim sourced.]

**Acceptance criteria:** [Given/When/Then — only where "done" is ambiguous. Delete otherwise.]

**Out of scope:** [Explicit exclusions]

**Open questions:** [Each with who can answer it]

**Source:** [PRD section, research, decision doc]
```

**INVEST, minus the E.** Check each story is Independent, Negotiable, Valuable, Small, and Testable. **Estimable is deliberately not checked here** — whether a story can be sized is engineering's judgment to make when they size it, and a PM ruling on it is the same overreach as supplying the estimate.

## Tracker integration

Create tickets only after the commitment gate has run and the user has approved the batch. Creation is a write to a shared system other people act on.

**Linear.** Create the parent issue first, then children with `parentId` set. Carry the type as a label so the section set on the page matches the type in the tracker.

**Jira.** Create the epic first, then stories with `epic_link` set. Map the four types to the project's own issue types rather than assuming Story/Task/Bug exist as named.

**Neither connected.** Emit copy-paste text, one block per ticket, with the type named at the top:

```
=== TICKET 1 — [Type] ===
Title: [Title]
Project: [Project]
Priority: [Priority]

[Body, using that type's section set]
```

**Field mapping caution.** Do not populate estimate, story-point, or sprint fields, even where the tracker exposes them and even where they are required to save. If a required field blocks creation, stop and tell the user which field the tracker is demanding — that is a decision for them and their engineers, not one to fill in with a guess.

## Dependencies

State dependencies where they exist, in the ticket:

```markdown
## Dependencies
- **Blocked by:** TICKET-3 — [why, in a few words]
- **Blocks:** TICKET-7 — [why]
```

After a batch, give the dependency summary: the chains, the longest chain, and which tickets are independent. Report the chain as a sequence, not as a duration — **the critical path has no timeline attached here**, because that requires sizing.

Circular dependencies mean the tickets are cut wrong; restructure rather than annotate. A ticket with three or more blockers is usually one domain change that got split by surface — see the one-ticket-per-domain-change rule in `SKILL.md`.

## Early-stage or partial PRDs

When requirements are still fuzzy, the honest move is to say so on the ticket rather than invent precision:

- Raise a **spike** for each genuine unknown, with a timebox and the decision it unblocks
- Mark unresolved requirements `[TBD]` and name who resolves them, so they become writeback targets
- Do not write acceptance criteria for requirements that are still moving
- Do not skip the ticket — untracked fuzzy work is still work

Open the batch with a note: "PRD is at [stage]. [N] tickets carry [TBD] requirements; each names who resolves it."
