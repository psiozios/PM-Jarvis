# Sub-Agents

7 reviewer personas for multi-perspective feedback. Each is defined in `sub-agents/`.

## What Every Persona Owes

**Cite the section you are objecting to.** A persona's job is to refute, and a refutation that names no passage cannot be checked — the parent has to reopen the document for anything it promotes to a blocker, and it cannot do that against "this feels underspecified". Every finding names the section, requirement, or line it is about, and quotes the phrase it is arguing with.

**Do not supply facts the document did not.** "Last three times we tried this it failed" is a claim about history the persona was not given. Ask the question instead: name what you would need to see. Inventing the evidence for your own objection is the one failure that makes a panel worse than no panel, and `/ralph-wiggum` — the skeptic persona as a skill — already holds itself to this. The personas hold to it too.

## Available Agents

| Agent | File | Perspective |
|-------|------|-------------|
| Engineer | `sub-agents/engineer-reviewer.md` | Technical feasibility, complexity, performance, dependencies |
| Designer | `sub-agents/designer-reviewer.md` | UX/UI, usability, accessibility, visual consistency |
| Executive | `sub-agents/executive-reviewer.md` | Strategic alignment, business impact, ROI |
| Legal | `sub-agents/legal-advisor.md` | Compliance, risk, regulatory, privacy |
| UX Researcher | `sub-agents/uxr-analyst.md` | User research synthesis, insight validation |
| Skeptic | `sub-agents/skeptic.md` | Devil's advocate, assumption challenges |
| Customer Voice | `sub-agents/customer-voice.md` | Simulated user perspective, adoption barriers |

## Spawning Protocol

When spawning sub-agents for review:

1. **State the agent** you're invoking
2. **Give each agent** the specific document or task to review
3. **Synthesize feedback** across all agents at the end
4. **Flag conflicts** between perspectives (e.g., engineer says "too complex" while designer says "need more features")
5. **Re-read the document yourself for anything that becomes a verdict.** A persona's job is to refute — to find the objection you would not have raised. The finding it hands back is a pointer, and promoting one to a blocker means opening the document at that section and confirming it says what the report says it says. A report about a document is not the document (`references/capabilities.md`), and a quoted line inside a report is the most persuasive part of it, not the most checked.

## When to Use

- `/prd-review-panel` automatically spawns all 7 agents
- You can invoke individual agents for targeted feedback
- Use 2-3 agents for focused reviews, all 7 for comprehensive reviews

## Parallel Execution

**Two shapes, and the choice is between independence and cost.** Spawning the personas in parallel keeps each one from being biased by the others' feedback, which is the whole value of a panel — that is `/prd-review-panel`. Reading the persona file and answering in-session costs no extra context window but loses that independence, because one agent holding all seven lenses converges them — that is how `/prd-draft` uses them for a lighter pass.

Pick by what the output is for. **A panel whose disagreements you need is spawned; two or three lenses you want applied to a draft are read in-session.** Neither is a default: state which you used. The cost side is `references/capabilities.md`; a per-item fan-out is a different shape again, see below.

**A fixed panel is not a per-item fan-out.** The seven personas above are a bounded set reading one document, and each returns a perspective the others cannot. Spawning one agent per candidate down a list of thirty is a different shape with a different cost — see the spawn gate in `references/capabilities.md` before building one.
