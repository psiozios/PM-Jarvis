# Skill Eval Protocol

**Principle: EVAL ON EVERY RUN.**

Every skill invocation ends with a formal eval pass. A separate agent evaluates the output in a clean context window. Failures loop back for revision until the output passes all checks.

**The loop is the backstop, not the mechanism.** `config/house-style.md` is applied *before* drafting — the cheapest slop to remove is the sentence never written. An eval that catches a banned word has already cost a rewrite the drafting agent could have avoided by reading the standard first. Treat a house-style FAIL as evidence the standard was not read, not as the standard working.

## Skill File Structure

Each skill directory contains three files:

| File | Purpose | Created with skill? |
|------|---------|-------------------|
| `SKILL.md` | Skill definition, workflow, informal self-check | Yes |
| `evals.md` | Formal pass/fail evaluation criteria (8-12 checks) | Yes |
| `skill-memory.md` | Living improvement journal | Yes (starts empty) |

## Separation of Concerns

| Layer | File | Analogy | When |
|-------|------|---------|------|
| Informal self-check | `SKILL.md` | Pilot checklist | Before delivery, same agent |
| Formal eval | `evals.md` | Quality inspector | After output, separate agent |
| Improvement journal | `skill-memory.md` | Team retro notes | After notable runs, on confirm |

## Running Evals

### Automatic Flow (every skill invocation)

1. Original agent produces skill output and runs the informal Output Quality Self-Check in SKILL.md
2. Original agent spawns a **separate eval agent** with a clean context window
3. Eval agent reads:
   - The skill output file
   - The skill's `evals.md`
   - `config/house-style.md` (for voice checks)
   - **The sources the output cites**, where a check turns on whether the output is grounded in them
4. Eval agent evaluates each criterion independently → PASS / FAIL / PARTIAL
5. Eval agent returns a results table to the original agent
6. **If any FAIL:** eval agent includes specific remediation instructions → original agent applies fixes → re-submits for eval
7. **Loop until zero FAILs**
8. Final results appended to the Eval Results Log in `evals.md` (keep last 5 runs) — see "Legible Eval Results Log" below for what the log entry must contain beyond pass/fail counts

### Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps — eval agent documents what's missing
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if the eval agent documents what's missing and it's acknowledged.

## Legible Eval Results Log

The Eval Results Log at the bottom of each `evals.md` is more than a running tally — it must stay legible enough that a future run can tell *what broke and what fixed it*, not just how many checks passed.

Each row keeps the base columns (Date, Pass, Partial, Fail) and extends the Notes column (or adds columns) to carry:

- **Which check IDs failed** (e.g. "E8, E11")
- **What remediation was applied** (one clause — what changed between the failing attempt and the passing one)
- **The re-check result** (confirmed pass on re-submission, or still-partial with what remains)

A worked PASS-after-fix row is in `references/eval-archetypes.md`.

Keep the last 5 runs, same as before — the enrichment is in what each row *contains*, not how many rows are kept.

## Eval Categories

Every `evals.md` has 4 categories. Specific checks within each category depend on the skill's archetype.

### Category 1: Structure & Format
Does the output have required sections, correct naming, appropriate length?

### Category 2: Quality & Voice
Does it avoid AI slop, match house style, sound human-authored?

### Category 3: Substance & Specificity
Is it grounded in real context, specific not generic, actionable?

### Category 4: Completeness & Context
Does it cover all requirements, use available context sources, offer next steps?

## Eval Versioning & Category Extension

Every `evals.md` carries `eval-version` (an integer) and `last-updated` in its frontmatter. The four base categories above (Structure & Format, Quality & Voice, Substance & Specificity, Completeness & Context) are the **floor, not the ceiling** — a skill is free to grow a fifth category once its judgment genuinely outgrows the four.

**When to bump the version:** Only when a skill's judgment grows a whole new *category* of check — not when a check is reworded or tightened within an existing category. Rewording E7's criteria stays at the same version; adding a whole new category with checks E13+ bumps `eval-version` from 1 to 2 and updates `last-updated`.

A worked fifth category, for a standing-radar skill, is in `references/eval-archetypes.md`.

## Universal Checks (apply to ALL archetypes)

These checks appear in every skill's evals.md regardless of archetype.

**The two universal writing checks are normalized — E4 and E5 below are the canonical wording.** They are identical in every `evals.md` and in `templates/skill-evals-template.md`. Do not reintroduce a local variant, and do not let either check drift into restating the `CLAUDE.md` absolute rules, which are scored separately.

- **E4 — No AI slop**: Zero banned words and zero slop patterns per `config/house-style.md`. The 14-word list carried inline in each `evals.md` (delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm) is a **fast tripwire, not the list** — the full 29-word §3 list and the P1-P17 pattern catalog govern. Passing the tripwire is not passing the check.
- **E5 — House style compliance**: Conforms to `config/house-style.md`, including any rules the user has set in its "Your own rules" section. The formatting rules (§6) apply to **prose only**, per the prose test in §2 — **artifact scaffolding is exempt by design, not a violation**. Template headings, table structure, checklists, status columns, ticket fields, and genuinely parallel lists are intentional structure; flagging them is a false positive.

**`config/house-style.md` is live and the check is real.** There is no auto-PASS. An eval agent that cannot read the file scores E5 **PARTIAL** and says so explicitly ("could not read `config/house-style.md`"). It never assumes compliance and never records a vacuous PASS. Use **N/A** only for checks needing an input the agent genuinely does not have — see §8 of the standard.

**E7 needs a fourth input, and for a long time it did not get one.** "Context-grounded" asks whether the output's names, numbers, and quotes come from the sources — a question the output cannot answer about itself. An agent handed only the output, the rubric, and the style file was scoring E7 from plausibility, which by `config/house-style.md` §8 is a vacuous PASS. So: **hand the eval agent the sources the output cites**, and it spot-checks the specific claims rather than the general impression. Where a source genuinely cannot be reached — a live tool the eval agent has no access to — E7 is **N/A with the reason named**, never PASS. A check that cannot run says it could not run.

- **Human-sounding**: Varied sentence lengths, contractions used naturally, no formulaic paragraph openings
- **Context-grounded**: References specific data from context sources — not generic placeholder language
- **Durability** (Document-Writer, Analysis, and Research-Synthesis archetypes — see `references/protocols/freshness-provenance.md`): No volatile point-in-time status is asserted as standing fact. Ephemeral state is either dated ("as of `<DATE>`"), routed to its live source, or absent — never baked into the document as if it were permanent
- **Source coverage** (any skill that reads a live source — see `references/protocols/source-preflight.md`): The output names which sources answered and, separately, any source that was unavailable with its reason. A source that never answered is never listed as swept, and its silence never kills a candidate. **A run where a source failed and the output does not say so is a FAIL**, not a PARTIAL — the reader has no other way to know

## Skill Archetypes

Six archetypes, each with its own eval emphasis: **Document-Writer**, **Analysis**, **Research-Synthesis**, **Workflow-Orchestration**, **Communication-Draft**, **Code-Technical**. The table, and what each one's four categories should actually check, is `references/eval-archetypes.md` — read it when creating a skill's `evals.md` or when deciding which archetype a skill is.

## Creating Evals for New Skills

When creating a new skill (via `anthropic-skills:skill-creator` or manually):

1. **Copy `templates/skill-template.md` to `.claude/skills/<name>/SKILL.md`** and follow the copy procedure in its header comment. The template carries the canonical section names, the size budget, and the never-restate rule — see `references/protocols/prompt-architecture.md` for the standard it enforces.
2. Determine the skill's archetype from the table above
3. Generate `evals.md` from `templates/skill-evals-template.md` using the archetype guidance and universal checks
4. Include 8-12 checks across the 4 categories, tailored to the skill's specific purpose
5. Generate `skill-memory.md` from `templates/skill-memory-template.md` (starts with empty Entries section)
6. Keep the `## Formal Eval` section the template ships, after `## Output Quality Self-Check`
7. Add `skill-memory.md` to the skill's `## Context Routing` table

## Skill Memory Protocol

The third file in every skill directory has its own protocol, including the feedback loop that carries a confirmed journal entry back into `SKILL.md` and `evals.md`: `references/protocols/skill-memory.md`. Read it when a run produces a durable learning about the skill itself.
