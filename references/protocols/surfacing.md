# Surfacing

**Principle: A LINE REACHES THE READER CURRENT AND LINKED, OR IT DOES NOT REACH THEM.**

This protocol governs what a sweep-class skill puts in front of the reader: a radar list, a digest section, a notification body, a chat summary, a reply. `references/protocols/evidence-ledger.md` governs how an item earned its verdict. This file governs whether that verdict still holds at the moment it is shown, and whether the reader can get from the line to the source.

## 1. Currency is checked at render time

**The read that found an open loop goes stale before delivery.** Discovery and delivery are different moments, and in a run that verifies, ranks, and renders, the gap between them is long. In one run an answer landed 90 minutes after the thread was discovered, and the list shipped it as open.

So re-read each listed thread's tail just before composing, meaning its last messages as they stand now rather than the snapshot discovery took. At the same moment, cross-check the three places an answer lands when it does not land in the thread: a meeting held since discovery, a sibling thread on the same topic in another channel or DM, and the tracker. The re-read is a lookup like any other: it goes into the lookup log as it returns, and the item's verdict is re-run on it (`references/protocols/evidence-ledger.md` §1 and §4). Where the re-read closes an item, it leaves the list with one line quoting what closed it (`references/protocols/skill-patterns.md` discipline #3). Where it moves the next move to someone else, the item is re-classified. This holds per rendering: each checkpoint, digest, and notification re-reads its own items, and a routine combining several skills' sections re-reads them before it sends.

**The last speaker does not settle who owes the next move.** Read the user's own last message in the thread, whoever spoke after it, for a condition they are waiting on: "once legal signs off", "after Thursday's numbers", "if you can get me the export". Until that condition is met, the move sits with whoever owes the condition. A thank-you after the user's ask does not meet it.

**A delta run narrows discovery only.** A skill that sweeps "since the last run" uses the window to find new candidates and for nothing else. Every carried item is re-read every run, whatever the window says (`references/protocols/evidence-ledger.md` §4, carried rows).

## 2. Every listed item carries its deep link, in every rendering

The link belongs to the item, not to one copy of the list. It has to survive into the dated file, the chat summary, the notification body, and any reply that mentions the item again. A summary that drops links sends the reader back to search for what the run already found, and a digest assembled from several skills' outputs is where links get dropped, because the assembler shortens.

A deep link opens the item itself: the message permalink, the ticket URL, the doc anchor. A link to the channel or to a search results page is not a deep link. Where no link exists (a commitment spoken in a meeting with no transcript), name the source and its date and say there is no link. A rendering that cuts the list down keeps the link on every line it keeps.

## Cross-References

- `references/protocols/evidence-ledger.md` — the verdict each surfaced item carries, and the §4 carried-row rule that this file's §1 extends to delta runs
- `references/protocols/skill-patterns.md` — discipline #10, delivering in checkpoints; this file is what each checkpoint checks before it renders
- `references/protocols/notifications.md` — item 3, render before you post; the rendered copy is the one these rules apply to
