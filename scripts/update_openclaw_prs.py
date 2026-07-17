#!/usr/bin/env python3
"""Refresh Arca's public OpenClaw PR ledger from GitHub.

The script rewrites the generated README section and data/openclaw-prs.json.
Manual context lives in data/pr-notes.json and is never overwritten.
"""
from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = "openclaw/openclaw"
AUTHOR_SCOPES = {
    "arcabotai": {
        "role": "Arca agent identity",
        "since": None,
    },
    "felirami": {
        "role": "Arca founder",
        "since": "2026-02-12",
    },
}
START = "<!-- OPENCLAW_PRS_START -->"
END = "<!-- OPENCLAW_PRS_END -->"
API = "https://api.github.com"


def request_json(path: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "arca-openclaw-contributions-ledger",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"{API}{path}", headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def request_text(url: str) -> str | None:
    headers = {"User-Agent": "arca-openclaw-contributions-ledger"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError:
        return None


def package_version(sha: str) -> str | None:
    raw = request_text(f"https://raw.githubusercontent.com/{REPO}/{sha}/package.json")
    if not raw:
        return None
    try:
        return json.loads(raw).get("version")
    except json.JSONDecodeError:
        return None


def short(sha: str | None) -> str:
    return sha[:12] if sha else "unknown"


def label_value(labels: list[str], prefix: str) -> str | None:
    return next((label.removeprefix(prefix) for label in labels if label.startswith(prefix)), None)


def latest_clawsweeper_comment(number: int) -> dict | None:
    comments = request_json(f"/repos/{REPO}/issues/{number}/comments?per_page=100")
    matches = [
        c for c in comments
        if c.get("user", {}).get("login", "").removesuffix("[bot]") == "clawsweeper"
        and "<!-- clawsweeper-review item=" in c.get("body", "")
    ]
    if not matches:
        return None
    comment = max(matches, key=lambda c: c.get("updated_at", ""))
    body = comment.get("body", "")
    overall = re.search(r"Overall:\s*([^\n]+)", body)
    proof = re.search(r"Proof:\s*([^\n]+)", body)
    patch = re.search(r"Patch quality:\s*([^\n]+)", body)
    result = re.search(r"Result:\s*([^\n]+)", body)
    return {
        "url": comment["html_url"],
        "updatedAt": comment.get("updated_at"),
        "overall": overall.group(1).strip() if overall else None,
        "proof": proof.group(1).strip() if proof else None,
        "patchQuality": patch.group(1).strip() if patch else None,
        "result": result.group(1).strip() if result else None,
    }


def collect() -> list[dict]:
    notes_path = ROOT / "data" / "pr-notes.json"
    notes = json.loads(notes_path.read_text()) if notes_path.exists() else {}
    authored_by_number = {}
    for author, scope in AUTHOR_SCOPES.items():
        terms = f"repo:{REPO} type:pr author:{author}"
        if scope["since"]:
            terms += f" created:>={scope['since']}"
        query = urllib.parse.quote(terms)
        search = request_json(f"/search/issues?q={query}&per_page=100&sort=created&order=desc")
        for item in search.get("items", []):
            authored_by_number[item["number"]] = item

    authored = authored_by_number.values()
    rows = []
    for pr in authored:
        number = pr["number"]
        details = request_json(f"/repos/{REPO}/pulls/{number}")
        labels = [label["name"] for label in details.get("labels", [])]
        head_sha = details["head"]["sha"]
        base_sha = details["base"]["sha"]
        merged = bool(details.get("merged_at"))
        state = "merged" if merged else details["state"]
        review = latest_clawsweeper_comment(number)
        note = notes.get(str(number), {})
        author = details.get("user", {}).get("login", "unknown")
        identity_role = AUTHOR_SCOPES.get(author, {}).get("role", "Arca-associated identity")
        rows.append({
            "number": number,
            "author": author,
            "identityRole": identity_role,
            "title": details["title"],
            "url": details["html_url"],
            "state": state,
            "draft": details.get("draft", False),
            "createdAt": details.get("created_at"),
            "updatedAt": details.get("updated_at"),
            "closedAt": details.get("closed_at"),
            "mergedAt": details.get("merged_at"),
            "headSha": head_sha,
            "baseSha": base_sha,
            "headOpenClawVersion": package_version(head_sha),
            "baseOpenClawVersion": package_version(base_sha),
            "labels": labels,
            "ratingLabel": label_value(labels, "rating: "),
            "statusLabel": label_value(labels, "status: "),
            "priority": next((x for x in labels if re.fullmatch(r"P[0-3]", x)), None),
            "clawSweeper": review,
            "arca": note,
        })
    return sorted(rows, key=lambda x: x["number"], reverse=True)


def render(rows: list[dict], generated_at: str) -> str:
    lines = [
        START,
        "## OpenClaw pull-request ledger",
        "",
        "This is the live record of upstream PRs authored through Arca's designated GitHub identities. It distinguishes open, closed, and merged work; an open PR is **not** presented as merged code.",
        "",
        f"Last refreshed: `{generated_at}` from the GitHub API.",
        "",
        "| PR | Author | State | OpenClaw version worked on | Exact head | Rating | Current work / blocker |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        note = row.get("arca", {})
        version = note.get("workedOnVersion") or row.get("headOpenClawVersion") or "source main"
        state = row["state"]
        if note.get("workStatus"):
            state = f"{state}; {note['workStatus']}"
        rating = row.get("ratingLabel") or "not rated"
        blocker = note.get("currentWork") or row.get("statusLabel") or "—"
        lines.append(
            f"| [#{row['number']}]({row['url']}) {row['title']} | [@{row['author']}](https://github.com/{row['author']}) | {state} | `{version}` | "
            f"[`{short(row['headSha'])}`](https://github.com/{REPO}/commit/{row['headSha']}) | {rating} | {blocker} |"
        )
    lines.extend([
        "",
        "### Version and evidence policy",
        "",
        "- **OpenClaw version worked on** is the source package version at the exact PR head, unless a manually verified release/tag is recorded in `data/pr-notes.json`.",
        "- Every row preserves the exact head and base SHAs in [`data/openclaw-prs.json`](data/openclaw-prs.json).",
        "- Ratings and statuses come from current public GitHub labels and the latest ClawSweeper review.",
        "- `@arcabotai` is Arca's agent identity. `@felirami` is included only from Arca's operating period beginning 2026-02-12; earlier personal work is not retroactively attributed to Arca.",
        "- Planned next work is maintained manually; live PR state refreshes automatically every six hours.",
        "- Closed PRs remain in the ledger. They are never silently rewritten as merged contributions.",
        END,
    ])
    return "\n".join(lines)


def main() -> None:
    rows = collect()
    data_path = ROOT / "data" / "openclaw-prs.json"
    previous = None
    if data_path.exists():
        try:
            previous = json.loads(data_path.read_text())
        except json.JSONDecodeError:
            previous = None
    if previous and previous.get("pullRequests") == rows:
        generated_at = previous.get("generatedAt") or datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    else:
        generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    identities = [
        {"login": login, **scope}
        for login, scope in AUTHOR_SCOPES.items()
    ]
    data = {
        "generatedAt": generated_at,
        "source": f"https://github.com/{REPO}",
        "authors": identities,
        "pullRequests": rows,
    }
    data_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

    readme_path = ROOT / "README.md"
    readme = readme_path.read_text()
    block = render(rows, generated_at)
    if START in readme and END in readme:
        readme = re.sub(re.escape(START) + r".*?" + re.escape(END), block, readme, flags=re.S)
    else:
        insertion = readme.find("## Public record")
        readme = readme[:insertion] + block + "\n\n" + readme[insertion:]
    readme_path.write_text(readme)
    print(f"updated {len(rows)} PR records at {generated_at}")


if __name__ == "__main__":
    main()
