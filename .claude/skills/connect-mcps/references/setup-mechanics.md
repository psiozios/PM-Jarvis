# Setup Mechanics

Bulk reference for `/connect-mcps`. Read during Steps 3, 6, 7 and 8 — what to extract from a tool's docs, how its category maps to skills, the block written into each skill file, and the registry format.



### What I Look For in Documentation

When researching an MCP, I extract:

**1. Setup Requirements**
- NPM package name or server URL
- Authentication method (API key, OAuth, token)
- Required configuration (workspace ID, project ID, etc.)
- Environment variables needed

**2. Tool Catalog**
- Available tools/functions
- Tool purposes and descriptions
- Parameter requirements (required vs optional)
- Return value structures

**3. Common Use Cases**
- Typical queries and operations
- Example workflows
- Best practices
- Rate limits or constraints

**4. Category Classification**
- Primary category (analytics, PM, research, etc.)
- Secondary categories if multi-purpose
- Keywords for routing logic

### Web Search Strategy

I use multiple search queries to find comprehensive information:

1. **"[tool] MCP server documentation 2026"** - Official MCP docs
2. **"[tool] MCP integration guide"** - Setup tutorials
3. **"[tool] Claude MCP setup"** - Claude-specific instructions
4. **"[tool] API authentication requirements"** - Auth details

I parse the results looking for:
- API key locations in the tool's settings
- Step-by-step setup instructions
- Code examples showing MCP usage
- Tool lists and function signatures




### How I Determine MCP Category

**Analytics/Metrics Keywords:**
analytics, metrics, data, dashboard, reporting, charts, insights, KPI, measurement, funnel, cohort, retention, events

**Project Management Keywords:**
tickets, issues, tasks, projects, sprints, backlog, epics, stories, roadmap, planning

**Research/Interviews Keywords:**
research, interviews, transcripts, insights, quotes, themes, tagging, synthesis, user feedback

**Transcription Keywords:**
transcription, audio, recording, speech-to-text, meeting recording, voice notes

**Communication Keywords:**
slack, email, messaging, notifications, chat, channels, DMs

**Documentation Keywords:**
docs, wiki, knowledge base, pages, workspace, notes

**Design/Prototyping Keywords:**
design, prototype, mockup, wireframe, UI, UX, Figma, components

**Web Search Keywords:**
search, browse, web, internet, competitor, market research

### Mapping Logic Examples

**Amplitude MCP detected** →
- Category: Analytics (keywords: analytics, metrics, events, funnel, cohort)
- Maps to: feature-metrics, impact-sizing, retention-analysis, activation-analysis, feature-results, metrics-framework, experiment-metrics

**Linear MCP detected** →
- Category: Project Management (keywords: issues, projects, tickets)
- Maps to: create-tickets, meeting-notes, status-update, prioritize

**Dovetail MCP detected** →
- Category: Research + Transcription (keywords: research, interviews, transcripts, insights)
- Maps to: user-interview, user-research-synthesis, interview-guide, meeting-notes




### Skill File Update Template

```markdown
### Using [MCP Name] (If Connected)

[1-2 sentence description of what this MCP provides]

**Available Tools:**
- `tool_name` - [Brief description]
- `tool_name_2` - [Brief description]

**Integration Example:**
```pseudocode
# [Example showing typical usage in this skill's context]
[tool_name].method({
  param1: value1,
  param2: value2
})
```

**Benefits:**
- [Benefit 1 - e.g., Real-time data access]
- [Benefit 2 - e.g., No manual exports needed]

**Fallback:** [What happens when MCP not available - e.g., "Upload CSV data to context-library/metrics/ for manual analysis"]
```

### Insertion Point Logic

1. **If "Prerequisites" section exists** → Insert immediately after
2. **If "How It Works" section exists** → Insert immediately after
3. **Otherwise** → Insert after title and frontmatter, before main content

This ensures MCP integration info appears early but doesn't interrupt the skill's primary instructions.

### Registry Format (`references/mcp-routing.md`)

**Registry Table:**
```markdown
| MCP | Purpose | Category | Used In | Key Tools |
|-----|---------|----------|---------|-----------|
| Amplitude | Product analytics | Analytics | feature-metrics, impact-sizing, retention-analysis | query_insights, get_funnels, cohort_analysis |
| Linear | Project management | PM Tools | create-tickets, meeting-notes, status-update | create_issue, update_issue, search_issues |
| Dovetail | User research | Research | user-interview, user-research-synthesis | search_insights, get_themes, export_quotes |
```

**Routing Logic:**
```markdown
**Analytics Queries** → Analytics MCPs (Amplitude, Mixpanel, Posthog)
- Pattern: "give me metrics on X", "show funnel for Y", "retention for Z"
- Multi-MCP: Ask user which tool to use
- Fallback: Check context-library/metrics/

**Task Queries** → PM MCPs (Linear, Jira)
- Pattern: "show my tasks", "create ticket for X", "status of epic Y"
- Multi-MCP: Ask user which tool to use
- Fallback: Check context-library/meetings/ for action items
```




When you run `/connect-mcps connect to amplitude`:

1. **I search the web** for Amplitude MCP documentation
2. **I parse** the results to extract setup requirements
3. **I prompt you** for each required credential
4. **I test** the connection to verify it works
5. **I discover** available tools by querying the MCP
6. **I categorize** the MCP (Analytics) based on keywords
7. **I map** to relevant skills (feature-metrics, impact-sizing, etc.)
8. **I read** each skill file to find insertion points
9. **I add** MCP integration sections to each skill
10. **I update** `references/mcp-routing.md` with the registry entry, the dialect row, and the routing logic
11. **I create** an integration log with full details
12. **I confirm** success and show you how to use it

All of this happens automatically in seconds. You just provide credentials and I handle the rest.

---

**Ready to connect your first MCP? Try:**

```
/connect-mcps connect to [your analytics tool]
```

And I'll guide you through the rest!

---

---

## Category to Skill Map

Based on the MCP category, I automatically map it to relevant skills:

**Analytics MCPs** (Amplitude, Mixpanel, Posthog, Pendo)
→ feature-metrics, impact-sizing, retention-analysis, activation-analysis, feature-results, metrics-framework, experiment-metrics

**Project Management MCPs** (Linear, Jira)
→ create-tickets, meeting-notes, status-update, prioritize

**Research MCPs** (Dovetail)
→ user-interview, user-research-synthesis, interview-guide

**Transcription MCPs** (Otter.ai, Fireflies)
→ meeting-notes, meeting-cleanup, user-interview

**Communication MCPs** (Slack)
→ slack-message, status-update, meeting-notes

**Documentation MCPs** (Notion, Confluence)
→ decision-doc, status-update, meeting-notes

**Design MCPs** (Figma)
→ generate-ai-prototype, napkin-sketch, prototype-feedback

**Web Search MCPs**
→ competitor-analysis, competitive-intel

**Multi-category MCPs** are mapped to multiple skill groups.
