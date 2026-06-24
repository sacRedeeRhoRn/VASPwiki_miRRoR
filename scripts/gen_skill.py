"""
gen_skill.py — Emit SKILL.md (bundle router) and _meta/provenance.md.

Counts are derived from the actual bucketed reference tree under references/
(produced by organize.py); falls back to classifying pages.json if the tree
is not present yet.  Run AFTER organize.py for accurate per-bucket counts.
"""

import json
from datetime import date
from pathlib import Path

from wiki_common import BASE_DIR, _META, REFERENCES

# Reuse the canonical bucket order + classifier from organize.py.
from organize import BUCKETS, classify

SNAPSHOT = date.today().isoformat()
SOURCE_BASE = "https://vasp.at/wiki/"


def count_buckets() -> tuple[dict[str, int], int]:
    """
    Count pages per bucket.  Prefer the real bucketed tree (references/<bucket>/
    *.md, excluding _index.md).  If buckets are empty, fall back to classifying
    pages.json so provenance still has numbers.
    """
    counts = {b: 0 for b in BUCKETS}
    total = 0
    have_tree = False
    for b in BUCKETS:
        d = REFERENCES / b
        if not d.exists():
            continue
        n = sum(1 for p in d.glob("*.md") if p.name != "_index.md")
        counts[b] = n
        total += n
        if n:
            have_tree = True

    if have_tree:
        return counts, total

    # Fallback: classify fetched pages from pages.json.
    pages_path = _META / "pages.json"
    if pages_path.exists():
        pages = json.loads(pages_path.read_text(encoding="utf-8"))
        for page in pages:
            if "fetched_at" not in page:
                continue
            counts[classify(page)] += 1
            total += 1
    return counts, total


def total_indexed_pages() -> int:
    pages_path = _META / "pages.json"
    if not pages_path.exists():
        return 0
    return len(json.loads(pages_path.read_text(encoding="utf-8")))


def write_skill(counts: dict[str, int], total: int) -> Path:
    description = (
        "Use when answering any question about VASP setup, an INCAR tag's "
        "meaning / default / allowed options, input or output file formats "
        "(POSCAR, KPOINTS, OUTCAR, CHGCAR, ...), a calculation method or "
        "workflow (GW, BSE, RPA, hybrid functionals, machine-learned force "
        "fields), or a step-by-step tutorial: this bundle is an offline mirror "
        "of the full VASP wiki (vasp.at) covering INCAR tags, input/output file "
        "formats, methods, and tutorials."
    )

    lines = []
    lines.append("---")
    lines.append("name: vasp-wiki")
    lines.append(f"description: {description}")
    lines.append("---")
    lines.append("")
    lines.append("# VASP Wiki (offline mirror)")
    lines.append("")
    lines.append(
        f"Offline snapshot of the VASP wiki (<{SOURCE_BASE}>), taken "
        f"{SNAPSHOT}, {total} pages. Content is GFDL 1.2, © VASP wiki "
        "contributors. Each reference file carries its own source URL + revid "
        "in an HTML-comment header."
    )
    lines.append("")
    lines.append(
        "This is a ROUTER, not a content dump. Find the one reference file that "
        "answers the question and open ONLY that file — do not load the whole "
        "bundle."
    )
    lines.append("")
    lines.append("## How to navigate")
    lines.append("")
    lines.append(
        "- **INCAR tag** (e.g. ENCUT, ISMEAR, ALGO) → "
        "`references/incar-tags/<TAG>.md`"
    )
    lines.append(
        "- **Input file** (POSCAR, KPOINTS, POTCAR, INCAR) → "
        "`references/input-files/<NAME>.md`"
    )
    lines.append(
        "- **Output file** (OUTCAR, OSZICAR, CHGCAR, vasprun.xml, DOSCAR) → "
        "`references/output-files/<NAME>.md`"
    )
    lines.append(
        "- **Method / functional / workflow** (GW, BSE, RPA, ACFDT, hybrid "
        "functionals, machine-learned force fields) → `references/methods/`"
    )
    lines.append(
        "- **Step-by-step tutorial / how-to** → `references/tutorials/`"
    )
    lines.append(
        "- **Theory / background** → `references/theory/`"
    )
    lines.append(
        "- **Category landing pages** → `references/categories/`"
    )
    lines.append(
        "- **Anything else** → `references/misc/`"
    )
    lines.append("")
    lines.append(
        "If you don't know the exact filename, open `references/index.md` "
        "(master list grouped by bucket) or a bucket's `_index.md` and pick the "
        "page, then open that file."
    )
    lines.append("")
    lines.append("## Bucket sizes")
    lines.append("")
    for b in BUCKETS:
        lines.append(f"- `{b}/` — {counts.get(b, 0)} pages")
    lines.append("")
    lines.append(
        "Internal `[[links]]` between pages are relative paths within "
        "`references/`; links to pages not in this snapshot point to the live "
        f"wiki at <{SOURCE_BASE}>."
    )
    lines.append("")

    out = BASE_DIR / "SKILL.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def write_provenance(counts: dict[str, int], total: int, indexed: int) -> Path:
    lines = []
    lines.append("# Provenance — VASP Wiki Offline Mirror")
    lines.append("")
    lines.append(f"- **Source base:** {SOURCE_BASE}")
    lines.append(f"- **Snapshot date:** {SNAPSHOT}")
    lines.append(f"- **Pages indexed (crawl):** {indexed}")
    lines.append(f"- **Pages mirrored (converted + bucketed):** {total}")
    lines.append("")
    lines.append("## License & attribution")
    lines.append("")
    lines.append(
        "Content is reproduced from the VASP wiki (https://vasp.at/wiki/) and "
        "is licensed under the **GNU Free Documentation License, Version 1.2 "
        "(GFDL 1.2)**. Copyright © the VASP wiki contributors. This is an "
        "unofficial offline mirror created for research convenience; it is not "
        "affiliated with or endorsed by the VASP group. No image binaries are "
        "redistributed — image references point at the live wiki."
    )
    lines.append("")
    lines.append(
        "Each reference markdown file begins with an HTML-comment header "
        "carrying its own per-page source URL and MediaWiki revision id "
        "(revid), plus the GFDL 1.2 notice, e.g.:"
    )
    lines.append("")
    lines.append("```")
    lines.append(
        "<!-- Source: https://vasp.at/wiki/index.php/ENCUT | revid: NNNNN | "
        "retrieved: YYYY-MM-DD -->"
    )
    lines.append(
        "<!-- © VASP wiki contributors. Licensed under GNU Free Documentation "
        "License 1.2 (GFDL 1.2). -->"
    )
    lines.append("```")
    lines.append("")
    lines.append("## Per-bucket page counts")
    lines.append("")
    lines.append("| Bucket | Pages |")
    lines.append("| --- | ---: |")
    for b in BUCKETS:
        lines.append(f"| {b} | {counts.get(b, 0)} |")
    lines.append(f"| **total** | **{total}** |")
    lines.append("")

    out = _META / "provenance.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> None:
    counts, total = count_buckets()
    indexed = total_indexed_pages()
    skill_path = write_skill(counts, total)
    prov_path = write_provenance(counts, total, indexed)
    print(f"Wrote {skill_path}")
    print(f"Wrote {prov_path}")
    print(f"Snapshot {SNAPSHOT}: {total} mirrored / {indexed} indexed pages.")
    for b in BUCKETS:
        print(f"  {b}: {counts.get(b, 0)}")


if __name__ == "__main__":
    main()
