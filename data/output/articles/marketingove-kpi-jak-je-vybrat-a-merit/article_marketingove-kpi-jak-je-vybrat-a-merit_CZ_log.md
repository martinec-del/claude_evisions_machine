# Log: Marketingové KPI: jak je vybrat a měřit

**Slug:** marketingove-kpi-jak-je-vybrat-a-merit
**Content Plan:** SEO-30 — Kategorie: SEO, podskupina "3 – Analytika a metriky" (`topic_cluster_analytika-a-metriky_CZ`)
**Content Plan zdroj:** data/output/content_plan_index.md (lokální ledger, TODO položka nalezena a přeřazena na In Progress se SEO-30)
**Typ obsahu:** How-to / edukativní (viz ToV Guide sekce 4)
**Vytvořeno:** 2026-08-19

## Init

- Krok 0 Duplicate Check: shoda s TODO položkou "Marketingové KPI: jak je vybrat a měřit" v `content_plan_index.md` pod SEO — Skupina 3 (Analytika a metriky). Žádný Published článek na téma nenalezen. Přiřazeno ID SEO-30, Next ID posunuto na SEO-31.
- Žádná existující verze ve `data/output/articles/marketingove-kpi-jak-je-vybrat-a-merit/` — NEW mode, v1.
- Příbuzné publikované/rozpracované obsahy ve stejné podskupině (kandidáti na interní prolinkování):
  - SEO-07 — Universal Analytics končí, ať žije Google Analytics 4! — https://www.evisions.cz/blog/universal-analytics-konci-at-zije-google-analytics-4/
  - SEO-19 — Share of Voice (SOV): K čemu je a jak metriku spočítat? — https://www.evisions.cz/blog/share-of-voice-sov-k-cemu-je-a-jak-metriku-spocitat/
  - SEO-21 — Google Search Console: Jak ji v SEO využít naplno? — https://www.evisions.cz/blog/google-search-console-jak-ji-v-seo-vyuzit-naplno/
  - Rozpracovaný draft (Krok 6 hotov, Krok 7 chybí) — Webová analytika: co to je a jak ji využít pro marketing — `data/output/articles/webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing/`

## Step 1 — Konkurenční research + klíčová slova

**Seed keyword:** "marketingové KPI" (ověřeno přes WebSearch — reálně používaný termín v CZ marketingových blozích, žádné rozpory s intent)

**Provider:** Ahrefs MCP (domain rating, site-explorer-metrics s `protocol=https` — bez tohoto parametru endpoint padal na "internal server error", `mode=exact`) + keywords-explorer (matching-terms, related-terms)

**URL research:** 4 WebSearch dotazy ("marketingové KPI vysvětleno", "marketingové KPI návod", "jak na marketingové KPI", "jak vybrat správné KPI pro marketing") → 11 unikátních CZ URL po deduplikaci (1 mezinárodní/anglický zdroj ui42.com vyřazen). Obohaceno o DR + organic traffic. Top 10 dle DR (radanakoppova.cz vyřazeno — DR 0, nejslabší). 9 z 10 úspěšně fetchnuto; yashica-digital.cz/co-je-kpi/ vrátil obsah homepage agentury místo cílového článku — označeno FETCH MISMATCH ve xlsx, nepoužito pro content gap analýzu.

**Klíčový content gap:** Žádný z 9 fetchnutých konkurenčních článků nenabízí přehlednou tabulku "KPI podle marketingového kanálu a fáze funnelu" ani reálnou case study s konkrétními čísly z agenturní praxe. Lagging vs. leading KPI a KPI benchmark zmiňuje jen mytimi.cz, povrchně. Nikdo nepropojuje výběr KPI s konkrétními měřicími nástroji (GA4, Search Console) ani s vlastními zdroji.

**Kanibalizace v rámci vlastního clusteru (topic_cluster_analytika-a-metriky_CZ):** GA4 pokrývá SEO-07, Search Console SEO-21, Share of Voice SEO-19, obecná webová analytika rozpracovaný draft (viz Init) — tento článek proto tyto nástroje/metriky jen zmíní a prolinkuje, s důrazem na výběr a metodiku KPI (SMART, lagging/leading), ne na jednotlivé nástroje.

**Klíčová slova:** 30 navrženo (viz xlsx list "Keywords") — hlavní cluster "kpi marketing" / "marketing kpi" / "kpi v marketingu" (~140/měsíc kombinovaně), definiční cluster kolem "co je kpi" / "kpi zkratka" / "kpi ukazatele" (~1500+/měsíc kombinovaně), metodologický cluster "smart kpi" / "okr vs kpi", praktický cluster "kpi příklady" / "kpi výpočet" / "kpi dashboard" / "kpi tabulka", plus KPI metriky jako konkrétní příklady (konverzní poměr, návratnost investic, návštěvnost webu, ppc kpi). Mimo-oborové výsledky (výroba, HR, logistika, supply chain) vyřazeny jako irelevantní pro marketingový úhel.

**Marketing Miner cross-check (nově formalizováno jako krok 5.5 v `prompts/write_step1_research.md`):** `python src/marketing_miner_api.py volume ...` na 8 hlavních keywordech — čísla se s Ahrefs shodují v řádu (co je kpi 450 vs Ahrefs 400, kpi marketing 70 vs 80, konverzní poměr 170 vs 200...), žádný extrémní rozpor nenalezen. "marketingové kpi" nemá data ani v MM — potvrzuje, že jde o frázi pod trackovaným prahem v obou nástrojích, ne o chybu Ahrefs. `suggestions` na seed "kpi marketing" nepřinesl nové CZ-relevantní nápady — téměř výhradně anglické long-tail varianty s volume 10/měsíc. Cross-check hodnoty zapsány do sloupce Notes v listu "Keywords". Nutné volat s `PYTHONUTF8=1 PYTHONIOENCODING=utf-8`, jinak se diakritika v argumentech poškodí a API nenajde shodu.

**xlsx uložen:** `data/output/articles/marketingove-kpi-jak-je-vybrat-a-merit/marketingove-kpi-jak-je-vybrat-a-merit_step1.xlsx`

## Step 2 — Brief & osnova

**Typ obsahu:** How-to / trend analýza — téma je definiční a metodologické (výběr a měření KPI), case study formát by nedával smysl.

**Cíl počtu slov:** 1900–2200 (konkurenční průměr ze Step 1 ~2030 slov, mírně zúženo kvůli vynechání hloubkového GA4/Search Console výkladu — kanibalizace v rámci clusteru).

**Diferenciace od konkurence:** Tabulka "KPI podle marketingového kanálu a fáze funnelu" (content gap ze Step 1, žádný konkurenční článek ji nenabízí). Krátký ilustrativní příklad s konkrétními čísly z agenturní praxe místo abstraktních tvrzení. Lagging vs. leading KPI rozvinuto do praktického doporučení. Záměrně vynecháno: hloubkový výklad GA4/Search Console (pokryto jinde v clusteru) a hloubkový PPC-specifický rozbor (patří do PPC kategorie).

**Kostra nadpisů (H2):**
1. Co je KPI a čím se liší od cíle a metriky (+ H3 KPI vs. cíl vs. metrika)
2. Jak vybrat správné marketingové KPI (+ H3 SMART metoda pro výběr KPI, H3 Lagging vs. leading KPI)
3. Příklady marketingových KPI podle kanálu a fáze funnelu (+ H3 tabulka KPI podle kanálu a fáze funnelu)
4. Jak KPI měřit a reportovat
5. Časté chyby při práci s marketingovými KPI
6. Klíčové závěry
7. Zdroje

**Plán interních odkazů (5, + 1 kandidát po publikaci):**

| # | Cílový článek | Umístění |
|---|----------------|----------|
| 1 | Universal Analytics končí, ať žije Google Analytics 4! (SEO-07) | H2 "Jak KPI měřit a reportovat" |
| 2 | Google Search Console: Jak ji v SEO využít naplno? (SEO-21) | H2 "Jak KPI měřit a reportovat" |
| 3 | Share of Voice (SOV) (SEO-19) | H3 "KPI podle kanálu a fáze funnelu" |
| 4 | 6 hlavních linkbuildingových metrik (SEO-27) | H3 "KPI podle kanálu a fáze funnelu" |
| 5 | Cíle reklamy na Facebooku: dosah, návštěvnost, nebo konverze? (PPC-12) | H3 "KPI podle kanálu a fáze funnelu" |

**Content validace:** PASS — struktura logicky odpovídá tématu (definice → metodika výběru → příklady → měření → chyby → závěr), všechny klíčové koncepty pro How-to obsah přítomny, pořadí sekcí didakticky správné, chybějící hloubka u GA4/GSC je záměrná (zdůvodněno diferenciací, ne opomenutí).

**Osnova uložena:** `data/output/articles/marketingove-kpi-jak-je-vybrat-a-merit/article_marketingove-kpi-jak-je-vybrat-a-merit_CZ_outline.docx`

## Step 3 — Draft

**Typ obsahu:** How-to / trend analýza
**Počet slov:** 1906 (cíl: 1900–2200)

### Integrace klíčových slov

| # | Keyword | Volume | Umístění | Kontextová věta |
|---|---------|--------|-----------|-------------------|
| 1 | marketingové kpi / kpi marketing | 80 (MM cross-check 70) | H1 | "Marketingové KPI: jak je vybrat a měřit" |
| 2 | co je kpi | 400 | H2 "Co je KPI a čím se liší od cíle a metriky" (nadpis + definice) | "KPI (Key Performance Indicator, česky klíčový ukazatel výkonnosti) je měřitelný ukazatel, který ukazuje, jak si vedete vůči konkrétnímu cíli." |
| 3 | klíčové ukazatele výkonnosti | 80 | Úvodní definice v H2 1 | "KPI (Key Performance Indicator, česky klíčový ukazatel výkonnosti)..." |
| 4 | smart kpi | 10 | H3 "SMART metoda pro výběr KPI" | Nadpis + rozbor jednotlivých písmen metody |
| 5 | kpi příklady | 100 | H2 "Příklady marketingových KPI podle kanálu a fáze funnelu" | Nadpis + tabulka |
| 6 | kpi dashboard | 50 (MM cross-check 40) | H2 "Jak KPI měřit a reportovat" | "KPI dashboard, který míchá oba rytmy do jednoho pohledu bez rozlišení, obvykle vede k tomu, že tým reaguje na šum..." |
| 7 | konverzní poměr | 200 (MM cross-check 170) | Napříč článkem (definice, tabulka, příklady) | "Konverzní poměr je ukazatel, podle kterého poznáte, jestli se k cíli blížíte — třeba konverzní poměr e-shopu." |
| 8 | návratnost investic | 70 | H2 "Jak KPI měřit a reportovat" | "Návratnost investic (ROI) nebo návratnost výdajů na reklamu (ROAS) patří mezi KPI, které nejde vyčíst z jednoho nástroje..." |
| 9 | ppc kpi | 80 | H2/H3 "Příklady..." (řádek PPC v tabulce + odstavec o cílech Facebook reklamy) | Tabulka + "U PPC kanálů se KPI liší i podle zvoleného cíle kampaně." |

### Odchylky od osnovy

| # | Typ | Popis | Důvod |
|---|-----|-------|--------|
| 1 | Rozšíření (ne strukturální) | Sekce "Co je KPI", "Jak vybrat KPI" (SMART), "Příklady podle kanálu" a "Jak KPI měřit" dostaly o 1 odstavec navíc oproti bodům v osnově (např. rozbor S/M vedle D/R v SMART, odstavec o frekvenci reportingu, odstavec o přístupu k dashboardu pro celý tým, odstavec o logice fází funnelu) | První draft dle přesných bodů osnovy vyšel na ~1200 slov, pod cílem 1900–2200. Rozšíření je věcné (nové konkrétní příklady/doporučení v rámci již schválených H2/H3), ne výplňové — žádný nový nadpis nepřibyl ani neubyl. |
| 2 | Rozšíření | Přidána 5. častá chyba "Kopírování KPI od konkurence bez vlastního kontextu" nad rámec 4 bodů v osnově | Navazuje na content gap ze Step 1 (topranker.cz zmiňuje KPI benchmark) a dorovnává rozsah sekce k ostatním prohloubeným sekcím. |

### Plný článek se zdroji

Uložen v `article_marketingove-kpi-jak-je-vybrat-a-merit_CZ.md`. Faktická tvrzení převzatá z konkurenčního researche Step 1 označena v textu zdrojem v hranaté závorce ([marketingppc.cz], [mytimi.cz], [ppcprofits.cz], [grapefruit.cz], [topranker.cz]) a shrnuta v sekci Zdroje na konci článku. Modelový příklad v sekci "Příklady..." je explicitně označen jako ilustrativní ("Modelový příklad"), ne jako reálná klientská case study — v souladu s Structure Guide sekcí 3 (Požadavky na faktickou přesnost, žádné neověřitelné konkrétní výsledky).

## Step 4 — ToV Check

**Zkontrolováno vět:** ~85
**Nalezeno problémů:** 4

| # | Location | Issue Type | Original (full sentence) | Corrected (full sentence) |
|---|----------|------------|---------------------------|----------------------------|
| 1 | H2 "Časté chyby při práci s marketingovými KPI", úvodní věta | Rekapitulace ("z předchozích kapitol") — ToV Guide sekce 5, "Jak jsme již zmínili…" → smazat, nerekapitulovat | "I se správně zvolenými KPI z předchozích kapitol se dá jejich smysl v praxi snadno rozmělnit. Pět nejčastějších chyb se opakuje napříč obory i velikostí firem." | "Správně zvolené KPI se dá v praxi snadno rozmělnit. Pět nejčastějších chyb se opakuje napříč obory i velikostí firem." |
| 2 | H3 "SMART metoda pro výběr KPI", odstavec o písmenu M | Rytmus — jedna souvětná věta ~38 slov, nad doporučených 10–18 slov průměr | "Měřitelné vyžaduje jasně definovaný zdroj dat ještě předtím, než KPI začnete sledovat — pokud si tým neshodne, jestli konverzi počítá GA4 nebo interní CRM, výsledná čísla se budou lišit a diskuze se zvrhne v spor o data místo o strategii." | "Měřitelné vyžaduje jasně definovaný zdroj dat ještě předtím, než KPI začnete sledovat. Pokud si tým neshodne, jestli konverzi počítá GA4 nebo interní CRM, výsledná čísla se budou lišit a diskuze se zvrhne v spor o data místo o strategii." |
| 3 | H3 "SMART metoda pro výběr KPI", odstavec o písmenu R | Rytmus — souvětná věta ~34 slov | "Relevantní zase odděluje KPI od aktivit, které jen dobře vypadají v prezentaci pro vedení — počet publikovaných článků nebo příspěvků na sociálních sítích je aktivita, ne výsledek, pokud se neváže na konkrétní obchodní dopad." | "Relevantní zase odděluje KPI od aktivit, které jen dobře vypadají v prezentaci pro vedení. Počet publikovaných článků nebo příspěvků na sociálních sítích je aktivita, ne výsledek — pokud se neváže na konkrétní obchodní dopad." |
| 4 | H2 "Jak KPI měřit a reportovat", odstavec o frekvenci reportingu | Rytmus — 4. věta v řadě bez krátké kontrastní věty, 22 slov nad doporučeným průměrem | "KPI dashboard, který míchá oba rytmy do jednoho pohledu bez rozlišení, obvykle vede k tomu, že tým reaguje na šum místo na skutečný trend." | "KPI dashboard bez tohoto rozlišení obvykle vede k jednomu efektu: tým reaguje na šum, ne na skutečný trend." |

**Ostatní kontroly bez nálezu:** žádné casual markery ("prostě", "tak nějak", "celkem", "vlastně"), žádný hype jazyk, žádná povýšenost, žádná vágní tvrzení bez konkrétního "jak", konzistentní vykání napříč celým textem, emoční kalibrace v pořádku, modelový příklad korektně rámovaný jako ilustrativní (ne jako neověřitelný reálný výsledek).

## Step 5 — Struktura & formátování

**Audit odstavců (povinná první akce):** Zkontrolováno všech 21 odstavců v článku. Žádný nepřekračuje 100 slov (nejdelší, odstavec o socialu a e-mailu v sekci "Příklady...", má ~93 slov). Žádné rozdělení odstavce podle délky nebylo potřeba.

**Délka článku:** STŘEDNÍ (~1915 slov po úpravách v tomto kroku)

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | Callout typ opraven | Label "Modelový příklad:" v sekci "Příklady marketingových KPI podle kanálu a fáze funnelu" změněn na "Example:" (text "Modelový příklad z praxe —" zachován uvnitř bloku) | `src/step4_html.py` mapuje callout styl jen na přesné labely tip/warning/important/note/keep in mind/example (`CALLOUT_MAP`) — "Modelový příklad" by se v Kroku 6 vyrenderoval jako nestylovaný blockquote místo callout boxu. Ilustrativní rámování (Structure Guide sekce 3) zachováno v textu bloku. |
| 2 | H3 přidáno | "Frekvence reportingu a nástroje" pod H2 "Jak KPI měřit a reportovat" | Structure: sekce měla 6 po sobě jdoucích odstavců bez vizuálního zlomu (Structure Guide sekce 4, limit 3) — rozdělení na podsekce obnovuje skenovatelnost |
| 3 | H3 přidáno | "Revize KPI a přístup k dashboardu" pod H2 "Jak KPI měřit a reportovat" | Stejný důvod jako #2 — druhá polovina sekce (KPI audit + přístup týmu k dashboardu) dostala vlastní podnadpis |

**Kontrola hierarchie nadpisů:** 1× H1, 7× H2 (5 obsahových sekcí + Klíčové závěry + Zdroje), 6× H3 (4 původní + 2 nové) — žádné přeskočené úrovně. 7 H2 je na horní hranici doporučeného rozsahu (3–7), odpovídá schválené osnově z Kroku 2 (7 H2 bodů včetně Klíčových závěrů a Zdrojů).

**Kontrola calloutů:** 3 (Tip, Example, Keep in Mind) — v rámci limitu pro střední délku článku (2–3), žádné dva za sebou, max. 1 na H2 sekci.

**Kontrola tabulek:** 2 (KPI vs. cíl vs. metrika; KPI podle kanálu a fáze funnelu) — v rámci limitu pro střední délku (1–2).

**Kontrola seznamů:** 2 odrážkové seznamy (SMART kritéria; Klíčové závěry). Sekce "Časté chyby při práci s marketingovými KPI" ponechána jako 5 tučně uvozených odstavců místo seznamu — konzistentní s precedentem `webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing` (odpovídá vzoru ToV Guide, zachovává prostor pro vysvětlující větu u každé chyby).

**Navigační prvky:** Obsah (ToC) záměrně NEpřidán ručně do markdownu — `src/step4_html.py` ho generuje automaticky z H2/H3 nadpisů v Kroku 6 (ruční verze by v předchozím projektu vedla k duplicitě a nefunkčním anchor odkazům, viz log `webova-analytika...` Krok 6 oprava #1). Interní odkazy: 5/5 z plánu Kroku 2 potvrzeno přítomných (SEO-07, SEO-21, SEO-19, SEO-27 linkbuilding, PPC-12 Facebook). Sekce Zdroje přítomna s 5 externími citacemi.

**Autorská atribuce:** Záměrně NEpřidána ručně — `step4_html.py` generuje author-box automaticky (placeholder "evisions Advertising" / "Content Team") v Kroku 6. Content Plan Index Sheet nemá u SEO-30 vyplněný sloupec "zpracoval" — otevřená položka pro Krok 7.

**Otevřená položka pro Krok 6:** Zdrojové značky v hranatých závorkách v těle textu ([marketingppc.cz], [mytimi.cz], [ppcprofits.cz], [grapefruit.cz], [topranker.cz]) jsou pracovní QA značky z Kroku 3 — podle precedentu (`webova-analytika...` Krok 6) je potřeba je při HTML konverzi odstranit z těla textu (fakta zůstávají, zdroje jsou v sekci "Zdroje").

## Step 6 — HTML konverze

**Použitý nástroj:** `src/step4_html.py` (`convert_to_html()`) — deterministická konverze markdownu na evisions.cz šablonu.

**Opravy provedené před konverzí (dokončení otevřené položky z Kroku 5):**

Odstraněno 8× pracovní zdrojové značky v hranatých závorkách z těla textu (např. "...která nikomu nepomůžou se rozhodnout [marketingppc.cz]." → "...která nikomu nepomůžou se rozhodnout.") — 2× [marketingppc.cz], 2× [mytimi.cz], 1× [grapefruit.cz], 1× [ppcprofits.cz], 2× [topranker.cz]. Fakta beze změny, zdroje zůstávají dostupné v sekci "Zdroje" na konci článku. Odpovídá stejné opravě provedené u precedentu `webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing` (Krok 6, oprava #2).

| # | Element | Description |
|---|---------|-------------|
| 1 | Struktura stránky | Header, breadcrumb, ToC, article, author-box, disclaimer, footer — v povinném pořadí |
| 2 | ToC | Vygenerováno automaticky z H2/H3 nadpisů (13 položek: 7 H2 + 6 H3) |
| 3 | Callouty | 3 stylované bloky (Tip, Example, Keep in Mind) převedeny na `callout` divy se správnou CSS třídou — label "Example" (opraveno v Kroku 5) se správně namapoval na `callout-example` |
| 4 | Meta title | `<title>` vygenerován automaticky šablonou z H1 ("Marketingové KPI: jak je vybrat a měřit \| evisions.cz Blog", 58 znaků) — v SEO limitu 50–60 znaků, žádná ruční úprava nutná |
| 5 | Meta popisek | Doplněn ručně (šablona ho negeneruje automaticky): "Jak vybrat a měřit marketingové KPI podle SMART metody, kanálu a fáze funnelu. Praktické příklady, časté chyby a tipy pro reporting i výběr nástrojů." (149 znaků — mírně pod cílových 150–160, akceptováno) |
| 6 | Autor box | Auto-generován šablonou s placeholder hodnotou "evisions Advertising" / "Content Team" — Content Plan Index Sheet nemá u SEO-30 vyplněný sloupec "zpracoval", ke skutečné atribuci viz otevřená položka z Kroku 5 |
| 7 | Poznámka k obsahu | Vygenerována automaticky šablonou (nebyla duplikována ručně) |

**Oprava názvu souboru:** `convert_to_html()` ukládá výstup jako `{slug}_CZ.html` bez prefixu `article_` — přejmenováno na `article_marketingove-kpi-jak-je-vybrat-a-merit_CZ.html` podle konvence pojmenování projektu (CLAUDE.md).

**Nástroj pro log HTML:** `src/generate_write_log.py` (viz `webova-analytika...` Krok 6) — vygenerováno `article_marketingove-kpi-jak-je-vybrat-a-merit_CZ_log.html`.

**Finální počet slov (article_..._CZ.md):** ~1910 (po Kroku 5 úpravách a odstranění zdrojových značek v tomto kroku, obsahově beze změny oproti Kroku 4)

**Soubory vygenerovány:**
- `data/output/articles/marketingove-kpi-jak-je-vybrat-a-merit/article_marketingove-kpi-jak-je-vybrat-a-merit_CZ.html`
- `data/output/articles/marketingove-kpi-jak-je-vybrat-a-merit/article_marketingove-kpi-jak-je-vybrat-a-merit_CZ_log.html`

## Step 7 — QA + aktualizace Content Plan

### Content validace — marketingový expert review

- [x] Všechna fakta technicky přesná — standardní, nesporné marketingové koncepty (definice KPI, SMART, lagging/leading, funnel fáze), žádné kontroverzní tvrzení
- [x] Žádné zjednodušení, které by čtenáře zmátlo — SMART písmena, lagging/leading pár u SEO/PPC/e-mailu vysvětleny s konkrétními příklady, ne jen abstraktně
- [x] Koncepty vysvětleny ve správném pořadí — definice → výběr metody (SMART, lagging/leading) → příklady dle kanálu/funnelu → měření a reporting → časté chyby → závěr
- [x] Příklady realistické a relevantní — modelový příklad (e-shop CTR→CPA) explicitně označen jako ilustrativní, ne jako neověřitelný reálný klientský výsledek (Structure Guide sekce 3)
- [x] Nic nechybí, co by čtenář v tématu očekával — hloubkový GA4/GSC výklad záměrně vynechán kvůli kanibalizaci v rámci clusteru (zdůvodněno v Kroku 2), zbytek tématu pokryt kompletně

### QA Checklist

**Přesnost obsahu**
- [x] Všechna fakta odpovídají zdroji citovanému v Kroku 3 (zdroje teď jen v sekci "Zdroje", ne inline — viz Krok 6)
- [x] Žádné informace nepřidány ani neodebrány oproti schválenému draftu (Krok 5–6 měnily jen prezentaci: nadpisy, callout label, odstranění pracovních citačních značek)
- [x] Odkazy strukturálně validní — 5 interních odkazů míří na Published články z ledgeru (SEO-07, SEO-21, SEO-19, SEO-27, PPC-12), 5 externích zdrojů dohledáno WebSearchem v Kroku 1
- [ ] Obrázky na správných pozicích — N/A, článek je čistě textový (žádná Mapa obrázků v osnově Kroku 2)

**ToV compliance**
- [x] Tón odpovídá ToV Guide (How-to/edukativní) — ověřeno v Kroku 4 (4 problémy nalezeny a opraveny), žádný nález při finální kontrole
- [x] Žádné zakázané fráze — potvrzeno v Kroku 4
- [x] Žádné garance konkrétních výsledků — modelový příklad rámovaný jako ilustrativní

**Structure compliance**
- [x] E-E-A-T prvky přítomny — autor box (placeholder "Content Team" / "evisions Advertising", Content Plan Sheet nemá u SEO-30 vyplněné "zpracoval"), datum aktualizace auto-generováno, sekce Zdroje s 5 citacemi
- [x] Hierarchie nadpisů správná — 1× H1, 7× H2, 6× H3, žádné přeskočené úrovně
- [x] Interní odkazy přítomny — 5/5 z plánu Kroku 2

**Technické**
- [x] HTML se správně renderuje — ověřeno čtením vygenerovaného souboru (ToC anchor ID odpovídají heading ID, callouty mají správné CSS třídy, tabulky a seznamy strukturálně validní)
- [ ] Obrázky se načítají — N/A
- [x] Žádné nefunkční odkazy zjištěny při statické kontrole (viz "Přesnost obsahu" výše)

**Doplňkové (Write Workflow)**
- [x] Zdrojové citace u všech faktických tvrzení — 5 zdrojů v sekci "Zdroje"
- [x] Žádné [SOURCE NEEDED], [IMAGE NEEDED] ani jiné placeholder značky — ověřeno grep kontrolou nad finálním markdownem

**Verdikt: PASS**

### Soubory k uložení — kontrola 4/4

- [x] `article_marketingove-kpi-jak-je-vybrat-a-merit_CZ.md`
- [x] `article_marketingove-kpi-jak-je-vybrat-a-merit_CZ_log.md`
- [x] `article_marketingove-kpi-jak-je-vybrat-a-merit_CZ.html`
- [x] `article_marketingove-kpi-jak-je-vybrat-a-merit_CZ_log.html`

### Aktualizace Content Plan Sheetu a lokálního ledgeru

**Rozhodnutí:** Status v ledgeru ZŮSTÁVÁ "In Progress", NEpřesunuto na "Published". Workflow guide (sekce 12) předpokládá přesun na Published + zápis živé URL po skutečném publikování — ten zatím neproběhl (článek nebyl nahrán na živý web, URL sloupec v ledgeru je stále "—"). Označení "Published" bez živé URL by bylo nepřesné a mohlo by v ledgeru vytvořit falešný dojem, že je téma vyřízené. Ledger i xlsx mirror proto zůstávají beze změny — QA proběhlo a obsah je připraven k publikaci, ale samotné publikování (nahrání na evisions.cz) je krok mimo tento nástroj.

**Až bude článek nahraný na živý web:** dodat živou URL, pak provést: (1) editovat řádek SEO-30 v `data/output/content_plan_index.md` — Status → Published, doplnit URL; (2) `.venv/Scripts/python.exe src/generate_content_plan_xlsx.py`; (3) vypsat řádek k ručnímu vložení do Google Sheetu (ID SEO-30, Status Published, URL).
