# evisions.cz Blog — Skill Router

Arguments: $ARGUMENTS

## Účel

Tento skill je **hlavní vstupní bod** pro veškerou tvorbu a editaci obsahu evisions.cz blogu. Sám neprovádí žádnou content práci — jeho úkol je:

1. Dát přehled, jaké sub-skilly existují a co každý dělá
2. Pomoci rozhodnout, který sub-skill spustit pro konkrétní úkol
3. Sdílet projektový kontext (paths, Content Plan Sheet) společný pro všechny sub-skilly

> **Tento skill nic negeneruje a nic needituje.** Pokud chceš pracovat na konkrétním článku, použij přímo příslušný sub-skill.

## Project Paths

> **Convention:** všechny cesty v skillech jsou **relativní k project root** (`Evisions claude machine`). CWD musí být project root.

| Účel | Cesta (project-relative) |
|------|-------|
| Articles output | `data/output/articles/[slug]/` |
| Keywords templates | `data/output/keywords/[slug]_keywords.xlsx` |
| Guides (ToV, Structure, Inventory, Workflow) | `data/output/guides/` |
| Generator script | `src/model_tester.py` |
| Keywords template script | `src/create_keyword_xlsx.py` |
| HTML converter | `src/step4_html.py` |
| Drive upload script | `src/upload_to_drive.py` |

## Content Plan — Google Sheet

**Primární Sheet:** [Content Plan Index Sheet](https://docs.google.com/spreadsheets/d/1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q/edit?gid=754600260#gid=754600260)
**File ID:** `1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q`
**Sekundární Sheet (jen na vyžádání):** původní "evisions.cz - Content Plan", file ID `1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY` — bohatší historická data, skilly z něj automaticky nečtou.
**Čtení:** přes připojený `mcp__claude_ai_Google_Drive__read_file_content` (autentizováno jako analytics@evisions.cz) — žádný service account potřeba pro čtení.

**Struktura (jedna záložka per kategorie, stejná jako `data/output/content_plan_index.xlsx`):**

Záložky podle kategorie (SEO, PPC, Social, AI & SEO, Copywriting, Konference, Marketing, evisions interní, International, Kariéra ×2), každá s vlastním ID prefixem (SEO-XX, PPC-XX, SOC-XX, AI-XX, CW-XX, CONF-XX, MKT-XX, EVI-XX, INTL-XX, PC-XX, CAR-XX). Uvnitř kategorií jsou "Skupina" podskupiny (řádek se štítkem skupiny).

| Sloupec | Pole |
|---------|------|
| — | Lokace |
| — | Lekce |
| — | Kapitola / Nadpis (= **ID**, ne titulek) |
| — | Obsah kapitoly - podtéma (= skutečný titulek/téma) |
| — | Typ obsahu |
| — | zpracoval |
| — | Článek/Case |
| — | odhad práce |
| — | klíčová slova |
| — | brief |
| — | složka s výstupy |
| — | final docs (URL) |
| — | log |
| — | Status |
| — | Počet |

**Jak poznat stav řádku:** prázdné ID + "nový text - lekce" v Typ obsahu → TODO/plánovaný. Vyplněná URL + Status "Published" → živý článek.

Detaily: `data/output/guides/evisions_content_inventory.md`

## Sub-Skills — kdy použít který

### 1. `/evisions-new-article [ID z Content Plan | téma]`

**Účel:** Vytvořit článek **od nuly**.

**Použij když:**
- Řádek v Content Plan Sheetu má Status "TODO"
- Lokální složka `data/output/articles/[slug]/` ještě neexistuje
- Klient/tým zadal nové téma bez existujícího řádku v Sheetu

**Workflow:** Konkurenční research + Klíčová slova → Brief & osnova → Draft → ToV kontrola → Struktura → HTML → QA.

**Output:** `article_[slug]_CZ.md`, `.docx`, `.html`, `_log.md`, `_log.html`.

---

### 2. `/evisions-rewrite-article [URL | path]`

**Účel:** **Editovat existující článek** (publikovaný na evisions.cz blogu nebo lokálně rozpracovaný).

**Použij když:**
- Článek je živý na webu a chceme upgrade (ToV, struktura, keywords, E-E-A-T)
- Existuje lokální draft a chceš pokračovat v editaci

**Workflow:** Klíčová slova → ToV rewrite → Struktura & formátování → HTML → QA.

**Output:** `article_[slug]_CZ[_vN].md`, `.docx`, `.html`, `_log.html`.

---

### 3. `/evisions-proofread [path | text]`

**Účel:** **Jazykový proofread v češtině** existujícího textu. Pouze jazyková kvalita, neřeší obsah, SEO, strukturu ani relevanci.

**Použij když:**
- Máš hotový draft a chceš zkontrolovat gramatiku, pravopis, interpunkci, styl, plynulost
- Před finalizací článku jako poslední QA krok
- (Volitelně) mezi Krokem 2 a Krokem 3 v `/evisions-rewrite-article` workflow

**Scope:** Spisovná čeština. Žádné pomlčky místo interpunkce tam, kde nepatří. Konzistentní vykání.

---

### 4. `/evisions-topic-cluster`

**Účel:** **Topic Authority audit + kontrola kanibalizace klíčových slov** pro dané téma v rámci publikačního plánu. Analyzuje, zda naše stávající články k tématu dostatečně pokrývají klíčová slova/search intent, zmapuje konkurenci v SERPu a navrhne akční plán (revize stávajících článků, nový obsah, kanibalizace, prolinkování).

**Použij když:**
- Plánuješ nebo revidueš publikační plán pro celé téma/kategorii (ne jeden článek)
- Chceš ověřit, že nové navrhované téma nekoliduje s existujícím článkem na stejné primární klíčové slovo
- Potřebuješ zmapovat content gaps vůči konkurenci před zadáním nových článků

**Workflow:** Klíčová slova (Ahrefs + Google) → Analýza konkurence v SERPu (primární keywords) → Rozšířená analýza konkurence (7+ dalších keywords k širšímu tématu) → Audit obsahu + Content Gap → Finální akční plán, každý krok STOP na schválení.

**Output:** `data/output/clusters/[topic-slug]/topic_cluster_[topic-slug]_CZ.md` (nezasahuje do žádného existujícího článku — návrhy z reportu se realizují přes `/evisions-new-article` nebo `/evisions-rewrite-article`).

---

### 5. `/evisions-category-gap`

**Účel:** **Rychlá gap analýza celé kategorie** (SEO / PPC / AI & SEO / Analytika / E-commerce / Případovky) — porovnává naplánovaná + existující témata v Content Planu s reálně hledanými klíčovými slovy a navrhne chybějící témata článků pro lepší Topic Authority kategorie. Neřeší SERP konkurenci ani kanibalizaci (na to slouží `/evisions-topic-cluster`).

**Použij když:**
- Chceš rychle zkontrolovat, zda kategorie jako celek pokrývá důležitá hledaná podtémata
- Plánuješ doplnit content plán o nová témata a chceš je nejdřív podložit keyword daty
- Nepotřebuješ (zatím) hloubkovou SERP/konkurenční analýzu jednotlivého tématu

**Workflow:** Gap analýza + návrh prioritních kws na základě expertízy → STOP na schválení → ověření a rozšíření kws (Ahrefs + Marketing Miner).

**Output:** `data/output/category-gaps/[kategorie-slug]/category_gap_[kategorie-slug]_CZ.md` + `.docx`.

**Tip:** použij jako první, rychlý průchod před `/evisions-topic-cluster`, pokud chceš nejdřív zmapovat, co v kategorii vůbec chybí, než se pustíš do hloubkové analýzy jednoho tématu.

---

## Decision Tree — který skill zvolit?

```
Řeším jeden konkrétní článek, celé téma/cluster, nebo celou kategorii?
│
├── CELÁ KATEGORIE (rychlý gap check proti keyword datům)
│   └── /evisions-category-gap
│
├── CELÉ TÉMA / publikační plán (+ SERP konkurence, kanibalizace)
│   └── /evisions-topic-cluster
│
└── JEDEN ČLÁNEK → existuje už lokálně nebo na webu?
    │
    ├── NE (nový obsah)
    │   └── /evisions-new-article
    │
    └── ANO (existuje)
        │
        ├── Potřebuju editovat obsah / strukturu / ToV / keywords? → /evisions-rewrite-article
        └── Potřebuju jen jazykový proofread? → /evisions-proofread
```

## Shared rules (platí pro všechny sub-skilly)

Detaily jsou v guides:

- **Spisovná čeština** (ne hovorová), vykání s přímým, aktivním oslovením
- **Žádné neopodstatněné garance výsledků** — case study rámovat jako "u klienta X", nikdy jako obecný slib
- **Data-driven** — každé číslo má jmenovaný zdroj
- **E-E-A-T** — autor s rolí, citované zdroje, přiznání limitů metody
- **Logy** — celá původní věta → celá nová věta, nikdy výňatky

## Reference Documents (shared)

| Guide | Path |
|-------|------|
| ToV Guide | `data/output/guides/evisions_tov_guide_CZ.md` |
| Structure Guide | `data/output/guides/evisions_structure_guide_CZ.md` |
| Content Inventory | `data/output/guides/evisions_content_inventory.md` |
| Brand Analysis | `data/output/guides/evisions_brand_analysis_CZ.md` |
| Edit Workflow | `data/output/guides/evisions_workflow_CZ.md` |
| Write Workflow | `data/output/guides/evisions_write_workflow_CZ.md` |

## Entry behavior

Když uživatel zavolá `/evisions-content`:

1. Vypiš krátkou tabulku sub-skillů (název → účel → kdy použít)
2. Pokud user uvedl argument (URL, slug, ID z Content Plan, téma, kategorie), zkus odhadnout správný sub-skill a navrhni ho:
   - URL z `evisions.cz/blog/` → `/evisions-rewrite-article [URL]`
   - ID z Content Plan Sheetu se Status "TODO" → `/evisions-new-article [ID]`
   - Path k draftu + požadavek "proofread" → `/evisions-proofread [path]`
   - Název kategorie (SEO / PPC / Social / AI & SEO / Copywriting / Konference / Marketing / evisions interní / International / Kariéra) bez konkrétního tématu → `/evisions-category-gap [kategorie]`
   - Konkrétní téma + seznam existujících článků k němu → `/evisions-topic-cluster`
3. **STOP** a počkej na potvrzení uživatele. Tento skill nikdy nespouští sub-skill automaticky.

## Notes

- Tento router neobsahuje žádný content workflow — všechen workflow je v sub-skillech.
- Pokud potřebuješ rozšířit o nový typ obsahu (např. glosář marketingových pojmů, newsletter), přidej nový `/evisions-*` skill a zaregistruj ho v tomto routeru — stejný vzor jako `/academy-glossary` u FTMO.
- **Mimo scope tohoto routeru:** `/evisions-lead-opportunity` — analyzuje evisions.cz jako **celý web** (service/product stránky, ne blog content plán), hledá SEO příležitosti pro navýšení B2B leadů. Použij, když řešíš web jako celek a jeho leadový potenciál, ne konkrétní blog článek/kategorii/téma.
