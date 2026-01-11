#!/usr/bin/env python3
"""Update category index.html topics arrays based on folder contents."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SKIP_DIRS = {".git", ".githooks", "__pycache__"}


def title_from_filename(filename):
    stem = Path(filename).stem
    text = stem.replace("_", " ").replace("-", " ")
    words = [w for w in text.split() if w]
    return " ".join(words).title()


def build_topics_entries(files):
    lines = []
    for file_path in files:
        title = title_from_filename(file_path.name)
        lines.append(f'    {{ file: "{file_path.name}", title: "{title}" }},')
    return "\n".join(lines)


def update_index(index_path):
    text = index_path.read_text(encoding="utf-8")
    pattern = re.compile(r"(const topics = \[)(.*?)(\n\s*\];)", re.S)

    files = sorted(
        [p for p in index_path.parent.glob("*.html") if p.name != "index.html"],
        key=lambda p: p.name.lower(),
    )
    entries = build_topics_entries(files)

    replacement = r"\1"
    if entries:
        replacement += "\n" + entries
    replacement += r"\3"

    new_text, count = pattern.subn(replacement, text, count=1)
    if count == 0:
        print(f"WARNING: topics array not found in {index_path}")
        return False

    if new_text != text:
        index_path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main():
    updated = 0
    checked = 0

    for path in sorted(ROOT.iterdir(), key=lambda p: p.name.lower()):
        if not path.is_dir():
            continue
        if path.name in SKIP_DIRS or path.name.startswith("."):
            continue

        index_path = path / "index.html"
        if not index_path.exists():
            continue

        checked += 1
        if update_index(index_path):
            updated += 1

    print(f"Checked {checked} folders. Updated {updated} index files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
