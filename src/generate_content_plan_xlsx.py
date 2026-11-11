"""Generate an XLSX mirror of the evisions.cz Content Plan Google Sheet.

Reads data/output/content_plan_index.md (the AI-facing dedup ledger — source
of truth, edited by Claude during /evisions-new-article Krok 0 and Krok 7)
and renders it as data/output/content_plan_index.xlsx: one worksheet per
category, columns matching the primary Content Plan Index Sheet
(https://docs.google.com/spreadsheets/d/1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q/),
rows with Status "In Progress" highlighted so the user can see at a glance
what Claude has added/changed since the last time they synced that Sheet,
and copy those rows over manually (Google Drive MCP can only read the Sheet,
not write cells). The primary Sheet is itself a user-uploaded copy of an
earlier run of this script's output, so the two stay structurally identical.

Usage:
    python src/generate_content_plan_xlsx.py

Run this after any edit to content_plan_index.md (new ID assigned, Status
changed to Published, ledger refreshed from the Sheet, etc.) to keep the
xlsx mirror in sync.
"""

import re
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
LEDGER_MD = PROJECT_ROOT / "data" / "output" / "content_plan_index.md"
OUTPUT_XLSX = PROJECT_ROOT / "data" / "output" / "content_plan_index.xlsx"

SHEET_COLUMNS = [
    "Lokace",
    "Lekce",
    "Kapitola / Nadpis",
    "Obsah kapitoly - podtéma",
    "Typ obsahu",
    "zpracoval",
    "Článek/Case",
    "odhad práce",
    "klíčová slova",
    "brief",
    "složka s výstupy",
    "final docs",
    "log",
    "Status",
    "Počet",
]

HEADER_FONT = Font(bold=True, color="FFFFFF")
HEADER_FILL = PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid")
GROUP_FONT = Font(bold=True, italic=True)
GROUP_FILL = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
NEW_ROW_FILL = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
ANOMALY_FILL = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
BORDER = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)


def parse_next_id_table(text: str) -> list[dict]:
    section = re.search(
        r"## Next ID per kategorie.*?\n\n(.*?)\n\n>", text, re.S
    )
    rows = []
    if not section:
        return rows
    for line in section.group(1).splitlines():
        line = line.strip()
        if not line.startswith("|") or "---" in line or "Kategorie" in line:
            continue
        cells = [c.strip().strip("*") for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        name, prefix, last_used, next_id = cells[0], cells[1], cells[2], cells[3]
        rows.append(
            {
                "name": name,
                "prefix": prefix.replace("-XX", ""),
                "last_used": last_used,
                "next_id": next_id,
            }
        )
    return rows


def parse_existing_content(text: str) -> dict[str, list[dict]]:
    section = re.search(
        r"## Existující obsah \(Published\).*?\n(.*?)\n---\n\n## TODO", text, re.S
    )
    by_prefix: dict[str, list[dict]] = {}
    if not section:
        return by_prefix
    blocks = re.split(r"\n### ", section.group(1))
    for block in blocks[1:]:
        lines = block.splitlines()
        heading = lines[0].strip()
        for line in lines[1:]:
            line = line.strip()
            if not line.startswith("|") or "---" in line or line.startswith("| ID"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 4:
                continue
            article_id, title, skupina, status = cells[0], cells[1], cells[2], cells[3]
            url = cells[4] if len(cells) > 4 else ""
            prefix = article_id.split("-")[0] if "-" in article_id else heading
            by_prefix.setdefault(prefix, []).append(
                {
                    "id": article_id,
                    "title": title,
                    "skupina": skupina,
                    "status": status,
                    "typ_obsahu": "",
                    "url": url,
                }
            )
    return by_prefix


def parse_todo_topics(text: str) -> dict[str, list[dict]]:
    section = re.search(
        r"## TODO / plánovaná témata.*?\n(.*?)\n---\n\n## Lokální", text, re.S
    )
    by_prefix: dict[str, list[dict]] = {}
    if not section:
        return by_prefix
    blocks = re.split(r"\n### ", section.group(1))
    for block in blocks[1:]:
        lines = block.splitlines()
        heading = lines[0].strip()
        m = re.match(r"([A-Za-zÁ-Žá-ž& ]+?)\s*—\s*Skupina\s*\d+\s*\(([^)]*)\)", heading)
        if not m:
            continue
        prefix = m.group(1).strip()
        skupina_label = m.group(2).strip()
        for line in lines[1:]:
            line = line.strip()
            if not line.startswith("-") or line.startswith("*("):
                continue
            topic = line.lstrip("- ").strip()
            typ_obsahu = "nový text - lekce"
            tm = re.search(r"\(Typ:\s*([^)]+)\)", topic)
            if tm:
                typ_obsahu = tm.group(1).strip()
            url = ""
            um = re.search(r"(https?://\S+?)[`,)]", topic + " )")
            if um:
                url = um.group(1)
            by_prefix.setdefault(prefix, []).append(
                {
                    "id": "",
                    "title": topic,
                    "skupina": skupina_label,
                    "status": "",
                    "typ_obsahu": typ_obsahu,
                    "url": url,
                }
            )
    return by_prefix


INVALID_SHEET_CHARS = re.compile(r"[\\/*?:\[\]]")


def write_category_sheet(wb: Workbook, category: dict, rows: list[dict]) -> None:
    title = INVALID_SHEET_CHARS.sub("-", category["name"])[:31]
    ws = wb.create_sheet(title)

    for col, header in enumerate(SHEET_COLUMNS, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(horizontal="center", wrap_text=True)
        cell.border = BORDER

    r = 2
    current_skupina = None
    for row in rows:
        if row["skupina"] != current_skupina:
            current_skupina = row["skupina"]
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(SHEET_COLUMNS))
            gcell = ws.cell(row=r, column=1, value=f"Skupina {current_skupina}")
            gcell.font = GROUP_FONT
            gcell.fill = GROUP_FILL
            r += 1

        values = [
            "",  # Lokace — not tracked locally
            "",  # Lekce — not tracked locally
            row["id"],
            row["title"],
            row["typ_obsahu"],
            "",  # zpracoval — not tracked locally
            "",  # Článek/Case — not tracked locally
            "",  # odhad práce
            "",  # klíčová slova
            "",  # brief
            "",  # složka s výstupy
            row.get("url", ""),  # final docs (URL)
            "",  # log
            row["status"],
            "",  # Počet
        ]
        is_new = row["status"] == "In Progress"
        for col, value in enumerate(values, 1):
            cell = ws.cell(row=r, column=col, value=value)
            cell.border = BORDER
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            if is_new:
                cell.fill = NEW_ROW_FILL
        r += 1

    widths = [8, 8, 12, 50, 20, 16, 12, 10, 20, 16, 22, 30, 12, 14, 8]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width
    ws.freeze_panes = "A2"


def write_legend_sheet(wb: Workbook, next_id_rows: list[dict]) -> None:
    ws = wb.active
    ws.title = "Legenda"

    ws["A1"] = "Content Plan Index — mirror Google Sheetu"
    ws["A1"].font = Font(bold=True, size=14)

    ws["A3"] = (
        "Tento soubor je vygenerovaný z data/output/content_plan_index.md "
        "(lokální dedup ledger). Google Drive MCP umí Content Plan Sheet jen "
        "číst, ne zapisovat jednotlivé buňky — proto Claude ID a Status "
        "přiřazuje/aktualizuje tady, a vy zvýrazněné řádky ručně zkopírujete "
        "do skutečného Google Sheetu."
    )
    ws["A3"].alignment = Alignment(wrap_text=True)
    ws.row_dimensions[3].height = 60
    ws.merge_cells("A3:F3")

    ws["A5"] = "Barevné značení"
    ws["A5"].font = Font(bold=True)
    ws["A6"] = "Zelená"
    ws["A6"].fill = NEW_ROW_FILL
    ws["B6"] = "Status = 'In Progress' — nový/změněný řádek, zatím není v živém Google Sheetu. Zkopírujte ho tam."
    ws["B6"].alignment = Alignment(wrap_text=True)
    ws.merge_cells("B6:F6")

    ws["A8"] = "Poznámka"
    ws["A8"].font = Font(bold=True)
    ws["A9"] = (
        "Sloupce Lokace, Lekce, zpracoval, Článek/Case, odhad práce, klíčová "
        "slova, brief, složka s výstupy a log se lokálně netrackují pro "
        "existující (Published) řádky — pro plný přehled viz živý Google "
        "Sheet. Sloupec 'final docs' (URL) je doplněný. Tento mirror slouží "
        "primárně k vizuální kontrole nově přiřazených ID a stavů."
    )
    ws["A9"].alignment = Alignment(wrap_text=True)
    ws.row_dimensions[9].height = 60
    ws.merge_cells("A9:F9")

    ws["A11"] = "Next ID per kategorie"
    ws["A11"].font = Font(bold=True)
    headers = ["Kategorie", "Prefix", "Poslední použité", "Další volné ID"]
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=12, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.border = BORDER
    for i, row in enumerate(next_id_rows, 13):
        ws.cell(row=i, column=1, value=row["name"]).border = BORDER
        ws.cell(row=i, column=2, value=row["prefix"]).border = BORDER
        ws.cell(row=i, column=3, value=row["last_used"]).border = BORDER
        cell = ws.cell(row=i, column=4, value=row["next_id"])
        cell.border = BORDER
        cell.font = Font(bold=True)

    widths = [30, 34, 20, 18, 18, 18]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def main() -> None:
    text = LEDGER_MD.read_text(encoding="utf-8")
    next_id_rows = parse_next_id_table(text)
    existing_by_prefix = parse_existing_content(text)
    todo_by_prefix = parse_todo_topics(text)

    wb = Workbook()
    write_legend_sheet(wb, next_id_rows)

    for cat in next_id_rows:
        prefix = cat["prefix"]
        rows = list(existing_by_prefix.get(prefix, [])) + list(todo_by_prefix.get(prefix, []))
        if not rows:
            continue
        write_category_sheet(wb, cat, rows)

    OUTPUT_XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUTPUT_XLSX)
    print(f"Vygenerováno: {OUTPUT_XLSX}")


if __name__ == "__main__":
    main()
