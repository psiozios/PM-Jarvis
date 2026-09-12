# Skill Memory Protocol

**Principle: A JOURNAL ENTRY IS A NOTE UNTIL IT CHANGES WHAT THE SKILL DOES.**

`skill-memory.md` is the third file in every skill directory, beside `SKILL.md` and `evals.md`. It follows the knowledge-capture protocol: propose, don't auto-write. Read this when a run produces a durable learning about the skill itself.

`skill-memory.md` follows the knowledge-capture protocol: propose, don't auto-write.

At the end of a skill run, if a durable learning about the skill itself was discovered:

1. Propose a specific entry (2-3 sentences, dated)
2. Wait for user confirmation
3. Prepend to the Entries section of `skill-memory.md`
4. If entries exceed 20, consolidate oldest into Archived Patterns
5. **If the confirmed entry changes how the skill should run, propagate it the same pass** — see "Memory-to-Method Feedback Loop" below. A journal entry that never reaches `SKILL.md` or `evals.md` is a note nobody acts on.

**What belongs in skill-memory.md:**
- Patterns that produce better output
- Edge cases the skill handles poorly and workarounds
- Context sources that proved especially valuable or misleading
- Structural improvements that worked well

**What does NOT belong:**
- Eval pass/fail results (those go in `evals.md` results log)
- User preferences (those go in `memory/`)
- Feature-specific context (that goes in `context-library/`)

### Memory-to-Method Feedback Loop

A `skill-memory.md` entry is a journal note until it changes what the skill actually does. When a confirmed entry describes a change to the skill's *method* (not just an observation), close the loop in the same pass:

1. **Update `SKILL.md`** — if the entry describes a better way to do a step, edit that step's instructions directly. The journal entry explains *why* the change happened; `SKILL.md` reflects the *current* method going forward — don't make a future run rediscover the same lesson from the journal.
2. **Update `evals.md`** — if the entry describes a failure mode worth guarding against permanently, add or tighten a check for it. This is exactly the trigger described in "Eval Versioning & Category Extension" above: if the new check doesn't fit an existing category, add one and bump `eval-version`.
3. Only entries that change method require this propagation. An entry that's purely an observation ("context source X was unusually rich this run") stays in `skill-memory.md` alone.

This closes the loop the four-category floor implies: informal self-check (SKILL.md) → formal eval (evals.md) → improvement journal (skill-memory.md) → back into SKILL.md and evals.md. Without step 3, the journal accumulates insight the skill never actually learns from.
