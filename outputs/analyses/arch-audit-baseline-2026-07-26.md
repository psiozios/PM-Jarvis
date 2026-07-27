# Prompt-Architecture Baseline Audit — 2026-07-26

Ten check classes from `references/protocols/prompt-architecture.md` §5, run across the whole tree **before any skill was edited**. This is the before-picture every correction pass is measured against.

## Scope

| Surface | Count |
|---------|-------|
| Skills (`.claude/skills/*/SKILL.md`) | 87 |
| Eval files (`evals.md`) | 87 |
| Skill memory files (`skill-memory.md`) | 87 |
| Always-on core (`CLAUDE.md`) | 1 |
| Layer-1 files (`references/`, `references/protocols/`, `config/`) | 15 |
| Routine prompts (`routines/*/SKILL.md`) | 1 |
| Templates | 5 (`skill-template.md` new this round) |

**Excluded:** `all-skills.md` (a generated 38,896-line concatenation of all 87 skills — see F-14), `outputs/`, `templates/knowledge/` (third-party CSV/MD assets), `context-library/` content files.

## Baseline totals

| Metric | Value |
|--------|-------|
| Total lines across all `SKILL.md` | **38,279** |
| Mean `SKILL.md` | **440** lines |
| Over ceiling (150) | **73 of 87** |
| Over target (120) | **80 of 87** |
| Within ceiling | **14 of 87** (the automation-layer tier) |
| Largest | `connect-mcps` 1,281 · `meeting-notes` 1,058 · `prd-draft` 1,028 · `decision-doc` 1,002 · `daily-plan` 971 |
| Frontmatter description chars (loaded **every session**) | **13,099** (~3,270 tokens) |
| Descriptions over ceiling (350) | **1** |
| Descriptions under 100 chars (too vague to route on) | **35** |
| Always-on core | 178 lines (163 at round start) |
| `evals.md` | 66 lines each, all 87 — perfectly uniform |

## Findings by severity

**Blocker 6 · High 10 · Medium 11 · Low 5 — 32 total.**

### Blocker

| Rule | File : line | Finding | Fix |
|------|-------------|---------|-----|
| B-1 | `config/house-style.md` (pre-round) + all 87 `evals.md`:E5 | **The house-style check was a no-op in all 87 skills.** The file existed but every rule in it was commented out, and E5 reads "Follows any **active** rules". Active rules = the empty set, so E5 was a vacuous PASS everywhere. Functionally identical to an auto-PASS clause, reached by a different route. | Standard 1 written; E5 renormalized. **Closed this round.** |
| B-2 | C7 · `.claude/skills/code-first-draft/SKILL.md:37,72` | `context-library/technical/codebase-overview.md` — the `technical/` directory **has never existed**, and line 72 instructs the agent to *create* it, which also violates the core's file-creation rule ("never to `context-library/`"). Two defects, one line. | Repoint to `outputs/`. Do **not** create the directory. |
| B-3 | C7 · `.claude/skills/weekly-review/SKILL.md:629` | `context-library/personal-context/lessons-learned.md` — `personal-context/` is not a directory. The core's routing table uses the **file prefix** `context-library/personal-context-*.md`. One concept, two conventions, and the skill proposes writing to `context-library/` which the core forbids. | Repoint to the real convention; destination `outputs/`. |
| B-4 | C9 · all 81 skills with a Context Routing section | **Zero of 87 skills point at `references/mcp-routing.md`.** Every routing table names local files only. The live-source layer is entirely unreferenced from the skills — the protocol exists and nothing routes to it. | Add one pointer line with a trigger per skill. |
| B-5 | C10 · `experiment-metrics/SKILL.md:16-27` vs `feature-metrics/SKILL.md:92-131` | **Two skills teach STEDII with four of six letters different.** `experiment-metrics` (sourced, credits Aakash Gupta, URL at :379): Sensitive / Timely / **Efficient** / **Debuggable** / **Interpretable** / **Isolated**. `feature-metrics` (unsourced backronym): Sensitive / Timely / **Easy to Understand** / **Directional** / **Implementable** / **Independent**. **`prd-draft` cites both inside one file** — `:56` and `:646` route to `feature-metrics`, `:287` to `experiment-metrics`, treated as synonyms. Their descriptions are near-identical ("STEDII framework" + "trustworthy" + "experiment metrics" in both), which is what made the collision invisible. Seven more skills route to one or the other unaware of the split. **This is a factual contradiction, not untidiness — it outranks every duplication finding.** | `experiment-metrics` owns STEDII (sourced expansion wins). `feature-metrics` keeps its own artifact and uses the framework as a screen. Differentiate both descriptions. |
| B-6 | C7 · `code-first-draft/SKILL.md:37,72` + `prototype-feedback/SKILL.md:33` | **One concept, three destinations.** `context-library/technical/codebase-overview.md` is read at `code-first-draft:37`, *created* at `:72` (violating the core's write-zone rule), referenced as a directory at `prototype-feedback:33` — and **the core routes it nowhere**: `CLAUDE.md` has no row for technical/codebase context and `file-creation-rules.md` has no `technical/` row. Meanwhile `/explore-codebase` writes the genuinely equivalent artifact to `outputs/analyses/explore-*.md`, and neither skill references the other. Supersedes and expands B-2. | `/explore-codebase` owns codebase context. Repoint both readers; delete the create-block. |

### High

| Rule | File : line | Finding | Fix |
|------|-------------|---------|-----|
| H-1 | Rule 1 · C4 · 87 files | **The `## Formal Eval` block is pasted into all 87 skills**, 73 in the full 12-line form, and its own last line points at `references/protocols/skill-evals.md` — the protocol that already specifies it. Pointer plus paste, rule 1 in its purest form. ~950 lines. | Collapse to three lines; keep only the non-obvious facts inline. |
| H-2 | Rule 1 · H-1 wording | The pasted block opens "**Runs automatically after every skill invocation.** After generating output:" — an instruction that invites being skipped once the user already holds the deliverable. No hard gate anywhere in the tree. | Open with "Do not present the output until this has run." |
| H-3 | Rule 4 · C3 · 73 files | **73 of 87 skills are over the 150-line ceiling**, mean 440. Only one skill in the repo (`second-brain`) has a `references/` subdirectory, so the extraction mechanism rule 4 assumes is essentially unused. | Progressive disclosure on the monoliths. Extraction only. |
| H-4 | Rule 7 · C6 · 81 files | **The sources-to-read concept carries six spellings**: `Context Routing Logic (Internal - for Claude)` ×47, `Context Routing Logic` ×14, `Context Routing Strategy` ×11, `Context Routing` ×7, `Context Routing Logic (Internal)` ×2, `Context Routing (Check Before Wireframing)` ×1. | Canonicalize to `## Context Routing`. |
| H-5 | Rule 7 · C6 · 36 files | **36 skills carry two or more chaining blocks** under different spellings, able to offer contradictory next steps. `## Cross-Skill Links` ×87 (canonical) plus `### Cross-Skill Integration` ×20, `## Next Steps` ×15, `### Related Skills` ×14, and six more variants. `meeting-agenda` has 6; `meeting-notes` 5. | One canonical block per skill. |
| H-6 | Rule 8 · C8 · 38 files | **38 of 87 skills exceed 20 `##` headings.** `meeting-agenda` 64, `status-update` 62, `decision-doc` 48, `prd-draft` 47, `meeting-notes` 43. Outlines do not read as tables of contents. | Fence template bodies; extract; demote. |
| H-8 | C10 · `prd-draft/SKILL.md:960-1005` | **A mode inside a large skill that is another whole skill.** `--brief` reproduces `/prd-lite` section for section (Problem / Hypothesis / Why Now / rough solution / Business Case with the same four fields in the same order / Risks / Next Step), with the **same explicit 300-400 word budget** and the same output directory. `prd-draft` never mentions `prd-lite` anywhere, and `:1002` has the mode **escalate to its own containing skill**. | Delete the mode; keep a two-line alias to `/prd-lite`. |
| H-9 | C10 · `.claude/skills/code-review/` | **Local skill collides with two harness built-ins that route to its name.** Built-in `/review` says "for your working diff use `/code-review`" and plugin `simplify` says "use `/code-review` for that" — both handoffs now land on this repo's PM-oriented 8-dimension skill that writes `outputs/analyses/` and reads `context-library/prds/`. Its `### 6. Security` dimension also duplicates built-in `/security-review` with no cross-reference either way. | Boundary declaration at the top plus a `/security-review` handoff. |
| H-10 | C10 · 6 pairs | **Load-bearing reciprocity gaps** — A declares a sequencing or *write* dependency on B and B has no idea. Worst two: `chat-ingest` says "`second-brain` `ingest` mode does the actual wiki write" but `second-brain`'s writers list omits it; `prd-lite` says it "feeds into `/prd-draft`" but `prd-draft` never mentions it and ships the competing mode in H-8. Also `backlog-groom`→`sprint-planning`, `refinement-prep`→`sprint-planning`, `weekly-review-fill`→`weekly-review`, `monthly-review-fill`→`weekly-review`. | Add the reciprocal line in each B. |
| H-7 | C2 · 30 files | Frontmatter is non-uniform. Missing `user-invocable` on 14 skills, missing `disable-model-invocation` on 16. Unknown keys: `version` and `modifies-workspace` (`connect-mcps`). **Misspelled key: `disable-model-invocable`** (`sales-battlecard`) — silently inert. | Uniform allowed-key set on all 87. |

### Medium

| Rule | File : line | Finding | Fix |
|------|-------------|---------|-----|
| M-1 | C2 · 35 files | **35 descriptions are under 100 chars and too vague to route on** — "Initial feature implementation" (30), "Set next week's priorities" (26), "Generate PM daily plan with context" (35), "Comprehensive product launch planning" (37). These are what the model reads when deciding to reach for a skill unprompted. **The distribution is bimodal and only one end is a length problem.** | Right-size both directions, then test cold. |
| M-2 | C2 · `second-brain` | Only description over the 350-char ceiling (445). Carries mode lists and routing logic that already live in the body. | Cut method, keep triggers. |
| M-3 | C5 chaining · `daily-plan/SKILL.md:897` | `/daily-review` does not resolve — self-annotated "(If created)". | Drop the target. |
| M-4 | C5 chaining · `weekly-plan/SKILL.md:438` | `/quarter-plan` does not resolve — self-annotated "(If exists)". | Drop the target. |
| M-5 | C3 · `CLAUDE.md` | The core is **178 lines against the 170 ceiling** set this round. The skills category table (13 lines) is a lookup table by the standard's own definition. | Extract the category table; rules and routing stay inline. |
| M-7 | C10 · `impact-sizing/SKILL.md:262-300` vs `opportunity-sizing/SKILL.md:58-90` | TAM/SAM/SOM taught twice — same three definitions, same Top-Down/Bottom-Up split, same "use both, investigate if far apart" guidance. Overlap is partial, not total: `opportunity-sizing` wraps it in problem validation, willingness-to-pay and an investment thesis. Neither links the other. | `opportunity-sizing` owns TAM/SAM/SOM; pointer from `impact-sizing`. |
| M-8 | C7 · `weekly-plan/SKILL.md:407` | `context-library/strategy/OKRs.md` — phantom file no skill produces. Ten skills correctly glob `context-library/strategy/*.md`; `/okr-planning` writes `okrs-[quarter]-[date].md`. A user following this line literally creates a filename nothing expects. | Point at the directory or at `/okr-planning`. |
| M-9 | C7 · 5 refs | `context-library/research/interviews/`, `research/interview-guides/`, `research/personas*.md` — three phantom subdirectories under a flat `research/`. The two processing skills write to `outputs/research-synthesis/` with **two different naming conventions**. | Flatten the refs; unify the two conventions. |
| M-10 | C7 · `status-update/SKILL.md:820` | `context-library/meetings/status-updates/` phantom archive target. | Repoint. |
| M-11 | Rule 9 · `metrics-framework/SKILL.md:21,664` | Writes `outputs/metrics-framework-[date].md` at the `outputs/` root, outside the taxonomy in `file-creation-rules.md`. | Route to `outputs/analyses/`. |
| M-6 | Rule 9 · `all-skills.md` | A tracked, generated 38,896-line concatenation of every skill — a full second copy of the entire skill tree in the repo. Referenced once, in passing, by `setup/installation-guide.md:193`. It goes stale the moment any skill is edited, and it doubles every grep in the tree. | Out of scope this round; flagged for a decision (regenerate, gitignore, or delete). |

### Low

| Rule | File : line | Finding | Fix |
|------|-------------|---------|-----|
| L-1 | C7 · `references/protocols/knowledge-capture.md:26` | Example path `context-library/decisions/auth-approach-2025-q2.md` carries a stale quarter. Illustrative, inside a quoted proposal. | Cosmetic. |
| L-2 | C7 · `weekly-plan/SKILL.md:407` | `context-library/strategy/OKRs.md` does not exist, but the parent directory does and the line is a "fill this out" instruction, not a read. | Cosmetic. |
| L-3 | C6 · arrow glyph | Mixed `->` and `→` across chaining lines. | Normalize on canonicalization. |

## Not findings — checked and correct by design

Recorded so this is not re-litigated next run, and so nobody later "fixes" a deliberate choice.

- **C1 three-file completeness is clean.** All 87 skills have `SKILL.md`, `evals.md`, and `skill-memory.md`. Set difference is empty. No files to create.
- **The 14-word banned list has zero drift.** It is carried identically in `references/protocols/skill-evals.md`, `templates/skill-evals-template.md`, and all 87 `evals.md`. **This contradicts the round's expectation of divergent lists needing a merge — there was one list in three places, not many lists.** Consolidation was therefore additive (14 → 29) rather than reconciliatory.
- **The `writing-style-*.md` files carry no banned-word lists.** Their `Avoid:` lines are per-audience *phrase* examples ("Avoid: 'Leverage our robust API infrastructure'") — register, not word bans. Nothing to cut; they stay.
- **The predicted mass protocol-paste does not exist here.** Probes for `READ FREELY, WRITE ON CONFIRM`, `Never auto-write`, `degrade gracefully`, `Context Acquisition Protocol`, and `freshness-provenance` return **zero hits** across all 87 skills. The one shared protocol gate that is referenced, `commitment-gate`, appears in 5 skills as a **pointer with a per-skill trigger line and no paste** — already correct. Pass C3 is a no-op in this repo.
- **All 15 layer-1 files have ≥2 referrers.** The lowest are `capabilities.md`, `file-creation-rules.md`, `mcp-routing.md`, `context-acquisition.md`, `sub-agents.md` at 2 each. No unreachable layer-1 file exists — contrary to the round's expectation. The two standards added this round were wired into `CLAUDE.md` at creation so they do not become the first.
- **No orphan `###` headings.** No file has a `###` preceding its first `##`. The guard already holds; the canonicalization pass must not break it.
- **`evals.md` uniformity.** All 87 are exactly 66 lines with identical frontmatter keys (`skill`, `archetype`, `eval-version`, `last-updated`). No drift.
- **`wiki/index.md` and `wiki/log.md`** are created at runtime by `/second-brain` under `context-library/second-brain/{slug}/wiki/`. Not dangling.
- **`outputs/**/YYYY-MM-DD-*.md` paths** are filename patterns, not references. Not dangling.
- **Emoji and symbol use in `/execution-plan`, `/journey-map`, `/napkin-sketch`, `/prototype`, `/slack-message`, `/content-marketing`** is functional inside those artifacts. Named as carve-outs in `config/house-style.md` §2 and delegated to the owning skill. Flagging them is a false positive.

## Corrections made to the standards from this audit

Per the round's rule: correcting the standard from evidence is the standard working.

1. **`prompt-architecture.md` §4** — the retired-spellings column was built by grepping this tree, not assumed. Six live spellings of Context Routing and ten of chaining were found and recorded; several (`(Internal - for Claude)`, `Context Routing (Check Before Wireframing)`, `## Follow-up Actions`) would not have been guessed.
2. **`prompt-architecture.md` §3** — the `SKILL.md` ceiling was derived from the fourteen automation-layer skills (101-131 lines, mean 118), not by analogy. Target 120, ceiling 150.
3. **`house-style.md` changelog** — records that no banned-list drift was found, so a future reconciliation does not go looking for merges that never happened.
4. **C5 probe list** — five of the eighteen candidate probes return zero hits repo-wide and were dropped rather than published. An untested probe list is a fake audit.
5. **Open against the standard itself:** M-5 — the core is 8 lines over the ceiling this round set for it. Either the extraction in pass C7 closes it or the ceiling is wrong; that is resolved in C7 and recorded there, not assumed away here.

---

# Re-audit delta — 2026-07-26, after the correction passes

All ten check classes re-run with **fresh greps against the live tree**, not against the baseline's line numbers. Re-grepping is what found the references the baseline missed (see New Blockers below).

## Findings by severity, before and after

| Severity | Baseline | After | Closed | Open |
|----------|----------|-------|--------|------|
| Blocker | 6 | 0 | 6 | 0 |
| High | 10 | 2 | 8 | 2 |
| Medium | 11 | 3 | 8 | 3 |
| Low | 5 | 2 | 3 | 2 |
| **Total** | **32** | **7** | **25** | **7** |

## Numbers that moved

| Metric | Baseline | After |
|--------|----------|-------|
| Total `SKILL.md` lines | 38,279 | 36,837 |
| Mean `SKILL.md` | 440 | 423 |
| Over the 150 ceiling | 73 | 72 |
| `evals.md` total lines | 5,742 | 5,307 |
| Frontmatter description chars (every session) | 13,099 | 23,341 |
| Descriptions over ceiling | 1 | 0 |
| Descriptions under 100 chars (unroutable) | 35 | 0 |
| Always-on core | 178 | 164 |
| Skills pointing at the live-source protocol | 0 | 82 |
| Spellings of "sources to read" | 6 | 1 |
| Files with a `## Formal Eval` hard gate | 0 | 87 |

**The description total went up 78%, on purpose.** This pass was mostly *lengthening* 52 descriptions that were too vague to route on, not trimming. The cost is roughly +2,560 tokens per session; the return is that the model can now tell `backlog-groom` from `refinement-prep` without opening either file. Recorded as a deliberate trade, not an accident.

## Every Blocker and High, named

**Blockers — all 6 closed.** B-1 house-style no-op (standard written, E5 renormalized across 87). B-2 and B-6 phantom `context-library/technical/` (repointed to `/explore-codebase`; the write-zone violation deleted rather than satisfied by creating the directory). B-3 phantom `personal-context/` directory (repointed to the core's real file-prefix convention). B-4 live-source layer unreferenced (82 skills now carry the pointer with a trigger). B-5 STEDII contradiction (`experiment-metrics` named owner, `feature-metrics` reduced to a screen, `prd-draft`'s three references repointed, both descriptions differentiated, ownership recorded in `references/skill-categories.md`).

**Highs — 7 closed, 3 open.**

Closed: H-1 eval boilerplate (87 collapsed, 485 lines out). H-2 no hard gate (87 now open "Do not present the output until this has run"). H-4 six routing spellings (one). H-7 frontmatter (87 uniform on four keys; `disable-model-invocable` typo fixed; `version` and `modifies-workspace` dropped with the constraint moved into the description). H-8 `prd-draft --brief` (deleted, two-line alias to `/prd-lite`). H-9 `code-review` collision (boundary declaration naming `/review`, `/security-review`, `/simplify`). H-3 partially — see below.

**OPEN — H-3, progressive disclosure. 72 of 87 skills remain over the 150-line ceiling.** One monolith was extracted as proof of method: `decision-doc` 998 → 602, with 404 lines moved to two reference files behind triggered pointers, and parity verified mechanically by reconstructing the original from the new `SKILL.md` plus the extracted bodies (diff: two added blank lines, zero content). **Shortening a file does not push it under a line** — the other 71 need the same treatment. The extractions that would recover the bulk, in order: `connect-mcps` 1,273 (troubleshooting trees and per-tool catalogs only — every workflow step stays inline, since the skill exists so the user can connect a tool from `SKILL.md` alone), `meeting-notes` 1,054, `prd-draft` 977, `daily-plan` 961, `status-update` 919, `meeting-agenda` 864, `prd-review-panel` 834. Those seven alone are ~6,900 lines, roughly 18% of the tree.

**H-5 chaining consolidation — CLOSED.** All 87 skills now carry exactly one `## Cross-Skill Links` block (84 real, 3 sanctioned exceptions stating their reason inline: `connect-mcps` setup utility, `learning-mode` terminal sink, `routine-responder` chain-is-its-routine). Zero retired spellings remain. 512 `/skill-name` references re-checked, zero dead. Net −500 lines.

**The real scale was 52 skills with multiple blocks, not the 36 the baseline reported.** The baseline grepped heading spellings only and missed **45 skills carrying an inline `**Cross-Skill Links:**` block inside their `## Context Routing` section** — in most of the 26 generic-block skills that inline block held the *only* real chains in the file. Two baseline counts were also inflated by in-fence template headings: `meeting-agenda` has one block, not six (the other five are `### [40-45 min] Next Steps` agenda timeboxes), and `meeting-notes` has three, not five. 20 of the 21 `## Next Steps` occurrences are inside fences and were correctly left alone.

**A fifth spelling surfaced only during application**, after a stale-line-number crash forced a rewrite to content-addressed editing: `## Integration With Other Commands` (×3) and `## Integration With Existing Skills` (×1) were live rival "what next" surfaces neither the baseline nor the plan had caught. Per the extraction-only rule they were **retitled, not deleted** — to `## Handoff Details` and `## What Each Skill Files And Pulls` — keeping every line while removing them from competition as chain lists.

**Three `## Cross-Skill Links` headings were corrupted by this round's own C9 heading sweep** (`create-tickets`, `feature-request-analysis`, `prd-lite` — the sweep renamed unrelated sections onto the canonical name, two of them inside fenced templates). Each was restored to its true heading and given a real chaining block. This is the C9 failure mode the round warned about, caught because C5 re-grepped rather than trusting the earlier pass.

**OPEN — H-6, outline hygiene. 38 of 87 exceed 20 `##` headings — unchanged from baseline, and it briefly improved to 37 before rising back.** The rise is a deliberate consequence of extraction-only: C5 preserved 22 `## Where Files Go`, 11 `## Link to Other Work`, 3 `## Key Questions to Revisit` and 9 framework-credit footers by promoting them to their own headings rather than deleting them. Trading a heading count for zero content loss is the correct call under this round's rules, and it means H-6 cannot close before H-3 does. This is now known to be almost entirely **unfenced output-template bodies**, not real outline entries — 8 files carry duplicate `##` headings, which is the signature. It resolves as a side effect of H-3, as it already did for `prd-draft`.

## New Blockers the baseline never listed, caught by re-grepping

- **`connect-mcps` referenced a `CLAUDE.md` → "MCP Integrations" section that has never existed**, on three separate lines. The baseline's C7 pass only globbed backticked `.md` paths, so a prose reference to a *section* slipped through. Repointed to `references/mcp-routing.md`.
- **An unclosed code fence in `prd-draft`** left the AI-PRD template open, swallowing every subsequent section into a code block. The baseline had recorded the symptom inverted — as unfenced template bodies. Closing the fence properly resolved both. A tree-wide fence-balance check now runs clean on all 87.
- **Three skills asked the agent to judge whether prose "sounds like AI generated it"** (`prd-draft` ×2, `status-update` ×1), which the new standard prohibits outright — detectors are not in the loop and their verdicts cannot be checked. Rewritten to name the defect, never the author.

## Further corrections to the standards, from re-audit evidence

4. **`prompt-architecture.md` §4 canonical table — five rows rewritten.** The first draft named spellings the tree barely used. Correcting it by measurement rather than forcing 63 files into `## Fit` is recorded inline in that section.
5. **§3 size budgets — the layer-1 row split into Protocol (80/130) and Standard (130/160).** Both standards written this round breached the single generic ceiling while every protocol file sits at 36-95 with room. A protocol describes one process; a standard carries catalogs that must stay resident. The rows split because the number was wrong, not because the files were.
6. **M-5 resolved as predicted, not assumed away.** The core was 8 lines over its own new ceiling. Extracting one lookup table (the skill-category breakdown, now `references/skill-categories.md`) brought it to 164/170. Every rule statement, stakes line, and attribution stayed inline. The chaining instruction was *strengthened* on the way past — from "check its Cross-Skill Links and offer" to "read it and **actively offer** the next step whose trigger the current run just met" — because a passive phrasing was the regression risk the round warned about.

## Still not findings

Everything in the baseline's "Not findings" section stands. Adding:

- **`all-skills.md` is now definitively stale** — it is a generated 38,896-line snapshot of the pre-round tree. It was already flagged (M-6) and is deliberately untouched: regenerating it would double this round's diff for no review value. It needs a decision (regenerate, gitignore, or delete) as its own task.
- **`/review`, `/security-review`, and `/simplify`** appear in `code-review`'s new boundary declaration and resolve to harness built-ins, not local skills. Intentional, not dangling.
