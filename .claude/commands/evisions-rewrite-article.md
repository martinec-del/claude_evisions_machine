# evisions.cz Blog — Rewrite Article

Arguments: $ARGUMENTS

## Reference Documents

**Workflow:** `data/output/guides/evisions_workflow_CZ.md`
**ToV Guide:** `data/output/guides/evisions_tov_guide_CZ.md`
**Structure Guide:** `data/output/guides/evisions_structure_guide_CZ.md`
**Content Inventory:** `data/output/guides/evisions_content_inventory.md`
**Content Plan Index (dedup ledger):** `data/output/content_plan_index.md` — at INIT, look up the target URL here to recover its ID/category; if missing, look it up in the Sheet by URL and add the row here (existing published article the ledger doesn't know about yet).
**Competitor SERP check:** `prompts/step1b_competitor_check.md` (Krok 1.5, mezi Kroky 1 a 2)
**HTML template script:** `src/step4_html.py`
**Docx export script (automatický, hned po HTML):** `src/export_article_docx.py` — generuje čitelný Word export finálního článku vedle `.html`, viz `prompts/step4_html.md` sekce "Docx export".
**Log export script:** `src/generate_log.py`

### Content Plan — Google Sheet

**Primary Sheet:** [Content Plan Index Sheet](https://docs.google.com/spreadsheets/d/1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q/edit?gid=754600260#gid=754600260) — read via `mcp__claude_ai_Google_Drive__read_file_content` (file ID `1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q`). Used to check whether the article's Status is already "Published" and to find its category (per-category tab / ID prefix) for internal-link suggestions. Secondary Sheet (file ID `1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY`) only if the user asks for its richer historical data.

## Usage Modes

| Mode | Invocation | Behavior |
|------|-----------|----------|
| **rewrite** (default) | `/evisions-rewrite-article [URL]` | Full 6-step workflow (Krok 1, 1.5, 2, 3, 4, 5), creates edited file |
| **quick** | `/evisions-rewrite-article quick [URL]` | Top 5 issues only, no full rewrite (skips Krok 1.5) |
| **tov** | `/evisions-rewrite-article tov [URL]` | ToV-only pass (Krok 2 in isolation, skips Krok 1.5) |
| **structure** | `/evisions-rewrite-article structure [URL]` | Structure-only pass (Krok 3 in isolation, skips Krok 1.5 — no competitor gap-filling available in this mode) |
| **eeat** | `/evisions-rewrite-article eeat [URL]` | E-E-A-T audit only (author, sources, dates) |
| **check** | `/evisions-rewrite-article check [path]` | Translate/verify sentence change log |

Default with no mode keyword = full `rewrite`.

## Entry Point

### A) URL or path provided

Go to Initialization (`data/output/guides/evisions_workflow_CZ.md` section 3b), run the workflow for the requested mode.

### B) No arguments — show menu and STOP

```
evisions.cz Blog — Article Editor

Dostupné módy:
  1. Full rewrite (zadejte URL)
  2. Quick audit (zadejte URL)
```

Do NOT read any reference documents. Do NOT start any workflow. Wait for user input.

## Input Format

```
Článek: https://www.evisions.cz/blog/[slug]/
Keywords: data/output/keywords/[slug]_keywords.xlsx
```

If the keywords file does not exist, create an empty template via `src/create_keyword_xlsx.py [slug]` and stop — ask the user to fill it before Krok 1 (or confirm to proceed with weaker keyword integration).

## Workflow

Follow `data/output/guides/evisions_workflow_CZ.md` exactly — Krok 1 (Klíčová slova) → **Krok 1.5 (Konkurenční SERP kontrola)** → Krok 2 (ToV) → Krok 3 (Struktura) → Krok 4 (HTML) → Krok 5 (QA), each ending with an explicit STOP for user confirmation.

**Core principle (do not violate):** preserve content, enhance presentation. Facts, numbers, and meaning from the original article never change — only word choice, keyword integration, and formatting.

**One narrow exception:** Krok 1.5 checks the article's content depth against 2-3 top-ranking competitors for its primary keywords. If it finds real content gaps, it stops and asks the user to choose Mode A (competitively rewrite — write and insert new sections to close the gaps, approved at the Krok 3 STOP) or Mode B (log the gaps only, no new content — default "preserve content" rule stays intact). Mode A is the only place in this entire workflow where new information may be added, and only after explicit user approval.

**Log integrity:** every "Original" cell must be copied verbatim from the article file at the time of the change — never reconstructed from memory.

## Usage

```
/evisions-rewrite-article https://www.evisions.cz/blog/[slug]/
/evisions-rewrite-article quick https://www.evisions.cz/blog/[slug]/
/evisions-rewrite-article tov https://www.evisions.cz/blog/[slug]/
/evisions-rewrite-article
```
