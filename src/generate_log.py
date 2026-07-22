"""generate_log.py — Convert _log.md to _log.html and _log.pdf.

Usage:
    python src/generate_log.py data/output/articles/[slug]/article_[slug]_CZ_log.md
"""

import html
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import platform
import shutil

def _find_chrome() -> str:
    """Find Chrome executable across platforms."""
    if platform.system() == "Darwin":
        mac_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        if Path(mac_path).exists():
            return mac_path
    found = shutil.which("google-chrome") or shutil.which("chromium")
    if found:
        return found
    return "google-chrome"

CHROME = _find_chrome()

BADGE_CLASS: dict[str, str] = {
    "DONE": "badge-done",
    "SKIP": "badge-skip",
    "PENDING": "badge-pending",
    "NEW": "badge-new",
    "REJECTED": "badge-rejected",
}

STATUS_CLASS: dict[str, str] = {
    "DONE": "status-done",
    "PENDING": "status-pending",
    "SKIP": "status-pending",
    "NEW": "status-pending",
    "REJECTED": "status-pending",
}

# Reason tag prefixes → CSS class
_TAG_MAP: list[tuple[str, str]] = [
    ("ToV", "tag-tov"),
    ("E-E-A-T", "tag-tov"),
    ("KW", "tag-kw"),
    ("Navigation", "tag-kw"),
    ("SKIP", "tag-skip"),
    ("Structure", "tag-struct"),
    ("Struct", "tag-struct"),
]

CSS = """:root {
    --red-bg: #ffeef0;
    --red-text: #b91c1c;
    --red-border: #f87171;
    --green-bg: #f0fdf4;
    --green-text: #15803d;
    --green-border: #4ade80;
    --gray-bg: #f8f9fa;
    --border: #e1e5eb;
    --dark: #111827;
    --muted: #6b7280;
    --blue: #0781fe;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    font-size: 13px;
    line-height: 1.6;
    color: var(--dark);
    background: #fff;
    padding: 2rem;
    max-width: 1100px;
    margin: 0 auto;
}

.doc-header {
    border-bottom: 3px solid var(--dark);
    padding-bottom: 1rem;
    margin-bottom: 2rem;
}
.doc-header h1 {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}
.doc-meta {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 0.25rem 2rem;
    font-size: 0.8125rem;
    color: var(--muted);
}
.doc-meta span strong { color: var(--dark); }

.legend {
    display: flex;
    gap: 1.5rem;
    padding: 0.75rem 1rem;
    background: var(--gray-bg);
    border-radius: 6px;
    margin-bottom: 2rem;
    font-size: 0.8125rem;
    font-weight: 500;
}
.legend-item { display: flex; align-items: center; gap: 0.5rem; }
.legend-dot {
    width: 14px;
    height: 14px;
    border-radius: 3px;
    flex-shrink: 0;
}
.legend-dot-red { background: var(--red-bg); border: 1.5px solid var(--red-border); }
.legend-dot-green { background: var(--green-bg); border: 1.5px solid var(--green-border); }
.legend-dot-gray { background: #e5e7eb; border: 1.5px solid #9ca3af; }

.step-section {
    margin-bottom: 3rem;
    page-break-inside: avoid;
}
.step-header {
    display: flex;
    align-items: baseline;
    gap: 1rem;
    margin-bottom: 0.75rem;
}
.step-title {
    font-size: 1.125rem;
    font-weight: 700;
    color: var(--dark);
}
.step-meta {
    font-size: 0.8125rem;
    color: var(--muted);
}

.diff-table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid var(--border);
    border-radius: 6px;
    overflow: hidden;
    font-size: 0.8125rem;
}
.diff-table thead tr {
    background: var(--gray-bg);
    border-bottom: 1px solid var(--border);
}
.diff-table thead th {
    padding: 0.5rem 0.75rem;
    text-align: left;
    font-weight: 600;
    color: var(--muted);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}
.diff-table th:first-child { width: 28px; }
.diff-table th.col-orig { width: 34%; }
.diff-table th.col-new { width: 34%; }
.diff-table th.col-reason { width: auto; }

.diff-row { border-bottom: 1px solid var(--border); }
.diff-row:last-child { border-bottom: none; }
.diff-row td {
    padding: 0.625rem 0.75rem;
    vertical-align: top;
}
.diff-row td:first-child {
    text-align: center;
    color: var(--muted);
    font-weight: 600;
    font-size: 0.75rem;
    background: var(--gray-bg);
    border-right: 1px solid var(--border);
}

.cell-orig {
    background: var(--red-bg);
    border-right: 1px solid var(--border);
}
.cell-orig .text {
    color: var(--red-text);
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 0.8rem;
}
.cell-orig .text::before {
    content: "- ";
    font-weight: 700;
    opacity: 0.7;
}

.cell-new {
    background: var(--green-bg);
    border-right: 1px solid var(--border);
}
.cell-new .text {
    color: var(--green-text);
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 0.8rem;
}
.cell-new .text::before {
    content: "+ ";
    font-weight: 700;
    opacity: 0.7;
}

.cell-merged {
    background: #f3f4f6;
    border-right: 1px solid var(--border);
}
.cell-merged .text {
    color: var(--muted);
    font-style: italic;
    font-size: 0.8rem;
}

.cell-reason {
    color: var(--muted);
    font-size: 0.75rem;
}
.cell-reason .tag {
    display: inline-block;
    background: #e0e7ff;
    color: #3730a3;
    padding: 0.1rem 0.4rem;
    border-radius: 3px;
    font-size: 0.6875rem;
    font-weight: 600;
    margin-right: 0.25rem;
}
.cell-reason .tag-tov { background: #e0e7ff; color: #3730a3; }
.cell-reason .tag-kw { background: #dcfce7; color: #166534; }
.cell-reason .tag-skip { background: #fef9c3; color: #854d0e; }
.cell-reason .tag-struct { background: #fce7f3; color: #9d174d; }

.kw-table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid var(--border);
    border-radius: 6px;
    overflow: hidden;
    font-size: 0.8125rem;
}
.kw-table thead tr { background: var(--gray-bg); }
.kw-table thead th {
    padding: 0.5rem 0.75rem;
    text-align: left;
    font-weight: 600;
    color: var(--muted);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    border-bottom: 1px solid var(--border);
}
.kw-table td {
    padding: 0.5rem 0.75rem;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
}
.kw-table tr:last-child td { border-bottom: none; }
.kw-table .orig {
    color: var(--red-text);
    background: var(--red-bg);
    font-family: monospace;
    font-size: 0.775rem;
}
.kw-table .orig::before { content: "- "; font-weight: 700; opacity: 0.7; }
.kw-table .newv {
    color: var(--green-text);
    background: var(--green-bg);
    font-family: monospace;
    font-size: 0.775rem;
}
.kw-table .newv::before { content: "+ "; font-weight: 700; opacity: 0.7; }
.kw-table .skip-row td { opacity: 0.55; }

.badge {
    display: inline-block;
    padding: 0.1rem 0.4rem;
    border-radius: 3px;
    font-size: 0.6875rem;
    font-weight: 600;
}
.badge-done { background: #dcfce7; color: #166534; }
.badge-skip { background: #fef9c3; color: #854d0e; }
.badge-pending { background: #fed7aa; color: #9a3412; }
.badge-new { background: #dbeafe; color: #1e40af; }
.badge-rejected { background: #fee2e2; color: #991b1b; }
.vol { color: var(--muted); font-size: 0.75rem; }

.struct-table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid var(--border);
    font-size: 0.8125rem;
}
.struct-table thead tr { background: var(--gray-bg); }
.struct-table thead th {
    padding: 0.5rem 0.75rem;
    text-align: left;
    font-weight: 600;
    color: var(--muted);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    border-bottom: 1px solid var(--border);
}
.struct-table td {
    padding: 0.5rem 0.75rem;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
}
.struct-table tr:last-child td { border-bottom: none; }
.struct-table .added { color: var(--green-text); font-weight: 600; }

.summary-table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid var(--border);
    border-radius: 6px;
    overflow: hidden;
    font-size: 0.875rem;
}
.summary-table thead tr { background: var(--dark); }
.summary-table thead th {
    padding: 0.625rem 1rem;
    text-align: left;
    color: #fff;
    font-weight: 600;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.summary-table td {
    padding: 0.625rem 1rem;
    border-bottom: 1px solid var(--border);
}
.summary-table tr:last-child td { border-bottom: none; }
.status-done { color: var(--green-text); font-weight: 600; }
.status-pending { color: #b45309; font-weight: 600; }

@media print {
    body { padding: 1cm; font-size: 11px; }
    .step-section { page-break-inside: avoid; }
    .diff-table { page-break-inside: auto; }
    .diff-row { page-break-inside: avoid; }
}"""


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------


def _h(text: str) -> str:
    """HTML-escape a string."""
    return html.escape(str(text))


def _clean_cell(val: str) -> str:
    """Strip surrounding backticks or quotes from a cell value."""
    val = val.strip()
    if len(val) >= 2 and val[0] == "`" and val[-1] == "`":
        val = val[1:-1]
    if len(val) >= 2 and val[0] == '"' and val[-1] == '"':
        val = val[1:-1]
    return val


def _parse_md_table(lines: list[str]) -> tuple[list[str], list[list[str]]]:
    """Parse a markdown pipe table. Returns (headers, data_rows).

    Each data_row is a list of raw cell strings (not yet cleaned).
    """
    headers: list[str] = []
    rows: list[list[str]] = []

    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            break
        inner = stripped.strip("|")
        # Skip separator line: only dashes, colons, spaces, pipes
        if re.match(r"^[\s\-\:\|]+$", inner):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if not headers:
            headers = cells
        else:
            while len(cells) < len(headers):
                cells.append("")
            rows.append(cells)

    return headers, rows


def _get_status_key(status: str) -> str:
    """Extract the first word of a status field, e.g. 'DONE (approved)' → 'DONE'."""
    for key in BADGE_CLASS:
        if status.strip().upper().startswith(key):
            return key
    return status.strip().upper()


def _render_badge(status: str) -> str:
    """Render a coloured status badge."""
    key = _get_status_key(status)
    css = BADGE_CLASS.get(key, "badge-skip")
    return f'<span class="badge {css}">{_h(key)}</span>'


def _render_reason(reason: str) -> str:
    """Render a reason cell, promoting leading prefix to a coloured tag."""
    for tag_text, tag_cls in _TAG_MAP:
        if reason.startswith(f"{tag_text}:"):
            rest = _h(reason[len(tag_text) + 1:].strip())
            return f'<span class="tag {tag_cls}">{tag_text}</span> {rest}'
    return _h(reason)


# ---------------------------------------------------------------------------
# Log parser
# ---------------------------------------------------------------------------


def parse_log(path: Path) -> dict[str, Any]:
    """Parse a _log.md file into structured data dict."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    result: dict[str, Any] = {
        "title": "",
        "article": "",
        "source": "",
        "date": "",
        "steps": [],
        "summary_rows": [],
    }

    # Header metadata (first ~10 lines)
    for line in lines[:10]:
        if line.startswith("# ") and not result["title"]:
            result["title"] = line[2:].strip()
        elif "**Article:**" in line:
            result["article"] = line.split("**Article:**", 1)[1].strip().strip("`*")
        elif "**Source:**" in line:
            result["source"] = line.split("**Source:**", 1)[1].strip().strip("*")
        elif "**Date:**" in line:
            result["date"] = line.split("**Date:**", 1)[1].strip().strip("*")

    # Split by ## section headers
    sections: list[tuple[str, list[str]]] = []
    cur_name = ""
    cur_lines: list[str] = []
    for line in lines:
        if line.startswith("## "):
            if cur_name:
                sections.append((cur_name, cur_lines))
            cur_name = line[3:].strip()
            cur_lines = []
        elif cur_name:
            cur_lines.append(line)
    if cur_name:
        sections.append((cur_name, cur_lines))

    step_re = re.compile(r"^Step (\d+) Log:\s*(.+)$")

    for sec_name, sec_lines in sections:
        step_match = step_re.match(sec_name)
        if step_match:
            step_num = int(step_match.group(1))
            step_label = step_match.group(2).strip()
            _process_step(result, step_num, step_label, sec_lines)
        elif sec_name.strip() == "Summary":
            tbl = [l for l in sec_lines if l.strip().startswith("|")]
            _, rows = _parse_md_table(tbl)
            result["summary_rows"] = rows

    return result


def _process_step(
    result: dict[str, Any],
    step_num: int,
    step_label: str,
    lines: list[str],
) -> None:
    """Extract metadata, table rows, and post-table notes from a step section."""
    meta: dict[str, str] = {}
    table_start = 0

    for j, line in enumerate(lines):
        stripped = line.strip()
        # Bold metadata: **Key:** value
        if stripped.startswith("**") and ":**" in stripped:
            inner = stripped.strip("*")
            key, _, val = inner.partition(":**")
            meta[key.strip()] = val.strip().strip("*").strip()
        elif stripped.startswith("|"):
            table_start = j
            break

    table_lines = lines[table_start:]
    _, rows = _parse_md_table(table_lines)

    # Post-table notes (lines after the table block)
    post_notes: list[str] = []
    in_table = True
    for line in table_lines:
        if in_table and not line.strip().startswith("|"):
            in_table = False
        if not in_table and line.strip() and not line.strip().startswith("---"):
            post_notes.append(line.strip())

    result["steps"].append(
        {
            "num": step_num,
            "label": step_label,
            "meta": meta,
            "rows": rows,
            "post_notes": post_notes,
        }
    )


# ---------------------------------------------------------------------------
# Step renderers
# ---------------------------------------------------------------------------


def _render_step1(step: dict[str, Any]) -> str:
    """Step 1: Keyword Integration → kw-table."""
    rows = step["rows"]
    meta = step["meta"]

    # Expected columns: # | Original | Changed To | Keyword | Volume | Position | Status
    # Position (index 5) is omitted in HTML output
    C_NUM, C_ORIG, C_NEW, C_KW, C_VOL, _C_POS, C_STATUS = 0, 1, 2, 3, 4, 5, 6

    def _get(row: list[str], idx: int) -> str:
        return row[idx] if idx < len(row) else ""

    done_count = sum(
        1 for r in rows if _get_status_key(_get(r, C_STATUS)) == "DONE"
    )
    skip_count = sum(
        1 for r in rows if _get_status_key(_get(r, C_STATUS)) == "SKIP"
    )

    kw_file = meta.get("Keywords file", "")
    meta_parts: list[str] = []
    if kw_file:
        meta_parts.append(f"Keywords file: {_h(kw_file)}")
    meta_parts.append(f"{done_count} integrated")
    meta_parts.append(f"{skip_count} skipped")
    step_meta = " &nbsp;&middot;&nbsp; ".join(meta_parts)

    tbody_parts: list[str] = []
    for row in rows:
        while len(row) <= C_STATUS:
            row.append("")

        num = _get(row, C_NUM)
        orig = _clean_cell(_get(row, C_ORIG))
        new = _clean_cell(_get(row, C_NEW))
        kw = _get(row, C_KW)
        vol = _get(row, C_VOL)
        status = _get(row, C_STATUS)
        status_key = _get_status_key(status)

        if status_key == "SKIP":
            # SKIP: extract parenthetical reason from status
            paren = re.search(r"\((.+?)\)", status)
            skip_text = f"{kw} — {paren.group(1)}" if paren else kw
            tbody_parts.append(
                f'<tr class="skip-row">'
                f'<td style="color:var(--muted);text-align:center">{_h(num)}</td>'
                f'<td colspan="3" style="color:var(--muted);font-style:italic;font-size:0.775rem">{_h(skip_text)}</td>'
                f'<td class="vol">{_h(vol)}</td>'
                f"<td>{_render_badge(status)}</td>"
                f"</tr>"
            )
        else:
            is_no_change = (
                new in ("—", "")
                or "already" in new.lower()
                or "unchanged" in new.lower()
            )
            if is_no_change:
                display_text = new if new not in ("—", "") else "Already contains keyword — no change"
                new_td = (
                    f'<td style="color:var(--muted);font-style:italic;'
                    f'font-size:0.775rem;padding:0.5rem 0.75rem">{_h(display_text)}</td>'
                )
            else:
                new_td = f'<td><span class="newv">{_h(new)}</span></td>'

            orig_td = (
                f'<td><span class="orig">{_h(orig)}</span></td>'
                if orig not in ("—", "")
                else '<td style="color:var(--muted);font-style:italic;font-size:0.775rem;padding:0.5rem 0.75rem">—</td>'
            )

            tbody_parts.append(
                f"<tr>"
                f'<td style="color:var(--muted);text-align:center">{_h(num)}</td>'
                f"{orig_td}"
                f"{new_td}"
                f'<td style="font-size:0.75rem">{_h(kw)}</td>'
                f'<td class="vol">{_h(vol)}</td>'
                f"<td>{_render_badge(status)}</td>"
                f"</tr>"
            )

    # Post-table note: "Keywords already naturally present: ..."
    post_html = ""
    for note in step.get("post_notes", []):
        if "naturally present" in note.lower() or "already" in note.lower():
            clean = re.sub(r"\*+", "", note).strip()
            label, _, rest = clean.partition(":**")
            if not rest:
                label, _, rest = clean.partition(":")
            post_html = (
                f'<p style="margin-top:0.75rem;font-size:0.8125rem;color:var(--muted)">'
                f"<strong>{_h(label.strip())}:</strong> {_h(rest.strip())}</p>"
            )
            break

    tbody = "\n".join(tbody_parts)
    return f"""<!-- ===================== STEP 1 ===================== -->
<div class="step-section">
    <div class="step-header">
        <span class="step-title">Step 1 — Keyword Integration</span>
        <span class="step-meta">{step_meta}</span>
    </div>
    <table class="kw-table">
        <thead>
            <tr>
                <th style="width:24px">#</th>
                <th style="width:37%">Original sentence</th>
                <th style="width:37%">New sentence</th>
                <th style="width:12%">Keyword</th>
                <th style="width:6%">Vol.</th>
                <th style="width:5%">Status</th>
            </tr>
        </thead>
        <tbody>
{tbody}
        </tbody>
    </table>{post_html}
</div>"""


def _render_step2(step: dict[str, Any]) -> str:
    """Step 2: ToV Rewrite → diff-table."""
    rows = step["rows"]
    meta = step["meta"]
    classification = meta.get("Topic classification", "")

    meta_parts: list[str] = []
    if classification:
        meta_parts.append(f"Topic classification: {_h(classification)}")
    meta_parts.append(f"{len(rows)} changes")
    step_meta = " &nbsp;&middot;&nbsp; ".join(meta_parts)

    # Columns: # | Original (full) | New (full) | Reason
    tbody_parts: list[str] = []
    for row in rows:
        while len(row) < 4:
            row.append("")

        num = row[0]
        orig = _clean_cell(row[1])
        new = row[2].strip()
        reason = row[3]

        # Detect removed/merged: *(removed)* or lone dash or empty new
        is_removed = new in ("*(removed)*", "—", "") or re.match(r"^\*\(", new)

        if is_removed:
            label = "(removed)" if new in ("*(removed)*", "") else _h(new)
            new_td = f'<td class="cell-merged"><span class="text">{label}</span></td>'
        else:
            new_td = f'<td class="cell-new"><span class="text">{_h(_clean_cell(new))}</span></td>'

        tbody_parts.append(
            f'<tr class="diff-row">'
            f"<td>{_h(num)}</td>"
            f'<td class="cell-orig"><span class="text">{_h(orig)}</span></td>'
            f"{new_td}"
            f'<td class="cell-reason">{_render_reason(reason)}</td>'
            f"</tr>"
        )

    tbody = "\n".join(tbody_parts)
    return f"""<!-- ===================== STEP 2 ===================== -->
<div class="step-section">
    <div class="step-header">
        <span class="step-title">Step 2 — Tone of Voice Rewrite</span>
        <span class="step-meta">{step_meta}</span>
    </div>
    <table class="diff-table">
        <thead>
            <tr>
                <th>#</th>
                <th class="col-orig">Original sentence (full)</th>
                <th class="col-new">New sentence (full)</th>
                <th class="col-reason">Reason</th>
            </tr>
        </thead>
        <tbody>
{tbody}
        </tbody>
    </table>
</div>"""


def _render_step3(step: dict[str, Any]) -> str:
    """Step 3: Structure & Formatting → struct-table."""
    rows = step["rows"]
    meta = step["meta"]

    article_length = meta.get("Article length", "")
    step_meta = _h(article_length) if article_length else ""

    # Columns: # | Change Type | Description | Reason
    tbody_parts: list[str] = []
    for row in rows:
        while len(row) < 4:
            row.append("")
        num, change_type, desc, reason = row[0], row[1], row[2], row[3]
        tbody_parts.append(
            f"<tr>"
            f'<td style="color:var(--muted);text-align:center">{_h(num)}</td>'
            f'<td><span class="added">{_h(change_type)}</span></td>'
            f"<td>{_h(desc)}</td>"
            f'<td style="color:var(--muted);font-size:0.75rem">{_render_reason(reason)}</td>'
            f"</tr>"
        )

    tbody = "\n".join(tbody_parts)
    return f"""<!-- ===================== STEP 3 ===================== -->
<div class="step-section">
    <div class="step-header">
        <span class="step-title">Step 3 — Structure &amp; Formatting</span>
        <span class="step-meta">{step_meta}</span>
    </div>
    <table class="struct-table">
        <thead>
            <tr>
                <th style="width:24px">#</th>
                <th style="width:18%">Change Type</th>
                <th style="width:42%">Description</th>
                <th>Reason</th>
            </tr>
        </thead>
        <tbody>
{tbody}
        </tbody>
    </table>
</div>"""


def _render_step4(step: dict[str, Any]) -> str:
    """Step 4: HTML Conversion → element table."""
    rows = step["rows"]

    # Columns: # | Element | Description
    tbody_parts: list[str] = []
    for row in rows:
        while len(row) < 3:
            row.append("")
        num, element, desc = row[0], row[1], row[2]
        tbody_parts.append(
            f"<tr>"
            f'<td style="color:var(--muted);text-align:center">{_h(num)}</td>'
            f'<td style="font-weight:500">{_h(element)}</td>'
            f'<td style="color:var(--muted);font-size:0.75rem">{_h(desc)}</td>'
            f"</tr>"
        )

    tbody = "\n".join(tbody_parts)
    return f"""<!-- ===================== STEP 4 ===================== -->
<div class="step-section">
    <div class="step-header">
        <span class="step-title">Step 4 — HTML Conversion</span>
    </div>
    <table class="struct-table">
        <thead>
            <tr>
                <th style="width:24px">#</th>
                <th style="width:22%">Element</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
{tbody}
        </tbody>
    </table>
</div>"""


def _render_summary(rows: list[list[str]]) -> str:
    """Summary table."""
    # Columns: Step | Status | Key Changes (or Changes)
    tbody_parts: list[str] = []
    for row in rows:
        while len(row) < 3:
            row.append("")
        step_name, status, changes = row[0], row[1], row[2]
        status_key = _get_status_key(status)
        status_css = STATUS_CLASS.get(status_key, "status-pending")
        tbody_parts.append(
            f"<tr>"
            f"<td><strong>{_h(step_name)}</strong></td>"
            f'<td><span class="{status_css}">{_h(status_key)}</span></td>'
            f"<td>{_h(changes)}</td>"
            f"</tr>"
        )

    tbody = "\n".join(tbody_parts)
    return f"""<!-- ===================== SUMMARY ===================== -->
<div class="step-section">
    <div class="step-header">
        <span class="step-title">Summary</span>
    </div>
    <table class="summary-table">
        <thead>
            <tr>
                <th>Step</th>
                <th>Status</th>
                <th>Changes</th>
            </tr>
        </thead>
        <tbody>
{tbody}
        </tbody>
    </table>
</div>"""


# ---------------------------------------------------------------------------
# HTML assembly
# ---------------------------------------------------------------------------

_STEP_RENDERERS = {1: _render_step1, 2: _render_step2, 3: _render_step3, 4: _render_step4}


def generate_html(data: dict[str, Any]) -> str:
    """Assemble the full HTML log document."""
    title = data.get("title") or "Edit Log"
    article = data.get("article", "")
    source = data.get("source", "")
    date = data.get("date", "")

    steps_html = ""
    for step in sorted(data["steps"], key=lambda s: s["num"]):
        renderer = _STEP_RENDERERS.get(step["num"])
        if renderer:
            steps_html += "\n\n" + renderer(step)

    summary_html = ""
    if data["summary_rows"]:
        summary_html = "\n\n" + _render_summary(data["summary_rows"])

    return f"""<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Log &mdash; {_h(title)}</title>
    <style>
{CSS}
    </style>
</head>
<body>

<!-- Header -->
<div class="doc-header">
    <h1>Edit Log &mdash; {_h(title)}</h1>
    <div class="doc-meta">
        <span><strong>Article:</strong> {_h(article)}</span>
        <span><strong>Source:</strong> {_h(source)}</span>
        <span><strong>Date:</strong> {_h(date)}</span>
    </div>
</div>

<!-- Legend -->
<div class="legend">
    <div class="legend-item">
        <div class="legend-dot legend-dot-red"></div>
        <span>Original sentence (removed / changed)</span>
    </div>
    <div class="legend-item">
        <div class="legend-dot legend-dot-green"></div>
        <span>New sentence (replacement)</span>
    </div>
    <div class="legend-item">
        <div class="legend-dot legend-dot-gray"></div>
        <span>Merged into another row / skipped</span>
    </div>
</div>
{steps_html}
{summary_html}

</body>
</html>"""


# ---------------------------------------------------------------------------
# PDF export
# ---------------------------------------------------------------------------


def export_pdf(html_path: Path, pdf_path: Path) -> None:
    """Export HTML to PDF via Chrome headless."""
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path.resolve()}",
        "--print-to-pdf-no-header",
        f"file://{html_path.resolve()}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        raise RuntimeError(
            f"Chrome exited with code {result.returncode}:\n{result.stderr}"
        )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python src/generate_log.py <path/to/_log.md>")
        sys.exit(1)

    md_path = Path(sys.argv[1]).resolve()
    if not md_path.exists():
        print(f"Error: file not found: {md_path}")
        sys.exit(1)
    if not md_path.name.endswith("_log.md"):
        print(f"Warning: expected a *_log.md file, got: {md_path.name}")

    html_path = md_path.with_suffix(".html")
    pdf_path = md_path.with_suffix(".pdf")

    print(f"Parsing: {md_path}")
    data = parse_log(md_path)

    print(f"Generating HTML: {html_path}")
    html_content = generate_html(data)
    html_path.write_text(html_content, encoding="utf-8")

    print(f"Exporting PDF:   {pdf_path}")
    try:
        export_pdf(html_path, pdf_path)
        print("Done.")
    except FileNotFoundError:
        print(f"Chrome not found at: {CHROME}")
        print("HTML saved. Install Chrome or update CHROME path to export PDF.")
    except RuntimeError as exc:
        print(f"PDF export failed: {exc}")
        print("HTML saved successfully.")


if __name__ == "__main__":
    main()
