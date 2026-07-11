# Freshness & Provenance Protocol

**Principle: STATUS STALES FASTEST — NEVER BAKE A POINT-IN-TIME FACT INTO A STANDING DOCUMENT.**

This protocol is generic governance, not a personal voice rule — it applies to any workspace, any user. It has two halves: Side A is the three rules themselves (documented here, optionally mirrored into memory as `feedback_` entries). Side B is how these rules get enforced automatically, via a fifth universal eval check.

## Side A: The Three Rules

### 1. Never hardcode point-in-time status

Status — what's live, what's dropped, what's currently gating what — stales faster than any other kind of content. Derive it live from the actual current source (the tracker, the doc, the system of record) rather than asserting it from memory or from a document written weeks ago.

Treat strategy and plan documents as **directional**, not a status oracle. A roadmap says where the team intends to go; it does not reliably say what's true right now. If a status claim can't be confirmed fresh at the moment of use, say so explicitly — "unconfirmed" is a correct and useful answer; a confident guess is not.

### 2. Evergreen vs. ephemeral durability test

Before a line of content enters a living or shared document, classify it: **durable-external** (true regardless of who's watching it right now — a decision's rationale, a customer's stated need, a framework) or **ephemeral-internal** (true only as of right now — who's currently assigned, what sprint something is in, what the current blocker is).

Ephemeral state does not get asserted as standing fact in an evergreen document. Three options, in order of preference:
1. **Cut it** — if it adds nothing durable, leave it out.
2. **Route it to its live source** — link to the tracker/system of record instead of restating its current value.
3. **Quarantine it in one dated snapshot** — if a snapshot is genuinely useful, timestamp it clearly as a snapshot, not a standing claim.

When something ends (a decision reversed, a status changed, an initiative dropped), the fix is a new dated line — **"was X, no longer as of `<DATE>`"** — appended alongside the old claim, never an edit that silently overwrites it. Editing "in place" to correct stale status resets the reader's sense of how fresh the whole document is; a dated append tells them exactly what to trust and when it changed.

### 3. Shared artifacts cite only shared-accessible sources

A document other people can open must cite only sources those people can also open. Never cite a private note, a local-only file, or the assistant's own memory system as a source inside a document meant for shared consumption.

The local-to-shared boundary runs one way: content can move from local/private into a shared artifact once verified, but a shared artifact should never depend on something only the author can see. A citation nobody else can follow isn't a citation — it's an assertion wearing a citation's clothes.

## Side B: Eval Enforcement

`references/protocols/skill-evals.md` already carries four universal checks (E4-E7: no AI slop, house style, human-sounding, context-grounded) that every skill's `evals.md` inherits verbatim. This protocol adds a **fifth universal check — durability** — for any skill whose output is a document meant to persist or be shared, not a one-off draft consumed once.

**Durability check (wire into `templates/skill-evals-template.md` for output-producing archetypes — Document-Writer, Analysis, Research-Synthesis):**

> No volatile point-in-time status is asserted as standing fact. Ephemeral state is either dated ("as of `<DATE>`"), routed to its live source, or absent — never baked into the document as if it were permanent.

See `templates/skill-evals-template.md` for the exact wording as it appears wired into the universal checks block.

## Durable Enforcement (Optional Memory Mirror)

Like the commitment-gate and routines protocols, these three rules can be mirrored as `feedback_` memory entries via the format in `memory/feedback_example.md`, so the per-turn hook reinforces them even outside a session actively producing a shared document.

This protocol seeds **no real `feedback_` entry** — asserting one before the user has a concrete document or workspace to apply it to would itself violate rule #1 (a hardcoded, unearned claim). When the user's first shared, living document goes into `context-library/` or `context-library/second-brain/`, propose the relevant mirror per the knowledge-capture protocol (propose, don't auto-write).

## Cross-Reference

- `references/protocols/skill-evals.md` — where the four base universal checks live; this protocol's durability check is the fifth
- `references/protocols/knowledge-capture.md` — the propose-don't-auto-write discipline this protocol's memory mirror follows
- `context-library/second-brain/` — the second-brain wikis are the highest-risk surface for rule #1 and #2 violations, since they're explicitly designed to compound over time
