# Tracker Writes

**Principle: THE SCALE IS FROZEN, THE TRACKER COMPUTES THE SCORE, AND THE CHAT GETS A TABLE — NEVER THE BODY.**

This protocol governs any skill that scores items or writes them into a tracker. It answers three questions that keep getting answered differently: what a number on an item means, which system owns it, and what the conversation shows.

## 1. Freeze the scales

**A score earns its keep only if it compares across the whole backlog.** A scale anchored to the items in front of you right now produces a number that means something different every sitting: a 4 in a thin week and a 4 in a heavy one are not the same 4, and ranking the two beside each other is arithmetic on nothing.

So every level of every factor is defined against a **fixed, external anchor** — a count, a currency figure, a named condition that is true or false independent of the batch. "Five or more distinct accounts asked" is an anchor. "Top 10% of what came in" is not; it moves when the denominator does.

Write the anchors down beside the scale. Changing one re-scores everything already scored, so a changed anchor is a migration with a re-score attached, not an edit.

## 2. The tracker computes; you supply the factors

Write each factor into **its own field** in the tracker, and let the tracker's own formula or rollup produce the score.

**Never write a computed field by hand.** A typed score goes stale the instant any factor changes, and it goes stale silently. Nobody can see which factor moved, because the number carries no derivation. And it starts disagreeing with the formula the moment somebody edits a factor in the UI — at which point the tracker shows two numbers that both claim to be the score.

If the tracker has no formula field, **the score does not go into the tracker at all.** It lives in the approval table in the chat (§7) and nowhere else. A field that looks computed but was typed is worse than no field, because people trust it.

## 3. Score at creation

**Nothing is born unscored.** An unscored item is missing from every ranked view, which makes it invisible to the exact process that would have surfaced it. Scoring at creation costs the seconds the factors take. A later scoring pass is a second backlog, and it does not happen.

## 4. Empty is neutral — and say so in the field

State what an unset factor means, in the field's own description, so it is not re-derived by whoever reads the board next. The defensible reading is **empty is neutral: the factor has not been assessed.**

That carries a consequence worth naming out loud, because it catches people out: **an explicit low value ranks below one never assessed.** Scoring a factor 1 is a judgment that the thing is bad. Leaving it empty is a statement that nobody looked. Those are different claims and the ranking should reflect it.

Where a formula averages its factors, **exclude empties from the denominator** rather than reading them as zero — an unassessed factor otherwise silently penalizes the item.

If a design genuinely wants unassessed items to sort last, that is a different rule and it must be written down. Be aware of what it costs: "unassessed" and "worst" stop being distinguishable, which is rarely what anyone wanted.

## 5. Bodies get a budget, taken off the corpus median

Measure the items your team actually picks up without asking questions, take the median length, and make that the budget. Not a number from a template, not a number from another team — this team's own median, from `references/<subject>-corpus.md` (`config/house-style.md` §9).

The budget is what stops a body growing to fill its template. A ticket at four times the median is not more thorough; it is a spec nobody finishes reading, and the part that mattered is in the middle.

## 6. A section template is a menu, not a checklist

The section set lists what a body **may** carry. It is not a form to complete.

**An empty section is deleted together with its header.** A header over nothing is worse than the section's absence: the reader stops to work out whether it was considered and came back empty, or whether something is missing. Padding is the same failure from the other side — three acceptance criteria that restate the title teach everyone to stop reading acceptance criteria.

Deleting a section is the correct, common outcome and needs no note.

## 7. The chat gets a table, then one line per item

**Before the write:** one table, one row per item, carrying the factors and the computed score. The user approves a ranking they can scan and argue with, not a wall of prose. A ranking is reviewable in a table and unreviewable as paragraphs.

**After the write:** one line per item — identifier, title, link. Nothing else.

**The body never appears in the chat.** Its home is the tracker. Rendering it doubles the reading cost for no gain, and the two copies start diverging the moment anyone edits the real one.

## 8. One priority vocabulary, and what the tiers mean

Five vocabularies were in use across the tree with one definition between them — and that definition was incident severity, which is a different axis. `P0` meant "top of the backlog" in one skill and "all users down" in another. A tier nobody has defined is a label, not a priority.

**Pick one vocabulary per tracker and define its tiers where the tracker can see them.** The default below is a starting point; replace the anchors with your own and keep the shape.

| Tier | Means | Test |
|------|-------|------|
| P0 | Drop other work | Someone is blocked right now, or the window closes this week |
| P1 | This cycle | Committed for the current sprint or month |
| P2 | Next cycle | Real, sequenced, nobody is waiting on it today |
| P3 | Someday | Kept for the record; no cycle claimed |

**Severity is a separate axis and keeps its own labels.** An incident's P0 is about blast radius, not about queue position — `/post-mortem` owns that scale and it does not map onto this one. A ticket can be severity-low and priority-P0, or the reverse, and collapsing the two loses both.

**`High / Medium / Low` and `Critical / High / Medium` are the same axis under different names.** Where a skill hands its output to a tracker, translate to the tracker's own live vocabulary at the point of write (`references/protocols/freshness-provenance.md`: read the values the board actually offers, every run). Do not invent a fourth spelling.

**`/prioritize`'s Leverage / Neutral / Overhead is not a priority tier** and never maps onto one. It classifies where a person's time goes, not what a team does next, and an L does not imply a P0.

## 9. Empty sections: delete, say so, or fail — which applies where

Three skills answered this differently and all three were right about their own artifact. The rule is about who reads the gap:

- **A tracker item: delete the section with its header** (§6). The reader is picking up work and a bare header costs them a stop.
- **A document with a fixed section set the reader expects — a prep doc, a read-ahead, a review entry: say the section is empty.** A missing section reads as an omission, and "no movement this week" is information. Where it is empty because the source was unavailable rather than quiet, say which (`references/protocols/source-preflight.md`).
- **A structural artifact whose sections are its method — a journey map's stages, a canvas's blocks: an empty one is a genuine gap and the check should fail.** The section is not optional content, it is a piece of the analysis that did not get done.

The test: **delete it where the artifact is a menu, name it where the reader is counting sections, fail it where the section is the method.**

## 10. Where the boundary sits: PM factors, engineering effort

The PM owns the factors that describe **value** — how many are affected, what it is worth, how it fits the current strategy, how badly it hurts today. Engineering owns **effort**, and that does not change because a formula has a slot for it.

A prioritization score may take an effort factor **only where engineering supplied it.** Otherwise that factor stays empty, which reads as neutral per §4. None of this licenses a PM-supplied estimate: see the no-estimating rule in `.claude/skills/create-tickets/SKILL.md`, which stands.

## Cross-References

- `config/house-style.md` §9 — corpus first: the median in §5 comes from mined evidence, not recall
- `references/protocols/freshness-provenance.md` — read the tracker's live field vocabulary every run before writing to it
- `references/protocols/commitment-gate.md` — scoring is cheap; creating committed work is not, and the gate fires on the second
- `references/protocols/skill-patterns.md` — disciplines #4 and #5: propose the batch, write on approval
