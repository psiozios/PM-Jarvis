# Surfacing

**Principle: A LINE REACHES THE READER CURRENT, LINKED, AND THEIRS TO ACT ON, OR IT DOES NOT REACH THEM.**

This protocol governs what a sweep-class skill puts in front of the reader: a radar list, a digest section, a notification body, a chat summary, a reply. `references/protocols/evidence-ledger.md` governs how an item earned its verdict. This file governs whether that verdict still holds at the moment it is shown, whether the reader can get from the line to the source, and whether the line belongs in front of this reader at all.

## 1. Currency is checked at render time

**The read that found an open loop goes stale before delivery.** Discovery and delivery are different moments, and in a run that verifies, ranks, and renders, the gap between them is long. In one run an answer landed 90 minutes after the thread was discovered, and the list shipped it as open.

So re-read each listed thread's tail just before composing, meaning its last messages as they stand now rather than the snapshot discovery took. At the same moment, cross-check the three places an answer lands when it does not land in the thread: a meeting held since discovery, a sibling thread on the same topic in another channel or DM, and the tracker. The re-read is a lookup like any other: it goes into the lookup log as it returns, and the item's verdict is re-run on it (`references/protocols/evidence-ledger.md` §1 and §4). Where the re-read closes an item, it leaves the list with one line quoting what closed it (`references/protocols/skill-patterns.md` discipline #3). Where it moves the next move to someone else, the item is re-classified. This holds per rendering: each checkpoint, digest, and notification re-reads its own items, and a routine combining several skills' sections re-reads them before it sends.

**The last speaker does not settle who owes the next move.** Read the user's own last message in the thread, whoever spoke after it, for a condition they are waiting on: "once legal signs off", "after Thursday's numbers", "if you can get me the export". Until that condition is met, the move sits with whoever owes the condition. A thank-you after the user's ask does not meet it.

**A delta run narrows discovery only.** A skill that sweeps "since the last run" uses the window to find new candidates and for nothing else. Every carried item is re-read every run, whatever the window says (`references/protocols/evidence-ledger.md` §4, carried rows).

## 2. Every listed item carries its deep link, in every rendering

The link belongs to the item, not to one copy of the list. It has to survive into the dated file, the chat summary, the notification body, and any reply that mentions the item again. A summary that drops links sends the reader back to search for what the run already found, and a digest assembled from several skills' outputs is where links get dropped, because the assembler shortens.

A deep link opens the item itself: the message permalink, the ticket URL, the doc anchor. A link to the channel or to a search results page is not a deep link. Where no link exists (a commitment spoken in a meeting with no transcript), name the source and its date and say there is no link. A rendering that cuts the list down keeps the link on every line it keeps.

## 3. Every surfaced item earns its line

List an item only if the user owns a move on it, or its topic is a current focus: named in this week's plan, in the active OKRs, or in something the user asked about recently. Waiting on someone counts as a move, because the chase is the user's. A relevant channel is not enough. Sitting in a channel the user reads makes a thread visible, not theirs, and a list padded with visible threads teaches the reader to skim the ones that are. An item that fails this test is a `KILL` row with its reason, reported beside the proposals (`references/protocols/evidence-ledger.md` §4). A `no owner` item is listed, as low-confidence, only when its topic is a current focus.

## 4. A clarification ships only if it passes three tests

1. **The run's own evidence cannot answer it.** Read before asking (`references/protocols/context-acquisition.md` §4).
2. **No role or recency anchor settles it.** The person who owns an area decides inside it, and the newer of two conflicting statements stands unless someone has said otherwise. Where an anchor settles the point, apply it and name it in the line instead of asking. An anchor settles a question; it never turns an `UNPROVEN` row into a `KILL`, which takes evidence.
3. **"If X rather than Y, then ___" completes with a real consequence**: a different action, owner, or date. If both answers lead to the same line, the question has no job.

An `UNPROVEN` row still ships as a one-line question (`references/protocols/evidence-ledger.md` §4) when it passes. One that fails test 3 stays `UNPROVEN` in the ledger and ships as one line marked unasked, with the reason that its answer would change nothing the reader does. It is never counted as a kill.

## 5. No trailing closer; a reply answers the asks and stops

**No trailing confirm-or-ignore line.** "Reply to confirm, or ignore", "let me know if anything's off", and "anything else?" invite silence, and silence is never an answer (`references/protocols/evidence-ledger.md` §4). A real ask that blocks the run is a question under §4 and ships first (`references/protocols/skill-patterns.md` discipline #10). A preview waiting on the user's selection is the step itself, not a closer. So is the one chaining nudge (`CLAUDE.md`, Skill chaining) and a specific write-back proposal (`references/protocols/knowledge-capture.md` §2): each names a next step, and neither asks for confirmation by silence.

**A reply answers the asks and stops.** Answer each thing the user asked, in their order, then end. Extra findings the run turned up go to their own audience (the next digest, the owning skill's list, a separate note the user opens when they choose) and are never appended to the answer. A line the user has questioned twice gets cut, not defended a third time. `references/protocols/knowledge-capture.md` §5 governs drafts to other people; this governs the assistant's own replies.

## 6. The user's rulings bind the next run

When the user rules on something in session ("that thread isn't mine", "drop X until the pricing call", "Priya owns pricing"), write it into the run file that turn, so the next run reads it instead of asking again. For a routine the run file is `routines/<name>/.rulings.md`, read at the bind-rules step and written by the routine's on-reply continuation. For a skill run interactively it is `outputs/state/rulings-<skill>.md`. One dated line per ruling: the user's words, and what they bind. The ruling is the user's own instruction, so writing it needs no second confirmation; echo the line written. A routine hands its `.rulings.md` to every skill it chains, and the skill reads it beside its own file; where two rulings conflict, the newer stands.

**A ruling binds inclusion, never discovery.** The sweep still reads the item, and the ruling decides whether it earns a line, so `references/protocols/skill-patterns.md` discipline #3's full re-examination holds. New evidence on the item (a new message, a status change, the ruling's own condition met) reopens it for that run, and its line says why it is back. A ruling about behavior in general ("never list FYI mentions") is a memory proposal under `references/protocols/knowledge-capture.md`, not run state.

## Cross-References

- `references/protocols/evidence-ledger.md` — the verdict each surfaced item carries, and the §4 carried-row rule that this file's §1 extends to delta runs
- `references/protocols/skill-patterns.md` — discipline #10, delivering in checkpoints; this file is what each checkpoint checks before it renders
- `references/protocols/notifications.md` — item 3, render before you post; the rendered copy is the one these rules apply to
