# evisions.cz Blog: Content Inventory

**Verze:** 3.0
**Vytvořeno:** 2026-07-10
**Aktualizováno:** 2026-08-18 — primárním zdrojem je nově Content Plan Index Sheet (viz Document History)

**Primární zdroj:** [Content Plan Index Sheet](https://docs.google.com/spreadsheets/d/1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q/edit?gid=754600260#gid=754600260) (file ID `1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q`)
**Sekundární zdroj (jen na vyžádání):** [původní "evisions.cz - Content Plan" Sheet](https://docs.google.com/spreadsheets/d/1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY/edit?gid=1262896623#gid=1262896623) (file ID `1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY`)

---

## Jak spolu souvisí ledger, xlsx a primární Sheet

1. **`data/output/content_plan_index.md`** — lokální dedup ledger, zdroj pravdy pro Claude. `/evisions-new-article` ho čte jako první krok (Krok 0 write workflow), aby nevytvořil duplicitní článek, a zapisuje do něj nově přiřazená ID.
2. **`data/output/content_plan_index.xlsx`** — vygenerovaný z ledgeru přes `src/generate_content_plan_xlsx.py` (jedna záložka na kategorii + záložka "Legenda"). Nové/změněné řádky (Status "In Progress") jsou zeleně zvýrazněné.
3. **Content Plan Index Sheet (primární, Google Sheets)** — uživatel nahrál `content_plan_index.xlsx` do Google Drive a ten se stal primárním pracovním dokumentem (2026-08-18). Má identickou strukturu jako xlsx mirror (stejné záložky, stejné sloupce), protože z něj vznikl. Uživatel do něj může psát přímo (doplňovat Lokace, zpracoval, klíčová slova, brief u starších řádků, přidávat nová TODO témata) — na rozdíl od `content_plan_index.xlsx`, který je jen lokální, needitovatelný výstup.

**Tok dat:** ledger (.md) → xlsx mirror → uživatel nahraje/aktualizuje v primárním Sheetu → Claude občas znovu přečte primární Sheet a osvěží ledger (viz "Refresh" níže). Google Drive MCP umí primární Sheet jen **číst**, ne zapisovat jednotlivé buňky — proto při Krok 0 (přiřazení ID) a Krok 7 (Status → Published) Claude vypíše hotový řádek k ručnímu vložení do primárního Sheetu, stejně jako předtím.

**Refresh ledgeru z primárního Sheetu:** proveď, když je podezření na rozpor (uživatel řekl, že něco do Sheetu ručně přidal/změnil, nebo dlouho neproběhl sync) — ne při každém spuštění skillu.

---

## Sekundární Sheet — kdy ho použít

Původní "evisions.cz - Content Plan" Sheet (`1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY`) má bohatší historická data pro starší články (přesné Lokace, zpracoval, klíčová slova, brief), která se do ledgeru/primárního Sheetu zatím nepřenesla. Skilly z něj **automaticky nečtou** — použij ho jen když se na něj uživatel výslovně odkáže (např. potřebuje dohledat, kdo článek psal, nebo přesné historické zařazení).

---

## Struktura Content Plan Index Sheetu (primární)

Editorial-calendar formát — samostatné záložky podle kategorie, každá se svým ID prefixem, a uvnitř kategorií "Skupina" podskupiny (řádek se štítkem skupiny nad příslušnými řádky).

**Kategorie a jejich ID prefixy:**

| Kategorie | ID prefix |
|-----------|-----------|
| SEO | SEO-XX |
| PPC | PPC-XX |
| Social | SOC-XX |
| AI & SEO | AI-XX |
| Copywriting | CW-XX |
| Konference | CONF-XX |
| Marketing | MKT-XX |
| evisions interní | EVI-XX |
| International | INTL-XX |
| Kariéra (rozhovory se zaměstnanci) | PC-XX |
| Kariéra (stáž/nábor) | CAR-XX |

**Sloupce:**

| Sloupec | Popis |
|---------|-------|
| Lokace | Umístění řádku v hierarchii kategorie/skupiny (u starších řádků často prázdné — dobírá se ze sekundárního Sheetu) |
| Lekce | Pořadí/číslo v rámci skupiny |
| Kapitola / Nadpis | **ID** článku (např. `SEO-30`), ne titulek |
| Obsah kapitoly - podtéma | Skutečný titulek/téma článku |
| Typ obsahu | Např. "nový text - lekce" pro plánovaný, ale ještě nenapsaný článek |
| zpracoval | Kdo článek píše/zpracovává |
| Článek/Case | Typ výstupu (článek vs. case study) |
| odhad práce | Odhad pracnosti |
| klíčová slova | Cílová klíčová slova |
| brief | Odkaz/poznámka k briefu |
| složka s výstupy | Cesta ke složce s výstupy (`data/output/articles/[slug]/`) |
| final docs | URL živého článku |
| log | Odkaz na log souboru |
| Status | TODO / In Progress / Published apod. |
| Počet | Počet slov/znaků nebo jiná kvantifikace |

**Jak poznat stav řádku:**
- Prázdné ID → **TODO/plánovaný** (kandidát pro `/evisions-new-article`)
- Status "In Progress" → Claude na tom právě pracuje, ještě nepublikováno
- Vyplněná URL + Status "Published" → **živý článek** (kandidát pro `/evisions-rewrite-article`)

---

## Interní prolinkování

Interní odkazy se řídí **tematickou příbuzností kategorie a skupiny**, ne pevnou posloupností:

- Články ve stejné kategorii/skupině → vzájemně prolinkovat, pokud jsou tematicky blízké
- Case study → prolinkovat na související how-to obsah stejné disciplíny (např. SEO case study → SEO how-to články)
- Nový článek → zkontrolovat Content Plan pro 2-3 relevantní publikované články k prolinkování (Status = Published, URL vyplněná)

---

## Document History

| Verze | Datum | Změny |
|-------|-------|-------|
| 1.0 | 2026-07-10 | První verze, dokumentovala placeholder sheet (`1W8VTbwT8...`) s 8 příklady + 1 TODO řádkem |
| 2.0 | 2026-08-18 | Opraveno na skutečný pracovní Content Plan sheet (`1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY`) — editorial-calendar formát s per-kategorie tabulkami místo plochého seznamu |
| 3.0 | 2026-08-18 | Uživatel nahrál vygenerovaný `content_plan_index.xlsx` do Google Drive jako editovatelný **Content Plan Index Sheet** (`1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q`) a určil ho jako primární zdroj pro všechny skilly. Sheet `1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY` degradován na sekundární/jen na vyžádání. |

---

*Companion document: [evisions.cz Write Workflow](evisions_write_workflow_CZ.md) | [Edit Workflow](evisions_workflow_CZ.md)*
