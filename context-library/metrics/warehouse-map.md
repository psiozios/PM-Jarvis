# Warehouse Map

**Fill this in before the first `/warehouse-brief` run.** The skill reads it in full before its first query, and stops if it is still the template: no warehouse, no brief. Every entry here is something a query got wrong once, or will. Keep it current, and date each change in the log at the bottom.

**Status:** template — replace this line with `filled, <date>` once the tables below are real.

## Connection

| Field | Value |
|-------|-------|
| Engine | [e.g., BigQuery, Snowflake, Postgres, Redshift, Databricks] |
| Source key | `<WAREHOUSE>`, with its preflight check registered in `config/source-preflight.json` |
| Read-only role | [the role or service account the brief uses; it must have no write grants] |
| Cost limits | [e.g., max bytes scanned per query, max queries per run] |
| Timezone of timestamps | [e.g., UTC in storage; convert to local at read] |

## Tables

One row per table a brief may touch. A table not listed is not queried until it is added here.

| Table | Grain (one row per…) | Primary key | Freshness | Owner | Notes |
|-------|----------------------|-------------|-----------|-------|-------|
| [schema.accounts] | [account] | [account_id] | [daily, 06:00 UTC] | [team or person] | [e.g., includes internal test accounts] |
| [schema.events] | [event] | [event_id] | [hourly, ~2h lag] | [...] | [...] |

## Join keys

| From | To | On | Cardinality | Watch for |
|------|----|----|-------------|-----------|
| [events] | [accounts] | [events.account_id = accounts.account_id] | [many-to-one] | [events from deleted accounts have no match] |

## Traps

The things that make a query return a plausible wrong number. Read every row before querying a table it names.

| Table | Trap | What to do |
|-------|------|------------|
| [accounts] | [test and internal accounts mixed in] | [filter `is_internal = false`] |
| [events] | [late-arriving rows for the last 48 hours] | [exclude the most recent two days from trends] |
| [subscriptions] | [one row per plan change, not per subscription] | [take the latest row per subscription_id] |
| [any] | [soft deletes] | [filter `deleted_at is null`] |

## Control totals and tolerance

Known figures a reconciliation can check against, and how far apart two paths may land before the insight is cut.

| Figure | Where it is reported | Tolerance |
|--------|----------------------|-----------|
| [active accounts, month end] | [finance close report] | [±1%] |
| [revenue, month] | [billing system export] | [±0.5%] |

## Change log

<!-- One dated line per change, newest first. Take the date from `date +%F` in the command that writes it. -->
