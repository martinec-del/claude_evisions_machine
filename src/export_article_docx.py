"""Export a finished article markdown (Step 3/5 output) to a readable .docx.

Unlike src/step4_html.py (which wraps the article in the full evisions.cz blog
page template — header, nav, footer, ToC, CSS), this produces a clean Word
document with just the article content: headings, paragraphs, bold text,
clickable hyperlinks, tables, bullet lists, and callouts. Intended as a
review/handoff copy for people who don't want to open raw HTML.

Runs automatically at the end of Krok 6 (HTML konverze) in both the write
workflow (write_step4_html.md) and rewrite workflow (step4_html.md), right
after convert_to_html(), so every article gets a .docx alongside its .html
without a separate manual step.

Usage:
    python src/export_article_docx.py data/output/articles/[slug]/article_[slug]_CZ.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

# evisions brand colors (placeholder — swap once real brand palette is known,
# same values as src/step4_html.py CSS and src/export_outline_docx.py)
EVI_DARK = RGBColor(0x12, 0x13, 0x1A)
EVI_ACCENT = RGBColor(0x00, 0x57, 0xFF)
EVI_BODY = RGBColor(0x1A, 0x1A, 0x2E)

CALLOUT_RE = re.compile(
    r"^>\s*\*\*(Tip|Warning|Important|Note|Keep in Mind|Example)\s*:\*\*\s*(.+)$",
    re.IGNORECASE,
)
LINK_OR_BOLD_RE = re.compile(r"(\[[^\]]+\]\([^)]+\)|\*\*[^*]+\*\*)")


def _strip_log(markdown_text: str) -> str:
    """Remove an appended Step-log section, if present (mirrors step4_html.py)."""
    parts = re.split(r"\n---\n+## Step \d+ Log:", markdown_text)
    return parts[0].strip()


def _create_document() -> Document:
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    style.font.color.rgb = EVI_BODY
    style.paragraph_format.space_after = Pt(8)
    style.paragraph_format.line_spacing = 1.25

    sizes = {1: 24, 2: 17, 3: 13}
    for level, size in sizes.items():
        hstyle = doc.styles[f"Heading {level}"]
        hstyle.font.name = "Calibri"
        hstyle.font.color.rgb = EVI_DARK
        hstyle.font.size = Pt(size)
        hstyle.font.bold = True
        hstyle.paragraph_format.space_before = Pt(18 if level == 2 else 12)
        hstyle.paragraph_format.space_after = Pt(8)
    return doc


def _add_hyperlink(paragraph, url: str, text: str) -> None:
    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)

    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0057FF")
    rpr.append(color)
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    rpr.append(underline)
    run.append(rpr)

    text_el = OxmlElement("w:t")
    text_el.text = text
    run.append(text_el)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)


def _add_runs(paragraph, text: str) -> None:
    """Split text on **bold** and [text](url) markdown, add runs/hyperlinks."""
    for part in LINK_OR_BOLD_RE.split(text):
        if not part:
            continue
        link_match = re.match(r"^\[([^\]]+)\]\(([^)]+)\)$", part)
        if link_match:
            _add_hyperlink(paragraph, link_match.group(2), link_match.group(1))
            continue
        bold_match = re.match(r"^\*\*([^*]+)\*\*$", part)
        if bold_match:
            run = paragraph.add_run(bold_match.group(1))
            run.bold = True
            continue
        paragraph.add_run(part)


def _clean_heading_text(text: str) -> str:
    """Strip markdown bold/link syntax from a heading (Word heading styles are already bold)."""
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


def _add_callout(doc: Document, label: str, text: str) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(10)
    run_label = p.add_run(f"{label.title()}: ")
    run_label.bold = True
    run_label.font.color.rgb = EVI_ACCENT
    _add_runs(p, text)


def _parse_table_line(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _add_table(doc: Document, table_lines: list[str]) -> None:
    rows = [
        _parse_table_line(line)
        for line in table_lines
        if not re.match(r"^\|[\s:-]+\|$", line.replace(" ", ""))
    ]
    if not rows:
        return
    num_cols = len(rows[0])
    table = doc.add_table(rows=len(rows), cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.style = "Table Grid"
    for i, row_data in enumerate(rows):
        row = table.rows[i]
        for j, cell_text in enumerate(row_data):
            if j >= num_cols:
                break
            cell = row.cells[j]
            cell.text = ""
            p = cell.paragraphs[0]
            if i == 0:
                run = p.add_run(re.sub(r"\*\*|\[|\]\([^)]*\)", "", cell_text))
                run.bold = True
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                shd = OxmlElement("w:shd")
                shd.set(qn("w:val"), "clear")
                shd.set(qn("w:color"), "auto")
                shd.set(qn("w:fill"), "12131A")
                cell._element.get_or_add_tcPr().append(shd)
            else:
                _add_runs(p, cell_text)
    doc.add_paragraph()


def convert_to_docx(markdown_text: str, slug: str, output_path: Path) -> Path:
    """Convert final article markdown to a clean, readable .docx.

    Args:
        markdown_text: Full content of article_[slug]_CZ.md (log, if embedded, is stripped).
        slug: URL slug used for the output filename.
        output_path: Directory where the .docx file will be saved.

    Returns:
        Path to the generated .docx file.
    """
    article_md = _strip_log(markdown_text)
    lines = article_md.split("\n")
    doc = _create_document()

    i = 0
    table_buffer: list[str] = []
    in_table = False

    while i < len(lines):
        stripped = lines[i].strip()

        if in_table and not stripped.startswith("|"):
            _add_table(doc, table_buffer)
            table_buffer = []
            in_table = False

        if stripped.startswith("|"):
            in_table = True
            table_buffer.append(stripped)
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        if stripped == "---":
            i += 1
            continue

        if stripped.startswith("### "):
            doc.add_heading(_clean_heading_text(stripped[4:]), level=3)
        elif stripped.startswith("## "):
            doc.add_heading(_clean_heading_text(stripped[3:]), level=2)
        elif stripped.startswith("# "):
            doc.add_heading(_clean_heading_text(stripped[2:]), level=1)
        else:
            callout_match = CALLOUT_RE.match(stripped)
            if callout_match:
                _add_callout(doc, callout_match.group(1), callout_match.group(2))
            elif stripped.startswith("- "):
                p = doc.add_paragraph(style="List Bullet")
                _add_runs(p, stripped[2:])
            else:
                p = doc.add_paragraph()
                _add_runs(p, stripped)
        i += 1

    if table_buffer:
        _add_table(doc, table_buffer)

    output_path.mkdir(parents=True, exist_ok=True)
    docx_file = output_path / f"article_{slug}_CZ.docx"
    doc.save(str(docx_file))
    return docx_file


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python src/export_article_docx.py <path/to/article_[slug]_CZ.md>")
        sys.exit(1)

    md_path = Path(sys.argv[1]).resolve()
    if not md_path.exists():
        print(f"Error: file not found: {md_path}")
        sys.exit(1)

    # slug derived from filename: article_[slug]_CZ.md
    stem = md_path.stem  # article_[slug]_CZ
    slug = re.sub(r"^article_", "", stem)
    slug = re.sub(r"_CZ(_v\d+)?$", "", slug)

    markdown_text = md_path.read_text(encoding="utf-8")
    docx_file = convert_to_docx(markdown_text, slug, md_path.parent)
    print(f"Generated: {docx_file}")


if __name__ == "__main__":
    main()
