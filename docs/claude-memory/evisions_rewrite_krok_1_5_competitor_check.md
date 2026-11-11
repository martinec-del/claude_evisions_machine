---
name: evisions-rewrite-krok-1-5-competitor-check
description: "/evisions-rewrite-article now has a Krok 1.5 competitor SERP gap-check between keywords and ToV, with a user-chosen Mode A/B"
metadata: 
  node_type: memory
  type: project
  originSessionId: 11098f8f-2ed3-4ea9-b78a-c6f169f13165
  modified: 2026-09-01T14:16:15.796Z
---

`/evisions-rewrite-article` was extended (2026-09-01) with a new **Krok 1.5: Konkurenční SERP kontrola**, inserted between Krok 1 (Klíčová slova) and Krok 2 (ToV). Workflow is now 6 steps, not 5.

**What it does:** takes 2-3 primary keywords from the article's keywords.xlsx, runs Ahrefs `serp-overview` (country cz) for each, WebFetches the top 3-4 organic competitor URLs (deduped), and compares their structure/depth against the article to find real content gaps (missing topics/sections, not formatting differences — formatting stays Krok 3's job).

**If gaps are found, it STOPs and asks the user to choose:**
- **Mode A — "konkurenceschopná revize":** allowed to write and insert new sections/paragraphs closing the gaps. This is drafted in a new **Fáze -1** at the very start of Krok 3 (Struktura), before the paragraph audit, and is the **only place in the entire rewrite workflow where new information may be added** — everywhere else the hard rule is still "never add/remove facts."
- **Mode B — "beze změny pravidla":** gaps are only logged as future recommendations; no new content is added, current strict behavior is preserved.

If no gaps are found, it skips the mode question and goes straight to Krok 2.

**Why:** [[evisions_dedup_ledger]] and the rest of the rewrite flow only ever reshuffled/enhanced presentation of existing content — there was no check for whether the rewritten article would actually be competitive enough to rank, since it never compared against what's currently ranking for the target keywords. The user explicitly wanted this gap-check to be a deliberate, per-run choice (STOP + explicit A/B decision), not an automatic content-adding step, and wanted Claude to actually draft the new content in Mode A (not just leave TODOs for a human).

**How to apply:** When running `/evisions-rewrite-article` in default `rewrite` mode, Krok 1.5 fires automatically after Krok 1. The `quick`, `tov`, and `structure` isolated modes skip it (structure-only mode has no competitor gap-filling available since it doesn't do keyword research).

**Files touched by this change:** `data/output/guides/evisions_workflow_CZ.md` (v1.2), `prompts/step1b_competitor_check.md` (new), `prompts/step3_structure.md` (new Fáze -1), `.claude/commands/evisions-rewrite-article.md`, `CLAUDE.md`.
