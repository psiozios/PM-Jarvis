# Item Classes, Their Bars, and the Output Shape

Bulk reference for `/proactive-gaps`. Read before scoring any candidate — the bar depends on which class the item is in, and picking the wrong class is how an item gets held to evidence it could never have.

## Why one bar was wrong

The previous version ran one gate over everything: size it or cut it, with the magnitude graded to evidence. That works where growth comes out of the existing book, because the book has transaction data behind it. It deletes the whole forward class wherever growth is gated on licensing, partnerships, or market structure — none of which has transaction history, by definition, because it has not happened yet.

The result was a back-book review with a strategic preamble. Every surviving item described the business the team already has, because that was the only kind of item that could produce a number graded above `[unsourced]`.

**Three classes, three bars.** An item is held to the bar for what it actually is.

## The three classes

### Book — money and volume in the business you already have

Demand being turned away, a segment converting far above the mean that nobody has grown, a job customers are paying someone else to do, pricing left on the table.

**Bar: a money or volume figure**, derivation shown, graded to its evidence per `references/absolute-rules.md`. This is the class where a number is available, so a number is required. No figure, no item.

### Forward — growth gated on something not yet in the book

A licence or approval that opens a market. A partnership or channel that changes who can be sold to. A market-structure shift — a competitor exiting, a platform opening, a regulation landing. A dated event the team could be first to.

**Bar: a date and a dependency.** The date is when the window opens or closes, and it has to be a real date from a real source — a filing, an effective date, a published roadmap, a contract term — not "next year". The dependency is the single thing that has to be true for the team to take it, named specifically enough that someone could go and check: a licence, a signature, a build, a hire.

**A forward item is not required to carry a money figure**, and demanding one is how the class gets deleted. Where a plausible magnitude exists, give it and grade it honestly. Where it does not, the date and the dependency carry the item.

### Outside-in hypothesis — a read on the market the workspace has no data for

Where the demand is moving, what a competitor's hiring implies, what a buyer's own economics will force them to do.

**Bar: a named test and a falsifier.** The test is the cheapest thing that would move your confidence — five calls to a named segment, one pricing probe, a specific query against a public dataset. The falsifier is what you would have to see to drop it. A hypothesis with no falsifier is a belief, and it does not ship.

Grade these as hypotheses, visibly. An outside-in item asserting itself as fact is worse than no item.

## Three deliberate divergences from the evidence ledger

`references/protocols/evidence-ledger.md` binds this scan — every candidate gets a row, and every cut is reported with its reason. Three of its defaults are overridden here on purpose, so nobody "fixes" them later:

**Cut, not `UNPROVEN`.** The ledger's default is that an item you cannot close ships as a one-line question. Here an item that misses its class bar is **cut**, because the bar is the finding. A book item with no figure is not an unproven opportunity; it is an opportunity nobody has sized. It says exactly that in the Cut list, which is where the reader can overrule it.

**The floor is a run check, not a quota.** Three upside items minimum does not license padding. Where the bars are not met, the honest output is a short list plus a Run Quality section — the same logic as the no-floor rule in `/create-tickets`. Neither skill manufactures content to hit a number; this one reports the shortfall.

**The one-constraint cap is a gate, not a volume limit.** Elsewhere a cap that bites triggers a re-check rather than a truncation. Here a second qualifying constraint means the scan drifted into a defect list, so the second one goes to Cut naming the cap, and the tracker is where it belongs.

## Composition

**At least one forward item survives, or the run says why not.** This is a composition rule, not a quota to pad toward. A run that ends with three book items and nothing forward has almost certainly read the money first and stopped — and where the business's real growth is gated on licensing or partnerships, that run has answered the wrong question competently. If nothing forward cleared its bar, the Run Quality section names what the forward read could not reach: no dated sources, no visibility into the partnership pipeline, no public filings.

**Ranking, within and across classes.** Rank by size × claimability where both classes carry a size. Where a forward item has no figure, rank it on the date — how soon the window closes — against claimability. State both factors either way, so the reader can disagree with either.

**Anything that fails its class bar is cut to the Cut list with its reason**, never dropped silently (`references/protocols/evidence-ledger.md`). A cut list with nothing in it means the bars were not applied.

## Output Template

```markdown
# Proactive Gaps Scan — <DATE>

## Framing Delta
<what leadership says internally vs. what the company says externally, each on a dated quote, and what the gap implies about where growth is expected to come from. "No delta found" is a result; say which two sources were compared and their dates.>

## Forward Upside
1. **<item>** — **Date:** <when the window opens or closes, and the source that dates it> — **Dependency:** <the one thing that must be true, named checkably> — **Size:** <figure and grade, or "unsized — carried on date and dependency"> — **Claimability:** <...> — <evidence, cited> — **Your lane:** <...>

## Book Upside
1. **<item>** — **Size:** <figure, derivation, evidence grade> — **Claimability:** <...> — <evidence, cited> — **Your lane:** <...>

## Outside-In Hypotheses
1. **<item>** — **Test:** <the cheapest thing that would move confidence> — **Falsifier:** <what would make you drop it> — <the reasoning and what it rests on> — **Your lane:** <...>

## Constraint (max 1, omit if none qualified)
1. **<item>** — **Cost or release:** <revenue or volume figure> — <evidence, cited> — **Your lane:** <...>

## Contrarian Read
<what the team is over-indexing on right now, and why that tension matters>

## Cut
- <item> — <class it was held to, and which bar it missed>

## Run Quality
<What the scan could not reach, and what would let the next run reach it. Required whenever no forward item survived, or fewer than three upside items cleared their bars. A statement about the run, never about the business.>
```
