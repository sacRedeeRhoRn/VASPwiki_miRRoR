#!/usr/bin/env python3
"""
convert_citations.py — Convert MediaWiki citation anchors in references/**/*.md
into GitHub-native footnotes ([^label]), recovering reference text from
_raw/html/<slug>.html via pandoc.

Usage:
    python convert_citations.py --prototype [--apply]
    python convert_citations.py --all [--apply]
    python convert_citations.py --fix-anchors [--apply]
"""

from __future__ import annotations

import argparse
import html as html_mod
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterator

# ---------------------------------------------------------------------------
# Repo constants (absolute paths only)
# ---------------------------------------------------------------------------

REPO_ROOT = Path("/Users/sacRedeeRhoRn/Sanctum/area2_develop/vasp-wiki")
REFERENCES_DIR = REPO_ROOT / "references"
HTML_DIR = REPO_ROOT / "_raw" / "html"
SLUGMAP_PATH = REPO_ROOT / "_meta" / "slugmap.json"
PANDOC_BIN = "/opt/homebrew/bin/pandoc"

PROTOTYPE_FILES = [
    REFERENCES_DIR / "theory" / "VASP_from_a_Gaussian-type_orbitals_perspective.md",
    REFERENCES_DIR / "incar-tags" / "GGA.md",
    REFERENCES_DIR / "incar-tags" / "METAGGA.md",
]

# ---------------------------------------------------------------------------
# HTML slug resolution
# ---------------------------------------------------------------------------

_slugmap_cache: dict[str, str] | None = None


def _load_slugmap() -> dict[str, str]:
    global _slugmap_cache
    if _slugmap_cache is None:
        with open(SLUGMAP_PATH, encoding="utf-8") as f:
            _slugmap_cache = json.load(f)
    return _slugmap_cache


def resolve_html_path(md_path: Path) -> Path | None:
    """Return the matching HTML file path or None if not found."""
    basename = md_path.stem  # strip .md
    candidate = HTML_DIR / f"{basename}.html"
    if candidate.exists():
        return candidate

    # Reverse lookup via slugmap: slugmap maps title -> slug.
    # Slug corresponds to html filename stem.  Try to find a slug whose
    # value matches the md basename, then look for html/<slug>.html.
    slugmap = _load_slugmap()
    for _title, slug in slugmap.items():
        if slug == basename:
            alt = HTML_DIR / f"{slug}.html"
            if alt.exists():
                return alt

    return None


# ---------------------------------------------------------------------------
# HTML reference extraction
# ---------------------------------------------------------------------------

# Match <li id="cite_note-..."> or <li id="cite&#95;note-...">
_LI_CITE_NOTE_RE = re.compile(
    r'<li\s+id="cite(?:&#95;|_)note-(?P<id>[^"]+)"[^>]*>',
    re.IGNORECASE,
)

# Reference-text span — capture content up to first </span>
# Reference-text spans do not nest same-class spans, so non-greedy is safe.
_REF_TEXT_SPAN_RE = re.compile(
    r'<span\s+class="reference-text">(.*?)</span>',
    re.DOTALL | re.IGNORECASE,
)


def _run_pandoc(html_snippet: str) -> str:
    """Convert an HTML snippet to GFM markdown via pandoc."""
    result = subprocess.run(
        [PANDOC_BIN, "-f", "html", "-t", "gfm-raw_html"],
        input=html_snippet,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(f"pandoc failed: {result.stderr.strip()}")
    # Collapse internal newlines and strip trailing whitespace
    md = result.stdout.strip()
    md = re.sub(r"\s*\n\s*", " ", md)
    return md


def extract_html_refs(html_path: Path) -> dict[str, str]:
    """
    Parse the HTML file and return an ordered dict of:
        cite_note_id -> markdown_text

    The id here is the raw string after "cite_note-" (e.g. "dion:prl:2004-1").
    """
    html = html_path.read_text(encoding="utf-8")
    refs: dict[str, str] = {}

    # Find all list items with cite_note ids
    for m in _LI_CITE_NOTE_RE.finditer(html):
        raw_id = html_mod.unescape(m.group("id"))
        # Search for reference-text span within this li block.
        # Grab from match end forward up to next </li> (greedy enough for
        # typical MW HTML, but we need the reference-text span).
        tail = html[m.end():]
        # Find closing </li> — take the first one (MW doesn't nest <li>s)
        li_close = tail.find("</li>")
        if li_close == -1:
            li_body = tail
        else:
            li_body = tail[: li_close + 5]

        sm = _REF_TEXT_SPAN_RE.search(li_body)
        if sm is None:
            continue

        inner_html = sm.group(1).strip()
        if not inner_html:
            continue

        try:
            md_text = _run_pandoc(inner_html)
        except RuntimeError:
            continue

        if raw_id not in refs:  # preserve order; first occurrence wins
            refs[raw_id] = md_text

    return refs


# ---------------------------------------------------------------------------
# Label sanitisation
# ---------------------------------------------------------------------------

def sanitize_label(raw_id: str) -> str:
    """Convert a raw cite_note id fragment to a safe GFM footnote label."""
    # Replace spaces and ] with hyphens; colons/dots/hyphens are fine in GFM
    label = re.sub(r"[ \]]", "-", raw_id)
    return label


# ---------------------------------------------------------------------------
# Inline citation transformation (body)
# ---------------------------------------------------------------------------

# Matches <sup ...>...</sup> with DOTALL — captures all cite_note fragments
_SUP_RE = re.compile(r"<sup\b[^>]*>.*?</sup>", re.DOTALL)

# Extract all #cite_note-<id> fragments from inside a sup block
# Handles both: [\[N\]](#cite_note-ID)  and  <a href="#cite_note-ID">
_CITE_NOTE_FRAG_RE = re.compile(r"#cite_note-([^\"\)]+)")


def transform_inline_citations(
    text: str,
) -> tuple[str, list[str], dict[str, str]]:
    """
    Replace all <sup>...</sup> blocks that contain #cite_note- references
    with [^LABEL] footnote markers.

    Returns:
        (transformed_text, ordered_list_of_labels_seen, raw_id_to_label_map)

    The raw_id_to_label_map maps the raw fragment id -> sanitized label
    (with collision suffixes applied).
    """
    id_to_label: dict[str, str] = {}       # raw_id -> label (persistent)
    label_counts: dict[str, int] = {}       # base_label -> count for dedup
    labels_in_order: list[str] = []

    def _label_for(raw_id: str) -> str:
        if raw_id in id_to_label:
            return id_to_label[raw_id]
        base = sanitize_label(raw_id)
        if base not in label_counts:
            label_counts[base] = 0
            chosen = base
        else:
            label_counts[base] += 1
            suffix = chr(ord("b") + label_counts[base] - 1)
            chosen = f"{base}-{suffix}"
        id_to_label[raw_id] = chosen
        return chosen

    def _replace_sup(m: re.Match) -> str:
        sup_text = m.group(0)
        frags = _CITE_NOTE_FRAG_RE.findall(sup_text)
        if not frags:
            # No cite_note references — leave unchanged
            return sup_text
        replacement = ""
        for raw_id in frags:
            label = _label_for(raw_id)
            if label not in labels_in_order:
                labels_in_order.append(label)
            replacement += f"[^{label}]"
        return replacement

    transformed = _SUP_RE.sub(_replace_sup, text)
    return transformed, labels_in_order, id_to_label


# ---------------------------------------------------------------------------
# References list removal
# ---------------------------------------------------------------------------

def remove_references_block(text: str) -> str:
    r"""
    Remove the contiguous numbered list of citation list items (those
    containing #cite_ref-) from the bottom of the file, and optionally
    the preceding References/Bibliography/Notes heading.

    Strategy:
    1. Find first line containing #cite_ref-.
    2. Walk back to find the start of its enclosing numbered list item
       (line matching ^\d+\.\s).
    3. Walk forward through all consecutive citation list items
       (items and their continuation lines) until we hit content that
       belongs neither to the list nor to blank/indented continuation.
    4. Remove that span.
    5. Remove preceding references heading if now empty under it.
    """
    lines = text.split("\n")
    n = len(lines)

    # Step 1: find any cite_ref line
    first_cite_ref_idx: int | None = None
    for i, line in enumerate(lines):
        if "#cite_ref-" in line:
            first_cite_ref_idx = i
            break

    if first_cite_ref_idx is None:
        return text  # nothing to remove

    # Regex for top-level numbered list item
    ITEM_RE = re.compile(r"^\d+\.\s")

    # Step 2: walk back to the enclosing list item start
    item_start = first_cite_ref_idx
    while item_start > 0 and not ITEM_RE.match(lines[item_start]):
        item_start -= 1

    # Step 3: walk forward through all consecutive citation list items
    # We collect the full span: [item_start .. block_end) inclusive.
    # A new numbered item starts at a line matching ITEM_RE.
    # An item "belongs" to the citation block if its gathered lines contain
    # #cite_ref-.  We scan item by item.
    # The block also includes blank lines between items and continuation
    # lines (indented or blank).

    def gather_item(start: int) -> tuple[int, bool]:
        """
        From `start` (a line matching ITEM_RE), gather forward until the
        next ITEM_RE line or a non-indented, non-blank line that isn't
        a continuation.
        Returns (end_exclusive, is_citation_item).
        """
        end = start + 1
        while end < n:
            line = lines[end]
            if ITEM_RE.match(line):
                break  # next list item
            # Continuation: blank or indented (leading whitespace)
            if line == "" or line.startswith(" ") or line.startswith("\t"):
                end += 1
                continue
            # Non-blank, non-indented line that isn't a new numbered item
            break
        body = "\n".join(lines[start:end])
        is_citation = "#cite_ref-" in body
        return end, is_citation

    # Start scanning from item_start
    pos = item_start
    block_end = item_start  # exclusive end of citation block

    while pos < n:
        if not ITEM_RE.match(lines[pos]):
            break
        end, is_citation = gather_item(pos)
        if is_citation:
            block_end = end
            pos = end
        else:
            break

    # Step 3b: consume trailing blank lines that belong to the block
    while block_end < n and lines[block_end].strip() == "":
        block_end += 1

    if block_end <= item_start:
        return text  # nothing found

    # Step 5: check for preceding references heading
    heading_re = re.compile(
        r"^#{1,3}\s+.*?\bReferences\b|"
        r"^#{1,3}\s+.*?\bBibliography\b|"
        r"^#{1,3}\s+.*?\bNotes\b",
        re.IGNORECASE,
    )
    # Find the heading immediately before item_start, skipping blanks
    heading_idx: int | None = None
    scan = item_start - 1
    while scan >= 0 and lines[scan].strip() == "":
        scan -= 1
    if scan >= 0 and heading_re.match(lines[scan]):
        heading_idx = scan

    # Build new lines
    if heading_idx is not None:
        # Remove heading + any blank lines between heading and block
        remove_start = heading_idx
    else:
        remove_start = item_start

    # Remove blank lines immediately before remove_start
    while remove_start > 0 and lines[remove_start - 1].strip() == "":
        remove_start -= 1

    new_lines = lines[:remove_start] + lines[block_end:]
    return "\n".join(new_lines)


# ---------------------------------------------------------------------------
# Footnote definition assembly
# ---------------------------------------------------------------------------

def build_footnote_defs(
    labels_in_order: list[str],
    id_to_label: dict[str, str],
    html_refs: dict[str, str],
) -> tuple[list[tuple[str, str]], list[str]]:
    """
    Build ordered list of (label, markdown_text) footnote definitions.

    Also returns a list of orphan labels (referenced in body but missing
    in html_refs).

    html_refs is keyed by raw id (e.g. "dion:prl:2004-1").
    id_to_label maps raw_id -> label.
    labels_in_order is the unique ordered list of labels referenced in body.
    """
    # Build reverse: label -> raw_id
    label_to_raw: dict[str, str] = {v: k for k, v in id_to_label.items()}

    defs: list[tuple[str, str]] = []
    orphans: list[str] = []
    seen_labels: set[str] = set()

    for label in labels_in_order:
        if label in seen_labels:
            continue
        seen_labels.add(label)
        raw_id = label_to_raw.get(label)
        if raw_id is None:
            orphans.append(label)
            continue
        if raw_id not in html_refs:
            orphans.append(label)
            continue
        defs.append((label, html_refs[raw_id]))

    return defs, orphans


# ---------------------------------------------------------------------------
# Per-page validation
# ---------------------------------------------------------------------------

def validate_page(
    transformed_body: str,
    defs: list[tuple[str, str]],
    labels_in_order: list[str],
) -> list[str]:
    """
    Run all per-page checks. Returns list of failure reasons (empty = pass).
    """
    errors: list[str] = []

    # 0: no remaining cite_note anchors
    if "#cite_note-" in transformed_body:
        errors.append("remaining #cite_note- in transformed text")

    # 1: no remaining cite_ref anchors
    if "#cite_ref-" in transformed_body:
        errors.append("remaining #cite_ref- in transformed text")

    # 2 & 3: every referenced label has exactly one def; every def is used
    def_labels = {label for label, _ in defs}
    ref_labels = set(labels_in_order)

    missing = ref_labels - def_labels
    if missing:
        errors.append(f"missing defs for labels: {sorted(missing)}")

    unused = def_labels - ref_labels
    if unused:
        errors.append(f"unused defs for labels: {sorted(unused)}")

    # 4: no empty or space-containing labels
    for label in ref_labels | def_labels:
        if not label:
            errors.append("empty label detected")
        if " " in label:
            errors.append(f"label contains space: {label!r}")

    # 5: check that each [^LABEL] in body matches a def (bijection check)
    body_refs = set(re.findall(r"\[\^([^\]]+)\](?!:)", transformed_body))
    for br in body_refs:
        if br not in def_labels:
            errors.append(f"body references [^{br}] but no def found")

    return errors


# ---------------------------------------------------------------------------
# Full per-page pipeline
# ---------------------------------------------------------------------------

class PageResult:
    __slots__ = (
        "md_path",
        "skipped",
        "skip_reason",
        "inline_count",
        "defs_count",
        "before_excerpt",
        "after_excerpt",
        "def_excerpts",
        "transformed_text",
    )

    def __init__(self, md_path: Path) -> None:
        self.md_path = md_path
        self.skipped = False
        self.skip_reason: str = ""
        self.inline_count = 0
        self.defs_count = 0
        self.before_excerpt: str = ""
        self.after_excerpt: str = ""
        self.def_excerpts: list[str] = []
        self.transformed_text: str = ""


def process_page(md_path: Path) -> PageResult:
    """
    Full pipeline for a single .md file.
    Returns a PageResult; if skipped, transformed_text is empty.
    """
    result = PageResult(md_path)

    # --- Resolve HTML ---
    html_path = resolve_html_path(md_path)
    if html_path is None:
        result.skipped = True
        result.skip_reason = "no matching html"
        return result

    # --- Extract html refs ---
    try:
        html_refs = extract_html_refs(html_path)
    except Exception as e:
        result.skipped = True
        result.skip_reason = f"html parse error: {e}"
        return result

    # --- Read md ---
    original_text = md_path.read_text(encoding="utf-8")

    # Early exit: if no cite_note at all, skip cleanly (nothing to do)
    if "#cite_note-" not in original_text and "#cite_ref-" not in original_text:
        result.skipped = True
        result.skip_reason = "no citations found"
        return result

    # --- Capture a before-excerpt (first sup containing a real #cite_note-) ---
    first_cite_sup: re.Match | None = None
    for _sup_m in _SUP_RE.finditer(original_text):
        if "#cite_note-" in _sup_m.group(0):
            first_cite_sup = _sup_m
            break
    if first_cite_sup is not None:
        result.before_excerpt = first_cite_sup.group(0)[:120]

    # --- Transform inline citations ---
    transformed_body, labels_in_order, id_to_label = transform_inline_citations(
        original_text
    )
    result.inline_count = len(labels_in_order)

    # --- Capture after-excerpt (same citation sup, shown as its replacement) ---
    if first_cite_sup is not None:
        # Extract the raw_ids from the BEFORE sup and build the [^label]... token(s)
        # that the transformation produced for exactly that sup.
        before_frags = _CITE_NOTE_FRAG_RE.findall(first_cite_sup.group(0))
        if before_frags:
            after_tokens = "".join(
                f"[^{sanitize_label(frag)}]" for frag in before_frags
            )
            result.after_excerpt = after_tokens[:120]

    # --- Remove references block ---
    transformed_body = remove_references_block(transformed_body)

    # --- Build footnote defs ---
    defs, orphans = build_footnote_defs(labels_in_order, id_to_label, html_refs)
    if orphans:
        result.skipped = True
        result.skip_reason = f"orphan ref(s): {', '.join(orphans)}"
        return result

    result.defs_count = len(defs)

    # --- Assemble final text ---
    # Strip trailing whitespace/newlines, then add defs
    final_body = transformed_body.rstrip("\n")
    if defs:
        def_lines = [f"[^{label}]: {text}" for label, text in defs]
        result.def_excerpts = def_lines[:2]
        final_text = final_body + "\n\n" + "\n".join(def_lines) + "\n"
    else:
        final_text = final_body + "\n"

    # --- Validate ---
    # For validation, extract labels from the final_text body (before defs section)
    errors = validate_page(final_text, defs, labels_in_order)
    if errors:
        result.skipped = True
        result.skip_reason = "validation failed: " + "; ".join(errors)
        return result

    result.transformed_text = final_text
    return result


# ---------------------------------------------------------------------------
# MD files discovery
# ---------------------------------------------------------------------------

def iter_md_files(paths: list[Path] | None = None) -> Iterator[Path]:
    """Yield .md files to process. If paths given, yield those; else all under references/."""
    if paths:
        for p in paths:
            yield p
    else:
        for p in sorted(REFERENCES_DIR.rglob("*.md")):
            yield p


# ---------------------------------------------------------------------------
# Non-citation anchor fix
# ---------------------------------------------------------------------------

def _github_heading_slug(text: str) -> str:
    """Compute GitHub heading slug from heading text."""
    # Cut at the MediaWiki edit-link marker if the <a> tag is incomplete
    # (heading text may be truncated at a line boundary before </a> appears).
    m = re.search(r'\\?\[?<a\b', text, re.IGNORECASE)
    if m:
        text = text[:m.start()]
    # Strip trailing edit-link HTML cruft: [...<a ...>edit</a>...]
    text = re.sub(r"\[?<a\b[^>]*>.*?</a>\s*\]?", "", text, flags=re.DOTALL)
    # Strip remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Strip markdown backslash escapes
    text = text.replace("\\", "")
    # Lowercase
    text = text.lower()
    # Keep only alphanumeric, spaces, hyphens
    text = re.sub(r"[^\w\s\-]", "", text, flags=re.UNICODE)
    # Replace spaces with hyphens
    text = re.sub(r"\s+", "-", text.strip())
    # Collapse multiple hyphens
    text = re.sub(r"-+", "-", text)
    return text


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)", re.MULTILINE)
_INTRAPAGE_LINK_RE = re.compile(r"\(#([^)]+)\)")


def fix_anchors_in_file(
    text: str,
) -> tuple[str, int, list[str]]:
    """
    Fix intra-page anchor links that don't match any heading slug.

    Returns (new_text, fix_count, dead_anchors).
    """
    # Build heading slugs
    heading_slugs: list[str] = []
    for m in _HEADING_RE.finditer(text):
        heading_text = m.group(2)
        slug = _github_heading_slug(heading_text)
        if slug:
            heading_slugs.append(slug)

    heading_slug_set = set(heading_slugs)

    fix_count = 0
    dead_anchors: list[str] = []
    replacements: list[tuple[str, str]] = []  # (old_anchor, new_anchor)

    for m in _INTRAPAGE_LINK_RE.finditer(text):
        anchor = m.group(1)

        # Skip citation anchors — they're handled elsewhere
        if anchor.startswith("cite_note") or anchor.startswith("cite_ref"):
            continue

        if anchor in heading_slug_set:
            continue  # already correct

        matched = None

        # Try replacing underscores with hyphens
        alt = anchor.replace("_", "-")
        if alt in heading_slug_set:
            matched = alt

        # Try removing trailing 'a' (MediaWiki artifact from old TOCs)
        if matched is None and anchor.endswith("a"):
            alt_a = anchor[:-1]
            if alt_a in heading_slug_set:
                matched = alt_a
            # Also try underscore→hyphen on the stripped version
            elif alt_a.replace("_", "-") in heading_slug_set:
                matched = alt_a.replace("_", "-")

        # Try fuzzy match with trailing-s (before and after underscore conversion)
        if matched is None:
            candidates_to_try = [anchor, anchor.replace("_", "-")]
            for candidate in candidates_to_try:
                for slug in heading_slugs:
                    if slug == candidate + "s" or candidate == slug + "s":
                        if matched is None:
                            matched = slug
                        else:
                            matched = None  # ambiguous
                            break
                if matched is not None:
                    break

        # Try prefix match
        if matched is None:
            prefix_matches = [s for s in heading_slugs if s.startswith(anchor) and len(s) > len(anchor)]
            if len(prefix_matches) == 1:
                matched = prefix_matches[0]

            # Also try prefix match on underscore-converted version
            if matched is None and alt != anchor:
                prefix_matches = [s for s in heading_slugs if s.startswith(alt) and len(s) > len(alt)]
                if len(prefix_matches) == 1:
                    matched = prefix_matches[0]

        if matched is not None:
            replacements.append((anchor, matched))
            fix_count += 1
        else:
            dead_anchors.append(anchor)

    # Apply replacements (reverse-sorted by position to keep indices stable,
    # but since we're doing string replacement, just do ordered substitution)
    new_text = text
    for old, new in replacements:
        # Only replace the anchor inside (#...) and avoid cite_ anchors
        new_text = re.sub(
            r"\(#" + re.escape(old) + r"\)",
            f"(#{new})",
            new_text,
        )

    return new_text, fix_count, dead_anchors


# ---------------------------------------------------------------------------
# CLI reporting helpers
# ---------------------------------------------------------------------------

def print_page_report(result: PageResult, dry_run: bool) -> None:
    rel = result.md_path.relative_to(REPO_ROOT)
    if result.skipped:
        print(f"  SKIP  {rel}")
        print(f"        reason: {result.skip_reason}")
        return

    action = "would write" if dry_run else "written"
    print(f"  OK    {rel}")
    print(f"        inline sups converted: {result.inline_count}")
    print(f"        defs appended: {result.defs_count}")
    if result.before_excerpt:
        print(f"        BEFORE excerpt: {result.before_excerpt!r}")
    if result.after_excerpt:
        print(f"        AFTER excerpt:  {result.after_excerpt!r}")
    if result.def_excerpts:
        for i, d in enumerate(result.def_excerpts[:2]):
            print(f"        def[{i}]: {d[:100]!r}")
    print(f"        [{action}]")


# ---------------------------------------------------------------------------
# Main citation conversion pipeline
# ---------------------------------------------------------------------------

def run_conversion(
    md_files: list[Path],
    dry_run: bool,
    verbose: bool = True,
) -> dict:
    """
    Process a list of md files. Returns summary dict.
    """
    results: list[PageResult] = []
    for md_path in md_files:
        r = process_page(md_path)
        results.append(r)
        if verbose:
            print_page_report(r, dry_run)

    skipped = [r for r in results if r.skipped]
    ok = [r for r in results if not r.skipped]

    if not dry_run:
        for r in ok:
            r.md_path.write_text(r.transformed_text, encoding="utf-8")

    total_inline = sum(r.inline_count for r in ok)
    total_defs = sum(r.defs_count for r in ok)

    action_word = "would write" if dry_run else "written"
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Pages processed:    {len(results)}")
    print(f"  Pages {action_word}:   {len(ok)}")
    print(f"  Pages skipped:      {len(skipped)}")
    print(f"  Inline citations:   {total_inline}")
    print(f"  Defs appended:      {total_defs}")

    if skipped:
        print()
        print("=== SKIPPED PAGES ===")
        for r in skipped:
            rel = r.md_path.relative_to(REPO_ROOT)
            print(f"  {rel}: {r.skip_reason}")
        print("=== END SKIPPED PAGES ===")

    return {
        "processed": len(results),
        "written": len(ok),
        "skipped": len(skipped),
        "total_inline": total_inline,
        "total_defs": total_defs,
        "skipped_pages": [(str(r.md_path.relative_to(REPO_ROOT)), r.skip_reason)
                          for r in skipped],
    }


# ---------------------------------------------------------------------------
# Non-citation anchor fix pipeline
# ---------------------------------------------------------------------------

def run_fix_anchors(
    md_files: list[Path],
    dry_run: bool,
    verbose: bool = True,
) -> dict:
    total_fixed = 0
    all_dead: list[tuple[str, str]] = []
    written = 0

    for md_path in md_files:
        text = md_path.read_text(encoding="utf-8")
        new_text, fix_count, dead = fix_anchors_in_file(text)
        total_fixed += fix_count
        for anchor in dead:
            all_dead.append((str(md_path.relative_to(REPO_ROOT)), anchor))

        if fix_count > 0:
            if verbose:
                print(f"  FIX   {md_path.relative_to(REPO_ROOT)}: {fix_count} anchor(s) fixed")
            if not dry_run:
                md_path.write_text(new_text, encoding="utf-8")
                written += 1
        elif verbose and dead:
            pass  # dead anchors are reported in summary

    action_word = "would write" if dry_run else "written"
    print()
    print("=" * 60)
    print("FIX-ANCHORS SUMMARY")
    print("=" * 60)
    print(f"  Files with fixes:   {written if not dry_run else total_fixed}")
    print(f"  Total anchors fixed: {total_fixed}")
    print(f"  Remaining dead anchors: {len(all_dead)}")
    if all_dead:
        print()
        print("  Dead anchors (file: anchor):")
        for fpath, anchor in all_dead:
            print(f"    {fpath}: #{anchor}")

    return {
        "fixed": total_fixed,
        "dead": all_dead,
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert MediaWiki citation anchors to GFM footnotes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    mode_group = parser.add_mutually_exclusive_group(required=False)
    mode_group.add_argument(
        "--prototype",
        action="store_true",
        help="Process only the 3 prototype files (dry-run unless --apply).",
    )
    mode_group.add_argument(
        "--all",
        action="store_true",
        help="Process all .md files under references/ (dry-run unless --apply).",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually write changed files (default is dry-run).",
    )
    parser.add_argument(
        "--fix-anchors",
        action="store_true",
        dest="fix_anchors",
        help="Fix non-citation intra-page anchors (independent of citation conversion).",
    )
    args = parser.parse_args()

    dry_run = not args.apply

    if args.fix_anchors:
        print("=== FIX-ANCHORS MODE ===")
        md_files = list(iter_md_files())
        run_fix_anchors(md_files, dry_run=dry_run)
        return

    if not args.prototype and not args.all:
        parser.print_help()
        sys.exit(1)

    if args.prototype:
        print("=== PROTOTYPE MODE (3 files) ===")
        if dry_run:
            print("(dry-run — pass --apply to write files)")
        md_files = PROTOTYPE_FILES
    else:
        print("=== FULL MODE (all references/**/*.md) ===")
        if dry_run:
            print("(dry-run — pass --apply to write files)")
        md_files = list(iter_md_files())

    run_conversion(md_files, dry_run=dry_run)


if __name__ == "__main__":
    main()
