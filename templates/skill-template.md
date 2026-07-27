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

5. Use ONLY the headings below, in this order. Delete every section you do not
   need. Do not invent a heading — add it to the canonical table in
   `references/protocols/prompt-architecture.md` §4 first.

A short skill is a good skill.
-->

One paragraph on what this skill does and the job it is for. No heading — the purpose is the opening paragraph. Lead with the point.

## When to Use This Skill

```
/skill-name
/skill-name <argument>
/skill-name --mode
```

- "a thing a user would actually type or say"
- "another realistic phrasing, not the internal framework name"

## Fit

**Use this when:** the one-line condition that makes this the right skill.

**Not this when:** the nearest neighbouring skill and what sends you there instead.

## Context Routing

| Need | Source | Trigger |
|------|--------|---------|
| <what this skill needs> | `context-library/<path>.md` | when <condition> |
| Live source data | `references/mcp-routing.md` | when the task wants live tool data |

## Workflow

1. **<Step name>** — what the agent does, concretely.
2. **<Step name>** — the next thing.
3. **<Step name>** — where it stops and what it hands back.

## Output

Write to `outputs/<category>/<name>-<YYYY-MM-DD>.md` — see `references/file-creation-rules.md` for the taxonomy.

```markdown
# <Artifact Title>

## <Section>
<one line on what goes here>

## <Section>
<one line on what goes here>
```

<!-- The template above is fenced on purpose: its headings must not pollute this file's outline. -->

## Hard Constraints

- <A constraint that changes what this skill may do — read-only, preview-before-write, never auto-send.>

## Failure Modes

- **<Named failure>** — the tell, and what to do instead.

## Cross-Skill Links

- `/other-skill` -> when <condition that triggers it>
- `/another-skill` -> when <condition that triggers it>

<!-- Omit this section only if the skill genuinely has no chains, and say why in
     one line where it would have been, so absence reads as a decision. -->

## Reference

- `.claude/skills/<skill-name>/references/<topic>.md` — read when <condition>.

## Output Quality Self-Check

- [ ] Read `config/house-style.md` **before drafting** — the standard is preventive; the eval loop is the backstop.
- [ ] Output written to the path above, named per `references/file-creation-rules.md`.
- [ ] <A check specific to this skill's failure mode.>

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window; hand it the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.
