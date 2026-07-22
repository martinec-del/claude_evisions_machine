# Krok 1: Konkurenční research

Zkoumáte konkurenční obsah pro článek na evisions.cz blogu, který zatím neexistuje. Cílem je pochopit, jak vypadá nejlépe umístěný obsah na dané téma, identifikovat strukturní vzory a odhalit mezery, které nový článek může vyplnit.

## ZÁKLADNÍ PRINCIP

> **POUZE RESEARCH.** V tomto kroku nepište žádný obsah článku.
> Výstupem je analýza toho, co konkurence pokrývá — ne draft, ne osnova.

---

## 0. Volba providera

1. **Primární — Ahrefs MCP.** Tento projekt má Ahrefs MCP připojené. Otestovat zavoláním `mcp__claude_ai_Ahrefs__site-explorer-domain-rating` na první kandidátské doméně.
2. **Fallback — WebSearch + WebFetch.** Pokud Ahrefs MCP selže, použít built-in nástroje (fungují vždy).

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
