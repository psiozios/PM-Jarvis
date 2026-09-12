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

## 8. Where the boundary sits: PM factors, engineering effort

The PM owns the factors that describe **value** — how many are affected, what it is worth, how it fits the current strategy, how badly it hurts today. Engineering owns **effort**, and that does not change because a formula has a slot for it.

A prioritization score may take an effort factor **only where engineering supplied it.** Otherwise that factor stays empty, which reads as neutral per §4. None of this licenses a PM-supplied estimate: see the no-estimating rule in `.claude/skills/create-tickets/SKILL.md`, which stands.

## Cross-References

- `config/house-style.md` §9 — corpus first: the median in §5 comes from mined evidence, not recall
- `references/protocols/freshness-provenance.md` — read the tracker's live field vocabulary every run before writing to it
- `references/protocols/commitment-gate.md` — scoring is cheap; creating committed work is not, and the gate fires on the second
- `references/protocols/skill-patterns.md` — disciplines #4 and #5: propose the batch, write on approval
