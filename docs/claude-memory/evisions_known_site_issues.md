---
name: evisions-known-site-issues
description: Known broken URL and HTML template gaps on evisions.cz blog content pipeline — check before reusing
metadata: 
  node_type: memory
  type: project
  originSessionId: dbbf0115-cf2e-4686-8069-8338ee720e18
  modified: 2026-09-01T14:16:35.005Z
---

**Broken internal link:** `https://www.evisions.cz/case-study-pripadova-studie/` no longer resolves to a dedicated page — it falls back to the generic `/blog/` listing. The correct current URL for case-study content is the tag archive: `https://www.evisions.cz/blog/tag/case-study-pripadova-studie/`. Found 2026-08-27 while rewriting "Jak vybrat nejlepší SEO agenturu?" (a pre-2026 article still linked the old URL). **How to apply:** before reusing `/case-study-pripadova-studie/` as an internal link target in any `/evisions-rewrite-article` or `/evisions-new-article` run, verify it live (WebFetch) or use the tag-archive URL instead.

**`src/step4_html.py` author box is hardcoded generic:** `_html_template()` always renders "Content Team / evisions Advertising" in the author box, regardless of the article's actual author (name/role discovered at Init, e.g. "Marek Foršt, Head of SEO"). This is a script limitation, not something fixable per-article in the markdown. **How to apply:** flag this as a known QA gap in Krok 5 for any rewrite/new-article run where the source article has a named author — either patch `_html_template()` to accept author params, or note it for manual fix in the CMS at publish time.

**Old-style evisions.cz blog URLs (`/blog-YYYY-MM-DD-slug/` pattern) are dead:** the live site silently redirects them (HTTP 200) to the generic `/blog/` listing page instead of 404ing, so `curl`/`WebFetch` status checks alone won't catch it — you have to check the *effective* final URL after redirect, not just the status code. Found 2026-09-01 in "SEO nástroje + 7 rozšíření" (SEO-24): its own internal link to `evisions.cz/blog-2020-08-05-pruvodce-seo-pro-zacatecniky/` redirected this way, and no live `/blog/[slug]/` replacement exists for that article (WebSearch confirms Google still indexes only the dead old-style URL). **How to apply:** in Krok 5 QA, when checking internal links follow redirects and compare the final URL to what was expected — a redirect to `/blog/` (not the specific article) means the link target is gone; don't just link it out, since there's usually no known-good replacement slug to substitute automatically — ask the user.

**Google's old `webmasters.googleblog.com` blog URLs are dead (404), moved to `developers.google.com/search/blog/...`:** any pre-2021 evisions.cz article citing a Google blog post via the old domain will 404. The path segment after the domain usually stays the same, e.g. `webmasters.googleblog.com/2020/05/evaluating-page-experience.html` → `developers.google.com/search/blog/2020/05/evaluating-page-experience` (drop the `.html`). Found 2026-09-01 in SEO-24. **How to apply:** in Krok 5 QA, when an external link uses `webmasters.googleblog.com`, try the `developers.google.com/search/blog/` equivalent before flagging it as unfixable.

**`src/export_article_docx.py` had two rendering bugs, fixed 2026-09-01:** (1) headings like `### **Text**` rendered the literal `**` in Word instead of stripping it (now handled by `_clean_heading_text()`); (2) standalone `---` markdown horizontal-rule lines rendered as literal "---" paragraphs in Word (now skipped). Both fixes are in the script itself, so they apply automatically to every future article — no per-article workaround needed, but worth knowing this Word-export path existed as a silent quality gap for a while.
