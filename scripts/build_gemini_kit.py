#!/usr/bin/env python3
"""Build the Gemini Gem kit: a folder of at most 10 Gemini-supported files
(Gems allow 10 knowledge files and reject script files), zipped with setup
instructions. Source files are copied or grouped unchanged; grouped files keep
each original under a "## File: <path>" heading.

Run from anywhere:  python scripts/build_gemini_kit.py
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)  # stable ZIP bytes, so unchanged sources don't trigger a commit


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def bundle(paths):
    return "\n\n---\n\n".join(f"## File: {p}\n\n{read(p)}" for p in paths)


def build(kit_name, layout, instructions):
    """layout: {kit path: source path (copy) or list of source paths (group)}"""
    assert len(layout) <= 10, "Gemini Gems accept at most 10 knowledge files"
    files = {}
    for dest, src in layout.items():
        files[f"{kit_name}/{dest}"] = bundle(src) if isinstance(src, list) else read(src)
    blob = "".join(files.values())
    sources = [s for v in layout.values() for s in (v if isinstance(v, list) else [v])]
    for s in sources:
        assert read(s) in blob, f"{s} not included verbatim"
    DIST.mkdir(exist_ok=True)
    (DIST / f"{kit_name}-INSTRUCTIONS.txt").write_text(instructions, encoding="utf-8", newline="\n")
    out = DIST / f"{kit_name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for name, text in [("GEM-INSTRUCTIONS.txt", instructions), *sorted(files.items())]:
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, text.encode("utf-8"))
    print(f"Wrote {out.relative_to(ROOT)} ({len(files)} knowledge files, {out.stat().st_size:,} bytes)")


INSTRUCTIONS = """HOW TO SET UP
1. Unzip maya-gemini-gem.zip.
2. In Gemini: Gems > New Gem. Name it "Maya".
3. Paste the text below the line into Instructions.
4. Under Knowledge, upload the maya-gemini-gem folder (9 files). Save.
--------------------------------------------------------------------------
You are Maya. Your knowledge files are a structured copy of the Maya skill package. Read SKILL.md first and follow it as your core instructions; safety rules always come first. When SKILL.md refers to a file, find it as follows:
- SERVICE-AND-SAFETY-SPEC.md and references/risk-and-safety.md, therapy-concepts.md, screening-tools.md are separate files with those names.
- references/faith-christian.md, faith-grail-message.md and faith-islam.md are sections headed "## File: <path>" inside references/faith-references.md.
- sources/README.md, sources/links.md, the templates/ files and CHANGELOG.md are sections headed "## File: <path>" inside sources-templates-changelog.md.

Use sources/world-english-bible.txt and sources/clearquran-allah-edition.txt only when the person asks for or agrees to faith support. Name the translation when quoting. When quoting the Qur'an, keep the wording unchanged and credit: "Translation by Talal Itani, ClearQuran.com."

Be clear that you are an AI therapy tool, not a licensed therapist or emergency service.
"""

LAYOUT = {
    "SKILL.md": "SKILL.md",
    "SERVICE-AND-SAFETY-SPEC.md": "SERVICE-AND-SAFETY-SPEC.md",
    "references/risk-and-safety.md": "references/risk-and-safety.md",
    "references/therapy-concepts.md": "references/therapy-concepts.md",
    "references/screening-tools.md": "references/screening-tools.md",
    "references/faith-references.md": [
        "references/faith-christian.md",
        "references/faith-grail-message.md",
        "references/faith-islam.md",
    ],
    "sources-templates-changelog.md": [
        "sources/README.md",
        "sources/links.md",
        "templates/overview.md",
        "templates/session-note.md",
        "templates/referral-summary.md",
        "CHANGELOG.md",
    ],
    "sources/world-english-bible.txt": "sources/christian/world-english-bible/engwebp_vpl.txt",
    "sources/clearquran-allah-edition.txt": "sources/islam/clearquran-allah-edition/clearquran-allah-edition.txt",
}

if __name__ == "__main__":
    build("maya-gemini-gem", LAYOUT, INSTRUCTIONS)
