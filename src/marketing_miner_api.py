"""Marketing Miner API client — CZ/SK keyword data, complements Ahrefs.

Used in /evisions-topic-cluster:
  Krok 1 — `volume` mode: cross-check Search Volume for keywords found via Ahrefs.
  Krok 3 — `suggestions` mode: additional keyword ideas for the topic (CZ/SK-tuned
           suggestion engine may surface long-tail Ahrefs doesn't).

API docs:
  https://help.marketingminer.com/en/article/keyword-search-volume-api/
  https://help.marketingminer.com/en/article/keyword-suggestions-api/

Costs/limits: search-volume-data = 3 credits/keyword, 120 keywords/minute.
              suggestions = 10 credits/keyword, 60 keywords/minute.

NOTE: the search-volume-data docs claim the `keyword` param can be repeated
for batch lookups (`keyword=a&keyword=b`), but in practice the API only
returns data for the last `keyword` value when the param is repeated —
confirmed by testing. This client sends one keyword per request.

Usage:
    python src/marketing_miner_api.py volume "seo" "ai v seo" "geo optimalizace"
    python src/marketing_miner_api.py suggestions "ai seo" --lang cs
"""

import argparse
import json
import sys
import time

import requests

from config import config

VOLUME_URL = "https://profilers-api.marketingminer.com/keywords/search-volume-data"
SUGGESTIONS_URL = "https://profilers-api.marketingminer.com/keywords/suggestions"
REQUEST_DELAY_SECONDS = 0.5  # keeps well under the rate limit for either endpoint
SUPPORTED_LANGS = {"cs", "sk", "us", "gb", "pl"}


def _check_lang(lang: str) -> None:
    if lang not in SUPPORTED_LANGS:
        raise ValueError(f"Unsupported lang '{lang}'. Supported: {sorted(SUPPORTED_LANGS)}")
    if not config.marketing_miner_api_key:
        raise ValueError("MARKETING_MINER_API_KEY not set in .env")


def get_search_volume(keywords: list[str], lang: str = "cs") -> list[dict]:
    """Fetch search volume data for a list of keywords from Marketing Miner.

    Returns a list of dicts (one per keyword found), each with keys:
    keyword, search_volume, cpc, yoy_change, peak_month, monthly_sv.
    Keywords with no data in Marketing Miner's database are simply omitted
    by the API — the caller should reconcile against the input list.
    """
    _check_lang(lang)

    results: list[dict] = []
    for idx, kw in enumerate(keywords):
        params = {"lang": lang, "api_token": config.marketing_miner_api_key, "keyword": kw}
        resp = requests.get(VOLUME_URL, params=params, timeout=30)
        resp.raise_for_status()
        payload = resp.json()

        if payload.get("status") != "success":
            raise RuntimeError(f"Marketing Miner API error for '{kw}': {payload}")

        results.extend(payload.get("data", []))

        if idx + 1 < len(keywords):
            time.sleep(REQUEST_DELAY_SECONDS)

    return results


def get_keyword_suggestions(seed_keyword: str, lang: str = "cs") -> list[dict]:
    """Fetch keyword suggestions for a single seed keyword from Marketing Miner.

    Returns a list of dicts, each with keys: keyword, search_volume, cpc,
    difficulty, serp_features, yoy_change, peak_month, monthly_sv.
    """
    _check_lang(lang)

    params = {"lang": lang, "api_token": config.marketing_miner_api_key, "keyword": seed_keyword}
    resp = requests.get(SUGGESTIONS_URL, params=params, timeout=30)
    resp.raise_for_status()
    payload = resp.json()

    if payload.get("status") != "success":
        raise RuntimeError(f"Marketing Miner API error for '{seed_keyword}': {payload}")

    return payload.get("data", {}).get("keywords", [])


def main() -> None:
    parser = argparse.ArgumentParser(description="Marketing Miner keyword data lookup")
    subparsers = parser.add_subparsers(dest="mode", required=True)

    volume_parser = subparsers.add_parser("volume", help="Search volume cross-check (Krok 1)")
    volume_parser.add_argument("keywords", nargs="+", help="Keywords to look up")
    volume_parser.add_argument("--lang", default="cs", choices=sorted(SUPPORTED_LANGS))

    suggestions_parser = subparsers.add_parser("suggestions", help="Keyword suggestions (Krok 3)")
    suggestions_parser.add_argument("seed_keyword", help="Seed keyword/topic")
    suggestions_parser.add_argument("--lang", default="cs", choices=sorted(SUPPORTED_LANGS))

    args = parser.parse_args()

    try:
        if args.mode == "volume":
            data = get_search_volume(args.keywords, lang=args.lang)
            found = {row["keyword"] for row in data}
            missing = [kw for kw in args.keywords if kw not in found]
            print(json.dumps(data, ensure_ascii=False, indent=2))
            if missing:
                print(f"\nNo Marketing Miner data for: {missing}", file=sys.stderr)
        else:
            data = get_keyword_suggestions(args.seed_keyword, lang=args.lang)
            print(json.dumps(data, ensure_ascii=False, indent=2))
            if not data:
                print(f"\nNo Marketing Miner suggestions for: {args.seed_keyword}", file=sys.stderr)
    except (ValueError, RuntimeError, requests.RequestException) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
