# MCP Routing

This file defines how natural-language queries route to the right MCP server or context-library fallback.

## Connected MCPs

| MCP | Purpose | Category | Auth | Used In | Key Tools |
|-----|---------|----------|------|---------|-----------|
| _None connected yet_ | Run `/connect-mcps connect to [tool]` to get started | - | - | - | - |

<!-- After connecting MCPs, entries appear like:
| Amplitude | Product analytics | Analytics | token | feature-metrics, impact-sizing, retention-analysis | query_insights, get_funnels, cohort_analysis |
| Linear | Project management | PM Tools | oauth | create-tickets, meeting-notes, status-update | create_issue, update_issue, search_issues |
-->

**The Auth column is load-bearing.** An `oauth` source cannot repair itself in an unattended run — the refresh needs a browser and a human, and the failure arrives as an empty result rather than an error. Record the auth type when you connect the tool and register a check for it in `config/source-preflight.json`. See `references/protocols/source-preflight.md`.

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

### Outward Content --> Brand / Design System MCPs (Figma, brand or style-guide services)

Trigger phrases: "launch copy", "announcement", "changelog", "release notes", "in-app copy", "onboarding copy", "help doc", "case study", "customer email"

- **Read the brand or style system live, before drafting.** It is the register authority for outward content — see `references/protocols/register.md`
- If a design system MCP is connected, query it for voice, vocabulary, and product naming rather than inferring them
- **Fallback:** a local mirror in `context-library/`, used only when the live system is unreachable, cited with its snapshot date, and never treated as the authority
- Positioning and messaging docs are **not** a fallback for voice — they answer a different question

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
2. Record the auth type, and register a preflight check for the source in `config/source-preflight.json`
3. Map the MCP to relevant skills
4. Update this routing table
5. Save integration log to `outputs/mcp-integration-logs/`

## Graceful Degradation

All skills work without MCPs by falling back to context-library files and manual user input. MCPs are optional enhancements, not requirements.

**Three failure modes, not one.** *Not connected* is the case this file was written for. *Connected but failing* — an expired token, a revoked scope, an OAuth refresh with no browser — is the dangerous one, because the tool answers with an empty result and the source leaves the run without saying so. *Connected and empty* is a real zero and a finding about the window. Only the last of the three may be read as data. `references/protocols/source-preflight.md` carries the check contract and the rule that a failed source is named with its reason and never counted as swept.
