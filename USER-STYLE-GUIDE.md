# HTML Slides Advanced — User Style Guide

A reference for every design system available in this skill.
Use this to choose a style before starting a new deck, or to understand what's
built into the system you already picked.

**How to select:** Answer Q5 during the skill questionnaire with the style name exactly as shown.

---

## How to Read This Guide

Each entry shows:
- **Description** — what it feels like and when to use it
- **Colors** — hex value · color name · ████ visual swatch · where it is used on slides
- **Typography** — font name · size range (pt equivalent at 1280px screen) · what it's applied to
- **Formality** — Low / Medium / High
- **Best for** — ideal use cases

---

# PART 1 — CORE STYLES

*Three fully specified design systems, ready to use out of the box.*

---

## #1 · Brand *(default)*

> Warm, editorial, and premium. Cream paper slides with near-black ink and a single sharp red accent. Feels like a quality print publication — confident but never corporate.

**Formality:** Medium-High · **Best for:** Pitches, product decks, conference talks, creator content, personal brand

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#FBEFD9` | Warm Paper | Slide background (~65% of all slides) |
| ██████ | `#100202` | Near-Black Ink | All body text, headings, borders, dark slide bg (cover/closing) |
| ██████ | `#D30B00` | Sharp Red | Spark mark, one accent word per headline, CTA buttons, active agenda item, chart fill, timeline NOW marker |
| ██████ | `#FFFFFF` | White | Card surfaces, mock panels, surface elements |
| ██████ `rgba(16,2,2,0.60)` | Ink 60% | Secondary text, captions, labels, footnotes |
| ██████ `rgba(16,2,2,0.14)` | Ink 14% | Borders, dividers |
| ██████ `rgba(211,11,0,0.10)` | Red Tint | Active item backgrounds, accent-dim fills |

*Dark slides (cover + closing):* background flips to `#100202`, text flips to `#FBEFD9`

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Crimson Pro | 500 Medium | ~50–70pt | Cover title, closing title |
| Crimson Pro | 500 Medium | ~33–45pt | Slide titles (h2) |
| Crimson Pro Italic | 500 | ~33–45pt | Accent word within headline (red italic) |
| Crimson Pro | 500 | ~25–35pt | Agenda numbers, quote text |
| Manrope | 700 Bold | ~15–18pt | Eyebrows / labels (uppercase, tracked) |
| Manrope | 400 Regular | ~16–20pt | Body text, sub-headings |
| Manrope | 600 SemiBold | ~15–18pt | Bullets, stat labels, card labels |
| Manrope | 400 Regular | ~15pt | Captions, footnotes (24px min) |
| Courier New / monospace | 400 | ~15pt | Code blocks (24px min) |

*Source: Google Fonts*

---

## #2 · Dark — "Midnight Sun Fun"

> Pure black slides with deep navy surfaces and a warm amber accent. Bold, high-contrast, and contemporary. Commands attention without feeling flashy.

*Palette source: [coolors.co/palettes](https://coolors.co/palettes) — Midnight Sun Fun*

**Formality:** Medium · **Best for:** Tech talks, developer audiences, product launches, keynotes, AI/data topics

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#000000` | Pure Black | Content slide background |
| ██████ | `#14213D` | Midnight Navy | Cover/closing slide bg, card surfaces, panel depth layers |
| ██████ | `#FCA311` | Warm Amber | Spark mark, ONE accent word per headline, CTA, stat numbers, active timeline/agenda marker, chart fill |
| ██████ | `#F5F0E8` | Warm Off-White | All body text, headings on dark backgrounds |
| ██████ `rgba(245,240,232,0.55)` | Off-White 55% | Secondary text, captions, labels |
| ██████ `rgba(245,240,232,0.12)` | Off-White 12% | Borders, dividers |
| ██████ `rgba(252,163,17,0.12)` | Amber Tint | Accent-dim fills, subtle highlights |

*Dark slides (cover + closing):* background shifts to `#14213D` for navy depth

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Manrope | 800 ExtraBold | ~50–70pt | Cover title, closing title |
| Manrope | 800 ExtraBold | ~33–45pt | Slide titles (h2) |
| Manrope | 400–500 | ~25–35pt | Sub-headings, agenda numbers, body text |
| DM Sans | 500 Medium | ~15–18pt | Eyebrows / labels |
| DM Sans | 400 Regular | ~16–20pt | Body text |
| DM Sans | 600 SemiBold | ~15–18pt | Bullets, stat labels |
| DM Sans | 400 Regular | ~15pt | Captions, footnotes |
| Courier New / monospace | 400 | ~15pt | Code blocks |

*Source: Google Fonts · Single-font system*

---

## #3 · Light — "Minimalist Serenity"

> Soft sage background with slate text and silver midtones. Calm, refined, and trustworthy. Feels like a well-designed annual report or premium investor brief.

*Palette source: [coolors.co/palettes](https://coolors.co/palettes) — Minimalist Serenity*

**Formality:** High · **Best for:** Executive presentations, investor decks, healthcare, finance, strategy, board-level content

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#EFF6EE` | Soft Sage | Slide background (all content slides) |
| ██████ | `#273043` | Deep Slate | All headings, body text, accent color (on light slides), cover/closing slide bg |
| ██████ | `#9197AE` | Muted Silver | Secondary text, captions, labels, borders, dividers |
| ██████ | `#FFFFFF` | White | Card surfaces, surface elements |
| ██████ `rgba(39,48,67,0.08)` | Slate Tint | Accent-dim fills, hover states |
| ██████ `rgba(145,151,174,0.30)` | Silver 30% | Borders |

*Dark slides (cover + closing):* background flips to `#273043` slate; text flips to `#EFF6EE` sage; accent becomes sage

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Plus Jakarta Sans | 800 ExtraBold | ~50–70pt | Cover title, closing title |
| Plus Jakarta Sans | 700 Bold | ~33–45pt | Slide titles (h2) |
| Plus Jakarta Sans | 600 SemiBold | ~25–35pt | Sub-headings |
| Plus Jakarta Sans | 700 Bold | ~15–18pt | Eyebrows / labels (uppercase, tracked) |
| Plus Jakarta Sans | 400 Regular | ~16–20pt | Body text |
| Plus Jakarta Sans | 500 Medium | ~15–18pt | Bullets, stat labels |
| Plus Jakarta Sans | 400 Regular | ~15pt | Captions, footnotes |
| Courier New / monospace | 400 | ~15pt | Code blocks |

*Source: Google Fonts · Single-font system — Plus Jakarta Sans used throughout*

---

# PART 2 — CURATED STYLE PRESETS

*12 fully specified presets, each with a distinct personality. Use when the three core styles don't match the brief.*

---

## #4 · Bold Signal

> Dark gradient with a bold colored card as the focal point. Confident, high-impact, and unmistakably design-led.

**Formality:** Medium · **Best for:** Agency credentials, brand launches, startup pitches, design reviews, founder keynotes

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#1a1a1a` | Near-Black | Slide background |
| ██████ | `#FF5722` | Signal Orange | Focal card, accent word, CTA, section numbers |
| ██████ | `#ffffff` | White | All text on dark bg |
| ██████ | `#1a1a1a` | Near-Black | Text sitting on orange card |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Archivo Black | 900 | ~50–70pt titles / ~33–45pt headings | Cover titles, section numbers, hero headlines |
| Space Grotesk | 400–500 | ~15–20pt body / ~13–15pt captions | All body text, labels, captions |

*Source: Google Fonts*

---

## #5 · Electric Studio

> High-contrast split panel — dark on one side, light on the other. Strong typographic presence. Feels like a polished brand book.

**Formality:** Medium-High · **Best for:** Product launches, investor pitches, brand showcases, keynotes

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#0a0a0a` | Near-Black | Dark panel background |
| ██████ | `#ffffff` | White | Light panel background, text on dark |
| ██████ | `#4361ee` | Electric Blue | Accent word, CTA, panel divider bar, active elements |
| ██████ | `#0a0a0a` | Near-Black | Text on light panel |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Manrope | 800 ExtraBold | ~50–70pt titles / ~33–45pt headings | All display text, titles, hero quotes |
| Manrope | 400–500 | ~50–70pt titles / ~33–45pt headings | All body text |

*Source: Google Fonts · Single-font system*

---

## #6 · Creative Voltage

> Electric blue split panels, neon yellow badges, halftone textures. Energized, retro-modern, and unapologetically bold.

**Formality:** Medium-Low · **Best for:** Creative agencies, developer tools, tech launches, hackathons, AI products

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#0066ff` | Electric Blue | Primary panel background |
| ██████ | `#1a1a2e` | Deep Dark | Secondary panel, dark slide bg |
| ██████ | `#d4ff00` | Neon Yellow | Accent word, badges, callouts, CTA |
| ██████ | `#ffffff` | White | All body text |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Manrope | 800 ExtraBold | ~50–70pt titles / ~33–45pt headings | All display text, titles, hero text |
| Manrope | 400–500 | ~15–20pt body | All body text, labels |
| Space Mono | 400–700 | ~13–15pt captions | Body text, labels, code-style copy |

*Source: Google Fonts*

---

## #7 · Dark Botanical

> Very dark background with soft blurred gradient circles. Elegant and premium. Feels like a luxury brand or gallery opening.

**Formality:** Medium-High · **Best for:** Luxury brands, fashion, galleries, wellness, premium B2B, artistic projects

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#0f0f0f` | Deep Black | All slide backgrounds |
| ██████ | `#e8e4df` | Warm Parchment | All body text, headings |
| ██████ | `#d4a574` | Warm Ochre | Accent word, CTA, decorative circles |
| ██████ | `#e8b4b8` | Soft Pink | Secondary accent, gradient overlays |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Cormorant | 400–600 | ~13–70pt | All display text, headlines, quote text |
| IBM Plex Sans | 300–400 | ~15–20pt body / ~13–15pt captions | Body text, labels, captions |

*Source: Google Fonts*

---

## #8 · Notebook Tabs

> Cream paper card sitting on a dark outer background, with colorful editorial tabs along the right edge. Tactile and organized.

**Formality:** Medium-High · **Best for:** Editorial content, conference programs, annual reports, structured presentations

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#f8f6f1` | Cream Paper | Slide card background |
| ██████ | `#2d2d2d` | Charcoal | Outer frame background, primary text |
| ██████ | `#98d4bb` | Mint Green | Section tab 1 |
| ██████ | `#c7b8ea` | Soft Lavender | Section tab 2 |
| ██████ | `#f4b8c5` | Blush Pink | Section tab 3 |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Bodoni Moda | 400–700 | ~50–70pt titles / ~33–45pt headings | Display headlines, section headings |
| DM Sans | 400–500 | ~15–20pt body / ~13–15pt captions | Body text, labels, tab text |

*Source: Google Fonts*

---

## #9 · Pastel Geometry

> White card on a soft pastel background with rounded vertical pills on the right edge. Friendly, organized, and modern.

**Formality:** Medium-Low · **Best for:** Lifestyle brands, SaaS onboarding, education, community, wellness

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#c8d9e6` | Soft Powder Blue | Outer slide background |
| ██████ | `#faf9f7` | Off-White | Card surface |
| ██████ | `#f0b4d4` | Pastel Pink | Right-edge pill 1 |
| ██████ | `#a8d4c4` | Pastel Mint | Right-edge pill 2 |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Plus Jakarta Sans | 700–800 | ~50–70pt titles / ~33–45pt headings | Display headlines |
| Plus Jakarta Sans | 400–500 | ~50–70pt titles / ~33–45pt headings | Body text, labels |

*Source: Google Fonts*

---

## #10 · Split Pastel

> Two-color vertical split background — peach on one side, lavender on the other. Playful badge pills and grid accents.

**Formality:** Medium-Low · **Best for:** Creator portfolios, lifestyle brands, DTC launches, beauty, wellness

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#f5e6dc` | Warm Peach | Left panel background |
| ██████ | `#e4dff0` | Soft Lavender | Right panel background |
| ██████ | `#c8f0d8` | Mint Badge | Pill badge 1 |
| ██████ | `#f0f0c8` | Yellow Badge | Pill badge 2 |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Outfit | 700–800 | ~50–70pt titles / ~33–45pt headings | All display headlines |
| Outfit | 400–500 | ~50–70pt titles / ~33–45pt headings | All body text, labels |

*Source: Google Fonts · Single-font system*

---

## #11 · Vintage Editorial

> Warm cream background with abstract geometric shapes and confident, witty typography. Feels like a premium magazine feature.

**Formality:** Medium · **Best for:** Brand manifestos, creative reviews, editorial pitches, founder vision decks

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#f5f3ee` | Warm Cream | Slide background |
| ██████ | `#1a1a1a` | Near-Black | All headings, body text |
| ██████ | `#e8d4c0` | Warm Warm | Geometric accent shapes, decorative elements |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Fraunces | 700–900 | ~50–70pt titles / ~33–45pt headings | All display headlines |
| Work Sans | 400–500 | ~15–20pt body / ~13–15pt captions | All body text, labels |

*Source: Google Fonts*

---

## #12 · Neon Cyber

> Deep navy with cyan and magenta neon accents, particle backgrounds, and grid patterns. Futuristic and techy.

**Formality:** Low-Medium · **Best for:** AI products, developer tools, futuristic tech, cybersecurity, gaming

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#0a0f1c` | Deep Navy | All slide backgrounds |
| ██████ | `#00ffcc` | Neon Cyan | Primary accent, CTA, active states |
| ██████ | `#ff00aa` | Neon Magenta | Secondary accent, highlight elements |
| ██████ | `#ffffff` | White | All body text |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Clash Display | 400–700 | ~50–70pt titles / ~33–45pt headings | All display headlines |
| Satoshi | 400–500 | ~15–20pt body / ~13–15pt captions | Body text, labels |

*Source: Fontshare*

---

## #13 · Terminal Green

> GitHub dark background with terminal green text. Monospace only. Scan lines and blinking cursor animations.

**Formality:** Low · **Best for:** Developer talks, CLI tools, open source, hacker aesthetic, engineering team content

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#0d1117` | GitHub Dark | All slide backgrounds |
| ██████ | `#39d353` | Terminal Green | All text, headings, accent elements, cursor |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| JetBrains Mono | 400–700 | ~50–70pt titles / ~15–20pt body (mono throughout) | Every text element — this style uses monospace exclusively |

*Source: JetBrains / Google Fonts*

---

## #14 · Swiss Modern

> Pure white, pure black, and a single red accent. Bauhaus-inspired grid. Precise, asymmetric, and visually disciplined.

**Formality:** Medium-High · **Best for:** Design talks, architecture, editorial, research, any content that benefits from strict visual discipline

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#ffffff` | Pure White | All slide backgrounds |
| ██████ | `#000000` | Pure Black | All headings, body text, grid lines |
| ██████ | `#ff3300` | Bauhaus Red | Accent word, CTA, geometric accents |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Archivo | 800 ExtraBold | ~50–70pt titles / ~33–45pt headings | All display headlines |
| Nunito | 400 Regular | ~15–20pt body / ~13–15pt captions | All body text, labels |

*Source: Google Fonts*

---

## #15 · Paper & Ink

> Warm cream with Cormorant Garamond serifs and a crimson accent. Literary, thoughtful, and elegant.

**Formality:** High · **Best for:** Editorial, literary, cultural institutions, academic, advisory, long-form brand storytelling

### Colors

| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ | `#faf9f7` | Warm Cream | Slide background |
| ██████ | `#1a1a1a` | Charcoal | All headings, body text |
| ██████ | `#c41e3a` | Crimson | Accent word, CTA, decorative rules |

### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Cormorant Garamond | 400–700 | ~50–70pt titles / ~25–35pt pull quotes | All display headlines, pull quotes |
| Source Serif 4 | 400 | ~15–20pt body / ~13–15pt captions | All body text, captions |

*Source: Google Fonts*

---

# PART 3 — BOLD TEMPLATE LIBRARY

*34 complete design systems from the bold template library. Each has its own palette, typography, layout grammar, and component vocabulary. Selected by name during Q5.*

---

## #16 · 8-Bit Orbit

> Pixel neon arcade on a deep dark void. Feels like a CRT screen at 2am.

**Scheme:** Dark · **Formality:** Low · **Density:** Medium
**Best for:** Gaming, cyberpunk, web3, hackathon demos, indie dev tools, synthwave brands

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#0a0514` | Void Purple-Black | Slide background |
| ██████ `#00ffcc` | Neon Cyan | Primary text accent, CTA, active elements |
| ██████ `#ff00ff` | Neon Magenta | Secondary accent, grid highlights |
| ██████ `#ffffff` | White | Body text |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Space Grotesk | 700–800 | ~50–70pt titles / ~33–45pt headings | All display text, section headers |
| Space Mono | 400 | ~15–18pt body / ~13–15pt captions | Body text, labels, UI chrome |
| Noto Sans SC | 400 | ~15–18pt | CJK fallback |

*Source: Google Fonts*


---

## #17 · Biennale Yellow

> Solar yellow on warm parchment. Art-biennale poster energy with Dutch editorial calm.

**Scheme:** Light · **Formality:** High · **Density:** Medium
**Best for:** Exhibition decks, arts institutions, design conferences, curatorial pitches, literary publications

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f5f0dc` | Warm Parchment | Slide background |
| ██████ `#ffd700` | Solar Yellow | Primary accent, headline highlight, CTA |
| ██████ `#1a1a1a` | Near-Black | All text |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Playfair Display | 700–800 Italic | ~50–70pt titles / ~33–45pt headings | All display headlines, editorial pull quotes |
| Work Sans | 400–500 | ~15–20pt body / ~13–15pt captions | Body text, labels, grid text |

*Source: Google Fonts*


---

## #18 · BlockFrame

> Neobrutalist chunky borders with pastel neon fills. Pop-graphic and design-led.

**Scheme:** Light · **Formality:** Medium-Low · **Density:** High
**Best for:** Indie SaaS, agency credentials, creative reviews, brand redesigns, bold design-led pitches

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#ffffff` | White | Slide background |
| ██████ `#000000` | Black | All borders (thick, 3px+), primary text |
| ██████ `#5544ff` | Electric Purple | Primary accent block |
| ██████ `#ff55aa` | Hot Pink | Secondary accent |
| ██████ `#aaff44` | Neon Lime | Tertiary accent |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Archivo Black | 900 | ~50–70pt titles / ~33–45pt headings | All display text, chunky bordered headers |
| Space Grotesk | 400–600 | ~15–20pt body / ~13–15pt captions | Body text, labels, UI elements |

*Source: Google Fonts*


---

## #19 · Blue Professional

> Clean, modern, and lightly authoritative. Cream paper with cobalt blue.

**Scheme:** Light · **Formality:** Medium-High · **Density:** Medium
**Best for:** B2B SaaS pitches, consulting deliverables, advisory updates, investor reports

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f8f6f1` | Warm Cream | Slide background |
| ██████ `#0071e3` | Cobalt Blue | Primary accent, CTA, active states |
| ██████ `#1a1a2e` | Near-Black Navy | All headings, body text |
| ██████ `#f0f4ff` | Pale Blue | Card surfaces, panel fills |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Playfair Display | 700 | ~50–70pt titles / ~33–45pt headings | Display headlines, section titles |
| Inter | 400–600 | ~15–20pt body / ~13–15pt captions | Body text, labels, data tables |

*Source: Google Fonts*


---

## #20 · Bold Poster

> Minimal copy, maximum typographic presence. Feels like a magazine cover.

**Scheme:** Light · **Formality:** Medium · **Density:** Low
**Best for:** Brand manifestos, founder vision decks, editorial pitches, creative reviews

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#fff8f0` | Soft Warm White | Slide background |
| ██████ `#1a1a1a` | Near-Black | All display text |
| ██████ `#D30B00` | Red | Single accent word, rule lines, CTA |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Archivo Black | 900 | ~50–70pt titles | Cover and poster headlines only — single large line |
| Manrope | 400–600 | ~15–20pt body / ~13–15pt captions | Supporting body text and labels |

*Source: Google Fonts*


---

## #21 · Broadside

> Newspaper headline energy on dark. Graphic, punchy, and literary.

**Scheme:** Dark · **Formality:** Medium-High · **Density:** Medium
**Best for:** Brand manifestos, magazine pitches, design talks, bilingual decks, founder vision statements

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#0c0c10` | Near-Black | Slide background |
| ██████ `#FF4500` | Fire Orange | Primary accent, headline highlight, masthead rule |
| ██████ `#f5f0e8` | Warm Off-White | All body text |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Playfair Display | 700–800 Italic | ~50–70pt titles / ~33–45pt headings | Newspaper-style masthead and section headers |
| Space Grotesk | 400–500 | ~15–20pt body / ~13–15pt captions | Body text, deck text, labels |

*Source: Google Fonts*


---

## #22 · Capsule

> Modular pill-shaped cards with a warm Y2K feel.

**Scheme:** Light · **Formality:** Medium-Low · **Density:** Medium
**Best for:** Lifestyle brands, creator portfolios, DTC launches, beauty, wellness, agency credentials

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#fdf6f0` | Warm Bone | Slide background |
| ██████ `#e05a20` | Burnt Orange | Primary accent, pill borders, CTA |
| ██████ `#2d2d2d` | Charcoal | All text |
| ██████ `#f0e0d0` | Warm Blush | Card fills, pill backgrounds |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Bodoni Moda | 400–700 Italic | ~50–70pt titles / ~33–45pt headings | Display headlines, pill card headings |
| Space Grotesk | 300–500 | ~15–20pt body / ~13–15pt captions | Body text, pill labels, captions |

*Source: Google Fonts*


---

## #23 · Cartesian

> Quiet, considered, and elegantly restrained. Warm-minimal with classical proportions.

**Scheme:** Light · **Formality:** High · **Density:** Low
**Best for:** Investment theses, white papers, advisory work, longform research, gallery decks

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#fafaf8` | Near-White | Slide background |
| ██████ `#2c2c2c` | Charcoal | Primary text, headings |
| ██████ `#8b7355` | Warm Umber | Accent word, rule lines, subtle highlights |
| ██████ `#d4cdc4` | Warm Gray | Borders, secondary text |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Playfair Display | 400–700 | ~50–70pt titles / ~33–45pt headings | Display headlines, section titles |
| Inter | 300–400 | ~15–20pt body / ~13–15pt captions | Body text, data labels, annotations |

*Source: Google Fonts*


---

## #24 · Cobalt Grid

> A quietly serious design research bulletin. One strict accent, printed-ledger calm.

**Scheme:** Light · **Formality:** High · **Density:** Medium
**Best for:** Studio annuals, design research, architecture, art publications, academic decks

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f8f9fa` | Off-White | Slide background |
| ██████ `#1e50b4` | Cobalt Blue | Primary accent, grid lines, section markers |
| ██████ `#1a1a2e` | Deep Navy | All headings, body text |
| ██████ `#e8edf8` | Pale Blue | Card fills, panel backgrounds |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Newsreader | 400–700 Italic | ~50–70pt titles / ~33–45pt headings | Editorial headlines, research section titles |
| Hanken Grotesk | 400–600 | ~15–20pt body / ~13–15pt captions | Body text, grid labels, data annotations |

*Source: Google Fonts*


---

## #25 · Coral

> Warm-graphic and editorial. A bold coral accent on a clean background.

**Scheme:** Mixed · **Formality:** Medium · **Density:** Medium
**Best for:** Fashion, beauty, fitness, lifestyle brands, agency credentials, creator portfolios

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#fff5f0` | Warm White | Slide background (light slides) |
| ██████ `#e84030` | Coral Red | Primary accent, CTA, headline highlight |
| ██████ `#1a1a1a` | Near-Black | All text |
| ██████ `#2d2020` | Deep Warm Dark | Dark slide background (cover/closing) |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Bebas Neue | 400 | ~50–70pt titles / ~33–45pt headings | All display headlines — condensed uppercase |
| Inter | 300–500 | ~15–20pt body / ~13–15pt captions | Body text, labels, supporting copy |

*Source: Google Fonts*


---

## #26 · Creative Mode

> Design-led and confident. Strong card layouts with expressive use of type and color.

**Scheme:** Light · **Formality:** Medium · **Density:** Medium-High
**Best for:** Creative agency pitches, design studio decks, ad credentials, brand reviews

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f8f8f6` | Off-White | Slide background |
| ██████ `#ff3c00` | Creative Orange | Primary accent, card highlight |
| ██████ `#1a1a1a` | Near-Black | All headings, body text |
| ██████ `#ffe8e0` | Pale Peach | Card fill, accent-dim |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Archivo Black | 900 | ~50–70pt titles / ~33–45pt headings | All display text, card headlines |
| Space Grotesk | 300–500 | ~15–20pt body / ~13–15pt captions | Body text, labels, card sub-copy |

*Source: Google Fonts*


---

## #27 · Daisy Days

> Friendly, warm, and joyful. Soft pastel backgrounds with cheerful accents.

**Scheme:** Light · **Formality:** Low · **Density:** Medium
**Best for:** Educational content, kids and family, wellness programs, workshops, craft/illustration creators

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#fff9f0` | Warm Cream | Slide background |
| ██████ `#ff8c42` | Sunny Orange | Primary accent, CTA |
| ██████ `#4ecdc4` | Soft Teal | Secondary accent |
| ██████ `#ffd93d` | Warm Yellow | Decorative fills, badge colors |
| ██████ `#2d2d2d` | Charcoal | All text |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Fredoka One | 400 | ~50–70pt titles / ~33–45pt headings | All display text — rounded, friendly |
| Quicksand | 400–600 | ~15–20pt body / ~13–15pt captions | Body text, badges, captions |

*Source: Google Fonts*


---

## #28 · Editorial Forest

> Quiet and warm editorial. Sage tones with a considered literary mood.

**Scheme:** Mixed · **Formality:** Medium · **Density:** Medium
**Best for:** Quarterly reviews, studio updates, creative agency presentations, research recaps

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f2f5f0` | Sage White | Slide background |
| ██████ `#2d4a38` | Forest Green | Primary accent, CTA, active states |
| ██████ `#3d3d35` | Warm Charcoal | All headings, body text |
| ██████ `#c8d8c0` | Sage Mist | Card fills, border color |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Source Serif 4 | 400–700 | ~50–70pt titles / ~33–45pt headings | All display headlines, pull quotes |
| Manrope | 400–500 | ~15–20pt body / ~13–15pt captions | Body text, labels, captions |

*Source: Google Fonts*


---

## #29 · Editorial Tri-Tone

> Three deliberate tones with serif/sans contrast. Feels like a fashion magazine spread.

**Scheme:** Mixed · **Formality:** Medium-High · **Density:** Medium
**Best for:** Fashion brands, lifestyle media, art direction reviews, editorial pitches

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f5f0e8` | Warm Parchment | Light slide background |
| ██████ `#1a1a1a` | Near-Black | Primary text, dark slide background |
| ██████ `#c8956c` | Warm Terracotta | Third tone — accent word, decorative elements |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Instrument Serif | 400 Italic | ~50–70pt titles / ~33–45pt headings | Display headlines — elegant, magazine feel |
| Bricolage Grotesque | 400–700 | ~15–20pt body | Body text, labels |
| JetBrains Mono | 400 | ~13–15pt captions | Data annotations, code elements |

*Source: Google Fonts*


---

## #30 · Emerald Editorial

> Serious magazine gravitas with a forest green masthead ornament.

**Scheme:** Mixed · **Formality:** Medium-High · **Density:** Medium
**Best for:** Leadership readouts, planning reviews, strategy briefings, product launches wanting editorial authority

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f8fdf8` | Pale Sage | Slide background |
| ██████ `#1a4a2a` | Emerald | Primary accent, masthead rule, CTA |
| ██████ `#1a1a1a` | Near-Black | All text |
| ██████ `#d0e8d4` | Mint Wash | Card fills, accent-dim |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Bodoni Moda | 400–700 Italic | ~50–70pt titles / ~33–45pt headings | Display headlines, editorial section titles |
| Manrope | 400–600 | ~15–20pt body / ~13–15pt captions | Body text, labels, supporting copy |

*Source: Google Fonts*


---

## #31 · Grove

> Organic, warm, and patient. Earthy serif typography with botanical calm.

**Scheme:** Mixed · **Formality:** Medium-High · **Density:** Medium
**Best for:** Sustainability brands, outdoor/nature, wineries, restaurants, literary/arts decks, advisory deliverables

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f5f2ec` | Natural Linen | Slide background |
| ██████ `#4a6741` | Grove Green | Primary accent, CTA |
| ██████ `#2d2820` | Warm Brown-Black | All text |
| ██████ `#c8b89a` | Warm Sand | Card fills, borders |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Playfair Display | 400–700 | ~50–70pt titles / ~33–45pt headings | Display headlines — organic, editorial feel |
| Jost | 300–500 | ~15–20pt body / ~13–15pt captions | Body text, labels, captions |
| JetBrains Mono | 400 | ~13–15pt | Code elements, data annotations |

*Source: Google Fonts*


---

## #32 · Long Table

> Warm, intimate, and hospitality-forward. Single warm accent, editorial voice.

**Scheme:** Light · **Formality:** Medium · **Density:** Medium
**Best for:** Supper clubs, restaurant brands, creative events, membership pitches, lifestyle brands

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#faf8f3` | Warm Off-White | Slide background |
| ██████ `#c8651e` | Terracotta | Primary accent, CTA, active states |
| ██████ `#2d2520` | Dark Umber | All headings, body text |
| ██████ `#f0e8d8` | Warm Cream | Card surfaces |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Fraunces | 700–900 Italic | ~50–70pt titles / ~33–45pt headings | Display headlines — warm, editorial |
| Bricolage Grotesque | 400–600 | ~15–20pt body / ~13–15pt captions | Body text, menu-style labels |

*Source: Google Fonts*


---

## #33 · Mat

> Mid-century, tactile, and intentional. Warm-modern with analog feel.

**Scheme:** Mixed · **Formality:** Medium · **Density:** Medium
**Best for:** Design studios, architecture, interior brands, ceramics, craft, furniture brands

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f0ebe3` | Stone Warm | Slide background |
| ██████ `#c86428` | Burnt Sienna | Primary accent, CTA |
| ██████ `#1e1a14` | Deep Warm Black | All text |
| ██████ `#d8cfc4` | Warm Putty | Card surfaces, borders |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Bricolage Grotesque | 600–800 | ~50–70pt titles / ~33–45pt headings | Display headlines — crafted, mid-century feel |
| DM Sans | 400–500 | ~15–20pt body | Body text, labels |
| DM Mono | 400 | ~13–15pt captions | Data labels, small annotations |

*Source: Google Fonts*


---

## #34 · Monochrome

> Black and white only. Words are the only thing on the page.

**Scheme:** Light · **Formality:** High · **Density:** High
**Best for:** User research, white papers, longform reports, academic briefs, advisory deliverables

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#fffef8` | Near-White | Slide background |
| ██████ `#111111` | Near-Black | All headings, body text, borders, accents |
| ██████ `#e0e0d8` | Light Gray | Card fills, dividers |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Lora | 400–700 Italic | ~50–70pt titles / ~33–45pt headings | Display headlines — literary, restrained |
| Jost | 200–400 | ~15–20pt body / ~13–15pt captions | Body text, labels — ultra-light, precise |

*Source: Google Fonts*


---

## #35 · Neo-Grid Bold

> Confident and editorial-graphic. Grid-structured layouts with punchy typography.

**Scheme:** Light · **Formality:** Medium · **Density:** High
**Best for:** Design-led pitches, brand work, founder talks, stat-heavy slides, comparison tables

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f5f5f3` | Off-White | Slide background |
| ██████ `#2828c8` | Electric Indigo | Primary accent, grid markers, CTA |
| ██████ `#1a1a1a` | Near-Black | All text |
| ██████ `#e8e8ff` | Pale Indigo | Card fills, accent-dim |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Space Grotesk | 600–700 | ~50–70pt titles / ~33–45pt headings | Display headlines, grid section markers |
| JetBrains Mono | 400–700 | ~15–20pt body / ~13–15pt captions | Body text, data labels, annotations |

*Source: Google Fonts*


---

## #36 · People's Platform

> Activist energy with bold block type. Honest, loud, and unapologetic.

**Scheme:** Light · **Formality:** Medium-Low · **Density:** Medium-High
**Best for:** Manifestos, civic decks, cultural commentary, campaign pitches, mission statements

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#fff8f8` | Warm White | Slide background |
| ██████ `#cc2060` | Hot Pink-Red | Primary accent, headline highlight |
| ██████ `#1a1a1a` | Near-Black | All text |
| ██████ `#ffe0ee` | Pale Pink | Card fills, accent-dim |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Alfa Slab One | 400 | ~50–70pt titles / ~33–45pt headings | All display text — bold, slab, activist |
| Caveat Brush | 400 | ~15–20pt body | Body text — handwritten energy |

*Source: Google Fonts*


---

## #37 · Pin & Paper

> Hand-crafted, warm, and literary. Safety-pin illustrations with paper-grain texture.

**Scheme:** Light · **Formality:** Medium · **Density:** Medium
**Best for:** Qualitative research, founder reflections, brand stories, workshop debriefs

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f8f5f0` | Natural Paper | Slide background |
| ██████ `#8b6914` | Warm Gold | Primary accent, CTA, pin illustration |
| ██████ `#2d2520` | Dark Umber | All text |
| ██████ `#e8e0d4` | Aged Cream | Card fills, texture overlay |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Space Grotesk | 500–700 | ~50–70pt titles / ~33–45pt headings | Display headlines, pinboard headers |
| Caveat | 500–700 | ~15–20pt body / ~13–15pt captions | Body text — handwriting style |

*Source: Google Fonts*


---

## #38 · Pink Script — After Hours

> Nocturnal, luxe, and intentionally moody. Script accents on dark.

**Scheme:** Dark · **Formality:** Medium-High · **Density:** Low
**Best for:** Fashion brands, creator personal brands, nightlife/spirits launches, luxury reveals, editorial features

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#1a0510` | Deep Dark Plum | Slide background |
| ██████ `#ff6496` | Neon Pink | Primary accent, script highlights, CTA |
| ██████ `#f0e8f0` | Pale Lilac | All body text |
| ██████ `#2d0820` | Dark Plum | Card surfaces |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| DM Serif Display | 400 Italic | ~50–70pt titles / ~33–45pt headings | Display headlines — elegant, nocturnal |
| Inter | 300–400 | ~15–20pt body / ~13–15pt captions | Body text, labels |

*Source: Google Fonts*


---

## #39 · Playful

> Warm, rounded, and approachable. Indie and human.

**Scheme:** Light · **Formality:** Low · **Density:** Medium
**Best for:** Creator portfolios, indie product launches, lifestyle brands, small-business pitches, newsletters

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f0fff4` | Mint Wash | Slide background |
| ██████ `#0a7040` | Forest Green | Primary accent, CTA |
| ██████ `#2d3d30` | Dark Forest | All text |
| ██████ `#c8f0d8` | Pale Mint | Card fills, accent-dim |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Manrope | 800 ExtraBold | ~50–70pt titles / ~33–45pt headings | Display headlines — clean, powerful |
| Space Grotesk | 400–500 | ~15–20pt body / ~13–15pt captions | Body text, card labels, captions |

*Source: Google Fonts*


---

## #40 · Raw Grid

> Direct and graphic-confident. No-nonsense layouts built on a visible grid.

**Scheme:** Light · **Formality:** Medium-Low · **Density:** High
**Best for:** Founder pitches, accelerator demos, brand decks, stat slides, comparison tables

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f8f8f8` | Near-White | Slide background |
| ██████ `#e82020` | Raw Red | Primary accent, grid markers, CTA |
| ██████ `#111111` | Near-Black | All text, thick borders |
| ██████ `#ffe8e8` | Pale Red | Card fills, accent-dim |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Bebas Neue | 400 | ~50–70pt titles / ~33–45pt headings | All display text — condensed, raw uppercase |
| Space Grotesk | 400–600 | ~15–20pt body / ~13–15pt captions | Body text, grid labels, data annotations |

*Source: Google Fonts*


---

## #41 · Retro Windows

> Knowingly nostalgic. Early OS aesthetic with a winking sense of humor.

**Scheme:** Light · **Formality:** Low · **Density:** Medium
**Best for:** Retro gaming, Y2K brands, tech-history talks, deliberately tongue-in-cheek decks

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#c0c0c0` | Classic Silver Gray | Slide background, window chrome |
| ██████ `#000080` | Classic Navy | Title bars, primary accent |
| ██████ `#ffffff` | White | Window interiors, body text areas |
| ██████ `#ff0000` | Classic Red | Close/warning elements |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| VT323 | 400 | ~50–70pt titles / ~33–45pt headings | Display text — pixel/bitmap terminal style |
| Press Start 2P | 400 | ~13–15pt | UI chrome, window labels — 8-bit style |
| Courier New | 400 | ~15–18pt body | Body text inside 'window' panes |

*Source: Google Fonts · System fonts*


---

## #42 · Retro Zine

> Printed, lo-fi, and crafted. Riso-print warmth.

**Scheme:** Light · **Formality:** Medium-Low · **Density:** Medium
**Best for:** Indie zines, music/arts brands, creator portfolios, small-batch craft, community decks

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f5f0e0` | Aged Paper | Slide background |
| ██████ `#e8430a` | Riso Orange-Red | Primary accent, headline highlight |
| ██████ `#1a1a1a` | Near-Black | All text |
| ██████ `#2244aa` | Riso Blue | Secondary accent, offset print effect |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Bebas Neue | 400 | ~50–70pt titles / ~33–45pt headings | Masthead and zine-style headlines — bold, condensed |
| Space Grotesk | 400–600 | ~15–20pt body / ~13–15pt captions | Body text, cut-and-paste labels |

*Source: Google Fonts*


---

## #43 · Sakura Chroma

> Vintage Japanese cassette packaging. Bold color, condensed type, tactile product-catalogue feel.

**Scheme:** Light · **Formality:** Low · **Density:** Medium
**Best for:** Indie hardware brands, music releases, analog studio retrospectives, kawaii-tech launches, zines

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#fef9ec` | Warm Ivory | Slide background |
| ██████ `#cc8800` | Cassette Gold | Primary accent, label color |
| ██████ `#ff4488` | Sakura Pink | Secondary accent, rainbow ribbon |
| ██████ `#44ccff` | Sky Cyan | Tertiary accent |
| ██████ `#1a1a1a` | Near-Black | All text |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Big Shoulders Display | 700–900 | ~50–70pt titles / ~33–45pt headings | Display headlines — ultra-condensed, cassette aesthetic |
| Albert Sans | 400–600 | ~15–20pt body | Body text, product labels |
| JetBrains Mono | 400 | ~13–15pt captions | Technical labels, serial-number style captions |

*Source: Google Fonts · Fontshare*


---

## #44 · Scatterbrain

> Post-it notes in Caveat handwriting. Feels like a designer's whiteboard.

**Scheme:** Light · **Formality:** Low · **Density:** High
**Best for:** Brainstorms, workshops, creative credentials, design-thinking sessions, ideation pitches

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#fffce8` | Pale Yellow | Slide background |
| ██████ `#887800` | Dark Yellow | Primary accent, border lines |
| ██████ `#ffee44` | Bright Yellow | Post-it fill |
| ██████ `#ff8844` | Orange | Secondary post-it color |
| ██████ `#1a1a1a` | Near-Black | Handwriting text |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Shrikhand | 400 | ~50–70pt titles / ~33–45pt headings | Display headlines — bold ink, personality-driven |
| Zilla Slab | 400 | ~15–20pt body / ~13–15pt captions | Body text — slightly editorial, post-it feel |

*Source: Google Fonts*


---

## #45 · Signal

> Quietly authoritative. Navy and gold for board-level trust.

**Scheme:** Mixed · **Formality:** High · **Density:** High
**Best for:** Investor decks, board presentations, consulting deliverables, legal/policy briefs

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f8faff` | Pale Blue-White | Light slide background |
| ██████ `#1e2d5a` | Deep Navy | All text, dark slide background |
| ██████ `#b8960a` | Antique Gold | Primary accent, rule lines, CTA |
| ██████ `#e8edf8` | Pale Blue | Card fills |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Source Serif 4 | 400–700 | ~50–70pt titles / ~33–45pt headings | Display headlines, board-level authority |
| IBM Plex Mono | 400 | ~13–15pt captions | Data annotations, reference labels |
| DM Sans | 400–500 | ~15–20pt body | Body text, table copy |

*Source: Google Fonts*


---

## #46 · Soft Editorial

> Literary, elegant, and unhurried. Sunday-supplement warmth.

**Scheme:** Light · **Formality:** High · **Density:** Low
**Best for:** Editorial features, longform brand stories, gallery decks, advisory deliverables, founder essays

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#fef8f2` | Warm Parchment | Slide background |
| ██████ `#b46040` | Warm Terracotta | Primary accent, CTA, pull-quote mark |
| ██████ `#2d2018` | Dark Umber | All headings, body text |
| ██████ `#e8c8a8` | Warm Sand | Card fills, dividers |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Cormorant Garamond | 400–700 Italic | ~50–70pt titles / ~33–45pt headings | Display headlines, pull quotes — literary serif |
| Work Sans | 400–500 | ~15–20pt body / ~13–15pt captions | Body text, labels, captions |

*Source: Google Fonts*


---

## #47 · Stencil & Tablet

> Archival, tactile, and weighty-graphic. Feels like a field manual.

**Scheme:** Light · **Formality:** Medium-High · **Density:** Medium
**Best for:** Museums, cultural institutions, art/architecture brands, longform research, manifestos

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#f5f2ea` | Bone Paper | Slide background |
| ██████ `#6a5028` | Dark Ochre | Primary accent, stencil elements, rule lines |
| ██████ `#1e1a10` | Deep Warm Black | All text |
| ██████ `#d8cdb0` | Aged Parchment | Card fills, texture areas |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Stardos Stencil | 400–700 | ~50–70pt titles / ~33–45pt headings | Display headlines — archival stencil aesthetic |
| Bowlby One | 400 | ~33–45pt sub-headings | Section sub-headings, tablet labels |
| Noto Serif SC | 400 | ~15–20pt body / ~13–15pt captions | Body text, footnotes |

*Source: Google Fonts*


---

## #48 · Studio

> Electric yellow on pure black. The slide *is* the brand statement.

**Scheme:** Dark · **Formality:** Medium · **Density:** Medium
**Best for:** Studio credentials, creative agency pitches, brand showcases, fashion/sneaker work

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#0a0a0a` | Pure Black | All slide backgrounds |
| ██████ `#FFD600` | Electric Yellow | Primary accent, headline highlight, CTA |
| ██████ `#f5f5f5` | Near-White | All body text |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Barlow | 700–800 | ~50–70pt titles / ~33–45pt headings | Display headlines — clean, contemporary studio feel |
| IBM Plex Mono | 400–600 | ~15–18pt body / ~13–15pt captions | Body text, labels — monospace adds craft precision |

*Source: Google Fonts*


---

## #49 · Vellum

> Scholarly, literary, and quietly intelligent. Navy canvas with Cormorant serifs.

**Scheme:** Dark · **Formality:** High · **Density:** Low
**Best for:** Research synthesis, white papers, academic briefs, advisory deliverables, longform editorial

### Colors
| Swatch | Hex | Name | Used On |
|--------|-----|------|---------|
| ██████ `#0d1b2a` | Deep Navy | All slide backgrounds |
| ██████ `#c8a96e` | Warm Gold | Primary accent, CTA, decorative marks |
| ██████ `#e8e4d8` | Warm Parchment | All body text, headings |
| ██████ `#1e3048` | Navy Surface | Card fills, panel backgrounds |


### Typography

| Font | Weight | Size Range (pt @ 1280px) | Applied To |
|------|--------|--------------------------|------------|
| Cormorant Garamond | 400–600 Italic | ~50–70pt titles / ~33–45pt headings | Display headlines — scholarly, literary authority |
| DM Sans | 400–500 | ~15–20pt body | Body text, labels |
| Courier Prime | 400 | ~13–15pt captions | Footnotes, citations, reference annotations |

*Source: Google Fonts*


---

# PART 4 — SHARED TYPOGRAPHY SCALE

*All design systems use the same font size scale at the 1920×1080 stage. Sizes below are the recommended defaults and their approximate point equivalent when viewed on a 1280px-wide screen.*

**Absolute minimum: 12pt rendered at any screen size. This equals 24px at stage size.**

| Text Role | Stage Size (px) | Approx. pt at 1280px | Notes |
|-----------|----------------|----------------------|-------|
| Cover / closing title | 96–112px | ~50–59pt | Max 2 lines |
| Slide title (h2) | 64–72px | ~34–38pt | Max 2 lines |
| Sub-heading (h3) | 44–52px | ~23–27pt | |
| Eyebrow / label | 26–28px | ~14–15pt | Uppercase, letter-spaced |
| Body / paragraph | 28–32px | ~15–17pt | Line-height 1.55 |
| Bullets / list items | 26–30px | ~14–16pt | |
| Captions / footnotes | 24–26px | ~13–14pt | Minimum floor |
| Stat numbers | 100–120px | ~53–63pt | Count-up animation |
| Stat suffix (M, %, ×) | 42–48px | ~22–25pt | |
| Stat label | 26–28px | ~14–15pt | |
| Code body | 24–26px | ~13–14pt | Monospace, line-height 1.68 |
| Agenda numbers | 48–56px | ~25–29pt | Display font |
| Quote text | 48–56px | ~25–29pt | |
| Timeline labels | 24–26px | ~13–14pt | Minimum floor |
| Chart axis / legend | 24–26px | ~13–14pt | Set in Chart.js options |

*If content cannot fit at these sizes without overflow → split into a new slide. Never shrink below floor.*

---

# PART 5 — QUICK SELECTION MATRIX

*Use this to match a brief to a style at a glance.*

| Situation | Recommended Styles |
|-----------|-------------------|
| Safe default for any deck | Brand |
| Tech talk, developer audience | Dark (Midnight), Terminal Green, Neon Cyber, Creative Voltage |
| Executive / board-level | Light (Serenity), Signal, Vellum, Cartesian, Monochrome |
| Creative agency / design studio | Bold Signal, Electric Studio, Studio, Creative Mode, Neo-Grid Bold |
| Startup pitch / investor | Brand, Blue Professional, Bold Poster, Raw Grid |
| Editorial / literary | Paper & Ink, Soft Editorial, Vintage Editorial, Biennale Yellow, Broadside |
| Playful / workshop | Scatterbrain, Daisy Days, Playful, Split Pastel, Pastel Geometry |
| Luxury / fashion | Dark Botanical, Pink Script, Emerald Editorial, Coral, Mat |
| Research / academic | Cobalt Grid, Monochrome, Vellum, Cartesian, Signal |
| Cultural / arts institution | Notebook Tabs, Biennale Yellow, Stencil & Tablet, Grove, Editorial Forest |
| Activist / mission-driven | People's Platform, Broadside, Bold Poster |
| Developer / hacker | Terminal Green, 8-Bit Orbit, Neon Cyber, Retro Windows |
| Handcrafted / indie | Scatterbrain, Retro Zine, Pin & Paper, Sakura Chroma, Capsule |

---

*Style Guide version: html-slides-advanced v4 · Palette source: https://coolors.co/palettes*
