# Decision Doc Templates

Extracted from `SKILL.md`. Read when you need the full template body or a non-standard format (one-way door, lightweight, approval-style).

## Standard Decision Doc Template

```markdown
# Decision Document: [Decision Title]

**Date:** [Date]
**Owner:** [Your name]
**Status:** [Proposed / Approved / Implemented]
**Decision Deadline:** [When we need to decide by]

---

## TL;DR

**Decision:** [One sentence: What we're deciding]

**Recommendation:** [One sentence: What you recommend]

**Impact:** [One sentence: Why this matters]

---

## Context

### Why We're Making This Decision

[Background and situation that created the need for this decision]

**What triggered this:**
- [Event/data/feedback that forced the decision]

**Current state:**
- [Where things stand today]
- [What's not working]
- [What's at stake]

**Example:**
- **Trigger:** 45% of our traffic is now from mobile devices, up from 25% 
  a year ago
- **Current state:** Mobile web experience has 35% bounce rate vs. 18% on 
  desktop
- **At stake:** Losing 2,000+ potential users per month due to poor mobile 
  experience

### Scope

**In scope:**
- [What this decision covers]

**Out of scope:**
- [What this decision does NOT cover]
- [Related decisions that will be made separately]

**Example:**
- **In scope:** Whether to build native iOS/Android apps
- **Out of scope:** Specific features for v1 (separate PRD), launch timing 
  (separate decision)

### Constraints

**Technical:**
- [Technology limitations]

**Resource:**
- [Budget/people limitations]

**Timeline:**
- [Time constraints]

**Business:**
- [Strategic or market constraints]

---

## Options Considered

[Full breakdown of each option using the framework from Step 2]

### Option 1: [Name]
[Complete analysis]

### Option 2: [Name]
[Complete analysis]

### Option 3: [Name]
[Complete analysis]

---

## Decision Criteria

**How we're evaluating options:**

| Criteria | Weight | Option 1 | Option 2 | Option 3 |
|----------|--------|----------|----------|----------|
| [Criterion 1] | High | 8/10 | 5/10 | 6/10 |
| [Criterion 2] | High | 6/10 | 9/10 | 7/10 |
| [Criterion 3] | Medium | 7/10 | 7/10 | 9/10 |
| **Total** | | **XXX** | **XXX** | **XXX** |

**Criteria definitions:**
- **[Criterion 1]:** [What this means and why it matters]
- **[Criterion 2]:** [What this means and why it matters]

**Example Criteria:**
- **User Impact** (High): How much this improves core user experience
- **Time to Value** (High): How quickly we can ship and see results
- **Resource Efficiency** (Medium): How efficiently this uses our limited resources
- **Strategic Alignment** (Medium): How well this supports our Q2 strategy

---

## Recommendation

[Complete recommendation using the framework from Step 3]

---

## Stakeholder Input

### Consulted

**Engineering:**
- [Name]: [Their input/concerns]
- [Name]: [Their input/concerns]

**Design:**
- [Name]: [Their input/concerns]

**Leadership:**
- [Name]: [Their input/concerns]

### Key Concerns Raised

**Concern 1:** [Stakeholder concern]
**Response:** [How you're addressing it]

**Concern 2:** [Stakeholder concern]
**Response:** [How you're addressing it]

### Unresolved Disagreements

[If anyone strongly disagrees, document it]

**[Name] believes:** [Their position]
**My reasoning for proceeding anyway:** [Why you're still recommending this]

---

## Success Metrics

**How we'll measure success:**

**Primary Metric:**
- [Metric]: [Current] → [Target] by [Date]

**Secondary Metrics:**
- [Metric]: [Current] → [Target] by [Date]
- [Metric]: [Current] → [Target] by [Date]

**Guardrail Metrics** (must not decline):
- [Metric]: Must stay above [threshold]
- [Metric]: Must stay above [threshold]

**Example:**
- **Primary:** Mobile user retention: 45% → 65% by end of Q3
- **Secondary:** 
  - Mobile DAU: 50K → 80K by end of Q3
  - Time in app: 12 min → 20 min by end of Q3
- **Guardrails:**
  - Overall retention must stay >60%
  - NPS must stay >40

### Leading Indicators (Early Signals)

**After 1 month:**
- [What we should see]

**After 3 months:**
- [What we should see]

**Example:**
- **After 1 month:** 2 mobile engineers hired, tech stack decided
- **After 3 months:** MVP in beta with 1,000 users, NPS >45

---

## Implementation Plan

### Timeline

| Phase | Milestone | Owner | Target Date |
|-------|-----------|-------|-------------|
| Phase 1 | [Milestone] | @[Owner] | [Date] |
| Phase 2 | [Milestone] | @[Owner] | [Date] |
| Phase 3 | [Milestone] | @[Owner] | [Date] |

### Next Steps

**Immediate (This Week):**
1. [Action item] - @[Owner]
2. [Action item] - @[Owner]

**Short-term (Next 2 Weeks):**
1. [Action item] - @[Owner]
2. [Action item] - @[Owner]

**Medium-term (Next Month):**
1. [Action item] - @[Owner]

### Dependencies

**Blockers:**
- [What must happen before we start]

**Parallel Work:**
- [What can happen at the same time]

---

## Risks & Mitigation

| Risk | Impact | Likelihood | Mitigation | Owner |
|------|--------|------------|------------|-------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Plan] | @[Owner] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Plan] | @[Owner] |

---

## Decision Log

**Proposed:** [Date] by [Name]
**Discussed:** [Date] in [Meeting/Channel]
**Approved:** [Date] by [Name]
**Implemented:** [Date]
**Reviewed:** [Date] - [Outcome]

---

## Appendix

### Supporting Data
- [Link to research]
- [Link to analysis]
- [Link to competitive intel]

### References
- [Related PRDs]
- [Related decisions]
- [Research documents]

### FAQ

**Q: [Common question]**
A: [Answer]

**Q: [Common question]**
A: [Answer]
```

---

## Alternative Formats

### DACI Format (When You Need Clear Roles)

```markdown
# DACI: [Decision Title]

## Roles

**Driver (owns the decision):** @[Name]
**Approver (makes the final call):** @[Name]
**Contributors (provide input):** @[Name], @[Name], @[Name]
**Informed (need to know outcome):** @[Name], @[Name]

## Decision
[What we're deciding]

## Recommendation
[Driver's recommendation]

## Context & Options
[Summary of situation and options]

## Approval Status
- [ ] Approver has reviewed
- [ ] Approver approves recommendation
- [ ] Decision communicated to Informed group
- [ ] Implementation started

**Date Approved:** [Date]
**Approver Comments:** [Any caveats or conditions]
```

### One-Way Door Format (For Irreversible Decisions)

```markdown
# One-Way Door Decision: [Title]

**Type:** ONE-WAY DOOR (Hard to reverse)

## Why This Is One-Way

[Explanation of why this decision is hard or impossible to reverse]

**Examples:**
- Architecture choices that lock us into a tech stack
- Partnerships with long-term contracts
- Decisions that create customer expectations
- Resource commitments that can't be unwound

## Extra Scrutiny Required

Because this is one-way, we're applying extra rigor:

**Questions we MUST answer:**
1. [Critical question 1]
2. [Critical question 2]
3. [Critical question 3]

**Validation we MUST do before deciding:**
- [Proof point 1]
- [Proof point 2]
- [Proof point 3]

**Dissenting voices we MUST hear from:**
- [Skeptic 1]: [Their concern]
- [Skeptic 2]: [Their concern]

**Example:**
- **Must answer:** Can we build this with our current team's skill set?
- **Must validate:** Talk to 3 companies who made similar decision - what 
  do they wish they knew?
- **Must hear from:** VP Eng (concerns about tech debt) and Lead Designer 
  (concerns about user impact)

## [Rest of standard decision doc]
```

### Lightweight Format (For Smaller Decisions)

```markdown
# Quick Decision: [Title]

**Date:** [Date]
**Owner:** [Name]

## The Decision
[What we're deciding in 1-2 sentences]

## Options
1. **[Option A]:** [Pro/Con in one line each]
2. **[Option B]:** [Pro/Con in one line each]

## Recommendation
**Go with [Option X]** because [one sentence reasoning].

## Next Steps
- [Action 1] - @[Owner] - [Date]
- [Action 2] - @[Owner] - [Date]

## How We'll Know It Worked
[One metric or signal]
```

---
