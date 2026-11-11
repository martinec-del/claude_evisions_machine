"""generate_write_log.py — Convert a New Article workflow _log.md to styled _log.html.

The New Article workflow (/evisions-new-article) uses a different log structure
(## Step N — Name, free-form prose + tables) than the Edit workflow's log
(generate_log.py, which expects "Step N Log:" sections with fixed table schemas
per step). This is a generic Markdown -> styled HTML renderer for that format:
it converts the whole log file with the `markdown` library (tables extension)
and wraps the result in a simple branded template.

Usage:
    python src/generate_write_log.py data/output/articles/[slug]/article_[slug]_CZ_log.md
"""

import sys
from pathlib import Path

import markdown

CSS = """
:root {
    --dark: #12131a; --muted: #6b7280; --border: #e1e5eb;
    --accent: #0057ff; --light: #f8f9fa;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    font-size: 14px; line-height: 1.65; color: #1f2937; background: #fff;
    max-width: 1000px; margin: 0 auto; padding: 2.5rem 2rem;
}
h1 { font-size: 1.5rem; font-weight: 700; color: var(--dark);
    border-bottom: 3px solid var(--dark); padding-bottom: 0.75rem; margin-bottom: 1.5rem; }
h2 { font-size: 1.15rem; font-weight: 700; color: var(--dark);
    margin: 2.25rem 0 0.75rem; padding-top: 1rem; border-top: 1px solid var(--border); }
h3 { font-size: 1rem; font-weight: 600; color: var(--dark); margin: 1.25rem 0 0.5rem; }
p { margin-bottom: 0.85rem; color: #374151; }
strong { color: var(--dark); }
ul, ol { margin: 0.5rem 0 1rem 1.5rem; color: #374151; }
li { margin-bottom: 0.3rem; }
table { width: 100%; border-collapse: collapse; margin: 1rem 0 1.5rem; font-size: 0.8125rem; }
th, td { padding: 0.5rem 0.75rem; text-align: left; border: 1px solid var(--border); vertical-align: top; }
th { background: var(--light); font-weight: 600; color: var(--dark); }
td { color: #374151; }
code { background: var(--light); padding: 0.1rem 0.35rem; border-radius: 3px; font-size: 0.85em; }
blockquote { border-left: 4px solid var(--accent); background: var(--light);
    padding: 0.75rem 1rem; margin: 1rem 0; color: #374151; }
a { color: var(--accent); }
hr { border: none; border-top: 1px solid var(--border); margin: 2rem 0; }
"""


def convert_log_to_html(log_md_path: Path) -> Path:
    """Convert a write-workflow _log.md file to a styled _log.html next to it."""
    text = log_md_path.read_text(encoding="utf-8")

    title_line = next((l for l in text.splitlines() if l.startswith("# ")), "")
    title = title_line[2:].strip() if title_line else log_md_path.stem

    body_html = markdown.Markdown(
        extensions=["tables", "fenced_code", "nl2br"],
        output_format="html",
    ).convert(text)

    html = f"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
{body_html}
</body>
</html>"""

    html_path = log_md_path.with_suffix(".html")
    html_path.write_text(html, encoding="utf-8")
    return html_path


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python src/generate_write_log.py <path/to/_log.md>")
        sys.exit(1)

    md_path = Path(sys.argv[1]).resolve()
    if not md_path.exists():
        print(f"Error: file not found: {md_path}")
        sys.exit(1)

    html_path = convert_log_to_html(md_path)
    print(f"Generated: {html_path}")


if __name__ == "__main__":
    main()
