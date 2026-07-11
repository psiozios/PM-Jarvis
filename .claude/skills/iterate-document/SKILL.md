---
name: iterate-document
description: Iterate a source-of-truth doc (plan, OKRs, strategy, roadmap, PRD, periodic review) based on what was learned since its last revision. Surgical deltas, not a rewrite. Validates numeric targets against the data source and confirms before any fundamental rewrite.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

**What to provide:** The doc to iterate (path or pasted content) and what's changed since it was last touched — new data, a decision, a shipped milestone.

```
/iterate-document <path or doc type>
[what's new since the last revision]
```

**What you get:** A surgical delta applied directly to the source doc — not a regenerated rewrite. Numeric targets are checked against the live data source before being restated. A fundamental rewrite only happens with explicit confirmation.

**Time:** A few minutes.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice, and honors whatever writing rules the target doc itself already carries (a PRD's own section conventions, a strategy doc's own format). This skill carries no independent voice rules of its own.

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Target doc | local file or external store (`<DOCS_HUB>`) | Current content, last-revised date if tracked |
| Metrics source | `<METRICS_SOURCE>` | Live values for any numeric target the doc states, to validate before restating |
| What's new | user input for this run | The specific learning driving the iteration |

## Workflow

### 1. Read the current doc in full

Don't skim. Understand its existing structure and claims before touching anything.

### 2. Identify what actually needs to change

Map "what's new" onto the doc's existing sections. Most iterations are localized — a target updates, a risk resolves, a milestone ships and its status flips. Identify exactly which sections are affected.

### 3. Validate numeric targets

Before restating any number (a metric, a date, a target), check it against `<METRICS_SOURCE>` rather than trusting the input as given. If the source and the stated update disagree, surface the discrepancy rather than silently trusting one.

### 4. Apply a surgical delta

Edit only the affected sections. Preserve everything else exactly as it was — structure, phrasing the user has already refined, sections unrelated to this update. This is not a regenerate-from-scratch pass.

### 5. Honor the doc's own rules

If the doc has its own section conventions or a stated writing style (a PRD template's required sections, a strategy doc's framework), keep the edit consistent with them rather than imposing a different structure.

### 6. Confirm before any fundamental rewrite

If the requested change is large enough that a surgical delta isn't really possible — the doc's premise itself has changed — say so explicitly and ask before doing a fundamental rewrite. Don't silently escalate a small ask into a full regeneration.

### 7. Apply directly to the source

Once the delta is confirmed, apply it directly to the source doc (local file or external store) — this skill's whole purpose is keeping the source of truth current, not producing a separate draft copy.

## Output Format

```markdown
# Iteration — <doc name>

## What Changed
- <section>: <what was updated and why>

## Numeric Targets Validated
- <target>: stated <value> — source confirms <value> (match / discrepancy flagged)

## Delta Applied
<diff-style summary: what was added/changed/removed, not a full reprint of the doc>
```

## Runs as a Routine

Can run as a routine when the trigger is periodic (e.g., re-validate numeric targets against the metrics source on a schedule) — see `references/protocols/routines.md` and `setup/routine-setup.md`. Otherwise on-demand, triggered by a specific piece of new learning.

## Output Quality Self-Check

- [ ] Only the affected sections changed — unrelated content is untouched
- [ ] Every restated numeric target was checked against the live metrics source
- [ ] Any discrepancy between the input and the source was surfaced, not silently resolved
- [ ] The doc's own existing writing rules and structure were honored
- [ ] A fundamental rewrite was proposed and confirmed, never applied silently in place of a delta

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Related:** `editing-assistant` (voice/clarity/audience edits on any doc; this skill is for content updates driven by new learning, not prose polish — chain them: iterate first, then polish)

## When to Use

- When a source-of-truth doc needs to reflect a real update — new data, a decision, a shipped milestone — without a full rewrite

## When NOT to Use

- For a prose/voice/audience edit with no new underlying information — use `editing-assistant`
- For reconciling two copies of the same doc (a local file vs. an external export) — use `sync-doc`

## Common Mistakes

- Regenerating the whole doc when only one section actually changed
- Restating a numeric target without checking it against the live data source
- Escalating a small update into a full rewrite without confirming first
