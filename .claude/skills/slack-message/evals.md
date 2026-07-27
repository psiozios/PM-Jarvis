---
skill: slack-message
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /slack-message

## How to Run

Runs automatically on every skill invocation, per `references/protocols/skill-evals.md` — that file owns the loop. The eval agent is handed this file, the skill output, and `config/house-style.md`, and the loop runs until zero FAILs.

## Eval Criteria

### Structure & Format

| ID | Check | Criteria |
|----|-------|----------|
| E1 | Channel-appropriate length | Under 300 words for channel posts, under 150 for DMs |
| E2 | Formatting Slack-native | Uses Slack formatting (bold, bullets, emoji) not markdown headers |
| E3 | Tone matches request | Message tone matches the requested style: Direct / Friendly / Formal / Urgent |

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
| E8 | Specific names and dates | Uses specific names, dates, and numbers — not 'the team' or 'soon' |
| E9 | Stakeholder profile used | If messaging a known stakeholder, communication style matches their profile |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | CTA in final sentence | Clear ask or call-to-action in the closing — not just information |
| E11 | Context sufficient for reader | Reader can understand and act without opening other documents |
| E12 | Thread-ready | If it's a reply, acknowledges the thread context before adding new info |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
