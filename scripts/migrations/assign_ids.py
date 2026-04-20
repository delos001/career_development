"""
One-time migration: assign stable IDs to Section 8 (EX) and Section 10 (PR)
entries in personal/knowledge/Experience_Inventory.md.

Rules:
- Section 8 entries (tasks): anchor is '^Role: ' line. Insert 'ID: EX-NNN'
  line directly above. Numbered sequentially in file order from EX-001.
- Section 10 entries (projects): anchor is '^Project: ' line. Insert 'ID: PR-NNN'
  line directly above. Numbered sequentially in file order from PR-001.
- Zero-padded to 3 digits minimum; widens automatically for values >= 1000.
- Sections 1-7, 9, 11 and the Background Roles block are not touched.

Writes directly to the source file. Review via 'git diff' after running;
'git restore' reverts if needed. Requires a clean git state before running.

Stdlib only. Deterministic: same input produces same output.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
INVENTORY = REPO_ROOT / "personal" / "knowledge" / "Experience_Inventory.md"

SEC8_START = "## 8. All Tasks Performed"
SEC8_END = "## Background Roles (Not Tagged)"
SEC10_START = "## 10. Independent & Volunteer Projects"

ROLE_ANCHOR = re.compile(r"^Role: ")
PROJECT_ANCHOR = re.compile(r"^Project: ")


def pad_id(prefix: str, n: int) -> str:
    """Zero-pad to 3 digits up to 999; widen naturally beyond."""
    return f"{prefix}-{n:03d}" if n < 1000 else f"{prefix}-{n}"


def find_line(lines: list[str], marker: str) -> int:
    for i, line in enumerate(lines):
        if line.rstrip("\r\n") == marker:
            return i
    raise ValueError(f"Section marker not found: {marker!r}")


def assign(lines: list[str]) -> tuple[list[str], int, int]:
    sec8_start = find_line(lines, SEC8_START)
    sec8_end = find_line(lines, SEC8_END)
    sec10_start = find_line(lines, SEC10_START)

    if not (sec8_start < sec8_end < sec10_start):
        raise ValueError("Section boundaries out of expected order.")

    out: list[str] = []
    ex_count = 0
    pr_count = 0

    for i, line in enumerate(lines):
        if sec8_start < i < sec8_end and ROLE_ANCHOR.match(line):
            ex_count += 1
            out.append(f"ID: {pad_id('EX', ex_count)}\n")
        elif i > sec10_start and PROJECT_ANCHOR.match(line):
            pr_count += 1
            out.append(f"ID: {pad_id('PR', pr_count)}\n")
        out.append(line)

    return out, ex_count, pr_count


def main() -> int:
    if not INVENTORY.exists():
        print(f"ERROR: inventory not found at {INVENTORY}", file=sys.stderr)
        return 1

    text = INVENTORY.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    try:
        updated, ex_count, pr_count = assign(lines)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    INVENTORY.write_text("".join(updated), encoding="utf-8")

    print(f"Updated: {INVENTORY}")
    print(
        f"  EX entries: {ex_count}  "
        f"({pad_id('EX', 1)} .. {pad_id('EX', ex_count)})"
    )
    print(
        f"  PR entries: {pr_count}  "
        f"({pad_id('PR', 1)} .. {pad_id('PR', pr_count)})"
    )
    print()
    print("Review: git diff personal/knowledge/Experience_Inventory.md")
    print("Revert: git restore personal/knowledge/Experience_Inventory.md")

    return 0


if __name__ == "__main__":
    sys.exit(main())
