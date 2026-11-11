---
name: fortuna-machine-build
description: "fortuna-content/ machine (RO/HR betting blogs, new-article only) lives at Desktop/fortuna-content; built 2026-10-22, test run pending; style sources and open client questions"
metadata:
  node_type: memory
  type: project
  originSessionId: 08286295-3616-478c-a620-2cf89f85cd63
  modified: 2026-10-22T09:22:13.070Z
---

Since 2026-10-22 a separate content machine exists at `C:\Users\Patrik Martinec\Desktop\fortuna-content\` (sibling of the evisions folder on purpose, so evisions CLAUDE.md doesn't leak in). It writes new articles only for efortuna.ro, casapariurilor.ro (RO) and psk.hr (HR). Skills: `/fortuna-new-article <web> #N`, `/fortuna-status`. Evisions machine must not be modified for it.

**Decisions by user:** STOP after every step; docx author field empty; clean HTML, docx is the main deliverable; outline/log in Czech, article in site language.

**Style source caveat:** all 3 sites + their CMS API are geoblocked from CZ ("Geoblock | FORTUNA GAME a.s."). User said to use ifortuna.cz as inspiration. Its articles come from `api.ifortuna.cz/cms-client/api/v1/articles/web/{slug}`. Help centers ajutor.efortuna.ro / ajutor.casapariurilor.ro / help.psk.hr are reachable via Exa for native terminology.

**Status:** build done and scripts tested on scratch copies. The real plan xlsx has NOT been written yet (columns Stav/Výstup/Poslední změna get added on first INIT). Proposed test run: efortuna.ro #9, CasaPariurilor.ro #6, psk.hr #5.

**Open client questions (compliance guide sec. 8):** athlete/celebrity profiles vs ONJN code 4.2.4 and HR ad ban on celebrities; exact RG closing text; efortuna self-exclusion period contradiction; HR age/helpline; odds in event articles.

**How to apply:** run the fortuna skills from a Claude Code session opened in fortuna-content. Update the ToV guides once the client sends real RO/HR sample articles.
