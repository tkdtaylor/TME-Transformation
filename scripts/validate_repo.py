# Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0).
"""Fast, zero-dependency repository validator for TME-Transformation."""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", ".docs_build", "site", "dist", ".venv", "venv", "__pycache__"}

SPDX_MARKER = "SPDX-License-Identifier: CC-BY-4.0"

SPDX_REQUIRED_FILES = [
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "Templates/ArchitectureDecisionRecord.md",
    "Templates/MigrationWaveReadinessGate.md",
]

SPDX_REQUIRED_DIRS = [
    "AIFoundationalSuite",
    "ProgramDelivery",
    "Examples/ApprovalGatedFinancialVarianceAgent",
]

LIST_RE = re.compile(r"^(?:[-*]|\d+\.)\s+")
SUBLIST_RE = re.compile(r"^\s+(?:[-*]|\d+\.)\s+")
COMBINED_LINK_RE = re.compile(
    r"\[!\[[^\]]*\]\(([^)]+)\)\]\(([^)]+)\)|!?\[[^\]]*\]\(([^)]+)\)"
)


def github_slug(heading_text: str) -> str:
    """Compute GitHub-compatible Markdown heading anchor slug."""
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading_text)
    cleaned = re.sub(r"[`*_~]", "", cleaned).strip().lower()
    chars = [ch for ch in cleaned if ch.isalnum() or ch in (" ", "-", "_")]
    return "".join(chars).replace(" ", "-")


def mkdocs_slug(heading_text: str) -> str:
    """Compute python-markdown toc extension anchor slug."""
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading_text)
    cleaned = re.sub(r"[`*_~]", "", cleaned).strip().lower()
    cleaned = re.sub(r"[^\w\s-]", "", cleaned)
    return re.sub(r"[-\s]+", "-", cleaned).strip("-")


def collect_headings(md_path: Path, slug_fn) -> set[str]:
    """Return all heading anchor slugs in md_path outside fenced code blocks."""
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    fence_char = ""
    with md_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            stripped = line.strip()
            if stripped.startswith(("```", "~~~")):
                marker = stripped[:3]
                if not in_fence:
                    in_fence = True
                    fence_char = marker[0]
                elif marker[0] == fence_char:
                    in_fence = False
                continue
            if in_fence:
                continue
            match = re.match(r"^#{1,6}\s+(.+?)\s*#*$", line.rstrip("\n"))
            if match:
                base = slug_fn(match.group(1))
                if base in counts:
                    counts[base] += 1
                    slugs.add(f"{base}-{counts[base]}")
                else:
                    counts[base] = 0
                    slugs.add(base)
    return slugs


def iter_files(root: Path, suffix: str) -> list[Path]:
    """Walk root excluding SKIP_DIRS and return sorted files with suffix."""
    results: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fname in sorted(filenames):
            if fname.endswith(suffix):
                results.append(Path(dirpath) / fname)
    return results


def strip_inline_code(line: str) -> str:
    """Remove inline code spans so template syntax is not parsed as links."""
    return re.sub(r"`[^`]*`", "", line)


def check_markdown_links_and_boxes(
    scan_root: Path, slug_fn, check_boxes: bool = True
) -> tuple[list[str], int, int]:
    """Validate relative links, #anchors, and optional ASCII box widths."""
    issues: list[str] = []
    md_files = iter_files(scan_root, ".md")
    heading_cache = {p.resolve(): collect_headings(p, slug_fn) for p in md_files}
    link_count = 0
    box_count = 0

    for md_path in md_files:
        rel_src = md_path.relative_to(scan_root)
        src_dir = md_path.parent
        with md_path.open("r", encoding="utf-8") as fh:
            lines = fh.read().splitlines()

        in_fence = False
        fence_char = ""
        fence_lines: list[tuple[int, str]] = []

        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith(("```", "~~~")):
                marker = stripped[:3]
                if not in_fence:
                    in_fence = True
                    fence_char = marker[0]
                    fence_lines = []
                elif marker[0] == fence_char:
                    in_fence = False
                    if check_boxes and any("+---" in fl for _, fl in fence_lines):
                        box_count += 1
                        issues.extend(
                            validate_ascii_boxes(rel_src, fence_lines)
                        )
                continue

            if in_fence:
                fence_lines.append((idx, line))
                continue

            cleaned = strip_inline_code(line)
            for match in COMBINED_LINK_RE.finditer(cleaned):
                targets = (
                    [match.group(1).strip(), match.group(2).strip()]
                    if match.group(1) is not None
                    else [match.group(3).strip()]
                )
                for target in targets:
                    if not target or target.startswith(("http://", "https://", "mailto:")):
                        continue
                    link_count += 1
                    if target.startswith("#"):
                        anchor = target[1:]
                        if anchor not in heading_cache[md_path.resolve()]:
                            issues.append(f"{rel_src}:{idx}: Broken same-file anchor '{target}'")
                        continue

                    if "#" in target:
                        file_part, anchor = target.split("#", 1)
                    else:
                        file_part, anchor = target, None

                    resolved = (src_dir / file_part).resolve()
                    if not resolved.exists():
                        issues.append(f"{rel_src}:{idx}: Broken relative link '{target}'")
                    elif anchor is not None and resolved.is_file() and resolved.suffix == ".md":
                        if anchor not in heading_cache.get(resolved, set()):
                            issues.append(f"{rel_src}:{idx}: Broken cross-file anchor '{target}'")

    return issues, len(md_files), link_count if not check_boxes else link_count + (box_count * 0)


def check_list_blank_lines(root: Path) -> list[str]:
    """Ensure top-level lists after paragraph/label lines are preceded by a blank line."""
    issues: list[str] = []
    for md_path in iter_files(root, ".md"):
        rel_src = md_path.relative_to(root)
        lines = md_path.read_text(encoding="utf-8").splitlines()
        in_fence = False
        fence_char = ""
        for idx, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith(("```", "~~~")):
                marker = stripped[:3]
                if not in_fence:
                    in_fence = True
                    fence_char = marker[0]
                elif marker[0] == fence_char:
                    in_fence = False
                continue
            if in_fence or idx == 0:
                continue
            if LIST_RE.match(line):
                prev = lines[idx - 1]
                prev_s = prev.strip()
                if (
                    prev_s != ""
                    and not LIST_RE.match(prev)
                    and not SUBLIST_RE.match(prev)
                    and not prev.startswith(("#", ">", "|", "---", "***", "<!--"))
                ):
                    issues.append(
                        f"{rel_src}:{idx + 1}: Missing blank line before list item after '{prev_s[:60]}'"
                    )
    return issues


def validate_ascii_boxes(rel_src: Path, fence_lines: list[tuple[int, str]]) -> list[str]:
    """Check equal line widths across contiguous box rows starting/ending with + or |."""
    issues: list[str] = []
    contiguous: list[tuple[int, str]] = []

    def flush() -> None:
        if len(contiguous) >= 2:
            widths = {len(text) for _, text in contiguous}
            if len(widths) > 1:
                summary = ", ".join(f"L{ln}={len(t)}" for ln, t in contiguous)
                issues.append(f"{rel_src}: Inconsistent ASCII box row widths ({summary})")
        contiguous.clear()

    for ln, raw in fence_lines:
        trimmed = raw.rstrip()
        if trimmed.startswith(("+", "|")) and trimmed.endswith(("+", "|")) and len(trimmed) >= 2:
            contiguous.append((ln, trimmed))
        else:
            flush()
    flush()
    return issues


def parse_data_dictionary(dd_path: Path) -> dict[str, list[str]]:
    """Extract CSV column tables from Templates/DataDictionary.md."""
    result: dict[str, list[str]] = {}
    if not dd_path.exists():
        return result
    cur_csv: str | None = None
    in_table = False
    with dd_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            s = line.strip()
            heading = re.match(r"^##\s+([A-Za-z0-9_]+\.csv)\s*$", s)
            if heading:
                cur_csv = heading.group(1)
                result[cur_csv] = []
                in_table = False
                continue
            if cur_csv:
                if s.startswith("| Column |"):
                    in_table = True
                    continue
                if in_table and s.startswith("|---"):
                    continue
                if in_fence_or_table_row := (in_table and s.startswith("|")):
                    if in_fence_or_table_row:
                        cols = [c.strip() for c in s.strip("|").split("|")]
                        if cols:
                            result[cur_csv].append(cols[0])
                elif in_table and not s.startswith("|"):
                    cur_csv = None
                    in_table = False
    return result


def check_csvs(root: Path) -> tuple[list[str], int]:
    """Validate CSV row consistency, example parity, and DataDictionary schema parity."""
    issues: list[str] = []
    dd_cols = parse_data_dictionary(root / "Templates" / "DataDictionary.md")
    csv_files = iter_files(root, ".csv")

    for csv_path in csv_files:
        rel_csv = csv_path.relative_to(root)
        with csv_path.open("r", encoding="utf-8", newline="") as fh:
            rows = list(csv.reader(fh))
        if not rows:
            issues.append(f"{rel_csv}: Empty CSV file")
            continue
        header = rows[0]
        if header and header[0].startswith("<!--"):
            issues.append(f"{rel_csv}: Line 1 must be CSV header, not HTML comment")
        for row_idx, row in enumerate(rows, 1):
            if len(row) != len(header):
                issues.append(
                    f"{rel_csv}:{row_idx}: Column count mismatch (expected {len(header)}, got {len(row)})"
                )

        base_name = csv_path.name.replace(".example.csv", ".csv")
        if base_name not in dd_cols:
            issues.append(f"{rel_csv}: Missing schema section '## {base_name}' in Templates/DataDictionary.md")
        elif header != dd_cols[base_name]:
            issues.append(
                f"{rel_csv}: Header differs from Templates/DataDictionary.md ({header} != {dd_cols[base_name]})"
            )

        if csv_path.name.endswith(".example.csv"):
            parent_tmpl = root / "Templates" / base_name
            if not parent_tmpl.exists():
                issues.append(f"{rel_csv}: Missing parent template Templates/{base_name}")
            else:
                with parent_tmpl.open("r", encoding="utf-8", newline="") as pfh:
                    parent_header = next(csv.reader(pfh))
                if header != parent_header:
                    issues.append(f"{rel_csv}: Header differs from Templates/{base_name}")

    return issues, len(csv_files)


def check_spdx_headers(root: Path) -> tuple[list[str], int]:
    """Verify CC-BY-4.0 SPDX license header on line 1 of required Markdown files."""
    targets: list[Path] = []
    for rel in SPDX_REQUIRED_FILES:
        targets.append(root / rel)
    for rel_dir in SPDX_REQUIRED_DIRS:
        dpath = root / rel_dir
        if dpath.is_dir():
            targets.extend(sorted(dpath.glob("*.md")))

    issues: list[str] = []
    seen: set[Path] = set()
    for path in targets:
        if path in seen:
            continue
        seen.add(path)
        rel = path.relative_to(root)
        if not path.exists():
            issues.append(f"{rel}: Missing required SPDX-checked file")
            continue
        with path.open("r", encoding="utf-8") as fh:
            first_line = fh.readline().rstrip("\n")
        if SPDX_MARKER not in first_line:
            issues.append(f"{rel}:1: Missing '{SPDX_MARKER}' on line 1")
    return issues, len(seen)


def check_mkdocs_nav(root: Path, nav_file: Path) -> tuple[list[str], int]:
    """Parse nav: file paths in mkdocs.yml using stdlib regex and verify in .docs_build/."""
    issues: list[str] = []
    docs_build = root / ".docs_build"
    if not docs_build.is_dir():
        return [f"Missing '{docs_build}' directory; run scripts/build_docs_src.py first"], 0
    if not nav_file.is_file():
        return [f"Missing mkdocs config file: {nav_file}"], 0

    lines = nav_file.read_text(encoding="utf-8").splitlines()
    in_nav = False
    nav_paths: list[tuple[int, str]] = []
    for idx, line in enumerate(lines, 1):
        if re.match(r"^nav:\s*$", line):
            in_nav = True
            continue
        if in_nav:
            if line and not line[0].isspace() and not line.lstrip().startswith("#"):
                break
            match = re.search(r":\s+([^\s#]+\.md)\s*(?:#.*)?$", line)
            if match:
                nav_paths.append((idx, match.group(1).strip("'\"")))

    if not nav_paths:
        issues.append(f"{nav_file}: No .md entries found under nav:")
    for ln, rel_path in nav_paths:
        target = docs_build / rel_path
        if not target.is_file():
            issues.append(f"{nav_file.name}:{ln}: Nav entry '{rel_path}' missing in .docs_build/")

    docs_link_issues, _, _ = check_markdown_links_and_boxes(
        docs_build, mkdocs_slug, check_boxes=False
    )
    for item in docs_link_issues:
        issues.append(f".docs_build/{item}")

    for asset_key in ("extra_css", "extra_javascript"):
        in_section = False
        for idx, line in enumerate(lines, 1):
            if re.match(rf"^{asset_key}:\s*$", line):
                in_section = True
                continue
            if in_section:
                if line and not line[0].isspace() and not line.lstrip().startswith("#"):
                    break
                m = re.match(r"^\s+-\s+([^\s#]+)\s*(?:#.*)?$", line)
                if m:
                    val = m.group(1).strip("'\"")
                    if not val.startswith(("http://", "https://")):
                        if not (docs_build / val).is_file():
                            issues.append(
                                f"{nav_file.name}:{idx}: Asset '{val}' missing in .docs_build/"
                            )

    return issues, len(nav_paths)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate TME-Transformation repository integrity.")
    parser.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parent.parent),
        help="Repository root path (defaults to script parent directory).",
    )
    parser.add_argument(
        "--check-nav",
        metavar="MKDOCS_YML",
        help="Validate mkdocs.yml nav: entries and .docs_build/ links.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    all_issues: list[str] = []

    md_issues, md_count, link_count = check_markdown_links_and_boxes(root, github_slug, check_boxes=True)
    all_issues.extend(md_issues)

    all_issues.extend(check_list_blank_lines(root))

    csv_issues, csv_count = check_csvs(root)
    all_issues.extend(csv_issues)

    spdx_issues, spdx_count = check_spdx_headers(root)
    all_issues.extend(spdx_issues)

    nav_count = 0
    if args.check_nav:
        nav_path = (root / args.check_nav) if not os.path.isabs(args.check_nav) else Path(args.check_nav)
        nav_issues, nav_count = check_mkdocs_nav(root, nav_path)
        all_issues.extend(nav_issues)

    print(
        f"Validated {md_count} Markdown files ({link_count} relative links/anchors), "
        f"{csv_count} CSV files, {spdx_count} SPDX headers"
        + (f", {nav_count} MkDocs nav entries" if args.check_nav else "")
        + "."
    )

    if all_issues:
        print(f"Found {len(all_issues)} validation issue(s):")
        for issue in all_issues:
            print(f"  [ERROR] {issue}")
        return 1

    print("Validation passed with 0 errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
