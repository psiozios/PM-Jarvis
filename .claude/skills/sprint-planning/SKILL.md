---
name: sprint-planning
description: Turn the backlog into a sprint the team can genuinely commit to — sprint goal, capacity against team size, estimates, sequencing, and readiness checks. Commits people to work, so a commitment gate runs first. Use backlog-groom for whole-board hygiene and refinement-prep to slate the next ceremony.
user-invocable: true
disable-model-invocation: false
---

# /sprint-planning - Turn Backlog into Sprint Commitment

Sprint planning fails when PMs dump tickets into a sprint and hope for the best. This skill makes it intentional: a clear sprint goal, realistic capacity, sequenced priorities, and a team that knows what they're committing to.

**Commitment gate:** Before committing work to a sprint, run the five checks in `references/protocols/commitment-gate.md`.

## Quick Start

```
/sprint-planning

Two modes:

--plan    Sprint planning: Set sprint goal, commit to work, sequence tickets
--groom   Backlog grooming: Refine, estimate, clarify, and prioritize backlog items

Tell me:
1. Mode: --plan or --groom?
2. Sprint length (1 week / 2 weeks / 3 weeks)
3. Team size (rough number of engineers)
4. What's the top priority for this sprint? (can be a feature, a metric goal, or a fix)

Output: outputs/analyses/sprint-[number]-plan-[date].md
```

---

## Context Routing

**Automatic Context Checks:**

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Active PRDs | `context-library/prds/*.md` | sprint, milestone, ready for dev | Features ready to be ticketed |
| OKRs | `context-library/strategy/*.md` | OKR, key result, quarterly goal | Sprint's contribution to quarterly goals |
| Previous Meeting Notes | `context-library/meetings/*.md` | sprint review, retro, blockers | Velocity data, carryover items |
| Decisions | `context-library/decisions/*.md` | prioritization, build vs buy | Context for what's in vs out |

---


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected.

## Sprint Planning Mode (`--plan`)

### Step 1: Set the Sprint Goal

A good sprint goal is:
- One sentence that describes the outcome (not a list of tasks)
- Specific enough to tell you if the sprint succeeded
- Aligned to the current quarter's OKRs

**Strong sprint goal:** "Ship the onboarding checklist so new users can complete setup in under 10 minutes"
**Weak sprint goal:** "Work on onboarding"

If you can't write a one-sentence goal, the sprint lacks focus. Identify the single most important thing and name it.

### Step 2: Capacity Planning

```markdown
## Sprint Capacity

**Team size:** [N] engineers
**Sprint length:** [N] weeks
**Total person-days:** [N engineers × N days × 0.6 focus factor*]

*Focus factor: engineers spend ~40% of time on meetings, reviews, support, and admin

**Adjustments:**
- PTO / holidays: -[N] person-days
- On-call / incident rotation: -[N] person-days
- Tech debt / chores allocation (typically 20%): -[N] person-days

**Available for feature work:** [N] person-days
```

### Step 3: Prioritize and Sequence

Use these criteria to stack-rank tickets:

| Criterion | Questions |
|-----------|-----------|
| OKR alignment | Does this move a Key Result? |
| Sprint goal fit | Does this contribute to the sprint goal? |
| Dependencies | Does something else need to ship first? |
| Risk | Is this high-uncertainty work? (Put earlier in sprint) |
| Size | Balance big and small tickets so engineers always have something to pull |

**Sequencing rule:** High-risk or high-dependency work goes in week 1. Polish and clean-up in week 2.

### Step 4: The Sprint Commitment

```markdown
## Sprint [N] Plan

**Dates:** [Start] → [End]
**Sprint goal:** [One sentence]
**OKR connection:** [Which OKR/Key Result this advances]

### Committed Work

| Ticket | Owner | Estimate | Priority | Notes |
|--------|-------|----------|----------|-------|
| [Ticket] | [Engineer] | [S/M/L] | P0 | [dependency] |
| [Ticket] | [Engineer] | [S/M/L] | P1 | |

**Total committed:** [N] person-days / [N] available — [X%] loaded

### Stretch (if time allows)
| Ticket | Owner | Estimate |
|--------|-------|----------|
| [Ticket] | [Engineer] | [S/M/L] |

### Explicitly NOT this sprint
- [Item] — deprioritized because [reason]
- [Item] — moved to next sprint because [reason]

### Dependencies and blockers
- [Dependency]: Expected resolution by [date], owner: [name]
- [Blocker]: [Action being taken]
```

---

## Backlog Grooming Mode (`--groom`)

Grooming is about making tickets ready to pull — not about deciding what to build next.

### What "Ready" Means (INVEST criteria)

A ticket is ready to pull when it meets these criteria:

- **I — Independent:** Can be worked on without waiting for other tickets
- **N — Negotiable:** Scope can be adjusted if needed
- **V — Valuable:** Clear outcome for the user or system
- **E — Estimable:** Engineer can give a rough estimate after reading it
- **S — Small:** Completable in a sprint (if not, break it down)
- **T — Testable:** Clear acceptance criteria — how will we know it's done?

### Grooming Checklist (per ticket)

```markdown
## Ticket Review: [Ticket Title]

**User story (if missing):** As a [user], I want [action] so that [outcome]
**Acceptance criteria (if missing or vague):**
- [ ] [Specific, verifiable condition]
- [ ] [Specific, verifiable condition]
**Estimate:** [S = <1 day / M = 2-3 days / L = 4-5 days / XL = >5 days (break it down)]
**Dependencies:** [None / Requires: ticket X]
**Ready to pull:** Yes / No — [what's needed to make it ready]
**Questions for engineering:** [Any unclear technical decisions]
```

### Grooming Session Agenda (60 min)

| Time | Activity |
|------|----------|
| 0-5 min | Review sprint goal and OKRs — why we're grooming what we're grooming |
| 5-45 min | Review top 10-15 backlog tickets: read, estimate, add AC, flag questions |
| 45-55 min | Identify tickets that need more work before next sprint |
| 55-60 min | Confirm backlog order and top 5 "ready to pull" tickets |

**Grooming output:** The top 5-10 backlog tickets should emerge from each session with:
- Clear acceptance criteria
- Rough estimates
- Dependencies identified
- Questions surfaced for the PM to answer before next sprint

---

## Common Sprint Planning Mistakes

**Mistake 1: Committing to 100% capacity**
Engineers are not machines. 60-70% actual feature velocity is realistic when you include reviews, bugs, and meetings.

**Mistake 2: No sprint goal**
Without a goal, any ticket "counts" as success. Teams optimize for throughput, not outcomes.

**Mistake 3: Putting all the risk in week 2**
High-uncertainty tickets go first. Discovering a blocker in week 1 gives you time to adjust. Discovering it on day 9 means the sprint fails.

**Mistake 4: "We'll estimate in the sprint"**
Unestimated tickets that turn out to be XL blow up the plan. Groom first.

**Mistake 5: Grooming without the engineers**
The PM decides what to build. The engineers decide how long it takes. Grooming without them produces fictional estimates.

---

## Where Files Go

`outputs/analyses/sprint-[number]-plan-[date].md`

---

## Cross-Skill Links

- `/backlog-groom` -> before planning, for whole-board hygiene so stale and duplicate items do not reach the sprint
- `/refinement-prep` -> before planning, to slate and enrich the shortlist the ceremony works from
- `/prioritize` -> when priorities are contested and need LNO classification first
- `/prd-draft` or `/prd-lite` -> when a candidate has no spec to estimate against
- `/create-tickets` -> when sprint items need formatting with acceptance criteria; `--stories` for INVEST
- `/okr-planning` -> when the sprint goal needs to ladder to a Key Result
- `/meeting-notes` -> after the sprint, to process review and retro

## Output Quality Self-Check

- [ ] **Sprint goal is one sentence:** Specific outcome, not a list of tasks
- [ ] **Capacity calculated:** With focus factor and adjustments applied
- [ ] **Load % reasonable:** 60-80% for sustainable pace, flagged if over 85%
- [ ] **Not-this-sprint documented:** Explicit deprioritization with reasons
- [ ] **Dependencies flagged:** Each dependency has an owner and expected resolution date
- [ ] **For grooming: AC added:** Every reviewed ticket has testable acceptance criteria
- [ ] **Output saved:** `outputs/analyses/sprint-[number]-plan-[date].md`


## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it three things: the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## When to Use

- Sprint planning and backlog grooming.

## When NOT to Use

- When a different skill better fits the task. Check Cross-Skill Links for alternatives.
