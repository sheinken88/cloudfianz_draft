# Cloudfianz website — permanent working agreement

## Three languages are part of every website change

The user requires the entire redesigned website in Spanish (`es-AR`), English (`en`), and Brazilian Portuguese (`pt-BR`). Treat every request to change website content, functionality, navigation or design as a request for all three locales. Do not ask the user to repeat this requirement. Do not mark a change complete with missing or stale translations.

- The active site is `prototype/`, not the original `src/` website or `prototype/archive-v1/`.
- Keep one shared layout and behavior. Spanish source lives in `prototype/templates/`, `prototype/content/`, and `prototype/page_layouts/`.
- Every rendered text node and user-facing attribute (including alt text, accessible labels, titles and SEO descriptions) is translated at build time by `prototype/i18n/render.py`. English and Portuguese catalogs are `prototype/i18n/en.json` and `pt.json`, keyed by normalized Spanish source text. If a source sentence changes, add its reviewed translations to BOTH catalogs. Never substitute Spanish as a fallback or add untranslated placeholder values to make validation pass.
- Browser-generated copy belongs in `prototype/i18n/runtime.json`, with `es`, `en`, and `pt` for every message. Do not hardcode new user-facing text in JavaScript.
- Routes for every page and language belong in `prototype/i18n/routes.json`. When adding a page, also update the Spanish source route map and Vercel rewrites. Language links must open the equivalent page, not reset to Home. Keep internal navigation in the selected language. Maintain canonical URLs, `lang`, and reciprocal `hreflang` links.
- The language selector shares the site's Inter typography, navy text, mint selection and restrained rounded borders. Keep it available on mobile and usable by keyboard, including visible focus and Escape to close.
- Project images must remain static: no click-to-enlarge, image-file links or zoom cursors. The user explicitly accepted keeping original screenshot text in its source language.
- Keep client/product names and factual claims consistent. Translate editorial diagrams and mockups. Original client screenshots/logos may retain the source product's language; keep their descriptive alt text and captions localized.
- The same HubSpot form remains connected in all locales. Localize its configured labels, validation and submission states. Check external consent copy separately; do not remove consent, change subscription IDs, or submit test leads without a specific reason and authorization.

## Required validation before completion or push

1. Run `npm run build:proposal` (fails on untranslated new/changed source strings).
2. Run `npm run check:i18n` (39 pages today; checks routes, links, metadata, runtime coverage, and intentional missing-translation rejection).
3. Run `node --check prototype/dist/app.js` and `git diff --check`.
4. Check changed pages in all languages, at desktop and mobile widths. Pay attention to longer Portuguese labels, menu wrapping and form states. Do not claim checks you did not perform.
5. Commit shared sources, catalogs and regenerated `prototype/dist/` outputs together. Never fix only generated HTML.

The preview repository is remote `draft` (`sheinken88/cloudfianz_draft`), deployed from `main`. The original remote `origin` is a different repository. Do not push to the original by accident. A push requires a user request; a request to edit does not automatically request a push.
