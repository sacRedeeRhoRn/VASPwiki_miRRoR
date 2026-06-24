"""
wiki_common.py — Shared helpers for the VASP wiki offline-mirror pipeline.

Provides:
  - safe_slug(title)         : filesystem-safe filename stem for a wiki page title
  - http_get_json(url)       : fetch URL, parse JSON, retry on transient errors
  - http_get_text(url)       : fetch URL, return text, retry on transient errors
  - Path constants           : BASE_DIR, _META, _RAW, REFERENCES

All HTTP calls use:
  User-Agent: VASP-wiki-mirror/1.0 (offline research mirror; contact: local)
  Retry: 3 attempts with exponential backoff on URLError / HTTP 5xx.

Python stdlib only — no third-party packages.
"""

import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------------------
# Path constants — resolved relative to THIS file so they work from any cwd.
# ---------------------------------------------------------------------------
# scripts/ is the parent of this file; one level up is the project root.
_SCRIPTS_DIR = Path(__file__).resolve().parent
BASE_DIR = _SCRIPTS_DIR.parent          # vasp-wiki/

_META       = BASE_DIR / "_meta"        # JSON manifests
_RAW        = BASE_DIR / "_raw"         # raw HTML + wikitext
REFERENCES  = BASE_DIR / "references"  # final Markdown outputs

# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

_USER_AGENT = "VASP-wiki-mirror/1.0 (offline research mirror; contact: local)"

_MAX_RETRIES = 3
_BACKOFF_BASE = 2.0   # seconds — doubles each retry: 2, 4, 8


def _build_request(url: str) -> urllib.request.Request:
    """Return a Request with the project User-Agent header set."""
    return urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})


def _should_retry(exc: Exception) -> bool:
    """Return True for transient errors worth retrying (URLError, HTTP 5xx)."""
    if isinstance(exc, urllib.error.HTTPError):
        return exc.code >= 500
    if isinstance(exc, urllib.error.URLError):
        return True
    return False


def _fetch_raw(url: str) -> bytes:
    """
    Fetch *url* and return raw bytes.

    Retries up to _MAX_RETRIES times with exponential backoff on URLError or
    HTTP 5xx.  Raises the last exception if all retries are exhausted.
    """
    last_exc: Exception | None = None
    for attempt in range(_MAX_RETRIES):
        try:
            req = _build_request(url)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except Exception as exc:
            last_exc = exc
            if _should_retry(exc) and attempt < _MAX_RETRIES - 1:
                wait = _BACKOFF_BASE ** (attempt + 1)
                time.sleep(wait)
            else:
                raise
    # Should never reach here, but satisfy type checkers.
    raise last_exc  # type: ignore[misc]


def http_get_json(url: str) -> dict:
    """
    Fetch *url* and decode the response body as UTF-8 JSON.

    Returns the parsed dict.  Propagates exceptions after retries.
    """
    raw = _fetch_raw(url)
    return json.loads(raw.decode("utf-8"))


def http_get_text(url: str) -> str:
    """
    Fetch *url* and decode the response body as UTF-8 text.

    Returns the decoded string.  Propagates exceptions after retries.
    """
    raw = _fetch_raw(url)
    return raw.decode("utf-8", errors="replace")


# ---------------------------------------------------------------------------
# Slug helper
# ---------------------------------------------------------------------------

# Characters that are unsafe on common filesystems (Windows/macOS/Linux).
# We map them to deterministic ASCII replacements so slugs are portable.
_UNSAFE_CHARS = str.maketrans({
    "/":  "__",   # namespace separator common in wiki titles → double underscore
    " ":  "_",    # space → underscore
    ":":  "-",    # colon
    "*":  "-",    # asterisk
    "?":  "-",    # question mark
    '"':  "-",    # double-quote
    "<":  "-",    # less-than
    ">":  "-",    # greater-than
    "|":  "-",    # pipe
    "\\": "-",    # backslash
    "\n": "-",    # stray newlines
    "\r": "-",    # carriage return
})


def safe_slug(title: str) -> str:
    """
    Convert a MediaWiki page title to a portable filesystem slug.

    Rules (applied in order):
      1. Strip leading/trailing whitespace.
      2. Replace `/` with `__`  (retains namespace path readability).
      3. Replace spaces with `_`.
      4. Replace other unsafe chars (`:*?"<>|\\`) with `-`.
      5. Collapse consecutive `-` or `_` runs (optional cosmetic cleanup).
      6. Strip leading/trailing `-` or `_`.

    Examples:
      "ENCUT"                   → "ENCUT"
      "POSCAR"                  → "POSCAR"
      "Category:Input files"    → "Category-Input_files"
      "Wannier90:Interface"     → "Wannier90-Interface"
      "Tutorial/Basics"         → "Tutorial__Basics"
    """
    slug = title.strip()
    slug = slug.translate(_UNSAFE_CHARS)

    # Collapse runs of the same separator (e.g. `---` → `-`, `___` → `_`).
    slug = re.sub(r"-{2,}", "-", slug)
    # Don't collapse `__` (it encodes `/`) but collapse longer runs.
    slug = re.sub(r"_{3,}", "__", slug)

    # Strip leading/trailing separators.
    slug = slug.strip("-_")

    # Fallback for edge-case empty slug.
    if not slug:
        slug = "untitled"

    return slug
