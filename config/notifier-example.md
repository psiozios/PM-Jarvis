# Notifier Config (Configure Me)

Reference configuration for the notifier interface used by `routines/` — see `references/protocols/notifications.md` for the contract this fills in. This file is markdown, not the strict-JSON `config/settings-template.json`, so it can carry inline explanation next to each placeholder.

Copy this file, fill in the placeholders below, and point your chosen adapter at it. Never commit real tokens — use environment variable **names** here, not values.

---

## Identity

```json
{
  "notifier_adapter": "<ADAPTER_NAME>",
  "identity": {
    "user_id": "<USER_ID>",
    "bot_token_env_var": "<BOT_TOKEN_ENV_VAR_NAME>",
    "channel": "<CHANNEL_OR_DM_TARGET>"
  },
  "mention_token_template": "<MENTION_TOKEN_TEMPLATE>"
}
```

| Placeholder | What it is | Slack reference example |
|---|---|---|
| `<ADAPTER_NAME>` | Which adapter implements the contract for this notifier | `slack-reference-adapter` |
| `<USER_ID>` | The user's own id on the platform — the self-notification target | Slack member id, e.g. the value shown in a user's profile settings |
| `<BOT_TOKEN_ENV_VAR_NAME>` | Name of the environment variable holding the bot token — never the token itself | `SLACK_BOT_TOKEN` |
| `<CHANNEL_OR_DM_TARGET>` | Where routines post — typically the user's own id used as a DM channel | same value as `<USER_ID>` for a DM-based self-notification |
| `<MENTION_TOKEN_TEMPLATE>` | How to construct a "notify" mention in a message body | `<@<USER_ID>>` |

## Setup

1. Create the bot credential on your platform (a Slack app + bot token, or your adapter's equivalent) and grant it the minimum scopes needed to post and react in the user's own DM.
2. Set the token as an environment variable using the name you put in `bot_token_env_var` above. Never paste the token value into this file or any file under version control.
3. Fill in `user_id` and `channel` with your platform's identifiers.
4. Point your adapter at this file (or the equivalent env-driven config in your own notifier implementation).

## Swapping Adapters

Nothing in `routines/` or `references/protocols/notifications.md` is Slack-specific — the Slack mapping in `notifications.md` is one reference implementation of the six-item contract. To use a different platform, write an adapter satisfying the same six items and repoint this file's `notifier_adapter` and identity fields at it.
