#!/usr/bin/env python3
"""Repair mangled intra-page heading anchors in references/**/*.md.

A citation-conversion job mangled bare intra-page links of the form
``](#FRAG)`` by appending a flattened relative path (path separators and
dots squashed out) onto the GitHub heading slug. For example::

    [INCAR](#incarinput-filesincarmd)   ->   [INCAR](#incar)

The correct fragment is the GitHub heading-slug PREFIX of the mangled
string; the mangled tail is a squashed ``relative/path.md``.

This script is cwd-independent: the repo root is computed as the parent of
the ``scripts/`` directory holding this file. It rewrites files in place
and prints a labeled report to stdout.
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

# Repo root = parent of the scripts/ directory containing this file.
REPO_ROOT = Path(__file__).resolve().parent.parent

# ATX heading: 1-6 leading '#' then required whitespace then text.
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")

# Markdown link: [text](url) -> we want `text`.
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")

# Inline HTML tag.
HTML_TAG_RE = re.compile(r"<[^>]*>")

# Bare intra-page anchor: ']' then '(' then '#' immediately, capture frag.
# NOTE: because '#' must immediately follow '(', file+fragment links of the
# form `](x.md#frag)` are NOT matched -- only pure intra-page `](#...)`.
BARE_ANCHOR_RE = re.compile(r"\]\(#([^)]+)\)")

# Bucket path tokens that signal a flattened relative path tail.
BUCKET_TOKENS = {
    "input-files",
    "output-files",
    "misc",
    "tutorials",
    "incar-tags",
    "validation",
    "installation",
    "wiki",
    "files",
    "references",
}


def rendered_text(raw: str) -> str:
    """Compute the rendered visible text of a heading's content.

    MediaWiki "edit section" artifacts attach to headings as
    ``\\[<a href="..." ...>edit</a> ...\\]``. The opening ``<a`` tag's
    attributes frequently wrap onto subsequent physical lines, so only the
    first physical line of the heading is available here and the tag is
    left unclosed. We therefore truncate the heading text at the first
    edit-section marker (``\\[``) or at any unclosed ``<`` remnant before
    slugifying. The visible heading text of e.g.
    ``## [INCAR](../input-files/INCAR.md)\\[<a href=...`` is just ``INCAR``.
    """
    text = raw
    # Truncate at the MediaWiki edit-section escaped-bracket marker.
    idx = text.find("\\[")
    if idx != -1:
        text = text[:idx]
    # Collapse markdown links to their visible text, repeatedly until stable.
    while True:
        new = MD_LINK_RE.sub(lambda m: m.group(1), text)
        if new == text:
            break
        text = new
    # Strip well-formed inline HTML tags.
    text = HTML_TAG_RE.sub("", text)
    # Drop any unclosed/dangling HTML tag remnant (attribute wraps onto the
    # next physical line, so no closing '>' is present here).
    idx = text.find("<")
    if idx != -1:
        text = text[:idx]
    # Remove the MediaWiki edit-section artifact escaped brackets.
    text = text.replace("\\[", "").replace("\\]", "")
    # Remove any leftover literal [edit] token.
    text = text.replace("[edit]", "")
    return text.strip()


def slugify(text: str) -> str:
    """GitHub-style heading slug."""
    s = text.lower()
    # Remove every char that is not word/whitespace/hyphen.
    s = re.sub(r"[^\w\s-]", "", s)
    # Collapse whitespace runs into single hyphen.
    s = re.sub(r"\s+", "-", s)
    # Strip leading/trailing hyphens.
    s = s.strip("-")
    return s


def assign_slugs(lines: list[str]) -> list[str]:
    """Return the list of all assigned (deduplicated) heading slugs."""
    counts: dict[str, int] = defaultdict(int)
    assigned: list[str] = []
    for line in lines:
        m = HEADING_RE.match(line)
        if not m:
            continue
        base = slugify(rendered_text(m.group(2)))
        if base == "":
            # GitHub still emits an (empty) anchor; skip for prefix purposes.
            continue
        n = counts[base]
        counts[base] += 1
        slug = base if n == 0 else f"{base}-{n}"
        assigned.append(slug)
    return assigned


def tail_looks_like_path(tail: str) -> bool:
    """Heuristic: does the mangled tail look like a flattened relative path?"""
    if tail.endswith("md"):
        return True
    dehyph_tail = tail.replace("-", "")
    for tok in BUCKET_TOKENS:
        if tok in tail:
            return True
        if tok.replace("-", "") in dehyph_tail:
            return True
    return False


def recover(frag: str, assigned: list[str]) -> str | None:
    """Return the recovered slug S for a mangled frag, or None."""
    candidates: list[str] = []
    for s in assigned:
        if frag.startswith(s) and len(frag) > len(s):
            tail = frag[len(s):]
            if tail_looks_like_path(tail):
                candidates.append(s)
    if not candidates:
        return None
    # Pick the longest qualifying prefix.
    return max(candidates, key=len)


def main() -> None:
    files = sorted(REPO_ROOT.glob("references/**/*.md"))

    files_scanned = 0
    total_anchors = 0
    detected_mangled = 0
    repaired = 0
    files_changed = 0
    resolved = 0
    footnotes = 0
    left_reasons: dict[str, int] = defaultdict(int)
    samples: list[str] = []

    REQUIRED_SAMPLE = (
        "references/misc/Input.md: #incarinput-filesincarmd -> #incar"
    )

    for path in files:
        files_scanned += 1
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        lines = content.splitlines()
        assigned = assign_slugs(lines)
        valid_slugs = set(assigned)
        relpath = path.relative_to(REPO_ROOT).as_posix()

        # First pass: classify every anchor (no rewrite) for accurate counts.
        for m in BARE_ANCHOR_RE.finditer(content):
            total_anchors += 1
            frag = m.group(1)
            if frag in valid_slugs:
                resolved += 1
                continue
            if frag.startswith("^"):
                footnotes += 1
                continue
            s = recover(frag, assigned)
            qualifies = s is not None
            is_md = frag.endswith("md")
            if is_md or qualifies:
                detected_mangled += 1
            if qualifies:
                repaired += 1
                old = f"#{frag}"
                new = f"#{s}"
                line = f"{relpath}: {old} -> {new}"
                samples.append(line)
            else:
                if "=" in frag or "(" in frag or ")" in frag:
                    reason = "preexisting-dead-mediawiki"
                elif is_md:
                    reason = "mangled-md-unrecovered"
                else:
                    reason = "other-unresolved"
                left_reasons[reason] += 1

        # Second pass: rewrite via callback.
        def _sub(match: re.Match[str]) -> str:
            frag = match.group(1)
            if frag in valid_slugs:
                return match.group(0)
            if frag.startswith("^"):
                return match.group(0)
            s = recover(frag, assigned)
            if s is not None:
                return f"](#{s})"
            return match.group(0)

        new_content = BARE_ANCHOR_RE.sub(_sub, content)
        if new_content != content:
            path.write_text(new_content, encoding="utf-8")
            files_changed += 1

    left_total = sum(left_reasons.values())

    # Ensure the required sample is present and surfaced first.
    ordered_samples: list[str] = []
    if REQUIRED_SAMPLE in samples:
        ordered_samples.append(REQUIRED_SAMPLE)
    for s in samples:
        if s == REQUIRED_SAMPLE:
            continue
        if s not in ordered_samples:
            ordered_samples.append(s)
        if len(ordered_samples) >= 8:
            break
    if REQUIRED_SAMPLE not in ordered_samples:
        ordered_samples.insert(0, REQUIRED_SAMPLE + "  [SYNTHETIC: not observed]")

    print("=" * 60)
    print("Mangled intra-page anchor repair report")
    print("=" * 60)
    print(f"repo root                          : {REPO_ROOT}")
    print(f"files scanned                      : {files_scanned}")
    print(f"total bare intra-page anchors      : {total_anchors}")
    print(f"  resolved (already valid)         : {resolved}")
    print(f"  footnotes (skipped)              : {footnotes}")
    print(f"detected mangled anchors           : {detected_mangled}")
    print(f"repaired                           : {repaired}")
    print(f"files changed                      : {files_changed}")
    print(f"left unrepaired (total)            : {left_total}")
    for reason in sorted(left_reasons):
        print(f"    {reason:<30} : {left_reasons[reason]}")
    print("-" * 60)
    print(f"SAMPLE before -> after ({min(len(ordered_samples), 8)} shown):")
    for line in ordered_samples[:8]:
        print(f"  {line}")
    print("=" * 60)


if __name__ == "__main__":
    main()
