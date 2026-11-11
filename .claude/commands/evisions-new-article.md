# evisions.cz Blog — New Article

Arguments: $ARGUMENTS

## Reference Documents

**Workflow:** `data/output/guides/evisions_write_workflow_CZ.md`
**ToV Guide:** `data/output/guides/evisions_tov_guide_CZ.md`
**Structure Guide:** `data/output/guides/evisions_structure_guide_CZ.md`
**Content Inventory:** `data/output/guides/evisions_content_inventory.md` (use ONLY for internal linking decisions in Krok 2 and Krok 7 — NOT for task management)
**Content Plan Index (dedup ledger):** `data/output/content_plan_index.md` — read FIRST, before anything else, for the mandatory Duplicate Check & ID assignment (workflow guide Krok 0). Source of truth for "does this topic already exist" and "what's the next free ID", since the Drive MCP can only read the Sheet, not write to it.
**Content Plan Index (xlsx mirror):** `data/output/content_plan_index.xlsx`, generated from the ledger via `src/generate_content_plan_xlsx.py`. Regenerate it (`.venv/Scripts/python.exe src/generate_content_plan_xlsx.py`) any time the ledger changes (Krok 0 ID assignment, Krok 7 Published) so the user has a visual, Sheet-shaped file with new/changed rows highlighted green to copy into the real Google Sheet.
**HTML template script:** `src/step4_html.py`
**Docx export script (automatický, hned po HTML):** `src/export_article_docx.py` — generuje čitelný Word export finálního článku vedle `.html`/`_log.html`, viz `prompts/step4_html.md` sekce "Docx export".
**Keywords template script:** `src/create_keyword_xlsx.py`
**Marketing Miner cross-check script (optional, Krok 1):** `src/marketing_miner_api.py` — CZ/SK volume cross-check + supplementary keyword ideas, see `prompts/write_step1_research.md` krok 5.5. Skip silently if `MARKETING_MINER_API_KEY` is unset.
**Generator script (optional external LLM):** `src/model_tester.py`

> **Default:** Claude Code writes the draft directly (Krok 3). If the user wants an external LLM instead, offer a model picker (AskUserQuestion) before Krok 3 and run `.venv/bin/python src/model_tester.py --model [key] ...`.

### Content Plan — Google Sheet (primary source for topic/category)

**Primary Sheet:** [Content Plan Index Sheet](https://docs.google.com/spreadsheets/d/1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q/edit?gid=754600260#gid=754600260) — file ID `1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q`. The user's editable copy of `content_plan_index.xlsx` uploaded to Drive — same structure as the ledger/xlsx (one tab per category).
**Secondary Sheet (only if the user asks):** the original "evisions.cz - Content Plan", file ID `1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY` — richer historical data (Lokace, zpracoval, klíčová slova, brief) not yet carried over.
**Read via:** `mcp__claude_ai_Google_Drive__read_file_content` (already authenticated as analytics@evisions.cz — no service account needed)

**Structure:** editorial-calendar format — separate per-category tables (SEO, PPC, Social, AI & SEO, Copywriting, Konference, Marketing, evisions interní, International, Kariéra), each with its own ID prefix (SEO-XX, PPC-XX, SOC-XX, AI-XX, CW-XX, CONF-XX, MKT-XX, EVI-XX, INTL-XX, CAR-XX), grouped into "Skupina" subgroups (tag `topic_cluster_[slug]_CZ`).

**Columns:** Lokace | Lekce | Kapitola/Nadpis | Obsah kapitoly | Typ obsahu | zpracoval | Článek/Case | odhad práce | klíčová slova | brief | složka s výstupy | final docs | log | Status | Počet

**How to resolve a row:** Read the Sheet via the Drive MCP tool, parse the tables, match the user's input against the ID prefix or Kapitola/Nadpis. A row with empty ID + "nový text - lekce" in Typ obsahu is TODO/planned. If ambiguous (multiple topic matches), ask the user for the exact ID.

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

Follow `data/output/guides/evisions_write_workflow_CZ.md` exactly — **Krok 0 (Duplicate Check & ID assignment against `data/output/content_plan_index.md`) runs first, before INIT reads any other reference doc** — then INIT, then Kroky 1–7, each ending with an explicit STOP for user confirmation (see workflow guide section 15 — step confirmation is mandatory, never skip).

**Never skip Krok 0.** If the requested topic already exists (Published or already in the TODO list under a different entry point), stop and redirect instead of writing a duplicate article.

**Mandatory first action in Krok 5 (Struktura):** paragraph audit — see workflow guide section 10 / structure guide section 4. Split every paragraph over 100 words before any callouts, tables, or H3s.

**Log integrity:** every "Original" cell in every log table must be copied verbatim from the current file — never reconstructed from memory (workflow guide section 13).

## Usage

```
/evisions-new-article SEO-04
/evisions-new-article "SEO pro e-commerce"
/evisions-new-article continue seo-pro-e-commerce
/evisions-new-article
```
