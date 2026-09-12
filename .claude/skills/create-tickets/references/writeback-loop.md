# The Writeback Loop

Bulk reference for `/create-tickets`. Read when a ticket ships with an Open question, or when a source this run read contains the answer to one.

**An answer that resolves a ticket's ambiguity lands in the ticket before the thread that produced it closes.**

Ambiguities in tickets get resolved somewhere else — a chat thread, a hallway answer, a design review, a comment on a different ticket. The answer arrives, everyone present understands it, the thread goes quiet, and the ticket still says `[TBD]`. Whoever picks the work up later finds the question and not the answer, and asks it again.

The loop:

1. A ticket ships with an Open question naming who can answer it.
2. When that question gets answered anywhere, **edit the ticket description first** — before replying in the thread, before closing it, before moving on.
3. Write the answer into the description as a resolved statement with its source: who answered, where, and when. Do not leave it as a comment; comments are not read by whoever picks up the ticket.
4. Only then close the thread.

The ordering is the whole rule. Reply-then-update becomes reply-and-forget within one context switch, and the thread — which is the only remaining copy of the answer — is exactly the thing that gets archived.

When this skill runs and finds a ticket whose Open question was answered in a source it has read, it proposes the description edit as part of its output. Per `references/protocols/knowledge-capture.md` the edit is proposed and never written unprompted, since a ticket is a shared system other people are acting on.
