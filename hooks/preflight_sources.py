#!/usr/bin/env python3
"""
SessionStart hook: report every registered source as live, bad, or missing
BEFORE any work starts.

Why this exists: a connected source is not a working source. Tokens expire,
scopes get revoked, and an OAuth refresh needs a browser that a scheduled run
does not have. In all three cases the tool tends to answer with an empty result
rather than an error, so the source drops out of a sweep and the output looks
identical to a run where that source genuinely had nothing. Checking up front
turns a silent gap into a named one.

Registry: config/source-preflight.json
Protocol: references/protocols/source-preflight.md

Each check exits 0 for live and non-zero for failed, printing one reason word
from the closed vocabulary below. A check that fails without naming a reason
scores 'unknown', which is a defect in the check rather than a state of the
source.

This hook never fails the session and never prints a secret: it reports the key
name, the state, and the reason word only.
"""
import json
import subprocess
import sys
from pathlib import Path

REGISTRY = Path(__file__).resolve().parent.parent / "config" / "source-preflight.json"

REASONS = {
    "no-credential",
    "expired",
    "reauth-interactive",
    "scope-missing",
    "unreachable",
    "rate-limited",
    "unknown",
}

# A reason that names a missing setup step rather than a credential that broke.
MISSING_REASONS = {"no-credential"}


def reason_from(output: str) -> str:
    """Pull the first closed-vocabulary word out of a check's output."""
    for token in output.split():
        word = token.strip().strip(".,:;'\"").lower()
        if word in REASONS:
            return word
    return "unknown"


def run_check(name: str, spec: dict) -> tuple:
    """Return (state, reason) for one source. Never raises."""
    command = spec.get("check")
    if not command:
        return "missing", "no-credential"
    try:
        done = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=float(spec.get("timeout", 15)),
        )
    except subprocess.TimeoutExpired:
        return "bad", "unreachable"
    except Exception:
        return "bad", "unknown"

    if done.returncode == 0:
        return "live", ""
    reason = reason_from(f"{done.stdout} {done.stderr}")
    state = "missing" if reason in MISSING_REASONS else "bad"
    return state, reason


def main() -> int:
    if not REGISTRY.exists():
        return 0
    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except Exception:
        # A malformed registry is worth saying out loud — it means nothing is
        # being checked, which is exactly the silence this hook exists to break.
        print(
            "<source-preflight>\nRegistry config/source-preflight.json could not "
            "be parsed, so no source was checked. Treat every live source as "
            "unverified this session.\n</source-preflight>"
        )
        return 0

    sources = registry.get("sources", {})
    active = {k: v for k, v in sources.items() if v.get("enabled") is True}
    if not active:
        return 0

    rows, failures = [], []
    for name, spec in active.items():
        state, reason = run_check(name, spec)
        label = spec.get("label", name)
        auth = spec.get("auth", "none")
        rows.append((name, label, auth, state, reason))
        if state != "live":
            failures.append((name, label, state, reason, spec.get("fix", "")))

    out = ["<source-preflight>"]
    out.append(
        f"{len(rows) - len(failures)} of {len(rows)} registered sources answered. "
        "A source below that is not `live` is unavailable for this session: report "
        "it by name with its reason, exclude it from any list of sources swept, and "
        "never read its silence as evidence about a candidate "
        "(references/protocols/source-preflight.md)."
    )
    out.append("")
    out.append("| Source | Auth | State | Reason |")
    out.append("|---|---|---|---|")
    for name, label, auth, state, reason in rows:
        out.append(f"| {label} `{name}` | {auth} | {state} | {reason or '-'} |")

    if failures:
        out.append("")
        out.append("**Unavailable this session:**")
        for name, label, state, reason, fix in failures:
            line = f"- {label} `{name}` — {state}, {reason}."
            if reason == "reauth-interactive":
                line += " OAuth refresh needs a browser; no scheduled run can repair it."
            if fix:
                line += f" {fix}"
            out.append(line)
    out.append("</source-preflight>")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
