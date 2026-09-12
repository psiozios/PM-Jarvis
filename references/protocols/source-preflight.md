# Source Preflight

**Principle: A SOURCE IS UNAVAILABLE UNTIL IT ANSWERS THIS SESSION — AND AN UNAVAILABLE SOURCE IS NAMED, NEVER COUNTED AS SWEPT.**

A connected source is not a working source. Tokens expire, scopes get revoked, a server goes down, and an OAuth refresh that needs a browser cannot happen inside a scheduled run at 6am. In every one of those cases the tool answers with an empty result rather than an error, so the source drops out of the run and the output looks exactly like a run where that source had nothing to report. This protocol closes the gap in two moves: check every source before work starts, and make the failures visible in the output.

## 1. Why OAuth is its own class

A token credential either works or returns a 401 you can read. An OAuth credential has a third state: the access token has expired, the refresh needs a browser and a human, and there is no browser. An unattended run cannot fix this, cannot wait for it, and must not retry it — a retry loop against an interactive consent screen burns the run and still ends with no data.

**Mark OAuth-only sources in the registry and treat re-auth as a user action, never a run action.** The run's job is to say which source needs re-auth and why, so the user fixes it once instead of reading three days of quietly incomplete digests.

## 2. The three states

| State | Means | What the run does |
|-------|-------|-------------------|
| `live` | The check ran and the source answered | Use it. List it as swept. |
| `bad` | A credential exists and the source refused it | Skip it. Report it unavailable with its reason. |
| `missing` | No credential is configured for this source | Skip it. Report it unavailable with its reason. |

`bad` and `missing` are reported the same way and kept separate on purpose: `missing` is a setup step the user never did, `bad` is something that worked before and stopped.

## 3. The check contract

Every source that can fail gets **one check, registered under its own key** — the placeholder key the skills already use (`<TASK_TRACKER>`, `<CALENDAR>`, `<CHAT_PLATFORM>`, `<METRICS_SOURCE>`, and the rest). Registration lives in `config/source-preflight.json`; copy the example and fill in your own.

A check satisfies this contract when it:

1. **Makes the cheapest real call the source offers** — one record, one page, one profile lookup. A status flag is not proof of reachability, and neither is a non-empty environment variable.
2. **Exits 0 on success, non-zero on failure.** No other signal is read.
3. **Prints a named reason on the failure path**, drawn from the closed list below. A check that fails without naming why produces `unknown`, which is a defect in the check rather than a state of the source.
4. **Prints no secret values.** The key name, the state, and the reason. Never the token, and never an `echo` of the variable holding it.
5. **Returns fast and gives up.** A check that hangs is a check that has already failed; bound it in seconds.

**Reason vocabulary — this list is closed, so the prose downstream stays consistent:**

`no-credential` · `expired` · `reauth-interactive` · `scope-missing` · `unreachable` · `rate-limited` · `unknown`

`reauth-interactive` is the OAuth case from §1 and the only reason that says plainly: no run can fix this, a human has to.

## 4. When it runs

**Interactive sessions:** a `SessionStart` hook runs the whole registry once and prints the table before the first turn. Install it from `config/settings-template.json` — see `hooks/README.md`. Knowing at the top of the session that the tracker is dead is worth far more than finding out in the middle of a sweep.

**Unattended runs:** preflight is the first step, ahead of the idempotency guard — see discipline #9 in `references/protocols/routines.md`. A routine that finds a source `bad` or `missing` still runs; it reports the source unavailable and works with what answered. It does not abort, and it does not retry an interactive re-auth.

**Mid-run failures count too.** A source that passed preflight and then failed during the run moves to `bad` with the reason the failure gave. Preflight is where most of these get caught, not a guarantee that none happen later.

## 5. The coverage rule

**A source that did not answer is reported unavailable, with its reason, and is never listed among the sources swept.**

This is the half that matters to the reader. A sweep that names five sources and reached four is a four-source sweep, and saying so is the difference between a thin result the reader can act on and a thin result they will read as "nothing happened." Three consequences:

- **Every sweep-class output carries a coverage line** naming what was swept and, separately, what was unavailable and why. It ships even when everything was live — an always-present line is one the reader learns to trust.
- **No candidate is killed on the silence of an unavailable source.** The lookup did not run, so the row is `UNPROVEN`, not `KILL` (`references/protocols/evidence-ledger.md`). An empty result from a dead source is not evidence; it is the absence of a lookup wearing a lookup's clothes.
- **Coverage is stated, not implied.** "Swept every source" is a claim, and it is false in any run where a source was down. Name the ones that answered.

## 6. Degradation has three modes, not one

The fallback most skills carry — *degrade to the local files when a tool is not connected* — covers only the case where the user never connected anything. Two more exist, and they matter more because they are silent:

| Mode | Tell | Handling |
|------|------|----------|
| Not connected | No registry entry at all | Fall back to local files. Say so once. |
| Connected but failing | `bad` or `missing` at preflight | Fall back, report unavailable **with the reason**, exclude from the swept list |
| Connected and empty | `live`, zero results | A real zero, and a finding about the window — not a coverage gap |

Distinguishing the second from the third is the whole point. They look identical in the data and mean opposite things.

## Cross-References

- `references/mcp-routing.md` — the registry these checks are keyed to, and the auth type per source
- `references/protocols/routines.md` — discipline #9, preflight as the first step of an unattended run
- `references/protocols/context-acquisition.md` — the read-freely protocol this gates; its degradation section defers here for live sources
- `references/protocols/evidence-ledger.md` — why an unavailable source produces `UNPROVEN` rather than `KILL`
- `setup/environment-keys.md` — provisioning the credentials this checks
