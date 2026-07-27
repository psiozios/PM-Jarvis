---
skill: SKILL_NAME
archetype: ARCHETYPE
eval-version: 1
last-updated: YYYY-MM-DD
---

# Evals: /SKILL_NAME

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | | |
| E2 | | |
| E3 | | |

### Quality & Voice

| ID | Check | Criteria |
|----|-------|----------|
| E4 | No AI slop | Zero banned words and zero slop patterns per `config/house-style.md`. Fast tripwire (not the list): delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Conforms to `config/house-style.md`. Formatting rules apply to prose only — artifact scaffolding (headings, tables, checklists, parallel lists) is exempt by design, not a violation |
| E6 | Human-sounding | Per `config/house-style.md` §5 P11 and §7 (cadence, contractions, no formulaic openings) |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | Specific over generic, per `CLAUDE.md` Output Philosophy — real names, numbers, and quotes from context, not placeholder language |
| E8 | Durability *(Document-Writer / Analysis / Research-Synthesis only — delete this row for other archetypes)* | No volatile point-in-time status is asserted as standing fact. Ephemeral state is either dated ("as of `<DATE>`"), routed to its live source, or absent — never baked into the document as if it were permanent. See `references/protocols/freshness-provenance.md`. |
| E9 | | |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | | |
| E11 | | |
| E12 | | |

<!--
OPTIONAL Category 5+: the four categories above are the floor, not the
ceiling. Only add a new category when the skill's judgment grows a whole
new dimension — not for a reworded or tightened check within an existing
category (that doesn't bump the version). When you do add one, bump
`eval-version` in the frontmatter and update `last-updated`. See
references/protocols/skill-evals.md, "Eval Versioning & Category Extension"
for the full rule and a worked example.

### Category 5: <NAME>

| ID | Check | Criteria |
|----|-------|----------|
| E13 | | |
-->

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!--
Append after each run. Keep last 5. Notes must be legible enough to show
what broke and what fixed it — not just a pass/fail count. Include: which
check IDs failed, what remediation was applied, and the re-check result.
See references/protocols/skill-evals.md, "Legible Eval Results Log" for a
worked example row.
-->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
