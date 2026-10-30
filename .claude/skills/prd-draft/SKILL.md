---
name: prd-draft
description: Write the full PRD for a feature in themes, not teams — overview, problem, business metrics, constraints, solution, rollout, open questions — on graded evidence, through guided questions, then offer the review panel. `--retro` documents a product already shipped. Use prd-lite for a quick proposal before a feature is slated.
user-invocable: true
disable-model-invocation: false
---

The spec engineering builds from, written so every claim carries its evidence and every reader finds the same themes in the same order.

## Quick Start

**What to provide:** A feature idea, problem statement, or rough brief. Detailed or rough both work.

```
/prd-draft                                → Start from scratch with guided questions
/prd-draft [paste your feature idea]      → Skip the questions you already answered
/prd-draft --stage "team kickoff"         → Set the PRD stage upfront
/prd-draft --ai                           → Include the AI behavior contract
/prd-draft --retro [product]              → Retro PRD for a product already shipped
```

**What you get:** A 1-2 page PRD in themes: overview, problem, business metrics and goals, legal and risk constraints, solution, rollout plan, open questions, and a collapsible appendix. Saved to `outputs/prds/[feature-name-kebab-case]-[stage].md` (e.g., `voice-task-capture-team-kickoff.md`). Based on `templates/prd-template.md`. 10-20 minutes for a first draft.

## Binding Rules

Defers to `config/house-style.md` for voice and word choice, and writes in the PM's own style from `context-library/writing-style-*.md`.

**Commitment gate:** When a PRD moves past proposal into committed scope, run the five checks in `references/protocols/commitment-gate.md`.

**Sections are themes, never teams.** This order, at every stage: 1. Overview (what it is, what it is not, why now) · 2. Problem (hypothesis; current implementation gaps) · 3. Business metrics and goals · 4. Legal, compliance and risk constraints · 5. Solution (approach; high-level design) · 6. Rollout plan · 7. Open questions with owners · a collapsible appendix holding the design-decisions table. No section is named for a team.

**Every stage carries every theme.** A short stage keeps a theme to one line. Business metrics and constraints never drop out: where none apply yet, the section says "None identified" and names what was checked.

**The brief rests on graded evidence.** These hold before a line is written:

- **Read the current code path first, read-only, when a codebase is connected** (`/explore-codebase` does the read). Name where today's system falls short under Problem → Current implementation gaps, each gap pointing at the file or function it was read from and graded **"inferred from the code"** until its engineer confirms. That engineer goes in Open questions as the owner of the confirmation.
- **Why now is external and sourced:** a market shift, a competitor move, a regulation, client research, each with its source. Internal metrics belong under Business metrics and goals.
- **Name the version of every contract, policy, or spec read, and read its comments, resolved ones included.** On one run, two rulings that bound the design lived only in resolved comments.
- **Summary lines keep the body's grade, in a neutral voice.** The overview, any TL;DR, and the announcement carry the same grades as the sections they summarize, because the doc ships under the user's name. One run's TL;DR stated code inferences as fact.
- Grades follow `references/absolute-rules.md` (measured, reported, estimated, inferred from the code, unsourced, unknown). Real quotes and real numbers beat "users want a better experience".

**Length is a target, scored, and never paid for with the user's words.** Body only; the appendix does not count.

| Stage | Target words | Focus |
|-------|--------------|-------|
| Team Kickoff | 300-500 | Overview, problem, one line per other theme |
| Planning Review | 500-800 | Business metrics and goals, alternatives in the design-decisions table |
| XFN Kickoff | 800-1200 | Solution approach and high-level design, mockups, constraints with sources |
| Solution Review | 1000-1500 | Edge cases, behavior, rollout plan |
| Launch Readiness | 1500-2000 | Kill criteria, rollback, comms, go/no-go |
| Impact Review | 500-800 | Actuals against targets, what we would do differently |

Up to 250 words over the top of the range passes, 251-500 over is PARTIAL, more fails. The remedy is moving the run's own detail into the appendix. **The user's own text is never cut to hit a number**; where it alone keeps the count over, say so and leave it.

**AI features carry the behavior contract** under High-level design (task, inputs, constraints, disallowed behavior, latency budget, and a happy-path / edge-case / should-reject table); non-AI features carry the user flow and edge cases. Read `references/ai-features.md` when the feature is AI-powered.

## Context Routing

| Source | Location | What to Extract |
|--------|----------|-----------------|
| Strategy docs | `context-library/strategy/*.md` | The goal or pillar it serves |
| Related PRDs | `context-library/prds/*.md`, `outputs/prds/` | Dependencies, cross-functional impact |
| User research | `context-library/research/*.md` | Pain points, verbatim quotes, frequency |
| Business model | `context-library/business-info-template.md` | Revenue impact, North Star alignment |
| Competitor analysis | `context-library/research/competitive-*.md` | Positioning, and external why-now evidence |
| Stakeholders | `context-library/stakeholder-template.md` | Who owns which open question |
| Second brain | `context-library/second-brain/` `product-knowledge`, `customer-insights`, `competitive-intelligence`, `decisions` | Cited background for Overview and Problem |
| Current code path | the connected codebase, read-only (via `/explore-codebase`) | Where today's system falls short, graded "inferred from the code" |
| Contracts, policies, specs | `<DOCS_HUB>`, `context-library/` | The version read, and every comment, resolved ones included |

Priority: strategy and related PRDs first, then research and the problem, then business context and metrics, then competition. If `business-info-template.md` still holds placeholder brackets, or strategy docs are empty, say so and offer to fill them (or `/write-prod-strategy`) before drafting. If the second brain is thin on the topic, flag the evidence gap at the top of the PRD.

For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected. A source that is connected but fails — an expired credential, a revoked scope, an OAuth refresh with no browser — is reported unavailable by name with its reason and never listed among the sources swept (`references/protocols/source-preflight.md`).

## Workflow

**Read `references/conversation-scripts.md` when you are about to speak to the PM at any step below** — it holds the opening, the context check, the follow-ups, and the hand-offs, verbatim.

1. **Read context, then ask only the gaps.** Read the sources above and the code path, then summarize what you have and ask only what is missing: the problem, the hypothesis, the goal it serves, the stage, what it is not, the metric. Never ask about implementation details, exhaustive edge cases, or final copy and UI.
2. **Draft.** Fill `templates/prd-template.md` in theme order at the stage's length, every claim graded. Save to `outputs/prds/`.
3. **Offer a prototype** (optional): a napkin sketch, a tool prompt, or a flow, per the scripts file.
4. **Offer review:** `/prd-review-panel` runs seven perspectives in parallel.
5. **Iterate surgically.** **Read `references/iteration.md` when the PM asks for a revision.** For the end-to-end process around the draft, per-stage adjustments, the second-brain query, and where the PRD goes next, **read `references/full-workflow.md`.** A finished PRD moves to `context-library/prds/` only when the user moves it.

## Output Quality Self-Check

- [ ] Saved to `outputs/prds/` as `[feature-name-kebab-case]-[stage].md`
- [ ] Themes in order at every stage, metrics and constraints present even as "None identified" plus what was checked
- [ ] Body within 250 words of the stage target, appendix excluded, the user's own text untouched
- [ ] Current implementation gaps read from the code, each graded "inferred from the code" with its confirming engineer owning an open question
- [ ] Why now external and sourced; every contract, policy, or spec named with its version, comments read
- [ ] No summary line states as fact what its section grades lower, and none speaks as the user
- [ ] Hypothesis testable ("If we... then... because..."); goals cite actual strategy; each non-goal says why
- [ ] Metrics have baselines, targets, and dates; kill criteria are a threshold the team would act on, with an owner
- [ ] Every open question has an owner; at least one real quote where research exists
- [ ] Reads naturally aloud (`config/house-style.md` §5 P11, §7); name the defect, never the author

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it the output (or its absolute path), this skill's `evals.md`, `config/house-style.md`, and the sources the output cites — E7 cannot be scored without them, and scoring it from plausibility is a vacuous PASS. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Mode: --retro

A PRD for a product already shipped. **Read `references/retro-mode.md` when the run is `--retro`** — it carries the method and the shape. The rules:

- **Intended behavior comes from the user; the code is what gets checked.** Ask what it was meant to do before reading anything.
- **The core is a four-way cross-check:** code, contract, sales and ops material, ticket acceptance criteria. Every disagreement is a gap under Current implementation gaps, with an owner in Open questions.
- **Same themes, past tense. No rollout plan. A review trigger instead of kill criteria**, which evals score N/A, never PASS.
- **Status is date-stamped or linked live**, and "shipped" is two claims (`references/protocols/freshness-provenance.md` rule 5).

## Mode: --brief

Alias for `/prd-lite`, which owns the pre-commitment feature brief. Run `/prd-lite` instead — same artifact, and it is the skill that is maintained.

## Cross-Skill Links

- `/prd-lite` -> when the feature is not yet slated; write the short proposal first and escalate here
- `/user-research-synthesis` -> when the user problem is asserted rather than evidenced
- `/impact-sizing` -> when Business metrics and goals has no numbers behind it
- `/feature-metrics` -> when Business metrics and goals needs a primary metric, guardrails, and kill criteria
- `/write-prod-strategy` -> when the goal it serves is unclear and there is no pillar to point at
- `/second-brain` -> before drafting, to pull cited background from `product-knowledge` and `customer-insights`
- `/prd-review-panel` -> after drafting, for seven-perspective review before stakeholders see it
- `/create-tickets` -> after approval, to break the spec into engineering work
- `/launch-checklist` -> when the spec is settled and the launch needs planning
- `/feature-results` -> when a `--retro` run turns up a missed target rather than a spec gap

## When to Use

- Starting a new feature or initiative, or moving from prototype to formal spec
- Aligning cross-functional stakeholders, or preparing for a planning review
- Writing down what an already-shipped product does, and where it disagrees with what it was meant to do (`--retro`)

## When NOT to Use

- Before the feature is slated — `/prd-lite` is the decision-grade proposal
- To measure a shipped feature's results against its targets — that is `/feature-results`

## Common Mistakes

- **A section named for a team**, or a theme dropped at an early stage instead of kept to one line
- **Code inferences stated as fact**, in the body or, worse, in the summary line
- **An internal metric passed off as why-now**
- **A contract cited without its version**, or read without its resolved comments
- **Cutting the user's own text to hit the word target** instead of moving the run's detail to the appendix
- Generic claims ("increase engagement") where a number, a quote, or a named goal belongs
