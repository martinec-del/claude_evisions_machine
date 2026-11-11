# Content Plan Index — lokální dedup ledger

**Účel:** Zabránit duplicitní tvorbě obsahu. Google Drive MCP umí Content Plan Sheet pouze **číst**, ne zapisovat jednotlivé buňky — tento soubor je proto lokální zdroj pravdy pro (1) kontrolu, jestli téma/keyword už existuje nebo je plánované, a (2) přiřazování dalšího volného ID v rámci kategorie.

**Primární Sheet:** [Content Plan Index Sheet](https://docs.google.com/spreadsheets/d/1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q/edit?gid=754600260#gid=754600260) — uživatelova editovatelná kopie tohoto ledgeru/xlsx mirroru, nahraná do Google Drive 2026-08-18. Struktura je identická s tímto souborem (vznikl z něj), takže refresh odsud je 1:1.
**Sekundární Sheet (jen na vyžádání):** [původní evisions.cz - Content Plan](https://docs.google.com/spreadsheets/d/1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY/edit?gid=1262896623#gid=1262896623) — bohatší historická data (Lokace, zpracoval, klíčová slova, brief), ale už se nečte automaticky.
**Poslední plný sync s primárním Sheetem:** 2026-08-18 (počáteční sync proběhl ze sekundárního Sheetu; primární Sheet v té chvíli vznikal jako jeho kopie, takže obsah odpovídá)

---

## Jak se tento soubor používá

**`/evisions-new-article`** (viz `evisions_write_workflow_CZ.md` Krok 0):

1. **Před vytvořením nového článku** zkontrolovat zadané téma/keyword proti tabulkám níže:
   - Shoda s existujícím **Published** řádkem (ID/URL) → NENÍ nový článek, přesměrovat na `/evisions-rewrite-article`.
   - Shoda s řádkem v sekci **TODO / plánovaná témata** → téma už je v plánu; pokračovat pod jeho existujícím zařazením (Skupina/kategorie), ne jako úplně nová položka.
   - Žádná shoda → skutečně nové téma.
2. **Přiřazení ID:** pokud je téma nové a nemá ID, vzít další volné číslo z tabulky "Next ID per kategorie" níže, zvýšit ho v tomto souboru (Edit) a nastavit odpovídající "Next ID" na +1 pro příští běh.
3. **Výstup pro uživatele:** Init Summary vypíše hotový řádek (ID, Kapitola/Nadpis, klíčová slova, Typ obsahu, Status, složka s výstupy) k **ručnímu vložení** do Google Sheetu — MCP zápis do buněk neumí.
4. **Po publikaci** (Krok 7) aktualizovat v tomto souboru Status řádku na "Published" + doplnit URL, zrcadlově k tomu, co uživatel vloží do Sheetu.
5. **Refresh celého souboru** (přečíst Sheet znovu a přegenerovat tabulky) provést, když je podezření, že lokální ledger je zastaralý (např. dlouho nepoužívaný projekt, nebo uživatel nahlásí rozpor) — ne při každém spuštění skillu, aby se zbytečně nešetřily tokeny.

**`/evisions-rewrite-article`** (viz `evisions_workflow_CZ.md` sekce 3b):

1. Při INIT dohledat zadanou URL v tabulkách "Existující obsah" níže.
2. Nalezeno → převzít ID/kategorii, nic se nezapisuje.
3. Nenalezeno → jde o Published článek, který ledger ještě nezná. Dohledat ID v Sheetu podle URL a doplnit chybějící řádek sem (Edit). Pokud ID neexistuje ani v Sheetu, pokračovat bez ID a upozornit uživatele v Init Summary.

---

## Next ID per kategorie (další volné číslo)

| Kategorie | Prefix | Poslední použité | **Další volné ID** |
|-----------|--------|-------------------|----------------------|
| SEO | SEO-XX | SEO-32 | **SEO-33** |
| PPC | PPC-XX | PPC-15 | **PPC-16** |
| Social | SOC-XX | SOC-10 | **SOC-11** |
| AI & SEO | AI-XX | AI-09 | **AI-10** |
| Copywriting | CW-XX | CW-05 | **CW-06** |
| Konference | CONF-XX | CONF-04 | **CONF-05** |
| Marketing | MKT-XX | MKT-05 | **MKT-06** |
| evisions interní | EVI-XX | EVI-05 | **EVI-06** |
| International | INTL-XX | INTL-05 | **INTL-06** |
| Kariéra (rozhovory se zaměstnanci) | PC-XX | PC-02 | **PC-03** |
| Kariéra (stáž/nábor) | CAR-XX | CAR-01 | **CAR-02** |

> Číslování v aktuálním Sheetu je bezmezerové (SEO-01 až SEO-29 bez děr atd.) — další ID je vždy poslední použité číslo + 1. Pokud po refreshi zjistíš díru v sekvenci, přiřaď první volné chybějící číslo, ne konec řady.

---

## Existující obsah (Published) — pro kontrolu shody podle ID/URL/tématu

### SEO

| ID | Kapitola/Nadpis | Skupina | Status | URL |
|----|-------------------|---------|--------|-----|
| SEO-01 | breAd. [case study]: Jak ovládnout niche B2B na německém trhu pomocí SEO | 1 – Case studies | Published | https://www.evisions.cz/blog/bre-ad-case-study-jak-ovladnout-niche-b2-b-na-nemeckem-trhu-pomoci-seo/ |
| SEO-02 | Z nuly na SEO hvězdu: Pomohli jsme Kalkulátor.cz vyrůst o 700 % | 1 – Case studies | Published | https://www.evisions.cz/blog/z-nuly-na-seo-hvezdu-pomohli-jsme-kalkulator-cz-vyrust-o-700-diky-chytre-obsahove-strategii/ |
| SEO-12 | MONETA Money Bank: Jak jsme pomohli vybudovat SEO jedničku bankovního sektoru | 1 – Case studies | Published | https://www.evisions.cz/blog/moneta-money-bank-jak-jsme-pomohli-vybudovat-seo-jednicku-bankovniho-sektoru/ |
| SEO-13 | Šperky Rýdl: Jak jsme vyšperkovali blog a přivedli na něj 261 tisíc lidí | 1 – Case studies | Published | https://www.evisions.cz/blog/sperky-rydl-jak-jsme-vysperkovali-blog-a-privedli-na-nej-261-tisic-lidi/ |
| SEO-16 | Naordinovali jsme klinice SEO proceduru... Přeplněné KPI o 768 % | 1 – Case studies | Published | https://www.evisions.cz/blog/naordinovali-jsme-klinice-seo-proceduru-a-jaky-je-vysledek-preplnene-kpi-o-768/ |
| SEO-22 | Jak jsme okořenili blog Dáme jídlo a přivedli na něj 126 000 čtenářů | 1 – Case studies | Published | https://www.evisions.cz/blog/jak-jsme-okorenili-blog-dame-jidlo-a-privedli-na-nej-126-000-ctenaru/ |
| SEO-23 | Jak jsme zvýšili organickou návštěvnost ePojisteni.cz o 300 % | 1 – Case studies | Published | https://www.evisions.cz/blog/jak-jsme-zvysili-organickou-navstevnost-e-pojisteni-cz-o-300/ |
| SEO-26 | VašeČočky.cz/321Linsen.de: Jak na zvýšení návštěvnosti blogu o 3 474 % | 1 – Case studies | Published | https://www.evisions.cz/blog/vase-cocky-cz-321-linsen-de-jak-na-zvyseni-navstevnosti-blogu-o-3-474/ |
| SEO-28 | Jak zvýšit organickou návštěvnost o 1000 % | 1 – Case studies | Published | https://www.evisions.cz/blog/jak-zvysit-organickou-navstevnost-o-1000/ |
| SEO-29 | Lišáckým SEO a content marketingem k úspěchu | 1 – Case studies | Published | https://www.evisions.cz/blog/lisackym-seo-a-content-marketingem-k-uspechu-z-nuly-na-tisice-kliknuti-denne/ |
| SEO-05 | Strategie kreativního linkbuildingu napříč evropským trhem | 2 – Linkbuilding | Published | https://www.evisions.cz/blog/strategie-kreativniho-linkbuildingu-napric-evropskym-trhem-co-funguje-nejlepe-v-ruznych-zemich/ |
| SEO-09 | Linkbuilding jako efektivní nástroj optimalizace webu | 2 – Linkbuilding | Published | https://www.evisions.cz/blog/linkbuilding-jako-efektivni-nastroj-optimalizace-webu/ |
| SEO-10 | Mezinárodní linkbuilding je efektivním pomocníkem při expanzi do zahraničí | 2 – Linkbuilding | Published | https://www.evisions.cz/blog/mezinarodni-linkbuilding-je-efektivnim-pomocnikem-pri-expanzi-do-zahranici/ |
| SEO-27 | 6 hlavních linkbuildingových metrik. Je domain rating opravdu nejdůležitější? | 2 – Linkbuilding | Published | https://www.evisions.cz/blog/6-hlavnich-linkbuildingovych-metrik-je-domain-rating-opravdu-nejdulezitejsi/ |
| SEO-07 | Universal Analytics končí, ať žije Google Analytics 4! | 3 – Analytika a metriky | Published | https://www.evisions.cz/blog/universal-analytics-konci-at-zije-google-analytics-4/ |
| SEO-19 | Share of Voice (SOV): K čemu je a jak metriku spočítat? | 3 – Analytika a metriky | Published | https://www.evisions.cz/blog/share-of-voice-sov-k-cemu-je-a-jak-metriku-spocitat/ |
| SEO-21 | Google Search Console: Jak ji v SEO využít naplno? | 3 – Analytika a metriky | Published | https://www.evisions.cz/blog/google-search-console-jak-ji-v-seo-vyuzit-naplno/ |
| SEO-30 | Marketingové KPI: jak je vybrat a měřit | 3 – Analytika a metriky | In Progress | — |
| SEO-31 | Webová analytika: co to je a jak ji využít pro marketing | 3 – Analytika a metriky | In Progress | — |
| SEO-32 | Co je SEO a jak funguje | 11 – content GAP | In Progress | — |
| SEO-03 | Mají rich snippets vždy pozitivní vliv na míru prokliku? | 4 – Rich/Featured snippets | Published | https://www.evisions.cz/blog/maji-rich-snippets-vzdy-pozitivni-vliv-na-miru-prokliku/ |
| SEO-15 | Jak jsme s ČSOB Pojišťovnou zvýšili návštěvnost blogu o 620 % díky featured snippets | 4 – Rich/Featured snippets | Published | https://www.evisions.cz/blog/jak-jsme-s-csob-pojistovnou-zvysili-navstevnost-blogu-o-620-diky-featured-snippets/ |
| SEO-04 | Úspěšná SEO migrace webu Foodora.cz | 5 – Migrace webu | Published | https://www.evisions.cz/blog/uspesna-seo-migrace-webu-foodora-cz-od-stareho-k-novemu/ |
| SEO-17 | Průvodce migrací webu z pohledu SEO | 5 – Migrace webu | Published | https://www.evisions.cz/blog/pruvodce-migraci-webu-z-pohledu-seo-aneb-nezahravejte-si-s-organickou-navstevnosti/ |
| SEO-08 | 10 tasků, do kterých se SEO specialistovi vyplatí zapojit ChatGPT | 6 – AI v SEO | Published | https://www.evisions.cz/blog/10-tasku-do-kterych-se-seo-specialistovi-vyplati-zapojit-chat-gpt/ |
| SEO-11 | SEO Restart 2023: Využití AI, nulové hledanosti i změny ve světě linkbuildingu | 6 – AI v SEO | Published | https://www.evisions.cz/blog/seo-restart-2023-vyuziti-ai-nulove-hledanosti-i-zmeny-ve-svete-linkbuildingu/ |
| SEO-14 | Průvodce regulárními výrazy pro začátečníky | 7 – SEO nástroje | Published | https://www.evisions.cz/blog/pruvodce-regularnimi-vyrazy-pro-zacatecniky/ |
| SEO-24 | SEO nástroje + 7 rozšíření, která vám usnadní práci | 7 – SEO nástroje | Published | https://www.evisions.cz/blog/seo-nastroje-7-rozsireni-ktera-vam-usnadni-praci/ |
| SEO-20 | Infografika: Podíl vyhledávačů Google a Seznam #2021 | 8 – Trh vyhledávačů ČR | Published | https://www.evisions.cz/blog/infografika-podil-vyhledavacu-google-a-seznam-na-ceskem-internetu-2021/ |
| SEO-25 | Infografika: Podíl vyhledávačů Google a Seznam #2020 | 8 – Trh vyhledávačů ČR | Published | https://www.evisions.cz/blog/infografika-podil-vyhledavacu-google-a-seznam-na-ceskem-internetu-2020/ |
| SEO-18 | Kam s čárkou aneb Vyznejte se v interpunkci | 9 – Copywriting/jazyk | Published | https://www.evisions.cz/blog/kam-s-carkou-aneb-vyznejte-se-v-interpunkci/ |
| SEO-06 | Synergie PPC a SEO: Klíč k digitálnímu úspěchu? | 10 – PPC & SEO synergie | Published | https://www.evisions.cz/blog/synergie-ppc-a-seo-klic-k-digitalnimu-uspechu/ |

### PPC

| ID | Kapitola/Nadpis | Skupina | Status | URL |
|----|-------------------|---------|--------|-----|
| PPC-02 | Meta AI stack | 1 – Meta/Facebook Ads | Published | https://www.evisions.cz/blog/meta-ai-stack-co-dnes-skutecne-hybe-vykonem-reklam-na-mete/ |
| PPC-03 | Samurajská kampaň | 1 – Meta/Facebook Ads | Published | https://www.evisions.cz/blog/samurajska-kampan-jak-si-netradicni-pristup-ziskal-prizen-uzivatelu-facebooku-a-you-tube-1/ |
| PPC-10 | Co jsme si odnesli z nejnabušenějšího školení na téma „Meta reklamy"? | 1 – Meta/Facebook Ads | Published | https://www.evisions.cz/blog/co-jsme-si-odnesli-z-nejnabusenejsiho-skoleni-na-tema-meta-reklamy/ |
| PPC-12 | Cíle reklamy na Facebooku: dosah, návštěvnost, nebo konverze? | 1 – Meta/Facebook Ads | Published | https://www.evisions.cz/blog/cile-reklamy-na-facebooku-dosah-navstevnost-nebo-konverze/ |
| PPC-01 | MASO-PROFIT [case study] | 2 – Case studies | Published | https://www.evisions.cz/blog/maso-profit-case-study-5-ingredienci-ktere-nam-pomohly-navysit-trzby-o-90/ |
| PPC-13 | Spolupráce evisions a Nefertitis | 2 – Case studies | Published | https://www.evisions.cz/blog/spoluprace-e-visions-a-nefertitis-za-9-mesicu-zvyseni-trzeb-na-temer-150-diky-ppc/ |
| PPC-07 | Proč byste si příští rok rozhodně neměli nechat ujít PPC camp? | 3 – Konference a vzdělávání | Published | https://www.evisions.cz/blog/proc-byste-si-pristi-rok-rozhodne-nemeli-nechat-ujit-ppc-camp/ |
| PPC-08 | PPC Restart 2024 | 3 – Konference a vzdělávání | Published | https://www.evisions.cz/blog/ppc-restart-2024-jak-na-uspesne-kampane-trendy-a-cookie-apokalypsu/ |
| PPC-04 | Jak spolu souvisí budování značky a výkonnostní marketing? | 4 – Branding a výkonnostní strategie | Published | https://www.evisions.cz/blog/jak-spolu-souvisi-budovani-znacky-a-vykonnostni-marketing/ |
| PPC-05 | Marketplaces, srovnávače, nákupní galerie | 5 – E-commerce kanály | Published | https://www.evisions.cz/blog/marketplaces-srovnavace-nakupni-galerie-vite-kde-a-jak-podnikat-online-s-nami-se-zorientujete/ |
| PPC-06 | Kariéra v PPC: Od Juniora k Seniorovi | 6 – Kariéra v PPC | Published | https://www.evisions.cz/blog/kariera-v-ppc-od-juniora-k-seniorovi/ |
| PPC-09 | Co je Google Consent Mode V2 a musíte to řešit? | 7 – Analytika a compliance | Published | https://www.evisions.cz/blog/co-je-google-consent-mode-v2-a-musite-to-resit/ |
| PPC-11 | Microsoft Ads – proč nezapomínat na Bing? | 8 – Microsoft Ads/Bing | Published | https://www.evisions.cz/blog/microsoft-ads-proc-nezapominat-na-bing/ |
| PPC-14 | Koeficient sezónnosti | 9 – Sezónnost a plánování | Published | https://www.evisions.cz/blog/koeficient-sezonnosti-jak-se-bude-vas-obrat-vyvijet-v-jednotlivych-mesicich/ |

### Social (SOC)

| ID | Kapitola/Nadpis | Skupina | Status | URL |
|----|-------------------|---------|--------|-----|
| SOC-01 | Jak TikTok mění pravidla hry v digitálním marketingu? | 1 – TikTok | Published | https://www.evisions.cz/blog/jak-tik-tok-meni-pravidla-hry-v-digitalnim-marketingu/ |
| SOC-02 | Jak získat na TikToku followery... | 1 – TikTok | Published | https://www.evisions.cz/blog/jak-ziskat-na-tik-toku-followery-a-vse-co-o-tomto-fenomenu-potrebujete-znat/ |
| SOC-03 | Jak rychle a efektivně rozjet účet na Instagramu od nuly | 2 – Instagram | Published | https://www.evisions.cz/blog/jak-rychle-a-efektivne-rozjet-ucet-na-instagramu-od-nuly/ |
| SOC-08 | 28 tipů, jak získat followers na Instagramu | 2 – Instagram | Published | https://www.evisions.cz/blog/28-tipu-jak-ziskat-followers-na-instagramu-welcome-instagram-seo/ |
| SOC-07 | Jak jsme z minerálních hnojiv udělali hot FB topic | 3 – Facebook (case studies) | Published | https://www.evisions.cz/blog/jak-jsme-z-mineralnich-hnojiv-udelali-hot-fb-topic-a-zvysili-organicky-dosah-yo-y-o-269/ |
| SOC-09 | Jak jsme to na Facebooku rozjeli s klientem MAN Truck & Bus | 3 – Facebook (case studies) | Published | https://www.evisions.cz/blog/jak-jsme-to-na-facebooku-rozjeli-s-klientem-man-truck-and-bus-czech-republic/ |
| SOC-04 | Buffer, Later, ZoomSphere a další | 4 – Nástroje a reporting | Published | https://www.evisions.cz/blog/buffer-later-zoom-sphere-a-dalsi-nejlepsi-aplikace-pro-planovani-prispevku/ |
| SOC-06 | Krok za krokem: Co by měl obsahovat každý social report? | 4 – Nástroje a reporting | Published | https://www.evisions.cz/blog/krok-za-krokem-co-by-mel-obsahovat-kazdy-social-report/ |
| SOC-05 | Jak oslovit více než 5 000 000 zákazníků přes social | 5 – Obecné social media | Published | https://www.evisions.cz/blog/jak-oslovit-vice-nez-5-000-000-zakazniku-pres-social-a-byt-hvezdou-blesku/ |
| SOC-10 | Jak předejít Shadowbanu? | 5 – Obecné social media | Published | https://www.evisions.cz/blog/jak-predejit-shadowbanu/ |

### AI & SEO

| ID | Kapitola/Nadpis | Skupina | Status | URL |
|----|-------------------|---------|--------|-----|
| AI-01 | Query fan-out v praxi | 1 – AI a vyhledávání (GEO/AI search) | Published | https://www.evisions.cz/blog/query-fan-out-v-praxi-jak-na-zaklade-dat-optimalizovat-obsah-pro-ai/ |
| AI-02 | Jak funguje AI Mode od Googlu | 1 – AI a vyhledávání (GEO/AI search) | Published | https://www.evisions.cz/blog/jak-funguje-ai-mode-od-googlu-novy-zpusob-vyhledavani-strucne-a-jednoduse/ |
| AI-03 | MONETA Money Bank case study (SEO+GEO) | 1 – AI a vyhledávání (GEO/AI search) | Published | https://www.evisions.cz/blog/moneta-money-bank-seo-ai-case-study-preciznim-seo-a-geo-k-nejlepsimu-zobrazovani-v-ai-vyhledavani-ve-financnim-sektoru/ |
| AI-04 | Promptování jako dovednost | 2 – AI a copywriting | Published | https://www.evisions.cz/blog/promptovani-jako-dovednost-proc-profik-dostane-z-ai-vic-nez-laik/ |
| AI-05 | Temná stránka AI | 2 – AI a copywriting | Published | https://www.evisions.cz/blog/temna-stranka-ai-evoluce-nebo-exploze/ |
| AI-06 | AI v rukách copywritera | 2 – AI a copywriting | Published | https://www.evisions.cz/blog/ai-v-rukach-copywritera-partak-nebo-halucinujici-vypravec/ |
| AI-07 | AI pro copywritery | 2 – AI a copywriting | Published | https://www.evisions.cz/blog/ai-pro-copywritery-umelou-genialitu-zatim-ocekavat-netreba/ |
| AI-09 | PPC Restart 2023: AI, PMax, GA4 a jiné anomálie | 3 – AI na konferencích | Published | https://www.evisions.cz/blog/ppc-restart-2023-ai-p-max-ga-4-a-jine-anomalie/ |
| AI-08 | Filtrace od A do Z: Svatý grál SEO e-shopů | 4 – (mimo AI, možná chybná kategorie) | Published | https://www.evisions.cz/blog/filtrace-od-a-do-z-svaty-gral-seo-e-shopu/ |

### Copywriting (CW)

| ID | Kapitola/Nadpis | Skupina | Status | URL |
|----|-------------------|---------|--------|-----|
| CW-02 | Stylistika textů, II. díl | 1 – Psaní a stylistika textů | Published | https://www.evisions.cz/blog/stylistika-textu-ii-dil-jak-napsat-esej-reportaz-nebo-fejeton/ |
| CW-05 | Pište bez chyb | 1 – Psaní a stylistika textů | Published | https://www.evisions.cz/blog/piste-bez-chyb-nasli-jsme-pro-vas-vychytavky-ktere-si-budete-chtit-vytisknout/ |
| CW-03 | Jak začít s copywritingem | 2 – Základy copywritingu | Published | https://www.evisions.cz/blog/jak-zacit-s-copywritingem-a-proc-jednicky-ze-slohu-nestaci/ |
| CW-04 | Vše o normostraně | 2 – Základy copywritingu | Published | https://www.evisions.cz/blog/vse-o-normostrane-kolik-ma-znaku-a-proc-je-tak-dulezita/ |
| CW-01 | Jak na e-commerce expanzi do střední a východní Evropy v roce 2024? | 3 – (mimo copywriting, možná chybná kategorie) | Published | https://www.evisions.cz/blog/jak-na-e-commerce-expanzi-do-stredni-a-vychodni-evropy-v-roce-2024/ |

> **Orphan URL bez ID/titulku v Sheetu (Copywriting tabulka):** `https://www.evisions.cz/blog/jak-jsme-diky-seo-a-copywritingu-zvysili-navstevnost-webu-cez-o-130/` — řádek v Sheetu má vyplněnou jen URL, žádné ID ani Kapitolu/Nadpis. Pravděpodobně starší článek nikdy formálně nezaindexovaný. Ověřit s uživatelem, ne domýšlet.

### Konference (CONF)

| ID | Kapitola/Nadpis | Skupina | Status | URL |
|----|-------------------|---------|--------|-----|
| CONF-02 | SERP Conf. Vídeň 2024 | 1 – Reporty z konkrétních konferencí | Published | https://www.evisions.cz/blog/serp-conf-viden-2024-klicove-poznatky/ |
| CONF-04 | Konference SEO Vibes v Budapešti | 1 – Reporty z konkrétních konferencí | Published | https://www.evisions.cz/blog/konference-seo-vibes-v-budapesti-mela-opravdu-vibe-pripadove-studie-nastroje-ai-on-page-a-linkbuilding/ |
| CONF-03 | Váš průvodce marketingovými a SEO konferencemi ve střední a východní Evropě a DACH pro rok 2024 | 2 – Přehled konferencí | Published | https://www.evisions.cz/blog/vas-pruvodce-marketingovymi-a-seo-konferencemi-ve-stredni-a-vychodni-evrope-a-dach-pro-rok-2024/ |
| CONF-01 | Zvýšení neplacené návštěvnosti o 888 % ... AutoPalace | 3 – (mimo konference, možná chybná kategorie) | Published | https://www.evisions.cz/blog/zvyseni-neplacene-navstevnosti-o-888-v-hodnote-statisicu-korun-mesicne-tajemstvi-seo-uspechu-auto-palace/ |

### Marketing (MKT)

| ID | Kapitola/Nadpis | Skupina | Status | URL |
|----|-------------------|---------|--------|-----|
| MKT-01 | Mailing ve stínu AI buzzwordů | 1 – Marketingové kanály | Published | https://www.evisions.cz/blog/mailing-ve-stinu-ai-buzzwordu-jak-vyuzit-nejefektivnejsi-prodejni-kanal-na-maximum/ |
| MKT-02 | Offline marketing v éře digitalizace | 1 – Marketingové kanály | Published | https://www.evisions.cz/blog/offline-marketing-v-ere-digitalizace-je-cas-prepnout-na-online/ |
| MKT-05 | SMS marketing, geofencing a beaconing | 1 – Marketingové kanály | Published | https://www.evisions.cz/blog/sms-marketing-geofencing-a-beaconing-jak-to-funguje/ |
| MKT-03 | Nejčastější chyby marketérů – klam přeživších | 2 – Strategie a cílení | Published | https://www.evisions.cz/blog/nejcastejsi-chyby-marketeru-klam-prezivsich/ |
| MKT-04 | Cílová skupina a persony | 2 – Strategie a cílení | Published | https://www.evisions.cz/blog/cilova-skupina-a-persony-aneb-znate-sveho-zakaznika/ |

### evisions interní (EVI)

| ID | Kapitola/Nadpis | Skupina | Status | URL |
|----|-------------------|---------|--------|-----|
| EVI-01 | Šipka, která míří na cíl: Nový vizuál | 1 – Firemní novinky a identita | Published | https://www.evisions.cz/blog/sipka-ktera-miri-na-cil-novy-vizual-ktery-posouva-hranice/ |
| EVI-03 | Synergie evisions a FTMO | 1 – Firemní novinky a identita | Published | https://www.evisions.cz/blog/synergie-e-visions-a-ftmo-vstup-noveho-investora-do-online-sveta-marketingove-agentury/ |
| EVI-02 | Jak skloubit studium vysoké školy s prací? | 2 – Kariéra a produktivita v evisions | Published | https://www.evisions.cz/blog/jak-skloubit-studium-vysoke-skoly-s-praci/ |
| EVI-05 | Tahák: 12 klávesových zkratek | 2 – Kariéra a produktivita v evisions | Published | https://www.evisions.cz/blog/tahak-12-klavesovych-zkratek-ktere-vam-usnadni-zivot-nejen-v-praci/ |
| EVI-04 | Jak vybrat nejlepší SEO agenturu? | 3 – Jak vybrat SEO agenturu | Published | https://www.evisions.cz/blog/jak-vybrat-nejlepsi-seo-agenturu/ |

### International (INTL)

| ID | Kapitola/Nadpis | Skupina | Status | URL |
|----|-------------------|---------|--------|-----|
| INTL-02 | Online expanze do Německa | 1 – Expanze do konkrétních zemí | Published | https://www.evisions.cz/blog/online-expanze-do-nemecka-jak-na-uspesnou-lokalizaci-webovych-stranek/ |
| INTL-04 | Maďarská E-commerce | 1 – Expanze do konkrétních zemí | Published | https://www.evisions.cz/blog/madarska-e-commerce-zlaty-dul-pro-vase-podnikani/ |
| INTL-05 | Expanze do Polska - vyplatí se? | 1 – Expanze do konkrétních zemí | Published | https://www.evisions.cz/blog/expanze-do-polska-vyplati-se/ |
| INTL-01 | SEO Vibes Summit 2025 | 2 – Mezinárodní konference | Published | https://www.evisions.cz/blog/seo-vibes-summit-2025/ |
| INTL-03 | Nejdůležitější informace: Konference BrightonSEO září 2023 | 2 – Mezinárodní konference | Published | https://www.evisions.cz/blog/nejdulezitejsi-informace-konference-brighton-seo-zari-2023/ |

### Kariéra — rozhovory se zaměstnanci (PC)

| ID | Kapitola/Nadpis | Skupina | Status | URL |
|----|-------------------|---------|--------|-----|
| PC-01 | Z juniora na Head of PPC za 3 roky | 1 – Rozhovory se zaměstnanci o kariérním růstu | Published | https://www.evisions.cz/blog/z-juniora-na-head-of-ppc-za-3-roky-martina-o-vedeni-tymu-vykonu-a-rustu/ |
| PC-02 | Jak vzniká dobrý uživatelský zážitek? (Nika Novosadová) | 1 – Rozhovory se zaměstnanci o kariérním růstu | Published | https://www.evisions.cz/blog/jak-vznika-dobry-uzivatelsky-zazitek-nika-novosadova-o-sve-ceste-od-social-media-k-ux-leadershipu/ |

### Kariéra — stáž/nábor (CAR)

| ID | Kapitola/Nadpis | Skupina | Status | URL |
|----|-------------------|---------|--------|-----|
| CAR-01 | Chcete začít s digitálním marketingem? Pomůže vám stáž | 1 – Stáž a začátky v oboru | Published | https://www.evisions.cz/blog/chcete-zacit-s-digitalnim-marketingem-pomuze-vam-staz/ |

---

## TODO / plánovaná témata (bez ID zatím) — kontrolovat shodu PŘED přiřazením nového ID

### SEO — Skupina 2 (Linkbuilding)
- Jak zjistit zpětné odkazy: Kompletní průvodce 2026
- Jak získat zpětné odkazy: Strategie, které fungují v ČR
- Dofollow, nofollow a anchor text: Jak fungují typy zpětných odkazů

### SEO — Skupina 3 (Analytika a metriky, tag `topic_cluster_analytika-a-metriky_CZ`)
- Co je Google Tag Manager a jak ho nastavit

### SEO — Skupina 4 (Rich/Featured snippets, tag `topic_cluster_rich-featured-snippets_CZ`)
- Strukturovaná data: co to je a jak fungují

### SEO — Skupina 5 (Migrace webu, tag `topic_cluster_migrace-webu_CZ`)
- Redesign webu a SEO: jak při změně vzhledu nepřijít o pozice (Typ: Článek)

### SEO — Skupina 6 (AI v SEO, tag `topic_cluster_ai-v-seo_CZ`)
- Co je Google AI Overview a jak ovlivňuje SEO v Česku (Typ: Článek) — ⚠️ **řádek už má URL vyplněnou:** `https://www.evisions.cz/blog/geo-optimalizace-pro-ai-vyhledavace-nova-era-seo-je-tady/`, ale bez ID a bez Status=Published. Pravděpodobně článek už existuje živý pod jiným titulkem ("GEO optimalizace pro AI vyhledávače: nová éra SEO je tady") a řádek jen čeká na formální přiřazení ID/Status v Sheetu. **Než na toto téma cokoliv píšeš, over si tu URL** — nejspíš už je hotovo, jen chybí zápis v Sheetu.

### SEO — Skupina 7 (SEO nástroje)
*(žádné TODO řádky)*

### SEO — Skupina 11 (content GAP)
- Keyword research – jak najít klíčová slova pro SEO
- On-page SEO – optimalizace obsahu a meta tagů
- Technické SEO – audit a základy
- Core Web Vitals a rychlost webu
- Lokální SEO a Google Business Profil (Typ: "bude v rámci sepisování konzultantami")
- Co je E-E-A-T a jak ho naplnit (Typ: "bude v rámci sepisování konzultantami")
- Interní prolinkování – strategie a best practices
- Kanibalizace klíčových slov – jak jí předejít a řešit
- Google Core Update – jak reagovat na algoritmické změny

### PPC — Skupina 1 (Meta/Facebook Ads)
- Co je Facebook/Meta Pixel a jak ho nastavit (Typ: Článek)
- Reklama na Instagramu: kompletní návod (Typ: Článek)

### PPC — Skupina 10 (PPC audit, nová skupina — lead-opportunity podpora pro /ppc-audit/)
- **PPC-15** — Co je PPC audit a kdy ho dává smysl objednat (Typ: Článek; přiřazeno 2026-08-27, In Progress) — podpůrný informační článek k landing page https://www.evisions.cz/ppc-audit/, klíčová slova: ppc audit, audit ppc, ppc audit zdarma, ppc audity, audit ppc účtu, ppc audit report

*(PPC, Social, AI & SEO, Copywriting, Konference, Marketing, evisions interní, International, Kariéra: žádné další TODO řádky nalezeny v posledním syncu — všechny řádky v těchto kategoriích mají ID a Status Published.)*

---

## Lokální složky výstupů (`data/output/articles/`)

| Slug | Odpovídá TODO tématu | Stav | Poznámka |
|------|----------------------|------|----------|
| `webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing` | SEO-31 — "Webová analytika: co to je a jak ji využít pro marketing" | Draft hotový přes Krok 6 (HTML), Krok 7 chybí | Vytvořeno 2026-08-17 (mimo tuto session). ID SEO-31 přiřazeno 2026-08-24. Než znovu spouštět `/evisions-new-article` na toto téma, dokončit Krok 7 na existujícím draftu. |
| `co-je-ppc-audit-a-kdy-ho-dava-smysl-objednat` | PPC-15 — "Co je PPC audit a kdy ho dává smysl objednat" | Draft hotový přes Krok 6 (HTML + docx), Krok 7 (publikace + update Status/URL v Sheetu) chybí | Vytvořeno 2026-08-27. Podpůrný článek k lead-opportunity revizi landing page `/ppc-audit/` — doporučení viz `data/output/lead-opportunities/ppc_audit_landing_page_recommendations_CZ.md`. |

---

## Datové anomálie zjištěné při syncu (k ověření s uživatelem, neopravovat samovolně)

1. **AI-08** ("Filtrace od A do Z: Svatý grál SEO e-shopů") — Sheet sám má poznámku "obsahově nesouvisí s AI, možné chybné zařazení kategorie na webu".
2. **CW-01** ("Jak na e-commerce expanzi...") — stejná poznámka, nesouvisí s copywritingem.
3. **CONF-01** ("Zvýšení neplacené návštěvnosti o 888 %... AutoPalace") — nesouvisí s konferencemi.
4. Několik SEO řádků (SEO-13, 22, 26, 28, 04) má poznámku "ZKONTROLOVAT téma" — obsah/kategorie k ověření uživatelem, ne indikace duplicity.
5. Tabulka "Kariéra — rozhovory se zaměstnanci" (PC-XX) má v syrových datech Sheetu poškozený hlavičkový řádek (text "Co je Google Search Console a jak ji využít v SEO" na místě sloupce "Kapitola/Nadpis") — vypadá jako artefakt kopírování v samotném Sheetu, ne skutečná data. Nebráno jako TODO řádek; ověřit se s uživatelem, pokud se to zdá relevantní.

---

## Document History

| Verze | Datum | Změny |
|-------|-------|-------|
| 1.0 | 2026-08-18 | První verze — plný sync se Sheetem `1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY`, 11 kategorií, ~85 Published řádků, ~20 TODO řádků zaindexováno |
| 1.1 | 2026-08-18 | Doplněn sloupec URL ke všem Published řádkům (kromě 1 orphan URL bez ID v Copywriting) |
| 1.2 | 2026-08-18 | Primárním zdrojem je nově Content Plan Index Sheet (`1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q`, uživatelova editovatelná kopie tohoto ledgeru). Původní Sheet degradován na sekundární. Doplněn nalezený existující draft `webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing` (chybně veden jako čistě plánovaný bez lokální složky) |
