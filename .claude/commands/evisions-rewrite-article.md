# evisions.cz Blog — Rewrite Article

Arguments: $ARGUMENTS

## Reference Documents

**Workflow:** `data/output/guides/evisions_workflow_CZ.md`
**ToV Guide:** `data/output/guides/evisions_tov_guide_CZ.md`
**Structure Guide:** `data/output/guides/evisions_structure_guide_CZ.md`
**Content Inventory:** `data/output/guides/evisions_content_inventory.md`
**HTML template script:** `src/step4_html.py`
**Log export script:** `src/generate_log.py`

### Content Plan — Google Sheet

**Sheet:** [evisions.cz - Content Plan](https://docs.google.com/spreadsheets/d/1W8VTbwT8_HiYuEF62rgJzI6KRTKJ9neI7LU4vt4IC74/edit) — read via `mcp__claude_ai_Google_Drive__read_file_content` (file ID `1W8VTbwT8_HiYuEF62rgJzI6KRTKJ9neI7LU4vt4IC74`). Used to check whether the article's Status is already "Published" and to find its category for internal-link suggestions.

## Usage Modes

| Mode | Invocation | Behavior |
|------|-----------|----------|
| **rewrite** (default) | `/evisions-rewrite-article [URL]` | Full 5-step workflow, creates edited file |
| **quick** | `/evisions-rewrite-article quick [URL]` | Top 5 issues only, no full rewrite |
| **tov** | `/evisions-rewrite-article tov [URL]` | ToV-only pass (Krok 2 in isolation) |
| **structure** | `/evisions-rewrite-article structure [URL]` | Structure-only pass (Krok 3 in isolation) |
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

Follow `data/output/guides/evisions_workflow_CZ.md` exactly — Krok 1 (Klíčová slova) → Krok 2 (ToV) → Krok 3 (Struktura) → Krok 4 (HTML) → Krok 5 (QA), each ending with an explicit STOP for user confirmation.

**Core principle (do not violate):** preserve content, enhance presentation. Facts, numbers, and meaning from the original article never change — only word choice, keyword integration, and formatting.

**Log integrity:** every "Original" cell must be copied verbatim from the article file at the time of the change — never reconstructed from memory.

## Usage

```
/evisions-rewrite-article https://www.evisions.cz/blog/[slug]/
/evisions-rewrite-article quick https://www.evisions.cz/blog/[slug]/
/evisions-rewrite-article tov https://www.evisions.cz/blog/[slug]/
/evisions-rewrite-article
```
