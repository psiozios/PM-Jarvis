# The Hypothesis Bar and the Output Shape

Bulk reference for `/proactive-gaps`. Read before scoring any candidate.

## Why one class, and why the book moved out

The scan used to carry three classes — book, forward, and outside-in — each on its own bar. The book class read the org's own numbers, and the user already watches those numbers: in one run three of four items were dismissed as already known. Inside-out findings now run in `/warehouse-brief`, which computes from the warehouse what no dashboard shows. This scan keeps what only an outside read can find: problems other institutions have written down, which the org is already equipped to answer.

An earlier version ran one money-or-cut gate over everything, and that deleted every opportunity gated on licensing, partnerships, or market structure. The lesson stands: a forward item owes no figure. It owes the hypothesis bar, plus a date and a dependency where the text dates the window.

## The bar

An item ships only with all three parts.

**1. A problem quoted from another institution's primary text.** The institution's own words, verbatim, with the date and a link: a regulator's notice or register entry, a filing, an earnings-call transcript, a partner's published roadmap or API changelog, an RFP, a standards body's draft, a competitor's changelog or job posting. A press article, an analyst note, or a summary is secondary text: it can point to the primary text, and the item quotes the primary.

**2. Joined to an asset the org already owns.** A dataset, a licence, an integration, a customer segment, a capability, a contract. Named specifically enough that someone could go and confirm it exists. "Our data" is not an asset; "twelve months of settlement records for the 40 merchants on the legacy plan" is.

**3. A named test and a falsifier.** The test is the cheapest thing that would move confidence: five calls to a named segment, one pricing probe, one query. The falsifier is what you would have to see to drop it. A hypothesis with no falsifier is a belief, and it does not ship.

**A dated window adds two fields.** Where the primary text dates it (an effective date, a deadline, a sunset), the item carries that date and the one dependency that has to be true for the team to take it: a licence, a signature, a build, a hire. It needs no money figure. Where a plausible magnitude exists, give it and grade it honestly.

Grade every item as a hypothesis, visibly. One asserting itself as fact is worse than no item.

## Two deliberate divergences from the evidence ledger

`references/protocols/evidence-ledger.md` binds this scan — every candidate gets a row, and every cut is reported with its reason. Two of its defaults are overridden here on purpose, so nobody "fixes" them later:

**Cut, not `UNPROVEN`.** The ledger's default is that an item you cannot close ships as a one-line question. Here an item that misses the bar is **cut**, because the bar is the finding. A problem with no owned asset is not an unproven opportunity; it is someone else's. It says so in the Cut list, where the reader can overrule it.

**The floor is a run check, not a quota.** Three hypotheses minimum does not license padding. Where the bar is not met, the honest output is a short list plus a Run Quality section — the same logic as the no-floor rule in `/create-tickets`.

## Ranking

Rank on **window × claimability**. Window is how soon the primary text's date closes, or "undated". Claimability is how directly the owned asset answers the quoted problem. State both factors per item, so the reader can disagree with either.

**Anything that fails the bar is cut to the Cut list with its reason**, never dropped silently. The reasons are fixed: no primary text, secondary text only, no owned asset, no falsifier, inside-out (`/warehouse-brief`'s), a defect, already seen (and where).

## Output Template

```markdown
# Proactive Gaps Scan — <DATE>

## Framing Delta
<what leadership says internally vs. what the company says externally, each on a dated quote, and what the gap implies about where growth is expected to come from. "No delta found" is a result; say which two sources were compared and their dates.>

## Hypotheses

### 1. <the hypothesis, one line> — <gate: money / volume / advantage> — Window: <date and source, or "undated"> × Claimability: <...>

**Facts**
1. "<the problem, verbatim>" — <institution>, <document>, <date>, [link](<url>)
2. <the owned asset, named so it can be checked> — <where that is recorded>
3. <any further fact, each sourced>

**Logic:** <how the facts join: why this asset answers this problem, and why now>

**Falsifiers:** <what would make you drop it> · **Test:** <the cheapest thing that would move confidence> · **Dependency:** <the one thing that must be true, where the window is dated>

**Next steps in your lane:** <what the user, in their role, can do this week>

## Contrarian Read
<what the team is over-indexing on right now, and why that tension matters>

## Cut
- <item> — <the bar it missed; for "already seen", where the user sees it>

## Run Quality
<What the scan could not reach, and what would let the next run reach it. Required whenever fewer than three hypotheses cleared the bar. A statement about the run, never about the business.>
```
