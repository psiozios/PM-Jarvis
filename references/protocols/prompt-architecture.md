# Prompt Architecture

**Why this exists.** This workspace holds no source code. These markdown files *are* the codebase: an always-on core, a protocol layer, 87 skills, and the routine prompts. A design principle nobody can read is a principle the agent cannot follow, so the shape rules are written down here rather than left to convention.

## 1. The layer map

| Layer | File(s) | Scope | When loaded |
|-------|---------|-------|-------------|
| **0** | `CLAUDE.md` | Always-on core: absolute rules, routing, output philosophy | Every turn |
| **0** | `hooks/inject_memory.py` (optional) | Memory index injection | Every turn, if the hook is installed |
| **1** | `config/house-style.md` | Anti-slop writing standard | Before drafting any prose |
| **1** | `config/persona.md` | Interaction style | When interaction defaults are in question |
| **1** | `references/protocols/prompt-architecture.md` | This file — file shape and conformance | When creating or editing a skill or protocol |
| **1** | `references/protocols/context-acquisition.md` | Read-freely protocol | Before producing output from context |
| **1** | `references/protocols/knowledge-capture.md` | Write-on-confirm protocol | When a run yields a durable learning |
| **1** | `references/protocols/skill-evals.md` | Eval protocol | Every skill invocation; when creating a skill |
| **1** | `references/protocols/skill-patterns.md` | Reusable skill archetypes | Before building a radar / review / grooming skill |
| **1** | `references/protocols/routines.md` | Scheduled-work protocol | When defining or running a routine |
| **1** | `references/protocols/notifications.md` | Notifier contract | When a routine reports out |
| **1** | `references/protocols/commitment-gate.md` | Commitment gating | Before acting on a user commitment |
| **1** | `references/protocols/freshness-provenance.md` | Dating and sourcing | When an artifact asserts point-in-time state |
| **1** | `references/mcp-routing.md` | Live-source routing | When a task wants live tool data |
| **1** | `references/file-creation-rules.md` | Output taxonomy | Before writing any new file |
| **1** | `references/skill-chains.md` | Multi-skill sequences | When chaining beyond one nudge |
| **1** | `references/skill-categories.md` | Library shape, framework ownership | Before a second skill teaches an existing framework |
| **1** | `references/absolute-rules.md` | Lookup tables behind the core's rules | When a draft trips an absolute rule |
| **1** | `references/capabilities.md` | Parallelism, plan mode, web, code | When choosing an execution mode |
| **1** | `references/sub-agents.md` | Reviewer persona roster | When spawning a review panel |
| **2** | `.claude/skills/<name>/SKILL.md` | One skill's method | On invocation |
| **2a** | `.claude/skills/<name>/references/*.md` | That skill's bulk reference | On pointer, inside the skill |
| **2** | `.claude/skills/<name>/evals.md` | That skill's scored checks | By the eval agent, post-output |
| **3** | `routines/<name>/SKILL.md` | A schedule wrapped around a skill | On schedule |

**Path convention.** Two directories in this repo are called `references/`. Inside a `SKILL.md`, a bare `references/<file>.md` means **that skill's own** directory. A path starting `references/protocols/` or `references/<file>.md` written from the repo root means the **layer-1** protocol layer. A skill needing both in one file writes the layer-1 path in full from the repo root.

**The layer-1 split is historical.** Eight files sit under `references/protocols/` and five directly under `references/`. The table above is the index. **Do not move these files to tidy the split** — they are referenced by path from routine prompts, from `CLAUDE.md`, and from every skill, and a move breaks all of them silently.

## 2. The nine rules

**1. One home per rule.** Every rule lives in exactly one file; everything else carries a pointer. *Test:* if you are about to paste text you could grep for elsewhere, write the pointer instead.

**2. Downhill only.** Context flows 0 → 1 → 2 → 3. A lower layer may point up. It may never restate what a layer above it says.

**3. Thin wrapper.** A caller declares what to run and adds its own constraints, never restating the callee's method. Binds routines calling skills, skills calling protocols, and skills calling skills.

**4. Lightweight guide.** A `SKILL.md` tells the agent how to find and do the thing. Bulk reference — catalogs, worked examples, mode variants, long templates, troubleshooting trees — goes to `<skill>/references/`. **Over budget means extract, never delete.**

**5. Conditional load.** Every pointer states its trigger: read X **when the task touches** Y. A pointer with no trigger gets read always or never, and both are wrong.

**6. Specialize, do not restate.** Naming a global rule and adding what it means **for this skill's output** is correct and stays. Naming it and re-listing the same substitutions is duplication and goes. *Test:* does the block name a failure mode specific to this skill? If yes, keep. If no, cut to a pointer.

**7. One name per concept.** Use the canonical table in §4. Add a new concept to that table **before** using it in a second file. *Selection rule for future entries:* the shortest spelling that is still unambiguous.

**8. Outline hygiene.** `##` headings describe the skill. Template bodies, example output, and sample artifacts get fenced or extracted. *Test:* if `grep '^## '` on a `SKILL.md` does not read like a table of contents, the file is broken.

**9. Reachable, not resident.** Content that must exist but is not needed on every invocation goes behind a pointer. Content nothing points to gets **deleted, not archived**.

## 3. Size budgets

| File | Target | Ceiling | Over budget → |
|------|--------|---------|---------------|
| Always-on core (`CLAUDE.md`) | 140 | 170 | Move lookup tables out; rules stay |
| Protocol (layer 1) | 80 | 130 | Split by concern, or extract worked examples |
| Standard (layer 1) | 130 | 160 | Tighten prose only — the catalogs stay resident |
| `SKILL.md` | 120 | 150 | Extract to `<skill>/references/` (rule 4) |
| `<skill>/references/*.md` | — | — | No budget; this is where bulk lives |
| `evals.md` | 70 | 90 | Consolidate checks; do not drop coverage |
| Routine prompt | 100 | 140 | Push method back into the skill it wraps |
| Frontmatter `description` | 200 chars | 350 chars | Cut method, keep triggers and constraints |

**Deriving the `SKILL.md` ceiling — from this repo, not by analogy.** The fourteen automation-layer skills are the newest and most operationally precise in the tree: `weekly-readahead` 101, `sync-doc` 102, `proactive-gaps` 110, `iterate-document` 113, `refinement-prep` 114, `chat-ingest` 115, `meeting-prep` 119, `monthly-review-fill` 122, `quarterly-review-fill` 124, `backlog-groom` 125, `weekly-review-fill` 125, `routine-responder` 127, `action-sweep` 130, `loose-threads` 131. They span 101-131 with a mean of 118 and carry more operational precision than any legacy skill at five times the length. Target 120 sits at that mean; ceiling 150 leaves headroom above the observed maximum without licensing a return to 400.

**Why protocol and standard are separate rows.** Originally one row at 80/130. Then both layer-1 standards written this round breached it — `config/house-style.md` at 146 after two adversarial verification runs forced in fixes that could not be cut, and this file at 135 after the audit corrected its own canonical table. Meanwhile every *protocol* file in the tree sits at 36-95 and fits the original budget with room. That is the distinction: a **protocol** describes one process and stays short; a **standard** carries catalogs and lookup tables — the P1-P18 patterns, the canonical-names table, the ten check classes — that must be **resident** where they are used. The generic remedy, "extract worked examples", is wrong for a standard: putting the pattern catalog behind a pointer means the drafting agent does not have it while drafting, which defeats the file's whole preventive purpose. **These rows split because the number was wrong, not because the files were.**

**Deriving the core's budget — from what is irreducible in it.** Each absolute rule needs its statement, its stakes, and its attribution **inline**, because the whole point of the core is that it fires *before* drafting rather than after a pointer is followed. Those lines do not move. What moves out is the lookup tables behind the rules — substitution lists, watch lists, evidence-grade vocabularies — to `references/absolute-rules.md`. The budget above is set from the rules plus routing that must stay, not from a number borrowed elsewhere.

**Frontmatter descriptions are the largest always-on cost here** — all 87 load every session regardless of which skill runs. Method belongs in the body; the description carries triggers and hard constraints only. Note the trade: right-sizing them for routing accuracy *raises* this cost, and that is the correct call, but it is a cost.

## 4. Canonical section names

| Concept | Canonical spelling | Retired spellings |
|---------|-------------------|-------------------|
| Invocation examples | `## Quick Start` | `## Usage`, `## Invocation`, `## Triggers` |
| Purpose | *(opening paragraph, no heading)* | `## Purpose`, `## Overview`, `## What This Does`, `## TL;DR` |
| Fit | `## When to Use` | `## When to Use This Skill` |
| No-fit | `## When NOT to Use` | `## When NOT to Use This Skill`, `## Scope`, `## Not For` |
| Sources to read | `## Context Routing` | `## Context Routing Logic (Internal - for Claude)`, `## Context Routing Logic (Internal)`, `## Context Routing Logic`, `## Context Routing Strategy`, `## Context Routing (Check Before Wireframing)` |
| Method | `## Workflow` | `## Step-by-Step Workflow`, `## Process`, `## How It Works`, `## Method` |
| Artifact shape | `## Output Template` | `## Output Format`, `## Output`, `## Deliverable` |
| Chaining | `## Cross-Skill Links` | `### Cross-Skill Integration`, `### Related Skills`, `## Next Steps`, `### Next Steps`, `## What's Next`, `## Next Step`, `## Follow-up Actions` |
| Failure modes | `## Common Mistakes` | `## Common Mistakes to Avoid`, `## Pitfalls`, `## Anti-Patterns`, `## Failure Modes` |
| Hard constraints | `## Binding Rules` | `## Behavioral Rules`, `## Rules`, `## Guardrails`, `## Non-Negotiables` |
| Reference material | `## Reference` | `## Further Reading`, `## Appendix`, `## Resources` |
| Self-check | `## Output Quality Self-Check` | `## Self-Check`, `## Quality Check`, `## Before You Ship` |
| Eval pointer | `## Formal Eval` | `## Evals`, `## Evaluation` |
| Arrow glyph | `->` | `→`, `=>`, `»` |

**Correction, 2026-07-26.** Five rows were rewritten after the baseline audit measured actual usage: the first draft named `## When to Use This Skill`, `## Fit`, `## Output`, `## Failure Modes`, and `## Hard Constraints` — spellings the tree barely used or did not use at all. Forcing 63 files into `## Fit`, or 41 into a `## Failure Modes` heading nothing used, would be the table bending the repo rather than describing it. Selection rule applied as written, weighted by what is dominant. Evidence: `## When to Use` 71 vs `## When to Use This Skill` 16; `## When NOT to Use` 58; `## Common Mistakes` 25 vs `## Common Mistakes to Avoid` 16; `## Output Template` 32 vs `## Output Format` 18; `## Quick Start` 78.

Concepts that **keep their own heading** because they are real and skill-specific: mode definitions (`## Mode: --<name>`), framework sections a skill owns and teaches, and worked examples the skill is the home of. A **specialized absolute-rule block** keeps its heading where rule 6 protects it — but as a bold lead-in rather than a `##`, so it stops occupying an outline slot in eighty-seven files.

**Chaining sub-rule.** Every chaining line names a skill **and** the condition that triggers it: `- /skill-name -> <trigger condition>`. The Before / After / Related sub-structure is **optional** — forcing three buckets manufactures content. A skill may omit the block entirely **only if it states why in one line**, so absence reads as a decision rather than an oversight.

## 5. Checking conformance

Ten check classes, each runnable with Grep, Glob, and Read alone. **There is no skill for this, on purpose:** an 88th skill auditing the other 87 would violate rule 1.

| ID | Check | Method |
|----|-------|--------|
| C1 | Three-file completeness | Every skill dir has `SKILL.md`, `evals.md`, `skill-memory.md`. Report the set difference. |
| C2 | Frontmatter conformance | Allowed keys only (`name`, `description`, `user-invocable`, `disable-model-invocation`). Flag unknown keys, near-miss spellings, a `name` not matching its directory, a description over ceiling. |
| C3 | Size budget | Line count per file against §3. For anything over, name the largest `##` section as the extraction candidate. |
| C4 | Verbatim duplication | Grep a sentinel from each known boilerplate block, count files. **Threshold: an identical run of 3+ lines that is not pure section scaffolding.** At this scale "appears in more than two files" flags every shared heading and tells you nothing. A shared skeleton with skill-specific bodies is convergence, not duplication — duplicated **rule text** is the finding. |
| C5 | Upward restatement | Grep the rule keywords, read the surrounding lines, classify each hit as restatement (cut) or specialization (keep, per rule 6). Flag any file carrying the same rule keyword on 3+ lines as within-file duplication regardless of classification. **Test the probe list before publishing it; drop any probe returning zero hits repo-wide.** |
| C6 | Canonical section names | Grep `^## ` per file, diff against §4. Also flag any file carrying two headings from the same concept row. |
| C7 | Dangling references | Glob every backticked `.md` path in the core, the layer-1 files, and every `SKILL.md` / `evals.md`; report misses with referencing file and line. Also check every `/skill-name` resolves to a real skill directory. |
| C8 | Outline hygiene | Flag files over 20 `##` headings; report any heading sitting inside an output-template block. |
| C9 | Protocol reachability, both directions | For each layer-1 file, count referencing files; flag any referenced by fewer than two. For each skill with a `## Context Routing` section, flag it if the table names no live source **and** carries no pointer to `references/mcp-routing.md`. |
| C10 | Surface collisions | Compare skill names and purposes against each other and against loaded plugin skills; report same-concept pairs. Duplication at the skill level costs more than duplication at the line level. |

**Severity:** **Blocker** where a reference resolves to nothing or a required file is absent. **High** where a rule lives in more than one place or a file is over ceiling. **Medium** for naming, outline, and overlap findings. **Low** for cosmetics.

Every audit report carries a **"Not findings"** section naming what was checked and is correct by design, so the audit is not re-litigated next run and nobody later "fixes" a deliberate choice.

## 6. Enforcement

- **Creating a skill:** copy the three templates (`templates/skill-template.md`, `templates/skill-evals-template.md`, `templates/skill-memory-template.md`). Procedure in `references/protocols/skill-evals.md`.
- **Editing a skill:** run C1, C2, C3, C6 against that file before committing.
- **After a batch:** run all ten and confirm the finding count fell.

**Where draft-time triggers live, and why not in the skills.** Some rules have to fire *before* an agent writes, so they cannot live in a `SKILL.md` tail. They belong on the always-on surfaces: `CLAUDE.md`, and the optional `UserPromptSubmit` hook (`hooks/inject_memory.py`, installed from `config/settings-template.json`) as the second. Adding the same pointer to 87 skill files would be exactly the duplication this standard exists to prevent — and it would still sit below the point where drafting begins.

If a skill genuinely needs a draft-time rule the global surfaces do not cover, it goes **at the top of that skill, above the workflow** — never in the self-check.

**Auditor's caveat.** Reading a `SKILL.md` in isolation makes these rules look absent. Check the core and any always-on layer before reporting a draft-time rule as unreachable.
