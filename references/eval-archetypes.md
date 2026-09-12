# Eval Archetypes

The six skill archetypes and what each one's evals emphasise. A catalog, kept resident where it is used: read it when creating a skill's `evals.md` or when deciding which archetype a skill is. The eval loop itself is `references/protocols/skill-evals.md`.

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

---

## Worked Examples for the Eval Protocol

Both belong to `references/protocols/skill-evals.md`; they live here so that file stays inside its budget.

### A legible Eval Results Log row

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
| 2026-07-11 | 11 | 1 | 0 | Initial run failed E8 (verify-before-flag: two items missing `Checked:` lines) and E11 (auto-created a task instead of proposing it). Remediation: added `Checked:` line to both items citing the tracker cross-reference; converted the auto-created task to a proposed row in the follow-ups table. Re-check: E8 and E11 both PASS. E9 remains PARTIAL — sweep window was 10 days, not the full 14-day default; acknowledged and accepted for this run. |

### Adding a fifth category

A skill that produces standing-radar output (see `references/protocols/skill-patterns.md` Pattern 1) might outgrow the four base categories with a fifth:

```markdown
### Category 5: Verification Discipline

| ID | Check | Criteria |
|----|-------|----------|
| E13 | Verify-before-flag | Every flagged item carries a `Checked:` line naming a real cross-referenced source |
| E14 | Comprehensive-not-delta | The full sweep window was re-examined, not narrowed to new-since-last-run items |
| E15 | Ledger-derived list | A ledger exists in `outputs/ledgers/`, every proposed item has a `PROPOSE` row, killed rows are reported beside the proposals with their evidence, and no row was dropped to satisfy a volume cap |
```

**E15 is not only an example — it is live in every skill that binds the ledger.** `action-sweep`, `loose-threads`, `chat-ingest`, `meeting-cleanup`, `voice-of-customer`, `feature-request-analysis`, `refinement-prep`, and `proactive-gaps` each carry a ledger check under their own next unused ID. A skill that invokes `references/protocols/evidence-ledger.md` and has no eval for it leaves that protocol with no enforcement surface anywhere, which is how it went unchecked for a full round.

Bump `eval-version: 1` → `eval-version: 2`, set `last-updated` to the date of the change, and append the new category after Category 4 in that skill's `evals.md`. Do not renumber existing E-IDs — new checks always get the next unused number.
