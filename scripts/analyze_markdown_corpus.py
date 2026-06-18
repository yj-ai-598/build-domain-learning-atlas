#!/usr/bin/env python3
"""Audit a Markdown learning corpus for hierarchy and renderable structures."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,4})\s+(.+?)\s*$")
NUMBER_RE = re.compile(r"^(\d+(?:\.\d+)*)\.?\s")


def semantic_level(markers: str, title: str) -> int:
    numbered = NUMBER_RE.match(title)
    if numbered:
        return min(4, len(numbered.group(1).split(".")) + 1)
    return len(markers)


def analyze_file(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    headings = []
    in_fence = False

    for index, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if not match:
            continue
        title = match.group(2).strip()
        headings.append(
            {
                "line": index + 1,
                "index": index,
                "level": semantic_level(match.group(1), title),
                "title": title,
            }
        )

    level_counts = Counter()
    titles = Counter()
    empty_sections = []
    list_sections = 0
    table_sections = 0
    fenced_sections = 0

    for position, heading in enumerate(headings):
        level_counts[f"H{heading['level']}"] += 1
        titles[heading["title"]] += 1
        end = headings[position + 1]["index"] if position + 1 < len(headings) else len(lines)
        content_lines = lines[heading["index"] + 1 : end]
        content = "\n".join(content_lines).strip()
        meaningful = re.sub(r"^\s*---+\s*$", "", content, flags=re.MULTILINE).strip()
        if not meaningful:
            empty_sections.append({"line": heading["line"], "title": heading["title"]})
        if re.search(r"^\s*[-*+]\s+", content, flags=re.MULTILINE):
            list_sections += 1
        if re.search(r"^\s*\|?.+\|.+\n\s*\|?\s*:?-{3,}.+\|", content, flags=re.MULTILINE):
            table_sections += 1
        if "```" in content:
            fenced_sections += 1

    return {
        "file": path.name,
        "lines": len(lines),
        "headings": len(headings),
        "levels": dict(sorted(level_counts.items())),
        "has_h1": level_counts["H1"] == 1,
        "empty_sections": empty_sections,
        "list_sections": list_sections,
        "table_sections": table_sections,
        "fenced_sections": fenced_sections,
        "duplicate_headings": sorted(title for title, count in titles.items() if count > 1),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    files = sorted(args.directory.glob("*.md"))
    reports = [analyze_file(path) for path in files]
    totals = {
        "files": len(reports),
        "lines": sum(report["lines"] for report in reports),
        "headings": sum(report["headings"] for report in reports),
        "empty_sections": sum(len(report["empty_sections"]) for report in reports),
        "list_sections": sum(report["list_sections"] for report in reports),
        "table_sections": sum(report["table_sections"] for report in reports),
        "fenced_sections": sum(report["fenced_sections"] for report in reports),
    }
    result = {"totals": totals, "files": reports}
    rendered = json.dumps(result, ensure_ascii=False, indent=2)

    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
