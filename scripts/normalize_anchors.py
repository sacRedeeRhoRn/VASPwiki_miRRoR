"""
normalize_anchors.py
====================
Normalize intra-document markdown anchor links to GitHub heading slugs.

GitHub heading-anchor slug algorithm:
  1. Extract rendered visible text from the heading (strip markdown links, backticks, etc.)
  2. Lowercase
  3. Remove characters that are NOT [\\w\\s-]  (keeps letters, digits, underscores, spaces, hyphens)
  4. Replace each space with a single hyphen
  5. Duplicate headings (same slug) get suffixes -1, -2, ... in order of appearance

Fragment matching strategy:
  - Fragments in these wiki files are MediaWiki-style (spaces -> underscores, punctuation kept).
  - To match a fragment to a heading slug:
      a. First try: lowercase(fragment) == heading_slug
      b. Second try: slug_normalize(fragment) == heading_slug  (apply full slug algo)
      c. Third try: slug_normalize(fragment).replace('_', '-') == heading_slug
         This handles MediaWiki underscore-for-space convention.
  - Only rewrite if exactly ONE heading slug matches (unique match).

Usage:
  python3 normalize_anchors.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REFERENCES_DIR = Path("/Users/sacRedeeRhoRn/Sanctum/area2_develop/vasp-wiki/references")

# ATX heading: one or more # at start of line, at least one space, then text
_ATX_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")

# Fenced code block delimiter
_FENCE_RE = re.compile(r"^(`{3,}|~{3,})")

# Markdown link: [text](url)  — capture only the display text
_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")

# Inline code: `code`
_INLINE_CODE_RE = re.compile(r"`([^`]*)`")

# Bold/italic emphasis markers (as standalone delimiters, not mid-word)
# We strip **, __, *, _ only when they appear as pairs of markers.
# Simplest approach: strip them as punctuation (they'll be removed by the \w\s- rule anyway).
# But keep this explicit for clarity.
_BOLD_ITALIC_RE = re.compile(r"(\*\*|__|\*|_)")

# Wiki edit-section artifact: \[<a ... at end of heading lines (from mediawiki2markdown)
# These appear as literal backslash followed by [<a
_WIKI_EDITSECT_RE = re.compile(r"\\\[<a.*$", re.DOTALL)

# Intra-document fragment-only anchor link: ](#FRAGMENT)
# Only matches when # immediately follows ( — path+fragment links are excluded naturally.
_FRAG_LINK_RE = re.compile(r"\]\(#([^)]+)\)")

# Characters to remove for slug (keep \w = [a-zA-Z0-9_], \s, -)
_SLUG_STRIP_RE = re.compile(r"[^\w\s-]")

# Collapse runs of whitespace into a single space
_SPACE_COLLAPSE_RE = re.compile(r"\s+")


# ---------------------------------------------------------------------------
# Slug computation
# ---------------------------------------------------------------------------

def _extract_heading_text(raw_heading_text: str) -> str:
    """
    Extract the rendered visible text of a heading line for slug computation.

    Handles:
    - Wiki edit-section artifacts: \\[<a ...] (trailing, multi-line content
      starts on the same line — we strip from \\[<a onward)
    - Markdown links [text](url) -> text
    - Inline code `code` -> code
    - Bold/italic markers ** / __ / * / _
    """
    text = raw_heading_text

    # Strip trailing wiki edit-section artifact
    text = _WIKI_EDITSECT_RE.sub("", text)

    # Replace [text](url) with text
    text = _MD_LINK_RE.sub(r"\1", text)

    # Replace `code` with code
    text = _INLINE_CODE_RE.sub(r"\1", text)

    # Strip bold/italic markers (they'll be cleaned by slug rules but strip explicitly)
    text = _BOLD_ITALIC_RE.sub("", text)

    return text.strip()


def _slug_from_text(text: str) -> str:
    """
    Compute a GitHub heading slug from rendered heading text.

    Steps:
    1. Lowercase
    2. Remove [^\\w\\s-]
    3. Replace whitespace runs with single hyphen
    """
    slug = text.lower()
    slug = _SLUG_STRIP_RE.sub("", slug)
    slug = _SPACE_COLLAPSE_RE.sub("-", slug)
    # Strip leading/trailing hyphens that may appear after collapsing
    slug = slug.strip("-")
    return slug


def _slug_from_fragment(fragment: str) -> str:
    """
    Apply slug normalization to a raw fragment string.

    This is the same algorithm as _slug_from_text but underscores within the
    fragment are kept by the \\w rule (consistent with GitHub slug algorithm).
    """
    return _slug_from_text(fragment)


def _fragment_candidates(fragment: str) -> list[str]:
    """
    Return a list of candidate slugs to try when matching a fragment to headings.

    Order:
    1. fragment lowercased as-is (already a correct slug)
    2. slug_normalize(fragment)  (applies full slug algo)
    3. slug_normalize(fragment) with underscores replaced by hyphens
       (handles MediaWiki underscore-for-space convention)
    4. fragment lowercased with underscores replaced by hyphens directly
    5. MediaWiki _N suffix translation: base_N (N>=2) -> base-(N-1) in GitHub slugs
       (MediaWiki 2nd occurrence = _2, GitHub 2nd occurrence = -1)
    """
    lowered = fragment.lower()
    slugified = _slug_from_fragment(fragment)
    slugified_dehyph = slugified.replace("_", "-")
    lowered_dehyph = lowered.replace("_", "-")

    # MediaWiki duplicate-heading suffix translation.
    # MediaWiki uses base_N for the Nth occurrence (N >= 2).
    # GitHub uses base-M for the (M+1)th occurrence (M >= 1, so _2 -> -1, _3 -> -2, ...).
    mw_suffix_match = re.match(r"^(.+)_(\d+)$", fragment)
    mw_candidates: list[str] = []
    if mw_suffix_match:
        base_frag = mw_suffix_match.group(1)
        n = int(mw_suffix_match.group(2))
        if n >= 2:
            github_n = n - 1
            base_slug = _slug_from_text(base_frag).replace("_", "-")
            mw_candidates.append(f"{base_slug}-{github_n}")

    # Return in priority order, deduplicated
    seen: set[str] = set()
    candidates: list[str] = []
    for c in [lowered, slugified, slugified_dehyph, lowered_dehyph] + mw_candidates:
        if c not in seen:
            seen.add(c)
            candidates.append(c)
    return candidates


# ---------------------------------------------------------------------------
# Per-file heading slug map
# ---------------------------------------------------------------------------

def build_slug_map(lines: list[str]) -> dict[str, str]:
    """
    Parse heading lines (respecting fenced code blocks) and build a map:
        canonical_slug -> canonical_slug   (identity, for lookup)

    Also builds duplicate suffix tracking: if two headings produce the same
    base slug, the second gets -1, third gets -2, etc. (GitHub convention).

    Returns:
        A set of all canonical slugs (as a dict mapping slug -> slug for O(1) lookup).
    """
    slugs: list[str] = []  # ordered list of canonical slugs
    slug_count: dict[str, int] = {}  # base_slug -> number of times seen

    in_fence = False
    fence_marker: str | None = None

    for line in lines:
        # Track fenced code blocks
        fence_match = _FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)[0]  # ` or ~
            marker_len = len(fence_match.group(1))
            if not in_fence:
                in_fence = True
                fence_marker = fence_match.group(1)
            elif fence_marker is not None and line.startswith(marker * marker_len):
                in_fence = False
                fence_marker = None
            continue

        if in_fence:
            continue

        heading_match = _ATX_HEADING_RE.match(line)
        if heading_match:
            raw_text = heading_match.group(2)
            visible_text = _extract_heading_text(raw_text)
            base_slug = _slug_from_text(visible_text)

            if not base_slug:
                continue

            count = slug_count.get(base_slug, 0)
            slug_count[base_slug] = count + 1

            if count == 0:
                canonical = base_slug
            else:
                canonical = f"{base_slug}-{count}"

            slugs.append(canonical)

    return {s: s for s in slugs}


def find_matching_slug(fragment: str, slug_set: dict[str, str]) -> str | None:
    """
    Find the canonical heading slug that this fragment refers to.

    Returns the canonical slug string, or None if no unique match found.
    """
    candidates = _fragment_candidates(fragment)
    for candidate in candidates:
        if candidate in slug_set:
            return candidate
    return None


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------

def process_file(
    path: Path,
    dry_run: bool,
    unresolved: list[tuple[str, str]],
    examples: list[tuple[str, str, str]],
) -> tuple[int, int, int]:
    """
    Process a single markdown file.

    Returns:
        (anchors_found, rewritten, unresolved_count)
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    slug_set = build_slug_map(lines)

    anchors_found = 0
    rewritten_count = 0
    unresolved_count = 0

    def replace_fragment(m: re.Match) -> str:
        nonlocal anchors_found, rewritten_count, unresolved_count

        anchors_found += 1
        fragment = m.group(1)
        canonical = find_matching_slug(fragment, slug_set)

        if canonical is None:
            unresolved_count += 1
            if len(unresolved) < 50:  # cap collection
                unresolved.append((str(path.relative_to(REFERENCES_DIR)), fragment))
            return m.group(0)  # leave unchanged

        if fragment == canonical:
            return m.group(0)  # already correct

        rewritten_count += 1
        if len(examples) < 20:
            examples.append((str(path.relative_to(REFERENCES_DIR)), fragment, canonical))

        return f"](#{canonical})"

    new_text = _FRAG_LINK_RE.sub(replace_fragment, text)

    if new_text != text and not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return anchors_found, rewritten_count, unresolved_count


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Normalize intra-document anchor links to GitHub heading slugs."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report counts without writing any files.",
    )
    args = parser.parse_args()

    md_files = sorted(REFERENCES_DIR.rglob("*.md"))

    total_files = len(md_files)
    total_anchors = 0
    total_rewritten = 0
    total_unresolved = 0
    unresolved_examples: list[tuple[str, str]] = []
    rewrite_examples: list[tuple[str, str, str]] = []
    changed_files = 0

    for md_path in md_files:
        found, rewritten, unres = process_file(
            md_path,
            dry_run=args.dry_run,
            unresolved=unresolved_examples,
            examples=rewrite_examples,
        )
        total_anchors += found
        total_rewritten += rewritten
        total_unresolved += unres
        if rewritten > 0:
            changed_files += 1

    mode = "[DRY RUN] " if args.dry_run else ""
    print(f"\n{mode}=== normalize_anchors summary ===")
    print(f"  Files scanned            : {total_files}")
    print(f"  Files {'would be ' if args.dry_run else ''}changed  : {changed_files}")
    print(f"  Total (#...) anchors     : {total_anchors}")
    print(f"  Rewritten                : {total_rewritten}")
    print(f"  Unresolved (no heading)  : {total_unresolved}")

    if unresolved_examples:
        print(f"\n  Up to 15 unresolved examples:")
        for file_rel, frag in unresolved_examples[:15]:
            print(f"    {file_rel} :: #{frag}")

    if rewrite_examples:
        print(f"\n  Up to 10 before->after examples:")
        for file_rel, old_frag, new_frag in rewrite_examples[:10]:
            print(f"    {file_rel}")
            print(f"      #{old_frag}  ->  #{new_frag}")

    print()


if __name__ == "__main__":
    main()
