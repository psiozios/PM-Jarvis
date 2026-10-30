# Retro Mode: a PRD for a Product Already Shipped

Read when the run is `/prd-draft --retro`, or when the user asks for a PRD of something that is already live. The rules that bind it are in `SKILL.md` under Mode: --retro; this file carries the method and the shape.

## When it fits

A product shipped with no PRD, or with one that has drifted from what the code does. The retro PRD writes down what the product is, what it was meant to do, and where those disagree. It is not `/feature-results` (results against targets, which assumes a PRD with targets exists) and not `/post-mortem` (an incident's timeline and prevention). Hand off to either when the run turns up a missed target or an incident.

## Method

### 1. Intended behavior comes from the user

Ask first, before reading anything: what was it meant to do, for whom, under what rules? Their answer is the baseline, graded as reported by the user. Do not reconstruct intent from the code; the code is what gets checked against it.

### 2. Read the four sources, each on its own

| Source | What to read | Grade |
|--------|--------------|-------|
| **Code** | The live code path, read-only (`/explore-codebase`): entry points, handlers, the conditions that gate behavior | Inferred from the code, until its engineer confirms |
| **Contract** | The contract, terms, or policy in force, with its version and every comment, resolved ones included | Reported, with the version |
| **Sales and ops material** | Decks, FAQs, help-center pages, runbooks, support macros: what customers were told, and what the team does by hand | Reported, with the date of each document |
| **Ticket acceptance criteria** | The tickets that built it, read for their acceptance criteria, not their status | Reported, with the ticket IDs |

### 3. Cross-check, four ways, behavior by behavior

For each behavior the user named, put the five readings side by side: intended, code, contract, sales and ops, acceptance criteria. **Every disagreement is a gap**, listed under Problem → Current implementation gaps with the source on each side, and carrying an owner in Open questions. One run found a fee waiver narrower in the code than in any document: the contract, the sales deck, and the tickets all said one thing, and the code did another. That gap was the finding of the run.

Agreement across all five is reported too, in one line per behavior, so the reader can see what was checked.

### 4. Status is date-stamped or linked live

Every status claim either carries the date it was read or links to its live source (`references/protocols/freshness-provenance.md`). "Shipped" is two claims, code live and customers using it, each on its own source (rule 5).

## Shape

The same themes as a forward PRD, in the past tense, with two changes:

- **No rollout plan.** The section is omitted; the rollout already happened. Where its history matters, it goes in the appendix.
- **A review trigger instead of kill criteria.** Under Business metrics and goals: "Review trigger: if [threshold], [owner] reopens this document." Evals score kill criteria N/A for a retro, never PASS.

Target length: 800-1500 words in the body, scored like any stage (`SKILL.md`, Stage-Specific Length Guidance). Save to `outputs/prds/[product-name]-retro.md`.

```markdown
## Current implementation gaps

| Behavior | Intended (user) | Code | Contract (v_) | Sales and ops | Acceptance criteria | Gap | Owner |
|----------|-----------------|------|---------------|---------------|---------------------|-----|-------|
| [behavior] | [what it was meant to do] | [what the code does, file] | [clause] | [doc, date] | [ticket ID] | [the disagreement, or "agree"] | [name] |
```
