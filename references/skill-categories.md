# Skill Categories

Extracted from the always-on core (`CLAUDE.md`) — a lookup table, not a rule. Read it when you need the shape of the library rather than a specific skill. For routing to one skill, the frontmatter `description` is the surface; for multi-skill sequences, see `references/skill-chains.md`.

87 skills, in `.claude/skills/<name>/SKILL.md`.

| Category | Count | Coverage |
|----------|-------|----------|
| Core PM Workflows | 21 | Planning, meetings, PRDs, status updates, decisions, communication, document ops |
| User Research & Interviews | 7 | Interviews, research synthesis, surveys, VoC |
| Strategic Frameworks | 8 | Strategy, OKRs, prioritization, metrics, journey maps |
| Product Analysis | 13 | Impact sizing, experiments, retention, pricing, root cause |
| Prototyping & Design | 6 | Design direction, prototypes, wireframes, feedback loops |
| Competitive Intelligence | 2 | Competitor analysis, sales battlecards |
| Development & Execution | 18 | Tickets, launches, sprints, code, execution plans, grooming, refinement |
| Automation & Cadence | 8 | Action sweeps, radar, periodic-review cascade, read-aheads, routine replies |
| Learning & Growth | 1 | Technical PM education |
| Knowledge Management | 2 | Compounding second-brain wiki, chat ingestion |
| Fun | 1 | Devil's advocate reviewer |

**Framework ownership.** Where two skills touch the same named framework, one owns it and the other uses it as a screen. Current owners:

| Framework | Owner | Used as a screen by |
|-----------|-------|---------------------|
| STEDII (trustworthy experiment metrics) | `/experiment-metrics` | `/feature-metrics` |
| TAM / SAM / SOM | `/opportunity-sizing` | `/impact-sizing` |
| Pre-commitment feature brief | `/prd-lite` | `/prd-draft` (alias only) |
| Codebase context | `/explore-codebase` | `/code-first-draft`, `/prototype-feedback` |

Add a row here before a second skill starts teaching an existing framework — that is how the contradiction this table exists to prevent gets caught early.
