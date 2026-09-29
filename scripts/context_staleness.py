#!/usr/bin/env python3
"""Validate durable context front matter and flag records older than 90 days."""

from datetime import date, datetime
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MAX_AGE_DAYS = 90
ALLOWED_STATUS = {"idea", "proposal", "decision", "superseded"}
RECORD_DIRS = {"decisions", "meetings", "research", "prototypes", "work"}

def record_files():
    projects = ROOT / "projects"
    if projects.exists():
        for path in projects.rglob("*.md"):
            if path.name == "README.md":
                continue
            parts = set(path.relative_to(projects).parts)
            if parts & RECORD_DIRS:
                yield path

    shared = ROOT / "shared"
    if shared.exists():
        for path in shared.rglob("*.md"):
            if path.name != "README.md":
                yield path

def front_matter(text: str):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    block = text[4:end]
    values = {}
    for line in block.splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip("'\"")
    return values

def main() -> int:
    today = date.today()
    issues = []

    for path in sorted(set(record_files())):
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        fm = front_matter(text)
        if fm is None:
            issues.append(f"{rel}: missing YAML front matter")
            continue

        status = fm.get("status", "")
        owner = fm.get("owner", "")
        reviewed = fm.get("last-reviewed", "")

        if status not in ALLOWED_STATUS:
            issues.append(f"{rel}: status must be one of {sorted(ALLOWED_STATUS)}")
        if not owner:
            issues.append(f"{rel}: owner is required")
        if not reviewed:
            issues.append(f"{rel}: last-reviewed is required")
            continue

        try:
            reviewed_date = datetime.strptime(reviewed, "%Y-%m-%d").date()
        except ValueError:
            issues.append(f"{rel}: last-reviewed must use YYYY-MM-DD")
            continue

        age = (today - reviewed_date).days
        if age > MAX_AGE_DAYS:
            issues.append(
                f"{rel}: stale — last reviewed {age} days ago "
                f"(limit {MAX_AGE_DAYS})"
            )

    if issues:
        print("Context health issues:")
        for issue in issues:
            print(f"  {issue}")
        return 1

    print("Context staleness check passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
