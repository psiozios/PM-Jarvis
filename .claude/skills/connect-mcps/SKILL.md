---
name: connect-mcps
description: Set up a live tool connection (analytics, issue tracker, docs hub, chat) so skills pull real data instead of asking you for it — finds the server, walks you through credentials, tests it, probes its search dialect, and registers a preflight check. Modifies your workspace, editing skill files and the mcp-routing registry as part of setup.
user-invocable: true
disable-model-invocation: false
---

Connect an MCP server so your skills read live data instead of asking you to paste it. Finds the server, walks you through credentials, verifies the connection with a real call, records what its search actually does, and wires it into the registry and the skills that benefit.

## Quick Start

**What to provide:** the tool's name. Or say "batch" to do several.

```
/connect-mcps connect to linear
/connect-mcps connect to amplitude
/connect-mcps batch
```

**What you get:** the MCP connected, a preflight check registered for it, its search dialect recorded, the relevant skills updated, and a log in `outputs/mcp-integration-logs/`. **This skill edits your workspace** — skill files and `references/mcp-routing.md` — so it says what it changed.

**Time:** 5-20 minutes per tool.

## Binding Rules

Defers to `config/house-style.md` for voice and word choice.

**A connection that answered once is not a connection that works.** Tests are real calls, never a status flag, and the same is true three weeks later — which is why every connected source gets a registered check rather than a one-time green tick (`references/protocols/source-preflight.md`).

**Record the auth type, and mark OAuth as OAuth.** An OAuth refresh needs a browser, so an unattended run can never repair it. That fact has to be on the registry row before a routine depends on the source.

**A tool's search dialect is a property to verify.** Probe it and date the row. Assuming a tool supports `OR` when it ANDs every term produces zero hits with no error, and that false zero reads exactly like a real one (`references/protocols/evidence-ledger.md`).

**Credentials are never printed, echoed, or written into a file this skill creates.** They go to the MCP system or an environment variable named in `setup/environment-keys.md`.

**The registry has one address:** `references/mcp-routing.md`. `CLAUDE.md` points at it and holds no table of its own.

## Context Routing

| Need | Source | Trigger |
|------|--------|---------|
| Which MCPs are already connected, and their auth types | `references/mcp-routing.md` | always, before searching for a server |
| The check contract and reason vocabulary | `references/protocols/source-preflight.md` | when registering the preflight check |
| Existing check registrations | `config/source-preflight.json` | when registering the preflight check |
| Credential setup and the OAuth class | `setup/environment-keys.md` | when a tool needs a token or an OAuth app |
| Which skills a category maps to | `references/setup-mechanics.md` | at Step 6 |
| The tool's own MCP documentation | web search | at Steps 2-3 |

## Workflow

**Priority order:** official remote MCP server → local server via NPM/Docker → manual OAuth or API token. Always check for a remote server first; it is by far the least setup.

### 1. Parse and dedupe

Extract and normalize the tool name. Check `references/mcp-routing.md` — if it is already connected, offer to re-test, re-probe the dialect, or reconfigure instead of connecting again.

### 2. Look for an official remote server

Search for "<tool> official MCP server", "<tool> remote MCP server", "<tool> MCP server documentation". If you find a hosted endpoint, the whole setup is `claude mcp add --transport http <tool> <url>`, then `/mcp` in Claude Code to authenticate.

### 3. Otherwise research manual setup

Search for the integration guide, the Claude MCP setup, and the authentication requirements. Extract the package or server command, the auth method, the required parameters, and the tool surface. Details of what to extract: `references/setup-mechanics.md`.

### 4. Guide credential entry

Present exactly what is needed and where to get it, then prompt for each value. The MCP system handles the values; this skill never stores or echoes them.

### 5. Verify, probe, register

Three things, in order, and none of them is optional:

1. **Test with a real call** — one record, one page. A status flag is not proof.
2. **Probe the search dialect** — the four probes in `references/mcp-routing.md`, and fill in that tool's row with today's date. Probe 3 is the one that matters: if two terms where only one matches returns zero, the tool ANDs, and every multi-term query sent to it from now on is a false zero waiting to be read as a real one.
3. **Register a preflight check** in `config/source-preflight.json`, keyed on the placeholder the skills route on (`<TASK_TRACKER>`, `<CALENDAR>`, and so on), with the auth type recorded. See `references/protocols/source-preflight.md`.

### 6. Map to skills

Determine the tool's category and which skills benefit. The category-to-skill map is in `references/setup-mechanics.md`.

### 7. Update the skills and the registry

Add the integration block to each mapped skill, and update `references/mcp-routing.md`: the Connected MCPs row including auth type, the Search Dialects row from Step 5, and the routing rules. Block format and registry format: `references/setup-mechanics.md`.

### 8. Log it

Save to `outputs/mcp-integration-logs/<timestamp>-<tool>.md`, then show what changed: tools discovered, skills updated, the dialect finding, and how to phrase a query that routes here.

## Output Quality Self-Check

- [ ] **Remote server checked first** — manual setup only after confirming none exists
- [ ] **Connection tested with a real call** — a query returned actual results, not a "connected" status
- [ ] **Auth type recorded** — `oauth` / `token` / `none` on the registry row, and OAuth flagged as unrepairable by an unattended run
- [ ] **Search dialect probed and dated** — the four probes run, that tool's row filled in
- [ ] **Preflight check registered and enabled** — it makes a real call and reports `live`
- [ ] **Registry updated in `references/mcp-routing.md`** — never in `CLAUDE.md`, which holds no table
- [ ] **Skills updated** — every mapped skill has its integration block and a stated fallback
- [ ] **No credential printed, echoed, or written to a file**
- [ ] **Tools discovered and documented** — the available MCP tools listed with what each does
- [ ] **Category correctly assigned**, and no duplicate entry in the registry or a skill file
- [ ] **Integration log saved** to `outputs/mcp-integration-logs/`
- [ ] **Changes reported** — this skill edits the workspace, so it says what it touched
- [ ] **The user can actually use it** — example natural-language queries given, so they can start now

If any check fails, fix it before declaring success. A half-connected MCP causes more confusion than no MCP, because skills try to use it.

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it the output (or its absolute path), this skill's `evals.md`, `config/house-style.md`, and the sources the output cites — E7 cannot be scored without them. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

<!-- No Cross-Skill Links: this is a setup utility, not a workflow step. Every
     skill degrades gracefully without MCPs, and any static list of which skills
     benefit from which connector would be stale within a week — the live answer
     is the Used In column in references/mcp-routing.md. -->

## When to Use

- Setting up the workspace, or adding a tool you have started using
- Re-testing or reconfiguring a connection that has stopped answering

## When NOT to Use

- To diagnose a source that failed mid-run — that is `references/protocols/source-preflight.md` and the session-start hook
- To pick which tools are worth having — read `references/tool-catalog.md` first and decide, then come back

## Common Mistakes

- Treating a "connected" status as a working connection, or a set environment variable as a valid credential
- Skipping the dialect probe, then reading an AND-only tool's false zero as a real null
- Recording no auth type, so a routine later depends on an OAuth source that cannot re-auth unattended
- Writing the registry table into `CLAUDE.md`, leaving two registries to disagree
- Connecting every tool at once instead of the two or three that unblock real work

## Reference

- `references/tool-catalog.md` — which tools are worth connecting, by tier. Read when the user asks what to connect.
- `references/setup-mechanics.md` — doc extraction, category-to-skill map, skill block format, registry format. Read at Steps 3, 6, 7.
- `references/worked-examples.md` — full connections end to end, and how queries route afterward. Read when you want to see one.
- `references/troubleshooting.md` — failed tests, bad credentials, routing problems, disconnecting. Read when something breaks.
