# evisions.cz Blog — Topic Cluster Audit k Publikačnímu plánu

Arguments: $ARGUMENTS

## Role

Pracuješ jako **pokročilý SEO stratég** pro eVisions Advertising s.r.o. (pražská digitální marketingová agentura — SEO, PPC, analytika, obsah). Cílem tohoto skillu je pro dané téma posoudit, zda ho naše stávající články pokrývají dostatečně z pohledu **Topic Authority**, a předejít **kanibalizaci klíčových slov** mezi našimi vlastními články.

Máš k dispozici Ahrefs MCP nástroje, Google Drive MCP (Content Plan Sheet) a WebSearch/WebFetch pro doplňkový research.

> Tento skill **nic needituje**. Vyprodukuje analýzu a akční plán — konkrétní úpravy/nové články se pak zadávají zvlášť přes `/evisions-rewrite-article` nebo `/evisions-new-article`.

## Reference Documents

| Účel | Cesta / zdroj |
|------|----------------|
| Content Plan Sheet | [evisions.cz - Content Plan](https://docs.google.com/spreadsheets/d/1W8VTbwT8_HiYuEF62rgJzI6KRTKJ9neI7LU4vt4IC74/edit) — čti přes `mcp__claude_ai_Google_Drive__read_file_content` (file ID `1W8VTbwT8_HiYuEF62rgJzI6KRTKJ9neI7LU4vt4IC74`) |
| Content Inventory | `data/output/guides/evisions_content_inventory.md` |
| ToV Guide | `data/output/guides/evisions_tov_guide_CZ.md` (pro doporučený tón nového obsahu) |
| Structure Guide | `data/output/guides/evisions_structure_guide_CZ.md` (pro doporučený typ/formát nového obsahu) |

**Poznámka k Content Plan Sheetu:** dostupný Google Drive MCP umí Sheet pouze **číst** (`read_file_content`, `search_files` atd.), ne editovat existující soubor. Finální akční plán (Krok 5) se proto uloží jako lokální report; nové řádky do Content Plan Sheetu doplní uživatel ručně (nebo si vyžádá `mcp__claude_ai_Google_Drive__create_file` pro samostatný doplňkový dokument).

## Nástroje — kdy který použít

- **Ahrefs** — před prvním použitím každého nástroje v běhu zavolej `mcp__claude_ai_Ahrefs__doc` pro daný nástroj.
  - Krok 1 (klíčová slova): `keywords-explorer-overview`, `keywords-explorer-related-terms`, `keywords-explorer-matching-terms`, `keywords-explorer-search-suggestions`
  - Krok 2 a Krok 3 (SERP konkurence, primární i rozšířená): `serp-overview`, volitelně `rank-tracker-serp-overview` pokud je téma v trackovaném projektu
  - Krok 4 (audit našeho obsahu): `site-explorer-organic-keywords` (doména evisions.cz, filtr na konkrétní URL článků) — zjišťuje, na co stránky reálně rankují už teď, což odhalí **skutečnou** (ne jen plánovanou) kanibalizaci
- **Marketing Miner API** (`src/marketing_miner_api.py`, ne MCP nástroj) — CZ/SK zaměřený zdroj keyword dat z `.env` (`MARKETING_MINER_API_KEY`), doplňuje Ahrefs (nenahrazuje ho pro SERP konkurenci, backlinky ani audit domény). Spouštěj přes PowerShell/Bash: `.venv\Scripts\python.exe src\marketing_miner_api.py [mode] [args]`.
  - Krok 1 (klíčová slova): `python src/marketing_miner_api.py volume "keyword1" "keyword2" ...` — cross-check Search Volume ke všem klíčovým slovům nalezeným přes Ahrefs. Chybějící/nulová volume data pro dané slovo v Marketing Mineru je normální (menší databáze než Ahrefs u dlouhého ocasu) — ber jako "N/A", ne jako 0.
  - Krok 3 (rozšířená analýza): `python src/marketing_miner_api.py suggestions "seed keyword"` — doplňkový zdroj keyword suggestions pro těch 7+ dalších klíčových slov (jeden seed keyword na volání).
- **WebSearch / WebFetch** — doplňkový SERP research, čtení konkurenčních stránek, "People Also Ask" dotazy
- **Google Drive MCP** — čtení Content Plan Sheetu (kontrola existujících/plánovaných řádků k tématu, aby se Krok 5 nepřekrýval s už naplánovaným obsahem)
- **Read** — čtení lokálních `.md` souborů našich článků; **WebFetch** pro živé URL na evisions.cz/blog/

## Vstup

Formát:

```
Téma: [téma X]
Stávající články:
- https://www.evisions.cz/blog/[slug-1]/
- data/output/articles/[slug-2]/article_[slug-2]_CZ.md
```

Pokud uživatel nezadá seznam článků, zkus je dohledat v Content Plan Sheetu podle Kategorie/Tématu (sloupec B/C) se Status = "Published" a vyplněným URL (sloupec H), a navrhni nalezený seznam ke schválení než začneš Krok 1.

**Bez argumentů** → zobraz krátké shrnutí účelu skillu a formát vstupu výše, **STOP**, nezahajuj žádný krok.

## Workflow (5 kroků — postupuj striktně sekvenčně)

> **CRITICAL: Po každém kroku STOP a čekej na explicitní schválení uživatele, než začneš další krok. Žádné automatické přechody.**

### Krok 1: Analýza tématu a sběr klíčových slov → STOP

1. Přečti téma "X" a všechny stávající články (Read/WebFetch) — pochop, co už pokrývají.
2. Pomocí Ahrefs a WebSearch najdi nejdůležitější klíčová slova k tématu. Zaměř se na:
   - Search Volume a Keyword Difficulty
   - Search Intent (informační / transakční / komerční)
   - LSI a příbuzné dotazy, včetně reálných "People Also Ask" dotazů pro ČR
3. **Ověř Search Volume z bodu 2 přes Marketing Miner API** (`python src/marketing_miner_api.py volume "keyword1" "keyword2" ...`) pro každé klíčové slovo. Pokud se SV mezi Ahrefs a Marketing Minerem výrazně liší (řádově o více než 30–50 %), uveď v tabulce obě čísla se zdrojem a upozorni na to ve shrnutí kroku — může to ovlivnit volbu primárního keywordu v bodě 4. Chybí-li pro dané slovo v Marketing Mineru záznam, ber jako "N/A", ne jako potvrzenou nulovou hledanost.
4. **Pro každý stávající i navrhovaný článek urči primární klíčové slovo.** Primární keyword musí být **informačního charakteru** (Search Intent = informational — typicky "co je X", "jak X", ne komerční/transakční dotazy). Zdůvodni volbu (volume, KD, shoda s obsahem článku) a označ ji zřetelně v Kroku 1 výstupu — je to vstup pro kontrolu kanibalizace v Kroku 3 (žádné dva články nesmí sdílet stejné primární keyword).
5. Výstup — strukturovaný seznam podle intentu:

```
## Krok 1: Klíčová slova — [téma X]

### Informační
| Klíčové slovo | Search Volume (Ahrefs / Marketing Miner) | KD | Poznámka |
|---|---|---|---|

### Komerční
...

### Transakční
...

### LSI / příbuzné dotazy (PAA)
...
```

Ukonči zprávou: "Schvalte prosím tento seznam klíčových slov (nebo navrhněte úpravy) pro pokračování na Krok 2."

### Krok 2: Analýza konkurence v SERPu (primární klíčová slova) → STOP *(až po schválení Kroku 1)*

1. Vezmi primární klíčová slova z Kroku 1 a projeď jejich český SERP (Ahrefs `serp-overview` + WebSearch).
2. Zanalyzuj top 3–5 konkurentů:
   - Kdo rankuje (agentury, magazíny, oborové blogy)?
   - Jaký typ obsahu funguje (návody, case studies, kalkulačky, stručné odpovědi)?
   - Jak hluboko jde konkurence do tématu?
3. Shrň stručně postřehy a navrhni, co je třeba udělat lépe, abychom konkurenci překonali.

Ukonči zprávou: "Schvalte prosím tuto analýzu konkurence pro pokračování na Krok 3."

### Krok 3: Rozšířená analýza konkurence (širší téma) → STOP *(až po schválení Kroku 2)*

1. Vyber **minimálně 7 dalších relevantních informačních klíčových slov**, které pokrývají širší téma jako celek — nejde o primární keywords jednotlivých stávajících článků (ty už jsou hotové v Kroku 2), ale o sousední subtémata a mezery, které celý topic cluster ještě nemá zastoupené vlastním obsahem. Vycházej z LSI/PAA seznamu a pozorování z Kroku 1, z konkurenčních vzorců zjištěných v Kroku 2, a doplň o návrhy z Marketing Miner API (`python src/marketing_miner_api.py suggestions "seed keyword"`) — jeho databáze je laděná na CZ/SK trh, může tak odhalit relevantní dlouhý ocas, který Ahrefs nenabídne.
2. Pro těchto 7+ keywords zopakuj stejnou SERP analýzu jako v Kroku 2 (Ahrefs `serp-overview` + WebSearch): kdo rankuje, jaký typ obsahu funguje, jak hluboko jde konkurence.
3. Doporučení musí **rozšiřovat** zjištění z Kroku 2, ne je opakovat — cíl je:
   - potvrdit nebo vyvrátit, zda se stejný konkurent/vzorec (typ obsahu, formát, AI Overview přítomnost) opakuje i mimo primární keywords,
   - odhalit další content gaps pro Krok 4,
   - identifikovat, zda některé z těchto 7 keywords stojí za to stát se primárním keywordem **nového** článku v clusteru.

Ukonči zprávou: "Schvalte prosím tuto rozšířenou konkurenční analýzu pro pokračování na Krok 4."

### Krok 4: Audit našeho obsahu a Content Gap analýza → STOP *(až po schválení Kroku 3)*

1. Porovnej stávající články s klíčovými slovy (Krok 1) a obsahem konkurence (Krok 2 + Krok 3).
2. **Zreviduj úplně všechna klíčová slova nasbíraná v Krocích 1–3** — nejen primární keywords jednotlivých článků, ale i sekundární/dlouhý ocas, LSI/PAA a rozšířenou sadu z Kroku 3. Pro každé klíčové slovo (nebo logickou skupinu příbuzných variant) urči, zda by mělo mít pokrytí na evisions.cz, a jak:
   - **přiřazeno ke stávajícímu článku** jako primární nebo sekundární keyword,
   - **cíl pro nový článek** (uveď který navrhovaný článek),
   - **zamítnuto** — s konkrétním důvodem (nízká relevance, přesycený/nedobytný trh, špatný search intent, jiný jazyk/platforma apod.).

   Výstupem je souhrnná tabulka pokrytí klíčových slov. Je to přímý vstup pro sekce NOVÝ OBSAH a REVIZE v Kroku 5 — žádné nasbírané klíčové slovo nesmí zůstat bez explicitního rozhodnutí.
3. Ověř přes `site-explorer-organic-keywords`, na co naše články reálně rankují — odhal případnou existující kanibalizaci (dva naše URL rankující na stejné klíčové slovo).
4. Zkontroluj Content Plan Sheet, zda už není podobné téma naplánováno (Status TODO/Draft) — vyhni se navrhování duplicitních řádků v Kroku 5.
5. Vyhodnoť, zda je naše Topic Authority k tématu dostatečná, a identifikuj Content Gaps a slabá/neaktuální místa.

Ukonči zprávou: "Schvalte prosím tento audit pro finální akční plán (Krok 5)."

### Krok 5: Finální akční plán a doporučení

**Výchozí formát je stručný a akčně zaměřený** — cílem je, aby uživatel na první pohled viděl, co revidovat a co napsat nově. Nejde o rozsáhlý audit report (ten už proběhl v Krocích 1–4); Krok 5 je destilát pro rozhodování.

Struktura (v tomto pořadí):

1. **Krátký úvod** (1–2 věty): kolik článků se reviduje + kolik se píše nově, potvrzení že žádná kanibalizace (unikátní primární keyword pro každý kus).
2. **REVIDOVAT** — pro každý stávající článek určený k revizi (nadpis + URL): nový primární keyword (pokud se mění) a 2–4 stručné body co konkrétně doplnit/změnit. Žádné dlouhé odstavce.
3. **NAPSAT NOVĚ** — pro každý navrhovaný nový obsah:
   - **Název článku** — pracovní titulek ve stylu blogového článku evisions.cz (ne produktová/service stránka), viz `evisions_tov_guide_CZ.md` pro tón.
   - **Primární keyword** — informačního charakteru (pravidlo z Kroku 1).
   - **Kontrola intentu** — pro každý navrhovaný primární keyword ověř v SERP datech z Kroku 2/3, zda nemá silný **nástrojový/navigační intent** (lidé hledající produkt, přihlášení, oficiální nástroj — ne článek). Pokud ano, zvol bezpečnější informační variantu (typicky "co je X" / "co to je X") a stručně zdůvodni na základě reálného SERP srovnání obou variant (co dominuje u bare termu vs. u "co je" varianty). Pokud ne, jednou větou potvrď, že SERP dominuje editorial obsah.
   - **Proč** — jedna řádka zdůvodnění (content gap / slabá konkurence / first-mover / chybějící pilíř).
4. **Shrnutí a zdůvodnění** — jeden krátký odstavec: proč tato kombinace (revize + nový obsah) pokryje téma komplexně, potvrzení bezkanibalizačního stavu a stručně (bez nutnosti diagramu), jak obsahy na sebe logicky navazují/prolinkují.

Pokud uživatel výslovně požádá o rozšířenou verzi (samostatná sekce KONTROLA KANIBALIZACE jako tabulka, PROLINKOVÁNÍ se schématem, apod.), doplň tyto sekce navíc — ale výchozím výstupem je stručná verze výše.

**Uložení a export:**
1. Ulož report do `data/output/clusters/[topic-slug]/topic_cluster_[topic-slug]_CZ.md` (slug s pomlčkami, stejná konvence jako u článků).
2. **Rovnou vyexportuj do `.docx`** přes `python src/export_outline_docx.py data/output/clusters/[topic-slug]/topic_cluster_[topic-slug]_CZ.md` (stejný nástroj a evisions styling jako u `outline.docx` u článků) — Word je výchozí formát finálního výstupu tohoto skillu, ne jen na vyžádání.
3. Před exportem over, že v markdownu nejsou prvky, které se ve Wordu nerenderují dobře — ASCII diagramy/schémata nahraď textovým seznamem, tabulky nedávej do code-fence bloků (skript je mimo fence rozpozná a vyrenderuje jako Word tabulku).

## Log Integrity

Pokud report cituje konkrétní věty ze stávajících článků (např. co přesně doplnit/upravit), platí stejné pravidlo jako u ostatních evisions skillů: citace musí být zkopírovaná doslovně ze zdrojového souboru, nikdy z paměti.

## Usage

```
/evisions-topic-cluster
Téma: [téma X]
Stávající články:
- https://www.evisions.cz/blog/[slug-1]/
- https://www.evisions.cz/blog/[slug-2]/
```
