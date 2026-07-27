# House Style

The anti-slop standard. Agents read this **before drafting prose**, not after. The eval loop is the backstop, not the mechanism.

## 1. Precedence

`CLAUDE.md` Absolute Rules → **this file, including its "Your own rules" section** → `context-library/writing-style-*.md` (per-audience register) → the skill's own instructions. Higher wins on conflict.

**Register is chosen first.** Pick what the medium and audience want, then apply these rules inside that choice. "Concise" is not the same as "good" — a two-line reply that omits the decision is worse than a six-line one that lands it.

## 2. Scope: prose only

**The prose test:** a passage is prose if stripping its formatting would leave complete sentences that read as a paragraph. Sections 4-6 apply to prose passages only.

**Scaffolding is exempt by design.** Template headings, agenda subheadings, ticket fields, table structure, checklists, status columns, and any list whose items are genuinely parallel are intentional structure. Flagging them is a false positive, not a finding.

**Named carve-outs.** This file delegates to a skill wherever that skill defines a symbol as *functional inside its own artifact*. **This list is the grant** — a skill named here is covered without restating it, and a skill not named here has no carve-out whatever its own file says. Live carve-outs: `/execution-plan` (emoji status tokens, progress percentage), `/journey-map` (emotion row glyphs), `/napkin-sketch` and `/prototype` (ASCII and wireframe icons), `/slack-message` and `/content-marketing` (warm-channel and in-app copy, where a single emoji is register).

**Structure vs contents.** The §2 exemption covers table and list *structure* — the grid, the bullets, the headers, parallel labels and fields. Cell and item *contents* are scored as prose whenever the cell alone passes the prose test, and parallelism does not exempt an item from F1: parallel **arguments** in bullets are still F1. Apply the prose test to the whole passage, not item by item — a run of bullets is one passage.

## 3. Banned outright

Zero instances. An eval scores any occurrence **FAIL**.

> delve · leverage · utilize · unlock · harness · streamline · robust · cutting-edge · empower · elevate · foster · holistic · synergy · paradigm · seamless · effortless · game-changing · revolutionary · best-in-class · world-class · transformative · unparalleled · supercharge · deep dive · tapestry · testament · realm · plethora · boasts

**Exempt:** verbatim third-party quotes and raw transcripts — quote the source as it stands, never paraphrase to dodge a ban. Also exempt: **mention rather than use** — a word listed, quoted, or defined as an example inside a rule, checklist, or eval is not an occurrence; only the artifact's own assertions count. (This is what keeps the list above from failing its own rule.) And literal domain senses are exempt: financial leverage, a wiring harness, a last will and testament.

The 14-word subset carried in each `evals.md` (E4) is a **fast tripwire, not the list**. Passing the tripwire is not passing this section.

## 4. Cut on sight unless it's doing work

Soft tier — padding adverbs (*very, really, quite, actually, basically, essentially, simply, just, truly, incredibly, ultimately*) and padding phrases (*it's worth noting, it's important to remember, at the end of the day, in order to, the fact that, needless to say, at scale*). **Both lists are open** — they name the common cases, not the boundary. A word doing no work is soft-tier whether or not it is listed; the keep-test decides, not the list.

**The keep-test:** delete the word, reread the sentence. If meaning or emphasis changed, or the sentence reads **worse** aloud, put it back. Rhythm alone counts only when the sentence reads worse, not merely different — every deletion changes rhythm, so "changed" would make this test a no-op.

**Scored under dimension 4** of §8, capped at **PARTIAL** — soft-tier findings alone never push dimension 4 past PARTIAL, and never contribute to a FAIL. A blanket ban here fights the natural-idiom guidance the register files give. **Tiebreaker:** on a genuine tie, editing someone else's draft keeps the word (§7 case A); drafting from scratch cuts it (§7 case B). The keep-test runs first — the tiebreaker applies only when it comes out even.

## 5. Prose patterns

Seventeen named defects. Adapted from the public `petergyang/no-ai-slop` catalog; credit to that project.

| ID | Defect | Tell | Fix |
|----|--------|------|-----|
| P1 | Negative parallelism | "It's not X. It's Y." | State Y. Delete the X clause. |
| P2 | Throat-clearing opener | Sentence restates the question before answering | Open on the answer. |
| P3 | Faux-insight setup | "Here's the thing" / "The real question is" | Delete the setup; keep the claim. |
| P4 | Colon reveal | Short clause, colon, dramatic noun phrase | One sentence, no colon. |
| P5 | Superficial-analysis participle | "…, highlighting the need for…" tacked on | Cut the participle or make it a real claim. |
| P6 | Importance puffery | "crucial", "vital", "critical" with no stakes named | Name the actual consequence. |
| P7 | Weasel attribution or ungraded figure | "experts say", "studies show" — **and** any bare statistic, percentage, or date with no source | Name the source, or grade the claim. |
| P8 | Fake-strong verb | "drives", "powers", "fuels" doing no work | Use the literal verb. |
| P9 | Synonym cycling | Same referent renamed each mention | Pick one noun; repeat it. |
| P10 | Dramatic fragmentation | One-word sentences for effect. Like. This. | Rejoin into a sentence. |
| P11 | Robotic rhythm | Every sentence the same length and shape | Vary length deliberately. |
| P12 | Rhetorical setup | "But what does that mean?" / "So why does this matter?" | Delete; answer directly. |
| P13 | Fake-profound kicker | Closing aphorism that adds no fact | **Delete it.** See below. |
| P14 | Summary-recap ending | Final paragraph restates the piece | Delete; end on the last real point. |
| P15 | Hedging | "may perhaps somewhat suggest" | One hedge max, or commit. |
| P16 | Passive-for-agency | Actor hidden by passive voice | Go active. See below. |
| P17 | Aspirational closing | "…positioning us for the future" | Delete, or replace with the next action. |
| P18 | Prose contradicting the artifact | A sentence restates structured content — a table row, a status column, a checklist — and gets it wrong | **Fix the prose to match the data.** Never fix the data to match the prose, and never resolve it by deleting the sentence. |

**Overlapping patterns.** Cite **every** ID that fits, and apply the **strongest** fix. Where fixes conflict, the delete-fixes win (P13, P14, P17) — citing P1 on a closing aphorism and leaving half of it standing is the divergence this rule prevents. Count and report **per instance**, not per ID: P7 appearing three times is three findings.

**Three fixes that must not diverge between agents:**

- **P13** — the kicker is **deleted**, not rewritten into a better metaphor and not replaced with a new closing line. The piece ends on its last substantive sentence.
- **P7** — an unsourced claim worth keeping is **flagged in place** with an honest evidence grade (`[unsourced]`, `[from memory]`, `[needs check]`). Never silently cut a fact; never invent a source for it.
- **P16** — where the passive hides an owner the draft never names, go active with the actor you have and **flag the missing owner** (`[owner?]`). Never invent one. *Exception:* a blameless post-mortem timeline keeps the agentless passive on purpose — see `/post-mortem`.

**False positives are findings, not fixes.** P6 exempts terms of art (critical path, critical severity). P8 is not a defect when the literal verb is the accurate one ("the battery powers the sensor"). P9 fires only on renaming to avoid repetition with no change in meaning, not on pronouns or genuinely distinct aspects. P10 applies inside a prose paragraph, not to a one-word answer. P15 does not count evidence grades or scope qualifiers as hedges. P1 keeps the X clause when it corrects a misreading the reader is likely to hold.

## 6. Prose formatting

Read against the prose test in §2.

| ID | Rule |
|----|------|
| F1 | Bullets standing in for prose — if the items are sentences in an argument, write the paragraph. |
| F2 | Headings over sections too small to need them (a heading above two sentences). |
| F3 | Decorative bold — bold marks a term or a decision, not emphasis-by-habit. |
| F4 | Decorative emoji in prose (functional tokens are §2 carve-outs). |
| F5 | Nested template bodies polluting an outline — fence or extract them. |
| F6 | Formatting outweighing content — more structure than the substance requires. |

**Tiebreakers.** One malformed item inside a list that is otherwise doing real work is a **broken item, not a broken list** — fix the item. And a heading that appears in the artifact's own template is scaffolding under §2 **regardless of body length**; F2 reaches only headings the drafting agent introduced. When in doubt, the heading is scaffolding.

## 7. Drafting and editing principles

Written for the drafting agent first — the cheapest slop to remove is the sentence never written.

Know the job before the first sentence. Lead with the point. Be concrete: names, numbers, dates, mechanisms. Protect the specific fact. Active voice with human subjects. Make verbs do the work. Every sentence earns its place. Vary the cadence. Grade every claim to its evidence.

**Whose voice — two cases, opposite failure modes:**

**The test:** Case B applies **only** when you wrote every sentence in the passage in this session. Anything else — including a passage you drafted that the user has since edited — is Case A. If provenance is unknown, it is Case A.

- **Case A, the draft is a human's.** The voice to protect is the one in the draft. Note three to five concrete signals first (sentence length, contraction habit, favored connectives, hedging level, humor). Make the **minimum effective edit**. Over-editing is the failure mode here.
- **Case B, the agent is drafting from scratch.** There is no prior voice to protect, so "preserve the voice" would license the slop. **Under-editing is the failure mode.** Apply §3-§6 in full.

In both cases: facts and artifact structure are untouchable, and nothing is invented to patch a hole a cut opened.

## 8. Pass/fail checklist

**Procedure only.** Do not re-ask §3-§7 as two dozen separate questions — that is the duplication this file exists to prevent.

Score six dimensions **PASS / PARTIAL / FAIL / N/A**. For anything that is not a clean PASS, name the specific word, pattern ID, or rule.

| # | Dimension | Source |
|---|-----------|--------|
| 1 | Banned words | §3 — any occurrence is FAIL |
| 2 | Padding words | §4 — cite the word; **PARTIAL at worst, never FAIL** |
| 3 | Prose patterns | §5 — cite the P-ID |
| 4 | Prose formatting | §6 — cite the F-ID; §2 carve-out validity is scored here |
| 5 | Substance and voice | §7 — concrete, specific, claims graded to evidence |
| 6 | Absolute rules and your own rules | `CLAUDE.md` Absolute Rules, plus the "Your own rules" section below |

**No double-counting.** Score under dimension 5 only what no P-ID covers. Anything with a P-ID belongs to dimension 3.

**N/A** is required, not optional, for any check needing an input you do not have — comparing against a pre-edit source you were not given, or asserting a *process* rather than an observable property of the artifact. It also applies when the artifact contains no passage the dimension can reach, and to dimension 6 whenever both rule sources are empty (as they ship). **PASS means the dimension applied and found nothing.** Recording an unreachable check as PASS is a vacuous PASS.

**Two output rules, about the report and not the draft:** never assign a slop score, and never state or imply that a passage was AI-written. Detectors are not in this loop and their verdicts cannot be checked. **Name the defect, never the author.**

## Your own rules

Nothing here yet. When empty, dimension 6 of §8 scores N/A on the "your own rules" half.

<!-- Personal taste goes here, not above. These are configurable house rules, not universal craft.

EXAMPLE ONLY - NOT AN ACTIVE RULE. Delete or replace. Shown to demonstrate the shape
a rule of taste takes; it is not in force unless you move it above this comment.

  EXAMPLE - Rule: Never use the em dash. Use a comma, a colon, or two sentences.
  EXAMPLE - Before: The launch slipped - again - because staging was down.
  EXAMPLE - After:  The launch slipped again, because staging was down.
  EXAMPLE - Enforcement: a single leak is a failure. Exception: verbatim quotes.

Other rules of taste: spelling locale (color / colour), Oxford comma, capitalizing Product Manager,
exclamation marks. A must-never that cannot be missed on any output belongs in the CLAUDE.md
Absolute Rules zone instead - that file is always in context. -->

## Changelog

- **2026-07-26** — Created. Consolidated the 14-word tripwire carried identically in `references/protocols/skill-evals.md`, `templates/skill-evals-template.md`, and all 87 `evals.md` (no drift found between them) plus the 8-word commented example previously in this file, into the 29-word §3 list. The `writing-style-*.md` files carried no word lists to merge — their per-audience phrase examples are register and stay where they are. §5 adapted from `petergyang/no-ai-slop`. **Deliberate divergences from upstream, do not restore on a future reconciliation:** P13 is delete-only (upstream permits rewriting the kicker); §4 is capped at PARTIAL; the N/A verdict and the no-slop-score / no-authorship-claim rules in §8 are additions.
- **2026-07-26** — Hardened after two adversarial verification runs (one scoring this file against its own §8, one applying it to a draft seeded with 32 known defects across all tiers). Both independently found §4 had no scoring home; §8 now has six dimensions, not five. Other fixes, each closing a place two agents following this file would diverge: the **mention-vs-use** exemption in §3 (without it this file's own §3 list fails §3); **P18** added for prose contradicting the artifact's own tables — the seeded draft's worst real-world defect and the one the catalog was blindest to; the **overlap rule** and per-instance counting in §5; the **carve-out list is now the grant** (the previous "a skill claiming a carve-out states it in its own file" clause voided all six carve-outs, since none of the six declares one — verified); the **F2 vs §2 scaffolding tiebreaker**; the **Case A/B provenance test**; the **keep-test** no longer turns on "rhythm changed", which every deletion satisfies; the false-positive exemptions in §5, including the blameless-passive exception that `/post-mortem` depends on; and the no-double-counting rule between dimensions 3 and 5. The "Your own rules" worked example is now marked EXAMPLE ONLY — in raw text it read as a live em-dash ban. **This file is 145 lines against a generic layer-1 ceiling of 130.** The ceiling was wrong for a catalog standard, not the file; `references/protocols/prompt-architecture.md` §3 now carries a dedicated row (target 130, ceiling 160) with the reasoning.
