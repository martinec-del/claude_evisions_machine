"""Multi-model content tester for the evisions.cz blog workflow."""

import re
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import html2text
import pandas as pd
import requests
from bs4 import BeautifulSoup

from step4_html import convert_to_html

from adapters import ClaudeAdapter, GeminiAdapter, OpenAIAdapter
from adapters.base import BaseAdapter, ModelResponse
from config import Config, config


def fetch_article(url: str) -> tuple[str, str]:
    """
    Fetch article from URL and convert to markdown.

    Extracts the main blog content from evisions.cz pages,
    preserving heading structure and image positions.

    Args:
        url: Full URL of the evisions.cz blog article.

    Returns:
        Tuple of (markdown content, slug extracted from URL).

    Raises:
        requests.HTTPError: If the page cannot be fetched.
        ValueError: If no article content is found on the page.
    """
    print(f"Fetching: {url}")
    response = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # evisions.cz blog uses common WordPress-style content containers
    content_selectors = [
        "article.post",
        "div.entry-content",
        "div.post-content",
        "main article",
        "article",
        "main",
    ]
    container = None
    for selector in content_selectors:
        container = soup.select_one(selector)
        if container:
            break

    if not container:
        raise ValueError(f"No article content found at {url}")

    # Remove nav, footer, sidebar, script, style, and CTA/share/newsletter blocks
    for tag in container.select(
        "nav, footer, aside, script, style, "
        ".sidebar, .widget, .comments, "
        ".cta-block, .newsletter, .share-buttons, "
        "[class*='newsletter'], [class*='kontakt-cta'], [class*='share']"
    ):
        tag.decompose()

    # Convert to markdown
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False
    converter.body_width = 0  # no line wrapping
    converter.protect_links = True
    converter.mark_code = True

    markdown = converter.handle(str(container))

    # Clean up excessive blank lines
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

    # Extract slug from URL: /blog/nazev-clanku/ → nazev-clanku
    path = urlparse(url).path.rstrip("/")
    slug = path.split("/")[-1] if path else "clanek"

    return markdown, slug


def get_adapter(model_name: str, cfg: Config) -> BaseAdapter:
    """
    Get the appropriate adapter for a model.

    Args:
        model_name: Name of the model (e.g., 'gpt-4o', 'claude-3-5-sonnet').
        cfg: Configuration object.

    Returns:
        Initialized adapter for the model.

    Raises:
        ValueError: If model or provider is unknown.
    """
    if model_name not in cfg.models:
        raise ValueError(f"Unknown model: {model_name}")

    model_config = cfg.models[model_name]
    api_key = cfg.get_api_key(model_config.provider)

    adapters = {
        "openai": OpenAIAdapter,
        "google": GeminiAdapter,
        "anthropic": ClaudeAdapter,
    }

    adapter_class = adapters.get(model_config.provider)
    if not adapter_class:
        raise ValueError(f"Unknown provider: {model_config.provider}")

    return adapter_class(api_key, model_config.model_id)


def load_prompt(prompt_name: str, prompts_dir: Path) -> str:
    """
    Load a prompt template from file.

    Args:
        prompt_name: Name of the prompt file (without .md extension).
        prompts_dir: Directory containing prompt files.

    Returns:
        Prompt content as string.
    """
    prompt_path = prompts_dir / f"{prompt_name}.md"
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt not found: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")


def load_keywords(keywords_file: Path) -> str:
    """
    Load keywords from Excel file and format for prompt.

    Sorts by Volume descending (relative priority per workflow).

    Args:
        keywords_file: Path to keywords Excel file.

    Returns:
        Formatted keywords string sorted by volume (highest first).
    """
    if not keywords_file.exists():
        return "No keywords file provided."

    df = pd.read_excel(keywords_file)

    # Normalize column names: support "Keyword", "keyword", "Volume (CZ)", "Volume", etc.
    col_map: dict[str, str] = {}
    for col in df.columns:
        col_lower = str(col).lower().strip()
        if col_lower == "keyword":
            col_map["keyword"] = col
        elif "volume" in col_lower:
            col_map["volume"] = col
        elif col_lower == "kd":
            col_map["kd"] = col
        elif col_lower == "notes":
            col_map["notes"] = col

    kw_col = col_map.get("keyword")
    vol_col = col_map.get("volume")

    if kw_col is None:
        return "No 'Keyword' column found in keywords file."

    # Sort by volume descending (relative priority — no absolute thresholds)
    if vol_col:
        df = df.sort_values(by=vol_col, ascending=False, na_position="last")

    lines = ["# Target Keywords (sorted by volume, highest = top priority)\n"]
    for _, row in df.iterrows():
        keyword = row.get(kw_col, "")
        if not keyword or pd.isna(keyword):
            continue
        volume = row.get(vol_col, "") if vol_col else ""
        notes = row.get(col_map["notes"], "") if "notes" in col_map else ""

        line = f"- {keyword}"
        if volume and not pd.isna(volume):
            line += f" (vol: {int(volume) if str(volume).replace('.', '').isdigit() else volume})"
        if notes and not pd.isna(notes):
            line += f" | Note: {notes}"
        lines.append(line)

    return "\n".join(lines)


def sanitize_filename(name: str) -> str:
    """Convert string to safe filename."""
    return re.sub(r"[^\w\-]", "_", name.lower())


def _extract_log_section(text: str) -> str:
    """Extract the '## Step X Log:' section from AI step output."""
    match = re.search(r"\n(## Step \d+ Log:.*)", text, re.DOTALL)
    if not match:
        return ""
    return match.group(1).strip()


def _count_table_rows(section_text: str) -> int:
    """Count non-header data rows in the first markdown table within text."""
    count = 0
    header_skipped = False
    separator_skipped = False
    for line in section_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            if count > 0:
                break
            continue
        if not header_skipped:
            header_skipped = True
            continue
        if not separator_skipped and re.match(r"^[\|\s\-\:]+$", stripped):
            separator_skipped = True
            continue
        count += 1
    return count


def _build_editorial_log(
    title: str,
    source: str,
    date: str,
    slug: str,
    step1_out: str,
    step2_out: str,
    step3_out: str,
    tokens: dict[str, Any],
) -> str:
    """Compile step log sections into editorial _log.md for generate_log.py.

    Args:
        title: Article title (e.g. "SEO pro e-commerce").
        source: Source URL.
        date: Date string (YYYY-MM-DD).
        slug: URL slug used for article filename.
        step1_out: Full Step 1 AI output.
        step2_out: Full Step 2 AI output.
        step3_out: Full Step 3 AI output.
        tokens: Token usage dict with step1/step2/step3/total keys.

    Returns:
        Editorial log markdown string.
    """
    log1 = _extract_log_section(step1_out)
    log2 = _extract_log_section(step2_out)
    log3 = _extract_log_section(step3_out)

    rows1 = _count_table_rows(log1)
    rows2 = _count_table_rows(log2)
    rows3 = _count_table_rows(log3)

    article_file = f"article_{slug}_CZ.md"

    sections = [
        f"# {title} - Edit Log",
        "",
        f"**Article:** `{article_file}`",
        f"**Source:** {source}",
        f"**Date:** {date}",
        "",
        "---",
        "",
    ]

    if log1:
        sections += [log1, ""]
    if log2:
        sections += [log2, ""]
    if log3:
        sections += [log3, ""]

    sections += [
        "## Summary",
        "",
        "| Step | Status | Changes |",
        "|------|--------|---------|",
        f"| Step 1: Keywords | DONE | {rows1} keywords processed |",
        f"| Step 2: ToV Rewrite | DONE | {rows2} sentences changed |",
        f"| Step 3: Structure | DONE | {rows3} formatting changes |",
        "",
        "---",
        "",
        "## Token Usage",
        "",
        "| Step | Tokens |",
        "|------|--------|",
        f"| Step 1: Keywords | {tokens.get('step1', 'N/A')} |",
        f"| Step 2: ToV Rewrite | {tokens.get('step2', 'N/A')} |",
        f"| Step 3: Structure | {tokens.get('step3', 'N/A')} |",
        f"| **Total** | {tokens.get('total', 'N/A')} |",
        "",
    ]

    return "\n".join(sections)


def run_step(
    adapter: BaseAdapter,
    system_prompt: str,
    user_content: str,
    step_name: str,
    model_config: Any,
) -> tuple[str, ModelResponse]:
    """
    Run a single workflow step.

    Args:
        adapter: Model adapter to use.
        system_prompt: System instructions.
        user_content: Content to process.
        step_name: Name of the step for logging.
        model_config: Model configuration.

    Returns:
        Tuple of (output content, model response).
    """
    print(f"  Running {step_name}...")

    response = adapter.call(
        system_prompt=system_prompt,
        user_message=user_content,
        max_tokens=model_config.max_tokens,
        temperature=model_config.temperature,
    )

    print(f"    Tokens: {response.total_tokens} (in: {response.input_tokens}, out: {response.output_tokens})")

    return response.content, response


def confirm_step(next_step: str) -> bool:
    """
    Pause and ask user to confirm before proceeding to next step.

    Args:
        next_step: Name of the next step.

    Returns:
        True if user confirms, False to abort.
    """
    print(f"\n{'─' * 60}")
    answer = input(f"  Continue to {next_step}? [y/N] ").strip().lower()
    return answer in ("y", "yes")


def run_test(
    input_file: Path,
    keywords_file: Path | None,
    models: list[str],
    cfg: Config,
    auto: bool = False,
    slug: str | None = None,
    source_url: str = "",
) -> dict[str, dict[str, Any]]:
    """
    Run the full workflow test with multiple models.

    Args:
        input_file: Path to input content file.
        keywords_file: Path to keywords Excel file (optional).
        models: List of model names to test.
        cfg: Configuration object.
        auto: If True, skip step confirmations (run all steps automatically).
        slug: URL slug for output naming (from fetch_article).
        source_url: Original article URL for editorial log metadata.

    Returns:
        Dictionary mapping model names to their outputs.
    """
    # Load input content
    input_content = input_file.read_text(encoding="utf-8")
    print(f"Loaded input: {input_file.name} ({len(input_content)} chars)")

    # Load keywords
    keywords_str = ""
    if keywords_file and keywords_file.exists():
        keywords_str = load_keywords(keywords_file)
        print(f"Loaded keywords: {keywords_file.name}")

    # Load prompts
    prompts_dir = cfg.prompts_dir
    step1_prompt = load_prompt("step1_keywords", prompts_dir)
    step2_prompt = load_prompt("step2_tov", prompts_dir)
    step3_prompt = load_prompt("step3_structure", prompts_dir)

    results: dict[str, dict[str, Any]] = {}

    for model_name in models:
        print(f"\n{'=' * 60}")
        print(f"Model: {model_name}")
        print("=" * 60)

        try:
            adapter = get_adapter(model_name, cfg)
            model_config = cfg.models[model_name]
            article_slug = slug or sanitize_filename(input_file.stem)
            model_slug = sanitize_filename(model_name)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            date_str = datetime.now().strftime("%Y-%m-%d")
            step_dir = cfg.output_dir / f"{article_slug}_{model_slug}_{timestamp}"
            step_dir.mkdir(parents=True, exist_ok=True)

            # Step 1: Keywords
            step1_input = f"{input_content}\n\n---\n\n{keywords_str}"
            step1_output, step1_response = run_step(
                adapter, step1_prompt, step1_input, "Step 1: Keywords", model_config
            )
            step1_file = step_dir / "step1_keywords.md"
            step1_file.write_text(step1_output, encoding="utf-8")
            print(f"  Saved: {step1_file}")

            if not auto and not confirm_step("Step 2: ToV Rewrite"):
                print("  Stopped after Step 1.")
                results[model_name] = _partial_result(step1_output, "", "", step1_response)
                continue

            # Step 2: ToV Rewrite
            step2_output, step2_response = run_step(
                adapter, step2_prompt, step1_output, "Step 2: ToV Rewrite", model_config
            )
            step2_file = step_dir / "step2_tov.md"
            step2_file.write_text(step2_output, encoding="utf-8")
            print(f"  Saved: {step2_file}")

            if not auto and not confirm_step("Step 3: Structure & Formatting"):
                print("  Stopped after Step 2.")
                results[model_name] = _partial_result(step1_output, step2_output, "", step1_response, step2_response)
                continue

            # Step 3: Structure
            step3_output, step3_response = run_step(
                adapter, step3_prompt, step2_output, "Step 3: Structure", model_config
            )
            step3_file = step_dir / "step3_structure.md"
            step3_file.write_text(step3_output, encoding="utf-8")
            print(f"  Saved: {step3_file}")

            # Step 4: HTML Conversion (deterministic, no AI)
            print("  Running Step 4: HTML Conversion...")
            html_file = convert_to_html(step3_output, article_slug, step_dir)
            print(f"  Saved: {html_file}")

            # Calculate totals
            total_tokens = (
                step1_response.total_tokens
                + step2_response.total_tokens
                + step3_response.total_tokens
            )
            tokens_dict = {
                "step1": step1_response.total_tokens,
                "step2": step2_response.total_tokens,
                "step3": step3_response.total_tokens,
                "total": total_tokens,
            }

            # Step 4.5: Build and save editorial log for generate_log.py
            article_title = article_slug.replace("-", " ").replace("_", " ").title()
            editorial_log = _build_editorial_log(
                title=article_title,
                source=source_url,
                date=date_str,
                slug=article_slug,
                step1_out=step1_output,
                step2_out=step2_output,
                step3_out=step3_output,
                tokens=tokens_dict,
            )
            log_file = step_dir / f"article_{article_slug}_CZ_log.md"
            log_file.write_text(editorial_log, encoding="utf-8")
            print(f"  Saved: {log_file}")

            results[model_name] = {
                "step1": step1_output,
                "step2": step2_output,
                "step3": step3_output,
                "tokens": tokens_dict,
                "success": True,
                "error": None,
                "output_dir": str(step_dir),
                "log_file": str(log_file),
            }

            print(f"\n  Total tokens: {total_tokens}")
            print(f"  Output dir:   {step_dir}")

        except Exception as e:
            print(f"  ERROR: {e}")
            results[model_name] = {
                "step1": "",
                "step2": "",
                "step3": "",
                "tokens": {},
                "success": False,
                "error": str(e),
            }

    return results


def _partial_result(
    s1: str,
    s2: str,
    s3: str,
    r1: Any,
    r2: Any = None,
    r3: Any = None,
) -> dict[str, Any]:
    """Build a partial result dict when user stops early."""
    tokens: dict[str, Any] = {"step1": r1.total_tokens if r1 else 0}
    total = tokens["step1"]
    if r2:
        tokens["step2"] = r2.total_tokens
        total += r2.total_tokens
    if r3:
        tokens["step3"] = r3.total_tokens
        total += r3.total_tokens
    tokens["total"] = total
    return {"step1": s1, "step2": s2, "step3": s3, "tokens": tokens, "success": True, "error": None}


def save_outputs(
    results: dict[str, dict[str, Any]],
    article_name: str,
    output_dir: Path,
) -> None:
    """
    Save test outputs to files.

    Args:
        results: Dictionary of model results.
        article_name: Name of the article being tested.
        output_dir: Base output directory.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    slug = sanitize_filename(article_name)

    for model_name, data in results.items():
        if not data["success"]:
            continue

        model_slug = sanitize_filename(model_name)
        model_dir = output_dir / f"{slug}_{model_slug}_{timestamp}"
        model_dir.mkdir(parents=True, exist_ok=True)

        # Save step outputs
        (model_dir / "step1_keywords.md").write_text(data["step1"], encoding="utf-8")
        (model_dir / "step2_tov.md").write_text(data["step2"], encoding="utf-8")
        (model_dir / "step3_structure.md").write_text(data["step3"], encoding="utf-8")

        # Save log
        log_content = generate_log(model_name, data)
        (model_dir / "log.md").write_text(log_content, encoding="utf-8")

        print(f"Saved outputs: {model_dir}")


def generate_log(model_name: str, data: dict[str, Any]) -> str:
    """
    Generate a log file for the test run.

    Args:
        model_name: Name of the model.
        data: Test results data.

    Returns:
        Log content as string.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tokens = data.get("tokens", {})

    log = f"""# Test Log: {model_name}

**Timestamp:** {timestamp}
**Status:** {"Success" if data["success"] else "Failed"}

## Token Usage

| Step | Tokens |
|------|--------|
| Step 1: Keywords | {tokens.get("step1", "N/A")} |
| Step 2: ToV | {tokens.get("step2", "N/A")} |
| Step 3: Structure | {tokens.get("step3", "N/A")} |
| **Total** | {tokens.get("total", "N/A")} |

## Output Summary

### Step 1: Keywords
- Characters: {len(data.get("step1", ""))}

### Step 2: ToV Rewrite
- Characters: {len(data.get("step2", ""))}

### Step 3: Structure
- Characters: {len(data.get("step3", ""))}

"""

    if data.get("error"):
        log += f"\n## Error\n\n```\n{data['error']}\n```\n"

    return log


def main() -> None:
    """Main entry point for the model tester."""
    import argparse

    available_model_ids = list(config.models.keys())

    parser = argparse.ArgumentParser(
        description="evisions.cz blog content editor — runs Steps 1-3 via AI API.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"Available models: {', '.join(available_model_ids)}",
    )
    parser.add_argument(
        "--model",
        "-m",
        default="gpt-4o-mini",
        choices=available_model_ids,
        help="AI model to use (default: gpt-4o-mini)",
    )
    parser.add_argument(
        "--url",
        "-u",
        help="URL of evisions.cz blog article to fetch (e.g. https://www.evisions.cz/blog/[slug]/)",
    )
    parser.add_argument(
        "--input",
        "-i",
        default="data/raw/articles/example.md",
        help="Path to input article .md file (relative to project root, ignored if --url is set)",
    )
    parser.add_argument(
        "--keywords",
        "-k",
        default="data/output/keywords/example_keywords.xlsx",
        help="Path to keywords .xlsx file (relative to project root)",
    )
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Skip step confirmations and run all steps automatically",
    )
    args = parser.parse_args()

    # Resolve input: URL takes priority over --input file
    fetched_slug: str | None = None
    if args.url:
        article_content, fetched_slug = fetch_article(args.url)
        # Save fetched content to raw/articles for reference
        raw_dir = config.project_root / "data" / "raw" / "articles"
        raw_dir.mkdir(parents=True, exist_ok=True)
        raw_file = raw_dir / f"{fetched_slug}.md"
        raw_file.write_text(article_content, encoding="utf-8")
        print(f"Saved fetched article: {raw_file} ({len(article_content)} chars)")
        input_file = raw_file
    else:
        input_file = config.project_root / args.input

    # Auto-resolve keywords file if URL was given and no explicit --keywords
    if fetched_slug and args.keywords == "data/output/keywords/example_keywords.xlsx":
        kw_candidate = config.project_root / "data" / "output" / "keywords" / f"{fetched_slug}_keywords.xlsx"
        keywords_file = kw_candidate if kw_candidate.exists() else config.project_root / args.keywords
    else:
        keywords_file = config.project_root / args.keywords

    models = [args.model]

    # Validate API keys
    api_status = config.validate()
    print("API Key Status:")
    for provider, status in api_status.items():
        print(f"  {provider}: {'OK' if status else 'MISSING'}")

    # Filter models to those with valid API keys
    available_models = []
    for model in models:
        model_config = config.models.get(model)
        if model_config and api_status.get(model_config.provider):
            available_models.append(model)
        else:
            print(f"Skipping {model}: API key not configured")

    if not available_models:
        print("No models available. Check your .env file.")
        return

    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        return

    # Run tests
    results = run_test(
        input_file=input_file,
        keywords_file=keywords_file,
        models=available_models,
        cfg=config,
        auto=args.auto,
        slug=fetched_slug,
        source_url=args.url or "",
    )

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for model, data in results.items():
        status = "SUCCESS" if data["success"] else f"FAILED: {data['error']}"
        tokens = data.get("tokens", {}).get("total", "N/A")
        log_path = data.get("log_file", "")
        print(f"  {model}: {status} ({tokens} tokens)")
        if log_path:
            print(f"  Log: {log_path}")
            print(f"  Run: python src/generate_log.py {log_path}")


if __name__ == "__main__":
    main()
