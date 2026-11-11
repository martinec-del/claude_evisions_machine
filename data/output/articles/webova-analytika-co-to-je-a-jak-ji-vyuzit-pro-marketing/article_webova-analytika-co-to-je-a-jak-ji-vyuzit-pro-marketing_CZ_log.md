# Log: Webová analytika: co to je a jak ji využít pro marketing

**Slug:** webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing
**Content Plan:** bez ID (nový řádek) — Kategorie: SEO, podskupina "Analytika a metriky" (`topic_cluster_analytika-a-metriky_CZ`)
**Content Plan zdroj:** https://docs.google.com/spreadsheets/d/1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY/edit?gid=1262896623#gid=1262896623
**Typ obsahu:** How-to / edukativní (viz ToV Guide sekce 4)
**Vytvořeno:** 2026-08-17

## Init

- Sheet neobsahuje přiřazené ID ani klíčové slovo — vyplní se v Kroku 1.
- Příbuzné publikované články ve stejné podskupině (kandidáti na interní prolinkování):
  - SEO-07 — Universal Analytics končí, ať žije Google Analytics 4! — https://www.evisions.cz/blog/universal-analytics-konci-at-zije-google-analytics-4/
  - SEO-19 — Share of Voice (SOV): K čemu je a jak metriku spočítat? — https://www.evisions.cz/blog/share-of-voice-sov-k-cemu-je-a-jak-metriku-spocitat/
  - SEO-21 — Google Search Console: Jak ji v SEO využít naplno? — https://www.evisions.cz/blog/google-search-console-jak-ji-v-seo-vyuzit-naplno/
- Uživatel potvrdil: Content Plan zdroj pravdy = odkazovaný editorial calendar sheet (ne sheet z CLAUDE.md), použije se i pro update Status/URL v Kroku 7.

## Step 1 — Konkurenční research + klíčová slova

**Seed keyword:** "webová analytika" (ověřeno přes WebSearch, 4 dotazy × top výsledky)

**Provider:** Ahrefs MCP (domain rating, site-explorer-metrics, keywords-explorer)

**URL research:** 24 kandidátních URL nasbíráno (4 dotazy), deduplikováno a filtrováno (vynechány fóra, kurzy/služby bez article contentu, SK doména). 10 URL obohaceno o DR + organic traffic a fetchnuto. 1 z 10 (netdirect.cz) se ukázal jako JS blog-index, ne článek — označeno FAIL ve xlsx.

**Klíčový content gap:** Žádný konkurenční článek nerámuje webovou analytiku explicitně jako most "metrika → konkrétní marketingové rozhodnutí" — konkurence je buď encyklopedická (webglobe, cernovsky), nebo agenturně-prodejní (antee, robertnemec, digitalniarchitekti, dfsolutions) bez nezávislého edukativního tónu.

**Kanibalizace v rámci vlastního clusteru (topic_cluster_analytika-a-metriky_CZ):** Google Analytics/GA4 už pokrývá živý článek SEO-07, Google Search Console živý článek SEO-21, Google Tag Manager je naplánovaný samostatný článek ve stejné skupině Content Plan sheetu. Tento článek proto tyto nástroje jen zmíní a prolinkuje, bez hloubkového výkladu.

**Klíčová slova:** 20 navrženo (viz xlsx list "Keywords") — primární "webová analytika" (90/mo, KD 0), sekundární "analýza webu" (450), "digitální analytika", podpůrné metriky/nástroje (konverzní poměr, míra okamžitého opuštění, UTM parametry, Matomo, heatmapa...), 4 "mention only" kvůli kanibalizaci (GA, GA4, GTM, GSC), 2 mimo scope (Google Ads, SEO).

**xlsx uložen:** `data/output/articles/webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing/webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing_step1.xlsx`

## Step 2 — Brief & osnova

**Typ obsahu:** How-to / edukativní — téma je definiční a metrikové, cílem je propojit data s marketingovým rozhodnutím, ne prezentovat klientský výsledek.

**Cíl počtu slov:** 1600–1900 (konkurenční průměr ze Step 1 ~1930, ale rozsah zúžen kvůli vynechání hloubkového GA4/GSC/GTM výkladu — kanibalizace).

**Diferenciace od konkurence:** Explicitní most "metrika → konkrétní marketingové rozhodnutí" (content gap ze Step 1). Nezávislý edukativní tón bez prodejního rámce (na rozdíl od antee.cz, robertnemec.com, digitalniarchitekti.cz, dfsolutions.cz). Vyvážený pohled na nástroje včetně Matomo (konkurence je téměř výhradně GA-centrická).

**Kostra nadpisů (H2):**
1. Co je webová analytika (+ H3 Webová analytika vs. analýza webu)
2. Jaké nástroje webovou analytiku umožňují
3. Klíčové metriky a jak je číst (+ H3 Metriky vs. dimenze, H3 Konverzní poměr, H3 Míra okamžitého opuštění a zdroje návštěvnosti)
4. Jak webovou analytiku využít pro marketingová rozhodnutí
5. Časté chyby při interpretaci dat
6. Klíčové závěry
7. Zdroje

**Plán interních odkazů (5):**

| # | Cílový článek | Umístění |
|---|----------------|----------|
| 1 | Universal Analytics končí, ať žije Google Analytics 4! (SEO-07) | Sekce "Jaké nástroje..." |
| 2 | Google Search Console: Jak ji v SEO využít naplno? (SEO-21) | Sekce "Jaké nástroje..." |
| 3 | Share of Voice (SOV) (SEO-19) | Sekce "Klíčové metriky..." |
| 4 | Co je Google Consent Mode V2 a musíte to řešit? (PPC-09) | Sekce "Časté chyby..." |
| 5 | Synergie PPC a SEO (SEO-06) | Sekce "Jak webovou analytiku využít..." |

**Content validace:** PASS — struktura logicky odpovídá tématu (definice → nástroje → metriky → praktická aplikace → chyby → závěr), všechny klíčové koncepty pro How-to obsah přítomny, pořadí sekcí didakticky správné, nic klíčového nechybí (GA4/GSC/GTM záměrně zúženo a zdůvodněno v diferenciaci).

**Osnova uložena:** `data/output/articles/webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing/article_webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing_CZ_outline.docx`

## Step 3 — Draft

**Typ obsahu:** How-to / edukativní
**Počet slov:** 1601 (cíl: 1600–1900)

### Integrace klíčových slov

| # | Keyword | Volume | Umístění | Kontextová věta |
|---|---------|--------|-----------|-------------------|
| 1 | webová analytika | 90 | H1 + úvodní odstavec | "Webová analytika je sběr a vyhodnocování dat o chování návštěvníků na webu s cílem podpořit konkrétní marketingové rozhodnutí." |
| 2 | analýza webu | 450 | H3 "Webová analytika vs. analýza webu" | "Analýza webu bývá širší pojem, který kromě chování návštěvníků může zahrnovat i technický SEO audit, konkurenční analýzu nebo kontrolu přístupnosti." |
| 3 | digitální analytika | 10 | H2 "Co je webová analytika" | "Pojem se často zaměňuje se širším pojmem *analýza webu*, případně synonymem *digitální analytika*." |
| 4 | analytické nástroje | 100 | H2 "Jaké nástroje webovou analytiku umožňují" | "Analytické nástroje se liší podle toho, jestli měří chování na webu, výkon ve vyhledávání, nebo obojí." |
| 5 | matomo | 150 | H2 "Jaké nástroje..." | "Pro weby s vyššími nároky na ochranu dat existuje alternativa Matomo." |
| 6 | metriky a dimenze | 0 | H3 "Metriky vs. dimenze" (nadpis) | — |
| 7 | konverzní poměr | 200 | H3 "Konverzní poměr — metrika, která rozhoduje o rozpočtu" | "Konverzní poměr je podíl konverzí na celkovém počtu návštěv nebo uživatelů." |
| 8 | co je konverze | 0 | H3 "Konverzní poměr..." | "Konverze je akce, kterou web od návštěvníka očekává — nákup, odeslání formuláře, stažení ceníku." |
| 9 | míra okamžitého opuštění | 100 | H3 "Míra okamžitého opuštění a zdroje návštěvnosti" (nadpis) | — |
| 10 | zdroje návštěvnosti | 0 | H3 "Míra okamžitého opuštění a zdroje návštěvnosti" | "Proto se bounce rate vždy čte společně se zdrojem návštěvnosti." |
| 11 | analýza dat | 100 | H2 "Jak webovou analytiku využít pro marketingová rozhodnutí" | "Rozdíl dělá krok, který následuje po zjištění čísla — analýza dat, která vede ke konkrétnímu rozhodnutí, kam dál." |
| 12 | utm parametry | 150 | H2 "Jak webovou analytiku využít..." | "Bez UTM parametrů analytika nepozná, který konkrétní kanál přivedl konverzi — jen obecný zdroj návštěvnosti." |
| 13 | heatmapa | 100 | H2 "Jak webovou analytiku využít..." | "Heatmapy doplňují číselná data o vizuální pohled na chování na stránce — kam uživatelé klikají, kam scrollují a kde opouštějí formulář." |
| 14 | digitální marketing | 500 | Hook (context only) | "Digitální marketing bez dat je jen odhad." |
| 15 | google analytics / ga4 / google search console / google tag manager | mention only | H2 "Jaké nástroje..." | Zmíněny a prolinkovány (GA4 → SEO-07, GSC → SEO-21), GTM bez odkazu (plánovaný samostatný článek). |

### Odchylky od osnovy

| # | Typ | Popis | Důvod |
|---|-----|-------|--------|
| 1 | Rozšíření obsahu v rámci schválených sekcí | Přidáno 6 odstavců navíc oproti key points z osnovy (kontext "co to znamená pro marketéra" v Co je webová analytika; poznámka o přesnosti dat dle typu nástroje v sekci nástrojů; druhý příklad konverzního poměru pro B2B; věta o typické chybě v sekci Metriky vs. dimenze; odstavec o frekvenci sledování metrik; čtvrtá častá chyba "Spoléhání na souhrnný dashboard bez segmentace") | Cílový počet slov (1600–1900) nebyl bez rozšíření dosažen (draft v první verzi ~1330 slov); rozšíření jsou v rámci již schválených H2/H3 nadpisů, nepřidávají nové sekce ani nová témata mimo scope osnovy |

Žádné jiné odchylky — struktura nadpisů (H1/H2/H3) odpovídá schválené osnově přesně.

**Oprava (zjištěno při auditu v Kroku 5):** Tvrzení "všechny plánované interní odkazy (5/5) zapracovány" bylo nepřesné — v draftu chyběl odkaz č. 3 (Share of Voice, SEO-19) z plánu v sekci 5 osnovy. Skutečný stav po Kroku 3: 4/5 odkazů. Doplněno v Kroku 5, viz Step 5 log níže.

### Plný článek se zdroji

Viz `article_webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing_CZ.md`. Faktická tvrzení se zdrojovou citací v hranaté závorce:

- "Google Universal Analytics, předchůdce GA4, přestal zpracovávat data k 1. červenci 2023." [https://blog.google/products/ads-commerce/upgrade-to-google-analytics-4-before-july-1/]
- "Na rozdíl od GA4, který data odesílá na servery Google, umožňuje Matomo hostovat analytiku na vlastním serveru — data tak zůstávají výhradně majiteli webu." [https://matomo.org/100-data-ownership/]
- "Google Analytics tuto metriku nedávno přejmenoval na key event rate, princip výpočtu se ale nemění." [https://support.google.com/analytics/answer/9267568?hl=en]
- "Míra okamžitého opuštění (bounce rate) měří podíl návštěv, při kterých uživatel odejde po zobrazení jediné stránky, aniž by dál interagoval s webem." [https://support.google.com/analytics/answer/12195621?hl=en]
- "UTM parametry se přidávají k odkazu a označují zdroj, médium a název kampaně; Google pro jejich generování nabízí vlastní Campaign URL Builder." [https://support.google.com/analytics/answer/10917952?hl=en]
- "Apple's Intelligent Tracking Prevention omezuje životnost cookies nastavených přes JavaScript na sedm dní, což zkresluje počet skutečně vracejících se návštěvníků." [https://www.customerlabs.com/blog/understanding-safari-intelligent-tracking-prevention-apple-itp-impact/]

Ostatní tvrzení (definice, příklady výpočtu, doporučení) jsou interpretace/obecné znalosti — zdroj nepotřebují. Žádné [SOURCE NEEDED] značky.

**Uložen jako:** `data/output/articles/webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing/article_webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing_CZ.md`

## Step 4 — ToV Check

**Zkontrolováno vět:** ~70
**Nalezeno problémů:** 3

| # | Location | Issue Type | Original (full sentence) | Corrected (full sentence) |
|---|----------|------------|--------------------------|---------------------------|
| 1 | H3 "Metriky vs. dimenze" | Nepřímá formulace (ne "rovnou k věci") | "Odpověď na otázku "vzrostla u koho, odkud a na jakém zařízení" je přitom to, co z pouhého pozorování dělá použitelný podklad pro rozhodnutí." | "Až odpověď na otázku "u koho, odkud a na jakém zařízení" dělá z pozorování použitelný podklad pro rozhodnutí." |
| 2 | H2 "Jak webovou analytiku využít pro marketingová rozhodnutí" | Komplikovaná větná konstrukce s vloženým odkazem | "Tento typ propojení dat napříč kanály je stejný princip, jaký popisujeme v článku o tom, jak spolu [souvisí PPC a SEO](https://www.evisions.cz/blog/synergie-ppc-a-seo-klic-k-digitalnimu-uspechu/) — analytika je spojnice, která rozhoduje, kam rozpočet přesunout dál." | "Stejný princip propojení dat napříč kanály popisujeme v článku o [synergii PPC a SEO](https://www.evisions.cz/blog/synergie-ppc-a-seo-klic-k-digitalnimu-uspechu/) — analytika je spojnice, která rozhoduje, kam rozpočet přesunout dál." |
| 3 | Callout "Keep in Mind" v sekci "Časté chyby při interpretaci dat" | Gramaticky neobratné použití anglického přivlastňovacího 's v české větě | "Apple's Intelligent Tracking Prevention omezuje životnost cookies nastavených přes JavaScript na sedm dní, což zkresluje počet skutečně vracejících se návštěvníků [https://www.customerlabs.com/blog/understanding-safari-intelligent-tracking-prevention-apple-itp-impact/]." | "Nástroj Intelligent Tracking Prevention od Applu omezuje životnost cookies nastavených přes JavaScript na sedm dní, což zkresluje počet skutečně vracejících se návštěvníků [https://www.customerlabs.com/blog/understanding-safari-intelligent-tracking-prevention-apple-itp-impact/]." |

Ostatní kontrolní body čisté: otevření sekcí vede hodnotou (žádné "v této sekci..."), rytmus princip → mechanika → aplikace dodržen, žádné 3+ dlouhé věty za sebou, žádné casual markery, vykání konzistentní, žádný hype jazyk, žádná povýšenost, žádná vágní tvrzení bez čísel, emoční kalibrace v normě, žádná falešná jistota.

## Step 5 — Struktura & formátování

**Audit odstavců (povinná první akce):** Zkontrolováno všech 19 odstavců v článku. Žádný nepřekračuje 100 slov (nejdelší, úvod sekce "Jaké nástroje webovou analytiku umožňují", má ~69 slov). Žádné rozdělení nebylo potřeba.

**Délka článku:** STŘEDNÍ (1635 slov po úpravách v tomto kroku)

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | Interní odkaz doplněn | Přidána věta s odkazem na [Share of Voice (SOV)](https://www.evisions.cz/blog/share-of-voice-sov-k-cemu-je-a-jak-metriku-spocitat/) na úvod sekce "Klíčové metriky a jak je číst" | Oprava chybějícího odkazu č. 3 z plánu interního prolinkování (osnova sekce 5) — v Kroku 3 byl vynechán |
| 2 | Duplicitní prvek odstraněn | Odstraněn ručně vložený blok `> **Poznámka k obsahu:** Tento článek má edukativní charakter...` před sekcí "Zdroje" | `src/step4_html.py` vkládá tento blok automaticky v Kroku 6 — ruční verze by se duplikovala (viz `prompts/step3_structure.md`) |

**Kontrola hierarchie nadpisů:** 1× H1, 7× H2, 4× H3 — žádné přeskočené úrovně. 7 H2 sekcí je na horní hranici doporučeného rozsahu (3–7), odpovídá plánované osnově.

**Kontrola calloutů:** 3 (Tip, Example, Keep in Mind) — v rámci limitu pro střední délku článku (2–3), žádné dva za sebou, max. 1 na H2 sekci.

**Kontrola tabulek:** 3 (Pojem vs. analýza webu; přehled nástrojů; metrika → rozhodnutí). Mírně nad doporučeným rozsahem pro střední délku (1–2), ponecháno záměrně — všechny tři plní odlišnou funkci a tabulka "metrika → rozhodnutí" je jádrem diferenciace článku definované v Kroku 2.

**Kontrola seznamů:** 1 odrážkový seznam (Klíčové závěry, 5 položek). Sekce "Časté chyby" používá tučně uvozené odstavce místo seznamu — ponecháno, odpovídá vzoru z ToV Guide a zachovává prostor pro vysvětlující větu u každé chyby.

**Navigační prvky:** Obsah (ToC) přítomen (článek >1500 slov). Interní odkazy: 5/5 z plánu (po opravě #1). Sekce Zdroje přítomna s 6 externími citacemi.

**Otevřená položka pro Krok 7:** Autorská atribuce (jméno, role, datum aktualizace) není v Content Plan Sheetu u tohoto řádku vyplněná (sloupec "zpracoval" prázdný) — potřeba doplnit před publikací.

## Step 6 — HTML konverze

**Použitý nástroj:** `src/step4_html.py` (`convert_to_html()`) — deterministická konverze markdownu na evisions.cz šablonu.

| # | Element | Description |
|---|---------|-------------|
| 1 | Struktura stránky | Header, breadcrumb, ToC, article, author-box, disclaimer, footer — v povinném pořadí |
| 2 | ToC | Vygenerováno automaticky z H2/H3 nadpisů (11 položek) |
| 3 | Callouty | 3 styl. bloky (Tip, Example, Keep in Mind) převedeny na `callout` divy se správnou CSS třídou |
| 4 | Meta title | Vlastní kratší varianta "Co je webová analytika a jak ji využít \| evisions.cz Blog" (57 znaků) — H1 v těle zůstal beze změny, jen `<title>` tag zkrácen na SEO limit 50–60 znaků |
| 5 | Meta popisek | Doplněn ručně (šablona ho negeneruje automaticky): "Webová analytika propojuje chování návštěvníků webu s konkrétním marketingovým rozhodnutím. Zjistěte, jak číst klíčové metriky a vybrat správné nástroje." (153 znaků) |
| 6 | Autor box | Auto-generován šablonou s placeholder hodnotou "evisions Advertising" / "Content Team" — ke skutečné atribuci viz otevřená položka z Kroku 5 |
| 7 | Poznámka k obsahu | Vygenerována automaticky šablonou (nebyla duplikována ručně, viz oprava níže) |

**Opravy provedené před konverzí (nalezeno při přípravě Kroku 6):**

| # | Typ | Popis | Důvod |
|---|-----|-------|--------|
| 1 | Odstraněna duplicitní ruční sekce "## Obsah" z markdown článku (7 odrážek s ručně sestavenými anchor odkazy bez diakritiky) | `src/step4_html.py` generuje vlastní ToC automaticky z H2/H3 nadpisů (se zachovanou diakritikou v ID) — ruční verze měla nefunkční odkazy (neshodovaly se s generovanými `id` atributy) a duplikovala obsah |
| 2 | Odstraněno 6× syrové URL v hranaté závorce z těla textu (např. "...k 1. červenci 2023 [https://blog.google/...]." → "...k 1. červenci 2023.") | Hranaté závorky se zdrojovou URL byly pracovní citační značky pro QA v Krocích 3–5 (viz Step 3 log "Plný článek se zdroji"), ne prvek pro publikovaný web — zobrazení syrové URL v textu čtenáři odporuje Structure Guide sekci 7 (popisný kotvící text). Fakta zůstávají beze změny, zdroje jsou dostupné v sekci "Zdroje" na konci článku |

**Nástroj pro log HTML:** `src/generate_log.py` neodpovídá formátu logu Write workflow (očekává sekce `Step N Log:` s pevným schématem sloupců z Edit workflow — Keyword Integration/ToV Rewrite/Structure/HTML). Vytvořen nový obecný převodník `src/generate_write_log.py` (markdown → stylované HTML přes knihovnu `markdown` s rozšířením `tables`), který zpracuje libovolný obsah logu Write workflow bez závislosti na pevném schématu kroků.

**Finální počet slov (article_..._CZ.md):** 1590 (cíl: 1600–1900 — mírně pod cílem po odstranění syrových URL citací z těla textu, obsahově beze změny)

**Soubory vygenerovány:**
- `data/output/articles/webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing/article_webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing_CZ.html`
- `data/output/articles/webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing/article_webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing_CZ_log.html`
