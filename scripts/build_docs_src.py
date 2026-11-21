# Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0).
"""Build MkDocs-ready staged source tree in .docs_build/ without modifying repo files."""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

ROOT_FILES = [
    "README.md",
    "TechAdoptionFramework.md",
    "AIAdoptionFramework.md",
    "References.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
]

ROOT_DIRS = [
    "AIFoundationalSuite",
    "ProgramDelivery",
    "Templates",
    "Examples",
    "Workshops",
]

GITHUB_BLOB_BASE = "https://github.com/tkdtaylor/TME-Transformation/blob/main"
INLINE_CODE_RE = re.compile(r"(`[^`]*`)")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def rewrite_link_target(target: str, md_dir: Path, docs_dir: Path, root: Path) -> str:
    """Rewrite directory, LICENSE, repo-only file links, and GitHub double-hyphen anchors for MkDocs."""
    stripped = target.strip()
    if not stripped or stripped.startswith(("http://", "https://", "mailto:")):
        return target

    if stripped.startswith("#"):
        return "#" + re.sub(r"-{2,}", "-", stripped[1:])

    if "#" in stripped:
        file_part, anchor = stripped.split("#", 1)
        norm_anchor = "#" + re.sub(r"-{2,}", "-", anchor)
    else:
        file_part = stripped
        norm_anchor = ""

    clean_part = file_part.rstrip("/")
    resolved = (md_dir / clean_part).resolve()

    if resolved == (docs_dir / "LICENSE").resolve() or clean_part == "LICENSE":
        new_file = f"{file_part}.md" if not file_part.endswith(".md") else file_part
    elif resolved.is_dir() and (resolved / "README.md").is_file():
        prefix = clean_part if clean_part else "."
        new_file = f"{prefix}/README.md" if prefix != "." else "README.md"
    elif not resolved.exists():
        rel_dir = md_dir.relative_to(docs_dir)
        orig_target = (root / rel_dir / clean_part).resolve()
        if orig_target.exists():
            try:
                repo_rel = orig_target.relative_to(root.resolve()).as_posix()
                return f"{GITHUB_BLOB_BASE}/{repo_rel}{norm_anchor}"
            except ValueError:
                pass
        new_file = file_part
    else:
        new_file = file_part

    return f"{new_file}{norm_anchor}"


def transform_line(line: str, md_dir: Path, docs_dir: Path, root: Path) -> str:
    """Rewrite Markdown links outside inline code spans."""
    parts = INLINE_CODE_RE.split(line)
    for idx in range(0, len(parts), 2):
        parts[idx] = LINK_RE.sub(
            lambda m: f"[{m.group(1)}]({rewrite_link_target(m.group(2), md_dir, docs_dir, root)})",
            parts[idx],
        )
    return "".join(parts)


def rewrite_markdown_tree(docs_dir: Path, root: Path) -> int:
    """Rewrite links across all .md files inside .docs_build/."""
    count = 0
    for dirpath, dirnames, filenames in os.walk(docs_dir):
        dirnames.sort()
        for fname in sorted(filenames):
            if not fname.endswith(".md"):
                continue
            md_path = Path(dirpath) / fname
            lines = md_path.read_text(encoding="utf-8").splitlines(keepends=True)
            out_lines: list[str] = []
            in_fence = False
            fence_char = ""
            for line in lines:
                stripped = line.strip()
                if stripped.startswith(("```", "~~~")):
                    marker = stripped[:3]
                    if not in_fence:
                        in_fence = True
                        fence_char = marker[0]
                    elif marker[0] == fence_char:
                        in_fence = False
                    out_lines.append(line)
                    continue
                if in_fence:
                    out_lines.append(line)
                else:
                    out_lines.append(transform_line(line, md_path.parent, docs_dir, root))
            md_path.write_text("".join(out_lines), encoding="utf-8")
            count += 1
    return count


def build_docs_src(root: Path) -> Path:
    """Populate .docs_build/ cleanly from repository root."""
    docs_dir = root / ".docs_build"
    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)

    for rel_file in ROOT_FILES:
        src = root / rel_file
        if src.is_file():
            shutil.copy2(src, docs_dir / rel_file)

    for rel_dir in ROOT_DIRS:
        src_dir = root / rel_dir
        if src_dir.is_dir():
            shutil.copytree(src_dir, docs_dir / rel_dir)

    license_src = root / "LICENSE"
    if license_src.is_file():
        license_body = license_src.read_text(encoding="utf-8").rstrip()
        (docs_dir / "LICENSE.md").write_text(
            f"# License\n\n```text\n{license_body}\n```\n",
            encoding="utf-8",
        )

    rewritten = rewrite_markdown_tree(docs_dir, root)
    print(f"Staged {rewritten} Markdown files into {docs_dir}.")
    return docs_dir


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    build_docs_src(root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
