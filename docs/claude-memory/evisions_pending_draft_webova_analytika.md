---
name: evisions-pending-draft-webova-analytika
description: An unfinished "Webová analytika" article draft exists in data/output/articles/ from a prior session, stuck at Krok 6 with Krok 7 never run
metadata:
  type: project
  originSessionId: 4db7a601-a7eb-4368-8d80-eb78f8cee1e5
  modified: 2026-08-18T15:06:46.991Z
---

`data/output/articles/webova-analytika-co-to-je-a-jak-ji-vyuzit-pro-marketing/` contains a complete draft (article .md/.html + outline + step1 xlsx + log, 1590 words) created 2026-08-17 in an earlier session, for the SEO / "Analytika a metriky" TODO topic "Webová analytika: co to je a jak ji využít pro marketing". It went through Krok 1–6 of the write workflow but **Krok 7 (QA + Content Plan update) never ran** — the log's last entry (Step 6) flags one open item: author attribution ("zpracoval") is missing because the Content Plan row has no value for it.

**Why this matters:** discovered 2026-08-18 while rebuilding the dedup ledger — the ledger had wrongly noted this topic as "planned, no local folder yet." Fixed in `data/output/content_plan_index.md` (both the TODO entry and the "Lokální složky výstupů" table).

**How to apply:** if the user or a future `/evisions-new-article` run touches this topic again, resume/finish the existing draft (starting with Krok 7 — resolve the author attribution and run QA) rather than starting a new one from scratch. Don't create a second `webova-analytika...` folder.
