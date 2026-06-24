---
skill: connect-mcps
archetype: Workflow-Orchestration
eval-version: 1
last-updated: 2026-06-23
---

# Evals: /connect-mcps

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
| E1 | Tool identified correctly | Correctly identifies which MCP server the user needs based on their request |
| E2 | Setup steps sequential | Installation and configuration steps ordered logically with prerequisites noted |
| E3 | Verification step included | Includes a test command or check to verify the connection works |

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
| E8 | Permissions explained | States what data access the MCP requires and what it can/cannot do |
| E9 | Fallback documented | If MCP fails, explains what manual alternative is available |

### Completeness & Context

| ID | Check | Criteria |
|----|-------|----------|
| E10 | Integration benefits stated | Explains which skills benefit from this MCP connection |
| E11 | Troubleshooting section | Includes 2-3 common setup issues and how to resolve them |
| E12 | Security considerations noted | Notes any API key or token requirements and where they're stored |

## Scoring

- **PASS**: Criterion fully met
- **PARTIAL**: Mostly met with minor gaps (document what's missing)
- **FAIL**: Not met — must fix before delivery

**Passing threshold:** Zero FAILs. PARTIALs acceptable if documented.

## Eval Results Log

<!-- Append after each run. Keep last 5. -->

| Date | Pass | Partial | Fail | Notes |
|------|------|---------|------|-------|
