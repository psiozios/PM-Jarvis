---
name: prd-draft
description: Write the full PRD for a feature — overview, problem and hypothesis, business metrics, constraints, solution, rollout, open questions, in themes rather than teams — through guided clarifying questions, with an offer to run the multi-agent review panel afterward. The spec engineering builds from; use prd-lite for a quick proposal before a feature is slated.
user-invocable: true
disable-model-invocation: false
---

**Commitment gate:** When a PRD moves past proposal into committed scope, run the five checks in `references/protocols/commitment-gate.md`.

**The brief rests on graded evidence.** These hold for every draft, before a line is written:

- **Read the current code path first, read-only, when a codebase is connected** (`/explore-codebase` does the read). Name where today's system falls short under Problem → Current implementation gaps, each gap pointing at the file or function it was read from and graded **"inferred from the code"** until its engineer confirms. That engineer goes in Open questions as the owner of the confirmation.
- **Why now is external and sourced:** a market shift, a competitor move, a regulation, client research, each with its source. Internal metrics belong under Business metrics and goals, not in why-now.
- **Name the version of every contract, policy, or spec read, and read its comments, resolved ones included.** On one run, two rulings that bound the design lived only in resolved comments.
- **Summary lines keep the body's grade, in a neutral voice.** The overview, any TL;DR, and the announcement carry the same grades as the sections they summarize, because the doc ships under the user's name. One run's TL;DR stated code inferences as fact.
- Grades follow `references/absolute-rules.md` (measured, reported, estimated, inferred from the code, unsourced, unknown).

## Quick Start

**What to provide:** A feature idea, problem statement, or rough brief. Can be detailed or rough.

```
/prd-draft                                → Start from scratch with guided questions
/prd-draft [paste your feature idea]      → I'll skip questions you already answered
/prd-draft --stage "team kickoff"         → Set the PRD stage upfront
/prd-draft --ai                           → Include AI behavior specification sections
/prd-draft --retro [product]              → Retro PRD for a product already shipped
```

**What you get:** A 1-2 page PRD in themes: overview, problem, business metrics and goals, legal and risk constraints, solution, rollout plan, open questions, and a collapsible appendix. Saved to `outputs/prds/[feature-name-kebab-case]-[stage].md`. Based on `templates/prd-template.md`.

**Time:** 10-20 minutes for first draft. Then iterate.

**Filename convention:** `[feature-name-kebab-case]-[stage].md` (e.g., `voice-task-capture-team-kickoff.md`)

---

# /prd-draft - Modern PRD Creation

When the PM types `/prd-draft`, guide them through creating a modern, AI-era PRD.

## Context Routing

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Strategy Docs | `context-library/strategy/*.md` | feature name from chat | Strategic pillar alignment |
| Related PRDs | `context-library/prds/*.md` | feature dependencies | Related features and cross-functional impact |
| User Research | `context-library/research/*.md` | problem related to feature | User pain points, quotes, validation |
| Business Model | `context-library/business-info-template.md` | pricing, revenue, metrics | Revenue impact, North Star alignment |
| Competitor Analysis | `context-library/research/competitive-*.md` | feature name | Competitive positioning if relevant |
| Stakeholder Context | Stakeholder profiles | key stakeholders for this feature | Who to involve, communication style |
| Current code path | the connected codebase, read-only (via `/explore-codebase`) | the feature's entry points and handlers | Where today's system falls short, graded "inferred from the code" |
| Contracts, policies, specs | `<DOCS_HUB>`, `context-library/` | the clauses the feature touches | The version read, and every comment, resolved ones included |

**Context Priority:**
1. Strategic fit and related PRDs FIRST
2. User research and problem statement SECOND
3. Business context and metrics THIRD
4. Competitive positioning FOURTH

---


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected. A source that is connected but fails — an expired credential, a revoked scope, an OAuth refresh with no browser — is reported unavailable by name with its reason and never listed among the sources swept (`references/protocols/source-preflight.md`).

## Step 0: Understanding Your Feature Context

Before we draft, let me check what context exists...

**Checking:**
- `context-library/prds/` for any related feature PRDs
- `context-library/strategy/` for strategic alignment
- `context-library/research/` for user validation
- `context-library/business-info-template.md` for business context
- Stakeholder profiles for who needs to be involved

### Context Health Check

After reading context files, verify they contain real data (not placeholder brackets):

**If `business-info-template.md` contains unfilled placeholders** (e.g., `[Your Company]`, `[Your Product]`):
```
I notice your business context template hasn't been filled out yet. Your PRD will be much stronger with real company context.

Want to:
1. **Fill it out now** (5 min) - I'll ask you the key questions
2. **Proceed without it** - I'll draft the PRD but flag where company context would improve it
```

**If strategy docs are empty/missing:**
Flag this and suggest `/write-prod-strategy` or `/strategy-sprint` first.

**Based on what I find, I'll show you:**

### What We Know About This Feature

**Strategic Context:**
- [Which strategic pillar does this support? From your strategy doc]
- [Expected user impact: # of users affected]
- [Business outcome: revenue, retention, or engagement impact]

**User & Problem Validation:**
- [User research confirming this problem: quotes, frequency]
- [Current workaround: how users solve this today]
- [Problem severity: pain level from research]

**Feature Dependencies:**
- [Related features: what needs to ship first]
- [Cross-functional impact: which teams are involved]
- [Timing constraints: market window, competitive pressure]

### PM-Specific Diagnosis Questions

1. **Problem Validation:** Is this problem validated with real users, or hypothesis?
2. **Strategic Clarity:** Do you know how this fits into your Q# roadmap?
3. **Scope Clarity:** Is this a small v1 or full-featured release?
4. **Business Metrics:** Do you know what success looks like?
5. **Execution Readiness:** Do engineering and design understand the scope?

---

## When to Use

- Starting a new feature or initiative
- Need to align cross-functional stakeholders
- Moving from prototype to formal spec
- Preparing for planning/prioritization review

## Workflow

This is a 3-step conversational workflow:

### Step 1: Clarifying Questions
### Step 2: Generate First Draft
### Step 3: Multi-Agent Review

---

## Step 1: Clarifying Questions

**Adaptive Questions Rule:** Before asking clarifying questions, check what the PM has already provided in their prompt. Skip questions that are already answered. Start with: "Based on what you shared, I have [X, Y, Z]. Let me confirm: [summary]. A few remaining questions: [only the gaps]."

If the PM provided a detailed brief, you may have enough to skip straight to Step 2. Only ask what's genuinely missing.

When the PM types `/prd-draft` with no additional context, start with:

```
Let's create a modern PRD together. I'll reference your company context and PRD template from this workspace.

Before I draft anything, I need to understand the initiative. Don't worry about structure—just talk through it. Use dictation if that's easier.

**Required context:**
1. What problem are we solving? (Be specific about the user pain)
2. What's the hypothesis? (If we build X, then Y will happen because Z)
3. How does this fit our current strategy? (Reference specific goals from business-info.md)
4. What stage is this PRD at? (Team kickoff / Planning review / XFN kickoff / Solution review / Launch readiness / Impact review)

**Important details:**
5. Is this an A/B test or full launch?
6. What are the non-goals? (What are we explicitly NOT doing?)
7. What are the success metrics? (How will we know this worked?)
8. Who are the key stakeholders? (@ mention them if you have profiles in `context-library/stakeholder-template.md` or similar)

**AI-specific (if applicable):**
9. What are example prompts or user inputs?
10. How should it handle edge cases or weird inputs?
11. What should it NEVER do? (Rejection criteria)

Take your time. I'll ask follow-up questions if needed.
```

### Follow-Up Questions

Based on what the PM shares, ask:

- **If strategy fit is unclear:** "I see this solves [problem], but how does it ladder up to our [specific strategy goal]? Or is this a bet on a new direction?"

- **If non-goals are missing:** "What are we explicitly NOT including in v1? Any trade-offs you're making?"

- **If metrics are vague:** "When you say 'increase engagement,' what's the specific metric? What's the target? What's the guardrail (metric we can't harm)?"

- **If rollout plan is missing:** "Should this be an A/B test first? What's the passing criteria to roll out to everyone?"

- **If AI behavior is unclear:** "Can you give me 3 example inputs: one that should work great, one that's borderline, and one that should be rejected?"

### What NOT to Ask

- Don't ask about technical implementation details yet (that's for engineers)
- Don't ask for exhaustive edge case lists (capture the pattern, not every scenario)
- Don't ask for final copy or UI details (PRD is about "what" not "how exactly")

---

## Step 2: Generate First Draft

Once you have enough context, say:

```
Great, I have enough to draft a first version. This will be:
- Short (1-2 pages max)
- Focused on the key sections for this stage
- At the [STAGE] stage of evolution
- Using your [AUDIENCE] writing style
- Based on templates/prd-template.md

I'll create it now and save it to `outputs/prds/[feature-name-kebab-case]-[stage].md`.

After you review, we can iterate or get multi-perspective feedback.
```

### PRD Structure

**Sections are themes, never teams.** Use `templates/prd-template.md` and this order, at every stage: 1. Overview (what it is, what it is not, why now) · 2. Problem (hypothesis; current implementation gaps) · 3. Business metrics and goals · 4. Legal, compliance and risk constraints · 5. Solution (approach; high-level design) · 6. Rollout plan · 7. Open questions with owners · a collapsible appendix holding the design-decisions table. No section is named for a team ("Engineering", "Legal", "Design").

**Every stage carries every theme.** A short stage keeps a theme to one line. Business metrics and constraints never drop out: where none apply yet, the section says "None identified" and names what was checked.

### Writing Guidelines for the Draft

**Tone:**
- Use the appropriate writing style from `context-library/writing-style-*.md`
- Write like the PM would write (human, not AI-generated)
- Be direct and crisp

**Content:**
- Use exact quotes from user research when available
- Reference specific data from business-info.md
- Call out stakeholders by name
- Flag controversial decisions explicitly

**What to Include:**
- Real user quotes: "I'm frustrated when..."
- Actual numbers: "47% of users abandon at this step"
- Specific references: "This supports our Q2 goal of [X]"

**What to Avoid:**
- Generic statements: "Users want a better experience"
- Vague goals: "Increase engagement"
- Corporate jargon: "Leverage synergies to unlock value"

---

## Step 2.5: Generate Prototype (Optional)

After drafting the PRD, offer to create a quick prototype:

```
Want me to help you visualize this feature before engineering review?

**The $1-$10-$100 Rule:**
- $1: PM creates napkin sketch → catches issues early
- $10: Designer reworks based on feedback → moderate cost
- $100: Engineering builds wrong thing → expensive waste

Quick prototype options:
1. **Napkin Sketch** - ASCII wireframe right here
2. **v0.dev Prompt** - Generate a prompt for Vercel's v0
3. **Lovable Prompt** - Generate a prompt for Lovable.dev
4. **Figma Description** - Detailed spec for designer handoff
5. **User Flow Diagram** - Step-by-step flow visualization

Which would be helpful?
```

### Prototype Templates

**Napkin Sketch (ASCII):**
```
┌─────────────────────────────┐
│  Header / Navigation        │
├─────────────────────────────┤
│                             │
│  [Main Content Area]        │
│                             │
│  ┌─────────┐  ┌─────────┐  │
│  │ Card 1  │  │ Card 2  │  │
│  └─────────┘  └─────────┘  │
│                             │
│  [ Primary CTA Button ]     │
│                             │
└─────────────────────────────┘
```

**v0.dev / Lovable Prompt Template:**
```
Create a [component type] for [product context].

**User Goal:** [What the user is trying to accomplish]

**Key Elements:**
- [Element 1 with behavior]
- [Element 2 with behavior]
- [Element 3 with behavior]

**Interactions:**
- When user [action], [result]
- When user [action], [result]

**Style:** [Modern/minimal/playful] with [brand colors if known]

**Edge Cases:**
- Empty state: [what to show]
- Error state: [what to show]
- Loading state: [what to show]
```

**User Flow Diagram:**
```
[Entry Point] → [Step 1] → [Decision Point]
                              ↓ Yes      ↓ No
                          [Step 2A]   [Step 2B]
                              ↓           ↓
                          [Success]   [Recovery]
```

---

## Step 3: Multi-Agent Review

After generating the draft, offer:

```
First draft created! Saved to `outputs/prds/[feature-name]-[stage].md`.

Want me to review this from multiple perspectives?
- Engineer (technical feasibility, implementation concerns)
- Designer (UX/UI, user experience)
- Executive (strategic alignment, business impact)
- Legal (compliance, risk)
- Skeptic (devil's advocate)

Just let me know which perspectives would be helpful.
```

### How to Run Multi-Agent Review

When the PM requests review:

1. **Invoke each sub-agent explicitly:**
   ```
   I'll review this from [Engineer / Designer / Executive] perspective.
   Reading from `sub-agents/[agent-name].md`...
   ```

2. **For each agent, provide:**
   - ✅ What looks good
   - ⚠️ Concerns or risks
   - 💡 Suggestions for improvement
   - ❓ Clarifying questions

3. **Synthesize at the end:**
   ```
   **Summary of Feedback:**
   - All reviewers agree: [common feedback]
   - Conflicting perspectives: [engineer says X, but designer says Y]
   - Highest priority fixes: [what to address first]

   Want me to update the PRD with this feedback, or would you like to iterate on specific sections?
   ```

---

## Iterating on the PRD

The PM will likely want to refine sections. Common requests:

**"Make the hypothesis stronger"**
→ Add more specific user pain, quantify the problem, tie to data

**"Add more behavior examples"**
→ Create the Good/Bad/Reject table with real scenarios

**"The 'what it is not' line isn't clear"**
→ Make them more specific, add rationale for each

**"This needs to be shorter"**
→ Move supporting details to Appendix, tighten language

**"Make it sound more like me"**
→ Reference their writing style, use their voice patterns

---

## Stage-Specific Length Guidance

Word ranges are targets for the body. The appendix does not count.

| Stage | Target words | Focus |
|-------|--------------|-------|
| Team Kickoff | 300-500 | Overview, problem, one line per other theme |
| Planning Review | 500-800 | Business metrics and goals, alternatives in the design-decisions table |
| XFN Kickoff | 800-1200 | Solution approach and high-level design, mockups, constraints with sources |
| Solution Review | 1000-1500 | Edge cases, behavior, rollout plan |
| Launch Readiness | 1500-2000 | Kill criteria, rollback, comms, go/no-go |
| Impact Review | 500-800 | Actuals against targets, what we would do differently |

**Scoring against the target:** up to 250 words over the top of the range passes, 251-500 over is PARTIAL, more fails. The remedy is moving the run's own detail into the appendix. **The user's own text is never cut to hit a number**; where it alone keeps the count over, say so and leave it.

---

## Stage-Specific Adjustments

### Team Kickoff Stage
- Focus on: Overview, problem, hypothesis
- Keep to one line: business metrics, constraints, solution, rollout
- Include: Lots of open questions

### Planning Review Stage
- Focus on: Business metrics and goals, impact sizing, alternatives in the design-decisions table
- Include: Rough success metrics, estimated effort
- Skip: Detailed behavior examples

### XFN Kickoff Stage
- Focus on: Aligned solution, initial data/research
- Include: Mockups or prototype link
- Add: Stakeholder sign-offs needed

### Solution Review Stage
- Focus on: In-depth justification, edge cases, behavior examples
- Include: Detailed metrics, rollout plan
- Add: Technical feasibility assessment

### Launch Readiness Stage
- Focus on: Final details, rollback plan, kill criteria
- Include: Go/no-go checklist
- Add: Launch communication plan

### Impact Review Stage
- Focus on: Results, learnings, next steps
- Include: Actual vs. target metrics
- Add: What we'd do differently

---

## Tips for Great PRDs

**Keep gossiping to me:**
After stakeholder meetings, user research, or team discussions, tell me what happened. I'll help keep the PRD updated with:
- New insights
- Changed requirements
- Stakeholder concerns
- Shifted priorities

**Use dictation:**
Talking is faster than typing. Just ramble about the feature and I'll structure it.

**Don't aim for perfect:**
PRDs evolve. Ship the draft, get feedback, iterate.

**Add real examples:**
The best PRDs have real user quotes, actual data, and concrete examples.

**Make it yours:**
Customize the template for your company. Add sections that matter to your team.

---

## Common Pitfalls to Avoid

❌ **Too long** - If it's over 2 pages, move details to Appendix
❌ **Too generic** - Use specific data, quotes, and stakeholders
❌ **No "what it is not"** - Always clarify what you're NOT doing
❌ **Vague metrics** - "Increase engagement" is not specific enough
❌ **No rollout plan** - A/B test vs full launch matters
❌ **Missing kill criteria** - How will you know if this failed?
❌ **Formulaic prose** - Apply `config/house-style.md` §5 (P11 robotic rhythm, P2 throat-clearing)

---

## After the PRD is Done

```
Great work! Your PRD is ready for review.

**Next steps:**
1. Share with stakeholders for feedback
2. Walk through it in your XFN kickoff
3. Update it as you learn more (gossip to me!)
4. Move it to the next stage when ready

**Want me to:**
- `/create-tickets` -- Turn this PRD into engineering tickets
- `/slack-message` -- Draft a Slack message announcing this PRD
- `/feature-metrics` -- Primary metric, guardrails, and kill criteria for this PRD
- `/impact-sizing` -- Quantify the user/revenue impact
- `/generate-ai-prototype` -- Create a prototype prompt from this spec
```

---

## Where Files Go

**PRD documents:**
- Active work: `outputs/prds/[feature-name]-[stage].md`
- When finalized: Move to `context-library/prds/[feature-name].md` for historical reference
- Evolve through stages: Team Kickoff → Planning Review → XFN Kickoff → Solution Review → Launch → Impact

---

## Link to Other Work

After creating PRD:
- **Reference in status updates** - Feature appears in `/status-update` with link to PRD
- **Create tickets** - Use `/create-tickets` to turn PRD sections into engineering tasks
- **Plan roadmap** - PRD informs quarterly prioritization
- **Track results** - Use `/feature-results` to measure actual impact post-launch

---

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

## Output Quality Self-Check

Before presenting the PRD draft to the PM, verify:

- [ ] **Filename follows convention:** `[feature-name-kebab-case]-[stage].md` (e.g., `voice-task-capture-team-kickoff.md`)
- [ ] **Saved to correct location:** `outputs/prds/` (NOT `context-library/prds/`)
- [ ] **Word count matches stage:** body within 250 words of the stage target, appendix excluded, the user's own text untouched
- [ ] **Themes, in order, at every stage:** overview, problem, business metrics and goals, constraints, solution, rollout, open questions, collapsible appendix — and metrics and constraints present even as "None identified" plus what was checked
- [ ] **Hypothesis is testable:** Contains a clear "If we... then... because..." statement
- [ ] **Business goals reference actual strategy:** Cites specific goals from `context-library/strategy/`, not generic strategy language
- [ ] **"What it is not" is specific:** Each non-goal explains WHY it's excluded, not just what it is
- [ ] **Success metrics have baselines and targets:** Not just "increase X" but "X from [current] to [target] by [date]"
- [ ] **Kill criteria are realistic:** Would the team actually pull the plug at this threshold?
- [ ] **High-level design fits the feature:** AI features carry the behavior contract and example table; non-AI features the user flow and edge cases
- [ ] **Reads naturally:** Read it aloud — varied cadence, natural contractions, no formulaic openings (`config/house-style.md` §5 P11, §7). Name the defect, never the author.
- [ ] **User quotes included:** If user research exists in `context-library/research/`, at least one real quote is referenced
- [ ] **Open questions have owners:** Every open question has a @stakeholder assigned

---

**Remember:** The PRD is a tool for alignment, not a work of art. Ship it, discuss it, iterate on it.

---

# Part 2: Full PRD Workflow

For comprehensive end-to-end PRD creation, follow this 7-step process.


## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it the output (or its absolute path), this skill's `evals.md`, `config/house-style.md`, and the sources the output cites — E7 cannot be scored without them, and scoring it from plausibility is a vacuous PASS. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

### Step-by-Step Workflow

### Workflow Step 1: Gather Context (10 min)

Before touching AI, collect:

**Research & Data:**
- User research findings (interviews, surveys)
- Analytics data (usage patterns, metrics)
- Support tickets (common issues, requests)
- Competitive analysis

**Strategic Context:**
- How this ladders to OKRs
- Business case (revenue/user impact)
- Strategic importance (why now?)

**Technical Context:**
- Existing architecture constraints
- Integration requirements
- Known dependencies

### Workflow Step 2: Generate First Draft (5 min)

Use the conversational workflow in Step 1-3 above to generate your first draft.

### Workflow Step 3: Enhance Each Section (30-60 min)

**Problem:**
- [ ] Add specific customer quotes
- [ ] Include quantitative data
- [ ] Connect to company strategy

**Solution:**
- [ ] Explain WHY this solution
- [ ] Detail alternatives considered
- [ ] Call out tradeoffs made

**Business metrics and goals:**
- [ ] Define leading AND lagging indicators
- [ ] Set specific targets
- [ ] Define success criteria

### Workflow Step 4: Multi-Perspective Review (15 min)

Use the multi-agent review in Step 3 above to get feedback from:
- Engineering (feasibility)
- Design (UX)
- Executive (strategy)
- Customer voice (user needs)

### Workflow Step 5: Human Review

**Must review with:**
- Engineering lead
- Design lead
- Your manager

**Should review with:**
- Key stakeholders
- PM peers

### Workflow Step 6: Refine & Ship (30 min)

**Final checklist:**
- [ ] Can someone unfamiliar understand it?
- [ ] All sections complete
- [ ] Dependencies identified
- [ ] Success criteria clear
- [ ] Next steps defined

### Workflow Step 7: Announce

```
Hi team,

I've published the PRD for [Feature Name]: [link]

TL;DR: [One sentence]
Why now: [Strategic rationale]
Timeline: [When we plan to start/ship]

Action needed:
- Engineering: Review technical approach by [date]
- Design: Review UX approach by [date]

Questions? Drop them in [Slack channel].
```

---

# Part 3: AI Feature PRDs

**When to use:** When building any AI-powered feature, LLM integration, or ML product.

## Why AI PRDs Are Different

AI is fundamentally different from traditional features:
- **Non-deterministic:** Same input → different outputs
- **Probabilistic:** Can't guarantee 100% accuracy
- **Context-dependent:** Quality depends on prompt, data, user intent
- **Edge cases everywhere:** Infinite ways to break it

## AI PRD Additional Sections

### Behavior Specification (Required for AI)

Create a table with three categories:

| User Input | Expected Behavior | Category |
|------------|-------------------|----------|
| [Example 1] | [What AI should do] | ✅ Good |
| [Example 2] | [What AI should do] | ✅ Good |
| [Example 3] | [Graceful handling] | ❌ Bad |
| [Example 4] | [Must refuse] | 🚫 Reject |

**Good:** AI performs correctly
**Bad:** AI should handle gracefully (don't break)
**Reject:** AI must refuse (safety, policy violations)

**Tip:** Write 10-20 examples covering edge cases.

### AI Constraints

**Model constraints:**
- Model type: (GPT-5.2, Claude Opus 4.5, etc.)
- Max tokens: input/output limits
- Latency requirements: response time SLA
- Cost constraints: $ per 1M tokens

**Quality constraints:**
- Accuracy target: % correct responses
- Hallucination rate: max % of made-up facts
- Refusal rate: % of "I don't know" responses

**Safety constraints:**
- Content filtering requirements
- PII handling policy
- Bias mitigation requirements

### Edge Case Handling

**Common AI edge cases:**

1. **Ambiguous input**
   - AI asks clarifying questions

2. **Out-of-scope request**
   - AI explains what it can help with instead

3. **Harmful/unsafe request**
   - AI refuses with explanation

4. **Insufficient context**
   - AI asks for more information

5. **Low confidence**
   - AI admits uncertainty

### Graceful Degradation

**Fallback hierarchy:**
1. Retry with modified prompt
2. Offer alternative action
3. Escalate to human
4. Fail gracefully with clear message

### AI Evaluation Plan

**Pre-launch:**
- Test set: 100-500 hand-labeled examples
- Human evaluation: Team rates 50 outputs
- Edge case coverage: Test all known failure modes

**Post-launch:**
- Thumbs up/down feedback
- Correction rate (% of edited outputs)
- Abandonment rate
- Escalation rate

## 10 Principles for AI Products

1. **Focus on user value** - Users care about outcomes, not technology
2. **Anticipate mistakes** - Show confidence, allow corrections
3. **Start simple** - One use case, nail it, expand
4. **Make AI transparent** - What it can/can't do, when uncertain
5. **Build for iteration** - Feedback loops from Day 1
6. **Design for diverse users** - Beginners and experts
7. **Control context** - System instructions, user history, RAG
8. **Optimize for latency** - Streaming, perceived performance
9. **Safety is non-negotiable** - Input/output filtering, rate limiting
10. **Measure what matters** - Satisfaction, completion, corrections

## AI PRD Template Addition

Fold these into the standard themes for AI features: the behavior specification, AI constraints, and degradation path under 5. High-level design, safety and compliance under 4, and the AI kill criteria under 3:

```markdown
## AI Behavior Specification

| User Input | Expected Behavior | Category |
|------------|-------------------|----------|
| [Example] | [Response] | ✅ Good |
| [Example] | [Response] | ❌ Bad |
| [Example] | [Response] | 🚫 Reject |

## AI Constraints
- Model: [GPT-5.2 / Claude Opus 4.5 / etc.]
- Latency: P95 < ___ ms
- Accuracy target: >___%
- Hallucination rate: <___%

## Safety & Compliance
- Content filtering: [policy]
- PII handling: [policy]
- Audit logging: [policy]

## Graceful Degradation
1. [First fallback]
2. [Second fallback]
3. [Human escalation]
4. [Final error state]

## AI-Specific Kill Criteria
- Accuracy < ___% after 2 weeks
- User satisfaction < ___%
- Escalation rate > ___%
```

---

## Mode: --retro

A PRD for a product already shipped. **Read `references/retro-mode.md` when the run is `--retro`** — it carries the method and the shape. The rules:

- **Intended behavior comes from the user; the code is what gets checked.** Ask what it was meant to do before reading anything.
- **The core is a four-way cross-check:** code, contract, sales and ops material, ticket acceptance criteria. Every disagreement is a gap under Current implementation gaps, with an owner in Open questions.
- **Same themes, past tense. No rollout plan. A review trigger instead of kill criteria**, which evals score N/A, never PASS.
- **Status is date-stamped or linked live**, and "shipped" is two claims (`references/protocols/freshness-provenance.md` rule 5).

---

## Mode: --brief

Alias for `/prd-lite`, which owns the pre-commitment feature brief. Run `/prd-lite` instead — same artifact, and it is the skill that is maintained.

---

### Second Brain

Before drafting, query the second brain for the **Overview** and **Problem** sections. A good PRD starts with evidence, not assumptions. Pull from:

- **`product-knowledge`** — what we already know about this product area, constraints, dependencies
- **`customer-insights`** — the customer pain, jobs-to-be-done, verbatim quotes from prior research
- **`competitive-intelligence`** — how competitors solve this today, positioning gaps
- **`decisions`** — past decisions in this area that constrain or inform the current one

Equivalent of `/second-brain query "background context for <feature>" --focus=<each>`. Pull facts with `[Source:]` citations directly into the PRD's Overview and Problem sections so stakeholders can click through to the evidence.

If the brain is thin on this topic, flag it at the top of the PRD ("evidence gap: we don't yet have wiki pages for X, Y"). That's a research task, not a blocker — but it should be visible.

If `context-library/second-brain/` isn't initialized, proceed without — this hook is a force multiplier, not a prerequisite.
