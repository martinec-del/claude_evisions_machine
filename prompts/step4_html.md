# Krok 4: HTML konverze

Konvertujte finální markdown článek do stylovaného HTML pomocí evisions.cz blog šablony.

**Toto je deterministický krok — použijte přímo `src/step4_html.py` (`convert_to_html()`), nikoli LLM generování HTML od nuly.** Tento prompt slouží jako reference pro manuální/edge-case úpravy.

---

## ZÁKLADNÍ PRINCIP

> **PRAVIDLO:** Obrázky z originálního článku se drží svého TÉMATU (Mapa obrázků), ne pevné pozice.
> Význam obsahu se nikdy nemění. Aplikuje se pouze prezentace.

---

## Struktura stránky (povinné pořadí)

```
1. <header>          Černé pozadí, evisions logo + nav
2. <nav.breadcrumb>   Blog > Titulek článku
3. <toc>              Obsah (u článků >1500 slov)
4. <article>          Plný obsah článku
5. <div.author-box>   Autor + datum aktualizace
6. <div.disclaimer>   Poznámka k obsahu
7. <footer>           Černé pozadí, evisions logo + odkazy
```

---

## Brand barvy (placeholder — nahradit reálnou paletou evisions.cz)

| Proměnná | Hex | Použití |
|----------|-----|---------|
| `--evi-accent` | `#0057ff` | Odkazy, tlačítka, Tip callout akcent |
| `--evi-dark` | `#12131a` | H2/H3 nadpisy, ToC text, hlavičky tabulek |
| `--evi-gray` | `#6b7280` | Tělo textu |
| `--evi-light` | `#f8f9fa` | ToC pozadí, sudé řádky tabulky |

> **Až bude známá skutečná brand paleta evisions.cz, nahradit hex hodnoty v `src/step4_html.py` CSS bloku.**

---

## Typografie

**Font:** Poppins (Google Fonts) — stejně jako `src/step4_html.py`.

| Prvek | Velikost | Váha |
|-------|----------|------|
| H1 | 2.25rem | 700 |
| H2 | 1.5rem | 600 |
| H3 | 1.25rem | 600 |
| Tělo textu | 1rem | 400 |

---

## Obrázky

Každý obrázek se zabaluje do `<figure class="article-image">` s `<figcaption>` z alt textu:

```html
<figure class="article-image">
    <img src="[URL]" alt="[popisný alt text]" loading="lazy">
    <figcaption>[Krátký popisek obrázku]</figcaption>
</figure>
```

Chybějící obrázek u vizuálního tématu → placeholder s poznámkou `[IMAGE NEEDED: popis]`.

---

## Obsah (ToC)

Povinné u článků nad 1500 slov, umístěné po úvodu, před hlavním obsahem:

```html
<div class="toc">
    <p class="toc-title">Obsah</p>
    <ul>
        <li><a href="#core-web-vitals">Core Web Vitals a jejich dopad</a></li>
    </ul>
</div>
```

---

## Callout styling

| Typ | Třída |
|-----|-------|
| Tip | `callout callout-tip` |
| Warning | `callout callout-warning` |
| Important | `callout callout-important` |
| Note | `callout callout-note` |
| Keep in Mind | `callout callout-keep-in-mind` |

---

## Autor box a disclaimer

Generováno automaticky šablonou (`_html_template()` v `src/step4_html.py`) — obsahuje autor box s datem aktualizace a poznámku k obsahu. Neduplikovat ručně v markdownu.

---

## HTML Checklist

- [ ] Struktura stránky v povinném pořadí
- [ ] Poppins font načten
- [ ] ToC přítomen u článků >1500 slov
- [ ] Všechny obrázky mají popisný alt text a `loading="lazy"`
- [ ] Autor box s datem aktualizace
- [ ] Poznámka k obsahu přítomna
- [ ] Meta title 50-60 znaků
- [ ] Meta popisek 150-160 znaků
- [ ] Responzivní (max-width 1160px)

---

## Document History

| Verze | Datum | Změny |
|-------|-------|-------|
| 1.0 | 2026-07-10 | První verze, adaptováno z FTMO Academy step4_html.md |
