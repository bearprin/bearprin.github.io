#!/usr/bin/env python

"""Fetch Google Scholar citation stats and write assets/json/citations.json.

Runs on the gh-pages branch (the static build artifact actually served). Reuses
the scholarly fetch logic from bin/update_scholar_citations.py (master branch),
but writes a frontend-friendly JSON consumed by assets/js/citations.js instead
of the Jekyll YAML data file.
"""

import os
import sys
import json
from datetime import datetime
from scholarly import scholarly, ProxyGenerator

# gh-pages has no _data/socials.yml; the Scholar ID is public, so hardcode it.
SCHOLAR_USER_ID = "DqEP_nIAAAAJ"
OUTPUT_FILE = "assets/json/citations.json"


def setup_proxy() -> None:
    """Configure scholarly proxy. ScraperAPI if SCRAPER_API_KEY env is set, else FreeProxies."""
    pg = ProxyGenerator()
    api_key = os.environ.get("SCRAPER_API_KEY")
    if api_key:
        if pg.ScraperAPI(api_key):
            scholarly.use_proxy(pg)
            print("Proxy: ScraperAPI configured.")
            return
        print("Warning: ScraperAPI setup failed, falling back to FreeProxies.")
    if pg.FreeProxies():
        scholarly.use_proxy(pg)
        print("Proxy: FreeProxies configured.")
        return
    print("Warning: No proxy configured. Direct request likely blocked by Scholar.")


def get_scholar_citations() -> None:
    """Fetch Google Scholar citation data and write it to OUTPUT_FILE."""
    print(f"Fetching citations for Google Scholar ID: {SCHOLAR_USER_ID}")
    today = datetime.now().strftime("%Y-%m-%d")

    setup_proxy()
    scholarly.set_timeout(30)
    scholarly.set_retries(5)
    try:
        author = scholarly.search_author_id(SCHOLAR_USER_ID)
        author_data = scholarly.fill(author)
    except Exception as e:
        # Leave any existing citations.json untouched so the page keeps its last
        # good values instead of dropping to zeros.
        print(
            f"Error fetching author data for user ID '{SCHOLAR_USER_ID}': {e}. "
            f"Keeping existing {OUTPUT_FILE} unchanged."
        )
        sys.exit(1)

    if not author_data or "publications" not in author_data:
        print(
            f"Could not fetch usable author data for user ID '{SCHOLAR_USER_ID}'. "
            f"Keeping existing {OUTPUT_FILE} unchanged."
        )
        sys.exit(1)

    citation_data = {
        "total": author_data.get("citedby", 0),
        "h_index": author_data.get("hindex", 0),
        "i10_index": author_data.get("i10index", 0),
        "updated": today,
        "papers": {},
    }
    print(
        f"Author totals — citations: {citation_data['total']}, "
        f"h-index: {citation_data['h_index']}, i10-index: {citation_data['i10_index']}"
    )

    for pub in author_data["publications"]:
        try:
            pub_id = pub.get("pub_id") or pub.get("author_pub_id")
            if not pub_id:
                print(
                    f"Warning: No ID for publication '{pub.get('bib', {}).get('title', 'Unknown')}'. Skipping."
                )
                continue
            citation_data["papers"][pub_id] = {
                "title": pub.get("bib", {}).get("title", "Unknown Title"),
                "year": pub.get("bib", {}).get("pub_year", "Unknown Year"),
                "citations": pub.get("num_citations", 0),
            }
        except Exception as e:
            print(
                f"Error processing publication '{pub.get('bib', {}).get('title', 'Unknown')}': {e}. Skipping."
            )

    # Don't trust an empty result that would blank the page; keep the old file.
    if not citation_data["total"] and not citation_data["papers"]:
        print(f"Fetched empty data. Keeping existing {OUTPUT_FILE} unchanged.")
        sys.exit(1)

    try:
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        with open(OUTPUT_FILE, "w") as f:
            json.dump(citation_data, f, indent=2, sort_keys=True, ensure_ascii=False)
            f.write("\n")
        print(f"Citation data saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error writing citation data to {OUTPUT_FILE}: {e}.")
        sys.exit(1)


if __name__ == "__main__":
    try:
        get_scholar_citations()
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
