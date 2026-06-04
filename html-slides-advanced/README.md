# html-slides-advanced

Complete replacement for frontend-slides. Everything that skill did, plus 12 structured layout formats, content depth calibration, and mandatory Visual QA.

## File Map

| File | Role |
|------|------|
| `SKILL.md` | Master workflow — all 7 phases, all rules |
| `FORMATS.md` | HTML + CSS for all 12 canonical slide layouts + JS controller |
| `STYLES.md` | Brand, Dark (Midnight), Light (Serenity) + 12 style presets (full specs) |
| `ANIMATION-TOOLKIT.md` | Full animation CSS/JS, effect-to-feeling guide, per-format cheat sheet |
| `html-template.md` | HTML architecture, JS features, inline editing, image pipeline, code quality |
| `viewport-base.css` | Mandatory fixed 16:9 stage CSS — paste into every deck |
| `USER-STYLE-GUIDE.md` | Complete reference for all 49 design systems — colors, fonts, use cases |
| `render_slides.py` | Headless Playwright renderer for Visual QA |
| `bold-template-pack/selection-index.json` | Metadata for 34 bold templates — read in Phase 2 |
| `bold-template-pack/templates/*/preview.md` | Style cards for shortlisted bold templates |
| `bold-template-pack/templates/*/design.md` | Full design system for selected bold template |

## Workflow Summary

| Phase | What happens |
|-------|-------------|
| 0 | Detect mode: new presentation or enhancement of existing deck |
| 1 | Content discovery (5 questions) → image evaluation → calibration confirmation |
| 2 | Style discovery: 3 visual previews auto-generated and opened (safe / bold / wildcard) |
| 3 | Slide-by-slide outline with format + hero animation named — user approves before build |
| 4 | HTML generation using FORMATS + STYLES + ANIMATION-TOOLKIT + html-template |
| 5 | Save |
| 6 | Visual QA: render_slides.py → subagent inspection → fix → re-render |
| 6 | Deliver — open deck, summarize QA, explain navigation and inline editing |

## Style Library

**3 core styles:** Brand (paper/ink/red), Dark-Midnight (black/navy/amber), Light-Serenity (sage/slate/silver)
**12 curated presets:** Bold Signal, Electric Studio, Creative Voltage, Dark Botanical, Notebook Tabs, Pastel Geometry, Split Pastel, Vintage Editorial, Neon Cyber, Terminal Green, Swiss Modern, Paper & Ink
**34 bold templates:** full design systems in `bold-template-pack/`

**Palette source:** https://coolors.co/palettes

## The 12 Formats

1. Cover / Title · 2. Agenda · 3. Two-column · 4. Stat grid · 5. Feature bento
6. Comparison · 7. Steps / Process · 8. Roadmap / Timeline · 9. Chart
10. Code block · 11. Quote · 12. Closing / CTA
