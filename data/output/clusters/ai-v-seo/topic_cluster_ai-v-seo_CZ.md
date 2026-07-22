# Topic Cluster Audit: AI v SEO

Datum: 2026-07-21
Zpracoval: Claude Code (/evisions-topic-cluster)

## Zadání

**Téma:** AI v SEO

**Stávající články (zadané):**
- https://www.evisions.cz/blog/10-tasku-do-kterych-se-seo-specialistovi-vyplati-zapojit-chat-gpt/
- https://www.evisions.cz/blog/seo-restart-2023-vyuziti-ai-nulove-hledanosti-i-zmeny-ve-svete-linkbuildingu/
- https://www.evisions.cz/blog/geo-optimalizace-pro-ai-vyhledavace-nova-era-seo-je-tady/

**Doplněno auditem z Content Plan Sheetu (Krok 4):**
- https://www.evisions.cz/blog/query-fan-out-v-praxi-jak-na-zaklade-dat-optimalizovat-obsah-pro-ai/ (AI-01)
- https://www.evisions.cz/blog/jak-funguje-ai-mode-od-googlu-novy-zpusob-vyhledavani-strucne-a-jednoduse/ (AI-02)
- https://www.evisions.cz/blog/moneta-money-bank-seo-ai-case-study-preciznim-seo-a-geo-k-nejlepsimu-zobrazovani-v-ai-vyhledavani-ve-financnim-sektoru/ (FIN-01)

## Krok 1: Klíčová slova

Primární keywords (bez kanibalizace):

| Článek | Primární keyword | SV (Ahrefs/MM) |
|---|---|---|
| 10 tasků ChatGPT pro SEO | chatgpt seo | 10/– |
| SEO Restart 2023 | ai v seo | 20/– |
| GEO optimalizace pro AI vyhledávače | co je geo | 70/40 |

Cross-check Search Volume přes Marketing Miner API odhalil dva výrazné rozdíly nad prahem 30–50 %:
- **ai overview**: Ahrefs 200 / MM 360 (+80 %), MM navíc ukazuje rostoucí měsíční trend (450 v posledním měsíci)
- **co je geo**: Ahrefs 70 / MM 40 (−43 %), MM ukazuje prudký nárůst z ~0 na 90/měsíc za poslední 2 měsíce

Komerčně kontaminovaný klastr identifikován: bare "ai seo" (150 SV) a příbuzné dotazy ("ai seo expert", "ai seo konzultant", "kde najmout ai seo experta") nesou service/hiring intent — nevhodné jako blogový primární keyword.

## Krok 2: Konkurence — primární keywords

Dominantní konkurent napříč celým clusterem: **SEO Consult (seoconsult.cz)** — má service stránky (`/seo-pro-chatgpt`, `/seo-pro-ai-overviews`, `/seo-ai-specialista`) i blogové články na téměř identická témata. Další: Seokonzult.cz, Advisio.cz, JZShop.cz. Pro "co je geo" přeplněný prostor — 9+ CZ zdrojů (MarketingPPC, Sonet Studio, Avedeo, Khoder, Upgates, Digichef, Josef Pajer, Webotvůrci, Bronislav Markowicz, Shoptet).

Obsahový typ: návody/checklisty a vysvětlovací články dominují. Nikdo z konkurence nemá datově podložené case studies s konkrétním klientem — silná diferenciace pro evisions ToV.

## Krok 3: Rozšířená analýza (7+ dodatečných keywords)

| Klíčové slovo | SV (Ahrefs/MM) |
|---|---|
| ai overview | 200/360 (rostoucí) |
| co je ai overview | –/10 |
| generative engine optimization | 100/80 (YoY +300 %) |
| geo optimalizace / geo seo | 40/60,80 (YoY +430 %) |
| ai vyhledávání | –/70 (YoY +96 %, nalezeno jen přes Marketing Miner) |
| seo trendy (2026) | 150/– |
| seo a umělá inteligence | 20/– |

Klíčový fakt: **Google AI Overview byl v ČR spuštěn v květnu 2025** (ČR mezi prvními zeměmi v Evropě). Dopad: +49 % impresí, −30 % kliků z organiky, u informačních dotazů propad CTR až −88 %. Konkurence u "ai overview": Seokonzult, Shoptet, Upgates, Lady Virtual, Malá marketingová, MF Group, Advisio, Conviu, Webkat — žádný nestaví obsah na této konkrétní časové ose + tvrdých číslech.

## Krok 4: Audit obsahu a Content Gap

**Rozšíření zjištěno:** Content Plan Sheet obsahuje 3 další publikované AI & SEO články nezahrnuté v původním zadání (viz výše) — Query fan-out, AI Mode od Googlu, a MONETA case study (**explicitně o AI Overviews** — 13 % AIO visibility, 8 326 keywords v AIO, top 20 nejcitovanějších domén v ČR).

Ahrefs `site-explorer-organic-keywords`: žádný z původních 3 článků aktuálně nerankuje na nic (0 keywords) — ověřeno, že jde o reálný stav, ne mezeru v datech (starší obsah webu, např. "normostrana", běžně rankuje). Topic Authority AI/GEO clusteru je tedy nulová v měřitelné organické viditelnosti, i když obsahová hloubka je na místě.

### Souhrnná tabulka pokrytí klíčových slov

| Klíčové slovo | Rozhodnutí | Kam / proč |
|---|---|---|
| chatgpt seo | Primární | Článek 1 |
| ai v seo | Primární | Článek 2 |
| co je geo | Primární | Článek 3 |
| query fan-out (seo) | Primární | Článek 4 |
| ai mode google | Primární | Článek 5 |
| seo strategie ai overviews | Primární (branded) | Článek 6 (MONETA) |
| ai overview | Cíl pro nový článek | Chybí top-of-funnel hub |
| co je ai overview | Sekundární | K novému článku |
| ai vyhledávání | Sekundární | K novému článku |
| generative engine optimization | Sekundární | Článek 3 |
| geo optimalizace / geo seo | Sekundární | Článek 3 |
| seo a umělá inteligence | Sekundární | Článek 2 |
| seo trendy / seo trendy 2026 | Zamítnuto | Mimo AI fokus, vlastní cluster |
| ai seo (bare), seo ai, ai seo tool/audit/konzultant | Zamítnuto | Service/hiring intent kontaminace |

**Hlavní Content Gap:** chybí propojovací hub článek k "AI Overview", který by svazoval Query fan-out, AI Mode a MONETA case study dohromady pro čtenáře na začátku cesty.

## Krok 5: Finální akční plán

Revidují se 2 stávající články, píše se 1 nový. Žádná kanibalizace — každý kus obsahu má unikátní primární keyword.

### REVIDOVAT

**GEO optimalizace pro AI vyhledávače**
https://www.evisions.cz/blog/geo-optimalizace-pro-ai-vyhledavace-nova-era-seo-je-tady/
- Primární keyword beze změny: co je geo
- Doplnit sekundární keywords: "generative engine optimization", "geo seo" (anglický ekvivalent + synonymum, oboje s rostoucím trendem v MM)
- Přidat interní odkaz na nový hub článek "AI Overview" (viz níže) a na Query fan-out článek
- Zvážit rozšíření o aktuálnější příklad/data vzhledem k přeplněnému konkurenčnímu prostoru (9+ CZ zdrojů na stejné téma)

**SEO Restart 2023: Využití AI, nulové hledanosti i změny ve světě linkbuildingu**
https://www.evisions.cz/blog/seo-restart-2023-vyuziti-ai-nulove-hledanosti-i-zmeny-ve-svete-linkbuildingu/
- Primární keyword beze změny: ai v seo
- Doplnit sekundární keyword: "seo a umělá inteligence" (přímé synonymum)
- Přidat interní odkazy na novější články clusteru (Query fan-out, AI Mode, GEO) — článek je datovaný 2023 a bez prolinkování působí izolovaně od zbytku clusteru

### NAPSAT NOVĚ

**Co je Google AI Overview a jak ovlivňuje SEO v Česku**
- **Primární keyword:** ai overview
- **Kontrola intentu:** Ověřeno v Kroku 2/3 SERP datech — konkurence na "ai overview" je čistě editorial/informační (tech magazíny, SEO blogy vysvětlující funkci), žádný signál nástrojového/navigačního intentu. Bare termín je bezpečný jako primární keyword.
- **Proč:** Nejvyšší search volume v celém clusteru (200 Ahrefs/360 MM, rostoucí trend), silný datový hook (spuštění v ČR květen 2025, konkrétní CTR čísla), nulové současné pokrytí, a funguje jako chybějící top-of-funnel hub propojující Query fan-out, AI Mode a MONETA case study — ty zůstávají bez něj izolované.
- Sekundární keywords: "co je ai overview", "ai vyhledávání"
- Doporučené interní odkazy: Query fan-out v praxi, Jak funguje AI Mode od Googlu, MONETA case study (jako proof-of-execution)

### Shrnutí a zdůvodnění

Kombinace 2 revizí + 1 nového článku dobuduje kompletní topic authority k "AI v SEO": stávající 3 nově objevené články (Query fan-out, AI Mode, MONETA) mají hloubku a datový důkaz, ale chybí jim vstupní bod pro čtenáře na začátku cesty — to řeší nový hub o AI Overview. Revize GEO a SEO Restart článků doplňují sekundární keywords a prolinkování, aby celý cluster fungoval jako propojená síť, ne 6 izolovaných kusů obsahu. Žádné dva kusy obsahu nesdílí primární keyword — bezkanibalizační stav potvrzen jak plánovaně (Krok 1), tak reálně (Krok 4, Ahrefs organic keywords).
