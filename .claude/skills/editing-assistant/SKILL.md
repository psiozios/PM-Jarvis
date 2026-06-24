---
name: editing-assistant
description: Edit and improve any PM document. Modes for shortening, clarifying, adapting audience, polishing prose, and strengthening arguments. Works on PRDs, strategy docs, status updates, emails, Slack messages, and more.
disable-model-invocation: false
user-invocable: true
---

# /editing-assistant - Edit Any PM Document

Paste your draft. Tell me what's wrong with it. I'll fix it without starting from scratch.

## Quick Start

```
/editing-assistant

Paste your document and tell me the edit mode:

--shorten     Cut by 30-50% without losing meaning
--clarify     Fix confusing sections, improve flow
--audience    Rewrite for a different reader (exec, engineer, customer, board)
--polish      Improve word choice, rhythm, and readability
--strengthen  Sharpen arguments, close logical gaps, add specificity
--tighten     Remove filler, hedge words, and passive voice

Or just describe what's wrong: "the middle section is rambling", "the ask is buried",
"this sounds too corporate", "the numbers don't land right"

Output: Returns the edited document in the same format, with a brief change summary.
```

---

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Writing Style | `context-library/writing-style-*.md` | tone, voice, format | PM's preferred style |
| Stakeholder Profiles | `context-library/stakeholder-template.md` | audience name | Audience-specific preferences |

**The golden rule:** Preserve the PM's voice. Fix what's wrong, not what's different.

**Cross-Skill Links:**
- PRD edits → Use in `/prd-draft` or `/prd-review-panel`
- Status update edits → Use in `/status-update`
- Slack message edits → Use in `/slack-message`

---

## Edit Modes

### `--shorten`
**Goal:** Remove 30-50% of words without losing any meaning.

**Method:**
- Kill filler phrases: "in order to," "it is important to note," "as a result of," "in the context of"
- Convert passive to active voice
- Cut hedge words: "somewhat," "generally," "relatively," "perhaps"
- Merge sentences that say the same thing
- Replace paragraphs with bullet points where appropriate
- Remove preambles: "As you know..." / "Given the above..." / "It goes without saying..."

**Before/after example:**
- Before: "In order to better understand the needs of our users, we conducted a series of customer interviews over the course of the last month, the results of which have been summarized below."
- After: "Last month's customer interviews revealed:"

### `--clarify`
**Goal:** Make confusing sections immediately understandable.

**Method:**
- Identify the sentence(s) where the reader would get lost
- Break complex ideas into steps
- Add concrete examples for abstract claims
- Move the conclusion before the reasoning (executive audiences)
- Replace jargon with plain language (or define it inline)
- Reorder paragraphs so logic flows forward, not circular

### `--audience`
**Goal:** Rewrite for a different reader.

**Tell me the target audience:**
- **Executive / C-suite:** Lead with impact, cut details, state the ask first
- **Engineering team:** Technical precision, explicit constraints, what's in scope and out of scope
- **Customer-facing:** Benefits before features, plain language, empathetic tone, no internal acronyms
- **Board / investors:** Business performance narrative, financial framing, strategic implications
- **Cross-functional (Sales/CS):** "What's in it for them," practical guidance, their language

**I'll check `context-library/stakeholder-template.md`** for known audience preferences.

### `--polish`
**Goal:** Make the document read like a senior PM wrote it.

**Method:**
- Vary sentence length (short punchy sentences next to complex ones)
- Replace vague words with specific ones: "big" → "3x," "soon" → "by March 15," "users" → "enterprise buyers with 100+ seats"
- Apply house-style rules from `config/house-style.md` (punctuation, word choice, tone)
- Start paragraphs with the point, not context-setting

### `--strengthen`
**Goal:** Make arguments airtight.

**Method:**
- Identify every claim that could be challenged
- For each: Is there evidence? If not, flag for the PM to add or caveat
- Surface logical gaps: "You jump from A to C — where's B?"
- Check if the "so what" is clear for every major point
- Tighten hypotheses: "We believe this will help users" → "We expect 15-20pt improvement in D7 activation based on our onboarding research"
- Make the ask/recommendation crystal clear

### `--tighten`
**Goal:** Remove weakness without removing content.

**Common culprits:**
- Hedge language: "somewhat," "relatively," "might," "could potentially"
- Passive voice: "was decided" → "we decided," "has been identified" → "we found"
- Circular openers: "In order to..." "Given that..." "As a result of..."
- Redundant pairs: "each and every," "first and foremost," "new and innovative"
- Unnecessary qualifiers: "very," "really," "quite," "basically"

---

## Free-Form Edit Requests

Don't need a mode? Just describe the problem:

- "The second paragraph is circular — it says the same thing three ways"
- "The ask is buried at the bottom, can you move it to the top?"
- "This sounds like AI wrote it, make it sound more human"
- "The exec summary is too long — cut it to 3 bullets"
- "The metrics section has no context — readers won't know if 40% is good or bad"
- "The tone is too formal for a Slack update"
- "The intro is defensive — rewrite it to sound confident"

---

## Change Summary Format

After editing, I'll provide:

```
## What I changed

**Mode used:** [mode or description]

**Key edits:**
- [What changed and why — 3-5 bullets]

**What I preserved:**
- [Structure/sections/arguments I intentionally kept]

**Suggestions for further improvement:**
- [1-2 things the PM could add/verify that would strengthen the document]
```

---

## Voice Rules

Always apply these regardless of mode:
- Read and apply rules from `config/house-style.md` (punctuation, word avoidance, tone)
- Vary sentence length for natural rhythm
- Specific over vague: real numbers, real names, real outcomes

---

## Output Quality Self-Check

- [ ] **Voice preserved:** The edited document still sounds like the PM, not like a different writer
- [ ] **Nothing lost:** No meaningful content was removed, only improved
- [ ] **Mode applied correctly:** The specific edit mode was executed, not just a general cleanup
- [ ] **Change summary included:** PM knows exactly what was changed and why
- [ ] **Style rules applied:** House-style rules from `config/house-style.md` followed


## Formal Eval

**Runs automatically after every skill invocation.** After generating output:

1. Run the informal Output Quality Self-Check above (fast, same agent)
2. Spawn a separate eval agent in a clean context window to run `evals.md` (same directory)
3. Eval agent reads: the output, this skill's evals.md, and `config/house-style.md`
4. If any eval returns FAIL → eval agent returns remediation instructions → original agent applies fixes → re-submit for eval
5. Loop until zero FAILs
6. Log final results in the Eval Results Log table in `evals.md`

See `references/protocols/skill-evals.md`.

## When to Use

- Edit and improve any PM document.

## When NOT to Use

- When a different skill better fits the task. Check Cross-Skill Links for alternatives.

## Common Mistakes

- Skipping context: not reading relevant workspace files before generating output
- Generic output: producing content that could apply to any company instead of using specific context from your workspace
- Missing the handoff: not offering the logical next skill when this one completes

## Cross-Skill Links

**Before:** Check relevant context files and run any prerequisite skills
**After:** See `references/skill-chains.md` for recommended next steps
**Related:** See skill category peers in CLAUDE.md
