---
name: evisions-topic-cluster-output-prefs
description: "How the user wants /evisions-topic-cluster's final Krok 5 output formatted — concise, action-focused, Word export, tool-vs-article intent check for new articles"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7320a5b2-155e-4018-b2eb-0f57c498a824
---

For `/evisions-topic-cluster` (topic cluster / publikační plán audit skill), the user corrected the default Krok 5 (final report) format twice in the same session. Both corrections are now baked into `.claude/commands/evisions-topic-cluster.md` itself, so the skill should already produce this by default — this memory is a backup record of *why*, in case the skill file ever gets reverted or copied into a new project.

**Rule 1 — Krok 5 output must be short and decision-focused, not an exhaustive audit report.**
Format: short intro (how many revise / how many new + no-cannibalization confirmation) → **REVIDOVAT** (existing articles: URL, new primary keyword if changed, 2–4 bullet points to add) → **NAPSAT NOVĚ** (new articles) → one short **Shrnutí a zdůvodnění** paragraph.
Why: user's exact words — "chci hlavně jak přistoupit k článkům -> jaké vytvořit nové a jaké revidovat... ja musím hlavně označit stránky co revidovat a které v tomto topic clusteru napsat nové." The first Krok 5 draft (separate REVIZE / NOVÝ OBSAH / KONTROLA KANIBALIZACE / PROLINKOVÁNÍ sections with an ASCII link diagram) was too long for the actual use case, which is a quick reference for deciding what to hand off to `/evisions-rewrite-article` vs `/evisions-new-article`.
How to apply: default to the short format. Only add a formal cannibalization table or a link-scheme diagram section if the user explicitly asks for the expanded version.

**Rule 2 — Every new-article proposal needs an explicit tool-vs-article search-intent check.**
For each new article's primary keyword, check the Krok 2/3 SERP data for navigational/tool intent (e.g. the brand's own product/login pages dominating positions 1–4) before finalizing it as a blog-article target. If the bare term is tool-dominated, shift to the "co je X" / "co to je X" informational variant and justify it with the actual SERP contrast (what wins on the bare term vs. the "co je" term).
Why: user's words — "lidé můžou hledat pod nějakými kws spíše nástroj například než článek tak to ber v potaz a téma tomu přizpůsob aby článek měl šanci rankovat." Concrete case this session: "google tag manager" (2400/mo) is dominated by Google's own tagmanager.google.com + login/install sitelinks — a blog article can't win that. Switched primary keyword to "google tag manager co to je" (150/mo), where the SERP is actually editorial content.
How to apply: this check happens per new-article row in the Krok 5 output, with a one-line "Kontrola intentu" note — either flags the reframe + reason, or confirms in one sentence that editorial content already dominates.

**Rule 3 — Word export is the default deliverable for Krok 5, not opt-in.**
After saving `data/output/clusters/[slug]/topic_cluster_[slug]_CZ.md`, immediately run `python src/export_outline_docx.py <path>` to produce the `.docx` alongside it (same tool/styling the project already uses for article outlines). Before exporting, replace ASCII diagrams with plain bullet lists and keep tables outside of code fences, since the docx script has no fence-awareness and doesn't render ASCII art.
Why: user asked for the Word doc explicitly once, then treated the docx as the expected deliverable in all follow-ups without re-asking.
How to apply: always produce both the .md and .docx for this skill's final step; no need to wait for the user to ask for Word specifically.

See also: [[evisions-content]] (skill router), the skill file itself at `.claude/commands/evisions-topic-cluster.md` is the authoritative, executable version of these rules.
