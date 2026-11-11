---
name: evisions-cta-link-density-feedback
description: User dislikes double-linking the same target URL in adjacent sentences during conversion-focused CTA edits — keep one clear link per CTA moment
metadata: 
  node_type: memory
  type: feedback
  originSessionId: dbbf0115-cf2e-4686-8069-8338ee720e18
  modified: 2026-08-27T09:30:43.730Z
---

When adding conversion CTAs to evisions.cz blog articles (e.g. multiple mentions of a target URL like `/seo/`), don't link the same URL twice in immediately adjacent sentences (e.g. an inline keyword-anchor mention followed a sentence later by an explicit "Kontaktujte nás" CTA to the same target). User called this "nasilu" (forced/pushy) and asked for it to be toned down.

**Why:** During the "Jak vybrat nejlepší SEO agenturu?" rewrite (2026-08-27), a conversion-focused brief called for keyword anchors ("SEO agentura", "SEO agentura Praha") AND explicit CTA links, both pointing to `/seo/` within a few sentences of each other. This read as keyword-stuffed. User's fix: keep the keyword phrase as plain text, drop the redundant link, and let the one clear CTA link (e.g. "Kontaktujte nás", "Ozvěte se nám") carry the actual link.

**How to apply:** For future `/evisions-rewrite-article` or `/evisions-new-article` runs with conversion/CTA briefs — draft with one link per CTA moment (not one per keyword mention). If a section naturally wants both a keyword anchor and a closing CTA, prefer linking only the closing CTA and leaving the keyword mention as unlinked text. Related: [[evisions-content-plan-sheet-discrepancy]].
