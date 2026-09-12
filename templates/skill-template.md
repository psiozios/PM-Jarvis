---
name: skill-name-in-kebab-case
description: One sentence on what this does and when to reach for it. Carry the trigger vocabulary a user would actually say and any hard constraint that changes whether this is the right skill (read-only, preview-first, writes-on-confirm, draft-only, never-automated). Leave method out — it loads with the body. Ceiling 350 characters, target 200, because all 87 descriptions load into every session whether or not the skill runs.
user-invocable: true
disable-model-invocation: false
---

<!-- COPY PROCEDURE — delete this comment block before shipping.

1. Copy all three templates into `.claude/skills/<skill-name>/`:
     templates/skill-template.md        -> SKILL.md
     templates/skill-evals-template.md  -> evals.md
     templates/skill-memory-template.md -> skill-memory.md
   All three are required. See `references/protocols/skill-evals.md`.

2. SIZE BUDGET: target 120 lines, ceiling 150.
   Over budget means EXTRACT, never delete. Bulk reference — catalogs, worked
   examples, mode variants, long templates, troubleshooting trees — goes to
   `.claude/skills/<skill-name>/references/<topic>.md` behind a pointer.

3. NEVER RESTATE a rule that lives in the core or a protocol. Point at it.
   Naming a global rule and adding what it means FOR THIS SKILL'S OUTPUT is
   correct and stays. Re-listing the same substitutions is duplication and goes.

4. STATE YOUR TRIGGER on every pointer: "read X when the task touches Y."
   A pointer with no trigger gets read always or never, and both are wrong.

5. Use ONLY the headings below, in this order. These are the canonical
   spellings from `references/protocols/prompt-architecture.md` §4, in the
   order all fourteen automation-layer skills use. Delete every section you
   do not need. Do not invent a heading — add it to that table first.

A short skill is a good skill.
-->

One paragraph on what this skill does and the job it is for. No heading — the purpose is the opening paragraph. Lead with the point.

## Quick Start

**What to provide:** what the user has to bring, or "nothing required".

```
/skill-name
/skill-name <argument>
/skill-name --mode
```

**What you get:** the artifact in one sentence, including any hard constraint on it — read-only, draft-only, nothing written until confirmed.

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. Add only rules specific to **this skill's output**: a global rule named and specialized is correct, a global rule re-listed is duplication.

- <A constraint that changes what this skill may do — read-only, preview-before-write, never auto-send.>

## Context Routing

| Need | Source | Trigger |
|------|--------|---------|
| <what this skill needs> | `context-library/<path>.md` | when <condition> |
| Live source data | `references/mcp-routing.md` | when the task wants live tool data |

For live tool data, route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected. A source that is connected but fails — an expired credential, a revoked scope, an OAuth refresh with no browser — is reported unavailable by name with its reason and never listed among the sources swept (`references/protocols/source-preflight.md`).

<!-- If you add a Search Terms column, each term is its own query — one distinctive
     noun at a time, punctuation variants separately. See evidence-ledger.md. -->

## Workflow

### 1. <Step name>

What the agent does, concretely.

### 2. <Step name>

The next thing.

### 3. <Step name>

Where it stops and what it hands back.

## Output Template

Write to `outputs/<category>/<name>-<YYYY-MM-DD>.md` — see `references/file-creation-rules.md` for the taxonomy.

```markdown
# <Artifact Title>

## <Section>
<one line on what goes here>

## <Section>
<one line on what goes here>
```

<!-- The template above is fenced on purpose: its headings must not pollute this file's outline. -->

## Output Quality Self-Check

- [ ] Read `config/house-style.md` **before drafting** — the standard is preventive; the eval loop is the backstop.
- [ ] Output written to the path above, named per `references/file-creation-rules.md`.
- [ ] <A check specific to this skill's failure mode.>

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window; hand it the output (or its absolute path), this skill's `evals.md`, `config/house-style.md`, and the sources the output cites — E7 cannot be scored without them. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/other-skill` -> when <condition that triggers it>
- `/another-skill` -> when <condition that triggers it>

<!-- Omit this section only if the skill genuinely has no chains, and say why in
     one line where it would have been, so absence reads as a decision. -->

## When to Use

- <the one-line condition that makes this the right skill>

## When NOT to Use

- <the nearest neighbouring skill, and what sends you there instead>

## Common Mistakes

- **<Named failure>** — the tell, and what to do instead.

## Reference

- `.claude/skills/<skill-name>/references/<topic>.md` — read when <condition>.
