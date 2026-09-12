# Troubleshooting

Bulk reference for `/connect-mcps`. Read when a connection fails, a query does not route, or the user wants to disconnect a tool.



### Common Issues & Solutions

**1. MCP Documentation Not Found**
```
Me: I couldn't find setup documentation for [tool] MCP.

Do you have a link to the documentation or know the setup requirements?

User: [provides link or details]

Me: [proceeds with setup using provided info]
```

**2. Invalid Credentials**
```
Me: Connection test failed. The API key appears to be invalid.

Please double-check:
- API key is copied completely (no extra spaces)
- API key has required permissions
- API key hasn't expired

Want to try again? Enter your API key:
```

**3. MCP Already Connected**
```
User: /connect-mcps connect to amplitude

Me: Amplitude is already connected!

Current configuration:
- Category: Analytics
- Tools: query_insights, get_funnels, cohort_analysis
- Used in: 7 skills

Want to:
- Test connection (verify it still works)
- Reconfigure (update credentials)
- View integration details
```

**4. Skill File Read-Only**
```
Me: ⚠️ Warning: Couldn't update feature-metrics skill (file locked)

I'll continue with other skills and log this issue.

14 out of 15 skills updated successfully.

Check: outputs/mcp-integration-logs/[timestamp]-errors.md
```

**5. Ambiguous Category**
```
Me: I found [tool] MCP but I'm unsure which category it fits.

The tool appears to handle:
- Feature flagging
- A/B testing
- Analytics

Which PM Jarvis skills should integrate with this MCP?
A) Analytics skills (metrics, retention, experiments)
B) Product skills (PRD, decisions)
C) Both A and B

User: C

Me: [maps to both skill groups]
```




### "I couldn't find documentation for [tool] MCP"

**Solution:** The tool may not have an official MCP server yet. Check:
- The tool's official docs for MCP support
- GitHub for community MCP implementations
- The Anthropic MCP directory

If no MCP exists, you can still use the tool manually and store outputs in `context-library/`.

### "Connection test failed"

**Solution:**
1. Verify credentials are correct (no typos, no extra spaces)
2. Check API key hasn't expired
3. Confirm API key has required permissions/scopes
4. Test the API key in the tool's web interface first
5. Check for network/firewall issues blocking MCP server

### "Skills weren't updated"

**Solution:**
1. Check the integration log in `outputs/mcp-integration-logs/`
2. Look for error messages indicating which skills failed
3. Verify skill files aren't read-only or locked
4. Re-run `/connect-mcps connect to [tool]` to retry updates

### "Queries aren't routing to my MCP"

**Solution:**
1. Check `references/mcp-routing.md` → verify the MCP is listed
2. Verify routing logic includes your MCP category
3. Try being more explicit: "Use Amplitude to show me metrics on X"
4. Check if MCP connection is still active (test with simple query)

### "I want to disconnect an MCP"

**Solution:** Currently, to disconnect:
1. Remove the MCP from your system (uninstall server/remove credentials)
2. Edit `references/mcp-routing.md` to remove the MCP from the registry table
3. Optionally, remove MCP sections from skill files

(Future enhancement: `/mcp disconnect [tool]` command)

---




1. **Connect MCPs during initial setup** - The first-time workspace setup will prompt you to connect your tools. Do it then for a seamless experience.

2. **Use natural language after setup** - Don't think about which MCP to call. Just ask your question naturally and I'll figure out the routing.

3. **Batch connect if you can** - If you're setting up multiple tools, use `/connect-mcps batch` to go through them all at once.

4. **Test with simple queries first** - After connecting, try a simple query like "show me X" to verify the connection works before complex queries.

5. **Keep credentials handy** - Have your API keys and workspace IDs ready before running `/connect-mcps connect to [tool]` to speed up setup.

6. **Check the integration log** - Each connection creates a log in `outputs/mcp-integration-logs/` with full details about what was updated.

7. **MCPs are optional** - See `references/mcp-routing.md` for per-source fallbacks when a tool is not connected (e.g., "Upload CSV to context-library/metrics/").

8. **Re-run `/connect-mcps connect` to update** - If credentials change or expire, just run the connect command again to reconfigure.

9. **Check the routing table** - See `references/mcp-routing.md` for connected MCPs and query routing logic.

10. **Skills auto-update** - When you connect an MCP, relevant skills are automatically updated with integration instructions. No manual work needed.

---

## Ten Things Not To Do

❌ **Don't paste credentials in chat without the prompt** - Wait for me to explicitly ask for your API key. Don't volunteer it unprompted.

❌ **Don't skip the tool name** - Use `/connect-mcps connect to amplitude`, not just `/connect-mcps amplitude` or `/connect-mcps connect amplitude`.

❌ **Don't connect before installing** - Install the MCP server locally first (via NPM, Docker, etc.), then run `/connect-mcps connect to [tool]`.

❌ **Don't assume immediate availability** - After connecting, I'll tell you it's ready. Don't start querying until you see the success message.

❌ **Don't hand-edit the registry** - Let me update `references/mcp-routing.md` automatically. Manual edits break the routing logic and can leave the auth type or the dialect row stale.

❌ **Don't connect duplicate MCPs** - If you already have Amplitude connected, don't run `/connect-mcps connect to amplitude` again unless you're reconfiguring.

❌ **Don't ignore errors** - If connection fails, read the error message. It usually tells you exactly what's wrong (expired key, wrong format, etc.).

❌ **Don't use both individual and batch modes together** - Pick one. Use individual for one tool, batch for multiple. Don't mix them in the same command.

❌ **Don't forget to check prerequisites** - Some MCPs require specific permissions or scopes on the API key. Check the tool's documentation.

❌ **Don't skip the fallback** - Even with MCPs connected, keep some exported data in `context-library/` as backup for offline work.
