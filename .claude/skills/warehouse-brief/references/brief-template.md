# Brief Template

Bulk reference for `/warehouse-brief`. Read before writing the first insight.

## The four-part insight

Every insight is written the same way, so the reader can check it in the order they would argue with it.

1. **Facts, numbered.** Each one is a figure quoted from a query result, with the query's appendix ID. The reconciling figure is its own fact, with its own query.
2. **Logic.** How the facts lead to a change in the decision. One short paragraph, no new facts.
3. **Falsifiers.** What result, from what query or what person, would make the insight wrong. At least one per insight.
4. **Next steps in your lane.** What the user, in their role, can do with it this week: take it to the decision's owner, add it to a meeting's agenda, ask for a test. Never "the team should".

## Output Template

````markdown
# Warehouse Brief — <DATE>

**Swept:** <the sources that answered> · **Map read:** `context-library/metrics/warehouse-map.md`, last updated <its date>
**Unavailable:** <source — state, reason, and what repairs it; "none" when every source answered>

## 1. <the insight, one line> — moves: <decision> (owner: <name>, <where it lives>)
**Kind:** join / cohort split / unrun trend · **Ranked on:** <how far it moves the decision> × <when it is decided>

**Facts**
1. <figure> — Q1
2. <figure> — Q2
3. <the same headline figure by an independent path> — Q3 (within <tolerance> of fact 1)

**Logic:** <how the facts change the decision>

**Falsifiers:** <what would make this wrong>

**Next steps in your lane:** <what you can do this week>

## 2. ...

## Cut
- <candidate> — <already seen: where> / <changes no live decision> / <did not reconcile: both figures> / <a lookup, not a computation> / <over cap: rank N>

## Run Quality
<Required when fewer than three shipped: what blocked the rest. A statement about the run, never about the business.>

## Appendix: Queries
### Q1 — <what it computes>
```sql
<the SQL, verbatim as run>
```
Rows returned: <from the result> · Ran: <timestamp from the command>
````
