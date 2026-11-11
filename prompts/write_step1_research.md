# Krok 1: Konkurenční research

Zkoumáte konkurenční obsah pro článek na evisions.cz blogu, který zatím neexistuje. Cílem je pochopit, jak vypadá nejlépe umístěný obsah na dané téma, identifikovat strukturní vzory a odhalit mezery, které nový článek může vyplnit.

## ZÁKLADNÍ PRINCIP

> **POUZE RESEARCH.** V tomto kroku nepište žádný obsah článku.
> Výstupem je analýza toho, co konkurence pokrývá — ne draft, ne osnova.

---

## 0. Volba providera

1. **Primární — Ahrefs MCP.** Tento projekt má Ahrefs MCP připojené. Otestovat zavoláním `mcp__claude_ai_Ahrefs__site-explorer-domain-rating` na první kandidátské doméně.
2. **Fallback — WebSearch + WebFetch.** Pokud Ahrefs MCP selže, použít built-in nástroje (fungují vždy).
3. **Doplňkový — Marketing Miner (CZ/SK cross-check).** `src/marketing_miner_api.py` — viz krok 5.5 níže. Nepoužívat jako náhradu Ahrefs, jen jako CZ-laděný cross-check a doplňkový zdroj nápadů.

---

## Research proces

### 1. Objevit stránky

Spustit 4 WebSearch dotazy:
- `"[téma] vysvětleno"` — obecný
- `"[téma] návod"` — edukativní úhel
- `"jak na [téma]"` — praktický úhel
- téma-specifický úhel

4 dotazy × 6 URL = až 24 kandidátních URL. Deduplikovat + filtrovat (vynechat fóra, placený obsah).

**Prioritní zdroje** (fetchovat první, pokud jsou relevantní): Ahrefs Blog, Search Engine Journal, Search Engine Land, MOZ, české marketingové blogy (Marketing Miner, SEOnity, Webnode blog).

### 2. Obohatit metrikami

Pro všechny URL zavolat Ahrefs:
- `site-explorer-metrics` → organický traffic URL
- `site-explorer-domain-rating` → Domain Rating domény

### 3. Vybrat top 10 a extrahovat

Fetch top 10 URL (relevance > DR > traffic). Extrahovat: H1, H2/H3 strukturu, pokrytá/chybějící témata, hloubku, formáty (tabulky, srovnání), unikátní úhel, odhad počtu slov.

**Timeout:** 30s na WebFetch, jinak přeskočit.

### 4. Objevování klíčových slov

```
mcp__claude_ai_Ahrefs__keywords-explorer-matching-terms
mcp__claude_ai_Ahrefs__keywords-explorer-related-terms
```

Seed = hlavní keyword + 2-3 doplňkové seedy z H2 nadpisů konkurence.

### 5. Merge + dedup + filtr + clustering

Sloučit klíčová slova + témata z H2/H3. Odstranit duplicity a mimo-oborová slova. Seřadit dle objemu. Max 30 klíčových slov, intent clustering.

### 5.5. Marketing Miner cross-check (CZ)

**Účel:** Ahrefs má globální data, která mohou být pro úzce české fráze nepřesná nebo neúplná. Marketing Miner je CZ/SK-laděný a slouží jako druhé mínění, ne jako náhrada.

1. **Volume cross-check** — pro top 5–8 finálních keywordů (nejvyšší volume + hlavní/primární cluster) spustit:
   ```
   python src/marketing_miner_api.py volume "keyword1" "keyword2" ... --lang cs
   ```
   Pokud se čísla výrazně liší od Ahrefs (řádový rozdíl, ne jen ±20 %), zapsat obě hodnoty do sloupce "Notes" v listu "Keywords" (`MM cross-check: [N]/mo`) a v Kroku 2 dát přednost konzervativnějšímu odhadu.
2. **Doplňkové nápady** — pokud hlavní seed keyword nemá dost pokrytí z Ahrefs matching-terms/related-terms (typicky u úzce lokálních/CZ témat), spustit:
   ```
   python src/marketing_miner_api.py suggestions "seed keyword" --lang cs
   ```
   Přidat jen nové CZ-relevantní nápady, které Ahrefs nenašel — anglické/mezinárodní long-tail varianty s minimálním objemem (10/měsíc a nižší, časté u tohoto endpointu) ignorovat, pokud nejsou tematicky unikátní.
3. **Windows encoding:** volat s `PYTHONUTF8=1 PYTHONIOENCODING=utf-8` v prostředí, jinak se diakritika v argumentech/výstupu poškodí (potvrzeno testem — bez toho nemusí API najít shodu pro keywordy s diakritikou).
4. **Pokud `MARKETING_MINER_API_KEY` není v `.env` nastaven** nebo API selže, tento krok přeskočit bez blokování Kroku 1 — je doplňkový, ne povinný.

### 6. Generovat xlsx

`data/output/articles/[slug]/[slug]_step1.xlsx`:

**List "URLs":** `# | URL | Zdroj | DR | Organic Traffic | Stav fetch | H1 | Klíčová témata | Content gap | Počet slov`

**List "Keywords":** `# | Keyword | Volume | KD | Cluster | Status | Notes`

---

## Stop podmínka

> **Krok 1 dokončen.** [N] URL nasbíráno, [N] fetchnuto. [N] klíčových slov navrženo.
> Klíčový content gap: [věta].
> **xlsx uložen:** `[plná absolutní cesta]`
> Zkontrolujte → potvrďte pro Krok 2.
