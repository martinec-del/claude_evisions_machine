# evisions.cz Blog: New Article Writing Workflow

**Verze:** 1.0
**Vytvořeno:** 2026-07-10
**Účel:** Krok-za-krokem proces pro psaní nových článků na evisions.cz blog od nuly

---

## 1. Přehled workflow

```
VSTUP                          PROCES                                     VÝSTUP
─────                          ──────                                     ──────
Téma / řádek v Content Plan →  INIT: Načíst reference, log soubor    →   Init Summary + log
                            →  Krok 1: Konkurenční research + KW     →   [slug]_step1.xlsx
                            →  Krok 2: Brief & osnova                →   [slug]_outline.docx
                            →  Krok 3: Psaní draftu                  →   Plný draft + zdroje
                            →  Krok 4: ToV kontrola                  →   Opravený draft
                            →  Krok 5: Struktura & formátování       →   Formátovaný markdown
                            →  Krok 6: HTML konverze                 →   article_[slug]_CZ.html + .docx
                            →  Krok 7: QA + aktualizace Content Plan →   FINÁLNÍ SOUBORY
```

### Základní princip: Tvořit, ne kompilovat

> **KRITICKÉ:** Každý článek na evisions.cz blogu musí být originální a psaný v evisions ToV od první věty.
>
> Tento workflow NENÍ:
> - Shrnutí konkurenčního obsahu
> - SEO brief plný klíčových slov bez struktury
> - Neutrální draft, který se "opraví později"
>
> Tento workflow JE:
> - Research-informed originální psaní
> - evisions ToV aplikovaný od Kroku 3
> - Strukturovaný proces s jedním schvalovacím bodem na krok

**Co konkurenční research informuje:** rozsah tématu, vzory struktury, content gaps, sadu klíčových slov
**Co nedělá:** neposkytuje zdrojový text — to by byl plagiát

---

## 2. Vztah k Edit Workflow

| | Edit Workflow (`/evisions-rewrite-article`) | Write Workflow (`/evisions-new-article`) |
|--|---|---|
| **Vstup** | Existující článek na blogu | Článek zatím neexistuje |
| **Základní princip** | Zachovat obsah, vylepšit prezentaci | Vytvořit originální obsah v evisions ToV |
| **Krok 1** | Klíčová slova (integrace do textu) | Konkurenční research + objevování klíčových slov |
| **Krok 2** | ToV rewrite | Brief & osnova (architektura) |
| **Krok 3** | Struktura & formátování | Psaní draftu (originální text) |
| **Krok 4** | HTML | ToV kontrola (ověření, ne přepis) |
| **Krok 5** | QA | Struktura & formátování |
| **Krok 6** | — | HTML |
| **Krok 7** | — | QA + aktualizace Content Plan |

---

## 3. Referenční dokumenty

| Dokument | Použito v |
|----------|-----------|
| `evisions_tov_guide_CZ.md` | Init, Krok 3, Krok 4 |
| `evisions_structure_guide_CZ.md` | Init, Krok 2, Krok 5 |
| `evisions_content_inventory.md` | Init, Krok 2 |
| `data/output/content_plan_index.md` | Krok 0 (Duplicate Check & ID přiřazení), Krok 7 |
| `prompts/write_step1_research.md` | Krok 1 |
| `prompts/write_step2_brief.md` | Krok 2 |
| `prompts/write_step3_draft.md` | Krok 3 |
| `prompts/write_step4_tov_check.md` | Krok 4 |
| `prompts/step3_structure.md` | Krok 5 |
| `prompts/step4_html.md` | Krok 6 |

---

## 4. Vstupní identifikace — Content Plan řádek

> **"Google Sheet" v tomto dokumentu vždy znamená primární Content Plan Index Sheet** (viz `evisions_content_inventory.md` — sekundární sheet se čte jen na výslovnou žádost uživatele).

Každý článek má řádek v Google Sheet Content Plánu, identifikovaný **ID** (kategorie-prefix + číslo, např. `SEO-30`). To zabraňuje záměně podobně pojmenovaných článků.

**Přijímané formáty vstupu:**
- Pouze ID: `/evisions-new-article SEO-30` — vyhledá v Content Plan Sheetu / lokálním ledgeru
- Téma: `/evisions-new-article "SEO pro e-commerce"` — hledá podle názvu (upozorní při nejednoznačnosti)
- Bez vstupu: zobrazí interaktivní menu

Pokud řádek v Content Plánu neexistuje, pokračovat na **Duplicate Check** níže — teprve po něm se rozhodne, zda jde skutečně o nový článek.

---

## 5. Inicializace

Spouští se automaticky. Bez potvrzení uživatele — **kromě Duplicate Check kroku 2, který může vyžádat rozhodnutí uživatele.**

### Krok 0 — Duplicate Check & ID přiřazení (POVINNÉ, před vším ostatním)

> **Proč:** Google Drive MCP umí Content Plan Sheet jen číst, ne zapisovat. `data/output/content_plan_index.md` je proto lokální ledger existujícího + plánovaného obsahu a zdroj pravdy pro přiřazování ID. Tento krok zabraňuje vytvoření duplicitního článku k tématu, které už je Published nebo už je v Sheetu jako TODO.

1. **Přečíst `data/output/content_plan_index.md`.** Pokud soubor neexistuje nebo je uživatelem označen za zastaralý, přegenerovat ho: přečíst celý Content Plan Sheet přes `mcp__claude_ai_Google_Drive__read_file_content` a projít i lokální složky v `data/output/articles/`, pak přepsat ledger stejnou strukturou (Next ID tabulka, Existující obsah per kategorie, TODO témata, lokální složky, anomálie).
2. **Porovnat zadané téma/klíčové slovo/ID uživatele** proti ledgeru:
   - **Shoda na ID nebo URL v sekci "Existující obsah (Published)"** → článek už existuje. STOP, informovat uživatele a nabídnout `/evisions-rewrite-article [URL]` místo pokračování zde.
   - **Shoda na tématu v sekci "TODO / plánovaná témata"** (stejné nebo silně překrývající se primární klíčové slovo/téma) → téma už je v plánu pod konkrétní Skupinou/kategorií. Pokračovat pod tímto zařazením, ne jako nezávislá nová položka — a upozornit uživatele, pokud řádek má nějakou poznámku (např. už vyplněnou URL — možný náznak, že článek fakticky existuje, jen chybí ID/Status v Sheetu).
   - **Žádná shoda** → skutečně nové téma, pokračovat na přiřazení ID.
   - Při nejednoznačné/částečné shodě: krátce shrnout nalezenou shodu a zeptat se uživatele (AskUserQuestion), zda pokračovat jako REWRITE, jako záměrně odlišný NOVÝ úhel, nebo zrušit.
3. **Přiřadit ID** (jen pokud krok 2 potvrdil skutečně nové téma a Content Plan řádek žádné ID nemá): vzít hodnotu z tabulky "Next ID per kategorie" v ledgeru pro danou kategorii, zapsat ji do ledgeru (nová řádka v "Existující obsah" se Status "In Progress" + zvýšit "Next ID" o 1 pro danou kategorii — Edit tool).
4. **Regenerovat xlsx mirror:** spustit `.venv/Scripts/python.exe src/generate_content_plan_xlsx.py` (přečte aktualizovaný ledger a přepíše `data/output/content_plan_index.xlsx` — nový/změněný řádek bude zeleně zvýrazněný).
5. **Vypsat řádek k ručnímu vložení do Google Sheetu** (protože MCP tam zapsat neumí) — přesně ve formátu sloupců Sheetu: ID, Kapitola/Nadpis, Typ obsahu, klíčová slova, složka s výstupy, Status. Zobrazit ho jako součást Init Summary, ne skrytě, a odkázat uživatele na zvýrazněný řádek v `data/output/content_plan_index.xlsx` pro vizuální kontrolu.

### Akce (po Duplicate Check)

1. Přečíst referenční dokumenty: ToV Guide, Structure Guide, Content Inventory
2. Vyhledat/potvrdit řádek v Content Plan Google Sheetu (Kategorie, Klíčové slovo, Typ obsahu)
3. Určit režim:
   - **NEW:** Zkontrolovat existující soubory v `data/output/articles/[slug]/`. Pokud existují, určit další verzi (v2, v3…), nikdy nepřepisovat. Vytvořit log soubor. Pokračovat na Krok 1.
   - **CONTINUE:** Auto-detekce posledního dokončeného kroku dle existujících souborů (stejná logika jako u FTMO — viz tabulka níže).
4. Vypsat Init Summary

### CONTINUE — auto-detekce

| Nalezené soubory | Poslední dokončený krok | Pokračovat od |
|--------------------|----------------------------|-----------------|
| Jen `_log.md` | INIT | Krok 1 |
| `_step1.xlsx` | Krok 1 | Krok 2 |
| `_outline.docx` | Krok 2 | Krok 3 |
| `_CZ.md` (draft, bez HTML) | Krok 3-5 (dle logu) | Další nedokončený krok |
| `_CZ.html` + `_log.html` | Krok 6 | Krok 7 |

### Init Summary formát (NEW)

```
Téma:          [Název článku]
Duplicate Check: OK — žádná shoda v content_plan_index.md | Shoda nalezena, viz níže
Content Plan:  [ID — nově přiřazené nebo existující, např. SEO-30]
Kategorie:     [SEO / PPC / Social / AI & SEO / Copywriting / Konference / Marketing / evisions interní / International / Kariéra]
Slug:          [article-slug]
Existující ver.: Žádná | [soubor] — vytvoří se vN+1

--- Vlož ručně do Content Plan Sheetu (řádek v odpovídající kategorii) ---
ID: [SEO-30]  |  Kapitola/Nadpis: [téma]  |  Typ obsahu: nový text - lekce
klíčová slova: [doplní se v Kroku 1]  |  složka s výstupy: data/output/articles/[slug]/
Status: In Progress
---

Keywords: načteno v Kroku 1

Potvrďte pro start Kroku 1 (Konkurenční research + objevování klíčových slov).
```

---

## 6. Krok 1 — Konkurenční research + objevování klíčových slov

**Prompt:** `prompts/write_step1_research.md`

### Účel
Pochopit konkurenční prostředí před psaním. Zúžit rozsah tématu. Sestavit sadu klíčových slov.

### Krok 0: Volba providera

1. **Primární — Ahrefs MCP.** Tento projekt má Ahrefs MCP připojené (`mcp__claude_ai_Ahrefs__*` nástroje). Použít jako výchozí zdroj metrik a keyword discovery.
2. **Fallback — WebSearch + WebFetch.** Pokud Ahrefs MCP není dostupné, použít built-in WebSearch/WebFetch (funguje vždy, bez API klíče).
3. **Doplňkový — Marketing Miner.** `src/marketing_miner_api.py` — CZ/SK-laděný cross-check volume dat pro top keywordy + záložní zdroj nápadů, pokud Ahrefs nemá dost CZ pokrytí. Není náhrada Ahrefs, jen druhé mínění. Detailní postup viz `prompts/write_step1_research.md` krok 5.5.

### Krok 1: Ověření seed klíčového slova

1. Ověřit hlavní seed keyword pro dané téma (WebSearch: `"[téma] marketing"` nebo `"[téma] SEO"`)
2. Potvrdit nebo upravit seed dle skutečného použití v oboru

### Krok 2: WebSearch — 4 dotazy, 6 URL každý

1. Spustit 4 WebSearch dotazy s variacemi seed klíčového slova:
   - `"[seed] vysvětleno"` — obecný
   - `"[seed] návod"` — edukativní úhel
   - `"jak na [seed]"` — praktický úhel
   - téma-specifický úhel (přizpůsobit tématu)
2. Z každého dotazu vybrat top 6 URL
3. Deduplikace + filtr: vynechat fóra, placený obsah, ne-CZ stránky (pokud nejde o mezinárodní téma)

### Krok 3: Obohatit URL metrikami (Ahrefs)

Pro všechny URL zavolat:
- `mcp__claude_ai_Ahrefs__site-explorer-metrics` → organický traffic URL
- `mcp__claude_ai_Ahrefs__site-explorer-domain-rating` → Domain Rating domény

### Krok 4: Vybrat top 10 a extrahovat obsah

Fetch top 10 URL dle relevance > DR > traffic. Extrahovat: H1, H2/H3 strukturu, pokryté/chybějící témata, hloubku, formáty (tabulky, srovnání), unikátní úhel.

**Timeout:** 30s na WebFetch, jinak přeskočit a logovat jako timeout.

### Krok 5: Objevování klíčových slov

```
mcp__claude_ai_Ahrefs__keywords-explorer-matching-terms
mcp__claude_ai_Ahrefs__keywords-explorer-related-terms
```

Seed = hlavní keyword + 2-3 doplňkové seedy odvozené z H2 nadpisů konkurence.

### Krok 6: Merge + dedup + filtr + clustering

Sloučit klíčová slova z Ahrefs + témata z H2/H3 konkurence. Odstranit duplicity, mimo-oborová slova. Seřadit dle objemu.

### Krok 7: Generovat xlsx

Uložit jako `data/output/articles/[slug]/[slug]_step1.xlsx`:

**List "URLs":** `# | URL | Zdroj dotazu | DR | Organic Traffic | Stav fetch | H1 | Klíčová témata | Content gap | Počet slov`

**List "Keywords":** `# | Keyword | Volume | KD | Cluster | Status | Notes`

### Stop podmínka

> **Krok 1 dokončen.** [N] URL nasbíráno, [N] úspěšně fetchnuto. [N] klíčových slov navrženo.
> Klíčový content gap: [věta].
> **xlsx uložen:** `[plná absolutní cesta]`
> Zkontrolujte URL a klíčová slova → potvrďte pro Krok 2.

---

## 7. Krok 2 — Brief & osnova

**Prompt:** `prompts/write_step2_brief.md`

### Akce (v pořadí)

1. Klasifikovat typ: Case study nebo How-to/trend analýza (viz ToV Guide sekce 4)
2. Určit cílový počet slov (dle konkurenčního průměru + složitosti tématu)
3. Popsat diferenciaci od konkurence (co evisions dělá jinak)
4. Namapovat top 3-5 klíčových slov na H1/H2 nadpisy
5. Napsat plnou kostru nadpisů s klíčovými body, callouty a tabulkami na sekci
6. Naplánovat interní odkazy (3-5 minimum z Content Inventory)
7. Content validace (marketingový expert review)

### Content validace — kontrolní otázky

- Odpovídá struktura logicky tématu?
- Jsou přítomny všechny klíčové koncepty pro daný typ obsahu?
- Je pořadí sekcí didakticky správné?
- Chybí koncepty, které by čtenář očekával?

### Výstup — dva artefakty

**1. Outline soubor (.docx):**

```bash
.venv/bin/python src/export_outline_docx.py data/output/articles/[slug]/article_[slug]_CZ_outline.md
```

**2. Log soubor** — append Step 2 sekce do `article_[slug]_CZ_log.md`

### Stop podmínka

> **Krok 2 dokončen.** Osnova pro "[Titulek]" — [Case study/How-to], ~[N] slov.
> **Osnova uložena:** `[plná absolutní cesta k .docx]`
> Zkontrolujte → schvalte → pokračujte na Krok 3.

**Nezačínat psát draft, dokud osnova není schválena.**

---

## 8. Krok 3 — Psaní draftu

**Prompt:** `prompts/write_step3_draft.md`

### Základní omezení

1. **Sledovat schválenou osnovu.** Každé H2 a H3 se musí objevit.
2. **evisions ToV od první věty.** Žádný neutrální draft.
3. **Přirozeně integrovat klíčová slova** — sekundární priorita, ne checklist.
4. **Respektovat typ obsahu** (case study vs. how-to — viz ToV Guide sekce 4).
5. **Dodržet cílový počet slov.**

### Rytmus psaní

**Vzor:** Krátké tvrzení → střední vysvětlení s konkrétními čísly → krátký závěr/přechod.

```
Příklad:
"Organická návštěvnost vzrostla o 700 % za 30 měsíců. Klíčem byla
přepracovaná obsahová strategie postavená na analýze klíčových slov
a konkurence. Výsledek se ukázal jako stabilní, ne sezónní výkyv."
```

### Bez omáčky — rovnou k věci

Viz ToV Guide sekce 5 — stejná pravidla platí i pro draft.

### Step 3 Log

```markdown
## Step 3 — Draft

**Typ obsahu:** Case study | How-to
**Počet slov:** [N] (cíl: [N–N])

### Integrace klíčových slov

| # | Keyword | Volume | Umístění | Kontextová věta |
|---|---------|--------|-----------|-------------------|

### Odchylky od osnovy

| # | Typ | Popis | Důvod |
|---|-----|-------|--------|

### Plný článek se zdroji

Každé faktické tvrzení následováno zdrojem v hranaté závorce.
```

### Stop podmínka

> **Krok 3 dokončen.** Draft: "[Titulek]" — [N] slov.
> Zkontrolujte draft → schvalte nebo požádejte o úpravy → pokračujte na Krok 4.

---

## 9. Krok 4 — ToV kontrola

**Prompt:** `prompts/write_step4_tov_check.md`

Lehká verifikace, ne přepis. Kontroluje: otevření sekcí, rytmus vět, filler fráze, casual markery, hype jazyk, vágní tvrzení bez čísel.

### Stop podmínka

> **Krok 4 dokončen.** [N] problémů nalezeno a opraveno.
> Zkontrolujte opravy → schvalte → pokračujte na Krok 5.

---

## 10. Krok 5 — Struktura & formátování

**Prompt:** `prompts/step3_structure.md`

Stejná pravidla jako v Edit Workflow Kroku 3 (`evisions_workflow_CZ.md`) — povinný audit odstavců jako první akce, pak nadpisy, callouty, tabulky, seznamy.

### Stop podmínka

> **Krok 5 dokončen.** Formátovaný článek připraven.
> Schvalte → pokračujte na Krok 6 (HTML).

---

## 11. Krok 6 — HTML konverze

**Prompt:** `prompts/step4_html.md`

Generuje se současně:
1. `article_[slug]_CZ.html` — finální HTML článku
2. `article_[slug]_CZ_log.html` — stylovaný log
3. `article_[slug]_CZ.docx` — čitelný Word export článku (ne HTML, ne osnova z Kroku 2)

Použít `src/step4_html.py` (evisions.cz šablona) pro HTML, hned poté `src/export_article_docx.py` pro docx — viz `prompts/step4_html.md` sekce "Docx export". Není to volitelný doplněk, generuje se automaticky při každém běhu Kroku 6.

### Stop podmínka

> **Krok 6 dokončen.** HTML připraveno k revizi. Oba soubory uloženy.
> Schvalte → pokračujte na Krok 7 (QA).

---

## 12. Krok 7 — QA + aktualizace Content Plan

### Content validace — marketingový expert review

- [ ] Všechna fakta technicky přesná
- [ ] Žádné zjednodušení, které by čtenáře zmátlo
- [ ] Koncepty vysvětleny ve správném pořadí
- [ ] Příklady realistické a relevantní
- [ ] Nic nechybí, co by čtenář v tématu očekával

### QA Checklist

Stejný checklist jako v Edit Workflow Kroku 5 (`evisions_workflow_CZ.md` sekce 8), plus:
- [ ] Zdrojové citace u všech faktických tvrzení
- [ ] Žádné [SOURCE NEEDED] značky zbylé

### Soubory k uložení — všech 5 povinných

- [ ] `data/output/articles/[slug]/article_[slug]_CZ[_vN].md`
- [ ] `data/output/articles/[slug]/article_[slug]_CZ[_vN]_log.md`
- [ ] `data/output/articles/[slug]/article_[slug]_CZ[_vN].html`
- [ ] `data/output/articles/[slug]/article_[slug]_CZ[_vN]_log.html`
- [ ] `data/output/articles/[slug]/article_[slug]_CZ[_vN].docx` (vygenerováno v Kroku 6, ne ručně)

### Aktualizace Content Plan Sheetu a lokálního ledgeru

1. **Lokální ledger** (`data/output/content_plan_index.md`): přesunout řádek article ID ze stavu "In Progress" na "Published", doplnit URL (po skutečném publikování na web) — Edit tool, okamžitě.
2. **Regenerovat xlsx mirror:** `.venv/Scripts/python.exe src/generate_content_plan_xlsx.py`.
3. **Google Sheet:** vypsat uživateli hotový řádek k ručnímu vložení/aktualizaci (ID, Status → Published, URL) — MCP zápis do Sheetu neumí, totéž jako u přiřazení ID v Kroku 0.

### Stop podmínka

> **Krok 7 dokončen.** QA: [PASS / FAIL].
> Soubory uloženy: 4/4.
> Lokální ledger aktualizován: Status → Published.
> **Vlož ručně do Content Plan Sheetu:** ID [X] → Status: Published, URL: [živá URL].

---

## 13. Integrita logu — bez výjimek

Stejné pravidlo jako v Edit Workflow: originál se vždy čte ze souboru, nikdy z paměti.

---

## 14. Konvence pojmenování

```
[slug]_step1.xlsx                       # Krok 1: URL + klíčová slova
article_[slug]_CZ_outline.docx          # Krok 2: Brief + osnova
article_[slug]_CZ.md                    # Finální markdown
article_[slug]_CZ_log.md                # Write log (všechny kroky)
article_[slug]_CZ.html                  # Finální HTML
article_[slug]_CZ_log.html              # Log HTML
article_[slug]_CZ.docx                  # Krok 6: čitelný Word export článku (automatický)
```

> **Pozor na jméno:** `article_[slug]_CZ_outline.docx` (Krok 2, osnova) a `article_[slug]_CZ.docx` (Krok 6, hotový článek) jsou dva různé soubory ve stejné složce — nezaměňovat ani nepřepisovat jeden druhým.

Slugy používají pomlčky: `seo-pro-e-commerce`, ne `seo_pro_e_commerce`.

---

## 15. Pravidlo potvrzení kroku

> **Každý krok končí STOPEM.**
> Po výstupu každého kroku počkat na výslovné potvrzení uživatele ("ok", "pokračuj", "schváleno").
> Automatické přechody mezi kroky jsou zakázány.

---

## Document History

| Verze | Datum | Změny |
|-------|-------|-------|
| 1.0 | 2026-07-10 | První verze, adaptováno z FTMO Academy write workflow |
| 1.1 | 2026-08-18 | Přidán Krok 0 — Duplicate Check & ID přiřazení proti `data/output/content_plan_index.md` (lokální ledger, protože Google Drive MCP Sheet jen čte, nezapisuje) |

---

*Companion document: [evisions.cz Edit Workflow](evisions_workflow_CZ.md) — pro existující články*
*Reference: [ToV Guide](evisions_tov_guide_CZ.md) | [Structure Guide](evisions_structure_guide_CZ.md)*
