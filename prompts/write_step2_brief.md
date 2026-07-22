# Krok 2: Brief & osnova

Vytváříte redakční brief a osnovu obsahu pro nový článek na evisions.cz blogu. Tato osnova je blueprint pro draft — musí být schválena uživatelem před psaním.

## ZÁKLADNÍ PRINCIP

> **PLÁNOVAT, NEPSAT.** Tento krok produkuje strukturovanou osnovu s klíčovými body na sekci.
> Žádná próza, žádné plné věty v těle článku. Pouze architektura.

---

## Dostupné vstupy v tomto kroku

- Konkurenční analýza z Kroku 1 (témata, strukturní vzory, mezery)
- Keywords xlsx z Kroku 1 (keyword, volume, notes)
- Content Plan Sheet kontext (Kategorie, existující související články pro interní odkazy)
- ToV Guide klasifikace (Case study vs. How-to/trend analýza)

---

## Struktura briefu

### 1. Metadata článku

```
Téma:           [Název tématu]
Slug:           [article-slug]
Kategorie:      [SEO / PPC / AI & SEO / Analytika / E-commerce / Případovky]

Typ obsahu:     Case study | How-to / trend analýza
  Důvod:        [jednovětý důvod]

Cíl počtu slov: [rozsah, např. 1200–1600 slov]
  Podklad:      [konkurenční průměr / složitost tématu]
```

### 2. Diferenciace od konkurence

- Co tento článek dělá jinak, než co je vidět v konkurenčním researchi
- Jaká data/case study evisions přidává, co konkurence nemá
- Témata záměrně vynechaná (mimo rozsah)

### 3. Klíčová slova — nadpisy

Použít keyword set z Kroku 1 xlsx. Top 3-5 dle objemu → přiřadit k H1/H2, kde to téma přirozeně sedí. Nikdy nenutit keyword do nadpisu, pokud to láme přirozený jazyk.

| # | Keyword | Volume | Přiřazení nadpisu |
|---|---------|--------|----------------------|

### 4. Kostra nadpisů

Plná struktura H2/H3 s klíčovými body, callouty a tabulkami na sekci — viz Structure Guide sekce 5 pro šablonu dle typu obsahu (case study vs. how-to).

### 5. Plán interních odkazů

Min. 3-5 odkazů na související publikované články z Content Plan Sheetu (Status = Published).

### 6. Content validace

Zkontrolovat jako marketingový expert: Odpovídá struktura logicky tématu? Jsou přítomny všechny klíčové koncepty? Chybí něco, co by čtenář očekával?

Výstup: validation note (pass / flagged issues).

---

## Výstup — dva artefakty

**1. Outline soubor (.docx):**

```bash
.venv/bin/python src/export_outline_docx.py data/output/articles/[slug]/article_[slug]_CZ_outline.md
```

**2. Log soubor** — append Step 2 sekce do `article_[slug]_CZ_log.md`

---

## Stop podmínka

> **Krok 2 dokončen.** Osnova pro "[Titulek]" — [Case study/How-to], ~[N] slov.
> **Osnova uložena:** `[plná absolutní cesta k .docx]`
> Zkontrolujte → schvalte → pokračujte na Krok 3.

**Nezačínat psát draft, dokud osnova není schválena.**
