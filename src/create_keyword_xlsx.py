"""Create a keyword research XLSX template for an evisions.cz blog article.

Usage:
    python src/create_keyword_xlsx.py [slug]

Produces data/output/keywords/[slug]_keywords.xlsx with two sheets:
  - Keywords: target keyword, volume, KD, priority, section, internal link, notes
  - Competitors: competitor URL, domain, keywords covered, unique angle, takeaway

Fill in rows manually (or via Ahrefs export) before running /evisions-new-article
or /evisions-rewrite-article — the skills read this file in Step 1.
"""

import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter


def create_keywords_xlsx(output_path: str) -> None:
    """Create an empty keyword research XLSX template."""
    wb = Workbook()

    # Sheet 1: Keywords
    ws1 = wb.active
    ws1.title = "Keywords"

    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid")
    border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin"),
    )

    headers1 = [
        "Keyword",
        "Volume (CZ)",
        "KD",
        "Priority",
        "Section to Add/Expand",
        "Internal Link To",
        "Notes",
    ]

    for col, header in enumerate(headers1, 1):
        cell = ws1.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center")
        cell.border = border

    # Example placeholder row — replace with real Ahrefs data before use
    example_row = (
        "priklad klicoveho slova",
        0,
        0,
        "HIGH",
        "Doplnit sekci / rozsirit H2",
        "-",
        "Nahradit realnymi daty z Ahrefs pred spustenim workflow",
    )
    for col, value in enumerate(example_row, 1):
        cell = ws1.cell(row=2, column=col, value=value)
        cell.border = border

    col_widths1 = [30, 12, 6, 10, 40, 25, 40]
    for i, width in enumerate(col_widths1, 1):
        ws1.column_dimensions[get_column_letter(i)].width = width

    # Sheet 2: Competitors
    ws2 = wb.create_sheet("Competitors")

    headers2 = [
        "Competitor URL",
        "Domain",
        "Main Keywords Covered",
        "Unique Angles",
        "What evisions.cz Can Learn",
    ]

    for col, header in enumerate(headers2, 1):
        cell = ws2.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", wrap_text=True)
        cell.border = border

    col_widths2 = [60, 15, 45, 40, 45]
    for i, width in enumerate(col_widths2, 1):
        ws2.column_dimensions[get_column_letter(i)].width = width

    wb.save(output_path)
    print(f"Created: {output_path}")


if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "novy-clanek"
    project_root = Path(__file__).parent.parent.resolve()
    out_dir = project_root / "data" / "output" / "keywords"
    out_dir.mkdir(parents=True, exist_ok=True)
    output = str(out_dir / f"{slug}_keywords.xlsx")
    create_keywords_xlsx(output)
