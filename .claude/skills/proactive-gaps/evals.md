---
skill: proactive-gaps
archetype: Analysis
eval-version: 4
last-updated: 2026-09-11
---

# Evals: /proactive-gaps

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Class-separated structure | Output carries a Framing Delta, then Forward Upside, Book Upside, Outside-In Hypotheses, the Contrarian Read, and a Cut list — not a merged list |
| E2 | Ranked on two stated factors | Size × claimability where both exist; window × claimability for an unsized forward item. Both factors stated per item, never ranked on one |
| E3 | "Your lane" stated per item | Every item explicitly states what the user can do with it |

### Quality & Voice

| ID | Check | Criteria |
|----|-------|----------|
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language. **Spot-check the claims against the cited sources**; where a source cannot be reached, score N/A and name it rather than passing on plausibility |
| E8 | Durability | Evidence cited for each item is either dated or points to a live source, never asserted as an unchanging fact. See `references/protocols/freshness-provenance.md`. |
| E9 | Evidence-backed, and graded to its class | Book and forward items cite a real source. An outside-in item is allowed to run ahead of the data and is graded visibly as a hypothesis. FAIL on inference presented as fact; do **not** fail a forward or outside-in item for lacking workspace transaction data — that is what its own bar exists for |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Elevated-posture-but-landed | Every item connects a broad/elevated observation back to something concrete in the user's actual IC lane |
| E11 | Contrarian pass grounded | The over-indexing claim is backed by actual recent-meeting evidence, not a generic assertion |
| E12 | Surface-only honored | No task was created, no message drafted for sending, nothing written beyond the scan output itself |

### Category 5: Class Bars and Scan Order

| ID | Check | Criteria |
|----|-------|----------|
| E13 | Upside gate named per item | Every item states which gate it passed — more money, more volume, or advantage a competitor cannot copy. FAIL on any item that only prevents deterioration |
| E14 | Each item held to its own class bar | Book: a money or volume figure with derivation and grade. Forward: a real date from a real source plus one named dependency. Outside-in: a named test and a falsifier. **FAIL on a forward item cut for being unsized** — the money bar does not apply to it |
| E15 | Floor, forward rule, and cap held | At least three upside items, **at least one of them forward**, at most one constraint carrying a revenue or volume number |
| E16 | Not a defect list, and not a back-book review | No defect without a number. Constraints were not used to pad toward the floor. And the run did not stop at three sized book items without reaching the forward class |
| E17 | Empty run reported honestly | Where a bar went unmet — and always where no forward item survived — Run Quality says what the scan could not reach and frames it as a fact about the run, not about the business |
| E18 | Framing delta ran first, on dated quotes | The output opens on the internal-vs-external comparison, each side carrying a dated quote from a named source. "No delta" is acceptable only when it names the two sources compared and their dates |
| E19 | Scan order held | Forward landscape read before book upside, and outside-in last. FAIL where the evidence shows the money was read first and the forward class filled in afterward |
| E20 | Cut list populated | Every candidate that missed a bar appears in Cut with the bar it missed. An empty Cut list beside a full shortlist means the bars were not applied |
| E21 | Ledger-derived list | A ledger exists at `outputs/ledgers/proactive-gaps-<date>.md`, written before the list. Every surfaced item has a row, every dropped candidate has a row with the evidence that dropped it, those rows are reported beside the list, and no row was dropped to satisfy a cap. **A list with no cuts beside it is unverified, not clean** (`references/protocols/evidence-ledger.md`) |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
