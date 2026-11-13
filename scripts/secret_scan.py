#!/usr/bin/env python3
"""Lightweight repository secret scan using only the Python standard library."""

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]

EXCLUDED = {
    "scripts/secret_scan.py",
}

PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "Stripe live secret": re.compile(r"\bsk_live_[A-Za-z0-9]{16,}\b"),
    "OpenAI-style secret": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    "generic credential assignment": re.compile(
        r"(?i)\b(?:api[_-]?key|secret|token|password)\b\s*[:=]\s*['\"][A-Za-z0-9_./+=:-]{20,}['\"]"
    ),
}

def tracked_files():
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    for raw in result.stdout.split(b"\0"):
        if raw:
            yield raw.decode("utf-8", errors="replace")

def main() -> int:
    findings = []
    for rel in tracked_files():
        if rel in EXCLUDED:
            continue
        path = ROOT / rel
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if b"\0" in data:
            continue
        text = data.decode("utf-8", errors="ignore")
        for name, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append((rel, line, name))

    if findings:
        print("Potential secrets detected:")
        for rel, line, name in findings:
            print(f"  {rel}:{line}: {name}")
        print("\nRemove the value and rotate it if it was ever real.")
        return 1

    print("Secret scan passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
