# Skill Eval Protocol

**Principle: EVAL ON EVERY RUN.**

Every skill invocation ends with a formal eval pass. A separate agent evaluates the output in a clean context window. Failures loop back for revision until the output passes all checks.

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
4. Eval agent evaluates each criterion independently → PASS / FAIL / PARTIAL
5. Eval agent returns a results table to the original agent
6. **If any FAIL:** eval agent includes specific remediation instructions → original agent applies fixes → re-submits for eval
7. **Loop until zero FAILs**
8. Final results appended to the Eval Results Log in `evals.md` (keep last 5 runs)

### Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps — eval agent documents what's missing
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if the eval agent documents what's missing and it's acknowledged.

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

## Universal Checks (apply to ALL archetypes)

These checks appear in every skill's evals.md regardless of archetype:

- **No AI slop**: Zero instances of: delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm
- **House style compliance**: Follows any active rules in `config/house-style.md`
- **Human-sounding**: Varied sentence lengths, contractions used naturally, no formulaic paragraph openings
- **Context-grounded**: References specific data from context sources — not generic placeholder language

## Skill Archetypes

| Archetype | When to use | Eval emphasis |
|-----------|-------------|---------------|
| **Document-Writer** | Skills that produce written documents (PRDs, strategies, decision docs) | Structure, Voice, Completeness, Specificity |
| **Analysis** | Skills that quantify, model, or assess (impact sizing, retention, pricing) | Methodology, Evidence, Confidence, Actionability |
| **Research-Synthesis** | Skills that aggregate and interpret research data | Source fidelity, Bias, Completeness, Actionability |
| **Workflow-Orchestration** | Skills that plan, schedule, or coordinate (daily plans, sprints, launches) | Context-awareness, Prioritization, Realism, Integration |
| **Communication-Draft** | Skills that produce messages for specific audiences | Audience-fit, Tone, Brevity, Actionability |
| **Code-Technical** | Skills that produce or review code, tickets, or technical specs | Correctness, Convention-adherence, Coverage, Traceability |

### Archetype Eval Guidance

**Document-Writer:**
- Structure: Required sections present, length within stage guidance, filename convention followed
- Voice: No AI slop words, matches house style, reads as human-authored, natural sentence variation
- Substance: Uses real data/quotes from context-library, specific names/numbers, testable hypotheses
- Completeness: All stage-required sections filled, cross-skill links offered, output saved correctly

**Analysis:**
- Structure: Methodology stated, framework applied correctly, output format matches template
- Quality: Confidence levels on every assumption, math shown not just conclusions, sensitivity analysis present
- Substance: Grounded in context-library data, de-risking actions specific/actionable, tied to strategic goals
- Completeness: All requested scope covered, edge cases acknowledged, next-step recommendations

**Research-Synthesis:**
- Structure: Sources cited with dates, themes organized by pattern not chronology
- Quality: Internal data checked before external, confidence levels on claims, bias flagged
- Substance: Verbatim quotes preserved, contradictions surfaced, insights are non-obvious
- Completeness: All sources in routing table checked, gaps explicitly identified

**Workflow-Orchestration:**
- Structure: Correct output path, date/time-aware, priority framework applied
- Quality: Context-library consulted, stakeholder profiles used, realistic capacity
- Substance: Priorities tied to weekly/quarterly goals, conflicts flagged, MCP data included or degradation noted
- Completeness: All routing table sources checked, next-skill nudge offered

**Communication-Draft:**
- Structure: Channel-appropriate length, clear CTA, proper formatting for medium
- Voice: Matches audience writing style, no corporate jargon, human-sounding
- Substance: Specific names/dates/numbers, grounded in meeting context or PRD
- Completeness: All stakeholders addressed, tone matches persona

**Code-Technical:**
- Structure: Follows codebase conventions, correct file paths, proper test structure
- Quality: No placeholder TODOs, complete implementations, edge cases handled
- Substance: PRD requirements mapped to code, accessibility included for UI
- Completeness: Tests passing, coverage target met, summary document complete

## Creating Evals for New Skills

When creating a new skill (via `anthropic-skills:skill-creator` or manually):

1. Determine the skill's archetype from the table above
2. Generate `evals.md` using the archetype guidance and universal checks
3. Include 8-12 checks across the 4 categories, tailored to the skill's specific purpose
4. Generate `skill-memory.md` (starts with empty Entries section)
5. Add the "Formal Eval" section to SKILL.md after Output Quality Self-Check
6. Add `skill-memory.md` to the skill's Context Routing Logic table

## Skill Memory Protocol

`skill-memory.md` follows the knowledge-capture protocol: propose, don't auto-write.

At the end of a skill run, if a durable learning about the skill itself was discovered:

1. Propose a specific entry (2-3 sentences, dated)
2. Wait for user confirmation
3. Prepend to the Entries section of `skill-memory.md`
4. If entries exceed 20, consolidate oldest into Archived Patterns

**What belongs in skill-memory.md:**
- Patterns that produce better output
- Edge cases the skill handles poorly and workarounds
- Context sources that proved especially valuable or misleading
- Structural improvements that worked well

**What does NOT belong:**
- Eval pass/fail results (those go in `evals.md` results log)
- User preferences (those go in `memory/`)
- Feature-specific context (that goes in `context-library/`)
