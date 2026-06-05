# MCP Routing

This file defines how natural-language queries route to the right MCP server or context-library fallback.

## Connected MCPs

| MCP | Purpose | Category | Used In | Key Tools |
|-----|---------|----------|---------|-----------|
| _None connected yet_ | Run `/connect-mcps connect to [tool]` to get started | - | - | - |

<!-- After connecting MCPs, entries appear like:
| Amplitude | Product analytics | Analytics | feature-metrics, impact-sizing, retention-analysis | query_insights, get_funnels, cohort_analysis |
| Linear | Project management | PM Tools | create-tickets, meeting-notes, status-update | create_issue, update_issue, search_issues |
-->

## Query Routing Rules

### Analytics Queries --> Analytics MCPs (Amplitude, Mixpanel, Posthog, Pendo)

Trigger phrases: "metrics on", "funnel for", "retention for", "conversion rate", "DAU", "MAU"

- If multiple analytics MCPs connected, ask which to use
- **Fallback:** `context-library/metrics/` for exported data

### Feature Performance --> Analytics MCPs + Context Files

Trigger phrases: "how is feature X performing", "numbers for", "results of"

- Check analytics MCP first, then `context-library/prds/` and `context-library/metrics/`

### Task / Ticket Queries --> PM MCPs (Linear, Jira)

Trigger phrases: "open tasks", "status of epic", "create ticket", "update ticket"

- If multiple PM MCPs connected, ask which to use
- **Fallback:** `context-library/meetings/` for action items

### User Research --> Research MCPs (Dovetail) + Research Files

Trigger phrases: "users say about", "research on", "quotes about"

- Check research MCP first, then `context-library/research/`

### Competitor Intelligence --> Web Search + Competitive Files

Trigger phrases: "competitor doing", "how does X compare"

- Check `context-library/research/competitive-*.md` first, then web search

### Strategy / Decisions --> Context Library

Trigger phrases: "why did we decide", "strategy for", "decision log"

- Search `context-library/decisions/` and `context-library/strategy/`

### Meeting Notes / Action Items --> Context Library + PM MCPs

Trigger phrases: "action items from", "notes from meeting"

- Check `context-library/meetings/` first, then PM MCPs for task status

## Connecting New MCPs

Use `/connect-mcps connect to [tool name]` for guided setup.

**Priority order:** Remote MCP servers > Local servers > Manual OAuth/tokens

**After connecting:**
1. Test the connection and discover available tools
2. Map the MCP to relevant skills
3. Update this routing table
4. Save integration log to `outputs/mcp-integration-logs/`

## Graceful Degradation

All skills work without MCPs by falling back to context-library files and manual user input. MCPs are optional enhancements, not requirements.
