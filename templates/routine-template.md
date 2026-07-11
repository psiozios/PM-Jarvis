---
name: <ROUTINE_NAME>
description: "<ONE LINE: what this routine orchestrates and why it's scheduled>"
disable-model-invocation: true
user-invocable: false
---

<!--
Blank routine template. See routines/example-daily-digest/SKILL.md for a
filled worked example, and setup/routine-setup.md for the guided walkthrough
that fills this in step by step. Read references/protocols/routines.md
before filling this out — every step below cites a discipline from that
file rather than restating it.
-->

## What This Routine Does

<ONE LINE>

Orchestrates: `<SKILL_NAME>` (cite it — see discipline #1, thin wrapper. Do not restate the skill's internals here).

## Schedule

- **Period:** <daily | weekly | monthly | quarterly | custom cron>
- **Host:** <cloud (default) | local — state which and why, discipline #5>
- **Cron expression:** `<CRON_EXPRESSION>`
- **Timezone:** machine-local, computed at run time (discipline #8)

## State Files I Own

<!-- One owner per file (discipline #2). List every file this routine writes. -->

| File | Purpose |
|---|---|
| `routines/<ROUTINE_NAME>/outputs/YYYY-MM-DD-<slug>.md` | Dated output |
| `routines/<ROUTINE_NAME>/.last-run-<period>` | Already-ran guard |
| `routines/<ROUTINE_NAME>/.thread-pointer.json` | Notification thread anchor(s) |

## Step Skeleton

### 1. Bind rules

Read `references/protocols/routines.md`, `references/protocols/notifications.md`, and your notifier config (`config/notifier-example.md` or equivalent).

### 2. Guard

Compute the current period key in local time. Check it against `.last-run-<period>` (discipline #3: local state only, never chat history or downstream tool state). Missing/stale key → proceed, including catch-up for a missed prior period (discipline #4).

### 3. Gather

Read context per `<SKILL_NAME>`'s own Context Routing Logic table — don't duplicate that table here.

### 4. Decide

Run `<SKILL_NAME>` per its definition.

### 5. Execute

Apply the autonomy gate (discipline #7) to any proposed write:

- Standing approval on record for this routine → apply.
- No approval → list and stop.
- Write-to-others (anyone but the user, email, ticket, shared doc, invite) → never call unattended.

### 6. Deliver

See SENDING / THREADING below.

### 7. Stamp

Only after the send is confirmed: write the dated output, advance `.last-run-<period>`.

## SENDING

```
notifier.send(
  identity   = <BOT_IDENTITY>,
  target     = <USER_ID>,
  thread_key = "<period>|<anchor-id>",
  body       = <rendered output summary>,
  notify     = <true | false>,   # material update vs no-op — notifications.md item 4
)
```

## THREADING

```
if .thread-pointer.json has no entry for current period key:
    anchor = notifier.post_new_thread(target=<USER_ID>, title="<period date>")
    save .thread-pointer.json[period_key] = anchor.thread_id
else:
    anchor = load .thread-pointer.json[period_key]

notifier.reply_in_thread(anchor.thread_id, body, notify=<see SENDING>)
```

Self-heal on a missing anchor per `notifications.md` item 6: re-post, overwrite the pointer, retry once.

## Fill These

- [ ] `<ROUTINE_NAME>` replaced everywhere (frontmatter, file paths)
- [ ] `<SKILL_NAME>` names a real, existing skill
- [ ] Period, host, and cron expression chosen and next-run verified
- [ ] `<USER_ID>` and `<BOT_IDENTITY>` replaced with real notifier identity values
- [ ] State files table matches what the routine actually writes
- [ ] Schedule registered with your scheduler (cloud or local)
- [ ] First-fire verification run per `setup/routine-setup.md` Step 7

## Cross-Skill Links

- **Setup:** `setup/routine-setup.md`
- **Reply handling:** `.claude/skills/routine-responder/`
- **Protocol:** `references/protocols/routines.md`, `references/protocols/notifications.md`
