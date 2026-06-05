# File Creation Rules

## The Two-Zone Model

| Zone | Purpose | Who writes | Location |
|------|---------|-----------|----------|
| **Outputs** | Active work in progress | The assistant | `outputs/` |
| **Context Library** | Finalized reference and history | The user (with assistant help on confirm) | `context-library/` |

**Rule:** The assistant writes new files to `outputs/` only. Never to `context-library/`, `config/`, `templates/`, or any other location without explicit instruction from the user.

Once the user finalizes work from `outputs/`, they can move it to `context-library/` for future reference.

## Output Directory Taxonomy

| Directory | What goes here | Created by |
|-----------|---------------|-----------|
| `outputs/prds/` | PRDs being drafted | `/prd-draft`, `/prd-lite` |
| `outputs/meeting-notes/` | Processed meeting notes | `/meeting-notes`, `/meeting-cleanup` |
| `outputs/status-updates/` | Stakeholder updates | `/status-update` |
| `outputs/analyses/` | Impact sizing, feature analysis | `/impact-sizing`, `/feature-results`, `/activation-analysis`, `/retention-analysis` |
| `outputs/research-synthesis/` | Interview synthesis, research | `/user-research-synthesis`, `/user-interview` |
| `outputs/decisions/` | Decision docs in progress | `/decision-doc` |
| `outputs/slack-messages/` | Draft communications | `/slack-message` |
| `outputs/prototypes/` | Prototype prompts, wireframes | `/prototype`, `/generate-ai-prototype`, `/napkin-sketch` |
| `outputs/journey-maps/` | User/customer journey maps | `/journey-map` |
| `outputs/surveys/` | Survey designs | `/survey-builder` |
| `outputs/roadmaps/` | Roadmap drafts | various |
| `outputs/board-decks/` | Executive presentations | `/board-deck` |
| `outputs/business-canvases/` | BMC and Lean Canvas | `/business-model-canvas` |
| `outputs/okrs/` | OKR planning docs | `/okr-planning` |
| `outputs/pre-mortems/` | Pre-mortem risk registers | `/pre-mortem` |
| `outputs/post-mortems/` | Post-mortem reports | `/post-mortem` |
| `outputs/win-loss/` | Win/loss analyses | `/win-loss-analysis` |
| `outputs/content/` | Launch copy, changelogs, onboarding | `/content-marketing` |
| `outputs/plans/` | Tracked execution plans | `/execution-plan` |
| `outputs/weekly-plans/` | Weekly priority plans | `/weekly-plan` |
| `outputs/weekly-reviews/` | Weekly retrospectives | `/weekly-review` |
| `outputs/mcp-integration-logs/` | MCP connection logs | `/connect-mcps` |
| `outputs/skill-test-results/` | Skill test output | testing |

## Context Library Taxonomy

These folders store finalized, user-curated reference material:

| Directory | Content |
|-----------|---------|
| `context-library/prds/` | Finalized PRDs, one-pagers, feature briefs |
| `context-library/strategy/` | Roadmaps, OKRs, vision docs, GTM, framework references |
| `context-library/research/` | User research, competitive analysis, personas |
| `context-library/decisions/` | Decision logs, trade-off docs, RFCs |
| `context-library/launches/` | Launch plans, release notes, go-live checklists |
| `context-library/metrics/` | Analytics reports, A/B test results, dashboard exports |
| `context-library/meetings/` | Meeting notes, retros, syncs, 1:1s |
| `context-library/example-prds/` | Reference PRD examples |
| `context-library/second-brain/` | LLM-maintained wikis by focus area |
| `context-library/other/` | Anything that doesn't fit above |

## Naming Conventions

- Use kebab-case for file names: `voice-task-capture-team-kickoff.md`
- Include dates where relevant: `2025-03-15-stakeholder-sync.md`
- Include stage for PRDs: `[feature]-[stage].md` (e.g., `dark-mode-team-kickoff.md`)
