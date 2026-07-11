---
name: feedback-example
description: "Placeholder showing the feedback_ memory format. Delete this file and replace with real entries."
metadata:
  type: feedback
---

*Placeholder -- delete me once you have a real feedback_ entry.*

Behavioral rules the assistant must follow everywhere, including corrections and confirmed approaches.

**Example of a real feedback-type entry:**

Always include a "Not Doing" section in PRD drafts.

**Why:** PRDs without explicit non-goals led to scope creep during engineering review.

**How to apply:** In `/prd-draft` output, always include a "Not Doing (Explicitly)" section with 2-3 items, even if the user didn't ask for it. They can remove items they disagree with.

**Note:** A feedback_ memory entry is also the durable enforcer for the commitment-gate protocol (see `references/protocols/commitment-gate.md`). If you want the gate to fire automatically, save a feedback_ entry like: "Run the commitment-gate checklist before creating tickets or committing work to a sprint."

**Note:** The routines protocol (`references/protocols/routines.md`) and the freshness-provenance protocol (`references/protocols/freshness-provenance.md`) each name a short list of rules that can similarly be mirrored here as feedback_ entries once you have a real routine or a real shared document to apply them to. Neither protocol seeds a real entry on its own — that would assert an unearned rule. Propose the mirror when the concrete need shows up.
