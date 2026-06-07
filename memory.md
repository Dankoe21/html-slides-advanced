# Memory — html-slides-advanced

Append-only log of lessons from QA runs and user sessions for improving the skill itself (process improvements, not content rules — those live in `SKILL.md`). Newest on top. Keep each entry to 3–5 sentences. Read before editing the skill; add an entry after each meaningful session.

---

## 2026-06-07

Q5 style picker previously listed only ~28 of the 49 styles in arbitrary order, with emoji swatches and sparse descriptions — users had no reliable way to navigate the full library. Rebuilt Q5 as a three-section table (Core / Curated Presets / Bold Template Library) with real hex color values and USE-STYLE-GUIDE-sourced descriptions for all 49, numbered sequentially. Added `style-picker.html` as a standalone companion artifact with color-swatch cards, scheme/formality indicators, and live filtering by Dark/Light/Mixed/Formality/Category. Card numbers were initially overlaid on the first swatch color (invisible on dark-first palettes like Dark, 8-Bit Orbit, Neon Cyber); fixed by moving the number inline before the style name in the card body. Tri-theme deck (Brand → Dark → Light across a 9-slide session) confirmed as a valid and distinctive structural pattern worth explicitly documenting in SKILL.md.

## 2026-06-07 (earlier)

First production tri-theme deck built from 11 source articles — Brand (#1) for slides 1–4, Dark (#2) for slides 5–7, Light (#3) for slides 8–9. Visual QA via Playwright caught two issues: quote slides (2 and 6) had a large blank band at the bottom because the `slide-inner` flex container wasn't being sized to the full 1080px stage height — fixed by adding explicit `width: 1920px; height: 1080px` to all inner div variants. Lum-glow sweep was bleeding past the quote text and painting over the attribution line below it; scoped the effect to only the quote `<p>` element by switching from `overflow: hidden` on the container to `display: inline-block; width: 100%` on the target element. BCI diagram on slide 8 had text clipping inside the COMPUTER box — fixed by widening the rect from 170px to 210px and reducing font size from 22px to 21px.

