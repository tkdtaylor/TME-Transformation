# Copyright 2026 The TME-Transformation Authors. Licensed under CC-BY-4.0 (SPDX-License-Identifier: CC-BY-4.0).
"""Build downloadable starter-kit .zip release bundles without third-party dependencies."""

from __future__ import annotations

import argparse
import os
import sys
import zipfile
from pathlib import Path

SKIP_NAMES = {".DS_Store", "Thumbs.db", "__pycache__"}
SKIP_SUFFIXES = (".pyc", ".pyo", ".swp", ".swo")

BUNDLES: list[tuple[str, list[str]]] = [
    (
        "TME-AI-Foundational-Suite",
        ["AIFoundationalSuite", "AIAdoptionFramework.md", "References.md", "LICENSE"],
    ),
    (
        "TME-Templates-and-Program-Delivery",
        ["Templates", "ProgramDelivery", "Examples", "LICENSE"],
    ),
    (
        "TME-Workshops",
        ["Workshops", "AIAdoptionFramework.md", "TechAdoptionFramework.md", "LICENSE"],
    ),
]


def add_path_to_zip(zf: zipfile.ZipFile, src: Path, arc_prefix: Path) -> int:
    """Add a file or directory tree into zf under arc_prefix and return file count."""
    count = 0
    if src.is_file():
        if src.name in SKIP_NAMES or src.name.endswith(SKIP_SUFFIXES):
            return 0
        zf.write(src, arc_prefix.as_posix())
        return 1

    if src.is_dir():
        for dirpath, dirnames, filenames in os.walk(src):
            dirnames[:] = sorted(d for d in dirnames if d not in SKIP_NAMES and not d.startswith("."))
            rel_dir = Path(dirpath).relative_to(src)
            for fname in sorted(filenames):
                if fname in SKIP_NAMES or fname.endswith(SKIP_SUFFIXES):
                    continue
                file_path = Path(dirpath) / fname
                arc_name = arc_prefix / rel_dir / fname
                zf.write(file_path, arc_name.as_posix())
                count += 1
    return count


def build_bundles(root: Path, out_dir: Path) -> list[tuple[Path, int, int]]:
    """Create starter-kit .zip archives in out_dir and return metadata tuples."""
    out_dir.mkdir(parents=True, exist_ok=True)
    results: list[tuple[Path, int, int]] = []

    for bundle_name, entries in BUNDLES:
        zip_path = out_dir / f"{bundle_name}.zip"
        file_count = 0
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for entry in entries:
                src = root / entry
                if not src.exists():
                    raise FileNotFoundError(f"Missing bundle source path: {src}")
                file_count += add_path_to_zip(zf, src, Path(bundle_name) / entry)
        size_bytes = zip_path.stat().st_size
        results.append((zip_path, file_count, size_bytes))
        print(f"Created {zip_path} ({file_count} files, {size_bytes} bytes)")

    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Build TME-Transformation release .zip bundles.")
    parser.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parent.parent),
        help="Repository root directory.",
    )
    parser.add_argument(
        "--out-dir",
        default="dist",
        help="Output directory for generated .zip archives (default: dist).",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = root / out_dir

    build_bundles(root, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
