# Edit Log: SEO nástroje + 7 rozšíření, která vám usnadní práci

**URL:** https://www.evisions.cz/blog/seo-nastroje-7-rozsireni-ktera-vam-usnadni-praci/
**Content Plan ID:** SEO-24
**Kategorie:** SEO — Skupina "7 – SEO nástroje"
**Autor (původní):** Marek Foršt (Head of SEO)
**Datum publikace (původní):** 2020-10-28

---

## Step 1 Log: Keywords

**Keywords file:** `seo-nastroje-7-rozsireni-ktera-vam-usnadni-praci_keywords.xlsx`

| # | Original | Changed To | Keyword | Volume | Position | Status |
|---|----------|------------|---------|--------|----------|--------|
| 1 | "Žádný SEO konzultant se neobejde bez potřebných nástrojů, které mu umožňují dělat svou práci." | "Žádný SEO konzultant se neobejde bez potřebných SEO nástrojů, které mu umožňují dělat svou práci." | seo nástroje | 800 | Úvod, 1. věta | DONE |
| 2 | "a v textu si navíc kromě nejdůležitějších SEO nástrojů popíšeme i" | "a v textu si navíc kromě nejdůležitějších online SEO nástrojů popíšeme i" | seo nástroje online | 150 | Úvod | DONE |
| 3 | "## Základní nástroje, ve kterých se musíte orientovat 24/7" | "## Základní nástroje SEO, ve kterých se musíte orientovat 24/7" | nástroje seo | 200 | H2 | DONE |
| 4 | "Jsou to nástroje, ke kterým máte přístup zdarma a podávají vám základní a zároveň nejdůležitější informace." | "Jsou to SEO nástroje zdarma, ke kterým máte přístup a podávají vám základní a zároveň nejdůležitější informace." | seo nástroje zdarma | 800 | Tělo, sekce "Základní nástroje SEO" | DONE |
| 5 | "### **Neplacené nástroje**" | "### **SEO nástroje zdarma**" | seo nástroje zdarma | 800 | H3 | DONE |
| 6 | "Bohatě byste si ale měli vystačit s nástroji a rozšířeními uvedenými v článku." | "Bohatě byste si ale měli vystačit se SEO nástroji a rozšířeními uvedenými v článku." | seo nástroje | 800 | Závěr | DONE |

**Přeskočeno (SKIP) — bez zásahu do textu:**

| Keyword | Volume | Poznámka |
|---|---|---|
| seo nástroje free | 100 | Sémanticky pokryto novým H3 "SEO nástroje zdarma" (#5), doslovné "free" by bylo redundantní vedle "zdarma" ve stejné sekci |
| nástroje na seo | 100 | Pokryto morfologickými variantami "SEO nástroje/nástrojů" napříč textem, doslovná fráze nemá přirozené místo |
| seo optimalizace nástroje | 100 | Nepřirozený slovosled v češtině, vynucení by znělo kostrbatě; pokryto obecně tématem článku |
| seo nástroje analýza www | 80 | Sémanticky pokryto sekcí "Crawler a nástroje na technický audit" (Screaming Frog, PageSpeed Insight), doslovné "www" by v plynulém textu neznělo přirozeně |
| nejlepší seo nástroje | 20 | Záměna "základních" → "nejlepších" v H2 "Souhrn základních SEO nástrojů" by měnila význam (autor je označuje za "základní", ne "nejlepší") → porušení pravidla 2 |
| nástroje seo analýzy | 10 | Nízký objem, pokryto sekcí "Jakými nástroji se vyzbrojit na analýzu klíčových slov?" |
| nástroje seo analýzy zdarma | 10 | Nízký objem, pokryto stejnou sekcí + novým "SEO nástroje zdarma" |
| internetové seo nástroje | 10 | Nízký objem, pokryto "online SEO nástrojů" (#2) |
| nástroje pro audit seo | 10 | Nízký objem, pokryto sekcí "Crawler a nástroje na technický audit" |
| doporučení nástroje pro seo audit | 10 | Nízký objem, pokryto stejnou sekcí (Tip callouty u Screaming Frog/PageSpeed Insight) |
| nejlepší ai seo nástroje | 10 | Článek z r. 2020 AI SEO nástroje nepokrývá — vynucení by přidalo nové informace (zakázáno). Doporučuji jako námět na samostatný nový článek přes `/evisions-new-article` |

---

## Step 2 Log: ToV Rewrite

**Guide:** `evisions_tov_guide_CZ.md`
**Typ obsahu:** How-to / trend analýza

| # | Původní věta (celá) | Nová věta (celá) | Důvod |
|---|----------------------|-------------------|--------|
| 1 | "Google Search Console se podobně jako ostatní nástroje vyvíjí a v nedávné době se objevila nová funkce – takzvané *Core Web Vitals*, neboli nejdůležitější životní funkce, které souvisí s rychlostí webu (a celkově UX). Důležité je, že Google [explicitně zmínil](https://webmasters.googleblog.com/2020/05/evaluating-page-experience.html), že *Core Web Vitals* budou ze strany Googlu v budoucnu hodnoticím faktorem." | "Google Search Console se podobně jako ostatní nástroje vyvíjí a v nedávné době se objevila nová funkce: takzvané *Core Web Vitals*, neboli nejdůležitější životní funkce, které souvisí s rychlostí webu (a celkově UX). Google [explicitně zmínil](https://webmasters.googleblog.com/2020/05/evaluating-page-experience.html), že *Core Web Vitals* budou ze strany Googlu v budoucnu hodnoticím faktorem." | ToV: en dash zakázán → dvojtečka; smazána vycpávková fráze "Důležité je, že X" |
| 2 | "Pokud chcete z Google Search Console vytáhnout maximum, existuje API, pomocí kterého můžete z nástroje stáhnout více dat, než je v klasickém rozhraní (limit 1 000 dotazů)." | "Pokud chcete z Google Search Console vytáhnout maximum, využijte API: pomocí něj stáhnete z nástroje více dat, než je v klasickém rozhraní (limit 1 000 dotazů)." | ToV: existenciální "existuje X" → přímá výzva (aktivní rod, "Rovnou k věci") |
| 3 | "**Tip**: Jednou z takových příležitostí a takzvaných quick-wins je optimalizace snippetů stránek, které už dosahují dobrých pozic, ale nevyužívají svého potenciálu." | "**Tip**: Typickým quick-winem je optimalizace snippetů stránek, které už dosahují dobrých pozic, ale nevyužívají svého potenciálu." | ToV: "Jednou z... je" vycpávka → pojmenování věci přímo |
| 4 | "Je to však zároveň nástroj velmi komplexní a troufám si říct, že spousta specialistů nezná zdaleka všechny jeho funkce a používá sotva polovinu." | "Je to však zároveň nástroj velmi komplexní a spousta specialistů nezná zdaleka všechny jeho funkce a používá sotva polovinu." | ToV: 1. osoba jednotného čísla ("troufám si říct") → přímé tvrzení bez hedgingu |
| 5 | "[Marketing Miner](https://www.marketingminer.com/cs) od Filipa Podstavce patří osobně mezi mé oblíbené nástroje, a navíc se stále rozšiřuje." | "[Marketing Miner](https://www.marketingminer.com/cs) od Filipa Podstavce patří mezi naše oblíbené nástroje, a navíc se stále rozšiřuje." | ToV: 1. osoba jednotného čísla ("mé") → inkluzivní hlas značky ("naše") |
| 6 | "Ahrefs před pár týdny představil nový nástroj – svůj vlastní [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools)." | "Ahrefs před pár týdny představil nový nástroj: svůj vlastní [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools)." | ToV: en dash zakázán → dvojtečka |
| 7 | "Pak je pro vás nezbytnou nutností rozšíření [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen), které si osobně velmi pochvaluji." | "Pak je pro vás nezbytnou nutností rozšíření [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen), které vřele doporučujeme." | ToV: 1. osoba jednotného čísla ("osobně pochvaluji") → inkluzivní hlas značky |

**Poznámka mimo rozsah ToV (k rozhodnutí uživatele, ne automaticky opraveno):** Věta "Ahrefs před pár týdny představil nový nástroj..." (Tip u sekce Ahrefs) je fakticky datovaná — v originále z roku 2020 odkazuje na tehdy nový Ahrefs Webmaster Tools jako novinku "před pár týdny". V roce 2026 to čtenáře může mást. Oprava vyžaduje přidání/odebrání informace (aktuální stav Ahrefs Webmaster Tools), což přesahuje mandát Kroku 2 (žádné nové/odebrané informace) — navrhuji řešit explicitně v Kroku 5 (QA) nebo se zeptat, zda tuto větu přeformulovat na časově neutrální ("Ahrefs kromě klasického nástroje nabízí i vlastní Ahrefs Webmaster Tools.").

---

## Step 3 Log: Structure & Formatting

**Délka článku:** DLOUHÝ (~2 170 slov)

**Fáze 0 — Audit odstavců:** Zkontrolovány všechny odstavce. Nejdelší má 77 slov (limit pro povinné rozdělení je 100 slov) → žádný odstavec nebylo nutné rozdělit.

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | Callout odstraněn (demoted na odstavec) | Tip u Google Analytics (automatizace upozornění) → prostý odstavec | Redukce z 9 na max. 4 callouty (limit pro DLOUHÝ článek); obsah beze změny, jen bez blockquote formátování |
| 2 | Callout odstraněn (demoted na odstavec) | Tip u Seznam Webmaster Tools (vizualizace v Data Studiu) → prostý odstavec | Stejný důvod jako #1 |
| 3 | Callout odstraněn (demoted na odstavec) | Tip u PageSpeed Insight (web.dev) → prostý odstavec | Stejný důvod jako #1 |
| 4 | Callout odstraněn (demoted na odstavec) | Tip u Ahrefs (Ahrefs Webmaster Tools) → prostý odstavec | Stejný důvod jako #1 |
| 5 | Callout odstraněn (demoted na odstavec) | Tip u Collabim (upozornění) → prostý odstavec | Stejný důvod jako #1 |
| 6 | Callout odstraněn (demoted na odstavec) | Tip u Google Data Studio (monitoring) → prostý odstavec | Stejný důvod jako #1 |
| 7 | Callout přidán | **Keep in Mind** u Screaming Frog: caveat o placených alternativách (SiteBulb, Spotibo) vyňat z běžícího odstavce a zvýrazněn jako samostatný callout | Structure Guide: "Keep in Mind – 1 na how-to článek" (limit méně, ne přiznání limitů); ponechány oba odkazy i informace, jen jiné formátování |
| 8 | Ponecháno jako Tip | Tip u Google Search Console (quick-win optimalizace snippetů) | 1 ze 4 finálních calloutů — nejsilnější akční rada v článku |
| 9 | Ponecháno jako Tip | Tip u Marketing Miner (Google Trends pro sezónnost) | 1 ze 4 finálních calloutů |
| 10 | Odstavec → číslovaný seznam | GA report vstupních stránek: postup filtrace (2 kroky) převeden na `1. 2. 3.` | Structure: postupné kroky → číslovaný seznam (ne odrážky) |
| 11 | Odstavec → číslovaný seznam | Scraper: postup použití (klik → výběr → výsledek) převeden na `1. 2. 3.` | Stejný důvod jako #10 |
| 12 | Tabulka přidána | "Vychytávky, které vám usnadní práci" — souhrnná tabulka 7 rozšíření a jejich účelu (před první H3) | Structure: srovnání položek napříč atributem (K čemu slouží); odvozeno z existujícího textu, žádná nová informace |
| 13 | Interní odkaz přidán | "míry prokliku (CTR)" v GSC Tip → [Mají rich snippets vždy pozitivní vliv na CTR?](/blog/maji-rich-snippets-vzdy-pozitivni-vliv-na-miru-prokliku/) (SEO-03) | Interní prolinkování: min. 3-5 odkazů, tematicky přesná shoda (snippet CTR) |
| 14 | Interní odkaz přidán | "technického SEO" v úvodu sekce Linkbuilding → [Průvodce migrací webu z pohledu SEO](/blog/pruvodce-migraci-webu-z-pohledu-seo-aneb-nezahravejte-si-s-organickou-navstevnosti/) (SEO-17) | Stejný důvod jako #13 |
| 15 | Interní odkaz přidán | "cesta přesměrování" v sekci Redirect Path → [Úspěšná SEO migrace webu Foodora.cz](/blog/uspesna-seo-migrace-webu-foodora-cz-od-stareho-k-novemu/) (SEO-04) | Stejný důvod jako #13; celkem 4 interní odkazy v článku (1 původní + 3 nové) |
| 16 | E-E-A-T blok přidán | Na konec článku doplněno: Autor (Marek Foršt), Role (Head of SEO), Aktualizováno (2026-09-01) | Structure Guide: povinná autorská atribuce na konci článku |
| 17 | ToC — bez zásahu | Obsah (>1500 slov vyžaduje ToC) se negeneruje ručně v markdownu — `src/step4_html.py` ho staví automaticky z H2/H3 v Kroku 4 | Vyhnutí se duplicitě; viz `step4_html.py` `_build_toc()` |

**Callouty celkem:** 4 (3× Tip, 1× Keep in Mind) — v limitu pro DLOUHÝ článek (3-4).
**Tabulky celkem:** 1 (nová souhrnná tabulka rozšíření); dvě odrážkové listy Neplacené/Placené nástroje v sekci Souhrn ponechány beze změny, jsou pro shrnutí vhodnějším formátem.
**Seznamy:** číslované 2 (nové), odrážkové 2 (původní, beze změny).
**Nadpisy:** 8× H2, 19× H3 — beze změny oproti originálu (jen H2/H3 texty upravené v Kroku 1).

---

## Step 4 Log: HTML konverze

**Vstup:** `article_seo-nastroje-7-rozsireni-ktera-vam-usnadni-praci_CZ.md` po Kroku 3
**Výstupy:** `article_seo-nastroje-7-rozsireni-ktera-vam-usnadni-praci_CZ.html`, `article_seo-nastroje-7-rozsireni-ktera-vam-usnadni-praci_CZ.docx`

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | H1 přidán | `# SEO nástroje + 7 rozšíření, která vám usnadní práci` na začátek markdownu | Structure Guide: H1 povinný, 1 na stránku; `step4_html.py` z něj extrahuje title a intro-text třídu — v markdownu chyběl |
| 2 | 13× `[OBRAZEK-N]` nahrazeno reálným `![alt](url)` | Doplněny popisné alt texty (originál měl `alt=""` u všech 13 obrázků, zaznamenáno v Init) | Accessibility + SEO; obrázky beze změny pozice dle Mapy obrázků z Init |
| 3 | Formát callout labelu opraven | `> **Tip**: ` → `> **Tip:** ` (a totéž pro Keep in Mind) na všech 4 callout blocích | `step4_html.py`/`export_article_docx.py` očekávají dvojtečku uvnitř tučného labelu (dle vzoru v Structure Guide); jen formát, obsah beze změny |
| 4 | Pořadí callout/obrázek prohozeno | Sekce Screaming Frog: Tip (Force-Directed Crawl) + obrázek nyní PŘED Keep in Mind (dřív byly 2 callouty hned za sebou) | Bug: 2 blockquoty oddělené jen prázdným řádkem markdown slévá do jednoho `<blockquote>` → `_process_callouts()` je pak zpracoval jako 1 callout místo 2. Structure Guide navíc zakazuje callouty za sebou. Obsah beze změny, jen pořadí |
| 5 | Soubor přejmenován | `step4_html.py` generuje `[slug]_CZ.html` bez prefixu `article_` → přejmenováno na `article_[slug]_CZ.html` | Konvence pojmenování dle CLAUDE.md |
| 6 | Oprava skriptu `src/export_article_docx.py` | Nadpisy (`### **Text**`) se do .docx vkládaly doslovně s `**` — přidána `_clean_heading_text()` (strip markdown bold/link syntax před `add_heading()`) | Bug ve skriptu (ne v obsahu článku) — postihoval by všechny budoucí články s tučnými/odkazovanými nadpisy, ne jen tento |
| 7 | Oprava skriptu `src/export_article_docx.py` | Řádky `---` (horizontal rule) se do .docx vkládaly jako doslovný text "---" — nyní se přeskakují | Stejný typ bugu jako #6, obecná oprava skriptu |

**Ověřeno v HTML výstupu:** 1× H1, title tag správně, 4 callout divy (3 tip + 1 keep-in-mind), 13 figure/obrázků (vše s alt textem), 1 tabulka, ToC automaticky vygenerováno z 8×H2/19×H3, žádný zbylý `[OBRAZEK-N]` token, žádné doslovné `**` v textu.
**Ověřeno v .docx výstupu:** 112 odstavců/nadpisů, nadpisy bez markdown syntaxe, žádné osamocené řádky "---".

**Poznámka (známé omezení šablony, nikoli chyba tohoto běhu):** Author box v HTML šabloně (`step4_html.py`) je hardcoded na generický "Content Team / evisions Advertising" a nepoužívá skutečné jméno autora (Marek Foršt), přestože markdown obsahuje E-E-A-T blok s reálným autorem na konci článku. Toto je známé omezení šablony (viz interní poznámka), oprava přesahuje mandát Kroku 4 (šablona ovlivňuje všechny články) — ponecháno k rozhodnutí uživatele, zda opravit šablonu samostatně.

---

## Step 5 Log: QA & revize

### Přesnost obsahu
- [x] Všechna fakta odpovídají zdroji — kontrolováno proti verbatim extrakci z Init (žádné číslo/tvrzení nezměněno)
- [x] Žádné informace nepřidány ani neodebrány — jediné výjimky jsou 2 opravy nefunkčních odkazů níže (odkaz odstraněn/přesměrován, text věty beze změny)
- [x] Obrázky na správných pozicích — 13/13 dle Mapy obrázků z Init, alt texty doplněny (originál měl `alt=""` u všech)
- [ ] → [x] Odkazy fungují — **2 nefunkční odkazy nalezeny a opraveny:**

| # | Odkaz | Problém | Oprava |
|---|-------|---------|--------|
| 1 | "explicitně zmínil" (Core Web Vitals, Google) | `webmasters.googleblog.com/2020/05/evaluating-page-experience.html` → HTTP 404 (Google přesunul blog) | Nahrazeno oficiální aktuální URL stejného obsahu: `developers.google.com/search/blog/2020/05/evaluating-page-experience` (ověřeno HTTP 200) |
| 2 | "článku SEO pro začátečníky" (interní odkaz, úvod) | `evisions.cz/blog-2020-08-05-pruvodce-seo-pro-zacatecniky/` — starý URL formát, live web ho tiše přesměrovává na `/blog/` (výpis článků), cílový článek už na webu neexistuje. Google ho stále indexuje na staré adrese, ale žádná nová `/blog/[slug]/` verze nebyla nalezena | Odkaz odstraněn (text "článku SEO pro začátečníky" ponechán jako obyčejný text, informace nezměněna) — **k rozhodnutí uživatele, viz shrnutí Kroku 5** |

Zbylých 60+ externích i interních odkazů v článku ověřeno (HTTP 200, včetně Chrome Web Store rozšíření a nástrojů typu Ahrefs/Screaming Frog/atd.). `spotibo.com/seo-analyzer` vrací 466 na holý `curl` bez browser User-Agentu — s běžným UA prohlížeče vrací 200, jde o bot-ochranu (WAF), ne o nefunkční odkaz.

### ToV compliance
- [x] Tón odpovídá ToV Guide (How-to / trend analýza) — viz Krok 2
- [x] Žádné zakázané fráze — opětovný sken celého finálního textu (em/en dash, "garantujeme", "revoluční", "naprosto", "tajný trik", "je důležité zmínit", "existuje několik důvodů", "jedna z nejdůležitějších", "určitě už víte", "to přece každý ví", "je to jednoduché, stačí") → 0 nálezů
- [x] Žádné garance konkrétních výsledků

### Structure compliance
- [x] E-E-A-T prvky přítomny — Autor (Marek Foršt), Role (Head of SEO), Aktualizováno (2026-09-01) na konci článku
- [x] Hierarchie nadpisů správná — H1×1 → H2×8 → H3×19, žádné přeskočení úrovně
- [x] Interní odkazy přítomny — 3 (po opravě #2 výše; původně plánováno 4, jeden nefunkční odkaz odstraněn beze náhrady)

### Technické
- [x] HTML se správně renderuje — ověřeno BeautifulSoup parsováním výstupu (title, H1, callouty, figury, tabulka, ToC)
- [x] Obrázky se načítají — 13/13 URL z originálu, žádný přepsaný/rozbitý odkaz
- [x] Žádné nefunkční odkazy — viz oprava #1 a #2 výše; zbytek ověřen

---

**Rozhodnutí uživatele (obě položky vyřešeny):**

1. **Ahrefs Webmaster Tools — časově datovaná věta → OPRAVENO.** Uživatel: "určitě tam nechci nic zastaralého." Přeformulováno na časově neutrální znění:
   - Original: "Ahrefs před pár týdny představil nový nástroj: svůj vlastní [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools). Nástroj jsme již otestovali a první dojmy jsou více než skvělé. Rozšiřuje působnost nástroje Ahrefs do dalších oblastí a je zároveň uživatelsky velmi příjemný."
   - New: "Ahrefs kromě klasického nástroje nabízí i vlastní [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools). Nástroj jsme otestovali a dojmy jsou více než skvělé. Rozšiřuje působnost nástroje Ahrefs do dalších oblastí a je zároveň uživatelsky velmi příjemný."
   - Odstraněna časová vazba ("před pár týdny", "již") — fakta (existence nástroje, otestováno, kladné dojmy, rozšíření působnosti, uživatelská přívětivost) beze změny.
2. **Chybějící interní odkaz "SEO pro začátečníky" → ponecháno bez odkazu.** Uživatel: "zatím bez odkazu." Žádný náhradní publikovaný článek k dispozici (SEO-32 je "In Progress"). Text zůstává jako obyčejná zmínka bez hypertextu; jakmile SEO-32 vyjde, lze odkaz doplnit dodatečně.

HTML a .docx přegenerovány po opravě #1.

---

## Step 1.5 Log: Konkurenční SERP kontrola (retroaktivně, po přidání Kroku 1.5 do skillu)

**Klíčová slova prověřena:** seo nástroje (800), seo nástroje zdarma (800), nástroje na seo (na dotaz uživatele dodatečně)
**Konkurenti (URL), 10 celkem:**
1. vceliste.cz/blog/velky-prehled-seo-nastroju-zdarma/ (~6 500–7 000 slov, 17 nástrojů)
2. strafelda.cz/seo-nastroje (~2 200–2 500 slov)
3. seoprakticky.cz/blog/nejoblibenejsi-seo-nastroje/ (~400–500 slov)
4. marketingminer.com/cs/blog/seo-nastroje-zdarma (~2 800–3 000 slov)
5. whitepress.com/cz/blog/2202/seo-nastroje (~4 500–5 000 slov)
6. klarawebdesign.cz/seo-nastroje-zdarma/ (~1 200–1 400 slov, FAQ sekce)
7. seoprakticky.cz/seo-nastroje/ (~6 500–7 000 slov, srovnávací tabulka)
8. webhostingcentrum.cz/seo-nastroje-kompletni-seznam/ (~5 200–5 500 slov, 32 nástrojů, FAQ)
9. nastrojeproweb.cz/clanky/nejlepsi-seo-nastroje (~4 500–5 000 slov, číslovaný žebříček 1–12)
10. 5nej.cz/srovnani-seo-nastroju/ (~6 500–7 000 slov, 22parametrová srovnávací tabulka)

**Mezery nalezeny:** 6 nástrojů s frekvencí výskytu 4+/10 konkurentů, které náš článek buď vůbec nepokrývá, nebo jen jednou větou bez popisu:

| # | Mezera | Frekvence u konkurence | Návrh |
|---|--------|--------------------------|-------|
| 1 | Semrush — u nás jen 1 věta bez popisu | 6/10 | Vlastní H3 vedle Ahrefs |
| 2 | Google Keyword Planner — chybí úplně | 4/10 | H3 v sekci Analýza klíčových slov |
| 3 | Moz / Moz Pro — chybí úplně | 4/10 | Vlastní H3 vedle Ahrefs |
| 4 | Seznam Sklik (keyword tool) — chybí, máme jen Webmaster Tools | 4/10 | Kombinovaná H3 s Google Keyword Planner |
| 5 | Mangools — chybí úplně | 4/10 | Vlastní H3 vedle Ahrefs |
| 6 | Majestic — chybí úplně | 4/10 | Vlastní H3 vedle Ahrefs |

Nižší prioritu měly SEO Macroscope (2/10), FAQ sekce (2/10), srovnávací tabulka nástrojů (3/10) — konzultováno s uživatelem, do rozsahu této revize nezahrnuty.

**Shrnutí:** Náš článek (2 170 slov) byl hloubkou srovnatelný jen se střední třídou konkurence. 4 z 10 konkurentů (5 000–7 000 slov, katalogy 17–32 nástrojů, srovnávací tabulky/hodnocení) jsou výrazně obsáhlejší — plná parita s nimi by znamenala fakticky nový, mnohem delší článek, ne revizi, a mimo scope tohoto kroku.

**Zvolený mód:** **A (konkurenceschopná revize)** — uživatel po diskuzi zvolil střední variantu: doplnit všech 6 nástrojů s frekvencí 4+/10 + krátkou srovnávací tabulku (bez FAQ, bez plné 32položkové parity).

---

## Step 3 Log (Fáze -1): Doplnění obsahových mezer — Mód A

| # | Typ | Vložený text (celý) | Umístění | Zdroj/zdůvodnění |
|---|-----|----------------------|----------|-------------------|
| 1 | NOVÝ OBSAH (Mód A) | "Pokud spravujete i PPC kampaně, máte hledanost k dispozici zdarma přímo z reklamních platforem. [Google Keyword Planner](https://ads.google.com/intl/cs_cz/home/tools/keyword-planner/) je součástí Google Ads a ukáže vám orientační objem vyhledávání i návrhy souvisejících klíčových slov. Obdobně funguje [Sklik](https://www.sklik.cz/) od Seznamu, jehož plánovač klíčových slov bývá pro český trh přesnější než globální nástroje." + odstavec o orientační přesnosti dat | Nová H3 "Google Keyword Planner a Sklik" v sekci "Jakými nástroji se vyzbrojit na analýzu klíčových slov?", před H3 "Excel a OpenRefine" | Mezery #2 a #4 z Kroku 1.5 — 4/10 konkurentů pokrývá Google Keyword Planner, 4/10 Sklik jako keyword nástroj |
| 2 | NOVÝ OBSAH (Mód A) | "[Semrush](https://www.semrush.com/) pokrývá podobné oblasti jako Ahrefs — analýzu klíčových slov, linkbuilding, technický audit i monitoring konkurence. Navíc nabízí silnější nástroje pro PPC a správu sociálních sítí, pokud spravujete kampaně napříč více kanály. Databázi pro český trh má o něco menší než Ahrefs, ale u mezinárodních projektů je to jeden z referenčních nástrojů." | Nová H3 "Semrush" v sekci "Linkbuilding, off-page faktory, konkurence…", hned po Ahrefsu | Mezera #1 z Kroku 1.5 — 6/10 konkurentů, nejsilnější signál |
| 3 | NOVÝ OBSAH (Mód A) | "[Mangools](https://mangools.com/) je balík nástrojů (KWFinder, SERPWatcher, SERPChecker, LinkMiner, SiteProfiler) cílený na menší rozpočty. KWFinder se hodí na hledání long-tail klíčových slov s nižší konkurencí, SERPWatcher pak na sledování pozic. Ve srovnání s Ahrefsem nebo Semrushem má menší databázi zpětných odkazů, zato je jednodušší na ovládání pro začátečníky." | Nová H3 "Mangools", po Semrush | Mezera #5 z Kroku 1.5 |
| 4 | NOVÝ OBSAH (Mód A) | "[Moz Pro](https://moz.com/products/pro) je jeden z nejstarších all-in-one SEO nástrojů na trhu. Kombinuje analýzu klíčových slov, audit webu a přehled zpětných odkazů, včetně vlastní metriky Domain Authority. Pro český trh má slabší pokrytí dat než Ahrefs nebo Semrush, ale u anglicky psaného obsahu je to solidní alternativa." | Nová H3 "Moz Pro", po Mangools | Mezera #3 z Kroku 1.5 |
| 5 | NOVÝ OBSAH (Mód A) | "[Majestic](https://majestic.com/) se specializuje výhradně na analýzu zpětných odkazů. Místo širokého záběru nabízí hlubší pohled na odkazový profil — metriky Trust Flow a Citation Flow vám pomůžou odhadnout důvěryhodnost domény nezávisle na Ahrefs/Semrush skórování. Hodí se jako doplňkový zdroj dat při due diligence před nákupem odkazů nebo doménou." | Nová H3 "Majestic", po Moz Pro | Mezera #6 z Kroku 1.5 |
| 6 | NOVÝ OBSAH (Mód A) | Srovnávací tabulka (Nástroj / Zaměření / Cenová hladina / Vhodné pro) pro Ahrefs, Semrush, Mangools, Moz Pro, Majestic | Konec sekce "Linkbuilding, off-page faktory, konkurence…", po Majestic, před `---` | Uživatelem schválená "krátká srovnávací tabulka" jako součást Varianty 2 |
| 7 | NOVÝ OBSAH (Mód A) | Doplněna položka "Google Keyword Planner a Sklik" do seznamu "SEO nástroje zdarma"; položky "Semrush", "Mangools", "Moz Pro", "Majestic" do seznamu "Placené nástroje" | Sekce "Souhrn základních SEO nástrojů" | Konzistence souhrnu s nově přidaným obsahem — bez úpravy zůstal souhrn neúplný vůči tělu článku |

**Poznámka k odst. 2 v sekci Souhrn (nezměněno, zachováno z originálu 2020):** věta "...ocení například Semrush nebo SimilarWeb" nyní mírně duplikuje nové H3 Semrush. Ponecháno beze změny — je to původní text z roku 2020, mimo mandát tohoto zásahu (mění se jen doplněním, ne odebíráním/úpravou originálu).

**Ověření odkazů (6 nových):** všech 6 URL (ads.google.com, sklik.cz, semrush.com, mangools.com, moz.com, majestic.com) ověřeno HTTP 200 před vložením.

**Dopad na délku:** 2 170 → 2 488 slov (+318). Callouty beze změny (4, žádné nové nepřidány, aby se nepřekročil limit pro DLOUHÝ článek). Tabulky 1 → 2 (stále v limitu 2-3). H3 19 → 24.

**Fáze 0 (Audit odstavců) po vložení:** žádný odstavec (včetně nově vloženého textu) nepřesahuje 100 slov — nejdelší nový odstavec má 69 slov.

HTML a .docx přegenerovány po vložení Fáze -1.

---
