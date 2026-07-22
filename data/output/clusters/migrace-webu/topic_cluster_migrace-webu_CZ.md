# Topic Cluster Audit: Migrace webu

**Datum:** 2026-07-20
**Stávající články:**
- Průvodce migrací webu z pohledu SEO — https://www.evisions.cz/blog/pruvodce-migraci-webu-z-pohledu-seo-aneb-nezahravejte-si-s-organickou-navstevnosti/
- Úspěšná SEO migrace webu Foodora.cz — https://www.evisions.cz/blog/uspesna-seo-migrace-webu-foodora-cz-od-stareho-k-novemu/

---

## Krok 1: Klíčová slova

Ahrefs data pro ČR ukazují, že jde o typicky nízkoobjemové expertní B2B téma — většina long-tail variant má objem 0 a Ahrefs je vůbec nevrací. Žádné komerční ani transakční klíčové slovo s reálným objemem se nenašlo.

### Informační

| Klíčové slovo | Search Volume | KD | Poznámka |
|---|---|---|---|
| crawl budget | 300 | 22 | obecný SEO pojem, silně související |
| robots.txt | 200 | 73 | obecný SEO pojem |
| přesměrování 301 | 150 | – | přímo migrační téma |
| canonical tag | 100 | 59 | obecný SEO pojem |
| sitemap.xml | 100 | 85 | obecný SEO pojem |
| redesign webu | 100 | 0 | hraniční téma |
| migrace domény | 80 | – | primární keyword článku Foodora (Krok 1 návrh) |
| 301 redirect | 80 | 72 | anglická varianta |
| migrace wordpressu | 30 | – | CMS-specific, zamítnuto v Kroku 4 |
| co je sitemap | 20 | – | LSI |
| migrace webu | 10 | – | primární keyword Průvodce (Krok 1 návrh) |
| co je crawl budget | 10 | – | LSI |
| 301 vs 302 | 10 | – | technická otázka |
| 301 přesměrování | 10 | – | duplicitní forma |

### Komerční / Transakční
Žádné klíčové slovo s měřitelným objemem v ČR — téma je čistě informační/expertní.

### LSI / příbuzné dotazy (PAA)
- Jaký pokles návštěvnosti je normální (10–20 % dočasně, nad 30 % = problém)
- Jak dlouho trvá reindexace (2–4 týdny)
- Je nutná migrace při změně WP šablony bez změny URL?
- Lze dělat redesign a změnu domény zároveň? (nedoporučeno)
- Kdy migrovat web (ne v pátek, úterý/středa ráno)
- 1:1 redirect mapping
- Staging web a heslo
- noindex vs disallow
- Google Search Console — nahlášení změny adresy

---

## Krok 2: SERP analýza primárních keywords

**Klíčové zjištění:** Ahrefs nemá SERP data pro `migrace webu` a `migrace domény` (pod prahem crawlování). Živý Google SERP (WebSearch) odhalil, že bare termy jsou kontaminované jiným významem:

- `migrace webu` → dominují **hostingové firmy** (Webkitty, Webglobe, WEDOS, Forpsi, eGate, Besteto) nabízející technické stěhování mezi servery.
- `migrace domény` → dominují registrátoři/hostingy nabízející přenos domény jako technickou službu.

Po přidání "seo" se SERP kompletně překlápí na editorial obsah, kde už evisions.cz reálně figuruje.

**Úprava primárních keywords:**

| Článek | Nový primární keyword |
|---|---|
| Průvodce migrací webu z pohledu SEO | `migrace webu seo` |
| Foodora.cz case study | `seo migrace domény` |

### Konkurence (top hráči)

| Doména | Typ | Obsah |
|---|---|---|
| SEO Consult | agentura | 2 obsáhlé návody |
| SEOPRAKTICKY.cz | vzdělávací portál | komplexní "Checklist" |
| Ranktracker.com (CZ blog) | zahr. SaaS, lokalizace | dlouhý článek |
| Jan Pospíšil | freelance konzultant | osobní blog |
| iuntsevich.cz | butiková agentura | redesign+přesun úhel |
| jakpsatweb.cz | starý webmasterský portál | **unikátní: metodika odhadu poklesu** |
| ecommercebridge.cz | e-commerce magazín | rebrand/CMS v e-commerce |
| proficio.cz, dejtonaweb.cz, pureonline.cz, vceliste.cz | agentury | standardní návody |
| Google Search Console nápověda | oficiální dokumentace | nástroj Změna adresy |

**Co dělat lépe:** Kombinace case study + komplexní guide na jedné doméně nemá žádný konkurent. Chybí datový/kalkulační úhel. E-commerce specifický úhel (vzhledem k Foodora) můžeme držet silněji.

---

## Krok 3: Rozšířená analýza konkurence

8 dalších informačních keywords k širšímu tématu:

| # | Klíčové slovo | SERP charakter |
|---|---|---|
| 1 | propad návštěvnosti po migraci webu | plně editorial/SEO |
| 2 | redesign webu seo | žádná/minimální česká konkurence |
| 3 | crawl budget | mix zahraničních glosářů + slabší CZ weby |
| 4 | canonical tag co to je | silná česká glosářová konkurence |
| 5 | migrace e-shopu seo | dominují platform-specific návody (Shoptet, Shopify) |
| 6 | nástroj změna adresy GSC | úzká nika, ovládá ji Google dokumentace |
| 7 | změna domény seo rebrand | bohatě obsazené, emocionální/risk framing |
| 8 | 301 přesměrování jak nastavit | implementační (vývojářský) intent |

**Rozšířená zjištění:**
- Vzorec "bare term = jiný intent, qualifier = editorial" se opakuje napříč celým clusterem.
- `redesign webu seo` — content gap, minimální domácí konkurence (jeden nepřímý konkurent nalezen u příbuzného dotazu — rudolfschmelzer.cz "Redesign webu a SEO: checklist 2026").
- `změna domény seo rebrand` — bohatě obsazené, konkurence používá konkrétní % čísla (20–40 % pokles, návrat za 3–6 měsíců) a emocionální framing. Validuje volbu `seo migrace domény` pro Foodora, ale ukazuje potřebu explicitněji komunikovat vlastní čísla (8 % pokles) v kontrastu.
- `migrace e-shopu seo` a `301 přesměrování jak nastavit` — nevhodné pro nový článek (platform-specific dominance / vývojářský intent mimo personu).
- `nástroj změna adresy GSC` — lepší jako sekce ve stávajícím guide než samostatný článek (Google dokumentace vždy vyhraje #1).

---

## Krok 4: Audit obsahu a Content Gap analýza

**Content Plan Sheet:** žádný další naplánovaný řádek k tématu migrace webu — bez rizika duplicity.

**Kanibalizace:** Ahrefs nemá pro evisions.cz v ČR žádná organic keyword data (ani na úrovni domény). Podle živých SERP dat (Kroky 2–3): Průvodce se reálně objevuje ve výsledcích pro všechny testované qualified dotazy, Foodora case study se neobjevila v žádném. Žádná aktivní kanibalizace, ale Foodora case study má dnes nízkou informační SERP viditelnost — potřeba posílit v revizi.

### Souhrnná tabulka pokrytí

| Klíčové slovo / skupina | Rozhodnutí | Kam |
|---|---|---|
| `migrace webu seo` | Primární | Průvodce (revize) |
| `seo migrace domény`, `změna domény seo rebrand` | Primární | Foodora (revize) |
| `migrace webu`, `migrace domény` (bare) | Sekundární, nepřímo | oba stávající články |
| `redesign webu`, `redesign webu seo` | Cíl nového článku | NOVÝ #1 |
| `propad návštěvnosti po migraci webu` | Cíl nového článku | NOVÝ #2 |
| `crawl budget`, `co je crawl budget` | Sekundární | Průvodce |
| `canonical tag`, `canonical tag co to je` | Sekundární | Průvodce |
| `sitemap.xml`, `co je sitemap`, `robots.txt` | Sekundární | Průvodce |
| `přesměrování 301`, `301 redirect`, `301 vs 302`, `301 přesměrování` | Sekundární | Průvodce |
| `nástroj změna adresy GSC` | Sekundární, doplnit explicitně | Průvodce (revize) |
| LSI (doba reindexace, timing, staging+heslo, noindex vs disallow, redirect mapping 1:1) | Doplnit do checklistu | Průvodce (revize) |
| `migrace wordpressu` | Zamítnuto — hostingový/CMS intent, mimo personu | — |
| `migrace e-shopu seo` | Zamítnuto (prozatím) — platform-specific SERP dominance | — |
| `301 přesměrování jak nastavit` | Zamítnuto — implementační/vývojářský intent | — |

**Topic Authority:** Solidní základ (guide + case study), dvě mezery: (1) redesign jako samostatný spouštěč není pokryt, (2) chybí datově podložený "risk" obsah jako samostatný linkbait asset. Foodora case study je slabě propojená s informační SERP viditelností.

---

## Krok 5: Finální akční plán

Revidují se **2 stávající články**, píší se **2 nové**. Každý má unikátní primární keyword → bez rizika kanibalizace.

### REVIDOVAT

**Průvodce migrací webu z pohledu SEO**
https://www.evisions.cz/blog/pruvodce-migraci-webu-z-pohledu-seo-aneb-nezahravejte-si-s-organickou-navstevnosti/
Nový primární keyword: `migrace webu seo` (změna z bare `migrace webu` — tool intent kontaminace)
- Doplnit explicitní pojmenovanou zmínku nástroje "Změna adresy" v Google Search Console
- Doplnit konkrétní % benchmark poklesu návštěvnosti (10–20 % normální, nad 30 %/měsíc = problém) a dobu reindexace (2–4 týdny)
- Přidat prolinkování na oba nové články (redesign, propad návštěvnosti)
- Zesílit odkaz na Foodora case study jako "proof" příklad v úvodu/závěru

**Úspěšná SEO migrace webu Foodora.cz**
https://www.evisions.cz/blog/uspesna-seo-migrace-webu-foodora-cz-od-stareho-k-novemu/
Nový primární keyword: `seo migrace domény`
- Posílit title/meta/H2 strukturu směrem k informačnímu keywordu (dnes nulová viditelnost v testovaných SERP)
- Explicitně srovnat vlastní číslo (8% pokles non-brand prokliků) s "normálním" rozsahem 20–40 % z konkurenčních zdrojů
- Prolinkovat na Průvodce a na nový článek o propadu návštěvnosti

### NAPSAT NOVĚ

**Redesign webu a SEO: jak při změně vzhledu nepřijít o pozice** (pracovní titulek)
Primární keyword: `redesign webu seo`
Kontrola intentu: Exact-match dotaz nemá v CZ SERP téměř žádnou domácí konkurenci — výsledky jsou převážně zahraniční editorial obsah, žádný tool/nástrojový intent. Příbuzný dotaz odhalil jednoho přímého CZ konkurenta (rudolfschmelzer.cz), téma je tedy řádově méně obsazené než hlavní migrační termíny.
Proč: content gap z Kroku 3 — redesign je samostatný spouštěč migrace, dnes zmíněný v Průvodci jen okrajově.

**Kolik návštěvnosti se ztrácí při migraci webu? Reálná čísla a jak se poučit z chyb** (pracovní titulek)
Primární keyword: `propad návštěvnosti po migraci webu`
Kontrola intentu: SERP je plně editorial (vceliste.cz, janpospisil.cz, pureonline.cz, prowebo.cz aj.), žádný nástrojový/navigační prvek.
Proč: datový/risk-benchmark úhel chybí v clusteru, konkurence ho používá jako linkbait (např. Real Madrid −14M návštěv/měsíc), a máme vlastní reálná čísla z Foodora case study jako kontrast.

### Shrnutí a zdůvodnění

Guide (`migrace webu seo`) zůstává pilířem celého clusteru, Foodora case study (`seo migrace domény`) dokazuje reálný výsledek, a dva nové články prohlubují konkrétní subtémata (redesign scénář, datový risk benchmark), která dnes nikdo v české konkurenci nepokrývá se stejnou hloubkou. Všechny čtyři primární keywords jsou vzájemně odlišné → bez kanibalizace. Obsahy se přirozeně prolinkují: Guide odkazuje na oba nové články i na case study jako proof point; nové články odkazují zpět na Guide (proces) a na Foodora case study (reálná čísla); Foodora case study odkazuje na Guide jako obecný návod. Foodora case study jako jediný skutečný proof-point v celém českém SERP pro toto téma je klíčová diferenciace, kterou stojí za to v revizi maximálně využít.
