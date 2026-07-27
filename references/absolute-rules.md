# Absolute Rules — Lookup Tables

**This is a worked example set. Replace it with your own rules, or delete the examples and keep the shape.**

The rules themselves live in the Absolute Rules zone of `CLAUDE.md`, which is always in context. This file holds only the **lookup tables behind them** — substitution lists, watch lists, evidence-grade vocabularies. That split exists because a rule has to fire *before* drafting begins, while the table it consults can be fetched when a draft actually trips it.

**The mistake this file is designed to avoid:** a rule that keeps its stakes but loses its detection surface is a rule with teeth and no eyes. Every rule below keeps a **short inline tripwire** in `CLAUDE.md` — the handful of terms that actually show up — with the full table here behind the pointer. Moving the whole list out disarms the rule.

**Shape for each entry:** the rule restated in one line, a pointer back to the core, then the table.

---

## Example Rule 1 — No unsourced numbers

*Stated in `CLAUDE.md` Absolute Rules. Inline tripwire there: `roughly`, `about`, `~`, `most`, `majority`.*

Every quantitative claim carries an evidence grade. Ungraded numbers are the failure.

| Grade | Meaning | Written as |
|-------|---------|-----------|
| Measured | Read from a live source this run | `12.4% (metrics source, 2026-07-26)` |
| Reported | A person or document stated it | `12.4% (per the Q2 review doc)` |
| Estimated | Derived, with the derivation shown | `~12% (est. from 1.4k of 11.8k accounts)` |
| Unsourced | Believed but unverified | `12% [unsourced]` |
| Unknown | No basis at all | `[needs check]` — never a number |

Hedging words to watch, full list: roughly, about, approximately, around, some, most, many, majority, minority, significant, substantial, meaningful, material, sizeable, a fraction of, the bulk of.

## Example Rule 2 — No invented attribution

*Stated in `CLAUDE.md` Absolute Rules. Inline tripwire there: `the team`, `stakeholders`, `it was decided`.*

Where an artifact names an owner, a decision-maker, or a source, that name comes from context. A missing owner is flagged, never filled.

| Vague attribution | Correct handling |
|-------------------|------------------|
| "the team decided" | Name the people, or write `[decided by whom?]` |
| "stakeholders agreed" | Name them, or write `[which stakeholders?]` |
| "it was decided that" | Go active with the actor you have, or flag `[owner?]` |
| "experts say" / "studies show" | Cite the source, or grade the claim per Rule 1 |
| "users want" | Cite the research, or write `[which users? which study?]` |

## Example Rule 3 — Discussion is not decision

*Stated in `CLAUDE.md` Absolute Rules. Inline tripwire there: `we should`, `let's`, `agreed`.*

When writing up a transcript, thread, or meeting, a thing that was *discussed* is recorded as discussed. Promoting it to a decision is the failure.

| Heard in source | Records as |
|-----------------|-----------|
| "we should probably…" | Open question |
| "I think we're going to…" | Direction, not decided |
| "let's do X" (no dissent, no owner) | Proposal, owner unassigned |
| "we're doing X, <name> owns it, by <date>" | **Decision** |
| Silence after a proposal | Open question — not assent |

---

## Adding your own

1. Write the rule in the `CLAUDE.md` Absolute Rules zone: the statement, the stakes, the attribution, the datestamp, any exception. Those lines stay inline — they do not move here.
2. Leave a **short inline tripwire** in the core naming the terms that actually appear in real drafts.
3. Put the full table here under a matching heading, with the pointer line back to the core.
4. Optionally mirror the rule as a `feedback_` memory entry so the per-turn hook reinforces it. See `memory/README.md`.

Voice nuance — tone, sentence patterns, word preference — is not an absolute rule. It belongs in `config/house-style.md`.
