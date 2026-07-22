# Topic Cluster Audit: SEO nástroje

Datum: 2026-07-21
Zpracoval: Claude Code (/evisions-topic-cluster)

## Zadání

**Téma:** SEO nástroje

**Stávající články (dohledáno z názvů témat, potvrzeno uživatelem):**
- Průvodce regulárními výrazy pro začátečníky — https://www.evisions.cz/blog-2022-01-26-pruvodce-regularnimi-vyrazy-pro-zacatecniky/
- SEO nástroje + 7 rozšíření, která vám usnadní práci — https://www.evisions.cz/blog/seo-nastroje-7-rozsireni-ktera-vam-usnadni-praci/

## Krok 1: Klíčová slova

| Článek | Primární keyword | SV (Ahrefs/MM) | KD |
|---|---|---|---|
| SEO nástroje + 7 rozšíření | seo nástroje | 1000/260 | 0 |
| Průvodce regulárními výrazy | regulární výrazy | 100/230 | 0 |

Klíčové zjištění: bare "regex" (600 Ahrefs/1400 MM) má KD 92 a okolní matching-terms (php, java, python, c#, sql, notepad++, htaccess, jquery) ukazují, že poptávka je převážně programátorská, ne SEO/marketingová — vědomě zvolen "regulární výrazy" jako primární i přes nižší objem.

Cross-check přes Marketing Miner API odhalil výrazné rozdíly u "seo nástroje" (1000/260, −74 %), "nástroj na seo" (1400/120, −91 %) a "regulární výrazy" (100/230, +130 %, opačný směr).

## Krok 2: Konkurence — primární keywords

**"seo nástroje":** Marketing Miner (vlastní blog), Vceliste.cz (DR53, 1616 návštěv/měsíc — nejsilnější), Seoprakticky.cz, Strafelda.cz, Whitepress.com, Serpstat.com. Vzorec: téměř všichni mají "roku 2026" v titulku, formát komplexních přehledů/žebříčků vítězí nad úzkým rozsahem. AI Overview aktivně cituje 6 zdrojů.

**"regulární výrazy":** SERP 100% obsazen generickým programátorským/akademickým obsahem — Wikipedia, Microsoft Learn (.NET), ČVUT, MUNI, regularnivyrazy.info, root.cz. **Nulová SEO/marketingová konkurence** v top 10 — potvrzuje audience mismatch.

## Krok 3: Rozšířená analýza (7 dodatečných keywords)

| Klíčové slovo | SV (Ahrefs/MM) | Rozhodnutí |
|---|---|---|
| nástroj na seo | 1400/120 | Sekundární |
| seo nástroje zdarma | 800/410 (YoY +208 %) | Sekundární — stejný SERP/konkurenti jako primární keyword |
| seo nástroje online | 150/20 | Sekundární |
| co je regex | 20/– | Sekundární |
| regulární výrazy příklady | 10/10 | Sekundární |
| screaming frog | 250/390, KD5 | Zamítnuto — SERP 100% ovládnut vlastní značkou nástroje |
| seo checker | 700/–, KD87 | Zamítnuto — nástrojově kontaminovaný dotaz |

Marketing Miner suggestions nepřinesly žádného silného nového kandidáta nad rámec výše uvedených — potvrdily jen další programátorské varianty regexu a drobné slovosledové varianty SEO nástrojů. Žádná "regulární výrazy pro SEO" varianta s měřitelným objemem neexistuje.

## Krok 4: Audit obsahu a Content Gap

### Reálné rankování (Ahrefs, mode=exact)

**SEO nástroje + 7 rozšíření** — rankuje na 4 keywords, vše str. 2–3, prakticky bez návštěvnosti:

| Keyword | Pozice | Volume | Traffic |
|---|---|---|---|
| nástroj na seo | 21 | 2600 | 5 |
| seo program | 26 | 600 | 0 |
| seo nástroje | 16 | 600 | 0 |
| seo nástroj | 24 | 400 | 1 |

**Průvodce regulárními výrazy** — 0 keywords, žádné rankování.

Žádná kanibalizace mezi oběma články. Content Plan Sheet neobsahuje TODO/Draft duplicitu k žádnému z témat.

### Topic Authority

**SEO nástroje:** Slabá, ale snadno napravitelná — reálné rankování existuje, ale uvízlé na str. 2–3 i přes KD 0. Problém je v obsahu (rozsah, aktuálnost), ne v obtížnosti trhu.

**Regulární výrazy:** Nulová organická viditelnost, SERP zcela mimo cílové publikum. Realistické očekávání: podpůrný/E-E-A-T obsah, ne růstový driver.

## Krok 5: Finální akční plán

Revidují se **2 stávající články**, **nový obsah se nenavrhuje**. Bezkanibalizační stav potvrzen — unikátní primární keyword pro každý článek.

### REVIDOVAT

**SEO nástroje + 7 rozšíření, která vám usnadní práci**
https://www.evisions.cz/blog/seo-nastroje-7-rozsireni-ktera-vam-usnadni-praci/
- Primární keyword beze změny: seo nástroje
- Rozšířit rozsah z úzkých "7 rozšíření" na komplexnější přehled (nástroje + rozšíření dohromady) — konkurence (Vceliste, Whitepress, JZShop) má 10–20+ položek
- Přidat aktuální rok do titulku/H1 — konkurence to dělá důsledně ("roku 2026")
- Integrovat sekundární keywords: "seo nástroje zdarma", "nástroj na seo", "seo nástroj", "seo nástroje online"
- Zvážit doplnění o novější AI-éra nástroje — žádný konkurent to zatím nedělá důsledně, diferenciační příležitost

**Průvodce regulárními výrazy pro začátečníky**
https://www.evisions.cz/blog-2022-01-26-pruvodce-regularnimi-vyrazy-pro-zacatecniky/
- Primární keyword beze změny: regulární výrazy (žádná lepší SEO-specifická alternativa s objemem neexistuje)
- Doplnit sekundární keywords: "regulární výraz", "regulární výrazy příklady", "co je regex"
- Nastavit realistická očekávání jako podpůrný obsah pro topic authority/interní prolinkování, ne jako primární growth driver
- Přidat interní odkaz na revidovaný SEO nástroje článek (Screaming Frog je zmíněn v obou článcích — přirozený proplet)
- Zvážit refresh publikačního data (článek z 2022, staré URL schéma) kvůli signálu aktuálnosti

### NAPSAT NOVĚ

Žádný nový článek se nenavrhuje. Všech 7 dodatečných klíčových slov z Kroku 3 patří buď jako sekundární k oběma výše uvedeným článkům, nebo byly zamítnuty (screaming frog, seo checker, regex bare) kvůli kontaminovanému/nedosažitelnému SERP.

### Shrnutí a zdůvodnění

Revize obou článků pokryje téma kompletně bez nutnosti nového obsahu. SEO nástroje článek má jasný, rychle realizovatelný upside (KD 0, jen potřeba lepší rozsah a aktuálnost). Regex článek zůstává podpůrným, topic-authority budujícím obsahem s prolinkováním na SEO nástroje článek. Žádná kanibalizace — unikátní primární keyword pro každý kus obsahu, potvrzeno plánovaně i reálně (Ahrefs organic keywords).
