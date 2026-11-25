#!/usr/bin/env python3
"""Build dist/maya-therapeutic-support-single.md: SKILL.md plus the supporting
files, concatenated unchanged, for platforms that accept only one skill file.

Run from anywhere:  python scripts/build_single_file.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "maya-therapeutic-support-single.md"

# Load order follows manifest.json. Packaging/setup notes (README,
# REVIEW-AND-DELIVERY, adapters/, manifest.json) are not Maya's instructions
# and are left out.
FILES = [
    "SERVICE-AND-SAFETY-SPEC.md",
    "references/risk-and-safety.md",
    "references/therapy-concepts.md",
    "references/screening-tools.md",
    "references/faith-christian.md",
    "references/faith-grail-message.md",
    "references/faith-islam.md",
    "sources/README.md",
    "sources/links.md",
    "templates/overview.md",
    "templates/session-note.md",
    "templates/referral-summary.md",
    "CHANGELOG.md",
]

NOTE = (
    "\n\n---\n\n# Bundled reference files\n\n"
    "This single-file edition contains the files below in full, unchanged. "
    "Where the instructions point to a file path (for example "
    "references/risk-and-safety.md), use the section with that path as its heading.\n"
)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def main() -> None:
    version = json.loads(read("manifest.json"))["version"]
    note = NOTE.replace("# Bundled reference files\n\n", f"# Bundled reference files\n\nVersion {version} (from manifest.json).\n\n", 1)
    parts = [read("SKILL.md"), note]
    for rel in FILES:
        parts.append(f"\n\n---\n\n## File: {rel}\n\n")
        parts.append(read(rel))
    text = "".join(parts)
    for rel in ["SKILL.md", *FILES]:
        assert read(rel) in text, f"{rel} not included verbatim"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(text.encode('utf-8')):,} bytes)")


if __name__ == "__main__":
    main()
