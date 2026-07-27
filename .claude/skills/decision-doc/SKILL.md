---
name: decision-doc
description: Write down a product decision so it stops getting relitigated — how it was framed, the options with honest trade-offs, the recommendation, and what would change our mind. Use for build-versus-buy, competing approaches, architecture direction, or anything someone will question three months from now.
user-invocable: true
disable-model-invocation: false
---

# /decision-doc - Document Strategic Decisions That Stick

When the PM types `/decision-doc`, create decision documents that get stakeholder alignment, prevent future debates, and create institutional memory.

## When to Use

- Making a significant product direction choice
- Evaluating build vs. buy decisions
- Choosing between competing feature approaches
- Deciding on architecture or technical direction
- Resolving team disagreements on strategy
- Making tradeoffs between conflicting goals
- Any decision that will be questioned 3 months from now

---

## Workflow

This is a 4-step process:

### Step 1: Frame the Decision
### Step 2: Present Options with Tradeoffs
### Step 3: Make a Recommendation
### Step 4: Document the Decision

---

## Step 1: Frame the Decision

When the PM types `/decision-doc`, I'll start with:

```
Let's document this decision so it sticks.

**What decision are you making?**

Frame it as a clear choice:
- "Should we build feature X in-house or integrate with Partner Y?"
- "Should we launch with A/B test or full rollout?"
- "Should we prioritize mobile app or web improvements in Q2?"

**Why does this decision matter?**
- What's the impact if we get it right?
- What's the cost if we get it wrong?
- Who else needs to be involved?

**What's your timeline?**
- When do you need to decide?
- What forces the decision? (deadline, customer commitment, etc.)
- What happens if we delay?

Tell me about the decision and I'll help structure the document.
```

### What Makes a Good Decision to Document

**Do document:**
- ✅ Decisions with significant resource commitment
- ✅ Decisions with long-term consequences
- ✅ Decisions where reasonable people disagree
- ✅ Decisions that will be questioned later
- ✅ Decisions that set precedent for future choices
- ✅ Decisions involving multiple stakeholders

**Don't document:**
- ❌ Trivial tactical choices
- ❌ Decisions that can be easily reversed
- ❌ Decisions only affecting one person
- ❌ Decisions that are obvious/uncontroversial

---

## Step 2: Present Options with Tradeoffs

Once I understand the decision:

```
Great. Now let's map out your options.

**How many options are you considering?**
(Usually 2-4 options. More than 4 means you need to narrow first)

For each option, I need to understand:
- What it is (clear description)
- Why it's appealing (upsides)
- Why it's risky (downsides)
- What it costs (time, money, opportunity cost)
- What assumptions it requires

You can either:
- Tell me about each option
- Upload analysis you've already done
- Let me help you brainstorm options you might have missed

I'll structure this into a clear comparison framework.
```

### The Options Framework

For each option, I'll create:

```markdown
## Option [1/2/3]: [Name of Option]

### Description
[Clear, jargon-free explanation of what this option means]

**One-sentence summary:** [What this is in plain language]

### Pros (Why This Could Work)
- **[Pro 1]:** [Explanation and impact]
- **[Pro 2]:** [Explanation and impact]
- **[Pro 3]:** [Explanation and impact]

### Cons (Why This Could Fail)
- **[Con 1]:** [Explanation and risk]
- **[Con 2]:** [Explanation and risk]
- **[Con 3]:** [Explanation and risk]

### Costs & Resources Required
**Engineering:** [X weeks/people]
**Design:** [X weeks/people]
**Other Teams:** [Who else needs to be involved]
**Timeline:** [How long until we see results]
**Budget:** [Any direct costs - tools, services, licenses]

### Key Assumptions
[What needs to be true for this to work]

**Example assumptions:**
- "Assumes customers will adopt new workflow within 30 days"
- "Assumes partner API is stable and well-documented"
- "Assumes we can hire 2 senior engineers by Q2"

### Success Criteria
[How we'll know this option worked]

**Example criteria:**
- "Adoption >60% within first month"
- "Implementation completed in <8 weeks"
- "No degradation in core metrics"

### Risks & Mitigation
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [How we'd address it] |
| [Risk 2] | High/Med/Low | High/Med/Low | [How we'd address it] |

### Dependencies
- [Other team/project that must happen first]
- [External factor we can't control]
- [Technical prerequisite]

### Example: Mobile App vs Web

**Option 1: Build Native Mobile App**
- **Pro:** Better performance, offline support, push notifications
- **Con:** 6 month build time, need to hire mobile engineers, maintenance overhead
- **Cost:** 2 iOS engineers + 2 Android engineers for 6 months ($500K+)
- **Assumption:** 40% of usage will shift to mobile within 6 months
- **Risk:** Mobile engineers are hard to hire, could delay 3+ months
```

---

## Step 3: Make a Recommendation

After laying out options:

```
You've mapped the options clearly. Now it's time to make a call.

**What's your recommendation?**

Remember: The goal isn't to make everyone happy. It's to make the right 
decision for the business and clearly explain why.

A strong recommendation includes:
- **The choice:** Which option you're choosing
- **The why:** Your reasoning (data + logic)
- **The confidence level:** How certain you are (high/medium/low)
- **The failure mode:** What you'd do if you're wrong

Don't hedge. Make a clear call, even if you're not 100% certain.

I'll help you structure a compelling recommendation.
```

### Recommendation Structure

```markdown
## Recommendation: [Option Name]

### The Decision
I recommend we **[clear statement of choice]**.

**Example:** "I recommend we build a native mobile app starting Q2, 
rather than continuing to improve the mobile web experience."

### Rationale

**Why this option wins:**
1. **[Primary reason]** - [Data or logic supporting this]
2. **[Secondary reason]** - [Data or logic supporting this]
3. **[Tertiary reason]** - [Data or logic supporting this]

**Why alternatives fall short:**
- **[Alternative 1]** - [Specific reason it's not as good]
- **[Alternative 2]** - [Specific reason it's not as good]

**Key tradeoffs we're accepting:**
- We're trading [X] for [Y] because [reason]
- We're deprioritizing [A] to focus on [B] because [reason]

**Example:**
- We're trading faster time-to-market for better performance because 
  our user research shows performance is the #1 complaint
- We're deprioritizing web improvements to focus on mobile because 
  45% of usage is now mobile and growing 15% QoQ

### Confidence Level

**Confidence:** [High / Medium / Low]

**What would increase confidence:**
- [Test/data that would make you more certain]
- [Validation that's still needed]

**Example:**
- **Confidence:** Medium-High (75%)
- **Would increase to High if:** We validate mobile engineers can be 
  hired within 6 weeks, and tech lead confirms 6-month timeline is realistic

### What If We're Wrong?

**How we'll know:**
- [Leading indicator that this isn't working]
- [Timeline for when we should see results]

**Pivot plan:**
- [What we'd do if this fails]
- [How easily we could reverse course]

**Example:**
- **How we'll know:** If after 2 months we haven't hired mobile engineers, 
  or if recruitment timeline slips past 12 weeks
- **Pivot plan:** Pause mobile app, redirect resources to mobile web 
  improvements as interim solution

### What This Unlocks

**Positive outcomes if we're right:**
- [Business impact]
- [User impact]
- [Strategic advantage]

**Example:**
- Unlock 45% of our user base who prefer native apps
- Enable offline mode, which is #2 feature request
- Position us competitively against Competitor X who just launched mobile
```

---

## Step 4: Document the Decision

Finally, I'll create the complete decision document:

```
I'll create your decision document in the format that works best for 
your culture and stakeholders.

**Choose format:**
1. **Standard** - Comprehensive doc for important decisions
2. **DACI** - When you need clear roles and accountability
3. **One-Way Door** - For irreversible decisions (à la Amazon)
4. **Lightweight** - For smaller decisions that still need documentation

**Distribution:**
- Who needs to approve this?
- Who needs to be consulted?
- Who just needs to be informed?

I'll also create:
- Email/Slack summary to announce the decision
- FAQ section for common objections
- Timeline and next steps

Let's build this...
```

---

## Templates

The full standard template, plus the one-way-door, lightweight, and approval-style variants: `.claude/skills/decision-doc/references/templates.md`. Read it when drafting the artifact — it carries every section body verbatim.

## Common Mistakes

### ❌ Mistake 1: Analysis Without Recommendation

**Bad:** "Here are 3 options, all with pros and cons. Thoughts?"
**Good:** "I recommend Option 2 because [reasoning]. Here's why I'm not choosing the others."

### ❌ Mistake 2: Hiding the Tradeoffs

**Bad:** Only showing upsides of your preferred option
**Good:** Honest about what you're giving up: "We're trading speed for quality because..."

### ❌ Mistake 3: Decision by Committee

**Bad:** Trying to get everyone to agree
**Good:** Get input from stakeholders, but make a clear call as the owner

### ❌ Mistake 4: Vague Success Criteria

**Bad:** "Success means users are happier"
**Good:** "Success means mobile NPS increases from 40 to 55 within 3 months"

### ❌ Mistake 5: No Failure Plan

**Bad:** Not addressing what happens if you're wrong
**Good:** "If after 2 months we haven't hit 60% adoption, we'll pivot to..."

### ❌ Mistake 6: Too Much Detail

**Bad:** 20-page document that no one reads
**Good:** TL;DR at top, details in appendix, clear recommendation

---

## After the Decision

### Announcing the Decision

```
Use `/slack-message` to announce your decision.

I'll create:
- **For leadership:** Executive summary of decision and rationale
- **For team:** Full context and next steps
- **For stakeholders:** How this affects their work

**Announcement should include:**
- What was decided
- Why (brief rationale)
- What happens next
- Who owns implementation
- How to provide feedback if people disagree
```

### Following Up

```markdown
## Decision Review Checkpoints

**After 1 month:**
- Review leading indicators
- Adjust course if needed
- Document what we learned

**After 3 months:**
- Measure success metrics
- Compare to predictions
- Share results with stakeholders

**After 6 months:**
- Full retrospective
- Update decision doc with "What We Learned"
- Use insights for future decisions
```

### When to Revisit

```markdown
## Triggers to Revisit This Decision

**Automatic review if:**
- [ ] Success metrics aren't tracking toward targets
- [ ] Key assumption proves false
- [ ] Major market change makes this less relevant
- [ ] Resource constraints significantly change
- [ ] Stakeholder requests formal review

**Scheduled review:**
- [Date] - First checkpoint
- [Date] - Full review
```

---

## Handoff Details

### Informed by Competitive Analysis

```
Use `/competitor-analysis` first to understand market context.

Your decision doc should reference:
- Competitive positioning
- Market gaps you're exploiting
- Risks from competitive moves
```

### Feeds Into PRD

```
After the decision is approved, use `/prd-draft`.

I'll auto-populate:
- Strategic rationale from your decision doc
- Success metrics
- Non-goals (from rejected options)
- Open questions
```

### Tracked in Status Updates

```
Use `/status-update` to track implementation progress.

I'll reference:
- Timeline from decision doc
- Success metrics to track
- Risks to monitor
```

---

## Practice Notes

How to run the process well (write before the meeting, steel-man the alternatives, document disagreement, set review dates): `.claude/skills/decision-doc/references/practice-notes.md`. Read it when the user asks how to run the decision, not what the doc looks like.

## Context Routing

When the PM uses `/decision-doc`, I automatically:

### 1. Check Strategic Alignment
**Source:** `context-library/strategy/`, `context-library/prds/`
- **What I look for:** Current roadmap, strategic pillars, OKRs, company direction
- **How I use it:** Ensure recommendation aligns with broader strategy
- **Example:** If your strategy is "focus on activation," I'll note if this decision supports or conflicts with that

### 2. Identify Affected Stakeholders
**Source:** `context-library/stakeholder-template.md` + profiles
- **What I look for:** Who has input on this decision, who needs to approve, who will be affected
- **How I use it:** Build stakeholder consultation section automatically
- **Example:** If this decision affects Sales, I'll ask you to consult with VP Sales and note their input

### 3. Research Past Related Decisions
**Source:** `context-library/decisions/`
- **What I look for:** Similar decisions made before, how they were analyzed, what succeeded/failed
- **How I use it:** Reference precedent, avoid contradictory decisions, build on learnings
- **Example:** "In November we decided to focus on mobile. This decision respects that commitment by..."

### 4. Pull Success Metrics Framework
**Source:** `context-library/metrics/`, this chat thread
- **What I look for:** How you typically measure success, what metrics you care about
- **How I use it:** Suggest relevant metrics for this decision
- **Example:** If you've defined "activation rate" as key metric in past PRDs, I'll use that metric in success criteria

### 5. Extract Competitive Context
**Source:** `context-library/research/competitive-*.md`, web search if needed
- **What I look for:** Competitor moves, market trends, positioning implications
- **How I use it:** Include competitive rationale in decision reasoning
- **Example:** "If Competitor X launches this first, we'll lose positioning advantage"

### 6. Route Decision for Approval
**Routing logic:**
- **CEO/Board level decisions:** Flag as one-way door, require extra scrutiny
- **Cross-functional decisions:** Ensure all department heads are consulted
- **Tactical decisions:** Route to relevant team owner
- **Reversible decisions:** Use lightweight format

---


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected.

## Output Quality Self-Check

Before presenting output to the PM, verify:

- [ ] **File saved to correct location:** Output saved to `outputs/decisions/decision-[topic]-[date].md`
- [ ] **Context routing table was checked:** Reviewed `context-library/decisions/` for past decisions, `context-library/strategy/` for alignment, and `context-library/stakeholder-template.md` for stakeholder context
- [ ] **Decision framed as clear question:** The decision is stated as a specific, answerable question with 2-4 distinct options (not open-ended or vague)
- [ ] **Each alternative has pros, cons, and trade-offs:** Every option includes at least 2 pros, 2 cons, and explicit trade-offs with the other options
- [ ] **Recommendation includes explicit rationale:** The recommendation states which option is chosen and provides numbered reasons why, with data or logic supporting each
- [ ] **Stakeholders who need to sign off are named:** Specific people (not roles) are listed as approvers, contributors, and informed parties
- [ ] **Reversibility assessment included:** The document explicitly states whether this is a one-way door or two-way door decision, with reasoning
- [ ] **Conflicts with existing strategy or past decisions flagged:** Any tension with decisions in `context-library/decisions/` or goals in `context-library/strategy/` is called out with explanation of how the conflict is resolved

---


## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it three things: the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Mode: --deliberate (Pre-Decision Deliberation)

Use `/decision-doc --deliberate` before you know your recommendation. This mode helps you think through the options, not document what you've already decided.

**When to use:** You have a hard decision, competing pressures, and aren't sure which way to go. Use this mode to work through it, then switch to the standard `decision-doc` output to document the conclusion.

```
## Deliberation: [Decision Question]

### What I know for sure
[Facts, data, constraints that are not in dispute]

### What I believe but can't prove
[Assumptions I'm relying on — flag these explicitly]

### The options as I see them
1. [Option A] — [2 sentences on what this path looks like]
2. [Option B]
3. [Option C if applicable]

### Pressure mapping
For each option, who is pushing for it and why? What might be influencing their position?
- [Stakeholder]: wants [Option X] because [their actual reason, not just stated reason]
- [Stakeholder]: wants [Option Y] because...

### What I'm most afraid of getting wrong
[The failure mode I'm most worried about — often reveals the real risk]

### What I'd tell a peer
[If a fellow PM described this situation, what would I recommend? Getting outside your own head often clarifies.]

### My current lean
[Option X] — because [1-2 honest reasons]
[What would change my mind:]

### What I need before I can decide
[Data / stakeholder conversation / research / design spike that would resolve my uncertainty]
```

**Cross-skill:** After deliberating, run `/decision-doc` to formalize and communicate the final decision.

---

## Mode: --brainstorm (Option Generation)

Use `/decision-doc --brainstorm` when you've framed the decision but aren't sure you've considered all the options.

```
## Brainstorm: Options for [Decision Question]

**Constraints (real constraints only — don't over-constrain):**
- [Constraint 1]
- [Constraint 2]

**Options generated:**

Obvious options:
1. [What everyone would suggest first]
2. [The second obvious path]

Less obvious options:
3. [What if we did the opposite of option 1?]
4. [What if we deferred / did nothing?]
5. [What if we did a dramatically smaller version?]
6. [What would the boldest possible version look like?]
7. [What would someone outside our industry suggest?]

Hybrid options:
8. [Combination of 1 and 3]
9. [Phased approach: do X now, decide Y later]

**Gut check:** Which of these options, if it worked, would create the best outcome? Start there.
```

---

## Second Brain

**Before framing the decision:** query the `decisions` focus area for related past decisions. Don't re-litigate a debate that was already settled — reference it. Run equivalent of `/second-brain query "past decisions about <topic>" --focus=decisions` and surface any matches with `[Source:]` citations.

**Also pull evidence** from other focus areas relevant to the decision (e.g., `customer-insights` if customer impact matters, `competitive-intelligence` if competitive positioning is at stake).

**At the end of the run, offer: "File to Second Brain? (y/n)"**

If yes, ingest into the `decisions` focus area:
- The decision itself (one-line)
- Options considered and trade-offs
- Rationale for the choice
- Revisit trigger (what would change our mind)
- Who owns follow-through

Invoke `/second-brain ingest` with the decision doc as the source. If `decisions` doesn't exist yet, offer `/second-brain init decisions` first.

The brain is where decisions go to be remembered. The outputs folder is where they go to be found once; the brain is where they go to inform every future decision.

---

## Cross-Skill Links

- `/second-brain` -> before framing, query the `decisions` focus area so a settled debate is not relitigated; after, `ingest` to file this decision
- `/stakeholder-tactics` -> when the decision needs alignment before it will hold
- `/ralph-wiggum` -> when the rationale needs adversarial pressure before you publish it
- `/meeting-notes` -> when the decision came out of a meeting that also needs writing up
- `/status-update` -> when the decision changes what stakeholders were expecting
- `/pre-mortem` -> when a go/no-go decision needs failure modes surfaced first
