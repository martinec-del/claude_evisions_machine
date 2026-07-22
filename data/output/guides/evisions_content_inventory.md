# evisions.cz Blog: Content Inventory

**Verze:** 1.0
**Vytvořeno:** 2026-07-10
**Zdroj:** [Google Sheet "evisions.cz - Content Plan"](https://docs.google.com/spreadsheets/d/1W8VTbwT8_HiYuEF62rgJzI6KRTKJ9neI7LU4vt4IC74/edit)

---

## Jak se čte Content Plan

Na rozdíl od FTMO (service account s read-only Sheets API scope) tento projekt čte Content Plan Sheet přímo přes připojený **Google Drive MCP** (`mcp__claude_ai_Google_Drive__read_file_content`, file ID `1W8VTbwT8_HiYuEF62rgJzI6KRTKJ9neI7LU4vt4IC74`), protože MCP je autentizovaný přímo jako analytics@evisions.cz. Není potřeba samostatný service account jen pro čtení Sheetu.

Service account (`credentials/google_sheets.json`) je potřeba pouze pro standalone Python skripty spouštěné mimo Claude Code (`src/upload_to_drive.py` pro nahrávání souborů do Drive složky).

---

## Struktura Content Plan Sheetu

Na rozdíl od kurzové hierarchie FTMO Academy (Lokace X.Y.Z.N.) je evisions blog **plochý** — každý řádek je jeden článek.

| Sloupec | Pole | Popis |
|---------|------|-------|
| A | ID | Prefix kategorie + pořadové číslo, např. `SEO-04` |
| B | Kategorie | SEO / PPC / AI & SEO / Analytika / E-commerce / Případovky |
| C | Téma / pracovní název | Pracovní název článku |
| D | Klíčové slovo | Primární cílové klíčové slovo |
| E | Search Volume | Doplní se přes Ahrefs v Kroku 1 write workflow |
| F | Typ obsahu | Case study / How-to / Trend analýza / Srovnání |
| G | Status | TODO / Draft / Review / Published |
| H | URL | Živá URL po publikaci |
| I | Poznámky | Autor, kontext, poznámky |

---

## Aktuální stav (k 2026-07-10)

Sheet byl inicializován s existujícími živými články na evisions.cz blogu (pro referenci a jako podklad pro brand analýzu), plus jedním TODO příkladem:

| ID | Kategorie | Téma | Status |
|----|-----------|------|--------|
| SEO-01 | SEO | Z nuly na SEO hvězdu: Kalkulátor.cz | Published |
| PPC-01 | PPC | MASO-PROFIT case study | Published |
| AI-01 | AI & SEO | Query fan-out v praxi | Published |
| AI-02 | AI & SEO | Jak funguje AI Mode od Googlu | Published |
| PPC-02 | PPC | Meta AI stack | Published |
| SEO-02 | SEO | breAd. case study — B2B SEO | Published |
| FIN-01 | Analytika | MONETA Money Bank SEO/GEO case study | Published |
| PPC-03 | PPC | Samurajská kampaň | Published |
| SEO-03 | SEO | PŘÍKLAD — doplňte nové téma | TODO |

**Další kroky pro uživatele:** Smazat/upravit řádek `SEO-03` a přidat skutečná plánovaná témata s vlastním ID, kategorií a klíčovým slovem před spuštěním `/evisions-new-article`.

---

## Interní prolinkování

Protože struktura je plochá (ne kurz s prerekvizitami), interní odkazy se řídí **tematickou příbuzností kategorie**, ne pevnou posloupností:

- Články ve stejné kategorii → vzájemně prolinkovat, pokud jsou tematicky blízké
- Case study → prolinkovat na související how-to obsah stejné disciplíny (SEO case study → SEO how-to články)
- Nový článek → zkontrolovat Content Plan Sheet pro 2-3 relevantní publikované články k prolinkování (sloupec Status = Published, sloupec URL vyplněný)

---

## Document History

| Verze | Datum | Změny |
|-------|-------|-------|
| 1.0 | 2026-07-10 | První verze, Sheet inicializován s 8 existujícími články + 1 TODO příkladem |

---

*Companion document: [evisions.cz Write Workflow](evisions_write_workflow_CZ.md) | [Edit Workflow](evisions_workflow_CZ.md)*
