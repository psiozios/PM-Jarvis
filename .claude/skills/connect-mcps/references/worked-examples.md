# Worked Examples

Bulk reference for `/connect-mcps`. Read when you want to see a full connection end to end, or how a natural-language query routes after setup.



### Example 0: Figma (Design - Remote MCP Server) ⭐ RECOMMENDED METHOD

```
User: /connect-mcps connect to figma

Me:
Let me help you connect Figma to your PM Jarvis workspace.

[Searches: "Figma official MCP server"]
[Finds: https://developers.figma.com/docs/figma-mcp-server/]

✅ **Great news! Figma has an official remote MCP server.**

**This is the easiest method:**

1. Run this command in your terminal:
   ```bash
   claude mcp add --transport http figma https://mcp.figma.com/mcp
   ```

2. After adding, type `/mcp` in Claude Code

3. You'll see Figma in your MCP list (disconnected)

4. Press Enter on Figma to log in with your Figma account

5. Authenticate and you're done!

**No API keys needed, no OAuth setup, just authenticate and go.**

**Once connected, you can:**
- "Get the latest version of the checkout flow from Figma"
- "Export the mobile mockups from our design file"
- "Show me feedback comments on the dashboard design"
- "What components are in our design system?"

Full documentation: https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/
```

---

### Example 1: Amplitude (Analytics)

```
User: /connect-mcps connect to amplitude

Me:
Let me help you connect Amplitude to your PM Jarvis workspace.

[Searches: "Amplitude MCP server documentation 2026"]
[Finds: GitHub repo, NPM package, setup guide]

**To connect Amplitude, I need:**
1. Amplitude API Key (Settings → API Keys)
2. Project ID (Settings → Projects)

Find these at: https://analytics.amplitude.com/settings

**Enter your Amplitude API Key:**

User: [pastes: ak_live_abc123...]

Me: **Enter your Project ID:**

User: [pastes: 12345]

Me:
Testing connection... ✓ Connected successfully!

**Discovered Amplitude tools:**
- `query_insights` - Query product analytics data
- `get_funnels` - Retrieve funnel analysis
- `cohort_analysis` - Analyze user cohorts
- `event_tracking` - Track custom events
- `user_properties` - Get user property data

**Category:** Analytics

**Integrating with PM Jarvis skills...**
✓ feature-metrics updated
✓ impact-sizing updated
✓ retention-analysis updated
✓ activation-analysis updated
✓ feature-results updated
✓ metrics-framework updated
✓ experiment-metrics updated

**Updating the registry in references/mcp-routing.md...**
✓ MCP registry table updated
✓ Query routing logic updated

**Amplitude connected! 🎉**

You can now ask analytics questions in natural language:

Examples:
- "Give me metrics on the checkout feature in the last 2 weeks"
- "Show me the funnel for user onboarding"
- "What's the retention rate for users who signed up in December"
- "Compare conversion rates between mobile and web"

I'll automatically query Amplitude and return the data with insights.

Full log: outputs/mcp-integration-logs/2026-01-30-amplitude.md
```

### Example 2: Linear (Project Management)

```
User: /connect-mcps connect to linear

Me:
Let me help you connect Linear to your PM Jarvis workspace.

[Searches: "Linear MCP server documentation 2026"]

**To connect Linear, I need:**
1. Linear API Key (Settings → API → Personal API Keys)
2. Team ID (optional, for team-specific queries)

Find your API key at: https://linear.app/settings/api

**Enter your Linear API Key:**

User: [pastes: lin_api_...]

Me: **Enter your Team ID (or press Enter to skip):**

User: [presses Enter]

Me:
Testing connection... ✓ Connected successfully!

**Discovered Linear tools:**
- `create_issue` - Create new issues/tickets
- `update_issue` - Update existing issues
- `search_issues` - Search and filter issues
- `get_team_issues` - Get all team issues
- `create_project` - Create projects/epics

**Category:** Project Management

**Integrating with PM Jarvis skills...**
✓ create-tickets updated
✓ meeting-notes updated
✓ status-update updated
✓ prioritize updated

**Updating the registry in references/mcp-routing.md...**
✓ MCP registry updated
✓ Query routing logic updated

**Linear connected! 🎉**

You can now manage tasks naturally:

Examples:
- "Show my open tickets"
- "Create a ticket for the login bug"
- "What's the status of the redesign project"
- "Update ticket LIN-123 to mark it as done"

I'll automatically query Linear and perform operations.

Full log: outputs/mcp-integration-logs/2026-01-30-linear.md
```

### Example 3: Batch Connection

```
User: /connect-mcps batch

Me:
Let's connect multiple MCPs at once.

**Common PM tools:**
- Analytics: Amplitude, Mixpanel, Posthog, Pendo
- Project Management: Linear, Jira
- Research: Dovetail
- Documentation: Notion
- Communication: Slack

**Which tools would you like to connect?** (comma-separated)

User: amplitude, linear, notion

Me:
I'll connect these 3 MCPs. Starting with Amplitude...

**1/3: Amplitude**
To connect Amplitude, I need:
1. API Key (Settings → API Keys)
2. Project ID (Settings → Projects)

Enter your Amplitude API Key:

[... continues with guided setup for each tool ...]

**All 3 MCPs connected! 🎉**

Summary:
✓ Amplitude (Analytics) - 7 skills updated
✓ Linear (PM Tools) - 4 skills updated
✓ Notion (Documentation) - 3 skills updated

You can now:
- Ask analytics questions → I'll query Amplitude
- Manage tasks → I'll use Linear
- Access docs → I'll search Notion

Full logs saved to: outputs/mcp-integration-logs/2026-01-30-batch/
```




Once MCPs are connected, you can ask questions naturally and I'll route them automatically.

### Example: Analytics Query

```
User: Give me metrics on the login feature in the last 2 weeks

Me:
[Checks the registry in references/mcp-routing.md]
[Finds: Amplitude connected for analytics]
[Routes to: Amplitude MCP query_insights tool]

**Login Feature Metrics (Last 2 Weeks)**
Source: Amplitude

📊 **Volume:**
- Total logins: 45,832
- Unique users: 12,443
- Sessions with login: 38,291

✅ **Success Rate: 94.2%**
- Successful logins: 43,174
- Failed attempts: 2,658 (5.8%)

⏱️ **Performance:**
- Average time to login: 3.2 seconds
- Median time: 2.8 seconds

📈 **Trends (vs previous 2 weeks):**
- Login volume: +12% ↑
- Success rate: +2.1% (was 92.1%) ↑
- Avg time: -0.4s (faster) ↑

🔍 **Insights:**
- Mobile login success rate (91.3%) is 5.5% lower than web (96.8%)
- Password reset requests up 8% - may indicate login friction
- Peak login times: 9-10 AM and 2-3 PM

**Want me to:**
- Dig into mobile vs web differences?
- Analyze failed login reasons?
- Compare to last month?
```

### Example: Multi-MCP Disambiguation

```
User: Show me the checkout funnel

Me:
I found 2 analytics tools connected: Amplitude and Mixpanel.

Which one should I use for this query?
A) Amplitude
B) Mixpanel

User: A

Me:
[Queries Amplitude for funnel data]

**Checkout Funnel (Last 30 Days)**
Source: Amplitude

1. **Add to cart** → 25,432 users (100.0%)
2. **View cart** → 18,901 users (74.3%) ↓ 25.7% drop-off
3. **Enter payment** → 14,223 users (55.9%) ↓ 24.8% drop-off
4. **Complete purchase** → 11,887 users (46.7%) ↓ 16.4% drop-off

**Overall Conversion Rate: 46.7%**

**Biggest Drop-offs:**
1. Add to cart → View cart (25.7%)
2. View cart → Enter payment (24.8%)

**Segments:**
- New users: 38.2% conversion
- Returning users: 52.1% conversion
- Mobile: 41.3% conversion
- Web: 49.8% conversion

Want me to analyze why users drop off at specific steps?
```

### Example: Task Management Query

```
User: Show my open tasks in Linear

Me:
[Checks registry: Linear connected]
[Queries Linear: get_team_issues filtered by assignee]

**Your Open Tasks (8 total)**
Source: Linear

**High Priority (2):**
- LIN-234: Fix login bug on mobile Safari (Due: Tomorrow)
- LIN-189: Review Q1 metrics dashboard (Due: Friday)

**Medium Priority (4):**
- LIN-267: User interview synthesis
- LIN-255: Update PRD for checkout redesign
- LIN-241: Competitive analysis - payment flows
- LIN-228: Roadmap planning for H2

**Low Priority (2):**
- LIN-201: Document API endpoints
- LIN-177: Update team wiki

Want me to:
- Create tickets from our conversation?
- Update status of any tickets?
- Show details for a specific ticket?
```

