# Krok 3: Struktura & formátování

Formátujete marketingový obsah pro evisions.cz blog. Aplikujte hierarchii nadpisů, E-E-A-T prvky a vizuální formátování dle Structure Guide (`data/output/guides/evisions_structure_guide_CZ.md`).

## ZÁKLADNÍ PRINCIP

> **PRAVIDLO:** Přidávat formátovací prvky TAM, KAM SE HODÍ do existujícího obsahu.
> Význam obsahu se NIKDY nemění. Zlepšuje se pouze prezentace.
> **Jediná výjimka:** Fáze -1 níže, a jen pokud byl v Kroku 1.5 schválen Mód A.

## FÁZE -1 (jen Mód A): Doplnění obsahových mezer

> **Toto je jediné místo v celém rewrite workflow, kde je povoleno přidat novou informaci** — a jen když v Kroku 1.5 (Konkurenční SERP kontrola) uživatel výslovně zvolil **Mód A**. Pokud byl zvolen Mód B, nebo Krok 1.5 nenašel žádné mezery, tuto fázi úplně přeskoč a v logu ji vůbec nezmiňuj.

Postup (proveď před vším ostatním, i před Auditem odstavců):

1. Vezmi tabulku schválených mezer z logu Kroku 1.5.
2. Pro každou mezeru napiš konkrétní nový text (odstavec, případně vlastní H3 se sekcí) a vlož ho na místo, kam tematicky patří.
3. Piš rovnou v evisions ToV (viz `evisions_tov_guide_CZ.md`) — nepiš neutrální draft, který by ještě čekal na Krok 2, protože Krok 2 (ToV) se na tento nový text už normálně nevrací jako na "originál k přepisu".
4. Zaloguj každou vloženou pasáž samostatně, se štítkem `NOVÝ OBSAH (Mód A)`:

```markdown
| # | Typ | Vložený text (celý) | Umístění | Zdroj/zdůvodnění |
|---|-----|----------------------|----------|-------------------|
| 1 | NOVÝ OBSAH (Mód A) | "..." | Nový odstavec za H2 'X', před H3 'Y' | Mezera #2 z Kroku 1.5 — konkurence (ahrefs.com/...) pokrývá X, náš článek ne |
```

## POVINNÁ PRVNÍ AKCE (po Fázi -1, pokud proběhla): Audit odstavců

Před přidáním jakýchkoli calloutů, tabulek nebo H3 — zkontrolovat každý odstavec na délku (včetně nově vloženého textu z Fáze -1). Rozdělit každý odstavec nad 100 slov.

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
| 1 | NOVÝ OBSAH (Mód A) | Nový odstavec o X vložen za H2 "Y" | Krok 1.5 mezera #2 — jen pokud byl schválen Mód A |
| 2 | H3 přidáno | "Core Web Vitals" pod "Technické SEO" | Structure: logická podsekce |
| 3 | Tabulka přidána | Srovnání metrik před/po | Formatting: srovnávací data |
```

## Vstup

Zpracujte článek níže, aplikujte správnou strukturu a formátování při zachování obsahu a tónu.
