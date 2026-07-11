---
name: meeting-prep
description: Assemble substantive prep for an upcoming meeting — attendee context, recent history, current priorities, real talking points and risks — pulled from workspace and second-brain context, never a blank agenda.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

**What to provide:** Nothing required — defaults to the next meeting on the calendar.

```
/meeting-prep                    → prep for the next upcoming meeting
/meeting-prep "<meeting title>"  → prep for a named meeting
```

**What you get:** Per-attendee context, recent history with them, current priorities, real talking points, decisions to push, and risks — grounded in what actually exists in the workspace, not a template with blanks.

**Time:** A couple minutes.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own.

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Calendar | `<CALENDAR>` | The target meeting: time, attendees, stated topic |
| Stakeholder profiles | `context-library/second-brain/stakeholders/`, `context-library/stakeholder-template.md` | Per-attendee priorities, communication style, open asks |
| Meeting history | `outputs/meeting-notes/`, `context-library/meetings/` | Last interactions with each attendee, prior decisions on this topic |
| Recent calls | `<CALL_TRANSCRIPT_SOURCE>` | Substantive context from recent shared calls, not just 1:1s |
| Priorities | `outputs/weekly-plans/`, `context-library/strategy/` | Current priorities that give the meeting a "so what" |

## Workflow

### 1. Identify the target meeting

Read `<CALENDAR>` for the next upcoming meeting, or match the named meeting if one was given.

### 2. Pull per-attendee context

For each attendee: their stakeholder profile (priorities, communication style, pet peeves), the last time the user met with them (date, topic, what was discussed), and any open asks in either direction.

### 3. Mine recent calls, not just 1:1s

Check `<CALL_TRANSCRIPT_SOURCE>` for substantive shared calls involving any attendee in the recent window — a group call often surfaces context a 1:1 history alone misses.

### 4. Pull current priorities

Read `outputs/weekly-plans/` and `context-library/strategy/` for what's currently top of mind — this is what gives the meeting's talking points a strategic "so what" instead of a status recap.

### 5. Assemble real talking points

Draft specific talking points, decisions worth pushing for, and risks worth naming — grounded in what steps 2-4 actually turned up. If a section has nothing to say, say so explicitly rather than filling it with a generic placeholder (see `references/protocols/skill-patterns.md` discipline #1 — verify and read to resolution before asserting).

## Output Format

```markdown
# Meeting Prep — <meeting title>, <date/time>

## Attendees
### <Name> (<role>)
- Last met: <date> — <what was discussed>
- Open: <asks owed either direction>
- Style: <from stakeholder profile, if present>

## What's Current
<the priorities/strategy context that makes this meeting matter right now>

## Talking Points
- <specific point, grounded in real context>

## Decisions to Push
- <decision worth getting resolved in this meeting, and why now>

## Risks
- <risk worth naming going in>
```

## Runs as a Routine

A natural first step in a daily chain — see `references/protocols/routines.md` and `setup/routine-setup.md`. `routines/example-daily-digest/SKILL.md` runs this skill first, ahead of `action-sweep` and `loose-threads`.

## Output Quality Self-Check

- [ ] Every attendee has real per-person context, not a generic placeholder
- [ ] At least one talking point ties to a current priority, not just meeting-topic small talk
- [ ] Recent shared calls were checked, not just 1:1 history
- [ ] If a section genuinely has nothing to say, that's stated explicitly rather than padded
- [ ] Deep links or file references point to the actual source, not a generic mention

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Before this:** `daily-plan` (surfaces the day's meetings)

**After this:** `meeting-agenda` (formalize into a structured agenda), `meeting-notes` (capture outcomes afterward)

**Related:** `second-brain` (stakeholder and topic context)

## When to Use

- Ahead of any meeting where showing up informed actually matters

## When NOT to Use

- For a meeting that's purely a status broadcast with no real stakes — `meeting-agenda`'s necessity diagnostic may be the better starting point

## Common Mistakes

- Producing a blank agenda template instead of substantive, grounded talking points
- Only checking 1:1 history and missing context from a recent group call
- Padding a section with generic filler instead of stating plainly that there's nothing new
