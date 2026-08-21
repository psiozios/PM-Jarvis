# Evidence Ledger

**Principle: THE LOG IS WRITTEN AS THE LOOKUPS RETURN; THE LIST IS A TRANSCRIPTION OF IT.**

Any run that will drop, merge, or suppress candidates builds two artifacts before it builds a list: an append-only **lookup log**, written while the run happens, and a **ledger** carrying one row per candidate. The proposal list is derived from those two mechanically. A run that assembles its evidence at the end has skipped this protocol, and the output looks identical either way — which is why the rule is about when the writing happens, not how the table reads.

## 1. The lookup log

**Append one line the moment a lookup returns**, before the next lookup starts. Not at the end of the step, not when the section is being written.

| Field | Holds |
|-------|-------|
| Timestamp | When the lookup returned |
| Tool | The tool or source queried |
| Query | The query string **verbatim**, as sent |
| Hits | How many results came back, zero included |
| Candidate | Which ledger row this lookup was for |

**Composing the log afterwards is the fabrication itself.** One run that wrote its evidence up at the end produced three fabricated entries, among them timestamps for times that had not yet occurred. Appended as each lookup returns, the same log costs one line apiece and cannot carry a query that was never sent.

**Strike an unsupported claim; never back-fill it.** Running the missing query now and presenting the result as contemporaneous is the same defect wearing a fix's clothes. The claim goes.

**Expand every distinctive noun into its closed, hyphenated, and spaced forms in one query.** One word to a reader is three searches to a tool, and a miss because only one spelling was tried is a manufactured absence, not a finding.

## 2. The ledger

Written to `outputs/ledgers/<skill>-<date>.md` before any candidate is dropped — one row per candidate, no exceptions, including the ones that look obviously fine and the ones that look obviously dead.

| Column | Holds |
|--------|-------|
| Candidate | The item as it appeared in the source |
| Lookup run | The **targeted** query for this candidate, keyed on **its own nouns** — its ticket ID, its feature name, the person who owns it. Recorded as run, not as intended. |
| Evidence | What came back, **verbatim**. A paraphrase is not evidence. |
| Verdict | `PROPOSE` / `KILL` / `UNPROVEN` |

**The root cause this closes.** Reading a source for the window and checking one candidate are **different operations**. Sweeping the last thirty days of a channel tells you what happened in that channel; it does not tell you whether *this* commitment was met, because the answer may live somewhere the sweep never went. Substituting the sweep for the per-candidate lookup is the failure — and it is invisible from the outside. One lookup per candidate, keyed on that candidate's own nouns, or the row is `UNPROVEN`.

## 3. The evidence table is a join, not a composition

Build the table by joining the log to the candidate list on the candidate key. **A cell carries only a query that appears in the log; otherwise it stands empty.** An empty cell is a fact about the run — that lookup did not happen — and it ships empty. Filling it to make the table look complete is the fabrication class this whole protocol exists to close.

**Counts come off the file**, never off recall: to say "eleven items", count eleven rows. **No `PROPOSE` row, no proposal** — nothing reaches the user that does not have a row.

## 4. Verdicts

**Absence of a trace neither closes an item nor proves it open.** People decide things in rooms, and no tool logs that. A lookup that returned nothing supports exactly one verdict.

**The error asymmetry, which runs against intuition.** A false proposal costs the reader one line they scan and dismiss. A false kill silently loses a real commitment — nobody ever learns it was dropped, because a killed item leaves no trace to notice. The costs are nowhere near symmetric, so the burden of proof sits entirely on the kill: **an unproven kill is not a kill.** Confidence that something is already handled is not evidence that it is.

**`UNPROVEN` ships as a one-line question — never as a proposal, never as a silent drop.** A proposal asserts the item is live, and that is precisely what is unproven. A question puts the one fact the user holds and the tools do not where it costs them a line to answer.

**Report the kills beside the proposals.** Every output carries its killed rows with their evidence, next to the list. This is the check the reader runs on the run itself — **a list with no kills beside it is unverified**, not clean, and should be read as a run that skipped this protocol.

**Volume caps trigger a re-check, never a truncation.** A cap that bites means the run found more than expected, which is information about the ledger, not permission to cut its tail. Re-read the rows, look for the merge or the wrong-verdict cluster that inflated the count, and report the real number either way. Dropping rows to hit a number is a silent kill of every row below the line.

**Carried rows age out on the record.** An item appearing in the same bucket for a third consecutive run has stopped being news. It earns one **park-or-drop** line — say which, and why — and then it leaves the list. Carrying it silently forever is how a list stops being read.

## Cross-References

- `references/protocols/skill-patterns.md` — discipline #9 is the pointer into this file; the surrounding disciplines say when a skill is in this class
- `references/file-creation-rules.md` — where the ledger file goes (`outputs/ledgers/`)
- `references/protocols/knowledge-capture.md` — what may be proposed once a row says `PROPOSE`
