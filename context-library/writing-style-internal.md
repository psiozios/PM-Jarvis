<!-- TEMPLATE: Customize this file with your company's internal writing conventions.
     The structure and examples below are starting points. Replace placeholder values
     in [brackets] with your real preferences, add your own rules, and delete any
     sections that don't apply. -->

# Internal Writing Style

Use for team communication, PRDs, internal memos.

**Register basis:** `references/protocols/register.md`. The rules below are **axis two** — they describe how internal writing is *built*, and none of them is keyed to who outranks whom. Orthography comes from axis one, the named person, and belongs in that person's stakeholder profile rather than here. Every rule in this file should trace to a quote in a corpus (`config/house-style.md` §9); the starter rules below trace to nothing and are placeholders until you mine your own.

## Characteristics

**Tone:** Direct, collaborative, practical
**Audience:** Your team and colleagues
**Goal:** Get stuff done efficiently

## Rules

### 1. Be Direct
State the ask and the reason. Hedging costs the reader a round-trip to find out what you actually want.

- Avoid: "I would like to suggest that we might consider..."
- Better: "Let's do X because Y"

- Avoid: "Per our conversation..."
- Better: "Following up on our sync:"

### 2. Assume Context
Your team knows the background. Don't repeat it.

- Avoid: "As we all know, our company was founded in..."
- Better: "Update on [Quarter] roadmap:"

### 3. Make Asks Clear
Don't hint. Be explicit about what you need.

- Avoid: "It would be great if someone could look into this"
- Better: "@[Name] - can you review by [Day]?"

### 4. Don't Add Structure the Piece Doesn't Need
- Contractions, short sentences, and bullets are the default here — not a concession
- A message that won't be forwarded needs no headings and no restated context
- If it *will* be forwarded or decided from, it is an artifact: add the structure, keep the orthography

### 5. Link Context
Reference past discussions, docs, tickets.
- Link to project tracking tickets
- Reference Slack threads
- Cite previous decisions

## Examples

### PRD (Internal)
```
# [Feature Name]

## TL;DR
[Brief description]. [User need/evidence].
Expected to [impact metric] by [amount]. [Timeline] build.

## Why Now
- [Reason 1]
- [Reason 2]
- [Reason 3]
- [Reason 4]

## Approach
[Brief technical approach and rationale]

## Success Metrics
- [Metric 1]
- [Metric 2]
- [Metric 3]

## Open Questions
- [Question 1]
- [Question 2]

**Kickoff:** [Date]
**Review:** @[name] @[name] by [Date]
```

### Slack Update
```
[Emoji] [Update Title]

Winners:
[Result 1]
[Result 2]
[Result 3]

[Next step].

Full results: [link]
Questions: thread below
```

### Team Email
```
Subject: [Topic] - Input Needed by [Day]

Hey team,

[One sentence context].

**Action needed:**
[Action 1]
[Action 2]
[Action 3]

**Timeline:**
- Input: By [Date]
- Draft: [Date]
- Finalize: [Date]

**Context:**
- [Link 1]
- [Link 2]
- [Link 3]

Questions? Drop in #[channel] or DM me.

Thanks!
```

### Meeting Notes
```
## [Meeting Type] - [Topic]
Date: [Date]
Attendees: [Names]

**Decisions:**
- [Decision 1]
- [Decision 2]
- [Decision 3]

**Action Items:**
- [ ] [Name]: [Task] by [Date]
- [ ] [Name]: [Task] by [Date]
- [ ] [Name]: [Task] by [Date]

**Open:**
- [Open item 1]
- [Open item 2]

**Next sync:** [Date and time]
```

## When to Use
- PRDs and specs
- Team updates
- Slack messages
- Meeting notes
- Internal memos
- Planning docs
