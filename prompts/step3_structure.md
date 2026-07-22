# Krok 3: Struktura & formátování

Formátujete marketingový obsah pro evisions.cz blog. Aplikujte hierarchii nadpisů, E-E-A-T prvky a vizuální formátování dle Structure Guide (`data/output/guides/evisions_structure_guide_CZ.md`).

## ZÁKLADNÍ PRINCIP

> **PRAVIDLO:** Přidávat formátovací prvky TAM, KAM SE HODÍ do existujícího obsahu.
> Význam obsahu se NIKDY nemění. Zlepšuje se pouze prezentace.

## POVINNÁ PRVNÍ AKCE: Audit odstavců

Před přidáním jakýchkoli calloutů, tabulek nebo H3 — zkontrolovat každý odstavec na délku. Rozdělit každý odstavec nad 100 slov.

## Hierarchie nadpisů

| Úroveň | Použití | Frekvence |
|--------|---------|-----------|
| **H1** | Pouze název článku | 1 na stránku |
| **H2** | Hlavní sekce | 3-7 na článek |
| **H3** | Podsekce v rámci H2 | Dle potřeby |

**Pravidla:** Nikdy nepřeskakovat úrovně.

## Callout typy

| Typ | Použití | Frekvence |
|-----|---------|-----------|
| **Tip** | Praktická rada, pro-tip | 2-3 na článek |
| **Warning** | Upozornění na riziko/chybu | 1-2 na článek |
| **Note** | Doplňující kontext | Dle potřeby |
| **Important** | Kritická informace | Střídmě |
| **Example** | Praktická ilustrace | Dle potřeby |
| **Keep in Mind** | Limity metody/nástroje | 1 na how-to článek |

**Markdown formát:**
```markdown
> **Tip:** [Praktická rada]

> **Warning:** [Riziko nebo chyba]

> **Keep in Mind:** [Limit metody nebo nástroje]
```

**Pravidlo:** 1-2 callouty na H2 sekci max. Žádné callouty za sebou.

## Limity dle délky článku

| Délka článku | Callouty | Tabulky | Seznamy |
|---------------|----------|---------|---------|
| Krátký (<1000 slov) | 1-2 | 1 | 1-2 |
| Střední (1000-2000 slov) | 2-3 | 1-2 | 2-3 |
| Dlouhý (>2000 slov) | 3-4 | 2-3 | 3-4 |

## Struktura dle typu obsahu

Viz Structure Guide sekce 5:

**How-to/edukativní:** Hook → Hlavní koncept → Praktická aplikace → Časté chyby/limity → Klíčové závěry → Zdroje

**Case study:** Hook (silné číslo) → Výchozí stav → Strategie/metodologie → Výsledky → Co se osvědčilo/neosvědčilo → CTA

## Povinné E-E-A-T prvky

### Autorská atribuce (konec)
```markdown
---
**Autor:** [Jméno]
**Role:** [Role ve firmě]
**Aktualizováno:** [Datum]
---
```

### Poznámka k obsahu (po obsahu — vkládá se CMS/šablonou, neduplicit ručně)

Standardní blok vkládá `src/step4_html.py` automaticky — neduplikovat ručně v markdownu.

## Navigační prvky

| Prvek | Kdy povinné |
|-------|--------------|
| **Obsah (ToC)** | Pokud >1500 slov |
| **Interní odkazy** | 3-5 na článek minimum |
| **Zdroje** | Vždy u how-to obsahu |

## Co se mění / co zůstává

| Co se mění | Co zůstává |
|-------------|-------------|
| Nadpisy, callouty, tabulky, seznamy | Fakta |
| Rozdělení dlouhých odstavců | Význam |
| Interní odkazy | Klíčová slova z Kroku 1 |
| Tučné zvýraznění klíčových termínů | Tón z Kroku 2 |

## INTEGRITA LOGU

> Pro řádky odkazující na konkrétní text (např. rozdělený odstavec) kopírovat doslovně ze souboru po Kroku 2.

## Formát výstupu

> **KRITICKÉ:** Výstup jako plain markdown text, bez code fence. Článek začíná přímo `#` nadpisem.

```
---

## Step 3 Log: Structure & Formatting

**Délka článku:** [KRÁTKÝ/STŘEDNÍ/DLOUHÝ] ([X] slov)

| # | Change Type | Description | Reason |
|---|-------------|-------------|--------|
| 1 | H3 přidáno | "Core Web Vitals" pod "Technické SEO" | Structure: logická podsekce |
| 2 | Tabulka přidána | Srovnání metrik před/po | Formatting: srovnávací data |
```

## Vstup

Zpracujte článek níže, aplikujte správnou strukturu a formátování při zachování obsahu a tónu.
