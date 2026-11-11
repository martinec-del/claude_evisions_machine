# Log: Co je SEO a jak funguje

**Slug:** co-je-seo-a-jak-funguje
**Content Plan:** SEO-32 — Kategorie: SEO, podskupina "11 – content GAP"
**Content Plan zdroj:** data/output/content_plan_index.md (lokální ledger, TODO položka nalezena a přeřazena na In Progress se SEO-32)
**Vytvořeno:** 2026-08-24

## Init

- Krok 0 Duplicate Check: shoda s TODO položkou "Co je SEO a jak funguje" v `content_plan_index.md` pod SEO — Skupina 11 (content GAP). Žádný Published článek na téma nenalezen. Přiřazeno ID SEO-32, Next ID posunuto na SEO-33.
- Žádná existující verze ve `data/output/articles/co-je-seo-a-jak-funguje/` — NEW mode, v1.
- Skupina 11 (content GAP) je sada definičních/vzdělávacích témat bez vlastního topic clusteru se zavedeným tagem — sourozenecká témata (Keyword research, On-page SEO, Technické SEO, Core Web Vitals...) jsou zatím také jen TODO, ne Published, takže z nich nelze v Kroku 2 prolinkovat.
- Kandidáti na interní prolinkování z jiných Published článků (relevance k základům SEO):
  - SEO-14 — Průvodce regulárními výrazy pro začátečníky — https://www.evisions.cz/blog/pruvodce-regularnimi-vyrazy-pro-zacatecniky/
  - SEO-24 — SEO nástroje + 7 rozšíření, která vám usnadní práci — https://www.evisions.cz/blog/seo-nastroje-7-rozsireni-ktera-vam-usnadni-praci/
  - SEO-07 — Universal Analytics končí, ať žije Google Analytics 4! — https://www.evisions.cz/blog/universal-analytics-konci-at-zije-google-analytics-4/
  - SEO-06 — Synergie PPC a SEO: Klíč k digitálnímu úspěchu? — https://www.evisions.cz/blog/synergie-ppc-a-seo-klic-k-digitalnimu-uspechu/
  - (Přesný výběr se potvrdí v Kroku 2 dle skutečné struktury nadpisů draftu.)

## Step 1 — Konkurenční research + klíčová slova

**Seed keyword:** "co je SEO" (ověřeno přes WebSearch — reálně používaný dotaz, potvrzeno i Ahrefs volume 1200/mo)

**Provider:** Ahrefs MCP (domain rating, site-explorer-metrics s `protocol=https`, `mode=exact`) + keywords-explorer (matching-terms, related-terms)

**URL research:** 4 WebSearch dotazy ("co je SEO vysvětleno", "SEO pro začátečníky návod", "jak SEO funguje", "co je SEO optimalizace webu") → 23 unikátních CZ URL po deduplikaci a filtru (vyřazeny: 2× WordPress-specifické návody mimo obecný scope, 1× kurzová landing page bez článku, 2× tenké slovníčkové stub záznamy, 2× duplicitní stránky ze stejné domény jako už vybraný kandidát). Obohaceno o DR + organic traffic pro 18 kandidátů. Top 10 dle relevance/DR/traffic úspěšně fetchnuto, 0 FAIL.

**Klíčový content gap:** Žádný z 10 konkurenčních článků nepropojuje definici SEO s konkrétní agenturní expertízou/case studies ani s CZ specifickým kontextem vyhledávačů (Google vs. Seznam) — jen webnode.com Seznam vůbec zmiňuje. Téma GEO/AI Overviews vyváženě pokrývají jen 2 z 10 (seoprakticky.cz, mipaco.cz). Žádný konkurent nenabízí přehlednou tabulku "tři pilíře SEO → kam se prohloubit dál" propojenou s vlastním obsahem.

**Kanibalizace v rámci vlastní kategorie:** Sourozenecká TODO témata ve Skupině 11 (Keyword research, On-page SEO, Technické SEO, Core Web Vitals, Interní prolinkování, Kanibalizace klíčových slov, Google Core Update) jsou zatím nenapsaná — tento článek proto slouží jako "rodičovský" definiční hub, on-page/technické/off-page pilíře jen zmíní a nerozvíjí do hloubky, ať nekonkuruje budoucím specializovaným článkům ve stejné skupině.

**Klíčová slova:** 18 navrženo (viz xlsx list "Keywords") — primární definiční cluster "co je seo" / "seo co to je" / "co je to seo" (~2100/měsíc kombinovaně), přesná fráze tématu "co to je seo a jak funguje" (10/měsíc, nízký objem ale exact-match), cluster rozšíření zkratky "seo optimalizace pro vyhledávače" / "co je zkratka seo", marketing-kontext cluster "seo marketing" (~1300/měsíc kombinovaně). Mimo-oborové/jinam patřící výsledky (seo specialista, seo konzultant, seo agentura praha, seo studium, seo služby, seo expert, seo analytik, seo tools, seo katalogy, kniha seo — komerční/kariérní intent) vyřazeny jako mimo scope definičního článku.

**Marketing Miner cross-check:** `python src/marketing_miner_api.py volume ...` na 8 hlavních keywordech — většina čísel se s Ahrefs shoduje v řádu (co je seo 1300 vs Ahrefs 1200, co je zkratka seo 50 vs 50, co je seo optimalizace 120 vs 150...). **Jedna výjimka — řádový rozdíl:** "seo optimalizace pro vyhledávače" MM 100/mo vs. Ahrefs 900/mo. V Kroku 2 použít konzervativnější odhad MM (100/mo). Cross-check hodnoty zapsány do sloupce Notes v listu "Keywords".

**xlsx uložen:** `data/output/articles/co-je-seo-a-jak-funguje/co-je-seo-a-jak-funguje_step1.xlsx`

## Step 2 — Brief & osnova

**Typ obsahu:** How-to / definiční — téma je mechanické a definiční ("co SEO je, jak funguje"), case study formát by nedával smysl. Slouží jako "rodičovský" hub k sourozeneckým TODO tématům ve Skupině 11 (Keyword research, On-page SEO, Technické SEO...).

**Cíl počtu slov:** 1900–2300 (konkurenční rozsah 1300–8500 je extrémně široký; volen střed pásma srovnatelných konkurentů — mipaco.cz ~2800, itnetwork.cz ~2300, webglobe.cz ~2300, loudavymkrokem.cz ~2100 — kratší/delší extrémy neodpovídají evisions ToV).

**Diferenciace od konkurence:** Tabulka "tři pilíře SEO → kam se prohloubit" propojující každý pilíř s konkrétním publikovaným evisions článkem (content gap ze Step 1). CZ tržní kontext Google vs. Seznam s vlastními daty (infografiky). Reálný case study jako důkaz místo obecného slibu (ToV Guide sekce 7 compliance). Vyvážená zmínka AI/GEO vývoje s odkazem na vlastní AI cluster obsah. Záměrně vynecháno: hloubkový keyword research, on-page checklist, technický audit — patří sourozeneckým TODO článkům ve stejné skupině.

**Kostra nadpisů (H2):**
1. Co znamená SEO a čím se liší od placené reklamy
2. Jak funguje vyhledávač (+ H3 Procházení, H3 Indexace, H3 Hodnocení a zobrazení výsledků)
3. Tři pilíře SEO a kam se v nich prohloubit (+ H3 Technické SEO, H3 Obsahové/on-page SEO, H3 Off-page SEO/linkbuilding)
4. Proč je SEO důležité pro firmy v Česku
5. Časté mylné představy o SEO
6. Klíčové závěry
7. Zdroje

**Plán interních odkazů (6):**

| # | Cílový článek | Umístění |
|---|----------------|----------|
| 1 | Z nuly na SEO hvězdu: Pomohli jsme Kalkulátor.cz vyrůst o 700 % (SEO-02) | H2 "Proč je SEO důležité pro firmy v Česku" |
| 2 | Infografika: Podíl vyhledávačů Google a Seznam #2021 (SEO-20) | H2 "Proč je SEO důležité..." |
| 3 | 6 hlavních linkbuildingových metrik (SEO-27) | H3 "Off-page SEO / linkbuilding" |
| 4 | Úspěšná SEO migrace webu Foodora.cz (SEO-04) | H3 "Technické SEO" |
| 5 | Jak funguje AI Mode od Googlu (AI-02) | H2 "Proč je SEO důležité..." |
| 6 | SEO nástroje + 7 rozšíření, která vám usnadní práci (SEO-24) | Tabulka pilířů (obsahový pilíř) |

**Content validace:** PASS — struktura logicky odpovídá tématu (definice → mechanika vyhledávače → pilíře s dalším směrem → byznys relevance → mylné představy → závěr), didakticky vzestupné pořadí, chybějící hloubka u keyword research/on-page/technického auditu je záměrná (zdůvodněno diferenciací a sourozeneckými TODO tématy, ne opomenutí).

**Osnova uložena:** `data/output/articles/co-je-seo-a-jak-funguje/article_co-je-seo-a-jak-funguje_CZ_outline.docx`

## Step 3 — Draft

**Typ obsahu:** How-to / definiční
**Počet slov:** 1903 (cíl: 1900–2300)

### Integrace klíčových slov

| # | Keyword | Volume | Umístění | Kontextová věta |
|---|---------|--------|-----------|-------------------|
| 1 | co je seo | 1200 | H1 + úvodní odstavec definice | "SEO je zkratka pro Search Engine Optimization, česky optimalizace pro vyhledávače." |
| 2 | co to je seo a jak funguje | 10 (exact-match fráze) | H1 (blízké znění) | "Co je SEO a jak funguje" |
| 3 | seo co to je / co je to seo | 500 / 400 | H2 "Co znamená SEO..." (definiční odstavec) | "SEO je zkratka pro Search Engine Optimization, česky optimalizace pro vyhledávače." (stejná definiční věta pokrývá obě varianty) |
| 4 | co je zkratka seo | 50 | H2 "Co znamená SEO..." (rozepsání zkratky) | "SEO je zkratka pro Search Engine Optimization, česky optimalizace pro vyhledávače." |
| 5 | seo optimalizace pro vyhledávače | 900 (MM 100, konzervativně) | H2 "Co znamená SEO..." (plný název) | "...česky optimalizace pro vyhledávače." |
| 6 | pozice ve vyhledávačích | 700 | H3 "Hodnocení a zobrazení výsledků (ranking)" | "Pozice ve výsledcích se tak nepřiděluje jednou provždy, ale přepočítává průběžně..." |
| 7 | seo marketing | 1000 | H2 "Proč je SEO důležité pro firmy v Česku" (úvodní věta) | "SEO marketing dává smysl přesně tam, kde chcete růst návštěvnosti bez toho, aby náklady rostly lineárně s každým dalším zákazníkem." |
| 8 | on page seo | 600 (mention only) | H3 "Obsahové (on-page) SEO" (nadpis + text) | "On-page SEO se odehrává přímo na stránce — v textu, nadpisech, meta popiscích i vnitřní struktuře webu." |

### Odchylky od osnovy

| # | Typ | Popis | Důvod |
|---|-----|-------|--------|
| 1 | Rozšíření (ne strukturální) | Prakticky každá sekce dostala 1–2 odstavce navíc oproti bodům v osnově (např. odstavec o "organické návštěvnosti" v H2 1, odstavec o vzájemném posilování pilířů v H2 3, odstavec o rozpočtu SEO vs. PPC a o AI/citovatelnosti obsahu v H2 4) | První draft dle přesných bodů osnovy vyšel na ~1310 slov, pod cílem 1900–2300. Rozšíření je věcné (nové konkrétní příklady/vysvětlení v rámci již schválených H2/H3), ne výplňové — žádný nový nadpis nepřibyl ani neubyl. |
| 2 | Rozšíření | Přidána 4. mylná představa "Stačí zaplatit reklamu a SEO řešit nemusím" nad rámec 3 bodů v osnově | Přirozeně navazuje na kontrast SEO vs. PPC z úvodu článku a dorovnává rozsah sekce k ostatním prohloubeným sekcím. |

Žádné jiné odchylky — struktura nadpisů (H1/H2/H3) odpovídá schválené osnově přesně, plán interních odkazů dodržen 6/6.

### Plný článek se zdroji

Uložen v `article_co-je-seo-a-jak-funguje_CZ.md`. Faktická tvrzení převzatá z externího researche označena v textu zdrojem v hranaté závorce ([developers.google.com/search/docs/crawling-indexing] — mechanika crawling/indexace/ranking, [zpravy.aktualne.cz/...] — podíl vyhledávačů Google/Seznam v ČR) a shrnuta v sekci Zdroje na konci článku. Case study čísla (Kalkulátor.cz +700 %) čerpají z již publikovaného evisions článku (interní odkaz, ne nový zdroj) — v souladu s ToV Guide sekcí 7 doplněna věta o negarantování stejného výsledku jinému klientovi.

## Step 4 — ToV Check

**Zkontrolováno vět:** ~75
**Nalezeno problémů:** 5

| # | Location | Issue Type | Original (full sentence) | Corrected (full sentence) |
|---|----------|------------|---------------------------|----------------------------|
| 1 | H2 "Co znamená SEO a čím se liší od placené reklamy", 2. odstavec | Rytmus — jedna souvětná věta ~35 slov | "Konkrétně to znamená tohle: když někdo zadá do Google dotaz spojený s vaším produktem nebo službou, chcete se objevit mezi prvními výsledky, ne až na druhé stránce, kterou otevře jen zlomek lidí." | "Konkrétně to znamená tohle: když někdo zadá do Google dotaz spojený s vaším produktem nebo službou, chcete se objevit mezi prvními výsledky. Ne až na druhé stránce, kterou otevře jen zlomek lidí." |
| 2 | H2 "Jak funguje vyhledávač", úvodní odstavec | Rytmus — souvětná věta se dvěma "proč" klauzemi, ~38 slov | "Znát tenhle mechanismus není akademické cvičení — pomáhá pochopit, proč se optimalizace mnohdy neprojeví hned po publikaci článku, a proč jedna technická chyba dokáže shodit viditelnost celého webu, i když obsah zůstane beze změny." | "Znát tenhle mechanismus není akademické cvičení. Pomáhá pochopit, proč se optimalizace mnohdy neprojeví hned po publikaci článku, a proč jedna technická chyba dokáže shodit viditelnost celého webu, i když obsah zůstane beze změny." |
| 3 | H3 "Technické SEO", 1. věta | Rytmus — 3 věty za sebou v pásmu 24–28 slov bez krátkého zlomu | "Technické SEO řeší, jestli vyhledávač dokáže web vůbec efektivně projít a pochopit — rychlost načítání, mobilní verzi, strukturu URL adres i to, jestli se stránky nepřekrývají duplicitním obsahem." | "Technické SEO řeší, jestli vyhledávač dokáže web vůbec efektivně projít a pochopit. Do hry vstupuje rychlost načítání, mobilní verze, struktura URL adres i to, jestli se stránky nepřekrývají duplicitním obsahem." |
| 4 | H3 "Obsahové (on-page) SEO", 3. věta | Rytmus — souvětná věta ~47 slov, nejdelší v článku | "Kvalitní on-page SEO se pozná podle toho, že text čte přirozeně i bez znalosti klíčových slov, která autor cílil — nadpisy popisují obsah sekce, meta popisek láká ke kliknutí a stránka odpovídá přesně na dotaz, se kterým na ni návštěvník přišel, ne na pět různých témat najednou." | "Kvalitní on-page SEO se pozná podle toho, že text čte přirozeně i bez znalosti klíčových slov, která autor cílil. Nadpisy popisují obsah sekce, meta popisek láká ke kliknutí a stránka odpovídá přesně na dotaz, se kterým na ni návštěvník přišel — ne na pět různých témat najednou." |
| 5 | H2 "Proč je SEO důležité pro firmy v Česku", odstavec o rozpočtu | Rytmus — souvětná věta ~42 slov | "Rozpočet na SEO se navíc nemusí rovnat rozpočtu na PPC, aby přinesl srovnatelný efekt v čase — menší firmy, které si nemohou dovolit soutěžit v PPC aukcích s velkými hráči, tak SEO často využívají jako rovnocennější způsob, jak se dostat k zákazníkovi." | "Rozpočet na SEO se navíc nemusí rovnat rozpočtu na PPC, aby přinesl srovnatelný efekt v čase. Menší firmy, které si nemohou dovolit soutěžit v PPC aukcích s velkými hráči, tak SEO často využívají jako rovnocennější způsob, jak se dostat k zákazníkovi." |

**Ostatní kontroly bez nálezu:** otevření sekcí vede hodnotou (žádné "V této sekci..."), princip → mechanika → aplikace dodržen ve všech H2/H3, žádné casual markery ("prostě", "tak nějak", "celkem", "vlastně"), konzistentní vykání napříč celým textem, žádný hype jazyk, žádná povýšenost, žádná vágní tvrzení bez konkrétního "jak", emoční kalibrace v pořádku, case study (Kalkulátor.cz) korektně rámovaná jako "u klienta X" s explicitní no-guarantee větou, žádná falešná jistota.

## Step 5 — Struktura & formátování

**Audit odstavců (povinná první akce):** Zkontrolováno všech odstavců v článku po Kroku 4. Tři odstavce přesahovaly 100 slov a musely být rozděleny (povinné): H3 "Obsahové (on-page) SEO" (115 slov), H3 "Off-page SEO a linkbuilding" (107 slov), odstavec o AI vyhledávání v H2 "Proč je SEO důležité..." (~110 slov). Další dva odstavce byly pod hranicí 100 slov, ale rozděleny navíc kvůli "jedna myšlenka na odstavec" (H3 "Technické SEO" ~96 slov, mísilo definici/problémy/příklad migrace; odstavec o zavedené firmě a rozpočtu v H2 4 ~92 slov, mísilo dvě odlišné myšlenky).

**Délka článku:** STŘEDNÍ (1937 slov po úpravách v tomto kroku)

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | Odstavec rozdělen (povinné, >100 slov) | H3 "Obsahové (on-page) SEO" rozdělen na 2 odstavce | Audit odstavců — 115 slov |
| 2 | Odstavec rozdělen (povinné, >100 slov) | H3 "Off-page SEO a linkbuilding" rozdělen na 2 odstavce | Audit odstavců — 107 slov |
| 3 | Odstavec rozdělen (povinné, >100 slov) | Odstavec o AI vyhledávání v H2 "Proč je SEO důležité..." rozdělen na 2 odstavce | Audit odstavců — ~110 slov |
| 4 | Odstavec rozdělen (kvalitativní) | H3 "Technické SEO" rozdělen na 2 odstavce (definice/problémy vs. příklad migrace) | Pod hranicí 100 slov, ale mísil dvě odlišné myšlenky — Structure Guide "jedna myšlenka na odstavec" |
| 5 | Odstavec rozdělen (kvalitativní) | Odstavec o zavedené firmě/rozpočtu v H2 4 rozdělen na 2 odstavce | Stejný důvod jako #4 |
| 6 | H3 přidáno | "SEO vs. placená reklama" a "Pro koho se SEO vyplatí" pod H2 "Co znamená SEO..." | Sekce měla 6 odstavců za sebou bez vizuálního zlomu (Structure Guide sekce 4, limit 3) |
| 7 | H3 přidáno | "Jak pilíře vybrat a upřednostnit" pod H2 "Tři pilíře SEO..." | Syntetizující obsah napříč pilíři (dosud 4 odstavce za sebou po H3 Off-page) dostal vlastní podnadpis místo přívěsku k poslednímu pilíři |
| 8 | H3 přidáno (3×) | "Český trh: Google i Seznam", "Reálné výsledky, ne sliby", "SEO ve věku AI vyhledávání" pod H2 "Proč je SEO důležité..." | Sekce měla 8 odstavců za sebou bez vizuálního zlomu — nejzávažnější nález auditu, vyžadovalo rozdělení do 3 podsekcí |

**Kontrola hierarchie nadpisů:** 1× H1, 7× H2, 13× H3 — žádné přeskočené úrovně. 7 H2 na horní hranici doporučeného rozsahu (3–7), odpovídá schválené osnově z Kroku 2. Vysoký počet H3 (13) je přímý důsledek oprav #6–#8 z auditu odstavců, ne dekorativní přidání.

**Kontrola calloutů:** 2 (Tip, Keep in Mind) — v rámci limitu pro střední délku článku (2–3), žádné dva za sebou, max. 1 na H2 sekci.

**Kontrola tabulek:** 1 (Tři pilíře SEO v přehledu) — v rámci limitu pro střední délku (1–2); jde o klíčovou diferenciační tabulku definovanou v Kroku 2.

**Kontrola seznamů:** 1 odrážkový seznam (Klíčové závěry). Sekce "Časté mylné představy o SEO" ponechána jako 4 tučně uvozené odstavce místo seznamu — konzistentní s precedentem `marketingove-kpi-jak-je-vybrat-a-merit` a `webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing` (odpovídá vzoru ToV Guide, zachovává prostor pro vysvětlující větu u každé mylné představy).

**Navigační prvky:** Obsah (ToC) záměrně NEpřidán ručně do markdownu — `src/step4_html.py` ho generuje automaticky z H2/H3 nadpisů v Kroku 6. Interní odkazy: 6/6 z plánu Kroku 2 potvrzeno přítomných (SEO-02, SEO-20, SEO-27, SEO-04, AI-02, SEO-24). Sekce Zdroje přítomna s 2 externími citacemi.

**Autorská atribuce:** Záměrně NEpřidána ručně — `step4_html.py` generuje author-box automaticky (placeholder "evisions Advertising" / "Content Team") v Kroku 6. Content Plan Index Sheet nemá u SEO-32 vyplněný sloupec "zpracoval" — otevřená položka pro Krok 7.

**Otevřená položka pro Krok 6:** Zdrojové značky v hranatých závorkách v těle textu ([developers.google.com/search/docs/crawling-indexing] ×4, [zpravy.aktualne.cz/...] ×1) jsou pracovní QA značky z Kroku 3 — podle precedentu je potřeba je při HTML konverzi odstranit z těla textu (fakta zůstávají, zdroje jsou v sekci "Zdroje").

## Step 6 — HTML konverze

**Použitý nástroj:** `src/step4_html.py` (`convert_to_html()`) — deterministická konverze markdownu na evisions.cz šablonu.

**Opravy provedené před konverzí (dokončení otevřené položky z Kroku 5):**

Odstraněno 5× pracovní zdrojové značky v hranatých závorkách z těla textu (4× [developers.google.com/search/docs/crawling-indexing] v sekci "Jak funguje vyhledávač", 1× [zpravy.aktualne.cz/...] v sekci "Český trh: Google i Seznam"). Fakta beze změny, zdroje zůstávají dostupné v sekci "Zdroje" na konci článku.

| # | Element | Description |
|---|---------|-------------|
| 1 | Struktura stránky | Header, breadcrumb, ToC, article, author-box, disclaimer, footer — v povinném pořadí |
| 2 | ToC | Vygenerováno automaticky z H2/H3 nadpisů (20 položek: 7 H2 + 13 H3) |
| 3 | Callouty | 2 stylované bloky (Tip, Keep in Mind) převedeny na `callout` divy se správnou CSS třídou |
| 4 | Meta title | `<title>` z H1 vyšel jen na 42 znaků (pod SEO limitem 50–60) — ručně nahrazen rozšířenou variantou "Co je SEO a jak funguje: základy \| evisions.cz Blog" (51 znaků). H1 v těle beze změny. |
| 5 | Meta popisek | Doplněn ručně (šablona ho negeneruje automaticky): "Co je SEO, jak funguje vyhledávač a na jaké tři pilíře optimalizace (technické, obsahové, off-page) se zaměřit. Vysvětlení s příklady z praxe evisions." (151 znaků) |
| 6 | Autor box | Auto-generován šablonou s placeholder hodnotou "evisions Advertising" / "Content Team" — Content Plan Index Sheet nemá u SEO-32 vyplněný sloupec "zpracoval", ke skutečné atribuci viz otevřená položka z Kroku 5 |
| 7 | Poznámka k obsahu | Vygenerována automaticky šablonou (nebyla duplikována ručně) |

**Oprava názvu souboru:** `convert_to_html()` ukládá výstup jako `{slug}_CZ.html` bez prefixu `article_` — přejmenováno na `article_co-je-seo-a-jak-funguje_CZ.html` podle konvence pojmenování projektu (CLAUDE.md).

**Kontrola po konverzi:** 1 tabulka, 2 callouty (1× Tip, 1× Keep in Mind), 7× `<h2>`, 13× `<h3>` — odpovídá Kroku 5.

**Nástroj pro log HTML:** `src/generate_write_log.py` — vygenerováno `article_co-je-seo-a-jak-funguje_CZ_log.html`.

**Finální počet slov (article_..._CZ.md):** ~1937 (beze změny oproti Kroku 5, jen odstranění zdrojových značek v tomto kroku)

**Soubory vygenerovány:**
- `data/output/articles/co-je-seo-a-jak-funguje/article_co-je-seo-a-jak-funguje_CZ.html`
- `data/output/articles/co-je-seo-a-jak-funguje/article_co-je-seo-a-jak-funguje_CZ_log.html`

## Step 7 — QA + aktualizace Content Plan

### Content validace — marketingový expert review

- [x] Všechna fakta technicky přesná — mechanika crawling/indexace/ranking odpovídá Google Search Central dokumentaci, podíl Google/Seznam v ČR podložen zdrojem, žádné kontroverzní tvrzení
- [x] Žádné zjednodušení, které by čtenáře zmátlo — tři pilíře SEO odlišeny jasně, rozdíl SEO vs. PPC vysvětlen na konkrétních důsledcích (kdy návštěvnost končí/zůstává)
- [x] Koncepty vysvětleny ve správném pořadí — definice → mechanika vyhledávače → tři pilíře s dalším směrem → byznys relevance (CZ trh, case study, AI) → mylné představy → závěr
- [x] Příklady realistické a relevantní — case study Kalkulátor.cz s explicitní no-guarantee větou, modelové technické problémy (pomalé načítání, chybějící přesměrování) konkrétní a ověřitelné
- [x] Nic nechybí, co by čtenář v tématu očekával — hloubkový keyword research/on-page checklist/technický audit záměrně vynechány (zdůvodněno v Kroku 2, patří sourozeneckým TODO článkům ve Skupině 11)

### QA Checklist

**Přesnost obsahu**
- [x] Všechna fakta odpovídají zdroji citovanému v Kroku 3 (zdroje teď jen v sekci "Zdroje", ne inline — viz Krok 6)
- [x] Žádné informace nepřidány ani neodebrány oproti schválenému draftu (Krok 5–6 měnily jen prezentaci: nové H3 podnadpisy, dělení odstavců, odstranění pracovních citačních značek)
- [x] Odkazy strukturálně validní — 6 interních odkazů míří na Published články z ledgeru (SEO-02, SEO-20, SEO-27, SEO-04, AI-02, SEO-24), 2 externí zdroje dohledány WebSearchem v Kroku 1
- [ ] Obrázky na správných pozicích — N/A, článek je čistě textový

**ToV compliance**
- [x] Tón odpovídá ToV Guide (How-to/definiční) — ověřeno v Kroku 4 (5 problémů nalezeno a opraveno, vše rytmus vět), žádný nález při finální kontrole
- [x] Žádné zakázané fráze — potvrzeno v Kroku 4
- [x] Žádné garance konkrétních výsledků — case study Kalkulátor.cz explicitně rámovaná jako "u klienta X", s větou o negarantování stejného výsledku

**Structure compliance**
- [x] E-E-A-T prvky přítomny — autor box (placeholder "Content Team" / "evisions Advertising"), datum aktualizace auto-generováno, sekce Zdroje s 2 citacemi
- [x] Hierarchie nadpisů správná — 1× H1, 7× H2, 13× H3, žádné přeskočené úrovně
- [x] Interní odkazy přítomny — 6/6 z plánu Kroku 2

**Technické**
- [x] HTML se správně renderuje — ověřeno čtením vygenerovaného souboru + kontrolou počtu calloutů/tabulek/nadpisů proti očekávání z Kroku 5 (přesná shoda)
- [ ] Obrázky se načítají — N/A
- [x] Žádné nefunkční odkazy zjištěny při statické kontrole

**Doplňkové (Write Workflow)**
- [x] Zdrojové citace u všech faktických tvrzení — 2 zdroje v sekci "Zdroje"
- [x] Žádné [SOURCE NEEDED], [IMAGE NEEDED] ani jiné placeholder značky — ověřeno grep kontrolou nad finálním markdownem

**Verdikt: PASS**

### Soubory k uložení — kontrola 4/4

- [x] `article_co-je-seo-a-jak-funguje_CZ.md`
- [x] `article_co-je-seo-a-jak-funguje_CZ_log.md`
- [x] `article_co-je-seo-a-jak-funguje_CZ.html`
- [x] `article_co-je-seo-a-jak-funguje_CZ_log.html`

### Aktualizace Content Plan Sheetu a lokálního ledgeru

**Rozhodnutí:** Status v ledgeru ZŮSTÁVÁ "In Progress", NEpřesunuto na "Published" — stejné zdůvodnění jako u SEO-30 (Marketingové KPI). Článek nebyl nahraný na živý evisions.cz web, URL sloupec v ledgeru je stále "—". Označení "Published" bez živé URL by bylo nepřesné. Ledger i xlsx mirror zůstávají beze změny — QA proběhlo a obsah je připraven k publikaci, samotné nahrání na web je krok mimo tento nástroj.

**Až bude článek nahraný na živý web:** dodat živou URL, pak provést: (1) editovat řádek SEO-32 v `data/output/content_plan_index.md` — Status → Published, doplnit URL; (2) `.venv/Scripts/python.exe src/generate_content_plan_xlsx.py`; (3) vypsat řádek k ručnímu vložení do Google Sheetu (ID SEO-32, Status Published, URL).
