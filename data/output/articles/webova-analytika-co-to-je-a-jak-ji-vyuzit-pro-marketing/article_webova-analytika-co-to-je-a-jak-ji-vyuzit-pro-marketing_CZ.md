# Webová analytika: co to je a jak ji využít pro marketing

Digitální marketing bez dat je jen odhad. Webová analytika tento odhad mění na měřitelné rozhodnutí — kolik návštěvníků nakoupí, odkud přišli a proč část z nich odejde hned po vstupu na stránku. V článku ukážeme, jak vybrat základní nástroje, přečíst klíčové metriky a hlavně jak z nich vytěžit konkrétní marketingové rozhodnutí, ne jen další graf v dashboardu.

## Co je webová analytika

Webová analytika je sběr a vyhodnocování dat o chování návštěvníků na webu s cílem podpořit konkrétní marketingové rozhodnutí. Zahrnuje metriky jako počet návštěv, konverzní poměr nebo zdroje návštěvnosti — vždy ale s otázkou, co s daným číslem uděláte dál. Bez této vazby na rozhodnutí zůstává analytika jen sbírkou grafů.

Pojem se často zaměňuje se širším pojmem *analýza webu*, případně synonymem *digitální analytika*. Rozdíl je hlavně v rozsahu záběru — a záměna může vést ke špatnému očekávání od reportu, který dostanete.

Pro marketéra má webová analytika smysl přesně v okamžiku, kdy přestane být samoúčelným sledováním čísel a stane se podkladem pro rozhodnutí o rozpočtu, obsahu nebo cílení kampaně. Bez tohoto propojení se z ní snadno stane administrativní úkol — dashboard, který se občas otevře, ale nikdo podle něj nic nemění.

### Webová analytika vs. analýza webu

Webová analytika se soustředí na chování návštěvníků a jejich cestu k cíli — od vstupu na web až po konverzi. Analýza webu bývá širší pojem, který kromě chování návštěvníků může zahrnovat i technický SEO audit, konkurenční analýzu nebo kontrolu přístupnosti. V praxi se oba pojmy prolínají, ale stojí za to je od sebe odlišit.

| Pojem | Co zahrnuje |
|-------|-------------|
| Webová analytika | Chování návštěvníků, konverze, zdroje návštěvnosti, průběžné vyhodnocování |
| Analýza webu | Širší audit — SEO, technický stav, konkurence, UX, přístupnost |

## Jaké nástroje webovou analytiku umožňují

Analytické nástroje se liší podle toho, jestli měří chování na webu, výkon ve vyhledávání, nebo obojí. Základem pro většinu webů je kombinace Google Analytics 4 (GA4) a Google Search Console — oba nástroje jsou zdarma a společně pokrývají chování na webu i výkon ve vyhledávání. Google Universal Analytics, předchůdce GA4, přestal zpracovávat data k 1. červenci 2023. Přechodu a nastavení GA4 jsme se podrobně věnovali v článku [Universal Analytics končí, ať žije Google Analytics 4!](https://www.evisions.cz/blog/universal-analytics-konci-at-zije-google-analytics-4/).

Search Console zase propojuje organickou návštěvnost s konkrétními vyhledávacími dotazy — jak ji využít naplno, popisujeme v článku [Google Search Console: Jak ji v SEO využít naplno?](https://www.evisions.cz/blog/google-search-console-jak-ji-v-seo-vyuzit-naplno/). Google Tag Manager pak slouží k centrální správě měřicích kódů bez zásahu do kódu webu — tomuto nástroji se budeme věnovat v samostatném článku.

Pro weby s vyššími nároky na ochranu dat existuje alternativa Matomo. Na rozdíl od GA4, který data odesílá na servery Google, umožňuje Matomo hostovat analytiku na vlastním serveru — data tak zůstávají výhradně majiteli webu.

Výběr nástroje přitom neovlivňuje jen to, kam se data ukládají, ale i to, jak přesná ve výsledku budou. Nástroje závislé na cookies třetích stran ztrácejí přehled o návštěvnících dřív než ty, které stojí na vlastních doménách a serverovém zpracování — k tématu přesnosti dat se vrátíme v sekci o častých chybách.

| Nástroj | Co měří | Kdy použít |
|---------|---------|------------|
| Google Analytics 4 | Chování, konverze, cesty návštěvníků | Základní nástroj pro většinu webů zdarma |
| Google Search Console | Výkon ve vyhledávání, dotazy, indexace | Doplněk k GA4 pro organickou návštěvnost |
| Matomo | Stejná data jako GA4, hostovaná na vlastním serveru | Weby s vyššími nároky na ochranu dat/GDPR |
| Heatmapy (Smartlook, Hotjar) | Vizuální chování na stránce (kliky, scroll) | Kvalitativní doplněk k číselným datům |

> **Tip:** Pro většinu menších webů stačí kombinace GA4 a Search Console zdarma. Heatmapy a Matomo přidejte, až budete řešit konkrétní UX problém nebo nároky na soukromí dat.

## Klíčové metriky a jak je číst

Tento oddíl se soustředí na metriky, které si spočítáte přímo v GA4 nebo Search Console. Pokud navíc sledujete konkurenční viditelnost, funguje na podobném principu specializovaná metrika [Share of Voice](https://www.evisions.cz/blog/share-of-voice-sov-k-cemu-je-a-jak-metriku-spocitat/) — číslo samo o sobě nic neřeší, dokud ho nespojíte s kontextem trhu.

### Metriky vs. dimenze

Metrika je číslo — počet návštěv, konverzní poměr, míra okamžitého opuštění. Dimenze dává tomuto číslu kontext — zdroj návštěvnosti, typ zařízení nebo konkrétní stránku. Samotná metrika bez dimenze je jen statistika. Teprve v kombinaci s dimenzí se stává podkladem pro rozhodnutí.

Typická chyba je číst reporty jen na úrovni metrik — "návštěvnost vzrostla o 10 %" — bez toho, aby se k číslu přidala alespoň jedna dimenze. Až odpověď na otázku "u koho, odkud a na jakém zařízení" dělá z pozorování použitelný podklad pro rozhodnutí.

### Konverzní poměr — metrika, která rozhoduje o rozpočtu

Konverze je akce, kterou web od návštěvníka očekává — nákup, odeslání formuláře, stažení ceníku. Konverzní poměr je podíl konverzí na celkovém počtu návštěv nebo uživatelů. Google Analytics tuto metriku nedávno přejmenoval na key event rate, princip výpočtu se ale nemění.

U e-shopu s 10 000 měsíčními návštěvami a konverzním poměrem 2 % to znamená 200 objednávek. Zvýšení poměru na 2,5 % bez jediné koruny navíc do PPC přinese 50 objednávek navíc — proto je konverzní poměr metrika, která přímo ovlivňuje, kam alokovat rozpočet.

U B2B webu s formulářem místo košíku se logika nemění, jen se posouvá definice konverze. Cílem není nákup, ale odeslaný poptávkový formulář nebo stažení ceníku — konverzní poměr pak ukazuje, jak efektivně web mění návštěvnost v konkrétní obchodní příležitost, ne v objednávku.

### Míra okamžitého opuštění a zdroje návštěvnosti

Míra okamžitého opuštění (bounce rate) měří podíl návštěv, při kterých uživatel odejde po zobrazení jediné stránky, aniž by dál interagoval s webem. Sama o sobě ale nic neříká — vysoký bounce rate z placené kampaně signalizuje jiný problém než stejné číslo u organického vyhledávání.

Proto se bounce rate vždy čte společně se zdrojem návštěvnosti. Kombinace obou dimenzí ukáže, jestli problém leží v kampani, v obsahu stránky, nebo v očekávání, se kterým návštěvník na web přišel.

## Jak webovou analytiku využít pro marketingová rozhodnutí

Samotné sledování metrik nikoho neposune dál. Rozdíl dělá krok, který následuje po zjištění čísla — analýza dat, která vede ke konkrétnímu rozhodnutí, kam dál.

| Metrika | Co ukazuje | Jaké rozhodnutí z toho plyne |
|---------|------------|-------------------------------|
| Konverzní poměr klesá na mobilu | Problém v mobilním UX nebo checkoutu | Prioritizovat mobilní UX audit před dalším PPC rozpočtem |
| Vysoký bounce rate z placené kampaně | Nesoulad mezi reklamou a landing page | Upravit landing page nebo přecílit kampaň |
| Nízký podíl návratných návštěvníků | Slabá retence, ne akviziční problém | Investovat do remarketingu nebo e-mailu místo dalšího náboru |
| UTM data ukazují kanál s nejvyšší konverzí | Který kanál reálně přivádí platící zákazníky | Přesunout rozpočet směrem k ověřenému kanálu |

Bez UTM parametrů analytika nepozná, který konkrétní kanál přivedl konverzi — jen obecný zdroj návštěvnosti. UTM parametry se přidávají k odkazu a označují zdroj, médium a název kampaně; Google pro jejich generování nabízí vlastní Campaign URL Builder. Bez nich zůstává rozhodování o rozpočtu jen odhadem.

Heatmapy doplňují číselná data o vizuální pohled na chování na stránce — kam uživatelé klikají, kam scrollují a kde opouštějí formulář. Nenahrazují metriky z GA4, ale vysvětlují, proč se dané číslo chová tak, jak se chová.

> **Example:** Pokud konverzní poměr klesne jen na mobilních zařízeních a zdroj návštěvnosti zůstává stejný, problém je pravděpodobně v mobilním UX, ne v kampani samotné. Heatmapa v tomto případě rychle ukáže, kde uživatelé formulář opouštějí.

Stejný princip propojení dat napříč kanály popisujeme v článku o [synergii PPC a SEO](https://www.evisions.cz/blog/synergie-ppc-a-seo-klic-k-digitalnimu-uspechu/) — analytika je spojnice, která rozhoduje, kam rozpočet přesunout dál.

Rozhodnutí založená na datech přitom nemusí čekat na měsíční report. Konverzní poměr a zdroje návštěvnosti se vyplatí sledovat týdně, UTM data po každé nové kampani a heatmapy vždy, když se mění klíčová stránka — landing page, košík nebo formulář.

## Časté chyby při interpretaci dat

**Sledování metrik bez vazby na cíl.** Počet návštěv roste, ale bez propojení na konverze jde jen o vanity metriku — číslo, které dobře vypadá v reportu, ale samo o sobě nic neřídí.

**Ignorování dopadu cookie souhlasu na přesnost dat.** Odmítnutí trackování snižuje objem zachycených dat, takže výsledná čísla jsou vždy jen odhad, ne přesný součet. Souvislost mezi souhlasem uživatele a přesností měření jsme rozebrali v článku [Co je Google Consent Mode V2 a musíte to řešit?](https://www.evisions.cz/blog/co-je-google-consent-mode-v2-a-musite-to-resit/).

**Srovnávání nesourodých období nebo kanálů.** Porovnání víkendu s pracovním týdnem u B2B webu, nebo organické návštěvnosti s placenou kampaní bez zohlednění rozdílného chování, vede k mylným závěrům o tom, co skutečně funguje.

**Spoléhání na souhrnný dashboard bez segmentace.** Průměrný konverzní poměr celého webu skryje rozdíly mezi mobilem a desktopem, novými a vracejícími se návštěvníky nebo jednotlivými kampaněmi. Rozhodnutí založené na jednom souhrnném čísle tak snadno míří na špatný problém.

> **Keep in Mind:** Žádný analytický nástroj neměří 100 % návštěvnosti. Nástroj Intelligent Tracking Prevention od Applu omezuje životnost cookies nastavených přes JavaScript na sedm dní, což zkresluje počet skutečně vracejících se návštěvníků. Data z analytiky jsou model reality, ne přesný součet — důležitější je trend v čase než jednotlivé přesné číslo.

## Klíčové závěry

- Webová analytika má smysl jen tehdy, když každá sledovaná metrika vede ke konkrétnímu rozhodnutí.
- Metriku vždy čtěte v kontextu dimenze — zdroje, zařízení, časového období. Samostatné číslo nic neříká.
- Konverzní poměr a UTM data jsou nejsilnější dvojice pro rozhodování o rozpočtu.
- Data z žádného nástroje nejsou stoprocentně přesná — počítejte s tím při interpretaci.
- Pro start stačí GA4 a Search Console zdarma, další nástroje přidávejte podle konkrétní potřeby.

## Zdroje

- [Upgrade to Google Analytics 4 before July 1 — Google Blog](https://blog.google/products/ads-commerce/upgrade-to-google-analytics-4-before-july-1/)
- [About key events — Google Analytics Help](https://support.google.com/analytics/answer/9267568?hl=en)
- [Engagement rate and bounce rate — Google Analytics Help](https://support.google.com/analytics/answer/12195621?hl=en)
- [URL builders: Collect campaign data with custom URLs — Google Analytics Help](https://support.google.com/analytics/answer/10917952?hl=en)
- [100% Data Ownership — Matomo](https://matomo.org/100-data-ownership/)
- [Understanding Safari's Intelligent Tracking Prevention (ITP) and Its Impact — CustomerLabs](https://www.customerlabs.com/blog/understanding-safari-intelligent-tracking-prevention-apple-itp-impact/)
