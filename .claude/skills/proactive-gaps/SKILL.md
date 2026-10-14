---
name: proactive-gaps
description: Outside-in upside scan. Every item is a hypothesis — a problem quoted from another institution's primary text, joined to an asset the org already owns, with a test and a falsifier. Reads the forward landscape first, opens on a leadership framing delta, kills what you already see. Surface-only. Book findings: /warehouse-brief.
user-invocable: true
disable-model-invocation: false
---

## Quick Start

**What to provide:** Nothing required.

```
/proactive-gaps               → full outside-in scan
```

**What you get:** A framing delta, then a ranked list of hypotheses, each written as numbered facts, logic, falsifiers, and next steps in your lane, plus a contrarian read and a Cut list that names what was dropped as already known to you. Surface-only: nothing is created, nothing is sent. Takes a few minutes, longer where the primary texts have to be found outside the workspace.

---

## Binding Rules

Defers to `config/house-style.md` for voice and word choice. This skill carries no house voice rules of its own. Realizes Pattern 4 (Outside-In Hypothesis Scan) from `references/protocols/skill-patterns.md` — read that first for the mechanics this skill instantiates.

**The upside gate — every candidate passes it or does not ship.** If the reader acts on this item, does the business **make more money, move more volume, or gain advantage a competitor cannot copy?** One of the three, named explicitly. An item that only prevents something from getting worse has not passed.

**Cutting candidates binds `references/protocols/evidence-ledger.md`** — read it before the first lookup. Every candidate gets a row; everything that misses the bar is a reported cut. Two deliberate divergences from that protocol's defaults — cut rather than `UNPROVEN`, and a floor that is a run check rather than a quota — are set out with their reasons in `references/hypothesis-bar.md`.

**Every item is a hypothesis with three parts, or it is cut.** Read `references/hypothesis-bar.md` before scoring any candidate — it carries the bar, the ranking rule, and the output shape.

- **A problem quoted from another institution's primary text** — a regulator's notice, a filing, an earnings call, a partner's published roadmap, an RFP, a competitor's changelog — verbatim, dated, linked. A press summary or an analyst's take is secondary text and does not qualify on its own.
- **Joined to an asset the org already owns** — a dataset, a licence, an integration, a customer segment, a capability — named specifically enough that someone could check it exists.
- **A named test and a falsifier.**

**A dated window is still a hypothesis.** Where the primary text dates the window (an effective date, a deadline, a sunset), the item adds that date and one named dependency, and still owes all three parts.

**Book findings are not this skill's.** Money and volume computed from the org's own data belong to `/warehouse-brief`; a candidate like that is cut here with "inside-out" as its reason. So is a defect: it has no primary text behind it, and it belongs in the tracker.

**Kill what the user already sees.** Before an item ships, check it against what the user already sees (Pattern 4). A match is a `KILL` row naming where they see it.

**Three hypotheses minimum, as a run check.** A short list plus a Run Quality line beats padding. Nothing qualifying is a fact about the run, not about the business: say what the scan could not reach — no primary texts in reach, no dated filings, no visibility into the partnership pipeline — and never conclude the business has no upside because one scan did not find it.

## Context Routing

| Source | Location | What to Extract |
|--------|----------|------------------|
| Primary texts | web search, regulators' and licensing registers, filings and earnings transcripts, partners' published roadmaps, RFPs, competitors' changelogs and job postings | Problems other institutions have written down, quoted verbatim with date and link |
| Owned assets | `context-library/business-info-template.md`, `context-library/second-brain/product-knowledge/`, the product surface or codebase if accessible | What the org already has that a quoted problem needs |
| What the user already sees | the latest `outputs/weekly-plans/`, `context-library/strategy/` OKRs, `<TASK_TRACKER>`, recent meeting notes, the last two `outputs/briefs/proactive-gaps-*.md` and `outputs/briefs/warehouse-brief-*.md`, `outputs/state/rulings-proactive-gaps.md` | The kill list |
| Competitor intel | `context-library/second-brain/competitive-intelligence/`, `context-library/research/` | Positions a competitor structurally cannot take |
| Recent meetings | `outputs/meeting-notes/`, `context-library/meetings/` | What the team is currently spending its attention on (for the contrarian pass) |
| Leadership, internal | `context-library/strategy/`, `context-library/meetings/`, all-hands and exec notes | Dated quotes on where growth is expected to come from |
| Leadership, external | `<DOCS_HUB>`, the company's public site, press, filings, web search | Dated public statements on the same question — the other half of the framing delta |

For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected. A source that is connected but fails — an expired credential, a revoked scope, an OAuth refresh with no browser — is reported unavailable by name with its reason and never listed among the sources swept (`references/protocols/source-preflight.md`).

## Workflow

**The order is the method.** Framing delta, then the dated primary texts, then the rest. Undated reads first fill the list before anyone looks for a window that is about to close.

### 1. Leadership framing delta

Before any candidate exists, put what leadership says **internally** beside what the company says **externally**, each on a dated quote from a real source. Where the two diverge is the most useful signal in the run: a bet named in an all-hands but absent from the public story is a direction the team is already moving on quietly, and a public claim with no internal work behind it is a commitment someone will have to meet.

Run this first because it tells you where to point the forward read. "No delta found" is a real result — say which two sources you compared and their dates, so the reader can see it was actually checked (`references/protocols/freshness-provenance.md`: a quote carries its date, and a strategy doc is directional rather than a status oracle).

### 2. Forward landscape: dated primary texts

Find problems other institutions have dated: a licence or approval opening a market, a partner's roadmap changing who can be sold to, a competitor's sunset, a platform opening, a regulation landing. Quote the text, date it, link it. Sweep the launches of whoever already holds the gating capability, not only the names you watch (`references/protocols/freshness-provenance.md` rule 4).

### 3. The rest of the primary texts

Undated problems other institutions have written down: what a buyer's own filing says it must fix, what a competitor's hiring says it cannot do, what an RFP keeps asking for. Same bar: verbatim, dated, linked.

### 4. Join each to an owned asset, then name the test

For each quoted problem, name the asset the org already owns that answers it, specifically enough to check. No owned asset, cut it: "no owned asset". Then the cheapest test that would move confidence, and the falsifier that would drop it.

### 5. Kill what the user already sees

Check every surviving item against the kill-list sources above. A match is a `KILL` row naming where the user sees it: "already in this week's plan", "OKR KR2", "the 3 Oct leadership sync".

### 6. Contrarian pass

Name what the team is over-indexing on — from the recent-meetings evidence, not from impression — and the tension between that and what steps 2-4 surfaced. The framing delta usually sharpens this: attention going somewhere neither the internal nor the external story justifies is the finding.

### 7. Rank, then check the composition

Rank on window × claimability: how soon the primary text's date closes (or "undated"), against how directly the owned asset answers the quoted problem. State both factors per item. Then check the floor of three, and that the Cut list carries every miss with the bar it missed — a cut list with nothing in it means the bar was not applied.

### 8. Write each item in four parts, from an elevated posture landed in the user's lane

Numbered facts (each quoted and sourced), the logic from those facts to the hypothesis, the falsifiers, and next steps the user, in their actual IC role, can take. Adopt a head-of-product/CEO-level vantage point when scanning, but an item that only makes sense from a CEO's chair and gives the user nothing to do is noise, not alpha. Save the scan to `outputs/briefs/proactive-gaps-<DATE>.md`.

## Output Template

Template, the bar, the ranking rule, and the two deliberate divergences from the evidence ledger: `references/hypothesis-bar.md` — read before scoring the first candidate.

## Runs as a Routine

A periodic routine fits — `references/protocols/routines.md`, `setup/routine-setup.md`. Weekly or biweekly beats daily; opportunities this size do not appear overnight.

## Output Quality Self-Check

- [ ] The framing delta ran **first** on dated quotes from both sides, and dated primary texts were read before undated ones — or the output names which two sources were compared and found no delta
- [ ] Every item names which gate it passed: more money, more volume, or advantage a competitor cannot copy
- [ ] Every item has all three parts: a verbatim, dated, linked primary-text problem; a named owned asset; a test and a falsifier
- [ ] No item is a book finding or a defect — those are cut with their reason
- [ ] Every item was checked against what the user already sees, and the matches are `KILL` rows naming where
- [ ] Every item is written as numbered facts, logic, falsifiers, and next steps in the user's lane
- [ ] Ranked with both factors stated per item — window × claimability
- [ ] The contrarian pass is grounded in actual recent-meeting evidence, not a generic observation
- [ ] The Cut list carries every item that missed the bar, with the bar it missed
- [ ] Nothing was created, drafted-for-sending, or written beyond the scan and its ledger

## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it the output (or its absolute path), this skill's `evals.md`, `config/house-style.md`, and the sources the output cites — E7 cannot be scored without them, and scoring it from plausibility is a vacuous PASS. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/warehouse-brief` -> when a candidate's evidence is the org's own data rather than another institution's text
- `/pre-mortem` -> when a dated window warrants a formal failure-mode pass
- `/competitor-analysis` -> when the primary text is a competitor's and needs depth
- `/loose-threads` -> when a flagged gap is actually a dropped conversation, not a product problem
- `/decision-doc` -> when the contrarian pass changes a standing assumption

## When to Use

- Periodically, as a forcing function to surface what isn't showing up in the normal status-reporting cadence

## When NOT to Use

- As a replacement for `root-cause-analysis` on a known, specific problem — this skill is for surfacing what isn't yet on anyone's radar
- For money and volume in the business you already have — that is `/warehouse-brief`

## Common Mistakes

- **Paraphrasing the primary text.** A hypothesis rests on the institution's own words; a summary of them is a second-hand claim
- **No owned asset in the join.** A real problem the org has nothing to answer with is someone else's opportunity
- **Shipping what the user already sees.** One run had three of four items dismissed as known
- **Returning a defect list or a back-book review.** Broken things and the org's own numbers feel like insight; neither is an outside-in hypothesis
- Ranking on one factor, or ignoring whether this team can claim it
- Framing an item purely from an elevated vantage point with nothing the user can actually do
- Concluding the business has no upside when what actually happened is that one run found none
