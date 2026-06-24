---
skill: slack-message
archetype: Communication-Draft
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /slack-message

## How to Run (automatic on every skill invocation)

1. Original agent completes skill output and runs informal self-check
2. Original agent spawns a separate eval agent (clean context window)
3. Eval agent reads: this file, the skill output, `config/house-style.md`
4. Evaluates each criterion independently → PASS / FAIL / PARTIAL
5. FAILs returned to original agent for revision → re-eval loop
6. Zero FAILs achieved → log results below

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
| E4 | No AI slop | Zero instances of: delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge, empower, elevate, foster, holistic, synergy, paradigm |
| E5 | House style compliance | Follows any active rules in `config/house-style.md` |
| E6 | Human-sounding | Varied sentence lengths, contractions used naturally, no formulaic paragraph openings |

### Substance & Specificity

| ID | Check | Criteria |
|----|-------|----------|
| E7 | Context-grounded | References specific data from context sources — not generic placeholder language |
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
