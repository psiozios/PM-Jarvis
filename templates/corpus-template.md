<!-- TEMPLATE: Copy to `references/<subject>-corpus.md` and fill from real history.
     This file ships the method. It ships no findings, and a filled-in corpus
     never ships back — it is workspace-private evidence about real people. -->

# <Subject> Corpus — <DATE>

A dated evidence snapshot of how <subject> actually gets written here, mined before any rule about it is written or revised. Rules cite this file by quote ID. See `config/house-style.md` §9 for when a corpus is required.

**Snapshot, not a standing claim.** This file is true as of the date in its title and nothing else. Re-mine rather than edit when the history moves on; append a new dated section, never overwrite an old one (`references/protocols/freshness-provenance.md` rule 2).

## What was mined

| Field | Value |
|-------|-------|
| Subject | <the rule area: ticket descriptions, status updates, one specific person's voice> |
| Sources swept | <channels, docs, trackers — name them> |
| Window | <first date> to <last date> |
| Items read to resolution | <count> |
| Items skipped, and why | <count + reason: forwarded-only, no prose, wrong author> |
| Mined by | <who or what ran the sweep> |

## Coverage

One row per facet the rules will need to cover. **A facet with no evidence gets no rule** — it gets a gap line here and a question for the user.

| Facet | Items found | Enough to rule on? | Gap |
|-------|-------------|--------------------|-----|
| <e.g. opening line> | <n> | yes / no | <what is missing> |
| <e.g. how a decision is stated> | <n> | yes / no | |
| <e.g. contraction habit> | <n> | yes / no | |

## Hypotheses tested

State what you expected to find **before** reading, then record what the evidence did to it. A hypothesis with no verdict is an unfinished row.

| # | Hypothesis | Verdict | Evidence |
|---|-----------|---------|----------|
| H1 | <what you expected> | SUPPORTED / CONTRADICTED / UNDERDETERMINED | <quote IDs> |
| H2 | | | |

**UNDERDETERMINED is a real verdict and the most common honest one.** It means the corpus cannot settle the question — record it and ask, rather than promoting a hunch to a rule.

**Record contradicted hypotheses too.** A hypothesis the evidence killed is the most useful row in this table: it stops the same wrong rule being proposed again next round.

## Quotes

| ID | Verbatim quote | Source | Date | Facet | Flags |
|----|---------------|--------|------|-------|-------|
| Q1 | <exact text> | <where> | <when> | <facet> | <see below> |
| Q2 | | | | | |

**Verbatim means verbatim.** Typos, casing, missing apostrophes, broken markdown, and abandoned half-sentences are all preserved exactly. They are frequently the signal — a writer who never capitalizes a sentence opener is telling you something a cleaned-up quote would hide. Never normalize, never paraphrase, never "fix" a quote to make it presentable.

**The quote carve-out.** A quote that breaks a rule in `config/house-style.md` — a banned word, a P-pattern, a formatting rule — is **preserved as it stands and flagged in the Flags column** with the rule it breaks (`breaks §3: leverage`, `breaks P10`). It is never edited to conform and never dropped for being non-conforming. The carve-out runs one way: it protects the quote inside this file, and it grants nothing to prose written elsewhere.

Other flags worth carrying: `outlier` (real but unrepresentative), `secondhand` (quoted by someone else, not read at source), `redacted:<what>` (identifying detail removed — say what, so a later reader knows the quote is partial).

## Rules derived

The output of the corpus. Every row becomes a rule in a register file, and every rule carries its quote IDs back here.

| Proposed rule | Traces to | Facet | Confidence |
|--------------|-----------|-------|------------|
| <rule as it will be written> | Q1, Q4, Q9 | <facet> | <n quotes across m sources> |

**A rule with no quote IDs is taste, not a standard.** It does not ship. Say so plainly and offer it to the user as a question instead.

**One quote is an anecdote.** Note the count honestly in Confidence; a rule resting on a single quote ships as a question, not a rule.

## Open questions for the user

Things the corpus could not settle. These go to the user rather than into a rule.

- <question, with the facet and the gap that produced it>
