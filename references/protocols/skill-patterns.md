# Skill Patterns

**Principle: THE CATALOG IS THE SHAPE; THE EXAMPLE SKILLS ARE THE HOW.**

This is a catalog of reusable skill archetypes the template ships as worked, production skills, plus the disciplines every retrieval-and-writeback skill shares regardless of which archetype it follows. The skills named under each pattern below are concrete implementations of Patterns 1-3 — read this file for the shape, read those skills for a filled-in instance.

These are worked examples of a broader class, not the only class. If a new task doesn't fit any named pattern, that's fine — the cross-cutting disciplines still apply.

## Cross-Cutting Disciplines

Every skill in this class — anything that searches across sources and then proposes, surfaces, or writes back a list — follows these ten rules. Read-only skills are in scope: proposing nothing does not exempt a skill from having to be right about what it dropped.

### 1. A search hit is a pointer, never an answer

A match from a search (a keyword hit, a title match, a snippet) tells you where to look, not what's there. Open every candidate and read it to resolution before classifying it as anything. Never report a search result as a finding without having read the underlying content.

### 2. Verify before surfacing

Cross-check each candidate against orthogonal sources — a calendar, a tracker, an issue board, an email thread, a sibling skill's output — and emit a per-item `Checked:` line naming what was cross-referenced. Silence in one channel is not proof of anything; the absence of a follow-up in Slack doesn't mean the loop closed, it might mean the reply happened somewhere else entirely.

Verification runs on a budget, so spend it in rank order: rank the candidates first, gate the top N, and state the ungated count rather than implying the whole list was checked. What that gate may cost — one inline batch by default, a spawned agent only where a false positive is expensive — is in `references/capabilities.md`.

### 3. From-scratch re-discovery for standing radars

A skill that runs repeatedly over a rolling window (a radar, a periodic sweep) re-sweeps the **full** window every run. Prior-run state is used only to mark items new-vs-carried for the user's benefit — never to narrow the search or suppress items from being re-examined. Narrowing the sweep based on "we already looked at this" is how a radar quietly stops catching things that changed since the last pass.

**Carry forward means re-check, not re-present.** A carried item re-runs its own lookups as if it had never been seen, and the bucket it sits in exempts it from nothing — every gate that applies to a new item applies to it. Where this run's evidence closes it, close it yourself: one line naming the quote that closed it, and the item leaves the list. Handing back a stale list for the user to adjudicate is the same defect as listing an unchecked item, only deferred onto them.

### 4. Surface, then propose, then create-on-approval

Reading is free — do it liberally. A durable write to the user's own store (their tracker, their notes, their calendar) is proposed as a numbered list and only executed on explicit approval. Anything outward-to-others (a message, an email, a comment visible to someone else) is draft-only, always — see `references/protocols/knowledge-capture.md`.

### 5. Preview-first for write-heavy skills

If a skill's main output is a batch of writes, dry-run by default. Show what would be written; write nothing until an explicit go-ahead.

### 6. Dedupe against sibling skills' outputs

Before surfacing something as new, check whether a sibling skill already surfaced it. Two radars flagging the same stalled thread from different angles is noise, not signal — cross-check before adding.

**Dedupe across sections too, not only inside the list.** One item can appear once as flagged-for-awareness and once as could-not-verify, and neither section looks duplicated from inside itself, because the duplicate lives on the boundary between them. Run the check across the whole output before it ships.

### 7. False-positive discipline

Every flag survives a skeptic's pass before it ships: a long-lived thread is not automatically a stalled one; a deliberately light-touch document is not automatically a thin one; two similar-sounding items are not automatically duplicates. When confidence is genuinely low, mark the item low-confidence explicitly, or drop it rather than force a verdict.

### 8. Never mutate a shared system you don't own

A skill in this class does the judgment work and hands back an **execute-not-decide** artifact — a checklist, a ranked shortlist, a drafted comment — for a human to apply. It does not click the button, move the card, or edit the shared doc itself.

### 9. Deduplication is an artifact, not a judgment

**Write the log and the ledger before the list exists.** Any run that will drop, merge, or suppress candidates appends one line per lookup as it returns, writes one ledger row per candidate, and then derives the proposal list from those two files mechanically. The list is a transcription, not a second act of judgment.

The full process — the log's fields, the join that builds the evidence table, the three verdicts, and what an empty cell means — is `references/protocols/evidence-ledger.md`. Read it **before the first lookup of any run that will drop a candidate**, not when the table is being written; by then the run it governs is already over.

### 10. Deliver in checkpoints, one topic to one section

**Split the output where the reader's involvement splits.** The half that needs an answer from them — the questions, the `UNPROVEN` one-liners, anything blocked on a fact only they hold — ships as soon as it is ready and never waits behind the half still being verified. Two deliveries with a gap between them beat one that lands after the reader has moved on.

**Pick each item's section by what the reader does with it**, not by which check produced it. Where a second section has a caveat about the same item, fold the caveat into the line carrying the action — **fold rather than delete**, so the caveat survives at the point of use.

## Named Archetypes

### Pattern 1 — Open-Loop Radar (cross-source follow-through)

**Job:** Find stalled two-way loops the user may be dropping — across conversations they're a participant in and about work they own.

**Mechanics:** Sweep both directions (inbound asks/mentions directed at the user, and the user's own outbound posts awaiting a reply) across a defined set of channels. Classify each open item by whose court the next move is in. Verify-before-flag with a `Checked:` line per item (discipline #2). Bucket results by age — fresh, this-week, aging, stale. Comprehensive, not delta (discipline #3): every run re-sweeps the full window. Frame findings non-accusatory — this is triage, not a scorecard. Attach one real deep link per item so the user can jump straight to it. Propose a follow-up task only for items where the next move is genuinely the user's — not for items sitting in someone else's court.

**Eval archetype:** Workflow-Orchestration.

**Shipped implementation:** `.claude/skills/loose-threads/`. Dedupes against `.claude/skills/action-sweep/`, a sibling skill that also sweeps chat/email/meetings but for owed action items rather than stalled loops.

### Pattern 2 — Periodic-Review Assisted-Fill Cascade (week → month → quarter)

**Job:** Turn a recurring review ritual from a blank-page exercise into a pre-filled draft the user edits, at every cadence tier.

**Mechanics:** Auto-fill everything derivable from existing sources; ask the user only for genuine judgment calls — never hand over a blank questionnaire. Present an explicit "auto-filled vs. asked" table so the user can see what was inferred versus what needs their input. Forward-create the next N periods with dedupe against what's already scheduled. Writes are surgical: fetch current state, compute the delta, apply only the delta — never replace wholesale. All writes to the user's own store happen on confirm (discipline #4). Each higher cadence tier (month, quarter) rolls up and synthesizes the tier below it rather than re-deriving from scratch.

**Eval archetype:** Workflow-Orchestration.

**Shipped implementation:** `.claude/skills/weekly-review-fill/` → `.claude/skills/monthly-review-fill/` → `.claude/skills/quarterly-review-fill/`, a nested cascade where each tier rolls up and synthesizes the completed tier below it rather than re-deriving from raw activity.

### Pattern 3 — Read-Only "Prep-Then-UI" Grooming + "Slate-for-Ceremony" Pair

**Job:** Two read-only passes over a shared board (a backlog, a kanban, a review queue) that the skill never mutates directly — it prepares, a human clicks.

**Mechanics:**
- **Hygiene pass:** emits a checklist grouped by the actual click the human will make — close, reorder, re-allocate, tag, fix a description — with drafted replacement text inline where relevant, so applying the fix is a paste, not a rewrite.
- **Slate pass:** asks what the period's theme is first, then ranks a capped shortlist of candidates for the next ceremony (planning meeting, review, triage session), drafts each shortlisted item's enrichment (description, acceptance criteria, sizing note), and surfaces the 1-2 genuine unknowns that would cause rework if guessed wrong instead of asked.

Both passes are strictly read-only (discipline #8) and both establish priority live at run time, never from a stale cached ranking. They're designed as a paired cadence — hygiene keeps the board clean between ceremonies, slate prepares the next one.

**Eval archetype:** Workflow-Orchestration.

**Shipped implementation:** `.claude/skills/backlog-groom/` (hygiene pass) paired with `.claude/skills/refinement-prep/` (slate-for-ceremony pass) — the two skills this pattern describes as a pair.

### Pattern 4 — Multi-Horizon "Alpha Engine" Scan

**Job:** Answer "where is the upside?" across two time horizons at once — money and volume available now, and advantage available next — plus a contrarian pass on what the team is currently over-indexing on.

**Mechanics:** Run from a deliberately elevated posture (zoom out further than the user's day-to-day view would), but land every single item back in the user's actual lane — a horizon-scan that doesn't connect to something the user can act on is not useful, it's just anxiety. Surface-only: this pattern proposes nothing and writes nothing, it only reports.

**Gate the horizon, or it decays into a defect list.** This is the pattern's characteristic failure and it is gradual: broken things are the easiest thing to find in any workspace, they feel like insight, and a scan with no gate fills up with them until it is a bug list with a strategic preamble. The gate: if the reader acts, does the business make more money, move more volume, or gain advantage a competitor cannot copy? A defect passes only with a revenue or volume number attached. Enforce a floor of upside items against a hard cap of one constraint item, size everything or cut it, and rank by size × claimability rather than size alone. When nothing clears the gate, that is a finding about the run — thin sources, no metrics access — and never a conclusion about the business.

**Eval archetype:** Analysis or Research-Synthesis, depending on framing.

**Shipped implementation:** `.claude/skills/proactive-gaps/`

## Cross-References

- `references/protocols/context-acquisition.md` — the "read freely" half of discipline #1-3 above
- `references/protocols/knowledge-capture.md` — the "write on confirm" half of discipline #4-5 above
- `references/protocols/evidence-ledger.md` — the log-then-ledger-then-list process behind discipline #9
- `references/file-creation-rules.md` — where the ledger file goes (`outputs/ledgers/`)
- `references/protocols/routines.md` — every pattern above is a natural candidate to ship as a scheduled routine (a radar or periodic-review cascade in particular); see `setup/routine-setup.md` to wire one up
