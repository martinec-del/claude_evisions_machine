# evisions.cz Blog: Content Workflow (Edit)

**Verze:** 1.2
**Vytvořeno:** 2026-07-10
**Účel:** Krok-za-krokem proces pro editaci existujících článků na evisions.cz blogu

---

## 1. Přehled workflow

```
VSTUP                    PROCES                                     VÝSTUP
─────                    ──────                                     ──────
Existující článek   →    Krok 1:   Klíčová slova                →   integrace KW
+ Keywords xlsx     →    Krok 1.5: Konkurenční SERP kontrola    →   report + mód A/B
                    →    Krok 2:   ToV rewrite                  →   upravený text
                    →    Krok 3:   Struktura & formátování      →   finální markdown
                    →    Krok 4:   HTML konverze                →   .html + .docx
                    →    Krok 5:   QA & revize                  →   FINÁLNÍ
```

### ZÁKLADNÍ PRINCIP: Zachovat obsah, vylepšit prezentaci

> **KRITICKÉ:** Původní obsah článku (fakta, informace, význam) se NIKDY nemění.
> Workflow pouze VYLEPŠUJE článek:
> - Krok 1: Přirozené doplnění klíčových slov (žádné nové informace)
> - Krok 1.5: Report o obsahových mezerách vůči konkurenci — jedna výslovně schválená výjimka z "žádné nové informace" (Mód A), viz sekce 4.5
> - Krok 2: Zlepšení volby slov (stejný význam, lepší slova)
> - Krok 3: Přidání formátovacích prvků (tabulky, callouty, seznamy) + případné schválené doplnění obsahu z Kroku 1.5 (Mód A)
> - Krok 4: Konverze do HTML + zachování původních obrázků na stejném místě

**Co se mění:** klíčová slova, volba slov, formátování, prezentace, (volitelně, po schválení) chybějící obsahové sekce vůči konkurenci
**Co se NIKDY nemění bez výslovného schválení:** fakta, informace, význam, pořadí obsahu

---

## 2. Referenční dokumenty

| Dokument | Řeší | Použit v kroku |
|----------|------|-----------------|
| `[slug]_keywords.xlsx` | Cílová klíčová slova pro SEO | Krok 1 |
| `prompts/step1b_competitor_check.md` | Konkurenční SERP kontrola pro primární klíčová slova | Krok 1.5 |
| `evisions_tov_guide_CZ.md` | Hlas, tón, jazyk, volba slov | Krok 2 |
| `evisions_structure_guide_CZ.md` | Nadpisy, sekce, E-E-A-T, formátování | Krok 3 |
| `evisions_content_inventory.md` | Interní odkazy, mapa obsahu | Krok 3, 5 |
| `data/output/content_plan_index.md` | Dedup ledger — dohledání ID/kategorie článku podle URL, zápis chybějících Published řádků | Init |

---

## 3. Formát vstupu

```
Článek: https://www.evisions.cz/blog/[slug]/
Keywords: data/output/keywords/[slug]_keywords.xlsx
```

### Co se extrahuje z URL

| Prvek | Jak | Použito v |
|-------|-----|-----------|
| **Text článku** | WebFetch → markdown | Všechny kroky |
| **URL obrázků** | Extrakce z HTML zdroje | Init, Krok 3, Krok 4 |
| **Pozice obrázků** | Poznamenáno po kterém odstavci/H2/H3 | Init, Krok 3, Krok 4 |
| **Alt text obrázků** | Extrakce z `alt` atributu | Krok 4 |

### Mapa obrázků — POVINNÁ při inicializaci

```
## Mapa obrázků

| # | Původní pozice (po jakém nadpisu/odstavci) | URL obrázku | Alt text | Téma/kontext |
|---|---------------------------------------------|-------------|----------|---------------|
| 1 | Po H2 "Core Web Vitals", odstavec 2 | https://...cwv-graf.png | Core Web Vitals graf | Vysvětlení metrik |
```

**Pravidla:** Obrázky se drží tématu, ne pevného čísla odstavce. Pokud se obsah v Kroku 3 restrukturalizuje, obrázky se přesouvají s tématem.

### Co se extrahuje z Keywords souboru

| Sloupec | Očekávaný obsah | Povinné |
|---------|-------------------|---------|
| **Keyword** | Cílová klíčová fráze | ANO |
| **Volume (CZ)** | Objem vyhledávání → určuje prioritu | ANO |
| **KD** | Keyword difficulty | NE (reference) |
| **Notes** | Ruční pokyny pro konkrétní klíčová slova | NE |

### Priorita dle objemu (relativní)

| Priorita | Jak identifikovat | Umístění |
|----------|---------------------|----------|
| **Top klíčová slova** | Nejvyšší objem v souboru (top 3-5) | Nadpisy (H1, H2, H3), pokud to jde |
| **Sekundární** | Střední objem | Úvod, závěr, tělo textu |
| **Podpůrná** | Nižší objem | Tělo textu, kde to sedí |

---

## LOGOVACÍ POŽADAVKY

Každá změna musí být zalogována s důvodem.

### INTEGRITA LOGU — NEJKRITIČTĚJŠÍ PRAVIDLO

> **Sloupec "Original" MUSÍ být vždy zkopírován doslovně ze souboru článku v okamžiku změny.**
> NIKDY nerekonstruovat z paměti. NIKDY neparafrázovat.
>
> **Povinný proces pro každou zalogovanou změnu:**
> 1. Přečíst aktuální soubor článku (Read tool)
> 2. Najít přesnou větu/věty ke změně
> 3. Zkopírovat je doslovně do sloupce "Original"
> 4. Provést změnu
> 5. Zapsat přesnou novou verzi do sloupce "New"

### Formát logu

```
## Step [X] Log: [Název kroku]

| # | Original sentence (full) | New sentence (full) | Reason |
|---|--------------------------|----------------------|--------|
| 1 | "text před" | "text po" | [důvod dle guide] |
```

---

## 3b. Inicializace

Spouští se automaticky po zadání URL (bez potvrzení).

### Kroky

1. **Dohledat URL v `data/output/content_plan_index.md`** (ledger — viz `evisions_content_inventory.md` sekce "Dedup ledger"):
   - Nalezeno → převzít ID a kategorii, žádný zápis netřeba.
   - Nenalezeno → jde o Published článek, který ledger ještě nezná (typicky starší obsah nebo článek publikovaný mimo tento skill). Dohledat jeho ID v primárním Content Plan Index Sheetu (`mcp__claude_ai_Google_Drive__read_file_content`, viz `evisions_content_inventory.md` pro odkaz) podle URL; pokud tam ID chybí, zkusit sekundární sheet (jen pokud primární nic nemá). Pokud tam ID je, doplnit řádek do ledgeru (Edit tool, sekce "Existující obsah"). Pokud ID chybí úplně, pokračovat bez ID a na konci Init Summary na to upozornit uživatele.
2. Přečíst referenční dokumenty (ToV Guide + Structure Guide + Content Inventory)
3. Odvodit slug z URL (např. `seo-pro-e-commerce`)
4. Vytvořit složku `data/output/articles/[slug]/`, pokud neexistuje
5. Vytvořit log soubor: `data/output/articles/[slug]/article_[slug]_CZ_log.md`
6. Vytvořit keywords šablonu: `data/output/keywords/[slug]_keywords.xlsx` (pokud neexistuje) přes `src/create_keyword_xlsx.py [slug]`
7. Načíst původní článek (WebFetch URL) + vytvořit Mapu obrázků
8. Vypsat Init Summary

### Init Summary formát

```
Inicializováno: [Titulek článku]
Content Plan:   [ID z ledgeru, např. SEO-13 | CHYBÍ — nenalezeno ani v ledgeru, ani v Sheetu]
Slug:           [slug]
Kategorie:      [SEO / PPC / Social / AI & SEO / Copywriting / Konference / Marketing / evisions interní / International / Kariéra]
Složka:         data/output/articles/[slug]/
Keywords:       data/output/keywords/[slug]_keywords.xlsx [VYTVOŘENO / EXISTUJE]
Článek:         [N] slov, [N] obrázků
Obrázky:        [tabulka Mapy obrázků]

Vyplňte keywords zde: [plná absolutní cesta]
Potvrďte pro start Kroku 1.
```

---

## 4. Krok 1: Klíčová slova

### Účel
Přirozeně integrovat cílová klíčová slova do původního obsahu.

> **PRAVIDLO:** Klíčová slova pouze PŘIDÁVAT do existujícího textu. NIKDY neměnit význam ani informace.

### Pravidla integrace

1. **První zmínka = plná forma**
2. **Nikdy neměnit význam** — pokud substituce mění význam → SKIP
3. **Přirozený tok povinný** — pokud věta zní kostrbatě → SKIP
4. **Významné změny vyžadují potvrzení** — pokud klíčové slovo vyžaduje víc než drobnou úpravu, navrhnout jako PENDING, neaplikovat automaticky

### Status hodnoty

- `DONE` — změna aplikována
- `PENDING` — významná změna, čeká na potvrzení
- `SKIP` — podobný text neexistuje
- `NEW` — vyžaduje nový obsah
- `REJECTED` — navržená změna zamítnuta uživatelem

### Keywords checklist

- [ ] Klíčová slova seřazena dle objemu (sestupně)
- [ ] Top klíčová slova umístěna v nadpisech, kde to jde
- [ ] První zmínka používá plnou formu klíčového slova
- [ ] Drobné změny aplikovány přímo (DONE)
- [ ] Významné změny navrženy (PENDING)
- [ ] Žádné keyword stuffing
- [ ] Text čte přirozeně

---

## 4.5. Krok 1.5: Konkurenční SERP kontrola

**Účel:** Ověřit, zda je článek po Kroku 1 obsahově konkurenceschopný pro svá primární klíčová slova — zda pokrývá to, co dnes reálně rankuje na Google. Kompletní instrukce: `prompts/step1b_competitor_check.md`.

**Proces ve zkratce:**
1. Vyber 2-3 primární klíčová slova z keywords.xlsx (nejvyšší Volume / Priority HIGH).
2. Pro každé zavolej Ahrefs `serp-overview` (country: cz), vyber top 3-4 organické výsledky (bez placených, bez vlastní evisions.cz URL).
3. WebFetch každou vybranou URL (dedup přes klíčová slova) — extrahuj strukturu, hloubku, obsahové prvky, které náš článek nemá.
4. Vypiš stručný report mezer (tabulka: mezera → zdroj → návrh).

**STOP — volba módu** (jen pokud byly nalezeny mezery; žádné mezery = pokračuj rovnou do Kroku 2 bez dotazu):

- **Mód A — Konkurenceschopná revize:** povoluje jedinou výjimku z pravidla "žádné nové informace" v celém workflow — nové sekce/odstavce se navrhnou a vloží v Kroku 3 (viz sekce 6, "Fáze -1").
- **Mód B — Beze změny pravidla:** mezery zůstávají zaznamenané jen v logu jako doporučení, obsah workflow nedoplňuje.

> **Automatické přechody jsou zakázány stejně jako u ostatních kroků** — pokud se najdou mezery, musí uživatel explicitně zvolit A nebo B, než se pokročí do Kroku 2.

---

## 4.6. Volba modelu (před Krokem 2)

Stejný mechanismus jako u FTMO — uživatel může vybrat, který LLM generuje text.

```bash
.venv/bin/python src/model_tester.py --list
.venv/bin/python src/model_tester.py --model gpt-4o --url [URL] --keywords [xlsx]
```

Výchozí: pokud uživatel řekne "default" nebo "udělej to ty", Claude Code zpracuje vše bez API volání.

---

## 5. Krok 2: ToV Rewrite

### Účel
Upravit jazyk a tón dle ToV Guide. ŽÁDNÉ strukturní změny.

> **PRAVIDLO:** Měnit SLOVA, ne INFORMACE.

### Fáze 0: Klasifikace typu obsahu

Před přepisem klasifikovat typ článku (viz ToV Guide sekce 4):

| Typ | Tón markery |
|-----|--------------|
| **Case study** | Osobitější, silná čísla hned v úvodu, dramatický rytmus vět |
| **How-to / trend analýza** | Věcnější, krokový, TL;DR u delších textů |

> **Log requirement:** Zaznamenat klasifikaci v hlavičce Step 2 logu: `**Typ obsahu:** Case study` nebo `**Typ obsahu:** How-to`

### Co se mění

| Oblast | Příklad |
|--------|---------|
| **Volba slov** | "naprosto úžasné výsledky" → "nárůst o 90 % za rok" |
| **Struktura vět** | Kratší věty, činný rod |
| **Zakázané fráze** | Odstranit hype, vágní tvrzení (viz ToV Guide sekce 5) |

### Co zůstává stejné

Fakta, čísla, pořadí informací, klíčová slova z Kroku 1.

### Log formát (Krok 2)

```
## Step 2 Log: ToV Rewrite

**Guide:** `evisions_tov_guide_CZ.md`
**Typ obsahu:** Case study | How-to

| # | Original | Changed To | Reason |
|---|----------|------------|--------|
| 1 | "naprosto úžasné výsledky" | "nárůst o 90 % za rok" | ToV: hype bez dat → konkrétní číslo |
```

---

## 6. Krok 3: Struktura & formátování

### Účel
Aplikovat hierarchii nadpisů, E-E-A-T prvky a vizuální formátování dle Structure Guide.

### Fáze -1: Doplnění obsahových mezer — POUZE pokud byl v Kroku 1.5 zvolen Mód A

> **Toto je jediné místo v celém rewrite workflow, kde se smí přidat nová informace** — a jen pro mezery, které uživatel výslovně schválil v Kroku 1.5.

Před vším ostatním (i před Fází 0):
1. Vezmi tabulku schválených mezer z Kroku 1.5.
2. Pro každou navrhni konkrétní nový text (odstavec, sekce, případně H3) a vlož ho na logicky odpovídající místo v článku.
3. Zaloguj každou vloženou pasáž zvlášť se štítkem `NOVÝ OBSAH (Mód A)` a zdrojem/zdůvodněním (viz formát logu níže) — na rozdíl od ostatních řádků logu zde sloupec "Original" neexistuje (nic se nenahrazuje), místo něj uveď `[nový text]`.
4. Po vložení pokračuj běžnou Fází 0 (Audit odstavců) — nově vložený text podléhá stejným pravidlům délky odstavců jako zbytek článku.

Pokud byl zvolen Mód B nebo nebyly nalezeny žádné mezery, tuto fázi přeskoč beze zmínky v logu.

### Fáze 0: Audit odstavců — POVINNÁ PRVNÍ AKCE

> Před přidáním jakéhokoli formátování projít všechny odstavce a rozdělit ty nad 100 slov.

### Co se mění

| Oblast | Akce |
|--------|------|
| Nadpisy | Aplikovat H1 → H2 → H3 hierarchii |
| Odstavce | Rozdělit ty nad 100 slov |
| Callouty | Přidat Tip, Warning, Keep in Mind dle Structure Guide |
| Tabulky | Přidat srovnávací tabulky, kde existují data |
| Seznamy | Konvertovat odstavcové výčty na odrážky/číslované seznamy |
| Interní odkazy | Přidat 3-5 odkazů na související články |
| Obrázky | Aktualizovat pozice v Mapě obrázků, pokud se sekce restrukturalizovaly |

### Limity dle délky článku

| Délka | Callouty | Tabulky | Seznamy |
|-------|----------|---------|---------|
| Krátký (<1000 slov) | 1-2 | 1 | 1-2 |
| Střední (1000-2000 slov) | 2-3 | 1-2 | 2-3 |
| Dlouhý (>2000 slov) | 3-4 | 2-3 | 3-4 |

---

## 7. Krok 4: HTML konverze

### Účel
Konverze markdown do stylovaného HTML pomocí evisions.cz šablony.

```bash
.venv/bin/python -c "
from pathlib import Path
from src.step4_html import convert_to_html
md = Path('data/output/articles/[slug]/article_[slug]_CZ.md').read_text(encoding='utf-8')
convert_to_html(md, '[slug]', Path('data/output/articles/[slug]/'))
"
.venv/bin/python src/export_article_docx.py data/output/articles/[slug]/article_[slug]_CZ.md
```

Druhý příkaz generuje `article_[slug]_CZ.docx` — čitelný Word export článku (ne HTML, žádná hlavička/patička/CSS šablony). Není volitelný, generuje se automaticky hned po HTML, stejně jako u Write Workflow.

### Pravidla umístění obrázků

Stejná jako u FTMO: obrázky se drží svého tématu (dle Mapy obrázků), `<figure class="article-image">` s `<figcaption>`, `loading="lazy"`, alt text popisný.

---

## 8. Krok 5: QA & revize

### QA Checklist

**Přesnost obsahu**
- [ ] Všechna fakta odpovídají zdroji
- [ ] Žádné informace nepřidány ani neodebrány
- [ ] Odkazy fungují
- [ ] Obrázky na správných pozicích

**ToV compliance**
- [ ] Tón odpovídá ToV Guide (case study vs. how-to)
- [ ] Žádné zakázané fráze
- [ ] Žádné garance konkrétních výsledků

**Structure compliance**
- [ ] E-E-A-T prvky přítomny (autor, zdroje, datum)
- [ ] Hierarchie nadpisů správná
- [ ] Interní odkazy přítomny

**Technické**
- [ ] HTML se správně renderuje
- [ ] Obrázky se načítají
- [ ] Žádné nefunkční odkazy

---

## 9. Konvence pojmenování souborů

```
article_[slug]_CZ.md           # Finální markdown
article_[slug]_CZ_log.md       # Edit log (všechny kroky)
article_[slug]_CZ_log.html     # Log vyrenderovaný s diff barvami
article_[slug]_CZ.html         # Finální HTML článek
article_[slug]_CZ.docx         # Krok 4: čitelný Word export článku (automatický)
[slug]_keywords.xlsx           # Keywords soubor
```

### Export logu do HTML

```bash
.venv/bin/python src/generate_log.py data/output/articles/[slug]/article_[slug]_CZ_log.md
```

---

## 10. Rychlá reference

1. **Aplikovat klíčová slova** — přirozená integrace (Krok 1)
2. **Konkurenční SERP kontrola** — report mezer, volba Módu A/B (Krok 1.5)
3. **Aplikovat ToV** — pouze úprava jazyka (Krok 2)
4. **Aplikovat strukturu a formátování** — nadpisy, meta prvky, případné schválené doplnění obsahu (Krok 3)
5. **Konverze do HTML** (Krok 4)
6. **QA revize** — finální kontrola (Krok 5)

> **Klíčový princip:** Zachovat fakta, transformovat prezentaci.

---

## Document History

| Verze | Datum | Změny |
|-------|-------|-------|
| 1.0 | 2026-07-10 | První verze, adaptováno z FTMO Academy workflow |
| 1.1 | 2026-08-18 | Init doplněn o dohledání/doplnění ID v `data/output/content_plan_index.md` (ledger), aby zůstal v souladu s Content Plan Sheetem i pro rewrite flow |
| 1.2 | 2026-09-01 | Přidán Krok 1.5 (Konkurenční SERP kontrola) — lehká verze konkurenčního researche pro 2-3 primární klíčová slova (Ahrefs `serp-overview` + WebFetch top 3-4 konkurentů), s volbou Módu A (konkurenceschopná revize — jediná povolená výjimka z "žádné nové informace", řeší ji nová Fáze -1 v Kroku 3) nebo Módu B (beze změny pravidla, mezery jen zalogovány). Nový prompt `prompts/step1b_competitor_check.md` |

---

*Companion document: [evisions.cz Write Workflow](evisions_write_workflow_CZ.md) — pro nové články*
