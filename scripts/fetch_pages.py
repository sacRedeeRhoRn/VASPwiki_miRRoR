"""
fetch_pages.py — Download HTML and wikitext for every page in the index.

Usage
-----
    python3 fetch_pages.py [--limit N]

    --limit N   Fetch only the first N pages.  High-value pages are prepended
                to the fetch order so they are always captured first when N is
                small (see HIGH_VALUE_TITLES below).

Outputs
-------
  _raw/html/<slug>.html       Parsed HTML from the MediaWiki parse API.
  _raw/wikitext/<slug>.txt    Raw wikitext (best-effort; skipped on failure).
  _meta/pages.json            Updated in-place with revid/categories/
                              displaytitle/fetched_at per fetched page.
  _meta/slugmap.json          title → slug mapping (built incrementally).
  _meta/fetch_errors.log      One line per failed page (appended).

Throttle: ~0.7 s between pages.  Resumable: skips pages whose HTML already
exists AND whose pages.json entry already has 'fetched_at'.
"""

import argparse
import json
import os
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

from wiki_common import (
    _META,
    _RAW,
    http_get_json,
    http_get_text,
    safe_slug,
)

# API/page base URLs — defined here (wiki_common hosts path constants only).
API_BASE   = "https://vasp.at/wiki/api.php"
PAGE_BASE  = "https://vasp.at/wiki/index.php"

THROTTLE_S = 0.7   # seconds between pages

# High-value pages prepended to the fetch order when --limit is active.
HIGH_VALUE_TITLES = [
    "ENCUT",
    "ISMEAR",
    "POSCAR",
    "KPOINTS",
    "ALGO",
    "OUTCAR",
]


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def load_pages(path: Path) -> list[dict]:
    """Load pages.json; return list of page dicts."""
    if not path.exists():
        raise FileNotFoundError(
            f"pages.json not found at {path}. Run crawl_index.py first."
        )
    return json.loads(path.read_text(encoding="utf-8"))


def save_pages(path: Path, pages: list[dict]) -> None:
    """Persist pages.json atomically (write then rename)."""
    tmp = path.with_suffix(".json.tmp")
    try:
        content = json.dumps(pages, indent=2, ensure_ascii=False)
        # Use direct file operations to ensure proper flush
        with open(tmp, 'w', encoding='utf-8') as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())
    except Exception as e:
        print(f"[DEBUG] write failed: {type(e).__name__}: {e}")
        raise
    # Verify tmp exists before replacing
    if not tmp.exists():
        raise FileNotFoundError(f"Tmp file was not created: {tmp}")
    os.replace(str(tmp), str(path))


def load_slugmap(path: Path) -> dict[str, str]:
    """Load slugmap.json if present; otherwise return empty dict."""
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def save_slugmap(path: Path, slugmap: dict[str, str]) -> None:
    """Persist slugmap.json."""
    path.write_text(
        json.dumps(slugmap, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )


def log_error(log_path: Path, title: str, error: Exception) -> None:
    """Append a single error line to fetch_errors.log."""
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(f"{ts}\t{title}\t{error}\n")


# ---------------------------------------------------------------------------
# Fetch logic
# ---------------------------------------------------------------------------

def fetch_html_meta(title: str) -> dict:
    """
    Fetch parsed HTML + metadata for *title* via the parse API.

    Returns a dict with keys:
      html        : str   — the full parsed HTML body
      revid       : int
      displaytitle: str
      categories  : list[str]   — plain category titles (no "Category:" prefix)
    """
    params = {
        "action": "parse",
        "page":   title,
        "prop":   "text|categories|revid|displaytitle",
        "format": "json",
    }
    url = f"{API_BASE}?{urllib.parse.urlencode(params)}"
    data = http_get_json(url)

    parse = data.get("parse", {})
    html = parse.get("text", {}).get("*", "")
    revid = parse.get("revid", 0)
    displaytitle = parse.get("displaytitle", title)

    # Each category entry has a "*" key with the raw category title string
    # (e.g. "Category:Input files").  We strip the "Category:" prefix so the
    # stored list is clean plain names.
    raw_cats = parse.get("categories", [])
    categories = []
    for cat in raw_cats:
        cat_title = cat.get("*", "")
        # Strip leading "Category:" if present (case-insensitive).
        if cat_title.lower().startswith("category:"):
            cat_title = cat_title[len("category:"):]
        categories.append(cat_title)

    return {
        "html":         html,
        "revid":        revid,
        "displaytitle": displaytitle,
        "categories":   categories,
    }


def fetch_wikitext(title: str) -> str | None:
    """
    Best-effort fetch of raw wikitext for *title*.

    Returns the wikitext string, or None on any failure.
    """
    params = {"title": title, "action": "raw"}
    url = f"{PAGE_BASE}?{urllib.parse.urlencode(params)}"
    try:
        return http_get_text(url)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Ordering helper
# ---------------------------------------------------------------------------

def build_fetch_order(
    pages: list[dict],
    limit: int | None,
    title_index: dict[str, int],
) -> list[dict]:
    """
    Return the ordered list of pages to fetch.

    When *limit* is set:
      1. Collect high-value pages that actually exist in *pages*.
      2. Append remaining pages (skipping those already added).
      3. Truncate to *limit*.
    When *limit* is None: return *pages* as-is.
    """
    if limit is None:
        return list(pages)

    seen_ids: set[int] = set()
    ordered: list[dict] = []

    # Prepend high-value pages.
    for hv_title in HIGH_VALUE_TITLES:
        idx = title_index.get(hv_title)
        if idx is not None:
            page = pages[idx]
            ordered.append(page)
            seen_ids.add(page["pageid"])

    # Append remaining pages, deduplicating high-value ones.
    for page in pages:
        if page["pageid"] not in seen_ids:
            ordered.append(page)

    return ordered[:limit]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch HTML/wikitext for pages listed in _meta/pages.json."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        metavar="N",
        help="Fetch only the first N pages (high-value pages are prepended).",
    )
    args = parser.parse_args()

    # Ensure output directories exist.
    html_dir     = _RAW / "html"
    wikitext_dir = _RAW / "wikitext"
    html_dir.mkdir(parents=True, exist_ok=True)
    wikitext_dir.mkdir(parents=True, exist_ok=True)
    _META.mkdir(parents=True, exist_ok=True)

    pages_path   = _META / "pages.json"
    slugmap_path = _META / "slugmap.json"
    errors_path  = _META / "fetch_errors.log"

    # Load state.
    pages   = load_pages(pages_path)
    slugmap = load_slugmap(slugmap_path)

    # Build a title→index lookup for fast high-value lookup.
    title_index = {p["title"]: i for i, p in enumerate(pages)}

    # Determine fetch order.
    fetch_order = build_fetch_order(pages, args.limit, title_index)

    if args.limit is not None:
        print(f"Fetching {len(fetch_order)} pages (limit={args.limit}).")
        hv_present = [t for t in HIGH_VALUE_TITLES if t in title_index]
        print(f"High-value pages prepended: {hv_present}")
    else:
        print(f"Fetching all {len(fetch_order)} pages.")

    fetched   = 0
    skipped   = 0
    errors    = 0
    is_limited = args.limit is not None

    for i, page in enumerate(fetch_order, start=1):
        title = page["title"]
        slug  = safe_slug(title)

        # Update slugmap immediately (even for skipped pages).
        slugmap[title] = slug

        html_path     = html_dir     / f"{slug}.html"
        wikitext_path = wikitext_dir / f"{slug}.txt"

        # Resumability check: skip if HTML exists AND pages.json has fetched_at.
        existing_entry = pages[title_index[title]] if title in title_index else None
        if (
            html_path.exists()
            and existing_entry is not None
            and existing_entry.get("fetched_at")
        ):
            skipped += 1
            continue

        is_high_value = title in HIGH_VALUE_TITLES

        # --- Fetch HTML + metadata ---
        try:
            meta = fetch_html_meta(title)
        except Exception as exc:
            errors += 1
            log_error(errors_path, title, exc)
            print(f"  ERROR [{i}/{len(fetch_order)}] {title}: {exc}")
            time.sleep(THROTTLE_S)
            continue

        # Write HTML.
        html_path.write_text(meta["html"], encoding="utf-8")

        # --- Best-effort wikitext ---
        wikitext = fetch_wikitext(title)
        if wikitext is not None:
            wikitext_path.write_text(wikitext, encoding="utf-8")

        # --- Update pages.json entry ---
        ts_now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        if existing_entry is not None:
            existing_entry["revid"]        = meta["revid"]
            existing_entry["categories"]   = meta["categories"]
            existing_entry["displaytitle"] = meta["displaytitle"]
            existing_entry["fetched_at"]   = ts_now

        fetched += 1

        # Persist every page so the run is resumable.
        save_pages(pages_path, pages)
        save_slugmap(slugmap_path, slugmap)

        # Progress reporting.
        if is_limited and is_high_value:
            print(f"  [HIGH-VALUE] {title}  (slug: {slug})")
        elif fetched % 25 == 0:
            print(f"  Progress: {i}/{len(fetch_order)} processed, "
                  f"{fetched} fetched, {skipped} skipped, {errors} errors")

        time.sleep(THROTTLE_S)

    # Final save.
    save_pages(pages_path, pages)
    save_slugmap(slugmap_path, slugmap)

    print(
        f"\nDone. fetched={fetched}, skipped={skipped}, errors={errors}  "
        f"(errors logged to {errors_path})"
    )


if __name__ == "__main__":
    main()
