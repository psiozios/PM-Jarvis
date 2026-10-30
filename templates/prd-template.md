# PRD Template

> **How to use:** Copy this template for your feature, or run `/prd-draft` for guided creation. Sections are themes, never teams: there is no "Engineering" or "Legal" section, only the questions every reader needs answered, in this order.
>
> **Every stage carries every theme.** A short stage keeps a theme to one line. Business metrics and constraints never disappear: where none apply yet, write "None identified" and what was checked.
>
> **Stage word targets** (body only; the appendix does not count): Team Kickoff 300-500 · Planning Review 500-800 · XFN Kickoff 800-1200 · Solution Review 1000-1500 · Launch Readiness 1500-2000 · Impact Review 500-800. Up to 250 words over the top of the range passes; 251-500 over is a partial; more fails. Move detail to the appendix rather than cutting the author's own words.

---

**Stage:** Team Kickoff / Planning Review / XFN Kickoff / Solution Review / Launch Readiness / Impact Review
**Owner:** [name] · **Status:** Draft / In Review / Approved / Shipped · **Last updated:** [date]
**Links:** [Design]() · [Prototype]() · [Tracking]() · [Dashboard]() · [Runbook]()

---

## 1. Overview

**What this is:** [One or two sentences: what changes, for whom.]

**What it is not:** [Non-goals, each with why it is out.]

**Why now:** [The external reason, sourced: a market shift, a competitor move, a regulation, client research. Internal metrics go under section 3.]

## 2. Problem

### Hypothesis

If we [build X], then [Y metric] will [change by Z], because [assumption about user behavior].

**Evidence:** [user quote or data point, graded] · [user quote or data point, graded]

### Current implementation gaps

[Where today's system falls short, each gap named with where it lives: the code path, the contract clause, the process step. Graded: a gap read from the code is "inferred from the code" until its engineer confirms.]

## 3. Business metrics and goals

**Goal it serves:** [the strategic goal or OKR, with its source]

**Primary metric:** [name] · baseline [value, graded] · target [value] · by [date]

**Guardrails (must not harm):** [metric]: [acceptable range]

**Kill criteria:** If [threshold], [owner] will [rollback / pause / iterate].

[Impact sizing summary, if any. Detail goes in the appendix.]

## 4. Legal, compliance and risk constraints

| Constraint or risk | Source (and version) | What it requires | Detection / fallback | Owner |
|--------------------|----------------------|------------------|----------------------|-------|
| [e.g., data retention] | [policy name, v3.2] | [requirement] | [signal; fallback] | [name] |

[Or: "None identified. Checked: [the policies, contracts, and specs read, with versions]."]

## 5. Solution

### Approach

[What we will build and why this approach, in a paragraph. Trade-offs accepted.]

### High-level design

[User flow, key interactions, edge cases. For an AI feature, the behavior contract: primary task, inputs, constraints, disallowed behavior, latency budget, and a happy-path / edge-case / should-reject example table. Mockup or prototype link.]

## 6. Rollout plan

**Approach:** A/B test / phased rollout / full launch

| Phase | Audience | Duration | Pass criteria |
|-------|----------|----------|---------------|
| 1 | [who, % traffic] | [duration] | [what must be true to advance] |
| GA | everyone | ongoing | [steady-state monitoring] |

**Rollback:** If [scenario], [owner] will [action]. **Comms:** [release notes, in-product messaging, support docs]

## 7. Open questions

| Question | Owner | Needed by |
|----------|-------|-----------|
| [question] | [name] | [date] |

<details>
<summary><strong>Appendix</strong></summary>

### Design decisions

| Decision | Options considered | Chosen | Why | Owner | Date |
|----------|--------------------|--------|-----|-------|------|
| [decision] | [A / B / C] | [B] | [reason] | [name] | [date] |

### Supporting detail

[Impact sizing funnel, research excerpts, evaluation plan for AI features or experiments, meeting notes, changelog.]

</details>

---

## PRD Quality Checklist

> Check the items for the stage you are at. Every stage also checks: each theme present, metrics and constraints present (or "None identified" with what was checked), every open question owned.

- **Team Kickoff:** problem in two sentences; hypothesis testable; why-now sourced externally; gaps named and graded.
- **Planning Review:** goal and primary metric with a baseline; alternatives in the design-decisions table; constraints checked.
- **XFN Kickoff:** approach and high-level design; mockup or prototype linked; constraints with sources and versions.
- **Solution Review:** edge cases; rollout plan with pass criteria; tracking specified; risks with owners.
- **Launch Readiness:** kill criteria and rollback owned; comms ready; every engineering concern closed or owned.
- **Impact Review:** actuals against targets; what we would do differently; monitoring in place.
