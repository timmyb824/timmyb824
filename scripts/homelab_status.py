"""Generate homelab-status.svg for the profile README from the public API.

Fetches the redacted public snapshot from the homelab live-status API and
renders a compact SVG card (services up/total, infra up/total, freshness).
On any failure the badge says "unreachable" — it's a status badge, after all.
"""

import json
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

API = "https://status.timmybtech.com"
OUT = "homelab-status.svg"
TIMEOUT = 15
MINS_PER_HOUR = 60

OK, WARN, BAD = "#22c55e", "#f59e0b", "#ef4444"
BG, TEXT, MUTED = "#0b0f16", "#e7eefc", "#9fb0cf"

SVG = """
<svg xmlns="http://www.w3.org/2000/svg" width="460" height="96"
     viewBox="0 0 460 96">
  <rect width="460" height="96" rx="12" fill="{bg}"/>
  <rect x="0.5" y="0.5" width="459" height="95" rx="12" fill="none"
        stroke="{muted}" stroke-opacity="0.25"/>
  <circle cx="24" cy="26" r="5" fill="{color}"/>
  <text x="40" y="31" font-size="15" font-weight="650" fill="{text}"
        font-family="ui-sans-serif, system-ui, sans-serif"
        >Homelab: {label}</text>
  <text x="24" y="56" font-size="13" fill="{muted}"
        font-family="ui-monospace, monospace"
        >services {svc} up &#183; infra {infra} up</text>
  <text x="24" y="78" font-size="11" fill="{muted}"
        font-family="ui-monospace, monospace"
        >{updated} &#183; status.timmybtech.com</text>
</svg>
"""


def fetch_status() -> dict:
    """Fetch the public snapshot; raises on any failure.

    Sends an explicit User-Agent: Cloudflare blocks urllib's default
    (Python-urllib/*) with a 403 before the request ever reaches Traefik.
    """
    req = urllib.request.Request(
        f"{API}/api/v1/status",
        headers={"User-Agent": "GitHub-Actions homelab-status-badge"},
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.load(resp)


def up_count(items: list[dict]) -> int:
    """Count entries whose status is up."""
    return sum(1 for i in items if i.get("status") == "up")


def render(label: str, color: str, svc: str, infra: str, updated: str) -> str:
    """Render the SVG card."""
    return SVG.format(
        label=label,
        color=color,
        svc=svc,
        infra=infra,
        updated=updated,
        bg=BG,
        text=TEXT,
        muted=MUTED,
    )


def main() -> None:
    """Fetch, summarize, and write the SVG."""
    try:
        snap = fetch_status()
        services = snap.get("services", [])
        infra_items = snap.get("hosts", []) + snap.get("nodes", [])
        svc = f"{up_count(services)}/{len(services)}"
        infra = f"{up_count(infra_items)}/{len(infra_items)}"
        all_up = up_count(services) == len(services) and up_count(infra_items) == len(
            infra_items
        )
        gen = datetime.fromisoformat(snap["generated_at"].replace("Z", "+00:00"))
        mins = max(0, round((datetime.now(UTC) - gen).total_seconds() / 60))
        updated = (
            f"updated {mins}m ago"
            if mins < MINS_PER_HOUR
            else f"updated {round(mins / MINS_PER_HOUR)}h ago"
        )
        svg = render(
            "operational" if all_up else "degraded",
            OK if all_up else WARN,
            svc,
            infra,
            updated,
        )
    except Exception as exc:  # badge should reflect the outage, not crash CI
        svg = render("unreachable", BAD, "-/-", "-/-", f"error: {exc}"[:40])
    Path(OUT).write_text(svg.strip() + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
