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
