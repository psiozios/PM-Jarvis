---
name: proactive-gaps
description: Product-alpha scan answering "where is the upside?" — reads the forward landscape first, then the money, then the outside-in reads, each held to its own bar: a figure for book items, a date and a dependency for forward ones, a test and a falsifier for a hypothesis. Opens on a leadership framing delta. Surface-only, landed in the user's lane.
user-invocable: true
disable-model-invocation: false
---

## Quick Start

**What to provide:** Nothing required.

```
/proactive-gaps               → full two-horizon scan
```

**What you get:** A framing delta, then a ranked list across three classes — forward, book, and outside-in — at most one constraint, and a contrarian read, every item landed in something the user can act on. Surface-only: nothing is created, nothing is sent. Takes a few minutes, longer where the forward evidence has to be gathered from outside the workspace.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own. Realizes Pattern 4 (Multi-Horizon "Alpha Engine" Scan) from `references/protocols/skill-patterns.md` — read that first for the mechanics this skill instantiates.

**The upside gate — every candidate passes it or does not ship.** If the reader acts on this item, does the business **make more money, move more volume, or gain advantage a competitor cannot copy?** One of the three, named explicitly. An item that only prevents something from getting worse has not passed.

**Each class is held to its own bar. One bar for everything deletes a class.** Read `references/item-classes.md` before scoring any candidate — it carries the three classes, their bars, the ranking rule, and the output shape.

- **Book** — money and volume in the business you already have. **Bar: a money or volume figure**, derivation shown, graded to evidence.
- **Forward** — growth gated on a licence, a partnership, a market-structure shift, a dated event. **Bar: a date and a dependency**, both from a real source. A forward item is **not** required to carry a figure.
- **Outside-in hypothesis** — a read on the market the workspace has no data for. **Bar: a named test and a falsifier.**

**Size-or-cut applies to the book class only.** Holding a forward item to a transaction-backed figure is how this scan becomes a back-book review: where growth is gated on licensing, partnerships, or market structure, there is no transaction history behind it yet, so a money-first bar deletes the entire class before it reaches the page.

**A defect qualifies only once a number attaches.** Broken things are not alpha by default. A bug, a regression, a piece of debt, a normalized failure mode enters this scan only when a revenue or volume figure is attached to it — what it is costing, or what fixing it would release. Without the number it is a ticket, and it belongs in the tracker rather than here.

**Three upside items minimum, at least one of them forward, one constraint item maximum.** The floor, the forward rule, and the cap are all hard. A run that produces four constraints and one opportunity has drifted back into being a defect list; a run that produces three book items and nothing forward has read the money first and stopped.

**Nothing qualifying is a fact about the run, not about the business.** If a bar goes unmet, say so plainly and name what the scan could not reach — thin sources, no metrics access, no dated filings, no visibility into the partnership pipeline. Never pad with constraints to fill the space, and never conclude the business has no upside because one scan did not find it.

## Context Routing

| Source | Location | What to Extract |
|--------|----------|------------------|
| Customer insights | `<CALL_TRANSCRIPT_SOURCE>`, `context-library/second-brain/customer-insights/`, `context-library/research/` | Willingness to pay, jobs users are hiring something else for, what they asked to buy and could not |
| Incidents/exceptions | `context-library/decisions/`, `context-library/launches/`, error/incident logs if present | Repeated failure classes **with a cost attached** — the number is what makes them eligible |
| Metrics | `<METRICS_SOURCE>` | Volume the business is leaving on the table; segments converting far above or below the mean |
| Competitor intel | `context-library/second-brain/competitive-intelligence/`, `context-library/research/` | Positions a competitor structurally cannot take, and what it would take to hold one |
| Recent meetings | `outputs/meeting-notes/`, `context-library/meetings/` | What the team is currently spending its attention on (for the contrarian pass) |
| The product itself | codebase/product surface, if accessible | Direct evidence of unsolved problems, not just what's reported |
| Leadership, internal | `context-library/strategy/`, `context-library/meetings/`, all-hands and exec notes | Dated quotes on where growth is expected to come from |
| Leadership, external | `<DOCS_HUB>`, the company's public site, press, filings, web search | Dated public statements on the same question — the other half of the framing delta |
| Forward landscape | web search, regulatory and licensing sources, partnership and channel announcements, competitor filings and job postings | Dated events, licences, approvals, market-structure shifts — the evidence the forward class runs on |


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected. A source that is connected but fails — an expired credential, a revoked scope, an OAuth refresh with no browser — is reported unavailable by name with its reason and never listed among the sources swept (`references/protocols/source-preflight.md`).

## Workflow

**The order is the method.** Reading the money first ends the scan before the forward class is written down: three sized book items arrive, the floor is met, nobody looks further. Forward first, money second, narrative last.

### 1. Leadership framing delta

Before any candidate exists, put what leadership says **internally** beside what the company says **externally**, each on a dated quote from a real source. Where the two diverge is the most useful signal in the run: a bet named in an all-hands but absent from the public story is a direction the team is already moving on quietly, and a public claim with no internal work behind it is a commitment someone will have to meet.

Run this first because it tells you where to point the forward read. "No delta found" is a real result — say which two sources you compared and their dates, so the reader can see it was actually checked (`references/protocols/freshness-provenance.md`: a quote carries its date, and a strategy doc is directional rather than a status oracle).

### 2. Forward landscape

Find growth gated on something not yet in the book: a licence or approval opening a market, a partnership or channel changing who can be sold to, a competitor exiting, a platform opening, a regulation landing, a dated event the team could be first to. Hold each to the forward bar — a real date from a real source, and one named dependency someone could go and check.

### 3. Book upside

Now the money and volume available in the business you already have: demand being turned away, a segment converting far above the mean that nobody has grown, a job customers pay someone else to do, pricing left on the table. Every one carries a figure with its derivation and evidence grade, or it is cut.

### 4. Outside-in hypotheses

The narrative reads the workspace holds no data for — where demand is moving, what a competitor's hiring implies. Each carries a named test and a falsifier, and is graded visibly as a hypothesis.

### 5. The single constraint slot

At most **one**, and only if it outranks a real opportunity once both are ranked in step 7. It carries a revenue or volume number — what it costs, or what removing it releases. No number, no slot. Leaving this empty is valid and common.

### 6. Contrarian pass

Name what the team is over-indexing on — from the recent-meetings evidence, not from impression — and the tension between that and what steps 2-4 surfaced. The framing delta usually sharpens this: attention going somewhere neither the internal nor the external story justifies is the finding.

### 7. Rank, then check the composition

Rank by size × claimability where both exist. Where a forward item carries no figure, rank it on how soon its window closes against claimability. State both factors per item either way.

Then check: three upside items minimum, **at least one of them forward**, one constraint maximum. Everything that failed its class bar goes to the Cut list with the bar it missed — a cut list with nothing in it means the bars were not applied. If no forward item survived, that goes in Run Quality as a finding about the run.

### 8. Run from an elevated posture, land in the user's lane

Adopt a head-of-product/CEO-level vantage point when scanning — but every item must connect back to something the user, in their actual IC role, can act on or flag. An item that only makes sense from a CEO's chair and gives the user nothing to do with it is noise, not alpha.

## Output

Template, the three class bars, the ranking rule, and the composition check: `references/item-classes.md` — read before scoring the first candidate, not when the list is being written.

## Runs as a Routine

A natural periodic routine — see `references/protocols/routines.md` and `setup/routine-setup.md`. Weekly or biweekly suits "where is the upside" better than daily; opportunities this size do not appear overnight.

## Output Quality Self-Check

- [ ] The framing delta ran **first** on dated quotes from both sides, and the forward landscape was read **before** the money — or the output names which two sources were compared and found no delta
- [ ] Every item names which gate it passed: more money, more volume, or advantage a competitor cannot copy
- [ ] Each item was held to **its own class bar** — figure for book, date and dependency for forward, test and falsifier for outside-in
- [ ] At least one forward item survived, or Run Quality says what the forward read could not reach
- [ ] Three upside items minimum; at most one constraint item, and it carries a revenue or volume number
- [ ] Ranked with both factors stated per item — size × claimability, or window × claimability for an unsized forward item
- [ ] Every item cites real evidence, and every outside-in item is graded visibly as a hypothesis
- [ ] Every item states what the user, specifically, can do with it
- [ ] The contrarian pass is grounded in actual recent-meeting evidence, not a generic observation
- [ ] The Cut list carries every item that missed a bar, with the bar it missed
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

- **Returning a back-book review.** Reading the money first, meeting the floor on three sized book items, and never reaching the forward class. Where growth is gated on licensing, partnerships, or market structure, this answers the wrong question competently
- **Holding a forward item to a money bar** it could not possibly clear, then cutting it for being unsized
- **Returning a defect list.** The other common drift: broken things are easy to find and feel like insight. A defect without a number attached is a ticket, not alpha
- **Padding with constraints** to reach three items when the upside search came up short
- Shipping an item nobody sized, or ranking by size while ignoring whether this team can claim it
- Surfacing an item with no evidence behind it
- Framing an item purely from an elevated vantage point with nothing the user can actually do
- Concluding the business has no upside when what actually happened is that one run found none
