# evisions.cz Content System

AI-assisted content creation and editing system for the evisions.cz blog (SEO, PPC, analytika, AI a e-commerce marketing). Postaveno stejným principem jako FTMO Academy content systém, adaptovaným pro plochou blogovou strukturu a češtinu.

## Quick Start

### 1. Nastavení

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -e .
```

### 2. Konfigurace Claude Code

Tento projekt obsahuje čtyři slash commands jako project-level Claude Code skilly v `.claude/commands/`. Jsou automaticky dostupné při otevření Claude Code v tomto adresáři.

**Doporučené MCP servery:**
- **Ahrefs** — keyword research, SERP analýza, backlinky (viz `mcp__claude_ai_Ahrefs__*`)
- **Google Drive** — čtení/zápis Content Plan Sheetu (autentizováno jako analytics@evisions.cz)

Bez žádného MCP funguje Krok 1 přes built-in `WebSearch` + `WebFetch` (funguje vždy).

### 3. .env

```bash
copy .env.example .env
# Doplňte API klíče
```

## Content Plan

Zdroj témat: [Google Sheet "evisions.cz - Content Plan"](https://docs.google.com/spreadsheets/d/1W8VTbwT8_HiYuEF62rgJzI6KRTKJ9neI7LU4vt4IC74/edit)

Plochá struktura — žádná kurzová hierarchie jako u FTMO Academy. Každý řádek je jeden článek se sloupci: ID, Kategorie, Téma, Klíčové slovo, Search Volume, Typ obsahu, Status, URL, Poznámky.

Sheet byl inicializován s 8 existujícími live články z evisions.cz/blog/ (jako reference) + 1 TODO příkladem. Detaily: `data/output/guides/evisions_content_inventory.md`.

## Workflows

### `/evisions-content` — Router

Vstupní bod. Vypíše přehled sub-skillů a navrhne, který spustit dle zadaného argumentu (URL, ID z Content Plan, téma).

### `/evisions-new-article [ID | téma]` — Nový článek

7-krokový workflow pro psaní článků od nuly:

| Krok | Akce | Output |
|------|------|--------|
| INIT | Načíst reference, vytvořit log | Init summary |
| 1 | Konkurenční research + klíčová slova (WebSearch + Ahrefs MCP) | Seznam URL + sada klíčových slov |
| 2 | Brief & osnova | Schválená osnova |
| 3 | Psaní draftu | Plný článek + zdrojové citace |
| 4 | ToV kontrola | Log oprav |
| 5 | Struktura & formátování | Formátovaný markdown |
| 6 | HTML konverze | article.html + log.html |
| 7 | QA + aktualizace Content Plan | 4 finální soubory |

### `/evisions-rewrite-article [URL | path]` — Editace existujícího článku

5-krokový workflow pro úpravu živých článků:

| Krok | Akce |
|------|------|
| 1 | Integrace klíčových slov |
| 2 | ToV rewrite |
| 3 | Struktura & formátování |
| 4 | HTML konverze |
| 5 | QA revize |

Módy: `quick`, `tov`, `structure`, `eeat`, `check` — viz `.claude/commands/evisions-rewrite-article.md`.

### `/evisions-proofread [path | text]` — Jazykový proofread

Čistě jazyková kontrola (spisovná čeština, gramatika, styl) bez zásahu do obsahu/SEO/struktury.

## Project Structure

```
Evisions claude machine/
├── .claude/commands/              # Claude Code slash commands
│   ├── evisions-content.md        # /evisions-content router
│   ├── evisions-new-article.md    # /evisions-new-article
│   ├── evisions-rewrite-article.md # /evisions-rewrite-article
│   └── evisions-proofread.md      # /evisions-proofread
├── CLAUDE.md                      # Project instructions for Claude
├── credentials/                   # gitignored — google_sheets.json (jen pro upload_to_drive.py)
├── data/
│   ├── raw/articles/              # Zdrojové články (READ-ONLY, fetched)
│   ├── output/
│   │   ├── guides/                # ToV guide, Structure guide, Workflow, Content Inventory
│   │   ├── keywords/              # Keyword research XLSX soubory
│   │   └── articles/[slug]/       # Output: .md, _log.md, .html, _log.html
├── prompts/                       # Step-specific prompt šablony
│   ├── write_step1_research.md
│   ├── write_step2_brief.md
│   ├── write_step3_draft.md
│   ├── write_step4_tov_check.md
│   ├── step1_keywords.md
│   ├── step2_tov.md
│   ├── step3_structure.md
│   └── step4_html.md
├── src/                           # Python utility
│   ├── config.py                  # API keys, model config
│   ├── generate_log.py            # Log MD → HTML/PDF converter
│   ├── create_keyword_xlsx.py     # Keyword XLSX template generator
│   ├── model_tester.py            # Multi-model content generator
│   ├── step4_html.py              # HTML konverze (evisions.cz šablona)
│   ├── export_outline_docx.py     # Outline MD → DOCX
│   ├── read_outline_docx.py       # Outline DOCX → text
│   └── upload_to_drive.py         # Google Drive upload (service account)
├── .env.example
└── pyproject.toml
```

## Reference Documents

| Document | Účel |
|----------|------|
| `data/output/guides/evisions_tov_guide_CZ.md` | Tone of Voice — jak má obsah znít |
| `data/output/guides/evisions_structure_guide_CZ.md` | Struktura & E-E-A-T — formátování, nadpisy, callouty |
| `data/output/guides/evisions_write_workflow_CZ.md` | Write workflow — nové články |
| `data/output/guides/evisions_workflow_CZ.md` | Edit workflow — existující články |
| `data/output/guides/evisions_content_inventory.md` | Content plán — odkaz na Google Sheet |
| `data/output/guides/evisions_brand_analysis_CZ.md` | Podklad pro ToV/Structure (analýza živého blogu) |

## Output Files

Každý článek produkuje 4 soubory v `data/output/articles/[slug]/`:

```
article_[slug]_CZ.md          # Finální markdown
article_[slug]_CZ_log.md      # Audit/change log
article_[slug]_CZ.html        # Finální HTML (evisions.cz šablona)
article_[slug]_CZ_log.html    # Stylovaný HTML log
```

Verzování: `_v2`, `_v3` suffixy pro následné přepisy. Předchozí verze se nikdy nepřepisují.

## Key Rules

- **Potvrzení kroku povinné** — každý krok čeká na schválení uživatele před pokračováním
- **evisions Tone of Voice** — zkušený konzultant, ne akademik ani prodejce. Data-driven, žádný hype.
- **Audit odstavců** — povinná první akce ve Structure kroku: rozdělit odstavce nad 100 slov
- **Zdrojové citace** — každé faktické tvrzení potřebuje zdroj v logu
- **Log doslovně** — původní věty kopírované znak po znaku, nikdy z paměti

## Rozdíly oproti FTMO Academy

| | FTMO Academy | evisions.cz Blog |
|--|---------------|---------------------|
| Struktura obsahu | Kurzová hierarchie (Lokace X.Y.Z.N.) | Plochá (jeden řádek = jeden článek) |
| Jazyk | Angličtina (British English) | Čeština (spisovná) |
| Content plán | Google Sheet se service account (read-only Sheets API) | Google Sheet čtený přímo přes Google Drive MCP |
| Skill set | new-lesson, rewrite-article, glossary, proofread | new-article, rewrite-article, proofread |
| Compliance citlivost | YMYL (risk disclaimer, no profit guarantees) | Marketingová tvrzení (no result guarantees, case study framing) |

Založeno na struktuře `ftmo-academy` projektu — viz `data/output/guides/*.md` pro plné detaily každého kroku.
