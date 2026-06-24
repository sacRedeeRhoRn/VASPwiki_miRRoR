#!/usr/bin/env python3
"""Build a searchable index for the offline VASP wiki bundle.

Scans references/**/*.md, extracts per-page metadata (title, summary,
aliases from redirects, related links, keywords), and writes
_meta/index.json and INDEX.md at the bundle root.

Location-independent: bundle root is derived from this file's location
(parent of scripts/). No absolute paths are written into the outputs.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths (location-independent)
# ---------------------------------------------------------------------------
BUNDLE_ROOT = Path(__file__).resolve().parent.parent
REFERENCES = BUNDLE_ROOT / "references"
META = BUNDLE_ROOT / "_meta"
PAGES_JSON = META / "pages.json"
INDEX_JSON = META / "index.json"
INDEX_MD = BUNDLE_ROOT / "INDEX.md"

SNAPSHOT = "2026-06-24"
SOURCE_URL = "https://vasp.at/wiki/"

SUMMARY_CAP = 240
RELATED_CAP = 12

STOPWORDS = {
    "the", "a", "an", "of", "to", "in", "for", "and", "or", "is", "are",
    "be", "with", "by", "on", "as", "at", "from", "this", "that", "it",
    "its", "if", "not", "can", "will", "using", "used", "use", "set",
    "each", "e.g", "i.e", "see", "via",
}

# ---------------------------------------------------------------------------
# Regexes
# ---------------------------------------------------------------------------
HEADING_RE = re.compile(r"^#\s+(.*\S)\s*$")
SOURCE_RE = re.compile(r"<!--\s*Source:\s*(\S+)")
# outgoing relative .md links: ](../bucket/slug.md) or ](slug.md) or ](./slug.md)
LINK_RE = re.compile(r"\]\((\.{0,2}/?[^)]+?\.md)\)")
MD_LINK_INLINE_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


# ---------------------------------------------------------------------------
# Markdown cleaning helpers
# ---------------------------------------------------------------------------
def clean_markdown(text: str) -> str:
    """Strip common markdown artifacts from a prose fragment."""
    # [text](link) -> text
    text = MD_LINK_INLINE_RE.sub(lambda m: m.group(1), text)
    # escape backslashes used by the wiki dump: \[ \] \| \> etc.
    text = re.sub(r"\\([\[\]|>_*<])", r"\1", text)
    # remaining stray backslashes
    text = text.replace("\\", "")
    # bold / code markers
    text = text.replace("**", "").replace("`", "")
    # table pipes -> spaces
    text = text.replace("|", " ")
    # collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def clean_tagdef(text: str) -> str:
    """Clean the TYPE portion of a TAGDEF line (after '=')."""
    text = text.replace("\\[", "[").replace("\\]", "]")
    text = text.replace("\\|", "|").replace("\\>", ">").replace("\\<", "<")
    text = text.replace("\\", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def first_sentence(text: str) -> str:
    """Return text up to and including the first sentence-ending period."""
    # find first '. ' or a trailing '.'
    m = re.search(r"\.(?:\s|$)", text)
    if m:
        return text[: m.start() + 1].strip()
    return text.strip()


def cap_summary(text: str, cap: int = SUMMARY_CAP) -> str:
    """Cap to ~cap chars on a word boundary."""
    text = text.replace("\n", " ").strip()
    if len(text) <= cap:
        return text
    cut = text[:cap]
    # back up to last whitespace
    idx = cut.rfind(" ")
    if idx > 0:
        cut = cut[:idx]
    return cut.rstrip()


# ---------------------------------------------------------------------------
# File parsing
# ---------------------------------------------------------------------------
def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def parse_heading(lines: list[str]) -> str | None:
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            return m.group(1).strip()
    return None


def parse_source_title(lines: list[str]) -> str | None:
    for line in lines[:3]:
        m = SOURCE_RE.search(line)
        if m:
            url = m.group(1)
            marker = "index.php/"
            if marker in url:
                seg = url.split(marker, 1)[1]
                seg = seg.replace("_", " ").replace("/", " ").strip()
                if seg:
                    return seg
    return None


def title_for(path: Path, lines: list[str]) -> str:
    heading = parse_heading(lines)
    if heading:
        return heading
    src = parse_source_title(lines)
    if src:
        return src
    return path.stem


def body_after_heading(lines: list[str]) -> list[str]:
    """Return lines after the first '# ' heading."""
    out: list[str] = []
    seen = False
    for line in lines:
        if not seen:
            if HEADING_RE.match(line):
                seen = True
            continue
        out.append(line)
    return out


def find_description(body: list[str]) -> str | None:
    """Find the 'Description:' sentence, joining wrapped physical lines."""
    for i, line in enumerate(body):
        stripped = line.lstrip()
        if stripped.startswith("Description:"):
            collected = [stripped[len("Description:"):].strip()]
            # join following lines until a blank line or structural break
            j = i + 1
            while j < len(body):
                nxt = body[j]
                if not nxt.strip():
                    break
                if nxt.lstrip().startswith(("#", "|", "-", "*")):
                    break
                if nxt.strip().startswith("---"):
                    break
                collected.append(nxt.strip())
                j += 1
            raw = " ".join(c for c in collected if c)
            cleaned = clean_markdown(raw)
            return first_sentence(cleaned)
    return None


def find_fallback_prose(body: list[str], tagdef_line: str | None) -> str | None:
    """First non-empty prose line that is not table/tagdef/default."""
    for line in body:
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            continue
        if s.startswith("|"):
            continue
        if s.startswith("---") or set(s) <= {"-"}:
            continue
        if tagdef_line is not None and s == tagdef_line.strip():
            continue
        if s.startswith("Default:") or s.startswith("Default "):
            continue
        if s.lower().startswith("redirect to"):
            continue
        cleaned = clean_markdown(s)
        if cleaned:
            return first_sentence(cleaned)
    return None


def parse_tagdef_type(body: list[str]) -> str | None:
    """The line immediately after '# TAG' is the TAGDEF; return TYPE (after '=')."""
    for line in body:
        if line.strip():
            first = line.strip()
            break
    else:
        return None
    # TAGDEF may wrap (ISMEAR), but the '=' is on the first line.
    if "=" not in first:
        return None
    # The TAGDEF could itself wrap onto the next physical line; gather contiguous
    # non-empty lines until blank, then split on first '='.
    collected = []
    started = False
    for line in body:
        if not started:
            if line.strip():
                started = True
                collected.append(line.strip())
            continue
        if not line.strip():
            break
        if line.lstrip().startswith(("#", "|")) or line.strip().startswith("Default:"):
            break
        collected.append(line.strip())
    joined = " ".join(collected)
    if "=" not in joined:
        return None
    rhs = joined.split("=", 1)[1]
    return clean_tagdef(rhs) or None


def parse_default(lines: list[str], tag: str) -> str | None:
    """Find a 'Default: **TAG**' value, standalone or in a table cell."""
    pat = re.compile(r"Default:\s*\*\*" + re.escape(tag) + r"\*\*")
    for line in lines:
        if pat.search(line):
            # everything after the matching marker
            rest = line[pat.search(line).end():]
            # table cell form: '| = largest ENMAX ... |' ; standalone: ' = 1'
            # strip table pipes
            rest = rest.replace("|", " ")
            rest = rest.strip()
            if rest.startswith("="):
                rest = rest[1:].strip()
            cleaned = clean_markdown(rest)
            cleaned = cleaned.strip().rstrip(".")
            if cleaned:
                return cleaned
    return None


# ---------------------------------------------------------------------------
# Link normalization
# ---------------------------------------------------------------------------
def normalize_link(raw: str, page_bucket: str) -> str | None:
    """Normalize an outgoing .md link to 'bucket/slug.md'."""
    raw = raw.strip()
    if not raw.endswith(".md"):
        return None
    # forms: ../bucket/slug.md  |  ./slug.md  |  slug.md  |  bucket/slug.md
    if raw.startswith("../"):
        rest = raw[3:]
        parts = rest.split("/")
        if len(parts) >= 2:
            bucket = parts[0]
            slug = "/".join(parts[1:])
            return f"{bucket}/{slug}"
        return None
    if raw.startswith("./"):
        raw = raw[2:]
    # bare slug (same-bucket sibling) — no slash
    if "/" not in raw:
        return f"{page_bucket}/{raw}"
    # already bucket/slug form
    return raw


def extract_related(body: list[str], page_bucket: str, self_path: str) -> list[str]:
    text = "\n".join(body)
    related: list[str] = []
    seen: set[str] = set()
    for m in LINK_RE.finditer(text):
        norm = normalize_link(m.group(1), page_bucket)
        if not norm:
            continue
        if norm == self_path:
            continue
        if norm in seen:
            continue
        seen.add(norm)
        related.append(norm)
        if len(related) >= RELATED_CAP:
            break
    return related


# ---------------------------------------------------------------------------
# Redirect (alias) parsing
# ---------------------------------------------------------------------------
def parse_redirect(path: Path) -> tuple[str, str] | None:
    """Return (alias_title, normalized_target 'bucket/slug.md') or None."""
    lines = read_lines(path)
    alias = parse_heading(lines)
    if not alias:
        return None
    body = body_after_heading(lines)
    # find 'Redirect to:' then the first link target (may wrap)
    text_parts: list[str] = []
    seen_redirect = False
    for line in body:
        if not seen_redirect:
            if line.strip().lower().startswith("redirect to"):
                seen_redirect = True
            continue
        text_parts.append(line)
    blob = "\n".join(text_parts)
    # join wrapped link: collapse newlines+indent inside the markdown link
    blob = re.sub(r"\n\s*", " ", blob)
    m = MD_LINK_INLINE_RE.search(blob)
    if not m:
        return None
    target = m.group(2).strip()
    norm = normalize_link(target, path.parent.name)
    if not norm:
        return None
    return alias, norm


# ---------------------------------------------------------------------------
# Keywords
# ---------------------------------------------------------------------------
def build_keywords(title: str, aliases: list[str], summary: str,
                   categories: list[str]) -> list[str]:
    blob = " ".join([title, " ".join(aliases), summary, " ".join(categories)])
    tokens = re.split(r"[^A-Za-z0-9]+", blob)
    out: set[str] = set()
    for tok in tokens:
        tok = tok.lower()
        if len(tok) < 2:
            continue
        if tok in STOPWORDS:
            continue
        out.add(tok)
    return sorted(out)


# ---------------------------------------------------------------------------
# Main build
# ---------------------------------------------------------------------------
def is_index_file(path: Path) -> bool:
    return path.name == "_index.md" or path == REFERENCES / "index.md"


def main() -> None:
    # title -> categories map from pages.json
    pages_meta = json.loads(PAGES_JSON.read_text(encoding="utf-8"))
    cat_map: dict[str, list[str]] = {}
    for obj in pages_meta:
        title = obj.get("title")
        if title is not None:
            cat_map[title] = obj.get("categories", []) or []

    # Pass 1: collect primary pages (everything except redirects + index files)
    primary: list[dict] = []
    path_to_entry: dict[str, dict] = {}

    md_files = sorted(REFERENCES.rglob("*.md"))
    for path in md_files:
        if is_index_file(path):
            continue
        bucket = path.parent.name
        rel = f"{bucket}/{path.name}"
        if bucket == "redirects":
            continue  # become aliases, not primary entries

        lines = read_lines(path)
        title = title_for(path, lines)
        body = body_after_heading(lines)

        categories = cat_map.get(title, [])

        # summary
        desc = find_description(body)
        if desc is None:
            desc = find_fallback_prose(body, None) or ""

        if bucket == "incar-tags":
            type_str = parse_tagdef_type(body)
            default_str = parse_default(lines, title)
            prefix = ""
            if type_str and default_str:
                prefix = f"{type_str}, default = {default_str}. "
            elif type_str:
                prefix = f"{type_str}. "
            elif default_str:
                prefix = f"default = {default_str}. "
            summary = (prefix + desc).strip()
        else:
            summary = desc.strip()

        summary = cap_summary(summary)

        related = extract_related(body, bucket, rel)

        entry = {
            "path": rel,
            "title": title,
            "bucket": bucket,
            "categories": categories,
            "summary": summary,
            "aliases": [],          # filled in pass 2
            "related": related,
            "keywords": [],         # finalized after aliases
        }
        primary.append(entry)
        path_to_entry[rel] = entry

    # Pass 2: redirects -> aliases
    redirect_dir = REFERENCES / "redirects"
    for path in sorted(redirect_dir.glob("*.md")):
        if path.name == "_index.md":
            continue
        parsed = parse_redirect(path)
        if not parsed:
            continue
        alias, target = parsed
        entry = path_to_entry.get(target)
        if entry is None:
            continue  # target not a primary page (another redirect / missing)
        if alias not in entry["aliases"]:
            entry["aliases"].append(alias)

    # finalize aliases + keywords
    for entry in primary:
        entry["aliases"] = sorted(set(entry["aliases"]))
        entry["keywords"] = build_keywords(
            entry["title"], entry["aliases"], entry["summary"],
            entry["categories"],
        )

    # sort by bucket then title
    primary.sort(key=lambda e: (e["bucket"], e["title"].lower()))

    # ---- write index.json ----
    index_obj = {
        "snapshot": SNAPSHOT,
        "count": len(primary),
        "source": "https://vasp.at/wiki/",
        "pages": primary,
    }
    INDEX_JSON.write_text(
        json.dumps(index_obj, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # ---- write INDEX.md ----
    lines_out: list[str] = []
    lines_out.append("# VASP Wiki — Reference Index")
    lines_out.append("")
    lines_out.append(
        f"Snapshot: {SNAPSHOT} · {len(primary)} pages · "
        f"GFDL 1.2 (© VASP wiki contributors, from https://vasp.at/wiki/)"
    )
    lines_out.append(
        'How to use: run `vaspwiki search "<query>"` (tool in tools/vaspwiki) '
        "or grep this file, then open ONLY the listed reference files."
    )
    lines_out.append("")

    # group by bucket
    buckets: dict[str, list[dict]] = {}
    for entry in primary:
        buckets.setdefault(entry["bucket"], []).append(entry)

    for bucket in sorted(buckets):
        entries = sorted(buckets[bucket], key=lambda e: e["title"].lower())
        lines_out.append(f"## {bucket} ({len(entries)})")
        for entry in entries:
            summary = entry["summary"].replace("\n", " ").strip()
            title = entry["title"]
            path = entry["path"]
            alias_seg = ""
            if entry["aliases"]:
                alias_seg = "  ·  aliases: " + ", ".join(entry["aliases"])
            line = (
                f"- **{title}** — {summary}{alias_seg}  →  references/{path}"
            )
            line = line.replace("\n", " ")
            lines_out.append(line)
        lines_out.append("")

    INDEX_MD.write_text("\n".join(lines_out).rstrip("\n") + "\n", encoding="utf-8")

    # stdout summary
    alias_pages = sum(1 for e in primary if e["aliases"])
    print(f"Wrote {INDEX_JSON.relative_to(BUNDLE_ROOT)}: {len(primary)} entries")
    print(f"Wrote {INDEX_MD.relative_to(BUNDLE_ROOT)}")
    print(f"Pages with >=1 alias: {alias_pages}")


if __name__ == "__main__":
    main()
