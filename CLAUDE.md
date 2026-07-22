# evisions.cz Blog - Project CLAUDE.md

## PROJECT: evisions.cz Content

evisions Advertising s.r.o. — pražská digitální marketingová agentura (SEO, PPC, analytika, obsah). Tento projekt řídí tvorbu a editaci článků na [evisions.cz/blog/](https://www.evisions.cz/blog/) stejným principem jako FTMO Academy content systém, adaptovaným pro plochou blogovou strukturu a češtinu.

### CONTENT PLÁN

Zdroj: [Google Sheet "evisions.cz - Content Plan"](https://docs.google.com/spreadsheets/d/1W8VTbwT8_HiYuEF62rgJzI6KRTKJ9neI7LU4vt4IC74/edit) (file ID `1W8VTbwT8_HiYuEF62rgJzI6KRTKJ9neI7LU4vt4IC74`), čtený přímo přes připojený Google Drive MCP (`mcp__claude_ai_Google_Drive__read_file_content`) — žádná kurzová hierarchie, každý řádek je jeden článek. Sloupce: ID, Kategorie, Téma, Klíčové slovo, Search Volume, Typ obsahu, Status, URL, Poznámky.

Detaily: `data/output/guides/evisions_content_inventory.md`

---

### DVA WORKFLOW

#### Větev A — Editace existujícího článku (`/evisions-rewrite-article`)

Použít, když článek už existuje na živém webu.

```
/evisions-rewrite-article https://www.evisions.cz/blog/[slug]/
Keywords: data/output/keywords/[slug]_keywords.xlsx
```

5-krokový workflow: Klíčová slova → ToV → Struktura → HTML → QA
Definováno v: `data/output/guides/evisions_workflow_CZ.md`

#### Větev B — Nový článek od nuly (`/evisions-new-article`)

Použít, když článek zatím neexistuje (Status = TODO v Content Plan Sheetu).

```
/evisions-new-article [ID z Content Plan | téma]
```

7-krokový workflow: INIT → Konkurenční research + Klíčová slova → Brief & osnova → Draft → ToV kontrola → Struktura → HTML → QA
Definováno v: `data/output/guides/evisions_write_workflow_CZ.md`

#### Doplňkový skill — Proofread (`/evisions-proofread`)

Jazykový proofread (spisovná čeština, gramatika, styl) bez zásahu do obsahu/SEO/struktury. Použít jako poslední QA krok nebo samostatně.

#### Doplňkový skill — Topic Cluster Audit (`/evisions-topic-cluster`)

Audit Topic Authority a kontrola kanibalizace klíčových slov pro celé téma (ne jeden článek) v rámci publikačního plánu. Použít při plánování/revizi publikačního plánu pro téma/kategorii — před zadáním nových článků přes `/evisions-new-article` nebo revizí přes `/evisions-rewrite-article`.

```
/evisions-topic-cluster
Téma: [téma X]
Stávající články: [URL / cesty]
```

5-krokový workflow: Klíčová slova (primární keywords = informačního charakteru) → Analýza konkurence v SERPu → Rozšířená analýza konkurence (7+ dalších informačních keywords k širšímu tématu) → Content Gap audit → Akční plán
Definováno přímo v: `.claude/commands/evisions-topic-cluster.md`

---

### PRAVIDLA — OBA WORKFLOW

**NIKDY needitovat obsah ručně** bez použití příslušného skillu.

**POTVRZENÍ KROKU — POVINNÉ:**
Po každém kroku STOP a čekat na potvrzení uživatele před pokračováním.
Automatické přechody mezi kroky jsou ZAKÁZÁNY.

**AUDIT ODSTAVCŮ — POVINNÁ PRVNÍ AKCE VE STRUCTURE KROKU:**
Před přidáním jakýchkoli calloutů, tabulek nebo H3 — projít každý odstavec a zkontrolovat délku.
Rozdělit každý odstavec nad 100 slov. Toto je nejčastěji vynechávaná kontrola.

**JAZYK: ČEŠTINA.** Veškerý obsah se píše přímo v češtině — ne v angličtině s následným překladem. ToV Guide používá vykání s přímým oslovením (viz sekce 5), ne British English pravidla FTMO.

---

### REFERENČNÍ DOKUMENTY

| Dokument | Účel | Použit v |
|----------|------|----------|
| `data/output/guides/evisions_workflow_CZ.md` | Edit workflow (5 kroků) | `/evisions-rewrite-article` |
| `data/output/guides/evisions_write_workflow_CZ.md` | Write workflow (7 kroků) | `/evisions-new-article` |
| `data/output/guides/evisions_tov_guide_CZ.md` | Tone of Voice guide | Oba |
| `data/output/guides/evisions_structure_guide_CZ.md` | Structure & E-E-A-T guide | Oba |
| `data/output/guides/evisions_content_inventory.md` | Content plán (odkaz na Sheet) | Oba |
| `data/output/guides/evisions_brand_analysis_CZ.md` | Podklad pro ToV/Structure (analýza živého blogu) | Reference |

---

### LOG FORMAT — POUZE DOSLOVNĚ

> **TOTO JE NEJKRITIČTĚJŠÍ PRAVIDLO CELÉHO WORKFLOW.**
>
> Sloupec "Original" v každém logu MUSÍ být zkopírován znak po znaku ze souboru článku.
> NIKDY nerekonstruovat z paměti. NIKDY neparafrázovat. NIKDY neaproximovat.
>
> **Správný postup:**
> 1. Najít větu v aktuálním souboru (Read tool, pokud je potřeba)
> 2. Zkopírovat ji přesně — interpunkce, velká písmena, formátování včetně
> 3. Provést změnu
> 4. Zalogovat: [doslovně ze souboru] → [přesná nová verze] + důvod
>
> **Špatně:** psát, co si myslíte, že tam bylo
> **Správně:** přečíst soubor, zkopírovat přesný text, pak zalogovat

```markdown
| # | Original sentence (full) | New sentence (full) | Reason |
|---|--------------------------|----------------------|--------|
| 1 | "Naše kampaně přinášejí skvělé výsledky." | "Kampaň zvýšila konverzní poměr o 34 % za 3 měsíce." | ToV: hype bez dat → konkrétní číslo |
```

---

### KONVENCE POJMENOVÁNÍ

```
data/output/articles/[slug]/article_[slug]_CZ_outline.docx  # Krok 2: Brief + osnova (expert edituje)
data/output/articles/[slug]/article_[slug]_CZ.md            # Finální markdown (první verze)
data/output/articles/[slug]/article_[slug]_CZ_log.md        # Log (první verze)
data/output/articles/[slug]/article_[slug]_CZ.html          # Finální HTML (první verze)
data/output/articles/[slug]/article_[slug]_CZ_log.html      # Log HTML (první verze)
data/output/articles/[slug]/article_[slug]_CZ_v2.md         # Druhá verze
data/output/keywords/[slug]_keywords.xlsx                    # Keywords soubor
```

Slugy používají pomlčky (odpovídají URL slugům): `seo-pro-e-commerce`, ne `seo_pro_e_commerce`.

### PRAVIDLO VERZOVÁNÍ

Při přepisu článku (`/evisions-new-article [slug]` na existující slug):
- INIT detekuje existující soubory ve složce slugu
- Určí další číslo verze (v2, v3, ...) automaticky
- Použije tento suffix pro VŠECHNY 4 výstupní soubory nového běhu
- **Nikdy nepřepisuje ani nepřejmenovává existující soubory**

---

### MODELY

Konfigurace v `src/config.py`. Výchozí model pro testování: `gpt-4o-mini`.
Produkce: `gpt-4o` nebo `claude-sonnet-4-6`.

---

### MCP SERVERY

- **Ahrefs** (povinné pro Krok 1 keyword research) — již připojeno v tomto účtu
- **Google Drive** (pro čtení/zápis Content Plan Sheetu) — již připojeno, autentizováno jako analytics@evisions.cz
- Bez dalších MCP funguje Krok 1 přes built-in `WebSearch` + `WebFetch` (vždy dostupné)
