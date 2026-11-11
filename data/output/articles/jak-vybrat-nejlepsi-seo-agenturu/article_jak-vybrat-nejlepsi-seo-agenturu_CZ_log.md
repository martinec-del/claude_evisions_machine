# Edit Log: Jak vybrat nejlepší SEO agenturu?

**Content Plan ID:** EVI-04
**Kategorie:** evisions interní — Skupina 3 (Jak vybrat SEO agenturu)
**Zdrojová URL:** https://www.evisions.cz/blog/jak-vybrat-nejlepsi-seo-agenturu/
**Cílová URL pro leady (brief):** https://www.evisions.cz/seo/
**Speciální brief:** konverzní retrofit (CTA v těle, nová sekce "Jak pracujeme my v Evisions?", upravený závěr s CTA) — viz zadání uživatele 2026-08-27. Toto je vědomá výjimka ze standardního principu "Zachovat obsah, vylepšit prezentaci" (workflow guide sekce 1): přidává se nový konverzní obsah, ne jen se vylepšuje prezentace stávajícího. Fakta a informace z původního článku se nemění, pouze se doplňují.

---

## Step 1 Log: Klíčová slova

**Keywords file:** `data/output/keywords/jak-vybrat-nejlepsi-seo-agenturu_keywords.xlsx`

| # | Original sentence (full) | New sentence (full) | Reason | Status |
|---|--------------------------|----------------------|--------|--------|
| 1 | "Rozpoznat dobrou agenturu od špatné je velmi složitý úkol. Všechny o sobě tvrdí, že jsou nejlepší, všechny mají nekonečnou řadu referencí" | "Rozpoznat dobrou agenturu od špatné je velmi složitý úkol. Všechny SEO agentury o sobě tvrdí, že jsou nejlepší, všechny mají nekonečnou řadu referencí" | KW: doplněn implicitní podmět "SEO agentury" (dřív jen "Všechny") — zpřesňuje odkaz i integruje "seo agentury", beze změny významu | DONE |
| 2 | "## Je lepší freelancer nebo agentura?" | "## Je lepší freelancer nebo SEO agentura?" | KW: nadpis zpřesněn na "SEO agentura" — sekce je celá o SEO tendru, žádná změna významu | DONE |
| 3 | "## Hodnotící kritéria:" | "## Hodnotící kritéria při výběru SEO agentury:" | KW: nadpis zpřesněn, integruje "seo agentura"/"seo agentury" — jasnější i pro čtenáře, beze změny významu | DONE |

**Keyword coverage po Kroku 1 (v tělu původního textu):**

| Keyword | Cíl (brief) | Ahrefs volume (CZ) | Výskyty v textu po Kroku 1 | Poznámka |
|---|---|---|---|---|
| seo agentura | 3-5x | 700/měs | 4 (H1 + odst. 3 "dobrou SEO agenturu" + nadpis #2 upravený + nadpis Hodnotící kritéria) | V cíli. Prostor pro 1 další přirozený výskyt v novém obsahu (CTA/sekce Krok 3), pokud to sedne. |
| seo agentury | 1-2x | 800/měs | 2 (odst. 2 upravený + nadpis "Hodnotící kritéria" — stejný string, počítáno zvlášť) | V cíli, žádné další vynucování. |
| seo agentura praha | 1-2x | 800/měs | 0 v těle | SKIP v těle — text nemá žádný pražský/lokální kontext, vnucení by porušilo pravidlo "nikdy neměnit význam" a ToV (žádná vágní/neopodstatněná tvrzení). Status: **NEW** — vyřeší se v Kroku 3 jako anchor text interního odkazu ("SEO agentura Praha" → /seo/) v CTA bloku, ne v běžícím textu. |

**Keywords checklist**
- [x] Klíčová slova seřazena dle objemu (viz keywords xlsx)
- [x] Top klíčové slovo ("seo agentura") umístěno v nadpisech (H1 + 2× H2)
- [x] První zmínka používá plnou formu ("SEO agenturu" v H1)
- [x] Drobné změny aplikovány přímo (DONE)
- [x] Žádné keyword stuffing — žádná věta nemá víc než 1 vloženou keyword frázi
- [x] Text čte přirozeně
- [ ] "seo agentura praha" — přesunuto do Kroku 3 (NEW, viz výše)

---

## Step 2 Log: ToV Rewrite

**Guide:** `evisions_tov_guide_CZ.md`
**Typ obsahu:** How-to / trend analýza — článek dává kritéria a rady k výběru SEO agentury; case study (Skrz.cz) je citovaná jako podpůrný důkaz uprostřed textu, ne jako hlavní rámec článku (na rozdíl od klasické evisions case study s vlastními klientskými čísly v úvodu).

**Přímé citace Martina Sajala a Marka Foršta (blockquote v originále) — NEMĚNĚNY beze zbytku**, jde o cizí/autorský výrok, ne parafrázi redakce.

| # | Original | Changed To | Reason |
|---|----------|------------|--------|
| 1 | "Neexistují totiž žádná objektivní srovnávací kritéria kvality práce agentur. Porovnávat výsledky, přístupy, postupy či strategie na odlišných projektech v různých fázích vývoje nemá žádnou relevantní vypovídající hodnotu. Provádět A/B testování SEO služeb více různých dodavatelů z principu bohužel nelze." | "Neexistují totiž žádná objektivní srovnávací kritéria kvality práce agentur. Porovnávat výsledky, přístupy, postupy či strategie na odlišných projektech v různých fázích vývoje nedává smysl. A/B testování SEO služeb u více různých dodavatelů navíc z principu nejde." | ToV: akademicky suchý obrat "nemá žádnou relevantní vypovídající hodnotu" → přímé "nedává smysl"; "Provádět... nelze" → přímější činný tvar "nejde" |
| 2 | "Rozdíly v kvalitě a přístupu různých dodavatelů jsou natolik zásadní, že je více než žádoucí výběrové řízení nepodcenit a věnovat mu adekvátní úsilí, čas i energii." | "Rozdíly v kvalitě a přístupu různých dodavatelů jsou natolik zásadní, že se výběrové řízení vyplatí nepodcenit a věnovat mu dost času i energie." | ToV: formální/vágní "je více než žádoucí" a akademické "adekvátní úsilí" → přímější "vyplatí se" a "dost času i energie" |
| 3 | "Abyste nemuseli prošlapávat trnitou cestičku nastavování parametrů výběrového řízení zcela od začátku, dovolím si Vás odkázat na zajímavou případovou studii (case study), ve které Martin Sajal popsal své zkušenosti z pořádání výběrového řízení na SEO služby pro vyhledavač slev Skrz.cz." | "Parametry výběrového řízení nemusíte vymýšlet od nuly — podívejte se na případovou studii, ve které Martin Sajal popsal své zkušenosti z pořádání výběrového řízení na SEO služby pro vyhledavač slev Skrz.cz." | ToV: odstraněna květnatá metafora ("prošlapávat trnitou cestičku") a přehnaně zdvořilý obrat ("dovolím si Vás odkázat") → přímé, aktivní oslovení dle sekce "Rovnou k věci" |
| 4 | "Pokud jste ve fázi hledání dodavatele SEO služeb, mohl by pro Vás být článek velmi užitečný a pomoci Vám s přípravou zadání, nastavení kritérií i vyhodnocováním. S Martinovým souhlasem si dovoluji vypíchnout některé důležité části. Věřím, že Vás zaujmou natolik, abyste si vyhradili pár minut k prostudování celého originálního článku (citace z martinova článku jsou pro větší přehlednost odlišeny oranžovou barvou):" | "Pokud hledáte dodavatele SEO služeb, může vám tento článek pomoct s přípravou zadání, nastavením kritérií i vyhodnocováním výběrového řízení. Se svolením Martina níže vypichuji nejdůležitější části — doporučuji ale přečíst si i celý originální článek. Citace z Martinova textu jsou níže odlišené jako citace:" | ToV: zjednodušena přehnaná zdvořilostní formálnost ("dovoluji vypíchnout", "Věřím, že Vás zaujmou natolik, abyste si vyhradili"); popisek vizuálního odlišení citací upraven z "oranžové barvy" (vázáno na starou šablonu evisions.cz) na obecné "odlišené jako citace" — odpovídá blockquote formátu nové šablony (`step4_html.py`), řeší se formálně v Kroku 4 |
| 5 | "Nepochybuji o tom, že tomu tak bude i nadále." | "Věřím, že tomu tak bude i nadále." | ToV Compliance (sekce 7): "Nepochybuji" je absolutní tvrzení o budoucnu bez podložení číslem → umírněnější "Věřím", v souladu s principem nevyslibovat jistotu bez dat |
| 6 | "Jak je z Martinova článku zřejmé, vybrat správnou a dobrou digitální agenturu není vůbec jednoduché." | "Vybrat správnou a dobrou digitální agenturu není vůbec jednoduché." | ToV sekce 5 "Rovnou k věci": odstraněna rekapitulační rozjezdová fráze ("Jak je z Martinova článku zřejmé" ~ vzor "Jak jsme již zmínili…" → smazat) |

**Co zůstalo beze změny:** všechna fakta, čísla, pořadí informací, citace Martina Sajala a Marka Foršta, klíčová slova z Kroku 1, seznamy kritérií (obsahově nedotčené).

---

## Step 3 Log: Struktura & formátování

**Guide:** `evisions_structure_guide_CZ.md`
**Speciální brief:** viz hlavička logu — vědomá výjimka, přidává nový obsah (CTA, sekce, závěr).

### Fáze 0: Audit odstavců (povinná první akce)

Žádný odstavec nepřesahoval 100 slov (nejdelší = ~62 slov, "Pokud to s optimalizací..."). Jeden odstavec (~77 slov, "Vybrat správnou a dobrou digitální agenturu...") byl přesto rozdělen na dva kratší kvůli čitelnosti a max. 3 odstavcům bez vizuálního zlomu (Structure Guide sekce 4).

### Oprava fidelity z Kroku 2 (zjištěno při auditu)

Při Kroku 2 (úprava odstavce "Abyste nemuseli prošlapávat...") jsem si nevšiml, že věta obsahovala interní odkaz na `/case-study-pripadova-studie/` (anchor "(case study)"), a ten mi při přepisu vypadl. Opraveno zpět — nyní odkaz na `/case-study-pripadova-studie/` s anchor textem "případovou studii".

### Interní odkazy — restaurované z originálu (WebFetch extrakce je při prvotním přepisu ztratila, protože jsem tehdy tahal jen čistý text)

| Anchor text | Cíl | Poznámka |
|---|---|---|
| "SEO agenturu" (odst. 3) | /seo/ | Restaurováno — odpovídá pozici zjištěné z WebFetch extrakce odkazů |
| "SEO služeb" (odst. 5) | /seo/ | Restaurováno — přesná původní pozice v HTML nebyla dohledatelná, umístěno na nejbližší přirozený výskyt fráze |
| "případovou studii" (odst. 6) | /case-study-pripadova-studie/ | Restaurováno (viz oprava výše) |

### Nový obsah dle briefu

**1. Průběžná CTA (2× Tip callout v těle, dle brief bodu 1):**
- Po úvodní části (před "Ačkoliv je internet plný..."): "Řešíte výběr SEO agentury právě teď?..." → anchor "naše SEO služby" → /seo/
- Po uzavření Skrz.cz case study (před `---` divider): "Chcete vidět, jak podobný přístup vypadá v praxi?..." → anchor "reference" → /nase-vysledky/, anchor "SEO agentury" → /seo/

**2. Nová sekce "Jak pracujeme my v Evisions?" (dle brief bodu 2), ~110 slov, 4 body + CTA:**
Vložena na konec, po sekci "Jak vybrat reklamní (marketingovou) agenturu?" a před novým Závěrem — v brief šabloně byla umístěna dřív v článku, ale reálná struktura tohoto článku nemá samostatnou "Časté chyby" sekci, takže nejpřirozenější přechod je až po obecných tipech, těsně před CTA závěrem.
Anchor "SEO agentura Praha" → /seo/ (fráze "Jsme SEO agentura Praha s klienty po celé ČR i v zahraničí" — fakticky podložené, evisions je pražská agentura dle CLAUDE.md popisu firmy; styl je záměrně keyword-explicitní, běžné v české komerční webové copy pro lokální SEO anchor).

**3. Upravený závěr (dle brief bodu 3):** nová sekce `## Závěr` — 1-2 věty shrnutí + explicitní CTA. Původní uzavírací odstavec ("Pokud nepodceníte výše uvedená kritéria...") ZACHOVÁN beze změny, nový Závěr je až po něm a po sekci "Jak pracujeme".
**Kontaktní formulář (brief bod 3, "pokud to šablona podporuje"):** NEIMPLEMENTOVÁNO v markdownu — jde o CMS/šablonový prvek mimo rozsah tohoto contentového kroku. Pokud evisions.cz šablona vložený formulář podporuje, je potřeba ho doplnit na úrovni publikace (WordPress/CMS), ne v `article_..._CZ.md`. Upozornit uživatele v QA shrnutí.

**4. Tabulka Freelancer vs. Agentura** — nová, vizualizuje trade-off už popsaný v textu (Sajalova citace o zastupitelnosti a šíři znalostí), nepřidává nová fakta. Umístěna po odstavci "Každá z variant (freelancer/agentura)..." před `## Kvalita nabídek agentur:`.

### Keyword density po Kroku 3 (celý článek, ~1 280 slov)

| Keyword (libovolný pád) | Výskytů | Odhad hustoty |
|---|---|---|
| "seo agentur*" (agentura/agenturu/agentury dohromady) | 11 | ~1,7 % (11×2 slova / 1280) |
| — z toho "seo agentura" (nom.) | 4 | |
| — z toho "seo agenturu" (akuz.) | 3 | |
| — z toho "seo agentury" (gen./pl.) | 4 | |
| "seo agentura praha" | 1 | v cíli (1-2x) |

Poznámka: brief zadával "seo agentura" 3-5x a "seo agentury" 1-2x zvlášť, ale zároveň cílovou hustotu 1-2 % a vlastní příklady CTA/nadpisů, které samy o sobě znějí přes 5 výskytů. Počítáno dohromady přes všechny pády (lemma), ne striktně po jednotlivých tvarech — u skloňovaného jazyka jako čeština je to standardní přístup. Výsledná hustota 1,7 % je v zadaném rozmezí 1-2 %, ale absolutní počet (11) je nad brief's "3-5x" pokynem pro "seo agentura" samostatně. Pokud to uživatel považuje za příliš mnoho, lze 2-3 zmínky odstranit (kandidáti: "SEO agentury" v CTA-B, "Kontaktujte nás" duplicitní odkaz v Závěru).

### Interní odkazy — finální přehled

| Cíl | Počet | Anchor texty |
|---|---|---|
| /seo/ | 8 | "naše SEO služby", "SEO agenturu" (×2), "SEO služeb", "SEO agentury", "SEO agentura Praha", "Ozvěte se nám", "Kontaktujte nás" |
| /nase-vysledky/ | 1 | "reference" |
| /case-study-pripadova-studie/ | 1 | "případovou studii" |

8 odkazů na `/seo/` v jednom článku je nadstandardní hustota — záměrně, protože brief cílí na maximalizaci konverze. Pokud by to při publikaci působilo přeplácaně, doporučuji při finální revizi snížit na cca 5 (ponechat: 2 restaurované původní + 1 CTA + sekce Evisions + Závěr).

### Callouty a formátování

- 2× Tip callout (CTA A, B) — v mezích "2-3 callouty" pro střední délku článku (Structure Guide)
- 1× tabulka (Freelancer vs. Agentura) — v mezích "1-2 tabulky"
- Nadpisová hierarchie: H1 → H2 pouze, žádné přeskočení úrovní
- Standardní "Poznámka k obsahu" blok (Structure Guide sekce 3) se vkládá automaticky v Kroku 4 přes `step4_html.py`, není v markdownu ručně

---

## Step 5 Log: QA & revize

**Přesnost obsahu**
- [x] Všechna fakta z originálu beze změny (viz core principle výjimka v hlavičce — přidán byl jen nový CTA/sekční obsah, ne pozměněna fakta)
- [x] Odkazy ověřeny živě (WebFetch):
  - `/seo/` — existuje, H1 "SEO služby", kontaktní formulář ✅
  - `/nase-vysledky/` — existuje, "Naše výsledky – co dokážeme v praxi" ✅
  - `/case-study-pripadova-studie/` — **ROZBITÝ** (spadá na `/blog/`, není to samostatná stránka). Toto byl původní odkaz z živého článku, ne moje přidání. **Opraveno** na `/blog/tag/case-study-pripadova-studie/` (aktuální tag archiv case studies) — regenerováno HTML i docx po opravě.
- [x] Obrázky na správných pozicích — žádné obrázky v těle textu, autor profilovka mimo rozsah markdownu (viz níže)

**ToV compliance**
- [x] Tón odpovídá How-to klasifikaci
- [x] Žádné zakázané fráze
- [x] Žádné garance konkrétních výsledků (viz Krok 2, edit #5)

**Structure compliance**
- [x] Hierarchie nadpisů (H1 → H2, žádný přeskočený level)
- [x] Interní odkazy přítomny (10 odkazů: 8× /seo/, 1× /nase-vysledky/, 1× /blog/tag/case-study-pripadova-studie/)
- [ ] **E-E-A-T autor — ZNÁMÝ GAP:** `step4_html.py` šablona generuje generický autor box ("Content Team / evisions Advertising"), ne skutečného autora článku (Marek Foršt, Head of SEO) zjištěného při Initu. Toto je limit šablonového skriptu (autor box je hardcoded), ne něco opravitelné v tomto markdown souboru — je potřeba buď upravit `_html_template()` v `src/step4_html.py`, aby přijímal autor jméno/roli jako parametr, nebo doplnit ručně při publikaci v CMS.

**Technické**
- [x] HTML se správně renderuje (ověřeno gramaticky přes grep — žádné nerozbité `[text](url)` zbytky)
- [x] Žádné nefunkční odkazy (po opravě výše)
- [ ] Meta popisek (150-160 znaků) — **CHYBÍ.** Originál měl meta title "SEO agentura: Jak najít tu pravou pro váš byznys", meta description nebyla ve WebFetch extrakci dostupná. Nová šablona generuje `<title>` automaticky z H1 ("Jak vybrat nejlepší SEO agenturu? | evisions.cz Blog"), ale nevytváří `<meta name="description">` vůbec — šablona ho nepodporuje. Potřeba doplnit ručně v CMS při publikaci.

**Kvalita**
- [x] Odpovídá ToV Guide principům
- [x] Actionable závěr s jasnou CTA

### Otevřené body pro uživatele (nutno rozhodnout před publikací)

1. **8 odkazů na `/seo/`** — záměrně agresivní dle briefu, ale nadstandard. Ponecháno beze změny, protože uživatel na dotaz v Kroku 3 neřekl, ať se sníží.
2. **Kontaktní formulář v článku** (brief bod 3) — needimplementováno, jde o CMS prvek mimo markdown.
3. **Autor box v HTML** ukazuje generické "Content Team", ne Marka Foršta — limit šablony, ne obsahu.
4. **Meta description chybí** — nutno doplnit v CMS při publikaci, ideálně 150-160 znaků s "seo agentura" v textu.

### Výstupní soubory (finální)

```
data/output/articles/jak-vybrat-nejlepsi-seo-agenturu/article_jak-vybrat-nejlepsi-seo-agenturu_CZ.md
data/output/articles/jak-vybrat-nejlepsi-seo-agenturu/article_jak-vybrat-nejlepsi-seo-agenturu_CZ.html
data/output/articles/jak-vybrat-nejlepsi-seo-agenturu/article_jak-vybrat-nejlepsi-seo-agenturu_CZ.docx
data/output/articles/jak-vybrat-nejlepsi-seo-agenturu/article_jak-vybrat-nejlepsi-seo-agenturu_CZ_log.md
data/output/articles/jak-vybrat-nejlepsi-seo-agenturu/article_jak-vybrat-nejlepsi-seo-agenturu_CZ_log.html
data/output/keywords/jak-vybrat-nejlepsi-seo-agenturu_keywords.xlsx
```

---

## Post-QA úprava (na žádost uživatele)

Uživatel: "jen at tam ten formulář je vyznačen kde by měl být, a ty odkazy zas at to není úplně nasílu"

| # | Original | New | Reason |
|---|----------|-----|--------|
| 1 | "Jsme [SEO agentura Praha](/seo/) s klienty po celé ČR i v zahraničí" | "Jsme SEO agentura Praha s klienty po celé ČR i v zahraničí" | Odlinkováno — frázový keyword-anchor hned na začátku krátké sekce působil nuceně. Text (a tím i keyword) zůstává, jen bez odkazu; sekce už má vlastní CTA odkaz o dvě věty níž. |
| 2 | "Chcete najít tu pravou [SEO agenturu](/seo/) pro váš projekt? [Kontaktujte nás](/seo/) a probereme..." | "Chcete najít tu pravou SEO agenturu pro váš projekt? [Kontaktujte nás](/seo/) a probereme..." | Odlinkováno — dva odkazy na stejnou URL ve dvou po sobě jdoucích větách působily nuceně. Ponechán jen funkční CTA odkaz "Kontaktujte nás". |
| 3 | (chybělo) | *[ZDE VLOŽIT: zjednodušený kontaktní formulář (jméno, e-mail, zpráva) — pokud to šablona evisions.cz na blogu podporuje]* | Placeholder vložen na konec Závěru dle brief bodu 3 — je to CMS prvek, markdown ho nemůže implementovat, ale místo je teď jasně vyznačené pro toho, kdo bude publikovat. |

**Výsledek:** odkazy na `/seo/` sníženy z 8 na 6 (2 restaurované originální + 4 CTA momenty — po intro, po case study, konec sekce "Jak pracujeme", konec Závěru). HTML a docx přegenerovány.

**STAV: HOTOVO** (s otevřenými body níže k rozhodnutí uživatele před publikací na evisions.cz).

**Zbývající otevřené body** (nezměněny touto úpravou): autor box v HTML šabloně ukazuje generické "Content Team" místo Marka Foršta; meta description chybí a musí se doplnit v CMS.

---

## Post-QA úprava #2 (na žádost uživatele)

Uživatel: "jen ten kontaktní formulář mi přijde moc nízko ne třeba tolik uživatelů se tam docrolluje nebylo by lepší ho dát výše"

| Original pozice | Nová pozice | Reason |
|---|---|---|
| Konec Závěru (~99 % délky článku) | Za CTA callout po Skrz.cz case study, před `---` divider (~63 % délky článku) | Formulář na samém konci by ho většina čtenářů nikdy neviděla. Nová pozice je hned po prvním velkém "proof" momentu (case study) a před sekcí s obecnými tipy — čtenář, který se dostal až sem, má už dost kontextu, aby konvertoval, a zbytek článku (obecné tipy + Jak pracujeme + Závěr) pořád existuje pro ty, co chtějí číst dál. |

HTML a docx přegenerovány.

