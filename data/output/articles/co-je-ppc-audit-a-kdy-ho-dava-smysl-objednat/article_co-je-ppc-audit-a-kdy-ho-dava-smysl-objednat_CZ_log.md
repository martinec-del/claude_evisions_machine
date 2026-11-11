# Log: Co je PPC audit a kdy ho dává smysl objednat

**Slug:** co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat
**Content Plan:** PPC-15 — Kategorie: PPC, nová podskupina "10 – PPC audit" (lead-opportunity podpora pro landing page)
**Content Plan zdroj:** data/output/content_plan_index.md (lokální dedup ledger), primární Sheet https://docs.google.com/spreadsheets/d/1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q
**Typ obsahu:** Informační / edukativní s komerčním přesahem (lead-gen podpora pro /ppc-audit/)
**Vytvořeno:** 2026-08-27

## Init

**Zdroj zadání:** uživatelská lead-opportunity analýza landing page https://www.evisions.cz/ppc-audit/ (SERP na "ppc audit" míchá informační a komerční výsledky → prostor pro podpůrný článek bez kanibalizace LP; LP se v Google zobrazuje na 2. straně výsledků, cíl je posunout ji na 1. stranu společně s článkem přes interní prolinkování).

**Duplicate Check (Krok 0):** OK — žádná shoda v `data/output/content_plan_index.md` (Published ani TODO). Nové téma, přiřazeno ID PPC-15, nová Skupina 10 "PPC audit".

**Zadaná klíčová slova (Ahrefs / Marketing Miner volume):**
- ppc audit: 600 / 230
- audit ppc: 90 / 70
- ppc audit zdarma: — / 50
- ppc audity: — / 60
- audit ppc účtu: 100 / —
- audit ppc: — / 30, 20
- ppc audit report: 20 / 20

**Požadavky na obsah (z lead-opportunity akčního plánu):**
1. Vysvětlit co PPC audit je, kdy dává smysl, co odhaluje — primárně informační intent, LP až sekundárně.
2. Přirozené CTA v těle + na konci na https://www.evisions.cz/ppc-audit/.
3. 1–2 průběžná CTA (např. po přínosech auditu, po "kdy audit dává smysl") + sekce "jak k auditu přistupujeme v evisions". Pozor na CTA link density — jeden odkaz na CTA moment, needitovat stejnou URL 2× v sousedních větách ([[evisions_cta_link_density_feedback]]).
4. Interní prolinkování na relevantní PPC služby/obsah, 2–4 odkazy (LB standard).
5. Zvážit FAQ sekci (long-tail: jak často dělat PPC audit, co výstup obsahuje, kolik trvá audit).
6. Landing page /ppc-audit/ se needituje v rámci tohoto zadání — pouze nový článek.

**Kandidáti na interní prolinkování (stejná kategorie PPC, k ověření v Kroku 1/2):**
- PPC-14 — Koeficient sezónnosti — https://www.evisions.cz/blog/koeficient-sezonnosti-jak-se-bude-vas-obrat-vyvijet-v-jednotlivych-mesicich/
- PPC-09 — Co je Google Consent Mode V2 a musíte to řešit? — https://www.evisions.cz/blog/co-je-google-consent-mode-v2-a-musite-to-resit/
- PPC-04 — Jak spolu souvisí budování značky a výkonnostní marketing? — https://www.evisions.cz/blog/jak-spolu-souvisi-budovani-znacky-a-vykonnostni-marketing/
- SEO-06 — Synergie PPC a SEO: Klíč k digitálnímu úspěchu? — https://www.evisions.cz/blog/synergie-ppc-a-seo-klic-k-digitalnimu-uspechu/

## Step 1 — Konkurenční research + klíčová slova

**Seed keyword:** "ppc audit" (mixed informational/commercial intent podle Ahrefs `intents`)

**Provider:** Ahrefs MCP (`serp-overview` pro "ppc audit" cz, `keywords-explorer-matching-terms`, `keywords-explorer-related-terms`) + WebFetch top výsledků. Marketing Miner CZ cross-check (`src/marketing_miner_api.py volume`).

**Adaptace postupu:** místo standardních 4 WebSearch dotazů ("vysvětleno"/"návod"/"jak na"/téma-specifický) byl použit přímo Ahrefs `serp-overview` pro přesný komerční+informační keyword "ppc audit" — SERP je u tohoto dotazu úzce specifický (mix service pages a glosářů), obecné WebSearch varianty by přinesly hodně duplicitních/irelevantních výsledků. Tento research byl navíc sdílený s paralelním úkolem — analýzou konkurence pro doporučení k landing page `/ppc-audit/` (viz `data/output/lead-opportunities/ppc_audit_landing_page_recommendations_CZ.md`), aby se stejná data nesbírala dvakrát.

**URL research:** 7 URL z TOP 10 SERPu pro "ppc audit" (cz) fetchnuto/analyzováno, 1 (adsvantage.cz, nižší DR/traffic) přeskočeno. Podrobnosti viz `co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat_step1.xlsx`, list "URLs".

**Klíčový content gap:** Žádný informační/edukativní konkurenční výsledek nepokrývá "kdy PPC audit **nedává** smysl" — tento úhel má jen jedna service page (zaklik.cz, DR27). Silný diferenciátor a E-E-A-T signál pro nový článek. Zároveň nikdo z informačního obsahu nejde do hloubky srovnáním metod auditu (nástroj / self-audit / peer review / externí agentura) tak jako zaklik.cz na service page — prostor to zpracovat edukativně v článku.

**SERP featury:** "ppc audit" má AI Overview + AI Overview sitelinks (feo.cz, grou.cz, marf.cz aj.) — strukturovaný obsah s jasnými H2/Q&A pomáhá i do AI Overview zobrazení.

**Klíčová slova:** 11 navrženo (viz xlsx list "Keywords") — primární "ppc audit" (Ahrefs 600 / MM 230), sekundární varianty "audit ppc" (90/70), "audit ppc kampaní" (350/20 — **řádový rozdíl, MM konzervativnější**), "audit ppc účtů" (250, bez MM dat), "audit ppc účtu" (100/10 — řádový rozdíl), FAQ/long-tail "ppc audit zdarma" (50/50), "ppc audit report" (30/20), "ppc audit checklist" (10). Vyloučeno: "audit ppc kampaní praha" (lokální intent, mimo scope), "co je ppc" (250 — mention-only, riziko kanibalizace s případným samostatným článkem "Co je PPC").

**xlsx uložen:** `data/output/articles/co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat/co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat_step1.xlsx`

## Step 2 — Brief & osnova

**Typ obsahu:** How-to / edukativní (ne case study) — informační intent s komerčním přesahem, viz ToV Guide sekce 4/5.

**Cíl:** 1500–1800 slov.

**Diferenciace:** sekce "Kdy PPC audit nedává smysl" (nikdo v informačním TOP 10 nemá), srovnání 4 metod auditu (nástroj/self-audit/peer review/externí), krátká sekce "Jak k auditu přistupujeme v evisions". Vynecháno záměrně (patří na LP `/ppc-audit/`, ne do článku): cenové tiery, detailní deliverables formát, krokový proces objednávky — rozdělení koordinováno s `data/output/lead-opportunities/ppc_audit_landing_page_recommendations_CZ.md` sekce 4.

**Kostra:** Úvod (HOOK+TL;DR) → Co je PPC audit → Co kontroluje → Jak probíhá (4 metody) → Kdy dává smysl (CTA #1) → Kdy nedává smysl → Co je výstupem → Jak k auditu přistupujeme v evisions (CTA #2, case study Nefertiti) → FAQ → Klíčové závěry (CTA #3/závěrečné) → Zdroje.

**Interní odkazy (5):** `/ppc-audit/` ×2 (CTA po "kdy dává smysl" + závěrečné, různá formulace), PPC-13 (case study Nefertiti +150 % tržeb), PPC-09 (Consent Mode V2, u měření/trackingu), SEO-06 (Synergie PPC a SEO, volitelně kontext).

**Content validace:** Pass. Flagged: sekce "co audit kontroluje" zůstat čistě v PPC rovině, neprohlubovat do technického SEO (riziko okrajového přesahu k připravovaným SEO content-gap článkům, samo o sobě bez kanibalizace).

**Osnova uložena:** `data/output/articles/co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat/article_co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat_CZ_outline.docx`

## Step 3 — Draft

**Typ obsahu:** How-to / edukativní
**Počet slov:** ~1475 (cíl: 1500–1800; v rámci tolerance)

### Integrace klíčových slov

| # | Keyword | Volume (Ahrefs/MM) | Umístění | Kontextová věta |
|---|---------|--------|-----------|-------------------|
| 1 | ppc audit | 600/230 | H1 + úvod/TL;DR | "Co je PPC audit a kdy ho dává smysl objednat" |
| 2 | audit ppc | 90/70 | H2 "Co PPC audit konkrétně kontroluje" | "Audit ppc účtu se obvykle neomezuje na jednu kampaň..." |
| 3 | audit ppc kampaní | 350/20 | H2 "Jak probíhá PPC audit" | "V praxi audit ppc kampaní odhalí nejčastěji kombinaci menších problémů..." |
| 4 | audit ppc účtu/účtů | 100/10, 250/— | H2 "Co PPC audit konkrétně kontroluje" (úvod) | "Audit ppc účtu se obvykle neomezuje na jednu kampaň..." |
| 5 | ppc audit zdarma | —/50 | FAQ | "Je možné získat PPC audit zdarma?" |
| 6 | ppc audit report | 30/20 | H2 "Co je výstupem PPC auditu" + FAQ | "Co konkrétně obsahuje report z PPC auditu?" |

### Odchylky od osnovy

| # | Typ | Popis | Důvod |
|---|-----|-------|--------|
| 1 | Doplnění | Přidána 5. FAQ otázka "Jak dlouho PPC audit trvá?" nad rámec 4 otázek z osnovy | Explicitní požadavek z původního zadání uživatele ("kolik trvá audit" byl součástí navrhované FAQ v lead-opportunity akčním plánu), posiluje long-tail pokrytí bez rizika kanibalizace s LP (obecná odpověď, ne konkrétní SLA naší služby) |
| 2 | Rozšíření | Draft dosáhl 1475 slov místo cílových 1500–1800 (těsně pod dolní hranicí) | Osnova dodržena strukturně beze zbytku; další umělé natahování by šlo proti "bez omáčky" principu ToV — ponecháno k rozhodnutí uživatele, zda doplnit další sekci, nebo nechat v aktuálním rozsahu |

Ostatní: osnova dodržena přesně — všechny H2 ze schváleného briefu se objevují ve stejném pořadí, žádné téma vyhrazené pro landing page (ceny, deliverables formát, proces objednávky) do článku nepronikly.

### Zdrojové citace

| # | Tvrzení | Zdroj |
|---|---------|-------|
| 1 | Nárůst tržeb o téměř 150 % za 9 měsíců u klienta Nefertiti | Interní reporting evisions, publikovaná case study PPC-13 (https://www.evisions.cz/blog/spoluprace-e-visions-a-nefertitis-za-9-mesicu-zvyseni-trzeb-na-temer-150-diky-ppc/) |

Ostatní tvrzení v článku jsou obecné odborné znalosti/interpretace (principy PPC auditu, typické nálezy) a dle Kroku 3 pravidel nevyžadují externí zdroj. Žádné tvrzení nebylo vlajkováno jako [SOURCE NEEDED].

**Draft uložen:** `data/output/articles/co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat/article_co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat_CZ.md`

## Step 4 — ToV Check

**Zkontrolováno vět:** ~90
**Nalezeno problémů:** 3

| # | Location | Issue Type | Original (full sentence) | Corrected (full sentence) |
|---|----------|------------|---------------------------|----------------------------|
| 1 | H2 "Kdy má smysl PPC audit objednat", úvodní věta před výčtem | Bez omáčky — lead-in fráze (analog "Existuje několik důvodů, proč…") | "Několik situací signalizuje, že je audit na místě:" | "Audit dává smysl v pěti situacích:" |
| 2 | H2 "Kdy PPC audit naopak nedává smysl", 1. odstavec, poslední věta | Rytmus vět — 3+ dlouhé věty v odstavci za sebou | "Audit v tu chvíli hodnotí kampaň v přechodném stavu, ne v jejím skutečném provozu, a nálezy by za pár týdnů stejně neplatily." | "Audit v tu chvíli hodnotí kampaň v přechodném stavu, ne v jejím skutečném provozu. Nálezy by navíc za pár týdnů stejně neplatily." |
| 3 | H2 "Kdy má smysl PPC audit objednat", odrážka "Plánujete navýšit rozpočet" | Slovní volba — příliš hovorová metafora ("nasypaný rozpočet") pro how-to obsah, věcnější kalibrace dle ToV Guide sekce 4 | "Než do kampaně pošlete víc peněz, má smysl ověřit, že současné nastavení nasypaný rozpočet neztratí na stejných chybách." | "Než do kampaně pošlete víc peněz, má smysl ověřit, že současné nastavení dodatečný rozpočet neztratí na stejných chybách." |

Zbytek draftu prošel checklistem beze změn: konzistentní vykání, žádný hype/povýšenecký jazyk, žádné vágní tvrzení, case study správně rámovaná jako "u klienta Nefertiti", žádné casual filler slova ("prostě", "tak nějak", "celkem", "vlastně").

## Step 5 — Struktura & formátování

**Délka článku:** STŘEDNÍ (~1571 slov)

**Audit odstavců (povinná první akce):** proveden na celém draftu z Kroku 4. Žádný odstavec nepřekročil 100 slov (nejdelší 88 slov, sekce "Kdy PPC audit nedává smysl") — žádné rozdělení nutné.

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | Callout přidán (Warning) | "Bez validního trackingu konverzí je jakýkoliv další závěr auditu jen odhad..." pod bullet "Měření a tracking" v sekci "Co PPC audit konkrétně kontroluje" | Formatting: zdůraznění kritické závislosti (bez trackingu jsou ostatní nálezy jen odhad) |
| 2 | Tabulka přidána | Srovnání 4 metod auditu (Metoda / Čas / Hlavní výhoda / Hlavní limit) v sekci "Jak probíhá PPC audit", nahrazuje samostatný odstavec o čase | Formatting: srovnávací data lépe čitelná jako tabulka než prozaicky; odstranění duplicity s bold-odstavcovými popisy metod |
| 3 | Callout přidán (Keep in Mind) | "Automatizovaný nástroj a self-audit jsou dobrý první krok, ale..." po tabulce metod | Structure Guide: 1 Keep in Mind na how-to článek, limity metody |
| 4 | Callout přidán (Tip) | "Nejste si jistí, jestli je na audit vhodná chvíle?..." v sekci "Kdy má smysl PPC audit objednat" | Formatting: praktická rada (2-3 Tip callouty doporučené, žádné callouty za sebou) |
| 5 | H2 sloučeny do H3 pod novým H2 | "Kdy má smysl PPC audit objednat" a "Kdy PPC audit naopak nedává smysl" nyní H3 podsekce pod nový H2 "Kdy PPC audit dává a nedává smysl" | Structure: 10 H2 na článek přesahovalo doporučenou frekvenci 3-7; tyto dvě sekce jsou přirozený pár (stejné rozhodovací téma), sloučení snižuje počet H2 na 9 bez ztráty obsahu nebo CTA umístění |

**Celkem:** 3 callouty (Warning, Keep in Mind, Tip) — žádné dva za sebou, max 1 na H2 sekci. 1 tabulka. 3 seznamy (co kontroluje, kdy dává smysl, klíčové závěry) — v rámci limitu 2-3 pro střední délku článku.

**Flagged k rozhodnutí uživatele:** i po sloučení zůstává 9 H2 sekcí, nad doporučenou frekvencí 3-7 z Structure Guide. Vzhledem k rozsahu tématu (definice → rozsah → metody → kdy ano/ne → výstup → přístup evisions → FAQ → závěry → zdroje) jde o obsahově odůvodněný rozsah, ne formátovací přehmat — ponecháno bez dalšího sloučení, aby se nenarušila schválená osnova z Kroku 2. K posouzení uživatelem.

**Autorská atribuce:** neduplikována ručně v markdownu — dle precedentu (`webova-analytika...` draft) i CLAUDE.md poznámky o known site issues vkládá author box automaticky `step4_html.py` v Kroku 6.

**Struktura uložena:** `data/output/articles/co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat/article_co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat_CZ.md` (aktualizováno in-place, verze v1)

## Step 6 — HTML konverze

**Nástroj:** `src/step4_html.py` (`convert_to_html()`), voláno programově (skript nemá CLI — na rozdíl od `export_article_docx.py`/`generate_write_log.py`). Slug pro breadcrumb/ToC anchor předán jako čistý URL slug (`co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat`), výstupní soubor následně přejmenován na konvenci `article_[slug]_CZ.html` (stejný postup jako u existujícího draftu `webova-analytika...`, kde `convert_to_html()` sám o sobě soubor s prefixem "article_" negeneruje).

**ToC:** vygenerováno automaticky (článek 1571 slov > 1500 práh) — 11 položek včetně 2 vnořených H3 pod "Kdy PPC audit dává a nedává smysl".

**Meta title/popisek:** `convert_to_html()` negeneruje `<meta name="description">` a použije H1 přímo jako `<title>` — stejně jako u referenčního draftu (`webova-analytika...`) bylo nutné obojí doplnit ručně po generování:
- Title: "PPC audit: co to je a kdy ho objednat | evisions.cz Blog" (56 znaků, primární keyword na začátku)
- Meta popisek (156 znaků): "PPC audit odhalí, kde kampaně v Google Ads či Sklik ztrácí rozpočet. Zjistěte, co PPC audit kontroluje, jak probíhá a kdy se vyplatí ho objednat – i kdy ne."

**Callouty/tabulka/ToC render:** ověřeno — 3 callouty (`callout-warning`, `callout-keep-in-mind`, `callout-tip`) správně převedeny z blockquote syntaxe, srovnávací tabulka metod auditu vykreslena jako `<table>`.

**Obrázky:** žádné — téma nevyžaduje vizuální ilustrace, žádný `[IMAGE NEEDED]` placeholder.

**HTML Checklist:**
- [x] Struktura stránky v povinném pořadí
- [x] Poppins font načten
- [x] ToC přítomen (>1500 slov)
- [x] Autor box s datem aktualizace (generický Content Team box — známé omezení šablony, viz CLAUDE.md known site issues)
- [x] Poznámka k obsahu přítomna
- [x] Meta title 56 znaků (50–60 ✓)
- [x] Meta popisek 156 znaků (150–160 ✓)
- [x] Responzivní (šablona, max-width 1160px)
- [x] `.docx` vygenerován přes `src/export_article_docx.py`

**Výstupy:**
- `article_co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat_CZ.html`
- `article_co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat_CZ.docx`
- `article_co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat_CZ_log.html`

**Content Plan Sheet:** řádek PPC-15 zůstává Status "In Progress" v ledgeru (`data/output/content_plan_index.md`) — na Published se přepne až po skutečné publikaci na živém webu (Krok 7, mimo rozsah tohoto běhu).

## Step 7 — QA + aktualizace Content Plan

**Content validace (marketingový expert review):** PASS. Fakta technicky přesná, žádné zjednodušení, koncepty v logickém pořadí (definice → rozsah → metody → kdy ano/ne → výstup → náš přístup → FAQ → závěry), příklady realistické, nic z konkurenčního researchu Kroku 1 není opomenuto.

**QA Checklist:**
- [x] Fakta odpovídají zdroji
- [x] Žádné informace nepřidány/neodebrány mimo vlajkované odchylky (Krok 3 log)
- [x] Odkazy fungují — ověřeno WebFetch na všech 4 externích/interních odkazech (`/ppc-audit/`, case study Nefertiti, Consent Mode V2, Synergie PPC a SEO) — všechny OK, žádné 404. Případová studie Nefertiti potvrzena na skutečných +149,57 % tržeb — odpovídá formulaci článku "téměř 150 %".
- [x] Tón odpovídá ToV Guide (How-to kalibrace) — ověřeno v Kroku 4
- [x] Žádné zakázané fráze, žádné garance výsledků
- [x] E-E-A-T prvky přítomny (autor box, zdroje, datum aktualizace)
- [x] Hierarchie nadpisů správná (H1→H2→H3, bez přeskočení úrovní)
- [x] Interní odkazy přítomny (4 blog + 2 CTA na LP)
- [x] HTML se správně renderuje (ToC, callouty, tabulka ověřeny v Kroku 6)
- [x] Zdrojové citace u faktických tvrzení, žádné [SOURCE NEEDED] značky

**Soubory uloženy: 5/5** (`.md`, `_log.md`, `.html`, `_log.html`, `.docx`) — ověřeno na disku.

**Aktualizace Content Plan:** Uživatel potvrdil (AskUserQuestion, 2026-08-27), že článek ještě NENÍ publikován na živém webu. Lokální ledger proto **zůstává Status "In Progress"** — přepnutí na "Published" + doplnění URL proběhne až po skutečném nahrání na evisions.cz/blog/ (mimo rozsah tohoto běhu, workflow to výslovně vyžaduje "po skutečném publikování na web"). xlsx mirror se nepřegeneroval, protože ledger se v tomto kroku nezměnil.

**QA: PASS.** Soubory: 5/5. Ledger: beze změny (In Progress, čeká na publikaci).
