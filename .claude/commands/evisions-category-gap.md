# evisions.cz Blog — Category Topic Gap Analysis

Arguments: $ARGUMENTS

## Role

Pracuješ jako **oborový expert a SEO stratég** pro eVisions Advertising s.r.o. Cílem tohoto skillu je pro danou **kategorii** Content Planu (SEO / PPC / Social / AI & SEO / Copywriting / Konference / Marketing / evisions interní / International / Kariéra) posoudit, zda naplánovaná a existující témata dostatečně pokrývají **Topic Authority** kategorie jako celku, a navrhnout chybějící témata článků cílící na reálně hledaná klíčová slova.

Máš k dispozici Ahrefs MCP nástroje, Marketing Miner API, Google Drive MCP (Content Plan Sheet) a WebSearch/WebFetch pro doplňkový research.

> Tento skill **nic needituje** a **neřeší SERP konkurenci**. Vyprodukuje seznam chybějících témat + ověřená klíčová slova pro každé. Konkrétní nové články se pak zadávají zvlášť přes `/evisions-new-article`. Pokud potřebuješ i konkurenční SERP analýzu a kontrolu kanibalizace pro jedno konkrétní téma/cluster, použij `/evisions-topic-cluster`.

## Rozdíl oproti `/evisions-topic-cluster`

| | `/evisions-category-gap` | `/evisions-topic-cluster` |
|---|---|---|
| Rozsah | Celá kategorie (více podtémat) | Jedno konkrétní téma/cluster |
| Vstup | Kategorie + seznam témat (Content Plan) | Téma + konkrétní stávající články |
| SERP konkurence | Neřeší | Ano (Krok 2 + 3) |
| Kanibalizace | Neřeší explicitně | Ano (primární keyword check) |
| Výstup | Chybějící témata + ověřené kws | Revize + nový obsah + prolinkování |
| Rychlost | Rychlejší, lehčí | Hlubší, náročnější |

Použij tento skill jako **první, rychlý průchod** přes kategorii, než se pustíš do hloubkové analýzy jednotlivých témat přes `/evisions-topic-cluster`.

## Reference Documents

| Účel | Cesta / zdroj |
|------|----------------|
| Content Plan Sheet (primární) | [Content Plan Index Sheet](https://docs.google.com/spreadsheets/d/1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q/edit?gid=754600260#gid=754600260) — čti přes `mcp__claude_ai_Google_Drive__read_file_content` (file ID `1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q`); sekundární sheet jen na vyžádání, viz `evisions_content_inventory.md` |
| Content Inventory | `data/output/guides/evisions_content_inventory.md` |
| ToV Guide | `data/output/guides/evisions_tov_guide_CZ.md` (pro pracovní název nových témat) |

## Nástroje — kdy který použít

- **Google Drive MCP** — čtení Content Plan Sheetu, pokud uživatel nedodá seznam témat ručně; jen čtení, ne editace.
- **Ahrefs** — před prvním použitím každého nástroje v běhu zavolej `mcp__claude_ai_Ahrefs__doc`.
  - Krok 3 (ověření): `keywords-explorer-overview` (volume, KD, intent pro navržené kws)
  - Krok 3 (rozšíření): `keywords-explorer-related-terms`, `keywords-explorer-search-suggestions` (další hledaná kws k chybějícím podtématům)
- **Marketing Miner API** (`src/marketing_miner_api.py`, ne MCP nástroj) — CZ/SK zaměřený zdroj, doplňuje Ahrefs. Spouštěj přes PowerShell/Bash: `.venv\Scripts\python.exe src\marketing_miner_api.py [mode] [args]`.
  - `python src/marketing_miner_api.py volume "keyword1" "keyword2" ...` — cross-check Search Volume ke všem navrženým kws
  - `python src/marketing_miner_api.py suggestions "seed keyword"` — doplňkové návrhy dalších hledaných kws k chybějícímu podtématu (jeden seed keyword na volání)
  - Chybějící/nulová volume data pro dané slovo v Marketing Mineru je normální (menší databáze než Ahrefs u dlouhého ocasu) — ber jako "N/A", ne jako 0.
- **WebSearch** — doplňkový research k oborové expertíze v Kroku 1, pokud si nejsi jistý, jaká podtémata se v dané kategorii běžně řeší.

## Vstup

Formát:

```
Kategorie: [SEO | PPC | AI & SEO | Analytika | E-commerce | Případovky]
Témata v content plánu:
- [téma 1]
- [téma 2]
- [téma 3]
```

Pokud uživatel nedodá seznam témat, dohledej je v Content Plan Sheetu podle sloupce B (Kategorie) — vezmi **všechny** řádky bez ohledu na Status (TODO/Draft/Review/Published), protože i naplánovaná témata se počítají do budoucího pokrytí. Zobraz nalezený seznam ke schválení, než začneš Krok 1.

**Bez argumentů** → zobraz krátké shrnutí účelu skillu a formát vstupu výše, **STOP**, nezahajuj žádný krok.

## Workflow (3 kroky — postupuj striktně sekvenčně)

> **CRITICAL: Po Kroku 2 STOP a čekej na explicitní schválení uživatele, než začneš Krok 3. Krok 1 a 2 lze provést v jednom průchodu, protože Krok 2 je přímým výstupem Kroku 1.**

### Krok 1 + 2: Gap analýza a návrh prioritních kws → STOP

1. Přečti zadaná (nebo dohledaná) témata pro danou kategorii a pochop, co kategorie na blogu už pokrývá.
2. Jako oborový expert na danou kategorii zhodnoť, jaká důležitá pod-témata, úhly pohledu nebo typy dotazů čtenáři/klienti v této oblasti běžně řeší, a **nejsou** v seznamu zatím zastoupené. Mysli v kontextu blogových článků evisions.cz (ne produktových/service stránek).
3. Sestav seznam chybějících pod-témat (návrhy nových článků), která by kategorii doplnila na komplexnější Topic Authority.
4. Pro každé chybějící pod-téma navrhni (na základě expertízy, **zatím bez ověření v datech**) 1–3 klíčová slova, o kterých usuzuješ, že by mohla být pro dané pod-téma prioritní/hledaná. Preferuj informační search intent (viz `/evisions-topic-cluster` pravidlo — primární keyword by měl být informačního charakteru).

Výstup:

```
## Krok 1+2: Chybějící témata a navržené kws — kategorie [X]

| Chybějící pod-téma | Navržená prioritní kws (odhad) | Proč chybí / proč relevantní |
|---|---|---|
```

Ukonči zprávou: "Schvalte prosím tento seznam chybějících témat a navržených kws, než ověřím hledanost v Ahrefs a Marketing Mineru."

### Krok 3: Ověření a rozšíření kws *(až po schválení Kroku 2)*

1. Ověř každé schválené keyword v Ahrefs (`keywords-explorer-overview`) — Search Volume, Keyword Difficulty, Search Intent.
2. Zkřížově ověř Search Volume v Marketing Mineru (`python src/marketing_miner_api.py volume "kw1" "kw2" ...`). Pokud se SV mezi Ahrefs a Marketing Minerem výrazně liší (řádově o více než 30–50 %), uveď obě čísla se zdrojem.
3. Pro každé chybějící pod-téma zkus navíc dohledat další související hledaná kws (Ahrefs `related-terms`/`search-suggestions` + Marketing Miner `suggestions`), která by mohla být vhodnější jako primární keyword než původní odhad z Kroku 2.
4. Vylouč nebo jasně označ kws s nulovou/zanedbatelnou hledaností, nebo se silným komerčním/navigačním/nástrojovým intentem tam, kde má jít o informační obsah.
5. Zkontroluj Content Plan Sheet, zda podobné téma už není naplánováno pod jiným ID/kategorií — vyhni se duplicitám.

Finální výstup:

```
## Krok 3: Ověřená chybějící témata — kategorie [X]

| Pod-téma (návrh článku) | Finální primární keyword | Search Volume (Ahrefs / MM) | KD | Search Intent | Zdůvodnění |
|---|---|---|---|---|---|
```

Doplň krátké shrnutí (1–2 věty): kolik nových témat celkem navrhuješ, a proč toto doplnění zlepšuje Topic Authority kategorie [X].

**Uložení a export:**
1. Ulož report do `data/output/category-gaps/[kategorie-slug]/category_gap_[kategorie-slug]_CZ.md` (slug s pomlčkami, stejná konvence jako u článků a clusterů).
2. Rovnou vyexportuj do `.docx` přes `python src/export_outline_docx.py data/output/category-gaps/[kategorie-slug]/category_gap_[kategorie-slug]_CZ.md`.
3. Před exportem ověř, že v markdownu nejsou prvky, které se ve Wordu nerenderují dobře (ASCII schémata → textový seznam, tabulky mimo code-fence).

## Usage

```
/evisions-category-gap
Kategorie: SEO
Témata v content plánu:
- Z nuly na SEO hvězdu: Kalkulátor.cz
- breAd. case study — B2B SEO
```

nebo bez seznamu témat (dohledá se automaticky z Content Plan Sheetu):

```
/evisions-category-gap
Kategorie: PPC
```
