# evisions.cz — Lead Opportunity Analysis (Site-wide SEO Growth Audit)

**Datum:** 2026-07-28
**Konverzní cíl:** odeslaný poptávkový/kontaktní formulář ("Domluvte si schůzku")
**Zdroje dat:** Ahrefs Site Explorer + Keywords Explorer, manuální GSC export ("Performance on Search", období **poslední 3 měsíce k 2026-07-27**, tzn. cca 2026-04-27 – 2026-07-27), Marketing Miner (CZ cross-check)
**Vertikály v analýze:** PPC Audit, Linkbuilding, SEO agentura, Sociální sítě (B2B), GEO/AI Search Optimization

---

## Site-wide diagnóza

Téměř každá service stránka na webu sdílí stejný vzorec: **pozice 9–25 (spodek str. 1 až str. 3), stovky až tisíce impressions za 3 měsíce, ale CTR blízko nule (0–1,7 %).** To ukazuje na systémový problém (slabší doménová autorita, title/meta neodpovídající intentu, nedostatečné interní prolinkování), ne izolované chyby jednotlivých stránek. Zároveň existuje jasná **kanibalizace klíčových slov** kolem tématu "SEO agentura" (homepage, `/seo/` a blog článek si navzájem konkurují) a **nevyužitý potenciál existujícího blog obsahu**, který generuje vysoké impressions, ale neprolinkovává čtenáře na stránky s formulářem.

---

## 1. Tabulka prioritních příležitostí (existující stránky)

| Cílová URL | Klíčové slovo | Aktuální pozice | Hledanost (Ahrefs / MM) | Hlavní páka růstu | Konkrétní akční krok | Priorita |
|---|---|---|---|---|---|---|
| `/seo/` (+ konsolidace s `/`, `/blog/jak-vybrat-nejlepsi-seo-agenturu/`) | seo agentura | GSC 8,6 (dotaz), homepage blend 8,27, blog blend 9,08, `/seo/` blend 12,51 | 700 / 400 | **Internal Linking** (řešení kanibalizace) | Zvolit `/seo/` jako canonical cíl (má přímý CTA/formulář). Upravit interní odkazy z homepage a z blog článku "jak vybrat nejlepší SEO agenturu" tak, aby primární CTA vedly na `/seo/`, ne zpět na blog. Sjednotit title tagy, aby si nekonkurovaly na stejnou frázi. | **Nejvyšší** |
| `/audit-socialnich-siti/` | audit sociálních sítí | 7,7 | N/A / 60 (Ahrefs) | **Quick Win — title/meta** | Stránka je téměř na str. 1 (poz. 7,7), ale má 0 kliků z 197 impressions za 3M. Přepsat title/meta tag tak, aby odpovídal search intentu a obsahoval jasný CTA text. | **Nejvyšší** |
| `/seo-copywriting/` | seo copywriting / seo copy | 8,6 | 250 / 280 | **Quick Win — title/meta** | 16 349 impressions za 3 měsíce (druhý nejvyšší objem na webu), ale CTR jen 0,03 % (5 kliků). Přepsat title/meta — největší nepoměr pozice/CTR na celém webu, minimální úsilí, potenciálně velký dopad. | **Vysoká** |
| `/linkbuilding/` | linkbuilding | 13,8 (blend), dotaz 13,8 | 200 / 440 | **Internal Linking** | Blog článek "Linkbuilding jako efektivní nástroj..." generuje 6123 impressions/3M, ale neprolinkovává na tuto službovou stránku s CTA. Přidat viditelný CTA blok a interní odkaz z blogu na `/linkbuilding/`. | **Vysoká** |
| `/skoleni-linkbuildingu/` | školení linkbuilding | 13,4 | 700 / 110 (YoY **+347 %** dle MM) | **Content Gap** | Rozšířit obsah (osnova školení, termíny, reference, FAQ schema) — téma s explozivním růstovým trendem, aktuálně podvystavěné vůči poptávce. | **Vysoká** |
| `/ppc-audit/` | ppc audit | 24,1 (stránka), 23,1 (dotaz) | 800 / 230 | **Content Gap** | Reálná poptávka (606 impressions/3M na "ppc audit"), stránka existuje přesně pro tento dotaz, ale je na str. 3. Rozšířit obsah (konkrétní proces auditu, případové studie, FAQ) + technická SEO revize. | **Vysoká** |
| `/seo-ai-audit/` | geo audit / seo ai audit | 6,8 | N/A / 10 (nízký, ale rostoucí) | **Internal Linking + Content Gap** | Nejlepší CTR ze všech service stránek (1,7 %) — funguje, jen potřebuje víc podpory. Prolinkovat AI/GEO blog sérii (case study Moneta Money Bank, "AI Mode", "Query Fan-Out") přímo na tuto stránku s CTA. | **Vysoká** |
| `/strategie-linkbuildingu/` | strategie linkbuildingu | 10,9 | 100 / — | **Quick Win — blízko str. 1** | Nejblíž průlomu na str. 1 z celého linkbuilding clusteru. Menší technická/obsahová revize (title, interní odkazy z blogu) může stačit k posunu na str. 1. | **Střední-vysoká** |
| `/sprava-socialnich-siti/` | správa sociálních sítí | 17,2 | 450 / 300 | **Content Gap + Internal Linking** | Rozšířit obsah o konkrétní B2B use-case (ne DIY Instagram tipy) a prolinkovat z LinkedIn-relevantního blog obsahu. | Střední |
| `/sprava-ppc-kampani/` | správa ppc kampaní | 14,8 | — | **Internal Linking** | Prolinkovat case study `/blog/spoluprace-e-visions-a-nefertitis-...150-diky-ppc/` (reálný výsledek +150 % tržeb) přímo na tuto stránku s CTA — nevyužitý sociální důkaz. | Střední |

---

## 2. Tabulka nových příležitostí

| Klíčové slovo | Hledanost (Ahrefs / MM) | Navrhovaný typ stránky | Záměr (Intent) | Priorita |
|---|---|---|---|---|
| správa LinkedIn / LinkedIn správa profilů | N/A (MM) / GSC: 1074 impressions kumulativně za 3M napříč variantami | **Nová Landing Page** (dedikovaná sekce/stránka v rámci `/sprava-socialnich-siti/` nebo samostatná `/sprava-linkedin/`) | Commercial (B2B) | **Vysoká** — reálná poptávka, nulové pokrytí na webu. Prolinkovat na formulář s předvyplněným zájmem "SoMe". |
| seo agentura praha | 800 / 320 (YoY **+68 %** dle MM) | Úprava existující stránky (`/seo/` title/H1, ne nová stránka) | Commercial, lokální | **Vysoká** — rostoucí lokální komerční poptávka, jednoduchá úprava. |
| optimalizace pro ai vyhledávače | 10 / — (pozice aktuálně 47 — velmi špatná) | **Content cluster** navazující na `/seo-ai-audit/` | Informační → Commercial | Střední-vysoká — rostoucí téma 2026, nízký aktuální volume, ale strategický směr, kde web už má náskok (case study, blog série). |
| mezinárodní seo agentura | 50 / — | Sekce v rámci `/expanze-do-zahranici/` nebo `/seo/`, ne samostatná stránka | Commercial | Nízká-střední — nízký volume, ale nulová konkurence nákladů na realizaci (jen rozšíření existující stránky). |

---

## 3. TOP 5–10 Quick Wins

1. **`/audit-socialnich-siti/`** — přepsat title a meta description. Stránka je na pozici 7,7 (skoro str. 1) se 197 impressions/3M, ale 0 kliků — čistě CTR problém, nejrychlejší možný dopad na leady ze všeho v analýze.
2. **`/seo-copywriting/`** — přepsat title/meta. 16 349 impressions/3M při CTR 0,03 % — největší absolutní nepoměr pozice/CTR na webu.
3. **Vyřešit kanibalizaci "seo agentura"** — přesměrovat interní odkazy z homepage a z blog článku "Jak vybrat nejlepší SEO agenturu" na `/seo/` jako jediný canonical cíl s CTA. Nejvyšší absolutní impressions v celé analýze (3107/3M).
4. **Prolinkovat blog "Linkbuilding jako efektivní nástroj..."** (6123 impressions/3M) → přidat viditelný CTA blok vedoucí na `/linkbuilding/`.
5. **Prolinkovat case study "Spolupráce e-Visions a Nefertiti" (+150 % tržeb díky PPC)** → CTA na `/ppc-audit/` a `/sprava-ppc-kampani/`. Nevyužitý sociální důkaz s nulovými kliky.
6. **Přidat "Praha" do title/H1 na `/seo/`** — zachytit rostoucí lokální poptávku "seo agentura praha" (MM YoY +68 %).
7. **Vytvořit dedikovanou LinkedIn sekci/stránku** prolinkovanou na formulář — reálná poptávka (~1074 impressions/3M), nulové pokrytí.
8. **Rozšířit `/skoleni-linkbuildingu/`** (osnova, termíny, reference, FAQ) — téma s YoY +347 % růstem dle Marketing Mineru.
9. **Prolinkovat AI/GEO blog sérii** (Moneta Money Bank case study, "AI Mode", "Query Fan-Out") → CTA na `/seo-ai-audit/`, který už má nejlepší CTR ze všech service stránek.
10. **`/strategie-linkbuildingu/`** — menší technická/obsahová revize k posunu z pozice 10,9 na str. 1.

---

## 4. Návrh zadání s odhadem leadového dopadu (Tabulka 1 + Tabulka 2)

### Metodika odhadu (čti před tabulkami)

Evisions.cz nemá napojené sledování konverzí (GA4 goal / CRM) k tomuto reportu, proto jsou odhady leadů **modelované, ne měřené** — postavené na dvou předpokladech:

1. **CTR podle pozice** (odvětvový benchmark organického CTR, bez SERP funkcí): poz. 1 = 27,6 %, poz. 2 = 15,8 %, poz. 3 = 11,0 %, poz. 4 = 8,0 %, poz. 5 = 6,0 %, poz. 6 = 4,7 %, poz. 7 = 3,7 %, poz. 8 = 3,0 %, poz. 9 = 2,5 %, poz. 10 = 2,2 %, poz. 11–15 = 1,5 %, poz. 16–20 = 1,0 %, poz. 20+ = 0,5 %.
2. **Konverzní poměr klik → odeslaný formulář:** 3–5 % pro service/landing stránky s přímým CTA a jasným komerčním intentem; 4–6 % pro vysoce komerční audit/konzultační stránky; 1–2 % pro stránky se smíšeným/informačním intentem (např. seo copywriting); 0,5–1,5 % pro podpůrný blog obsah.

Výpočet pro každý řádek: **aktuální kliky/měsíc** (z GSC, 3M/3) → **cílové kliky/měsíc** (impressions × cílový CTR po realizaci zadání) → **čistý nárůst** → **odhad leadů/měsíc** (čistý nárůst × konverzní rozsah). Čísla ber jako rozpětí pro prioritizaci, ne jako garanci — doporučujeme po realizaci nasadit GA4 goal tracking na formulář a odhady kalibrovat na reálná data.

### Tabulka 1 — Existující stránky: zadání + odhad dopadu

| # | Cíl / URL | Návrh zadání | Aktuální kliky/měsíc | Cílová pozice/CTR | Čistý nárůst kliků/měsíc | Odhad leadů/měsíc | Čas do efektu |
|---|---|---|---|---|---|---|---|
| 1 | `/seo/` (konsolidace s `/`, blogem) | Zvolit `/seo/` jako canonical cíl pro "seo agentura", přesměrovat interní CTA z homepage a blogu, sjednotit title tagy | ~2,3 | Poz. 8,6 → 5–6 (benchmark CTR ~5,3 %) | ~53 | **1,6 – 2,7** | 3–6 měsíců |
| 2 | `/audit-socialnich-siti/` | Přepsat title/meta (čistě CTR fix, pozice se nemění) | 0 | Poz. 7,7 (beze změny) → CTR ~3,3 % | ~2 | **0,06 – 0,1** | 2–4 týdny |
| 3 | `/seo-copywriting/` | Přepsat title/meta (CTR fix) | ~1,7 | Poz. 8,6 (beze změny) → CTR ~2,75 % | ~148 | **1,5 – 3,0** | 2–4 týdny |
| 4 | `/linkbuilding/` | CTA blok v blogu "Linkbuilding jako efektivní nástroj..." + interní prolinkování | ~2,3 (stránka) | Poz. 13,8 → 9–10 (postupný ranking uplift) | ~2,2 | **0,07 – 0,12** | 2–4 měsíce |
| 5 | `/skoleni-linkbuildingu/` | Rozšířit obsah (osnova, termíny, reference, FAQ schema) | ~1,0 | Poz. 13,4 → 8–9 (CTR ~2,75 %, + YoY trend) | ~9,5 | **0,2 – 0,4** | 2–4 měsíce, dále rostoucí |
| 6 | `/ppc-audit/` | Rozšířit obsah (proces auditu, case studies, FAQ) + technická revize | ~0,7 | Poz. 24,1 → 8–10 (CTR ~2,6 %) | ~5 | **0,2 – 0,3** | 3–6 měsíců |
| 7 | `/seo-ai-audit/` | Prolinkovat AI/GEO blog sérii (Moneta case study, AI Mode, Query Fan-Out) | ~4,7 | Poz. 6,8 → 4–5 (CTR ~6–8 %) | ~12 | **0,5 – 0,7** | 1–3 měsíce |
| 8 | `/strategie-linkbuildingu/` | Menší title/meta revize + interní odkazy z clusteru | ~0,7 | Poz. 10,9 → 6–7 (CTR ~4,2 %) | ~1 | **0,03 – 0,05** | 1–2 měsíce |
| 9 | `/sprava-socialnich-siti/` | Rozšířit o B2B use-case + prolinkovat LinkedIn obsah | 0 | Poz. 17,2 → 9–10 (CTR ~2,35 %) | ~1,6 | **0,05 – 0,08** | 3–4 měsíce |
| 10 | `/sprava-ppc-kampani/` | Prolinkovat case study Nefertiti (+150 % tržeb) jako social proof | ~1,3 (CTR už nadprůměrný) | Beze změny pozice — efekt hlavně na konverzní poměr, ne traffic | ~1 | **0,03 – 0,05** | 1–2 měsíce |
| | | | | | **Mezisoučet:** | **≈ 4,2 – 7,5 leadů/měsíc** | |

### Tabulka 2 — Nové příležitosti: zadání + odhad dopadu

| # | Klíčové slovo / téma | Návrh zadání | Aktuální kliky/měsíc (proxy) | Cílová pozice/CTR | Čistý nárůst kliků/měsíc | Odhad leadů/měsíc | Čas do efektu |
|---|---|---|---|---|---|---|---|
| 1 | Správa LinkedIn | Vytvořit dedikovanou landing page/sekci `/sprava-linkedin/` s formulářem (zájem "SoMe") | ~0,3 | Nová stránka → poz. 8–10 (CTR ~2,6 %) | ~9 | **0,4 – 0,5** | 4–6 měsíců (nový obsah bez historie) |
| 2 | SEO agentura Praha | Přidat "Praha" do title/H1 na `/seo/` | ~0 (GSC ukazuje jen 6/měsíc, MM odhaduje 320/měsíc poptávky) | Poz. 11,1 → 8–10 (CTR ~2,5 %) | ~7,5 | **0,4 – 0,5** | 2–4 měsíce |
| 3 | Optimalizace pro AI vyhledávače | Content cluster navazující na `/seo-ai-audit/` | ~0,1 | Poz. 47 → 10–15 (CTR ~1,8 %) | ~0,2 | **< 0,05** (spíš strategická investice než krátkodobý lead kanál) | 4–6 měsíců |
| 4 | Mezinárodní SEO agentura | Sekce v rámci `/expanze-do-zahranici/` nebo `/seo/` | 0 | Poz. 11,4 → 7–9 (CTR ~3 %) | ~2,7 | **0,1 – 0,16** | 2–3 měsíce |
| | | | | | **Mezisoučet:** | **≈ 0,9 – 1,2 leadů/měsíc** | |

### Souhrnný odhad dopadu celého balíčku

| Období | Konzervativní odhad | Optimistický odhad |
|---|---|---|
| Za měsíc (po plném náběhu) | ~5,2 leadů | ~8,7 leadů |
| Za kvartál (po plném náběhu) | ~15 leadů | ~26 leadů |

**Poznámky k interpretaci:**
- Čísla jsou **kumulativní až po plném náběhu všech zadání** (typicky 3–6 měsíců od zahájení realizace) — v prvním měsíci realizace bude reálný přírůstek výrazně nižší, protože quick winy (dny/týdny) fungují dřív než content gap a nová landing page (měsíce).
- Nejsilnější poměr efekt/úsilí mají řádky #1, #3 a #7 z Tabulky 1 (konsolidace "seo agentura", `/seo-copywriting/`, `/seo-ai-audit/`) — vysoký objem impressions, nízké/střední úsilí na realizaci.
- Doporučený další krok: nasadit GA4 goal tracking na odeslání formuláře, aby šlo tyto modelové odhady po 1–2 měsících nahradit reálnými konverzními daty a zpřesnit prioritizaci.

---

*Report vygenerován skillem `/evisions-lead-opportunity`. Neobsahuje editace webu ani content plánu — realizace jednotlivých bodů se zadává samostatně.*
