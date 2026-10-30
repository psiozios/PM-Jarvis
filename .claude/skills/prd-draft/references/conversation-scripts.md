# Conversation Scripts

Bulk reference for `/prd-draft`, extracted verbatim from its `SKILL.md`. Read when you are about to speak to the PM at a step: the opening, the context check, the follow-ups, the draft hand-off, the prototype and review offers, the wrap-up. The rules this material serves stay in `SKILL.md`; nothing here overrides them.

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
8. Who are the key stakeholders? (I'll write them as plain names, not @-mentions, until you say the draft is ready)

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

I'll create it now and save it to `outputs/prds/[feature-name-kebab-case].md`.

After you review, we can iterate or get multi-perspective feedback.
```

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
First draft created! Saved to `outputs/prds/[feature-name].md`.

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
