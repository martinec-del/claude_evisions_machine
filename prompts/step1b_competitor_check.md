# Krok 1.5: Konkurenční SERP kontrola

Ověřujete, jestli je upravovaný článek obsahově konkurenceschopný pro svá primární klíčová slova — tedy jestli pokrývá to, co dnes reálně rankuje na Google.

## ZÁKLADNÍ PRINCIP

> Tento krok je REPORT + ROZHODNUTÍ, ne automatická úprava obsahu.
> Cílem je zjistit obsahové mezery vůči top rankující konkurenci a nechat uživatele zvolit, jak s nimi naložit (Mód A/B, viz níže).
> Toto je jediné místo v rewrite workflow, kde je za výslovně schválených podmínek (Mód A) povolena výjimka z pravidla "žádné nové informace" — a i tak jen po explicitním schválení uživatele u STOPu v Kroku 3.

## Proces

### 1. Vyber primární klíčová slova

Z `[slug]_keywords.xlsx` (list "Keywords") vyber **2-3 primární klíčová slova** — nejvyšší Volume / Priority HIGH z Kroku 1. Přeskoč klíčová slova se statusem SKIP.

### 2. SERP research (lehká verze)

Pro každé z 2-3 klíčových slov:

1. `mcp__claude_ai_Ahrefs__doc` (tool: `serp-overview`) — pokud se v tomto běhu ještě nevolalo.
2. `mcp__claude_ai_Ahrefs__serp-overview` (country: `cz`, keyword) → získej top výsledky.
3. Z výsledků vyber **top 3-4 organické** — přeskoč: placené výsledky, vlastní evisions.cz URL (ten porovnáváme, ne konkurenci), nerelevantní výsledky (nákupní srovnávače, fóra, sociální sítě).
4. `WebFetch` každou vybranou URL — z promptu si vyžádej: H1, H2/H3 strukturu, přibližný počet slov, klíčová témata/sekce, unikátní prvky (tabulky, kalkulačky, konkrétní data/čísla, které náš článek nemá).

**Dedup:** pokud se stejná URL objeví u více klíčových slov, fetchni ji jen jednou a přiřaď ji ke všem relevantním keywords.

**Timeout:** 20s na WebFetch, jinak přeskočit a poznamenat do reportu ("URL X nedostupná/timeout — vynechána").

### 3. Porovnání s naším článkem

Porovnej strukturu a hloubku aktuálního článku (stav po Kroku 1) s tím, co jsi zjistil u konkurence:

- **Chybějící témata/sekce** — co konkurence pokrývá a náš článek ne
- **Hloubka** — je náš článek u klíčového tématu podstatně kratší/mělčí než konkurence?
- **Obsahové prvky** — konkrétní data, čísla, srovnání, které konkurence uvádí a my ne

**Nezaznamenávej** čistě formátovací rozdíly (tabulky, callouty, seznamy) — to řeší obecně Krok 3 bez ohledu na konkurenci. Zaměř se výhradně na **obsahové** mezery (chybějící témata/informace).

### 4. Výstup — stručný report

```
## Krok 1.5: Konkurenční SERP kontrola

**Primární klíčová slova prověřena:** [kw1], [kw2], [kw3]
**Konkurenti analyzováni:** [N] URL ([doména1], [doména2], ...)
**Nedostupné/přeskočené:** [pokud nějaké, jinak vynechat řádek]

### Zjištěné obsahové mezery

| # | Mezera | Zjištěno u (doména/URL) | Návrh doplnění |
|---|--------|--------------------------|-----------------|
| 1 | ... | ... | ... |

**Shrnutí:** [1-2 věty — je náš článek obsahově konkurenceschopný, nebo má mezery?]
```

Pokud nebyla nalezena žádná významná mezera → napiš krátké shrnutí ("Obsahově srovnatelné s top konkurencí, žádné zásadní mezery.") a **pokračuj rovnou do Kroku 2 bez dotazu na mód** (mód je irelevantní, když není co doplňovat).

### 5. STOP — volba módu (pouze pokud byly nalezeny mezery)

```
Zjištěno [N] obsahových mezer vůči konkurenci (viz tabulka výše). Jak pokračovat?

A) Konkurenceschopná revize — navrhnu a rovnou dopíšu nové sekce/odstavce k uzavření mezer.
   Schválíte je při STOPu v Kroku 3 (Struktura), kde se reálně vloží do článku.
B) Beze změny pravidla — mezery zůstanou zaznamenané v logu jako doporučení pro budoucnost,
   obsah se nedoplňuje (dodržíme "žádné nové informace" beze zbytku).
```

**Nikdy nepokračuj do Kroku 2 bez explicitní volby uživatele, pokud byly mezery nalezeny.**

## Co dělat s výsledkem podle zvoleného módu

- **Mód B nebo žádné mezery:** pokračuj do Kroku 2 (ToV) jako obvykle. Zjištěné mezery (pokud nějaké) zůstávají jen v logu tohoto kroku — nikam jinam se nepropisují.
- **Mód A:** Krok 2 a Krok 3 proběhnou jako obvykle, ale **Krok 3 (Struktura) na svém úplném začátku** — před Fází 0 (Audit odstavců) — nejdřív navrhne a vloží konkrétní nový text uzavírající schválené mezery (viz `prompts/step3_structure.md`, sekce "Fáze -1"). Tento krok si vezme tabulku mezer z tohoto reportu jako vstup.

## Log formát

```
## Step 1.5 Log: Konkurenční SERP kontrola

**Klíčová slova prověřena:** kw1, kw2, kw3
**Konkurenti (URL):** ...
**Mezery nalezeny:** [N]
**Zvolený mód:** A (konkurenceschopná revize) | B (beze změny pravidla) | N/A (žádné mezery)

| # | Mezera | Zdroj | Návrh | Status |
|---|--------|-------|-------|--------|
| 1 | ... | ... | ... | SCHVÁLENO PRO MÓD A / ZAZNAMENÁNO (mód B) |
```

## Vstup

Zpracuj primární klíčová slova z keywords souboru a aktuální stav článku (po Kroku 1) níže.
