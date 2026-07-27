---
name: update-docs
description: Update README, CHANGELOG, and other docs after code changes by reading the actual implementation in the git diff rather than trusting what the docs already claim. Edits documentation files in place; run it with --check for an audit that finds stale docs and changes nothing.
user-invocable: true
disable-model-invocation: false
---

# /update-docs - Keep Docs Honest

Update documentation after code changes. The rule is simple: read the actual code, not the existing docs. Docs lie. Code doesn't.

## Quick Start

```
/update-docs

Options:
- /update-docs              — scan git diff for recent changes and update docs
- /update-docs [commit-ref] — update docs based on specific commit(s)
- /update-docs --check      — audit mode: find stale docs without updating

I'll read the actual implementation, compare it to existing documentation,
update what's wrong, and flag what needs manual review.

Output: Updated docs in place + summary at outputs/analyses/docs-update-[date].md
```

---

## Context Routing

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Git Changes | `git diff`, `git log` | modified, added, deleted | What changed in code |
| Existing Docs | `README.md`, `CHANGELOG.md`, `docs/` | features, API, usage | Current documentation state |
| PRDs | `context-library/prds/*.md` | requirements, behavior | Intended behavior vs actual |
| Code Reviews | `outputs/analyses/code-review-*.md` | changes, fixes | What was reviewed and why |

---


For live tool data (task tracker, chat platform, issue tracker, metrics source), route through `references/mcp-routing.md` — read it when the task wants data no local file holds. All sources degrade to the files above when a tool is not connected.

## When to Use

- After completing a feature (post `/code-first-draft`)
- After a bug fix that changes documented behavior
- Before a release to ensure docs match what shipped
- When onboarding reveals docs are out of sync with code
- Periodic audit to catch documentation drift

## When NOT to Use

- Writing new documentation from scratch (just write it)
- Editing PM documents like PRDs (use `/editing-assistant`)
- Creating user-facing release notes (use `/content-marketing`)

---

## Workflow

### Step 1: Identify What Changed

Read the git diff or recent commits to understand what code changed:
- New files, deleted files, renamed files
- Modified functions, changed interfaces, updated configs
- New features, bug fixes, behavior changes

### Step 2: Find Affected Documentation

Search for docs that reference the changed code:
- README.md (setup, usage, API reference)
- CHANGELOG.md (version history)
- Inline code comments and JSDoc/docstrings
- Any docs/ directory files
- Configuration examples

### Step 3: Verify Against Actual Implementation

**This is the critical step.** For each doc section that touches changed code:
- Read the current implementation (not the old docs)
- Compare what the docs say vs what the code actually does
- Note discrepancies, outdated examples, wrong parameter names

### Step 4: Update Documentation

Apply updates following these rules:
- **Concise over comprehensive.** Sacrifice grammar for brevity.
- **Code-verified only.** Every claim must match current implementation.
- **Examples over theory.** Show how to use it, not how it works internally.
- **CHANGELOG format:** Use Keep a Changelog categories (Added, Changed, Fixed, Removed, Deprecated, Security).

### Step 5: Flag Stale Docs

Some docs can't be auto-updated (they need human context):
- Architecture decisions that may have changed
- User-facing copy that needs product review
- API docs that need testing to verify
- Docs referencing removed features

Flag these for manual review rather than guessing.

---

## CHANGELOG Format

Follow [Keep a Changelog](https://keepachangelog.com/) conventions:

```markdown
## [Unreleased]

### Added
- [New feature or capability - user-facing language]

### Changed
- [Modified existing behavior - what changed and why it matters]

### Fixed
- [Bug fix - what was broken and how it's fixed now]

### Removed
- [Removed feature or capability]

### Deprecated
- [Feature that will be removed in a future version]

### Security
- [Security fix - be specific about the vulnerability class]
```

---

## Binding Rules

- **NEVER trust existing documentation as source of truth.** Read the actual code.
- **Be concise.** Documentation should be shorter than the code it describes.
- **Practical over theoretical.** Examples and usage patterns beat architectural explanations.
- **Ask if uncertain.** If you can't determine the intent behind a change from the code alone, ask the PM rather than guessing.
- **Flag, don't fabricate.** If docs reference something you can't verify, flag it for review instead of making up an explanation.
- **Audit mode (--check)** should only report problems, not fix them. Useful for understanding the scope before committing to updates.

---

## Output Template (Summary)

```markdown
# Documentation Update Summary

**Date:** [date]
**Trigger:** [git diff / specific commits / audit]
**Changes reviewed:** [count of code changes analyzed]

---

## Documentation Updated

| File | Section | Change | Verified |
|------|---------|--------|----------|
| [doc file] | [section] | [what was updated] | Yes |
| [doc file] | [section] | [what was updated] | Yes |

---

## Stale Docs Flagged (Needs Manual Review)

| File | Section | Issue | Why Manual |
|------|---------|-------|------------|
| [doc file] | [section] | [what's wrong] | [why I can't fix it automatically] |

---

## CHANGELOG Entry Added

[Show the CHANGELOG entry that was added]
```

---

## Output Quality Self-Check

- [ ] **Every update verified against actual code** - not copied from old docs
- [ ] **CHANGELOG follows Keep a Changelog format** - correct categories used
- [ ] **Stale docs flagged, not fabricated** - uncertain items marked for review
- [ ] **Concise** - docs are shorter than the code they describe
- [ ] **No aspirational documentation** - only documents what currently exists
- [ ] **Summary saved:** `outputs/analyses/docs-update-[date].md`


## Formal Eval

**Do not present the output until this has run.** Spawn a separate eval agent in a clean context window and hand it three things: the output (or its absolute path), this skill's `evals.md`, and `config/house-style.md`. It returns a PASS / PARTIAL / FAIL / N-A table with remediation for every FAIL. Loop until zero FAILs, then log the run in the Eval Results Log in `evals.md`.

See `references/protocols/skill-evals.md`.

## Cross-Skill Links

- `/code-first-draft` or `/code-review` -> before this, as the change whose docs are now stale
- `/content-marketing` -> when the change also needs user-facing release notes, not just internal docs
- `/editing-assistant` -> when the docs are accurate but badly written
- `/launch-checklist` -> when documentation is a launch gate that has to be signed off
