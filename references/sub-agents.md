# Sub-Agents

7 reviewer personas for multi-perspective feedback. Each is defined in `sub-agents/`.

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

## When to Use

- `/prd-review-panel` automatically spawns all 7 agents
- You can invoke individual agents for targeted feedback
- Use 2-3 agents for focused reviews, all 7 for comprehensive reviews

## Parallel Execution

When reviewing from multiple perspectives, spawn agents in parallel rather than sequentially. This is faster and prevents later agents from being biased by earlier feedback.

**A fixed panel is not a per-item fan-out.** The seven personas above are a bounded set reading one document, and each returns a perspective the others cannot. Spawning one agent per candidate down a list of thirty is a different shape with a different cost — see the spawn gate in `references/capabilities.md` before building one.
