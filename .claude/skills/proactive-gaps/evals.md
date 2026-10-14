---
skill: proactive-gaps
archetype: Analysis
eval-version: 5
last-updated: 2026-10-13
---

# Evals: /proactive-gaps

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Scan structure | Output carries a Framing Delta, then Hypotheses, the Contrarian Read, a Cut list, and Run Quality where required. No Book or Constraint section: those findings are `/warehouse-brief`'s |
| E2 | Ranked on two stated factors | Window × claimability, both stated per item, never ranked on one |
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
| E9 | Evidence-backed, graded as hypothesis | Every item is graded visibly as a hypothesis. FAIL on inference presented as fact; do **not** fail an item for lacking workspace transaction data, which this scan does not use |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Elevated-posture-but-landed | Every item connects a broad/elevated observation back to something concrete in the user's actual IC lane |
| E11 | Contrarian pass grounded | The over-indexing claim is backed by actual recent-meeting evidence, not a generic assertion |
| E12 | Surface-only honored | No task was created, no message drafted for sending, nothing written beyond the scan output itself |

### Category 5: The Hypothesis Bar and Scan Order

| ID | Check | Criteria |
|----|-------|----------|
| E13 | Upside gate named per item | Every item states which gate it passed — more money, more volume, or advantage a competitor cannot copy. FAIL on any item that only prevents deterioration |
| E14 | Three-part bar held | Every item carries (1) a problem quoted verbatim from another institution's primary text, dated and linked, (2) a named asset the org already owns, (3) a named test and a falsifier. A dated window adds its date and one dependency. FAIL on a paraphrase, on secondary text standing alone, and on a dated item cut for being unsized |
| E15 | Floor held as a run check | At least three hypotheses, or fewer with Run Quality saying what the scan could not reach. No padding toward the floor |
| E16 | Not a defect list, and not a back-book review | No defect and no figure computed from the org's own data ships as an item; each is cut with its reason ("a defect", "inside-out") |
| E17 | Empty run reported honestly | Where the bar went unmet, Run Quality says what the scan could not reach and frames it as a fact about the run, not about the business |
| E18 | Framing delta ran first, on dated quotes | The output opens on the internal-vs-external comparison, each side carrying a dated quote from a named source. "No delta" is acceptable only when it names the two sources compared and their dates |
| E19 | Scan order held | Dated primary texts read before undated ones, after the framing delta. FAIL where the evidence shows the dated read was filled in afterward |
| E20 | Cut list populated | Every candidate that missed the bar appears in Cut with the bar it missed. An empty Cut list beside a full shortlist means the bar was not applied |
| E21 | Ledger-derived list | A ledger exists at `outputs/ledgers/proactive-gaps-<date>.md`, written before the list. Every surfaced item has a row, every dropped candidate has a row with the evidence that dropped it, those rows are reported beside the list, and no row was dropped to satisfy a cap. **A list with no cuts beside it is unverified, not clean** (`references/protocols/evidence-ledger.md`) |
| E22 | Forward read beyond the watched names | The forward landscape swept the launches of whoever already holds the gating capability (licence, integration, charter), not only named competitors, and Run Quality names any provider list it read or could not reach (`references/protocols/freshness-provenance.md` rule 4) |
| E23 | Kills what the user already sees | Every item was checked against the user's plan, OKRs, tracker, recent meetings, the last two scans and warehouse briefs, and their rulings, and every match is a `KILL` row naming where the user sees it (`references/protocols/skill-patterns.md` Pattern 4) |
| E24 | Four-part item | Each item is written as numbered facts (each quoted and sourced), logic, falsifiers, and next steps in the user's lane |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
