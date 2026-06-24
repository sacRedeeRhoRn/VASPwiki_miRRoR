"""
organize.py — Bucket converted VASP-wiki markdown into reference folders,
fix internal links to point at each page's final bucketed location, and
generate index files.

Reads:
  _meta/pages.json     (per-page: title, pageid, ns, categories, revid, ...)
  _meta/slugmap.json   (title -> slug)
  references/_pages/<slug>.md   (flat converted markdown from convert.py)

Writes:
  references/<bucket>/<slug>.md   (moved + link-fixed)
  references/<bucket>/_index.md   (per-bucket page list)
  references/index.md             (master list grouped by bucket)

Buckets (first match wins, in this priority order):
  incar-tags, input-files, output-files, methods, tutorials, theory,
  categories, misc
"""

import json
import os
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

from wiki_common import _META, REFERENCES, safe_slug

# Bucket order defines priority: first matching bucket wins.
BUCKETS = [
    "incar-tags",
    "input-files",
    "output-files",
    "methods",
    "tutorials",
    "theory",
    "categories",
    "misc",
    "redirects",
]

WIKI_INDEX_BASE = "https://vasp.at/wiki/index.php"

# Known input/output file names (used by name-based fallbacks).
INPUT_FILE_NAMES = {"INCAR", "POSCAR", "POTCAR", "KPOINTS", "KPOINTS_OPT"}
OUTPUT_FILE_NAMES = {
    "OUTCAR", "OSZICAR", "CHGCAR", "CHG", "WAVECAR", "DOSCAR", "EIGENVAL",
    "PROCAR", "CONTCAR", "XDATCAR", "PARCHG", "LOCPOT", "ELFCAR", "IBZKPT",
    "PCDAT", "REPORT", "vasprun.xml", "WAVEDER", "TMPCAR", "DYNMATFULL",
    "ML_LOGFILE", "ML_ABN", "ML_FF", "BSEFATBAND",
}

# Substrings (lowercased) used to classify by category text.
_METHOD_HINTS = (
    "method", "functional", "gw", "bse", "rpa", "acfdt",
    "machine learning force field", "machine-learned force field",
    "hybrid functional", "dft+u", "vdw", "van der waals",
)
_THEORY_HINTS = ("theory", "background")
_TUTORIAL_HINTS = ("tutorial", "howto", "how to")


def _norm(s: str) -> str:
    return (s or "").replace("_", " ").lower()


def _is_incar_tag_title(title: str) -> bool:
    """Heuristic fallback: looks like an ALL-CAPS / underscore INCAR tag."""
    t = title.strip()
    if not t:
        return False
    # Allow letters, digits, underscores; must contain an uppercase letter and
    # be predominantly uppercase (tag-like, e.g. ENCUT, LREAL, NPAR, I_CONSTRAINED_M).
    if not re.fullmatch(r"[A-Z0-9_]+", t):
        return False
    return any(c.isalpha() for c in t)


def classify(page: dict) -> str:
    """Return the bucket name for *page* using the documented priority order."""
    title = page.get("title", "")
    ns = page.get("ns", 0)
    cats = page.get("categories", []) or []
    cats_norm = [_norm(c) for c in cats]
    cats_blob = " | ".join(cats_norm)

    # categories/ — namespace 14 (Category) pages always go here, but only if
    # nothing more specific applies.  Per priority, INCAR-tag etc. come first;
    # however a Category page is rarely also an INCAR tag, so we test it late.

    # 1. incar-tags
    if any("incar tag" in c for c in cats_norm):
        return "incar-tags"

    # 2. input-files
    if any("input file" in c for c in cats_norm):
        return "input-files"
    if ns == 0 and title in INPUT_FILE_NAMES:
        return "input-files"

    # 3. output-files
    if any("output file" in c for c in cats_norm):
        return "output-files"
    if ns == 0 and title in OUTPUT_FILE_NAMES:
        return "output-files"

    # 4. incar-tags heuristic (PROMOTED above the broad method-hint match):
    # an ALL-CAPS tag-like title in the main namespace that isn't a known
    # input/output file is almost certainly a parameter tag. We test it here so
    # an incidental "...method" category (e.g. "Projector-augmented-wave_method"
    # on a POTCAR_tag page like ENMIN) does not steal it into methods/.
    if ns == 0 and _is_incar_tag_title(title) and title not in INPUT_FILE_NAMES and title not in OUTPUT_FILE_NAMES:
        return "incar-tags"

    # 5. methods
    if any(h in cats_blob for h in _METHOD_HINTS):
        return "methods"

    # 6. tutorials
    if ns == 100:
        return "tutorials"
    if any(h in cats_blob for h in _TUTORIAL_HINTS):
        return "tutorials"

    # 7. theory
    if any(h in cats_blob for h in _THEORY_HINTS):
        return "theory"

    # 8. categories (namespace 14)
    if ns == 14:
        return "categories"

    # 9. misc
    return "misc"


def _h1_title(md_text: str, fallback: str) -> str:
    """Extract the first `# Heading` from converted markdown (provenance H1)."""
    m = re.search(r"^# (.+)$", md_text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return fallback


# Matches the body of a redirect stub: a "Redirect to:" marker (case-insensitive)
# appearing after the H1 title and the provenance header comments. convert.py
# emits these for MediaWiki #REDIRECT pages.
_REDIRECT_RE = re.compile(r"^\s*Redirect to:\s*$", re.IGNORECASE | re.MULTILINE)


def _is_redirect_stub(md_text: str) -> bool:
    """True if the converted page is just a redirect stub (no real content)."""
    if not _REDIRECT_RE.search(md_text):
        return False
    # Guard: a genuine article could mention the phrase, but a redirect stub is
    # tiny. Strip HTML-comment provenance lines and the H1, then check brevity.
    body = re.sub(r"<!--.*?-->", "", md_text, flags=re.DOTALL)
    body = re.sub(r"^# .+$", "", body, count=1, flags=re.MULTILINE)
    # A redirect stub's remaining body is short (just the target link line).
    return len(body.strip()) < 400


def main() -> None:
    pages_path = _META / "pages.json"
    slugmap_path = _META / "slugmap.json"
    pages_dir = REFERENCES / "_pages"

    for p in (pages_path, slugmap_path):
        if not p.exists():
            print(f"ERROR: {p} not found.")
            sys.exit(1)
    if not pages_dir.exists():
        print(f"ERROR: {pages_dir} not found. Run convert.py (full) first.")
        sys.exit(1)

    pages = json.loads(pages_path.read_text(encoding="utf-8"))
    slugmap = json.loads(slugmap_path.read_text(encoding="utf-8"))

    # slug -> page meta (only for pages that have a slug).
    slug_to_page = {}
    title_to_page = {}
    for page in pages:
        title = page.get("title")
        if not title:
            continue
        title_to_page[title] = page
        slug = slugmap.get(title)
        if slug:
            slug_to_page[slug] = page

    # slug -> bucket, for every page that has a converted markdown file.
    # Redirect stubs (body == "Redirect to: X") are routed to redirects/ so they
    # don't pollute incar-tags etc. We read each file once here and cache the
    # text for the link-fixing pass below.
    md_files = sorted(pages_dir.glob("*.md"))
    slug_to_bucket = {}
    text_cache = {}
    redirect_count = 0
    for md_path in md_files:
        slug = md_path.stem
        text = md_path.read_text(encoding="utf-8")
        text_cache[slug] = text
        if _is_redirect_stub(text):
            slug_to_bucket[slug] = "redirects"
            redirect_count += 1
            continue
        page = slug_to_page.get(slug)
        slug_to_bucket[slug] = classify(page) if page else "misc"

    # Ensure bucket dirs exist.
    for b in BUCKETS:
        (REFERENCES / b).mkdir(parents=True, exist_ok=True)

    # Reverse slugmap (slug -> title) for emitting nice titles and resolving
    # absolute wiki URLs for unfetched link targets.
    slug_to_title = {v: k for k, v in slugmap.items()}

    # Link-fix regex: matches the relative links convert.py emitted, of the
    # form ](./<slug>.md) possibly with an #anchor.
    rel_link_re = re.compile(r"\]\(\./([^)#]+?)\.md(#[^)]*)?\)")

    bucket_counts = defaultdict(int)
    bucket_entries = defaultdict(list)  # bucket -> list of (title, slug)

    for md_path in md_files:
        slug = md_path.stem
        bucket = slug_to_bucket[slug]
        text = text_cache.get(slug)
        if text is None:
            text = md_path.read_text(encoding="utf-8")

        def _fix_link(m: re.Match) -> str:
            target_slug = m.group(1)
            anchor = m.group(2) or ""
            target_bucket = slug_to_bucket.get(target_slug)
            if target_bucket is not None:
                # Compute path relative to THIS file's bucket dir.
                src_dir = REFERENCES / bucket
                tgt_file = REFERENCES / target_bucket / f"{target_slug}.md"
                rel = os.path.relpath(tgt_file, src_dir)
                rel = rel.replace(os.sep, "/")
                return f"]({rel}{anchor})"
            # Target was not fetched/converted — link to absolute wiki URL so it
            # still works online.  Recover a title from the slug if possible.
            title = slug_to_title.get(target_slug)
            if title is None:
                # Best-effort: invert safe_slug's space->underscore rule.
                title = target_slug.replace("__", "/").replace("_", " ")
            url_title = title.replace(" ", "_")
            return f"]({WIKI_INDEX_BASE}/{url_title}{anchor})"

        new_text = rel_link_re.sub(_fix_link, text)

        out_path = REFERENCES / bucket / f"{slug}.md"
        out_path.write_text(new_text, encoding="utf-8")

        page = slug_to_page.get(slug)
        title = (page or {}).get("title") or _h1_title(new_text, slug)
        bucket_counts[bucket] += 1
        bucket_entries[bucket].append((title, slug))

        # Remove the staging copy once moved.
        try:
            md_path.unlink()
        except OSError:
            pass

    # Per-bucket _index.md.
    for bucket in BUCKETS:
        entries = sorted(bucket_entries.get(bucket, []), key=lambda e: e[0].lower())
        lines = [f"# {bucket}", ""]
        if entries:
            for title, slug in entries:
                lines.append(f"- [{title}]({slug}.md)")
        else:
            lines.append("_(no pages)_")
        lines.append("")
        (REFERENCES / bucket / "_index.md").write_text("\n".join(lines), encoding="utf-8")

    # Master index.md.
    total = sum(bucket_counts.values())
    idx = [
        "# VASP Wiki — Offline Reference Index",
        "",
        f"Snapshot: {date.today().isoformat()}  ·  {total} pages  ·  GFDL 1.2 from vasp.at",
        "",
    ]
    for bucket in BUCKETS:
        entries = sorted(bucket_entries.get(bucket, []), key=lambda e: e[0].lower())
        if not entries:
            continue
        idx.append(f"## {bucket} ({len(entries)})")
        idx.append("")
        for title, slug in entries:
            idx.append(f"- [{title}]({bucket}/{slug}.md)")
        idx.append("")
    (REFERENCES / "index.md").write_text("\n".join(idx), encoding="utf-8")

    # Remove the now-empty staging dir.
    try:
        pages_dir.rmdir()
    except OSError:
        pass

    # Histogram.
    print("Bucket histogram:")
    width = max((len(b) for b in BUCKETS), default=0)
    for bucket in BUCKETS:
        c = bucket_counts.get(bucket, 0)
        bar = "#" * min(c, 60)
        print(f"  {bucket.ljust(width)}  {str(c).rjust(5)}  {bar}")
    print(f"  {'TOTAL'.ljust(width)}  {str(total).rjust(5)}")
    print(f"\n{redirect_count} redirect stub(s) routed to redirects/.")
    print(f"Wrote references/index.md and per-bucket _index.md files.")


if __name__ == "__main__":
    main()
