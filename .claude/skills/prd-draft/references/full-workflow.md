# Full PRD Workflow

Bulk reference for `/prd-draft`, extracted verbatim from its `SKILL.md`. Read when the PM wants the end-to-end process around the draft, the per-stage adjustments, or where the PRD goes next. The rules this material serves stay in `SKILL.md`; nothing here overrides them.

## Part 2: Full PRD Workflow

For comprehensive end-to-end PRD creation, follow this 7-step process.

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

## Where Files Go

**PRD documents:**
- Active work: `outputs/prds/[feature-name].md`, one file, revised in place as the stage moves
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

### Second Brain

Before drafting, query the second brain for the **Overview** and **Problem** sections. A good PRD starts with evidence, not assumptions. Pull from:

- **`product-knowledge`** — what we already know about this product area, constraints, dependencies
- **`customer-insights`** — the customer pain, jobs-to-be-done, verbatim quotes from prior research
- **`competitive-intelligence`** — how competitors solve this today, positioning gaps
- **`decisions`** — past decisions in this area that constrain or inform the current one

Equivalent of `/second-brain query "background context for <feature>" --focus=<each>`. Pull facts with `[Source:]` citations directly into the PRD's Overview and Problem sections so stakeholders can click through to the evidence.

If the brain is thin on this topic, flag it at the top of the PRD ("evidence gap: we don't yet have wiki pages for X, Y"). That's a research task, not a blocker — but it should be visible.

If `context-library/second-brain/` isn't initialized, proceed without — this hook is a force multiplier, not a prerequisite.

---

### Context Search Terms

The search terms behind the Context Routing table in `SKILL.md`, as the skill first shipped them.

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
