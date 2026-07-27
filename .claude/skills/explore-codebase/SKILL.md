---
name: explore-codebase
description: Map the problem space in a codebase before anyone writes code — where the change belongs, what it touches, dependencies, edge cases, and the questions worth settling first. Deliberately does not implement. The cached output feeds execution-plan and code-first-draft.
user-invocable: true
disable-model-invocation: false
---

# /explore-codebase - Understand Before You Build

Your job is NOT to implement. It's to fully understand the problem space, map the relevant code, and surface questions before anyone writes a line of code. This is the "think before you build" checkpoint.

## Quick Start

```
/explore-codebase

Tell me:
1. What are you trying to build or fix?
2. Where in the codebase do you think it lives? (or "I have no idea")
3. Any constraints I should know about? (timeline, tech debt, specific patterns to follow)

I'll explore, map dependencies, identify edge cases, and ask you the questions
that matter before you start coding.

Output: outputs/analyses/explore-[topic]-[date].md
```

---

## Context Routing

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| PRDs | `context-library/prds/*.md`, `outputs/prds/*.md` | feature, requirement, scope | What was specified vs what exists |
| Strategy | `context-library/strategy/*.md` | priority, roadmap, milestone | Strategic context for the work |
| Past Analyses | `outputs/analyses/*.md` | explore, cto-consult | Prior exploration or CTO consultations |
| Codebase | Project source files | imports, exports, function signatures | Architecture, patterns, dependencies |

---


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected.

## When to Use

- Before `/code-first-draft` on any non-trivial feature
- When evaluating if a PRD is technically feasible
- When onboarding to an unfamiliar codebase or module
- When debugging something you don't fully understand yet
- When you need to explain technical constraints to stakeholders

## When NOT to Use

- Simple one-file changes (just read the file and do it)
- You already understand the code well
- You want to implement something (use `/code-first-draft`)

---

## Workflow

### Step 1: Understand the Request

Ask clarifying questions until the problem is clear. Don't explore blindly.

Questions to ask:
- What's the user-facing behavior you want?
- What exists today? (working feature to extend, or greenfield?)
- Are there patterns in the codebase you want me to follow?
- Any files or modules you already suspect are involved?

### Step 2: Detect and Map the Codebase

Explore the project structure:
- Framework and language detection
- Directory structure and naming conventions
- Key configuration files (package.json, tsconfig, etc.)
- Existing patterns (state management, routing, API layer, auth)

### Step 3: Trace the Relevant Code Path

For the specific problem:
- Identify entry points (routes, handlers, components)
- Follow the data flow (user action → UI → API → DB → response)
- Map file dependencies (imports/exports graph)
- Note shared utilities and helpers that could be reused

### Step 4: Identify Edge Cases and Risks

- What could break? (race conditions, null states, auth gaps)
- What's fragile? (tightly coupled code, no tests, hardcoded values)
- What's missing? (no error handling, no loading states, no validation)
- What assumptions does the existing code make?

### Step 5: Ask Follow-Up Questions

Based on what you found, surface questions that matter:
- Ambiguities in the requirements
- Architecture decisions that need to be made
- Trade-offs between approaches
- Dependencies on other work

### Step 6: Deliver Exploration Summary

Write a clear summary that someone could use to start implementing.

---

## Binding Rules

- **NEVER write or modify code.** This is read-only exploration.
- **Ask questions.** Don't assume requirements. If something is ambiguous, ask.
- **Map dependencies visually** when helpful (ASCII diagrams for data flow).
- **Be honest about complexity.** If something is harder than it looks, say so.
- **Note reusable code.** If a utility or pattern already exists that solves part of the problem, call it out.
- **Keep it conversational.** This is a back-and-forth, not a monologue. Explore, ask, explore more.

---

## Output Template

```markdown
# Codebase Exploration: [Topic]

**Date:** [date]
**Problem:** [What we're trying to build or fix]

---

## Codebase Overview

**Framework:** [e.g., React + TypeScript, Next.js, etc.]
**Key patterns:** [State management, API layer, component structure]
**Relevant conventions:** [Naming, file organization, test patterns]

---

## Relevant Files

| File | Purpose | Relevance |
|------|---------|-----------|
| [path] | [what it does] | [why it matters for this work] |
| [path] | [what it does] | [why it matters] |

---

## Data Flow

[How data moves through the system for this feature]
[ASCII diagram if helpful]

---

## Reusable Code

- **[utility/component name]** at [path] - [what it does, how it helps]
- **[pattern name]** - [existing pattern to follow]

---

## Edge Cases and Risks

1. [Risk] - [Why it matters] - [Mitigation]
2. [Risk] - [Why it matters] - [Mitigation]

---

## Open Questions

- [ ] [Question that needs answering before implementation]
- [ ] [Decision that needs to be made]

---

## Complexity Assessment

**Estimated complexity:** [Low / Medium / High]
**Reasoning:** [Why]
**Suggested approach:** [Brief recommendation for how to tackle this]
```

---

## Output Quality Self-Check

- [ ] **No code written or modified** - exploration only
- [ ] **Dependencies mapped** - relevant files and their relationships identified
- [ ] **Edge cases surfaced** - at least 2-3 risks or edge cases noted
- [ ] **Questions asked** - ambiguities surfaced, not assumed away
- [ ] **Reusable code identified** - existing utilities and patterns noted
- [ ] **Complexity honestly assessed** - not under- or over-estimated
- [ ] **Output saved:** `outputs/analyses/explore-[topic]-[date].md`


## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it three things: the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/execution-plan` -> after exploring, to turn the map into a tracked step-by-step plan
- `/code-first-draft` -> after exploring, to implement once the shape is clear
- `/cto-consult` -> when exploration raised an architecture question that needs pushback
- `/learning-mode` -> when you hit a concept in the code you do not understand
- `/prd-draft` -> when exploration shows the spec is technically infeasible as written
