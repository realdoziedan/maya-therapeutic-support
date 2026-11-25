# Changelog

Versions follow semantic versioning: major for incompatible behavior or structure, minor for backward-compatible capability, patch for corrections. Entries are drawn from the repository's commit history.

## 1.3.0 — 2026-11-25
- Licensed the package under CC BY-NC 4.0 (`LICENSE`). Bundled scripture texts keep their own terms.
- Rewrote the skill description in SKILL.md frontmatter to present Maya as an AI therapy tool (not a licensed therapist or emergency service) and to say when to use it.
- README now opens with what Maya does and sample prompts, corrects the outdated note that no religious texts are bundled, and adds a License section.

## 1.2.0 — 2026-11-25
- Bundled two openly licensed texts, unchanged, with their publishers' notices: the World English Bible (public domain, eBible.org) in `sources/christian/world-english-bible/` and the ClearQuran Allah Edition by Talal Itani (CC BY-ND 4.0) in `sources/islam/clearquran-allah-edition/`.
- Updated the sources READMEs and links to record each text's edition, licence, credit line, and download date. The NKJV and Grail Message texts remain unbundled because their copyright does not allow redistribution.

## 1.1.0 — 2026-11-25
- Added a single-file edition (`dist/maya-therapeutic-support-single.md`) for platforms that accept only one skill file. It bundles SKILL.md with the safety spec, references, sources notes, templates, and this changelog, unchanged.
- Added `scripts/build_single_file.py` to regenerate the single file and a GitHub Action that rebuilds it on pushes to main.
- Grounded the Grail Message notes in the publisher's outline and added official Grail Message study references.
- Clarified conditional Google Drive source access.
- Identified the reviewed ClearQuran translation and its terms, the NKJV edition and its quotation guidance, and the reviewed Grail Message edition and rights.
- Added edition-specific religious source references and clarified religious source access and rights.

## 1.0.1 — 2026-11-24
- Documented and improved source-aware faith guidance.
- Added installation and upload instructions and documented the Skills CLI requirement.

## 1.0.0 — 2026-11-24
- Initial Maya therapeutic support skill package.
