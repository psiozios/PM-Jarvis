# Tool Catalog

Bulk reference for `/connect-mcps`. Read when the user asks which tools are worth connecting, or wants a recommended stack. Tiers and tool lists go stale — treat this as a starting map, and check the tool's own docs for what its MCP actually exposes today.



Based on real PM workflows, here's which MCPs provide the highest value. Start with Priority Tier, then add others as needed.

### Priority Tier: Must-Have MCPs ⭐⭐⭐⭐⭐

Connect these first. They provide immediate ROI for product managers.

#### 1. Analytics Tools (Amplitude, Mixpanel, Posthog, Pendo)

**Why connect:** Self-serve analytics without waiting on data team. Ask questions and get answers in seconds.

**What you can do:**
- "What's the funnel conversion rate for onboarding?"
- "Show me retention by signup cohort for last quarter"
- "Which features correlate with power user behavior?"
- "Pull session recordings for users who churned last week"

**Setup:** Run `/connect-mcps connect to amplitude` (or your analytics tool)

**Tools discovered:** query_insights, get_funnels, cohort_analysis, event_tracking, session_replays

**Best for:** Feature performance analysis, A/B test results, user behavior research

---

#### 2. Project Management (Linear, Jira, Asana)

**Why connect:** Batch create tickets from meeting notes. Generate sprint reports. Track engineering progress without tab-switching.

**What you can do:**
- "Take these action items and create Linear tickets"
- "Show completed tickets from current sprint"
- "List all blocked tickets and their reasons"
- "Update ticket LIN-123 to mark it as done"

**Setup:** Run `/connect-mcps connect to linear` (or your PM tool)

**Tools discovered:** create_issue, update_issue, search_issues, get_project_status

**Best for:** Meeting follow-ups, sprint planning, progress tracking

---

#### 3. Communication (Slack, Microsoft Teams)

**Why connect:** Share analysis summaries. Search past decisions. Draft announcements without leaving Claude.

**What you can do:**
- "Summarize this week's work and post to #engineering-updates"
- "Search Slack for conversations about pricing from last month"
- "Draft an announcement for the feature launch"
- "Find the decision about API versioning we discussed"

**Setup:** Run `/connect-mcps connect to slack`

**Tools discovered:** read_channels, post_message, search_history, manage_threads

**Best for:** Team updates, decision archaeology, communication drafts

---

#### 4. Documentation (Notion, Confluence, Google Drive)

**Why connect:** Access PRDs and specs. Create documents from templates. Search institutional knowledge.

**What you can do:**
- "Search my Drive for customer interview notes from Q3"
- "Create a PRD for dark mode and save to Product Docs"
- "Read the Q4 roadmap and summarize key themes"
- "Update the onboarding guide with new screenshots"

**Setup:** Run `/connect-mcps connect to notion` (or your docs tool)

**Tools discovered:** read_pages, create_document, search_workspace, update_pages

**Best for:** Document creation, knowledge search, team alignment

---

### High Value Tier: Very Useful ⭐⭐⭐⭐

Not required day one, but add these once core setup is done.

#### 5. Design Tools (Figma, Sketch)

**Why connect:** Reference designs in conversations. Extract specs from mockups. Track design feedback.

**What you can do:**
- "Summarize feedback on the new dashboard design"
- "Export the mobile mockups as PNGs"
- "What's the latest version of the checkout flow?"

**Setup:** Run `/connect-mcps connect to figma`

**Best for:** Design review, spec extraction, version tracking

---

#### 6. Calendar (Google Calendar, Outlook)

**Why connect:** Analyze time allocation. Schedule research sessions. Find focus time patterns.

**What you can do:**
- "Analyze my calendar this week - where did I spend time?"
- "Find a 1-hour slot for user interviews next week"
- "Create recurring 1:1s with my reports"

**Setup:** Run `/connect-mcps connect to google-calendar`

**Best for:** Time management, meeting scheduling, calendar analysis

---

#### 7. Code Repository (GitHub, GitLab)

**Why connect:** Track engineering progress. Review technical discussions. Understand implementation details.

**What you can do:**
- "What PRs were merged in the mobile repo this week?"
- "Summarize the discussion in issue #234 about performance"
- "Create a PR to update the API documentation"

**Setup:** Run `/connect-mcps connect to github`

**Best for:** Engineering collaboration, progress tracking, technical context

---

### Specialized Tier: Niche But Powerful ⭐⭐⭐

For specific workflows or advanced users.

#### 8. Customer Support (Zendesk, Intercom)

**What you can do:**
- Analyze support tickets for patterns
- Find common user issues
- Track resolution times
- Identify bug clusters

**Setup:** Run `/connect-mcps connect to zendesk`

**Best for:** Support insights, bug prioritization, customer pain points

---

#### 9. Revenue Tools (Stripe, ChartMogul)

**What you can do:**
- Analyze subscription trends
- Track MRR changes
- Identify churn patterns
- Monitor payment issues

**Setup:** Run `/connect-mcps connect to stripe`

**Best for:** Revenue analysis, subscription health, payment insights

---

#### 10. Social Listening (Twitter/X, Reddit)

**What you can do:**
- Monitor competitor mentions
- Analyze user sentiment
- Find feature requests in the wild
- Track industry trends

**Setup:** Run `/connect-mcps connect to reddit`

**Best for:** Competitive intelligence, user research, trend spotting

---

### Choosing Your Stack

**For Solo PM:**
- Analytics + Project Management + Slack + Docs
- Setup time: 30-45 minutes
- Covers 80% of daily workflows

**For PM Team:**
- Solo stack + Design + Calendar + GitHub
- Setup time: 1-2 hours
- Full workflow coverage

**For PM Leader:**
- Team stack + Support + Revenue tools
- Setup time: 2-3 hours
- Complete analytics and insights

**Pro tip:** Start small. Add one MCP at a time as you discover needs. More MCPs ≠ better.

---

### Setup Difficulty Guide

**Easy (5-10 min):**
- Linear, Jira: API token only
- Slack: Workspace token
- GitHub: Personal access token

**Medium (10-20 min):**
- Amplitude, Mixpanel: API key + Project ID
- Notion: Integration setup required
- Figma: OAuth flow

**Advanced (20-30 min):**
- Google Drive: OAuth + permission scopes
- Database tools: Credentials + read-only setup
- Calendar: OAuth + calendar selection

---

### Analytics Tool Details

Since analytics is the #1 requested integration, here's the specifics:

**PostHog MCP**
- Official server: `@anthropic/posthog-mcp`
- What you need: API key, host URL (US/EU/self-hosted)
- Tools: Insights, funnels, experiments, feature flags, session replays
- Query language: SQL-like HogQL
- Best for: Self-hosted analytics, session replay analysis

**Amplitude MCP**
- Official server: `@anthropic/amplitude-mcp`
- What you need: API key, Project ID
- Tools: Insights, funnels, cohorts, user profiles
- Query language: AQL (Amplitude Query Language)
- Best for: Behavioral analytics, cohort analysis

**Mixpanel MCP**
- Community server: `mcp-server-mixpanel`
- What you need: Project token, API secret
- Tools: Events, funnels, flows, retention
- Query language: JQL (Mixpanel JSON Query Language)
- Best for: Event-based analytics, user flows

**Pendo MCP**
- Beta status: Check Pendo docs for latest
- What you need: API key, subscription key
- Tools: Product usage, guides, NPS scores
- Best for: Product adoption analytics

**Common Analytics Queries:**
```
"What's our week-over-week active user growth?"
"Show me the conversion funnel for checkout"
"Which features have the highest correlation with retention?"
"Pull session recordings where users encountered errors"
"Create a cohort of power users who logged in 10+ times"
"What's the statistical significance of our pricing experiment?"
```

---

### Maintenance Tips

**Weekly:**
- Test critical integrations with simple queries
- Check MCP logs for errors (if issues arise)
- Update API tokens if expiring soon

**Monthly:**
- Update MCP servers to latest versions (`npm update`)
- Review permissions and access scopes
- Remove MCPs you haven't used

**Quarterly:**
- Evaluate new MCP releases
- Assess ROI of each integration
- Optimize configuration for performance

**Signs you need to update:**
- Connection errors or timeouts
- Missing tools that should be available
- Slow response times
- Authentication failures

---

### Security Best Practices

**API Keys:**
- Use read-only credentials whenever possible
- Store keys in environment variables, never in code
- Rotate keys quarterly or when team members leave
- Never share keys in Slack or email

**Permissions:**
- Grant minimum required scopes
- Audit access regularly
- Use separate keys for prod vs staging
- Revoke unused tokens immediately

**Data Privacy:**
- Don't query PII unless necessary
- Be mindful of GDPR/data regulations
- Use aggregated data when possible
- Don't export sensitive user data to logs

---

### Getting Help

**When MCP connection fails:**
1. Check API key is correct (no typos, extra spaces)
2. Verify token hasn't expired
3. Confirm required permissions are granted
4. Test the API key in the tool's web interface first
5. Check network/firewall isn't blocking MCP server

**Resources:**
- **MCP Documentation:** https://modelcontextprotocol.io
- **Anthropic Forums:** https://discuss.anthropic.com
- **GitHub Issues:** https://github.com/modelcontextprotocol/servers
- **Community Discord:** MCP Community server

**For PM-specific help:**
- Check `outputs/mcp-integration-logs/` for detailed error messages
- Ask in chat: "Why did my Amplitude connection fail?"
- Reference `references/mcp-routing.md` for routing logic

---

