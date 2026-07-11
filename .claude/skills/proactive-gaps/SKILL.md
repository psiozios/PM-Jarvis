---
name: proactive-gaps
description: Two-horizon product-alpha scan answering "what should I be worried about?" — present-state problems needing action now, forward inflections nobody is preparing for, and a contrarian pass on what the team over-indexes on. Surface-only, evidence-backed, run from an elevated posture but landed in the user's actual lane.
disable-model-invocation: false
user-invocable: true
---

## Quick Start

**What to provide:** Nothing required.

```
/proactive-gaps               → full two-horizon scan
```

**What you get:** A tight, ranked, evidence-backed list of present-state alpha, forward alpha, and a contrarian read on what the team over-indexes on — every item landed back in something the user can actually act on. Surface-only: nothing is created, nothing is sent.

**Time:** A few minutes to read evidence, longer if the workspace is thin and evidence has to be gathered from multiple sources.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own. Realizes Pattern 4 (Multi-Horizon "Alpha Engine" Scan) from `references/protocols/skill-patterns.md` — read that first for the mechanics this skill instantiates.

## Context Routing Logic

| Source | Location | What to Extract |
|--------|----------|------------------|
| Customer insights | `<CALL_TRANSCRIPT_SOURCE>`, `context-library/second-brain/customer-insights/`, `context-library/research/` | Unsolved problem patterns, normalized failure modes users have stopped mentioning |
| Incidents/exceptions | `context-library/decisions/`, `context-library/launches/`, error/incident logs if present | Fuzzy requirements that caused rework, repeated failure classes |
| Metrics | `<METRICS_SOURCE>` | Quant signals nobody is actively watching |
| Competitor intel | `context-library/second-brain/competitive-intelligence/`, `context-library/research/` | Competitive gaps, moves the team hasn't reacted to |
| Recent meetings | `outputs/meeting-notes/`, `context-library/meetings/` | What the team is currently spending its attention on (for the contrarian pass) |
| The product itself | codebase/product surface, if accessible | Direct evidence of unsolved problems, not just what's reported |

## Workflow

### 1. Gather the freshest evidence, in parallel

Read across all sources in the routing table. This is a surface-only skill, so breadth of evidence matters more than depth in any one source — read to resolution on each candidate signal, but don't over-invest in one channel at the expense of scanning the rest (see `references/protocols/skill-patterns.md` discipline #1).

### 2. Present-state alpha

Identify problems that need action **now**: unsolved customer-problem patterns (issues raised repeatedly that never got fixed), normalized failure modes (something broken so long it stopped being reported as broken), fuzzy requirements that are actively causing rework, competitive gaps already costing deals or users, and quant signals nobody is watching.

### 3. Forward alpha

Identify inflections **nobody is preparing for**: dated events with no prep started, a trajectory about to cross a threshold or cliff, the bet the market appears to be bending toward that the team hasn't placed yet.

### 4. Contrarian pass

Identify what the team is currently over-indexing on — using the recent-meetings evidence to see where attention is actually going — and name the tension between that and what steps 2-3 surfaced.

### 5. Run from an elevated posture, land in the user's lane

Adopt a head-of-product/CEO-level vantage point when scanning for what matters — but every single item in the output must connect back to something the user, in their actual IC role, can act on or flag. An item that only makes sense from a CEO's chair and gives the user nothing to do with it is noise, not alpha.

### 6. Rank and cap

Rank by impact. Cap the list tight — this skill's value is in forcing a small, sharp list, not an exhaustive audit.

## Output Format

```markdown
# Proactive Gaps Scan — <DATE>

## Present-State Alpha
1. **<item>** — <evidence, cited> — **Your lane:** <what the user can do with this>

## Forward Alpha
1. **<item>** — <evidence, cited> — **Your lane:** <what the user can do with this>

## Contrarian Read
<what the team is over-indexing on right now, and why that tension matters>
```

## Runs as a Routine

A natural periodic routine — see `references/protocols/routines.md` and `setup/routine-setup.md`. Weekly or biweekly cadence suits the "what should I be worried about" framing better than daily.

## Output Quality Self-Check

- [ ] Every item cites real evidence from a workspace source, not a speculative claim
- [ ] Every item states what the user, specifically, can do with it
- [ ] The list is ranked and capped, not an exhaustive dump
- [ ] The contrarian pass is grounded in actual recent-meeting evidence, not a generic observation
- [ ] Nothing was created, drafted-for-sending, or written — this skill only surfaces

## Formal Eval

**Runs automatically after every skill invocation.** See `references/protocols/skill-evals.md`. Eval agent reads `evals.md` in this directory in a clean context window.

## Cross-Skill Links

**Related:** `root-cause-analysis` (deeper dive once a present-state item is picked), `pre-mortem` (forward-alpha items may warrant a formal pre-mortem), `competitor-analysis` (feeds competitive-gap evidence)

## When to Use

- Periodically, as a forcing function to surface what isn't showing up in the normal status-reporting cadence

## When NOT to Use

- As a replacement for `root-cause-analysis` on a known, specific problem — this skill is for surfacing what isn't yet on anyone's radar

## Common Mistakes

- Surfacing an item with no evidence behind it
- Framing an item purely from an elevated vantage point with nothing the user can actually do
- Producing an exhaustive list instead of a tight, ranked one
