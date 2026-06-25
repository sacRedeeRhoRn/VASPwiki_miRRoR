"""
convert.py — Convert fetched VASP wiki HTML to GitHub-Flavored Markdown.

Usage
-----
    python3 convert.py [--sample]

    --sample    Write outputs to references/_sample/<slug>.md instead of
                references/<slug>.md.  Useful for spot-checking a subset.

Conversion pipeline
-------------------
1. Primary: pandoc (subprocess) — `pandoc -f html -t gfm`
   HTML is fed on stdin; GFM markdown is captured from stdout.
   (raw_html passthrough is ENABLED so complex tables survive as raw <table> HTML
   rather than being dropped as `[TABLE]` placeholders; residual span/div chrome
   is stripped by strip_html_chrome() in post-processing.)

2. Fallback (pandoc missing): markdownify (guarded by ImportError).
   Only activated if `subprocess` call for pandoc fails with FileNotFoundError.

Post-processing (applied after conversion)
-------------------------------------------
- Rewrite internal wiki links to relative `./<slug>.md` paths.
- Strip MediaWiki chrome:
    * `[edit]` / `[Edit]` section-edit links.
    * `action=edit` and `redlink=1` links.
    * "Retrieved from …" footer line.
    * Category list footers (lines starting with "Categories:" or
      "Category:").
    * Navigation "Jump to:" lines.
- Prepend provenance header:
    <!-- Source: https://vasp.at/wiki/index.php/<Title> | revid: <revid> | retrieved: <date> -->
    <!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

    # <displaytitle or title>

Outputs
-------
  references/<slug>.md          (default)
  references/_sample/<slug>.md  (with --sample)
"""

import argparse
import html as _html_module
import json
import re
import subprocess
import sys
import urllib.parse
from datetime import date, datetime, timezone
from pathlib import Path

from wiki_common import (
    _META,
    _RAW,
    REFERENCES,
    safe_slug,
)

PAGE_BASE = "https://vasp.at/wiki/index.php"

# ---------------------------------------------------------------------------
# Conversion: pandoc (primary) + markdownify (fallback)
# ---------------------------------------------------------------------------

def _convert_pandoc(html: str) -> str:
    """
    Convert *html* to GFM via pandoc on stdin/stdout.

    Raises FileNotFoundError if pandoc is not on PATH.
    Raises subprocess.CalledProcessError on non-zero exit.
    """
    result = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm"],
        input=html,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        raise subprocess.CalledProcessError(
            result.returncode, "pandoc", result.stdout, result.stderr
        )
    return result.stdout


try:
    import markdownify as _markdownify_lib
    _MARKDOWNIFY_AVAILABLE = True
except ImportError:
    _MARKDOWNIFY_AVAILABLE = False


def _convert_markdownify(html: str) -> str:
    """Fallback converter using the markdownify library."""
    if not _MARKDOWNIFY_AVAILABLE:
        raise RuntimeError(
            "Neither pandoc nor markdownify is available. "
            "Install pandoc or `pip install markdownify`."
        )
    return _markdownify_lib.markdownify(html, heading_style="ATX")  # type: ignore[attr-defined]


def html_to_markdown(html: str) -> str:
    """
    Convert *html* to GFM markdown.

    Tries pandoc first; falls back to markdownify if pandoc is missing.
    """
    try:
        return _convert_pandoc(html)
    except FileNotFoundError:
        # pandoc not installed — use markdownify fallback.
        return _convert_markdownify(html)


# ---------------------------------------------------------------------------
# Link rewriting
# ---------------------------------------------------------------------------

# Patterns that identify an internal wiki link target.
# Group 1 captures the raw page title (URL-encoded, possibly with query params).
_WIKI_LINK_PATTERNS = [
    # /wiki/index.php/Page_Name  or  /wiki/index.php/Page_Name#Anchor
    re.compile(r"/wiki/index\.php/([^)\s\"'#?]+)"),
    # /wiki/Page_Name  (shorter canonical form)
    re.compile(r"/wiki/([^)\s\"'#?]+)"),
    # index.php?title=Page_Name (query-param form)
    re.compile(r"index\.php\?[^)\s\"']*\btitle=([^&)\s\"'#]+)"),
]

# Strip action=edit / redlink=1 links entirely (including surrounding brackets).
_EDIT_LINK_RE = re.compile(
    r"\[?\(?https?://[^\s)\"']*(?:action=edit|redlink=1)[^\s)\"']*\)?\]?"
)
# Convert MediaWiki <math>…</math> spans that pandoc renders as
#   \[math\]\displaystyle{ … }\[/math\]   or   \[math\]…\[/math\]
# (also handles unescaped [math]…[/math] variants).
# Strategy: match the opening tag, an optional \displaystyle{…} group, and the
# closing tag.  We use a non-greedy .*? with DOTALL so we don't span multiple
# independent math expressions in one go.
_MATH_RE = re.compile(
    r"\\?\[math\\?\]\s*(?:\\?displaystyle\s*\{(.*?)\}\s*)?\\?\[/math\\?\]",
    re.DOTALL,
)

def _math_to_latex(m: re.Match) -> str:
    """Replace a [math]…[/math] span with $…$."""
    inner = m.group(1)
    if inner is not None:
        # Had \displaystyle{…} — use the captured content directly.
        return f"${inner.strip()}$"
    # No \displaystyle group — extract raw content between tags by slicing the
    # full match and stripping the outer [math]…[/math] wrappers.
    full = m.group(0)
    # Remove leading \[math\] / [math] and trailing \[/math\] / [/math].
    inner_raw = re.sub(r"^\\?\[math\\?\]\s*", "", full)
    inner_raw = re.sub(r"\s*\\?\[/math\\?\]$", "", inner_raw)
    return f"${inner_raw.strip()}$"


# ---------------------------------------------------------------------------
# Math un-escaping (pandoc over-escapes inside $…$ / $$…$$ spans)
# ---------------------------------------------------------------------------
# pandoc emits over-escaped sequences such as $E\_{\mathrm{cut}}$ (backslash-
# underscore) and \| inside math.  Within math spans only, unescape these so
# the LaTeX renders.  We DO NOT touch escapes outside math.
_INLINE_MATH_SPAN_RE = re.compile(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", re.DOTALL)
_BLOCK_MATH_SPAN_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)

# Map of over-escaped sequence -> intended character (inside math only).
_MATH_UNESCAPE = (
    (r"\_", "_"),
    (r"\|", "|"),
    (r"\{", "{"),
    (r"\}", "}"),
    (r"\<", "<"),
    (r"\>", ">"),
)


def _unescape_math_inner(inner: str) -> str:
    """Unescape pandoc's over-escaping within a single math span body."""
    for esc, ch in _MATH_UNESCAPE:
        inner = inner.replace(esc, ch)
    return inner


def unescape_math(md: str) -> str:
    """
    Within inline `$…$` and block `$$…$$` spans only, undo pandoc's
    over-escaping (`\\_`→`_`, `\\|`→`|`, `\\{`→`{`, `\\}`→`}`, `\\<`→`<`,
    `\\>`→`>`).  Escapes outside math are left untouched.

    Block spans are processed first so the inline regex does not bisect them.
    """
    def _block_sub(m: re.Match) -> str:
        return "$$" + _unescape_math_inner(m.group(1)) + "$$"

    def _inline_sub(m: re.Match) -> str:
        return "$" + _unescape_math_inner(m.group(1)) + "$"

    md = _BLOCK_MATH_SPAN_RE.sub(_block_sub, md)
    md = _INLINE_MATH_SPAN_RE.sub(_inline_sub, md)
    return md


# ---------------------------------------------------------------------------
# Image src rewriting (point site-relative wiki image paths to absolute URLs)
# ---------------------------------------------------------------------------
WIKI_SITE_BASE = "https://vasp.at"

# Image / asset rewriting.  pandoc renders a thumbnailed wiki image as
#   [![](/wiki/images/thumb/.../Foo.png)](/wiki/File:Foo.png)
# i.e. a markdown image whose src is `/wiki/images/...`, wrapped in a link whose
# target is `/wiki/File:...`.  Both are site-relative; rewrite both to absolute
# https://vasp.at/... URLs so they resolve online.  We do this BEFORE generic
# wiki-link rewriting so the link rewriter does not mangle these asset paths.
#
# Markdown image:  ![alt](/wiki/images/...)
_IMG_MD_RE = re.compile(r'(!\[[^\]]*\]\()(/wiki/[^)\s]+)(\))')
# Raw HTML <img src="/wiki/...">
_IMG_HTML_SRC_RE = re.compile(r'(<img\b[^>]*?\bsrc=")(/wiki/[^"]+)(")', re.IGNORECASE)
# Link target pointing at a File: description page: [text](/wiki/File:Foo.png)
# Also matches titles: [text](/wiki/File:Foo.png "title")
_FILE_LINK_RE = re.compile(r'(\]\()(/wiki/File:[^\s)]+)([^)]*?)(\))')


def rewrite_image_srcs(md: str) -> str:
    """
    Rewrite site-relative wiki image sources and File: link targets to
    ABSOLUTE `https://vasp.at/wiki/...` URLs so they resolve online.  Image
    binaries are not downloaded.  Run this BEFORE rewrite_wiki_links() so the
    generic link rewriter does not turn these asset paths into broken
    `./images__....md` links.
    """
    abs_sub = lambda m: m.group(1) + WIKI_SITE_BASE + m.group(2) + m.group(3)
    md = _IMG_MD_RE.sub(abs_sub, md)
    md = _IMG_HTML_SRC_RE.sub(abs_sub, md)
    # File: links now have 4 groups due to optional title
    file_link_sub = lambda m: m.group(1) + WIKI_SITE_BASE + m.group(2) + m.group(3) + m.group(4)
    md = _FILE_LINK_RE.sub(file_link_sub, md)
    return md


# Strip bare `[edit]` section markers that pandoc leaves as text or links.
# Also removes:
#   [edit source]  /  [edit | edit source]
#   bracketed link clusters on heading lines that contain index.php and "edit"
#   e.g. [(./index.php.md) | [edit source](./index.php.md)]
_SECTION_EDIT_RE = re.compile(
    r"\[edit(?:\s*\|\s*edit\s+source)?\]"
    r"|\[edit\s+source\]",
    re.IGNORECASE,
)
# Remove trailing bracketed edit-link clusters appended to ATX headings after
# link rewriting.  After rewrite, pandoc's section-edit markup ends up as one
# of these forms at the end of a heading line:
#
#   \[(./index.php.md) \| (./index.php.md)\]
#   \[(./index.php.md)") \| (./index.php.md)")\]   (POSCAR variant with stray ")
#
# We match: optional whitespace then a backslash-escaped opening bracket \[,
# any content that references index.php, then a backslash-escaped closing \].
# One or more such clusters are stripped from the end of the heading line.
_HEADING_EDIT_LINK_RE = re.compile(
    r"^(#{1,6} .*?)"                    # capture heading text (non-greedy)
    r"(?:\s*\\\[(?:[^\\[\]]*index\.php[^\]]*)\\\])+\s*$",
    re.MULTILINE,
)
# MediaWiki "Retrieved from" footer line.
_RETRIEVED_FROM_RE = re.compile(
    r"^Retrieved from [^\n]*$",
    re.MULTILINE,
)
# Category/Categories footer line.
_CATEGORY_FOOTER_RE = re.compile(
    r"^Categor(?:y|ies):?[^\n]*$",
    re.MULTILINE,
)
# "Jump to:" navigation line.
_JUMP_NAV_RE = re.compile(
    r"^Jump to:[^\n]*$",
    re.MULTILINE,
)


def _decode_title(raw: str) -> str:
    """URL-decode a raw wiki page name captured from a URL."""
    return urllib.parse.unquote(raw.replace("_", " "))


def rewrite_wiki_links(md: str, slugmap: dict[str, str]) -> str:
    """
    Replace internal wiki link targets with relative `./<slug>.md` paths.

    *slugmap* is title→slug.  For pages not present in the map, we compute
    safe_slug() directly (best-effort; keeps links relative).
    """
    def replace_target(match_obj: re.Match, group: int = 1) -> str:
        raw_page = match_obj.group(group)
        title = _decode_title(raw_page)
        slug = slugmap.get(title) or safe_slug(title)
        return f"./{slug}.md"

    # We rewrite inside markdown link syntax: [text](URL) and bare URLs.
    # Strategy: find markdown links first, rewrite href; then handle bare URLs.

    def _rewrite_md_link(m: re.Match) -> str:
        text = m.group(1)
        href = m.group(2)
        new_href = _maybe_rewrite_href(href)
        return f"[{text}]({new_href})"

    def _maybe_rewrite_href(href: str) -> str:
        """Try each pattern; return rewritten path or original href."""
        # Already-absolute URLs: leave untouched.
        if href.startswith("http://") or href.startswith("https://"):
            return href
        # Asset/image/File: paths — absolutize to https://vasp.at so they
        # resolve online (binaries are not downloaded).  Image *src* embeds are
        # already absolutized by rewrite_image_srcs(); this also catches plain
        # download links like [tutorial](/wiki/images/.../foo.pdf).
        if href.startswith("/wiki/images/") or href.startswith("/wiki/File:"):
            return WIKI_SITE_BASE + href
        if "/wiki/images/" in href or "/wiki/File:" in href:
            return href
        for pat in _WIKI_LINK_PATTERNS:
            mo = pat.search(href)
            if mo:
                title = _decode_title(mo.group(1))
                slug = slugmap.get(title) or safe_slug(title)
                return f"./{slug}.md"
        return href

    # Rewrite [text](href) markdown links.
    md = re.sub(r"\[([^\]]*)\]\(([^)]+)\)", _rewrite_md_link, md)

    return md


def strip_chrome(md: str) -> str:
    """Remove MediaWiki navigation/footer chrome from converted markdown."""
    # Convert [math]…[/math] spans to $…$ before any other stripping.
    md = _MATH_RE.sub(_math_to_latex, md)
    # Un-escape pandoc's over-escaping inside math spans.
    md = unescape_math(md)
    md = _EDIT_LINK_RE.sub("", md)
    md = _SECTION_EDIT_RE.sub("", md)
    # Strip trailing bracketed edit-link clusters from ATX headings.
    md = _HEADING_EDIT_LINK_RE.sub(r"\1", md)
    md = _RETRIEVED_FROM_RE.sub("", md)
    md = _CATEGORY_FOOTER_RE.sub("", md)
    md = _JUMP_NAV_RE.sub("", md)
    # Collapse runs of 3+ blank lines down to 2 (cosmetic cleanup).
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    return md


# ---------------------------------------------------------------------------
# HTML chrome stripping (span/div removal outside table blocks)
# ---------------------------------------------------------------------------

# Matches a complete <table>…</table> block, possibly multi-line.
_TABLE_BLOCK_RE = re.compile(r"<table\b.*?</table>", re.DOTALL | re.IGNORECASE)

# Tag patterns for span and div (opening and closing, incl. self-closing variants).
_SPAN_TAG_RE = re.compile(r"</?span\b[^>]*>", re.IGNORECASE)
_DIV_TAG_RE  = re.compile(r"</?div\b[^>]*>",  re.IGNORECASE)


def strip_html_chrome(md: str) -> str:
    """
    Remove residual HTML chrome (<span> and <div> wrapper tags) introduced by
    pandoc's raw_html passthrough, while leaving <table>…</table> blocks fully
    intact (including any spans/divs that happen to be *inside* table cells).

    Strategy:
    - Split the document into alternating [non-table, table, non-table, …] segments.
    - In non-table segments: strip <span …>, </span>, <div …>, </div> tags (keep
      inner text).
    - Table segments: pass through untouched.
    - Reassemble in original order.
    - Collapse any runs of 3+ blank lines to 2 (cosmetic, mirrors strip_chrome).
    """
    # Split around table blocks.  re.split with a capturing group gives:
    #   [before_table1, table1, between, table2, …, after_last_table]
    parts = _TABLE_BLOCK_RE.split(md)
    table_blocks = _TABLE_BLOCK_RE.findall(md)

    # parts has len(table_blocks)+1 non-table segments interleaved with table_blocks.
    result_parts: list[str] = []
    for i, segment in enumerate(parts):
        # Strip span/div tags from non-table prose.
        segment = _SPAN_TAG_RE.sub("", segment)
        segment = _DIV_TAG_RE.sub("", segment)
        result_parts.append(segment)
        # Re-insert the matching table block (if any) after this segment.
        if i < len(table_blocks):
            result_parts.append(table_blocks[i])

    reassembled = "".join(result_parts)
    # Cosmetic: collapse runs of 3+ blank lines to 2.
    reassembled = re.sub(r"\n{4,}", "\n\n\n", reassembled)
    return reassembled


# ---------------------------------------------------------------------------
# Provenance header
# ---------------------------------------------------------------------------

def build_header(
    title: str,
    displaytitle: str,
    revid: int | None,
    fetched_at: str | None,
) -> str:
    """
    Build the standard provenance comment block + H1 heading.

    *fetched_at* is an ISO 8601 UTC string; we extract only the date part.
    """
    url_title = urllib.parse.quote(title.replace(" ", "_"), safe=":/")
    source_url = f"{PAGE_BASE}/{url_title}"

    if fetched_at:
        try:
            retrieved = fetched_at[:10]   # YYYY-MM-DD
        except Exception:
            retrieved = str(date.today())
    else:
        retrieved = str(date.today())

    revid_str = str(revid) if revid else "unknown"
    # Use displaytitle for the H1; fall back to plain title.
    # Strip any HTML tags (e.g. <span class="mw-page-title-main">ENCUT</span>)
    # then unescape HTML entities so the heading is plain text.
    raw_h1 = displaytitle if displaytitle else title
    h1_title = _html_module.unescape(re.sub(r"<[^>]+>", "", raw_h1)).strip()

    header_lines = [
        f"<!-- Source: {source_url} | revid: {revid_str} | retrieved: {retrieved} -->",
        "<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->",
        "",
        f"# {h1_title}",
        "",
    ]
    return "\n".join(header_lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert fetched VASP wiki HTML to GitHub-Flavored Markdown."
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Write outputs to references/_sample/ instead of references/.",
    )
    args = parser.parse_args()

    # Determine output directory.
    # Full runs write flat to references/_pages/ (a staging dir); organize.py
    # then moves each page into its bucket folder under references/.
    if args.sample:
        out_dir = REFERENCES / "_sample"
    else:
        out_dir = REFERENCES / "_pages"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load metadata.
    slugmap_path = _META / "slugmap.json"
    pages_path   = _META / "pages.json"

    if not slugmap_path.exists():
        print(f"ERROR: {slugmap_path} not found. Run fetch_pages.py first.")
        sys.exit(1)
    if not pages_path.exists():
        print(f"ERROR: {pages_path} not found. Run crawl_index.py first.")
        sys.exit(1)

    slugmap: dict[str, str] = json.loads(
        slugmap_path.read_text(encoding="utf-8")
    )
    pages_list: list[dict] = json.loads(
        pages_path.read_text(encoding="utf-8")
    )

    # Build a slug→page-meta lookup for efficient access.
    # Keyed by slug (not title) so we can look up from the HTML filename.
    slug_to_meta: dict[str, dict] = {}
    for page in pages_list:
        slug = slugmap.get(page["title"])
        if slug:
            slug_to_meta[slug] = page

    html_dir = _RAW / "html"
    if not html_dir.exists():
        print(f"ERROR: {html_dir} not found. Run fetch_pages.py first.")
        sys.exit(1)

    html_files = sorted(html_dir.glob("*.html"))
    print(f"Found {len(html_files)} HTML files in {html_dir}")

    converted = 0
    skipped   = 0

    for html_path in html_files:
        slug = html_path.stem   # filename without .html

        # Only convert if we have a slugmap / pages.json entry.
        meta = slug_to_meta.get(slug)
        if meta is None:
            print(f"  WARN: no metadata for {slug!r} — skipping (orphan).")
            skipped += 1
            continue

        title        = meta.get("title", slug)
        displaytitle = meta.get("displaytitle", title)
        revid        = meta.get("revid")
        fetched_at   = meta.get("fetched_at")

        # Read HTML.
        html = html_path.read_text(encoding="utf-8")

        # Convert to markdown.
        try:
            md = html_to_markdown(html)
        except Exception as exc:
            print(f"  ERROR converting {slug}: {exc}")
            skipped += 1
            continue

        # Post-process.  Image/File asset paths first (absolute URLs) so the
        # generic wiki-link rewriter below does not mangle them.
        md = rewrite_image_srcs(md)
        md = rewrite_wiki_links(md, slugmap)
        md = strip_chrome(md)
        md = strip_html_chrome(md)

        # Prepend provenance header.
        header = build_header(title, displaytitle, revid, fetched_at)
        md = header + md

        # Write output.
        out_path = out_dir / f"{slug}.md"
        out_path.write_text(md, encoding="utf-8")
        converted += 1

    print(f"\nDone. converted={converted}, skipped={skipped}")
    print(f"Output directory: {out_dir}")


if __name__ == "__main__":
    main()
