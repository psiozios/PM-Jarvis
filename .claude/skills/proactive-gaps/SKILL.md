---
name: proactive-gaps
description: Two-horizon product-alpha scan answering "where is the upside?" — present and forward opportunities to make more money, move more volume, or build advantage a competitor cannot copy, plus a contrarian pass on what the team over-indexes on. Every item sized; defects qualify only with a number attached. Surface-only, evidence-backed, landed in the user's lane.
user-invocable: true
disable-model-invocation: false
---

## Quick Start

**What to provide:** Nothing required.

```
/proactive-gaps               → full two-horizon scan
```

**What you get:** A tight, ranked, sized list of present-state and forward upside, at most one constraint item, and a contrarian read on what the team over-indexes on — every item landed back in something the user can actually act on. Surface-only: nothing is created, nothing is sent.

**Time:** A few minutes to read evidence, longer if the workspace is thin and evidence has to be gathered from multiple sources.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own. Realizes Pattern 4 (Multi-Horizon "Alpha Engine" Scan) from `references/protocols/skill-patterns.md` — read that first for the mechanics this skill instantiates.

**The upside gate — every candidate passes it or does not ship.** If the reader acts on this item, does the business **make more money, move more volume, or gain advantage a competitor cannot copy?** One of the three, named explicitly. An item that only prevents something from getting worse has not passed.

**A defect qualifies only once a number attaches.** Broken things are not alpha by default. A bug, a regression, a piece of debt, a normalized failure mode enters this scan only when a revenue or volume figure is attached to it — what it is costing, or what fixing it would release. Without the number it is a ticket, and it belongs in the tracker rather than here.

**Three upside items minimum, one constraint item maximum.** The floor and the cap are both hard. A run that produces four constraints and one opportunity has drifted back into being a defect list, which is the failure this gate exists to stop.

**Size everything or cut it.** Every item carries a magnitude — revenue, volume, or share, with its derivation shown and graded to its evidence. An item nobody can size is an item nobody can rank, and it does not ship.

**Nothing qualifying is a fact about the run, not about the business.** If fewer than three items clear the gate, say so plainly and name what the scan could not reach — thin sources, no metrics access, a window with nothing in it. Never pad the list with constraints to fill the space, and never conclude the business has no upside because one scan did not find it.

## Context Routing

| Source | Location | What to Extract |
|--------|----------|------------------|
| Customer insights | `<CALL_TRANSCRIPT_SOURCE>`, `context-library/second-brain/customer-insights/`, `context-library/research/` | Willingness to pay, jobs users are hiring something else for, what they asked to buy and could not |
| Incidents/exceptions | `context-library/decisions/`, `context-library/launches/`, error/incident logs if present | Repeated failure classes **with a cost attached** — the number is what makes them eligible |
| Metrics | `<METRICS_SOURCE>` | Volume the business is leaving on the table; segments converting far above or below the mean |
| Competitor intel | `context-library/second-brain/competitive-intelligence/`, `context-library/research/` | Positions a competitor structurally cannot take, and what it would take to hold one |
| Recent meetings | `outputs/meeting-notes/`, `context-library/meetings/` | What the team is currently spending its attention on (for the contrarian pass) |
| The product itself | codebase/product surface, if accessible | Direct evidence of unsolved problems, not just what's reported |


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected.

## Workflow

### 1. Gather the freshest evidence, in parallel

Read across all sources in the routing table. This is a surface-only skill, so breadth of evidence matters more than depth in any one source — read to resolution on each candidate signal, but don't over-invest in one channel at the expense of scanning the rest (see `references/protocols/skill-patterns.md` discipline #1).

### 2. Present-state upside

Find money and volume available **now**: demand the product is turning away, a segment converting far above the mean that nobody has tried to grow, a job customers are hiring a competitor or a spreadsheet to do, pricing left on the table, a position the team already half-holds and could lock. Run the upside gate on each one before it goes further.

### 3. Forward upside

Find advantage available **next**: a dated event the team could be first to, a trajectory about to cross a threshold in the business's favour, a bet the market is bending toward that is still cheap to place, a capability that would compound into something a competitor cannot copy.

### 4. The single constraint slot

At most **one** item, and only if it outranks a real opportunity on size. It must carry a revenue or volume number — what the constraint is costing, or what removing it would release. No number, no slot; the item goes to the tracker instead. Leaving this slot empty is a valid and common outcome.

### 5. Contrarian pass

Identify what the team is currently over-indexing on — using the recent-meetings evidence to see where attention is actually going — and name the tension between that and what steps 2-4 surfaced.

### 6. Run from an elevated posture, land in the user's lane

Adopt a head-of-product/CEO-level vantage point when scanning for what matters — but every single item in the output must connect back to something the user, in their actual IC role, can act on or flag. An item that only makes sense from a CEO's chair and gives the user nothing to do with it is noise, not alpha.

### 7. Size, then rank by size × claimability

Size every surviving item — revenue, volume, or share — showing the derivation and grading it to its evidence per the absolute rules. Anything that cannot be sized is cut here, not carried.

Then rank by **size × claimability**, not size alone. Claimability is the honest odds this team, with what it has, actually captures the thing: a $2M opportunity the team is structurally unable to claim ranks below a $300k one it can take this quarter. State both factors per item so the reader can disagree with either.

Check the floor and the cap before shipping: three upside items minimum, one constraint maximum. If the floor is not met, report that as a finding about the run.

## Output Template

```markdown
# Proactive Gaps Scan — <DATE>

## Present-State Upside
1. **<item>** — **Gate:** money / volume / uncopyable advantage — **Size:** <figure, derivation, evidence grade> — **Claimability:** <honest odds this team takes it, and why> — <evidence, cited> — **Your lane:** <what the user can do with this>

## Forward Upside
1. **<item>** — **Gate:** money / volume / uncopyable advantage — **Size:** <figure, derivation, evidence grade> — **Claimability:** <...> — <evidence, cited> — **Your lane:** <...>

## Constraint (max 1, omit if none qualified)
1. **<item>** — **Cost or release:** <revenue or volume figure> — <evidence, cited> — **Your lane:** <...>

## Contrarian Read
<what the team is over-indexing on right now, and why that tension matters>

## Run Quality
<Only if fewer than three upside items cleared the gate: what the scan could not reach, and what would let the next run reach it. This is a statement about the run, not about the business.>
```

## Runs as a Routine

A natural periodic routine — see `references/protocols/routines.md` and `setup/routine-setup.md`. Weekly or biweekly cadence suits the "where is the upside" framing better than daily — opportunities of this size do not appear overnight.

## Output Quality Self-Check

- [ ] Every item names which gate it passed: more money, more volume, or advantage a competitor cannot copy
- [ ] Every item carries a size with its derivation shown and graded to evidence — nothing unsized shipped
- [ ] Three upside items minimum; at most one constraint item, and it carries a revenue or volume number
- [ ] Ranked by size × claimability, with both factors stated per item
- [ ] Every item cites real evidence from a workspace source, not a speculative claim
- [ ] Every item states what the user, specifically, can do with it
- [ ] The contrarian pass is grounded in actual recent-meeting evidence, not a generic observation
- [ ] If the floor was missed, the Run Quality section says what the scan could not reach
- [ ] Nothing was created, drafted-for-sending, or written — this skill only surfaces

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it three things: the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/root-cause-analysis` -> when a present-state item is picked up and needs diagnosing
- `/pre-mortem` -> when a forward inflection warrants a formal failure-mode pass
- `/competitor-analysis` -> when the gap evidence is competitive and needs depth
- `/loose-threads` -> when a flagged gap is actually a dropped conversation, not a product problem
- `/decision-doc` -> when the contrarian pass changes a standing assumption

## When to Use

- Periodically, as a forcing function to surface what isn't showing up in the normal status-reporting cadence

## When NOT to Use

- As a replacement for `root-cause-analysis` on a known, specific problem — this skill is for surfacing what isn't yet on anyone's radar

## Common Mistakes

- **Returning a defect list.** The most common drift: broken things are easy to find and feel like insight. A defect without a number attached is a ticket, not alpha
- **Padding with constraints** to reach three items when the upside search came up short
- Shipping an item nobody sized, or ranking by size while ignoring whether this team can claim it
- Surfacing an item with no evidence behind it
- Framing an item purely from an elevated vantage point with nothing the user can actually do
- Concluding the business has no upside when what actually happened is that one run found none
