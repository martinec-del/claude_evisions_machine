# evisions.cz Blog — New Article

Arguments: $ARGUMENTS

## Reference Documents

**Workflow:** `data/output/guides/evisions_write_workflow_CZ.md`
**ToV Guide:** `data/output/guides/evisions_tov_guide_CZ.md`
**Structure Guide:** `data/output/guides/evisions_structure_guide_CZ.md`
**Content Inventory:** `data/output/guides/evisions_content_inventory.md` (use ONLY for internal linking decisions in Krok 2 and Krok 7 — NOT for task management)
**HTML template script:** `src/step4_html.py`
**Keywords template script:** `src/create_keyword_xlsx.py`
**Generator script (optional external LLM):** `src/model_tester.py`

> **Default:** Claude Code writes the draft directly (Krok 3). If the user wants an external LLM instead, offer a model picker (AskUserQuestion) before Krok 3 and run `.venv/bin/python src/model_tester.py --model [key] ...`.

### Content Plan — Google Sheet (primary source for topic/category)

**Sheet:** [evisions.cz - Content Plan](https://docs.google.com/spreadsheets/d/1W8VTbwT8_HiYuEF62rgJzI6KRTKJ9neI7LU4vt4IC74/edit)
**File ID:** `1W8VTbwT8_HiYuEF62rgJzI6KRTKJ9neI7LU4vt4IC74`
**Read via:** `mcp__claude_ai_Google_Drive__read_file_content` (already authenticated as analytics@evisions.cz — no service account needed)

**Columns:** ID | Kategorie | Téma / pracovní název | Klíčové slovo | Search Volume | Typ obsahu | Status | URL | Poznámky

**How to resolve a row:** Read the Sheet via the Drive MCP tool, parse the markdown table, match the user's input against column A (ID) or column C (Téma). If ambiguous (multiple topic matches), ask the user for the exact ID.

## Prompts

| Krok | Prompt file |
|------|-------------|
| Krok 1 — Konkurenční research + Klíčová slova | `prompts/write_step1_research.md` |
| Krok 2 — Brief & osnova | `prompts/write_step2_brief.md` |
| Krok 3 — Draft | `prompts/write_step3_draft.md` |
| Krok 4 — ToV kontrola | `prompts/write_step4_tov_check.md` |
| Krok 5 — Struktura & formátování | `prompts/step3_structure.md` |
| Krok 6 — HTML | `prompts/step4_html.md` |

## Entry Point

When skill is invoked, determine mode:

### A) Arguments provided → parse mode

- **ID z Content Plan** (e.g. `SEO-04`) → lookup in Sheet, NEW article, go to INIT
- **Téma bez ID** (e.g. `"SEO pro e-commerce"`) → lookup in Sheet by name (warn if ambiguous or not found — proceed anyway as new, ask user to assign Kategorie + Klíčové slovo)
- **`continue` + slug/folder path** → CONTINUE mode, go to INIT with auto-detection (see workflow guide section 5)

### B) No arguments — interactive menu

```
evisions.cz Blog — New Article

Dostupné módy:
  1. Nový článek (zadejte ID z Content Plan nebo téma)
  2. Pokračovat v rozpracovaném článku (zadejte slug nebo cestu)
```

Wait for user input. Do NOT read reference documents or start workflow until input is given.

## Workflow

Follow `data/output/guides/evisions_write_workflow_CZ.md` exactly — INIT, then Kroky 1–7, each ending with an explicit STOP for user confirmation (see workflow guide section 15 — step confirmation is mandatory, never skip).

**Mandatory first action in Krok 5 (Struktura):** paragraph audit — see workflow guide section 10 / structure guide section 4. Split every paragraph over 100 words before any callouts, tables, or H3s.

**Log integrity:** every "Original" cell in every log table must be copied verbatim from the current file — never reconstructed from memory (workflow guide section 13).

## Usage

```
/evisions-new-article SEO-04
/evisions-new-article "SEO pro e-commerce"
/evisions-new-article continue seo-pro-e-commerce
/evisions-new-article
```
