"""
crawl_index.py — Build the VASP wiki page index.

Steps
-----
1. Query the MediaWiki siteinfo API to discover all registered namespaces.
2. Decide which namespace IDs to include:
     - Always: 0 (main/article) and 14 (Category).
     - Additionally: any custom namespace whose canonical name or local name
       matches (case-insensitive) "tutorial", "howto", or "construction".
3. For each included namespace, paginate through allpages (500 per request).
4. Write _meta/pages.json: a flat JSON list of {title, pageid, ns} objects.
5. Print namespace breakdown and total count.

Throttle: ~0.3 s between API calls.
"""

import json
import time
import urllib.parse
from datetime import datetime, timezone

from wiki_common import (
    _META,
    http_get_json,
    safe_slug,
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

API_BASE    = "https://vasp.at/wiki/api.php"
THROTTLE_S  = 0.3          # seconds between API calls

# Namespace IDs always included, regardless of their name.
_ALWAYS_INCLUDE = {0, 14}

# Keywords that trigger inclusion of a *custom* namespace when its name
# matches (case-insensitive substring match).
_CUSTOM_KEYWORDS = {"tutorial", "howto", "construction"}


# ---------------------------------------------------------------------------
# Namespace selection
# ---------------------------------------------------------------------------

def fetch_namespaces() -> dict[int, str]:
    """
    Query siteinfo and return a mapping of {ns_id: display_name} for all
    namespaces defined on the wiki.
    """
    url = (
        f"{API_BASE}?action=query&meta=siteinfo"
        "&siprop=namespaces&format=json"
    )
    data = http_get_json(url)
    raw_ns = data.get("query", {}).get("namespaces", {})

    result: dict[int, str] = {}
    for key, info in raw_ns.items():
        try:
            ns_id = int(key)
        except ValueError:
            continue
        # Prefer the canonical name; fall back to the localised name.
        name = info.get("canonical") or info.get("*") or info.get("content", "")
        result[ns_id] = name
    return result


def select_namespaces(all_ns: dict[int, str]) -> dict[int, str]:
    """
    Return the subset of namespaces to crawl.

    Inclusion criteria:
      - ns_id in _ALWAYS_INCLUDE (0 = main, 14 = Category).
      - OR the namespace name (canonical or local) contains one of
        _CUSTOM_KEYWORDS (case-insensitive).
    """
    selected: dict[int, str] = {}
    for ns_id, name in all_ns.items():
        name_lower = name.lower()
        if ns_id in _ALWAYS_INCLUDE:
            selected[ns_id] = name
        elif any(kw in name_lower for kw in _CUSTOM_KEYWORDS):
            selected[ns_id] = name
    return selected


# ---------------------------------------------------------------------------
# Page enumeration
# ---------------------------------------------------------------------------

def enumerate_pages(ns_id: int) -> list[dict]:
    """
    Return all pages in namespace *ns_id* via allpages pagination.

    Each returned dict has keys: title, pageid, ns.
    """
    pages: list[dict] = []
    continue_token: str | None = None

    while True:
        params = {
            "action":      "query",
            "list":        "allpages",
            "aplimit":     "500",
            "apnamespace": str(ns_id),
            "format":      "json",
        }
        if continue_token is not None:
            params["apcontinue"] = continue_token
            # The MW continue envelope also needs the top-level continue key.
            params["continue"] = ""

        url = f"{API_BASE}?{urllib.parse.urlencode(params)}"
        data = http_get_json(url)

        batch = data.get("query", {}).get("allpages", [])
        for page in batch:
            pages.append({
                "title":  page["title"],
                "pageid": page["pageid"],
                "ns":     page["ns"],
            })

        # Check for continuation.
        cont = data.get("continue", {})
        if "apcontinue" in cont:
            continue_token = cont["apcontinue"]
            time.sleep(THROTTLE_S)
        else:
            break

        time.sleep(THROTTLE_S)

    return pages


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    _META.mkdir(parents=True, exist_ok=True)

    # 1. Discover namespaces.
    print("Fetching siteinfo (namespaces)…")
    all_ns = fetch_namespaces()
    time.sleep(THROTTLE_S)

    # 2. Select which ones to crawl.
    selected = select_namespaces(all_ns)

    print("\nIncluded namespaces:")
    for ns_id, name in sorted(selected.items()):
        label = name if name else "(main)"
        tag = " [always]" if ns_id in _ALWAYS_INCLUDE else " [keyword match]"
        print(f"  ns={ns_id:4d}  {label}{tag}")

    # 3. Enumerate pages per namespace.
    all_pages: list[dict] = []
    ns_counts: dict[int, int] = {}

    for ns_id, ns_name in sorted(selected.items()):
        label = ns_name if ns_name else "(main)"
        print(f"\nEnumerating ns={ns_id} ({label})…", flush=True)
        pages = enumerate_pages(ns_id)
        ns_counts[ns_id] = len(pages)
        all_pages.extend(pages)
        print(f"  → {len(pages)} pages")
        time.sleep(THROTTLE_S)

    # 4. Write pages.json.
    pages_path = _META / "pages.json"
    pages_path.write_text(
        json.dumps(all_pages, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\nWrote {pages_path}")

    # 5. Summary.
    print("\nNamespace breakdown:")
    for ns_id, count in sorted(ns_counts.items()):
        label = selected[ns_id] if selected[ns_id] else "(main)"
        print(f"  ns={ns_id:4d}  {label:<30s}  {count} pages")
    print(f"\nTotal pages indexed: {len(all_pages)}")


if __name__ == "__main__":
    main()
