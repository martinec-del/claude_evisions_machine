# evisions.cz Blog: Content Structure & E-E-A-T Guide

**Verze:** 1.0 DRAFT
**Vytvořeno:** 2026-07-10
**Účel:** Strukturní standardy pro veškerý obsah na evisions.cz blogu — maximalizace E-E-A-T signálů, čitelnosti a výkonu ve vyhledávání

---

## 1. Souhrn

### Co tento dokument je

Komplexní průvodce **strukturou** obsahu na evisions.cz blogu — formát, hierarchie, šablona článku a technické požadavky.

> **Rozsah:** Struktura, formátování, šablony, E-E-A-T signály, technické SEO.
> **Pro hlas a tón viz:** [Tone of Voice Guide](evisions_tov_guide_CZ.md)

### Vztah k ToV Guide

| Dokument | Zaměření | Klíčová otázka |
|----------|----------|-----------------|
| ToV Guide | Hlas, jazyk, emoční kalibrace | "Jak máme znít?" |
| Structure Guide | Formát, hierarchie, šablony, technické požadavky | "Jak má být obsah organizovaný?" |

### Proč na struktuře záleží

1. **E-E-A-T signály** — Google hodnotí odbornost přes strukturní prvky
2. **UX** — většina čtenářů obsah spíš skenuje, než čte lineárně
3. **Přístupnost** — správná struktura umožňuje čtečkám obrazovky a asistivním technologiím fungovat
4. **Konverze** — jasná struktura snižuje kognitivní zátěž a zvyšuje dočtenost

---

## 2. E-E-A-T Framework

E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) je Google framework pro hodnocení kvality. Marketingové case studies a how-to obsah s konkrétními čísly a doporučeními jsou citlivé na tato kritéria podobně jako finanční (YMYL) obsah — čtenář se rozhoduje, kam investovat marketingový rozpočet.

### Experience

| Strukturní prvek | Implementace |
|-------------------|----------------|
| **Konkrétní příklady s čísly** | "U klienta s rozpočtem 200 000 Kč/měsíc jsme dosáhli…" |
| **Dokumentace procesu** | Krokové workflow se skutečnými čísly a časovým rámcem |
| **Sekce běžných chyb** | Ukázka znalosti reálných problémů klientů |
| **Scénáře z praxe** | "Pokud vaše CTR klesne pod X %…" |

### Expertise

| Strukturní prvek | Implementace |
|-------------------|----------------|
| **Autor s rolí** | Jméno, role (SEO Specialist, Head of PPC), odkaz na LinkedIn |
| **Citace zdrojů** | Odkaz na autoritativní zdroje (Google, Meta, nezávislé studie) |
| **Technická hloubka** | Metodologie, nástroje jmenovitě (Ahrefs, GSC, Marketing Miner) |
| **Odborný slovník** | Správná terminologie (vysvětlená při prvním použití) |

**Formát autorské atribuce:**

```markdown
---
**Autor:** [Jméno]
**Role:** [Role ve firmě]
**Specializace:** [Oblast]
**Aktualizováno:** [Datum]
---
```

### Authoritativeness

| Strukturní prvek | Implementace |
|-------------------|----------------|
| **Institucionální zázemí** | Konzistentní branding "evisions" |
| **Data ve velkém měřítku** | "Na základě analýzy X kampaní/klientů…" |
| **Externí reference** | Odkazy na uznávané zdroje |
| **Verzování** | Datum poslední aktualizace |

### Trustworthiness

| Strukturní prvek | Implementace |
|-------------------|----------------|
| **Transparentnost zdrojů** | Odkud tvrzení pochází |
| **Datum aktualizace** | Kdy byl obsah naposledy ověřen |
| **Vyvážený pohled** | Přiznání limitů metody/nástroje |
| **Kontakt** | Jak se dostat k dalším informacím |

---

## 3. Citlivá tvrzení — marketingový ekvivalent YMYL

### Co dělá marketingový obsah citlivým

Case studies a how-to obsah s konkrétními výsledky ovlivňují byznysová rozhodnutí čtenáře (kam investovat rozpočet). Platí obdobná opatrnost jako u finančního obsahu.

### Poznámka k obsahu (místo risk disclaimeru)

Standardní blok vkládaný na konec článku CMS/šablonou (viz `step4_html.py`):

```markdown
> **Poznámka k obsahu:** Tento článek má edukativní charakter.
> Konkrétní doporučení pro váš projekt vám rádi připravíme na míru.
```

### Případ-specifický disclaimer (case studies)

```markdown
> **Důležité:** Výsledky uvedené v této case study se vztahují ke
> konkrétnímu klientovi a jeho specifickým podmínkám (odvětví, rozpočet,
> výchozí stav). Nejde o garanci obdobných výsledků pro jiný projekt.
```

### Požadavky na faktickou přesnost

- **Všechny statistiky** musí mít zdroj a datum
- **Čísla z case studies** musí být ověřitelná (interní reporting, nástroj)
- **Žádné garance konkrétních výsledků** budoucím klientům (viz ToV Guide sekce 7)

---

## 4. Prvky struktury obsahu

### Hierarchie nadpisů

| Úroveň | Použití | Příklad |
|--------|---------|---------|
| **H1** | Pouze název článku (1 na stránku) | "SEO pro e-commerce: kompletní průvodce" |
| **H2** | Hlavní sekce | "Proč na technickém SEO záleží" |
| **H3** | Podsekce v rámci H2 | "Core Web Vitals a jejich dopad" |
| **H4** | Drobné dělení (používat střídmě) | "Jak měřit LCP" |

**Principy:**
- Nikdy nepřeskakovat úrovně (H2 rovnou na H4)
- H2 vytváří skenovatelnou osnovu
- 3-7 H2 sekcí na článek (optimum)

### Pravidla odstavců

| Zásada | Specifikace |
|--------|-------------|
| **Délka** | 2-4 věty (40-100 slov) |
| **Jedna myšlenka na odstavec** | Fokus na jeden koncept |
| **První věta** | Obsahuje hlavní bod (obrácená pyramida) |

**Maximum po sobě jdoucích odstavců bez vizuálního zlomu:** 3

### Seznamy: odrážky vs. číslované

**ODRÁŽKY pro:**
- Neseřazené položky (na pořadí nezáleží)
- Vlastnosti, charakteristiky, příklady
- Shrnutí a klíčové body

**ČÍSLOVANÉ SEZNAMY pro:**
- Postupné kroky (musí následovat v pořadí)
- Procesy s jasnými fázemi
- Instrukce vyžadující konkrétní pořadí

**Formátování:** 3-7 položek optimum, paralelní gramatická struktura.

### Tabulky

**Kdy použít:** srovnání 2+ položek napříč atributy, referenční data, before/after srovnání.

| Požadavek | Specifikace |
|-----------|-------------|
| Hlavičkový řádek | Vždy, tučně |
| Zarovnání | Text vlevo, čísla vpravo |
| Max. sloupců | 5 (širší tabulky se lámou na mobilu) |

### Callout boxy

evisions blog šablona (`step4_html.py`) podporuje tyto typy:

| Typ | Použití |
|-----|---------|
| **Tip** | Praktická rada, pro-tip |
| **Warning** | Upozornění na riziko/chybu |
| **Important** | Kritická informace |
| **Note** | Doplňující kontext |
| **Keep in Mind** | Limity metody, poctivé caveaty |
| **Example** | Praktická ilustrace |

**Markdown formát:**

```markdown
> **Tip:** [Praktická rada]

> **Warning:** [Riziko nebo chyba]

> **Important:** [Kritická informace]

> **Note:** [Doplňující kontext]

> **Keep in Mind:** [Limit metody nebo nástroje]

> **Example:** [Praktická ilustrace]
```

**Frekvence:** 1-2 callouty na hlavní sekci (H2), vyhnout se calloutům za sebou.

### Obrázky

Šablona zabaluje obrázky do `<figure class="article-image">` s `figcaption` z alt textu. Vždy vyplnit smysluplný alt text (accessibility + SEO).

---

## 5. Šablona a vzory článku

### Struktura how-to / edukativního článku

1. **HOOK** (1-2 věty) — proč na tom záleží, co se čtenář dozví (TL;DR u delších textů)
2. **HLAVNÍ KONCEPT** — definice/vysvětlení, příklad
3. **PRAKTICKÁ APLIKACE** — jak to použít, konkrétní příklady s čísly
4. **ČASTÉ CHYBY / LIMITY** — na co si dát pozor
5. **KLÍČOVÉ ZÁVĚRY** — 3-5 odrážek, actionable shrnutí
6. **ZDROJE** — sekce s odkazy na citované externí zdroje

### Struktura case study

1. **HOOK** — silné číslo/výsledek hned v úvodu
2. **VÝCHOZÍ STAV** — kde klient začínal, jaký byl problém
3. **STRATEGIE / METODOLOGIE** — co jsme udělali a proč
4. **VÝSLEDKY** — čísla v čase, tabulka/graf
5. **CO SE OSVĚDČILO / NEOSVĚDČILO** — poctivé shrnutí
6. **CTA** — odkaz na kontakt nebo podobnou case study

### Textové formátování

| Prvek | Použití |
|-------|---------|
| **Tučně** | Klíčové termíny, důležité body |
| *Kurzíva* | Zdůraznění, první výskyt nového termínu |
| > Citace | Klíčové principy, citace expertů |
| Odrážky | Seznamy, shrnutí |
| Číslované seznamy | Postupné kroky |

### Čísla a data

- Konkrétní čísla: "nárůst o 90 % za rok" ne "výrazný nárůst"
- Vždy s kontextem: "14 585 návštěv/měsíc (zdroj: Ahrefs, září 2025)"
- Měna: CZK jako výchozí, specifikovat pokud jiná

---

## 6. Čitelnost a UX

### Skenovatelnost

**F-pattern optimalizace:** hlavní sdělení na začátku odstavce, klíčové termíny na začátku odrážek, tučně pro skenovací kotvy.

**Obrácená pyramida:** začít závěrem/hlavním bodem, pak podpůrné detaily.

**Příklad:**

```markdown
DOBŘE (obrácená pyramida):
Organická návštěvnost vzrostla o 700 % za 30 měsíců. Klíčem byla
přepracovaná obsahová strategie postavená na analýze klíčových slov.

ŠPATNĚ (skrytý závěr):
Když se podíváme na to, jak probíhala spolupráce a jaké kroky byly
postupně podniknuty v rámci obsahové strategie, dostaneme se nakonec
k tomu, že návštěvnost nakonec vzrostla o 700 %.
```

### Typografie (dle `step4_html.py` šablony)

**Font:** Poppins (Google Fonts)

| Prvek | Velikost | Váha |
|-------|----------|------|
| H1 | 2.25rem (36px) | 700 |
| H2 | 1.5rem (24px) | 600 |
| H3 | 1.25rem (20px) | 600 |
| Tělo textu | 1rem (16px) | 400 |

| Specifikace | Hodnota |
|--------------|---------|
| Max. šířka obsahu | 1160px |
| Délka věty | 10-18 slov průměr |
| Délka odstavce | 40-100 slov |
| ALL CAPS | Vyhnout se (kromě zkratek) |

### Navigační prvky

**Obsah (ToC):** povinné pro články nad 1500 slov, odkazy na H2 sekce, umístěno po úvodu.

```markdown
## Obsah
- [Proč na technickém SEO záleží](#proc-na-technickem-seo-zalezi)
- [Core Web Vitals a jejich dopad](#core-web-vitals-a-jejich-dopad)
- [Klíčové závěry](#klicove-zavery)
```

---

## 7. Prohledávatelnost a technické SEO

### Sémantické HTML

| Prvek | HTML tag |
|-------|----------|
| Titulek článku | `<h1>` (jeden na stránku) |
| Sekce | `<h2>`, `<h3>`, `<h4>` |
| Odstavce | `<p>` |
| Seznamy | `<ul>`, `<ol>`, `<li>` |
| Tabulky | `<table>`, `<thead>`, `<tbody>` |
| Citace | `<blockquote>` |

### Structured Data (Schema.org)

**BlogPosting schema:**

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "SEO pro e-commerce: kompletní průvodce",
  "author": {
    "@type": "Person",
    "name": "Jméno autora"
  },
  "publisher": {
    "@type": "Organization",
    "name": "evisions Advertising"
  },
  "datePublished": "2026-07-10"
}
```

**FAQPage schema** (pokud článek obsahuje FAQ sekci) a **HowTo schema** (pro krokové návody) — stejná struktura jako u standardního Article SEO.

### Interní prolinkování

| Zásada | Specifikace |
|--------|-------------|
| **Min. odkazů na článek** | 3-5 interních odkazů |
| **Kotvící text** | Popisný (ne "klikněte zde") |
| **Odkaz na související články** | 2-3 na článek |
| **Odkaz na kontakt/audit** | 1 v CTA sekci |

```markdown
DOBŘE: Přečtěte si víc o [technickém SEO auditu](/blog/technicke-seo-audit/)
ŠPATNĚ: Klikněte [zde](/blog/technicke-seo-audit/) pro víc informací
```

### Meta požadavky

**Title tag:** `[Název článku] | evisions.cz Blog`, 50-60 znaků, obsahuje primární klíčové slovo.

**Meta popisek:** 150-160 znaků, obsahuje primární klíčové slovo, jasnou hodnotu.

---

## 8. Autorská transparentnost a čerstvost obsahu

### Požadované prvky

```markdown
---
**O autorovi**

**[Jméno]** je [role] v evisions Advertising se specializací na
[oblast]. Spojte se na [LinkedIn].

*Aktualizováno: [Datum]*
---
```

### Frekvence revize obsahu

| Typ obsahu | Frekvence revize | Spouštěč aktualizace |
|------------|-------------------|------------------------|
| Evergreen how-to (SEO/PPC základy) | Ročně | Zásadní změny algoritmu/platformy |
| Trend analýzy (AI, nové funkce platforem) | Čtvrtletně | Nové funkce, změny nástrojů |
| Case studies | Neaktualizuje se (časové razítko) | — |

---

## 9. Checklisty

### Pre-publish checklist

**E-E-A-T**
- [ ] Autor s rolí a odkazem na LinkedIn
- [ ] Všechny statistiky mají zdroj
- [ ] Žádné garance konkrétních výsledků
- [ ] Datum aktualizace uvedeno

**Struktura**
- [ ] Jediný H1 (název článku)
- [ ] Logická hierarchie H2-H3-H4 (bez přeskočení úrovní)
- [ ] Obsah (ToC) u článků nad 1500 slov
- [ ] Zdroje sekce u how-to obsahu

**Čitelnost**
- [ ] Průměrná délka věty 10-18 slov
- [ ] Odstavce 40-100 slov
- [ ] Max. 3 odstavce za sebou bez vizuálního zlomu
- [ ] Klíčové termíny tučně

**Formátování**
- [ ] Vhodné callout typy, ne za sebou
- [ ] Tabulky pro srovnání
- [ ] Seznamy správně formátované (odrážky vs. číslované)

**Technické SEO**
- [ ] Meta title 50-60 znaků
- [ ] Meta popisek 150-160 znaků
- [ ] 3-5 interních odkazů
- [ ] Popisný kotvící text
- [ ] Alt text u obrázků

**Kvalita**
- [ ] Odpovídá ToV Guide principům
- [ ] Case study vs. how-to struktura dle sekce 5
- [ ] Praktické příklady
- [ ] Actionable závěry

---

## Appendix: Rychlá reference

| Prvek | Kdy použít | Frekvence |
|-------|-------------|-----------|
| H1 | Název článku | 1 na stránku |
| H2 | Hlavní sekce | 3-7 na článek |
| H3 | Podsekce | dle potřeby |
| Tip callout | Praktická rada | 2-3 na článek |
| Warning callout | Riziko/chyba | 1-2 na článek |
| Keep in Mind | Limity metody | 1 na how-to článek |
| Tabulka | Srovnání | dle potřeby |
| Blockquote | Klíčové principy | 1-2 na článek |

---

## Document History

| Verze | Datum | Změny |
|-------|-------|-------|
| 1.0 DRAFT | 2026-07-10 | První verze |

---

*Companion document: [evisions.cz Blog Tone of Voice Guide](evisions_tov_guide_CZ.md)*
