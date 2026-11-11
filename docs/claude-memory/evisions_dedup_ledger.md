---
name: evisions-dedup-ledger
description: /evisions-new-article uses a local dedup ledger (data/output/content_plan_index.md) + manual paste-back to the Sheet, not direct Sheet writes
metadata:
  type: feedback
  originSessionId: 4db7a601-a7eb-4368-8d80-eb78f8cee1e5
  modified: 2026-08-18T14:48:43.118Z
---

`/evisions-new-article` now runs a mandatory "Krok 0 — Duplicate Check & ID přiřazení" before INIT: it reads `data/output/content_plan_index.md` (a local ledger synced from the Content Plan Sheet — [[evisions_content_plan_sheet_discrepancy]]) to check whether the requested topic/keyword already exists (Published or already a TODO row) before writing anything, and to assign the next free ID per category prefix (e.g. next SEO ID, next PPC ID...).

`/evisions-rewrite-article` also consults the ledger at INIT (added 2026-08-18 after the user asked whether this applied to rewrite too) — it looks up the target URL to recover its existing ID/category, and if the ledger doesn't know that URL yet (an older Published article never indexed), it looks the ID up in the Sheet by URL and backfills the ledger row. This keeps the ledger a complete map of all content, not just what was created through `/evisions-new-article`.

**Why:** the user explicitly asked (2026-08-18) to prevent duplicate article creation and wanted new articles to get an ID it can recognize later. Since Google Drive MCP can only *read* the Sheet (confirmed constraint, not re-tested), the user chose — via AskUserQuestion, picking the recommended option over "try direct Sheet writes" — a local ledger as the source of truth plus an explicit copy-paste block for the user to manually add to the real Google Sheet, rather than risking an experimental direct write to a live shared document.

**How to apply:** Any future work on `/evisions-new-article` (or a new dedup-adjacent skill) should keep this pattern: local ledger is authoritative for dedup + ID assignment, real Sheet updates stay manual via an explicit "vlož ručně do Sheetu" block at INIT and at Krok 7. Don't attempt `mcp__claude_ai_Google_Drive__update_file` on the Content Plan Sheet without asking the user first — confirmed 2026-08-18 that this tool only supports renaming/moving a file, not editing cell content, so it's not a viable path anyway. Full process lives in `data/output/guides/evisions_write_workflow_CZ.md` (Krok 0 + Krok 7) and `CLAUDE.md`.

**URL column (added 2026-08-18):** the user asked to add each article's live URL to the ledger rows. Added a 5th column (URL) to every per-category "Existující obsah" table in `content_plan_index.md`, populated from the full Sheet read done earlier in the session. Updated the parser/generator in `generate_content_plan_xlsx.py` to carry that URL into the xlsx's "final docs" column. One orphan row (a URL in the Copywriting Sheet tab with no ID/title) is flagged as an anomaly rather than guessed at.

**xlsx visual mirror (added 2026-08-18):** the user asked for a concrete Excel file mirroring the Sheet that Claude edits and the user then copies into Google Sheets by hand. Built `src/generate_content_plan_xlsx.py` — parses the MD ledger (regex, tailored to its exact section structure) and writes `data/output/content_plan_index.xlsx`: one worksheet per category (columns matching the real Sheet), rows grouped by Skupina, and any row with Status "In Progress" highlighted green so new/changed rows are obvious at a glance. Regenerate it (`.venv/Scripts/python.exe src/generate_content_plan_xlsx.py`) every time the ledger changes — wired into write workflow Krok 0 and Krok 7. Note: the xlsx only carries the fields the ledger tracks (ID, title, Skupina, Status) — Lokace/Lekce/zpracoval/URL/klíčová slova etc. are blank for pre-existing Published rows since the ledger never stored them; that's documented in the xlsx's own "Legenda" tab, not a bug.
