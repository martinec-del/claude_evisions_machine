---
name: evisions-content-plan-sheet-discrepancy
description: Primary Content Plan sheet for all /evisions-* skills is now 1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q (Content Plan Index Sheet); 1ru1ix1Nt... is secondary/on-request only
metadata: 
  node_type: memory
  type: project
  originSessionId: 4db7a601-a7eb-4368-8d80-eb78f8cee1e5
  modified: 2026-08-18T15:06:37.608Z
---

**Current primary (2026-08-18, later in the day):** [Content Plan Index Sheet](https://docs.google.com/spreadsheets/d/1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q/edit?gid=754600260#gid=754600260), file ID `1QGRBoGYILY-n96j8uvCh1CV4pWRvVksAzFZnn1cga7Q`. Turned out to be the user's own upload of the `content_plan_index.xlsx` mirror Claude had generated (confirmed by finding Claude's own Legenda text and "SEO-30" next-ID value inside it when reading it) — the user uploaded it to Drive and, when asked to confirm, said yes, this should become the editable primary going forward. It has the exact same structure as the ledger/xlsx (Legenda tab + one tab per category, "Kapitola / Nadpis" column = ID not title). All CLAUDE.md / skill / guide references were updated 2026-08-18 to a three-tier structure. See [[evisions_dedup_ledger]] for how the ledger/xlsx/primary-Sheet triangle works.

**Previous primary, now secondary (only read on explicit user request):** `1ru1ix1NtUmFPT5EFRGUFq5fYeatbyFF3zH_4yRV46TY` (tab gid=1262896623) — an editorial calendar with richer historical data than the ledger currently carries (Lokace, zpracoval, klíčová slova, brief for older articles). Columns: Lokace | Lekce | Kapitola/Nadpis | Obsah kapitoly | Typ obsahu | zpracoval | Článek/Case | odhad práce | klíčová slova | brief | složka s výstupy | final docs | log | Status | Počet, grouped into per-category tables (SEO, PPC, Social, AI & SEO, Copywriting, Konference, Marketing, evisions interní, International, Kariéra) each with their own ID prefix (SEO-XX, PPC-XX, SOC-XX, AI-XX, CW-XX, CONF-XX, MKT-XX, EVI-XX, INTL-XX, CAR-XX) and "Skupina" subgroups tagged with `topic_cluster_[slug]_CZ` markers.

**Why:** confirmed with the user 2026-08-17 (secondary sheet became primary that day); confirmed again 2026-08-18 that the uploaded mirror should replace it as primary, with the 08-17 sheet kept around "for reference" per the user's own words, not read automatically.

**How to apply:** `CLAUDE.md`, `data/output/guides/evisions_content_inventory.md`, `README.md`, `data/output/content_plan_index.md`, and all `.claude/commands/evisions-*.md` skill files reference the current primary sheet ID first, with the secondary sheet mentioned only as "on request." Only `src/evisions_content.egg-info/PKG-INFO` still has the oldest placeholder ID (`1W8VTbwT8...`) — auto-generated build artifact, not worth hand-editing. If the user asks to switch the primary sheet again, update the same set of files plus this memory.
