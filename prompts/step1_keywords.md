# Krok 1: Integrace klíčových slov

Optimalizujete marketingový obsah pro SEO. Vaším úkolem je přirozeně integrovat cílová klíčová slova do poskytnutého článku.

## ZÁKLADNÍ PRINCIP

> **KRITICKÉ:** Klíčová slova pouze PŘIDÁVAT do existujícího textu. NIKDY neměnit význam ani informace.
> Klíčová slova obohacují text, nenahrazují obsah.

## Pravidla

### Co se mění

| Oblast | Příklad |
|--------|---------|
| **Varianty klíčových slov** | "SEO audit" → "technický SEO audit" |
| **Přirozená synonyma** | "web" → "e-shop" (pokud je to keyword) |
| **Fráze** | Přidat keyword tam, kde to přirozeně sedí |

### Co zůstává stejné

| Oblast | Pravidlo |
|--------|----------|
| **Význam** | Význam věty nezměněn |
| **Fakta** | Žádné nové informace nepřidány |
| **Čitelnost** | Text musí plynout přirozeně |
| **Keyword stuffing** | NIKDY nenutit klíčová slova nepřirozeně |

## Priorita dle objemu (relativní)

| Priorita | Jak identifikovat | Cíl | Zaměření |
|----------|---------------------|------|-----------|
| **Top klíčová slova** | Nejvyšší objem v souboru (top 3-5) | 2-3x | Nadpisy + úvod + závěr |
| **Sekundární** | Střední objem | 1-2x | H3 + úvod/závěr |
| **Podpůrná** | Nižší objem | 0-1x | Tělo textu, kde to sedí |

## Pravidla integrace

1. **První zmínka = plná forma**
2. **Nikdy neměnit význam** — pokud substituce mění význam → SKIP
3. **Přirozený tok povinný** — pokud věta zní kostrbatě → SKIP
4. **Významné změny vyžadují potvrzení** — navrhnout jako PENDING, neaplikovat automaticky

## Rozhodovací strom

```
Zpracovat klíčová slova seřazená dle objemu (sestupně):

1. Určit relativní prioritu (top 3-5 → nadpisy, zbytek → tělo textu dle relevance)
2. Zkontrolovat sloupec Notes (specifické pokyny? následovat je)
3. Existuje relevantní text v článku? NE → SKIP/NEW. ANO → pokračovat
4. Lze keyword umístit do nadpisu? ANO+přirozené → H2/H3. NE → tělo textu
5. Jak velká změna je potřeba? DROBNÁ → DONE. VÝZNAMNÁ → PENDING
6. Sedí to přirozeně? ANO → přidat. NE → přeskočit tento výskyt
```

## INTEGRITA LOGU — BEZ VÝJIMEK

> **KRITICKÉ: Sloupec "Original" MUSÍ být zkopírován doslovně ze souboru článku — znak po znaku.**
> NIKDY nerekonstruovat z paměti. NIKDY neparafrázovat.
>
> Pokud si nejste jistí přesným zněním — přečtěte si soubor znovu před zalogováním.

## Formát výstupu

Výstupem je upravený článek s integrovanými klíčovými slovy. Po článku připojit change log:

```
---

## Step 1 Log: Keywords

**Keywords file:** `[filename].xlsx`

| # | Original | Changed To | Keyword | Volume | Position | Status |
|---|----------|------------|---------|--------|----------|--------|
| 1 | "SEO audit odhalil..." | "Technický SEO audit odhalil..." | technický seo audit | 320 | H3 | DONE |
```

**Status hodnoty:** `DONE` / `PENDING` / `SKIP` / `NEW` / `REJECTED`

## Vstup

Text článku a seznam klíčových slov následují níže. Zpracujte článek a přirozeně integrujte klíčová slova.
