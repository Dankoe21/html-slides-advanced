---
name: html-slides-advanced
description: Create stunning, animation-rich HTML presentations with 12 canonical slide formats, Visual QA, and a full library of design systems. Use when the user wants to build a presentation or create slides for a talk, pitch, or tutorial. Asks clarifying questions before any generation begins — this is required and must never be skipped.
---

# HTML Slides Advanced

Create zero-dependency, animation-rich HTML presentations that run entirely in the browser.
Single HTML file. No npm, no build tools, no frameworks.

---

## Core Principles

1. **Zero Dependencies** — Single HTML files with all CSS/JS inline.
2. **Always Ask First** — Phase 1 questions are mandatory before any slide generation. Never skip or shortcut them.
3. **Distinctive Design** — No generic AI defaults. Every deck must feel crafted for the brief. Vary fonts, palette, and layout. Reference https://coolors.co/palettes for palette ideas.
4. **Fixed 16:9 Stage (NON-NEGOTIABLE)** — Every deck uses a 1920×1080 canvas scaled uniformly to the viewport. Never reflow slide content for device.
5. **12 Canonical Formats** — Use a variety of the 12 layout formats in `FORMATS.md`. Never repeat the same layout on consecutive slides. Bullets on at most one-third of slides.
6. **Calibrated Copy** — Slide density is set by presentation type and audience mode. Slides should never read like a document.
7. **Visual QA (REQUIRED)** — Render PNGs and inspect with a subagent after generation. Never deliver without QA.
8. **Memory (REQUIRED)** — Read `memory.md` before beginning any session. Scan each entry for lessons that suggest an improvement to the skill itself (a missing rule, a recurring bug, a better default). If any are found, surface them to the user before proceeding — one sentence per item, flagged clearly. Append a 2–3 sentence entry after every meaningful session. Newest entry on top.

---

## Design Aesthetics

Actively resist generic AI convergence:

- **Typography:** Choose fonts that are distinctive and appropriate to the style. Avoid Inter, Roboto, Arial, or system fonts as display type. Use Google Fonts or Fontshare.
- **Color:** Commit fully to the chosen design system's palette. Use CSS variables for consistency throughout.
- **Motion:** Match animation character to style mood and content. See `ANIMATION-TOOLKIT.md`.
- **Backgrounds:** Create atmosphere with gradients, patterns, or contextual effects — not flat solids.

**Never use:**
- Accent lines or decorative bars under titles
- Centered body text
- The same bullet-list layout on consecutive slides
- Gratuitous glassmorphism without purpose
- Copy that reads like a document

---

## Fixed Stage Rules (Non-Negotiable)

- Every deck has a viewport wrapper filling the browser window.
- Every slide is authored inside a fixed **1920×1080** stage.
- Stage scales uniformly to fit viewport. No content reflow for device size.
- Slide visibility uses `.active`/`.visible` with `visibility`, `opacity`, `pointer-events`. **Never `display:none/block`** for switching.
- `clamp()` only outside the stage (nav dots).
- **Never negate CSS functions directly** — use `calc(-1 * clamp(...))`.
- Always include `prefers-reduced-motion` support.

**Paste full `viewport-base.css` contents into every deck.**

---

## Content Calibration

### Step 1: Presentation Type → Base depth

| Type | Sentences per body slide |
|------|--------------------------|
| High-level overview / pitch | 1–2 sentences or 2–3 bullets |
| Conference talk / keynote | 2–3 sentences or 3–4 bullets |
| Internal business update | 3–5 sentences or 4–6 bullets |
| Educational / tutorial | 4–7 sentences or structured steps |
| Technical / design deep-dive | 5–8 sentences, code blocks, diagrams |
| Report / handout | 5–8 sentences, tables, grids |

### Step 2: Audience Mode → Modifier

| Mode | Effect |
|------|--------|
| Live audience | Subtract 1–2 sentences — speaker fills the gap |
| Async / self-study | Add 1–2 sentences — content must stand alone |
| Mixed | Use base depth as-is |

### Step 3: Hard limits (always apply)

- Max 8 sentences or 6 bullets per slide. More → split into two slides.
- No paragraph blocks. Copy must be scannable.
- One idea per visual element.
- Never shrink font to fit. Split instead.
- **No card, grid item, or content block may be cut off by the slide boundary.** If a layout does not fit completely within 1920×1080 at the required font sizes, split the content across two slides. Reducing font size, padding, or spacing to avoid a split is not permitted.

---

## Phase 0: Detect Mode

- **Mode A: New Presentation** — From scratch. Go to Phase 1.
- **Mode C: Enhancement** — Read existing HTML, understand it, enhance carefully. Never add content that causes overflow — split instead.

---

## Phase 1: Questions (MANDATORY — never skip)

**Ask ALL questions in one message before doing anything else.**

---

**Q1 — Content:** Do you have content ready?
- `All content ready — I'll paste it`
- `Rough notes — help me shape them`
- `Topic only — help me outline it`

---

**Q2 — Length:** How many slides?
- `Short (5–8)` / `Medium (10–15)` / `Long (20+)`

---

**Q3 — Type:** What kind of presentation is this?
- `High-level overview / pitch`
- `Conference talk`
- `Educational / tutorial`
- `Technical or design deep-dive`
- `Internal business update`
- `Report or handout`

---

**Q4 — Audience:** How will people experience it?
- `Live — I'm presenting to a room`
- `Async — people read it on their own`
- `Mixed — I present it live, then share it`

---

**Q5 — Design system:** Choose your visual style. All 49 are available — type the number or name.

---

> ┌─────────────────────────────────────────────────────────────┐
> │  ★  CORE STYLES — Start here. Fully specified, always work. │
> └─────────────────────────────────────────────────────────────┘

| # | Colors | Name | Feel | Best For |
|---|--------|------|------|----------|
| **1** | `#FBEFD9` `#100202` `#D30B00` | **Brand** *(default)* | Warm editorial. Cream paper, near-black ink, sharp red. Serif + clean sans. | Pitches, product decks, conference talks, creator content, personal brand |
| **2** | `#000000` `#14213D` `#FCA311` | **Dark** — *Midnight Gold Sparkle* | Pure black, deep navy, warm amber. Bold, high-contrast, contemporary. | Tech talks, developer audiences, product launches, AI/data topics |
| **3** | `#EFF6EE` `#273043` `#9197AE` | **Light** — *Minimalist Serenity* | Soft sage, deep slate, muted silver. Calm, refined, trustworthy. | Executive, investor, healthcare, finance, board-level, strategy |

---

> ┌──────────────────────────────────────────────────────────┐
> │  ADDITIONAL STYLES (#4–49)                               │
> └──────────────────────────────────────────────────────────┘

| # | Colors | Name | Feel | Best For |
|---|--------|------|------|----------|
| 4 | `#1a1a1a` `#FF5722` `#ffffff` | **Bold Signal** | Dark gradient, bold orange focal card, large section numbers. | Agency credentials, startup pitches, design reviews, founder keynotes |
| 5 | `#0a0a0a` `#ffffff` `#4361ee` | **Electric Studio** | Split dark/white panel, strong typographic presence. | Product launches, investor pitches, brand showcases, keynotes |
| 6 | `#0066ff` `#1a1a2e` `#d4ff00` | **Creative Voltage** | Electric blue, neon yellow, halftone textures. Energized. | Creative agencies, developer tools, hackathons, AI products |
| 7 | `#0f0f0f` `#d4a574` `#e8b4b8` | **Dark Botanical** | Very dark, soft blurred gradient blobs. Elegant, gallery feel. | Luxury, fashion, galleries, wellness, premium B2B |
| 8 | `#f8f6f1` `#2d2d2d` `#98d4bb` `#c7b8ea` | **Notebook Tabs** | Cream paper card on dark, colorful editorial tabs on right edge. | Annual reports, conference programs, editorial content |
| 9 | `#c8d9e6` `#faf9f7` `#f0b4d4` `#a8d4c4` | **Pastel Geometry** | White card on pastel bg, rounded vertical pills. Friendly, organized. | Lifestyle, SaaS onboarding, education, community, wellness |
| 10 | `#f5e6dc` `#e4dff0` `#c8f0d8` `#f0f0c8` | **Split Pastel** | Two-color split bg, badge pills, grid accents. Playful. | Creator portfolios, DTC launches, beauty, wellness |
| 11 | `#f5f3ee` `#1a1a1a` `#e8d4c0` | **Vintage Editorial** | Warm cream, abstract geometric shapes, bold personality. | Brand manifestos, creative reviews, editorial pitches |
| 12 | `#0a0f1c` `#00ffcc` `#ff00aa` | **Neon Cyber** | Deep navy, cyan, magenta. Futuristic, techy, particle bg. | AI products, cybersecurity, gaming, developer tools |
| 13 | `#0d1117` `#39d353` | **Terminal Green** | GitHub dark, terminal green, monospace only, scan lines. | Developer talks, CLI tools, open source, hacker aesthetic |
| 14 | `#ffffff` `#000000` `#ff3300` | **Swiss Modern** | Pure white, pure black, red. Bauhaus grid, asymmetric. | Design talks, architecture, editorial, research |
| 15 | `#faf9f7` `#1a1a1a` `#c41e3a` | **Paper & Ink** | Warm cream, Cormorant Garamond serifs, crimson accent. Literary. | Editorial, cultural institutions, academic, advisory |

---



| # | Colors | Name | Feel | Best For |
|---|--------|------|------|----------|
| 16 | `#0a0514` `#00ffcc` `#ff00ff` | **8-Bit Orbit** | Pixel neon arcade on deep void. CRT screen at 2am. | Gaming, cyberpunk, web3, hackathons, synthwave, indie dev |
| 17 | `#f5f0dc` `#ffd700` `#1a1a1a` | **Biennale Yellow** | Solar yellow on warm parchment. Dutch editorial calm. | Arts institutions, design conferences, curatorial pitches |
| 18 | `#ffffff` `#000000` `#5544ff` `#ff55aa` `#aaff44` | **BlockFrame** | Neobrutalist, chunky black borders, pastel-neon blocks. | Indie SaaS, agency credentials, creative reviews |
| 19 | `#f8f6f1` `#0071e3` `#1a1a2e` | **Blue Professional** | Cream paper, cobalt blue. Modern, lightly authoritative. | B2B SaaS, consulting deliverables, advisory, investor reports |
| 20 | `#fff8f0` `#1a1a1a` `#D30B00` | **Bold Poster** | Minimal copy, maximum typographic presence. Magazine cover. | Brand manifestos, founder vision, editorial pitches |
| 21 | `#0c0c10` `#FF4500` `#f5f0e8` | **Broadside** | Dark editorial canvas, fire orange. Newspaper headline energy. | Brand manifestos, design talks, bilingual decks |
| 22 | `#fdf6f0` `#e05a20` `#2d2d2d` `#f0e0d0` | **Capsule** | Pill-shaped cards, warm bone, Y2K feel. | Lifestyle, DTC, beauty, wellness, creator portfolios |
| 23 | `#fafaf8` `#2c2c2c` `#8b7355` `#d4cdc4` | **Cartesian** | Quiet, warm-minimal, classical proportions. Restrained. | Investment theses, white papers, advisory, gallery decks |
| 24 | `#f8f9fa` `#1e50b4` `#1a1a2e` `#e8edf8` | **Cobalt Grid** | Design research bulletin. One strict cobalt accent. | Studio annuals, design research, architecture, art publications |
| 25 | `#fff5f0` `#e84030` `#1a1a1a` | **Coral** | Warm-graphic, bold coral accent on clean background. | Fashion, fitness, lifestyle brands, agency credentials |
| 26 | `#f8f8f6` `#ff3c00` `#1a1a1a` `#ffe8e0` | **Creative Mode** | Strong card layouts, expressive type and color. Design-led. | Creative agency pitches, design studio decks, ad credentials |
| 27 | `#fff9f0` `#ff8c42` `#4ecdc4` `#ffd93d` | **Daisy Days** | Friendly, warm, cheerful pastels. Rounded and joyful. | Educational, kids/family, wellness programs, workshops |
| 28 | `#f2f5f0` `#2d4a38` `#3d3d35` `#c8d8c0` | **Editorial Forest** | Quiet sage tones, considered literary mood. | Quarterly reviews, studio updates, creative agency recaps |
| 29 | `#f5f0e8` `#1a1a1a` `#c8956c` | **Editorial Tri-Tone** | Three deliberate tones, serif/sans contrast. Fashion magazine. | Fashion brands, lifestyle media, art direction reviews |
| 30 | `#f8fdf8` `#1a4a2a` `#1a1a1a` `#d0e8d4` | **Emerald Editorial** | Forest green masthead rule, serious editorial gravitas. | Leadership readouts, strategy briefings, product launches |
| 31 | `#f5f2ec` `#4a6741` `#2d2820` `#c8b89a` | **Grove** | Organic, earthy serif typography, botanical calm. | Sustainability, wineries, nature brands, advisory deliverables |
| 32 | `#faf8f3` `#c8651e` `#2d2520` `#f0e8d8` | **Long Table** | Warm, intimate, hospitality-forward. Single warm accent. | Restaurants, creative events, lifestyle, membership pitches |
| 33 | `#f0ebe3` `#c86428` `#1e1a14` `#d8cfc4` | **Mat** | Mid-century, tactile, intentional. Analog feel. | Design studios, architecture, interior brands, craft |
| 34 | `#fffef8` `#111111` `#e0e0d8` | **Monochrome** | Black and white only. Words are the only thing on the page. | Research, white papers, academic briefs, advisory |
| 35 | `#f5f5f3` `#2828c8` `#1a1a1a` `#e8e8ff` | **Neo-Grid Bold** | Confident, grid-structured, punchy typography. Editorial-graphic. | Design-led pitches, brand work, stat-heavy slides |
| 36 | `#fff8f8` `#cc2060` `#1a1a1a` `#ffe0ee` | **People's Platform** | Activist energy, bold block type. Honest and loud. | Manifestos, civic decks, mission statements |
| 37 | `#f8f5f0` `#8b6914` `#2d2520` `#e8e0d4` | **Pin & Paper** | Hand-crafted, warm, literary. Safety-pin aesthetic. | Qualitative research, brand stories, workshop debriefs |
| 38 | `#1a0510` `#ff6496` `#f0e8f0` `#2d0820` | **Pink Script — After Hours** | Nocturnal, luxe, moody. Script accents on dark. | Fashion, nightlife/spirits, luxury reveals, editorial |
| 39 | `#f0fff4` `#0a7040` `#2d3d30` `#c8f0d8` | **Playful** | Warm, rounded, approachable. Indie and human. | Creator portfolios, indie products, lifestyle, newsletters |
| 40 | `#f8f8f8` `#e82020` `#111111` `#ffe8e8` | **Raw Grid** | Direct, graphic-confident, no-nonsense layouts. | Founder pitches, accelerator demos, stat slides, comparisons |
| 41 | `#c0c0c0` `#000080` `#ffffff` `#ff0000` | **Retro Windows** | Nostalgic early OS aesthetic. Knowingly retro. | Retro gaming, Y2K brands, tech-history talks |
| 42 | `#f5f0e0` `#e8430a` `#1a1a1a` `#2244aa` | **Retro Zine** | Riso-print warmth, lo-fi crafted feel. | Indie zines, music/arts brands, community decks |
| 43 | `#fef9ec` `#cc8800` `#ff4488` `#44ccff` | **Sakura Chroma** | Vintage Japanese cassette packaging. Bold, tactile. | Indie hardware, music releases, kawaii-tech launches |
| 44 | `#fffce8` `#ffee44` `#ff8844` `#1a1a1a` | **Scatterbrain** | Post-it notes, Caveat handwriting, workshop feel. | Brainstorms, workshops, design-thinking, ideation |
| 45 | `#f8faff` `#1e2d5a` `#b8960a` `#e8edf8` | **Signal** | Deep navy, antique gold. Institutional, board-level trust. | Investor decks, board presentations, consulting deliverables |
| 46 | `#fef8f2` `#b46040` `#2d2018` `#e8c8a8` | **Soft Editorial** | Cormorant Garamond, warm paper, sage/blush. Literary. | Editorial features, gallery decks, advisory, founder essays |
| 47 | `#f5f2ea` `#6a5028` `#1e1a10` `#d8cdb0` | **Stencil & Tablet** | Bone paper, stencil headlines, six-color earth palette. | Museums, cultural institutions, art/architecture, manifestos |
| 48 | `#0a0a0a` `#FFD600` `#f5f5f5` | **Studio** | Electric yellow on pure black. The slide is the brand statement. | Studio credentials, creative agency, fashion, brand showcases |
| 49 | `#0d1b2a` `#c8a96e` `#e8e4d8` `#1e3048` | **Vellum** | Deep navy canvas, Cormorant serifs, warm gold. Scholarly. | Research synthesis, white papers, academic briefs, advisory |

Type the number (1–49) or style name. Default: `Brand` (style 1).

---

**Q6 — Animation level:** How animated should this feel?
- `Subtle — clean entrances, nothing distracting`
- `Moderate — purposeful motion, a few ambient effects`
- `Rich — full toolkit, looping effects, interactive depth`

---

**Q7 — Research:** Want me to research anything before drafting?
- `Yes, research the topic` / `Yes, let me specify what to search` / `No, just build it`

---

After all answers received:

**If user chose "All content ready"** — wait for paste before continuing.
**If research chosen** — search the web, summarize in 3–5 bullets, then continue.

**Calibration confirmation** — derive target depth from Content Calibration matrix and confirm in one line:
> *"Based on [type] for a [mode] audience, I'll aim for [X–Y sentences or bullets] per content slide."*

Ask: *"Does that sound right, or adjust?"* Wait for confirmation before proceeding to Phase 2.

---

## Phase 2: Outline

Produce a slide-by-slide outline before writing any HTML:

```
Slide 1:  Cover    — "[Title]" with tagline
Slide 2:  Agenda   — 3 sections
Slide 3:  Two-col  — "[Key point]" left, visual right
...
Slide N:  Closing  — "[Line]" + CTA
```

State the **format** (from the 12 canonical formats) and the **hero animation** for each slide.

Ask: *"Does this outline look right? Any changes before I build?"*

Wait for approval before writing any HTML.

---

## Phase 3: Generate HTML

**Read before writing any code:**
- `TYPOGRAPHY.md` — Type scale and hard floors ← READ FIRST
- `FORMATS.md` — HTML + CSS for all 12 layouts + JS controller
- `STYLES.md` — CSS variables for the chosen design system
- `ANIMATION-TOOLKIT.md` — Animation CSS/JS + per-format cheat sheet
- `viewport-base.css` — Paste full contents into every deck
- `html-template.md` — HTML architecture, JS features, inline editing, code quality

**If a bold template preset was chosen:** read that template's `design.md` from `bold-template-pack/templates/`. Treat it as the design recipe — preserve fonts, palette, decorative vocabulary, spacing rhythm. Translate to fixed 1920×1080 stage.

### Generation Rules

**Structure:**
- Single self-contained HTML file. All CSS and JS inline.
- Every slide: `<section class="slide [format-class]" data-slide="N">`
- First slide: add `active visible` classes.
- Paste full `viewport-base.css` in the `<style>` block.
- Include full `SlidePresentation` JS controller.
- Include full Animation Toolkit CSS.
- Add `/* === SECTION NAME === */` comments throughout.

**Typography (see TYPOGRAPHY.md for full rules):**
- Import from Google Fonts or Fontshare. Use `<link>` in `<head>` with `display=swap`.
- All font sizes in **fixed px** inside the stage — never `clamp()`, `vw`, or `%`.
- **24px minimum stage size** for every text element (= ≥12pt rendered at 1280px).
- Hard floors: body/bullets 26px · captions/labels 24px · code 24px · slide titles 52px · cover titles 80px · stat numbers 80px.
- Split slides rather than shrink fonts.

**Design:**
- Every slide has a visual element — text-only slides are not allowed.
- No accent lines under titles. No centered body text. No repeated consecutive layouts.
- **No content may be cut off or overflow the slide boundary.** If a grid, list, or card set does not fit at the required font sizes and spacing, split it across two slides. Never shrink content, reduce padding, or squeeze cards to make things fit. The split is always the right answer.

**Copy:**
- Apply the calibrated depth confirmed in Phase 1. Do not drift.
- Max 8 sentences or 6 bullets per slide. No paragraph blocks.

**Navigation (every deck):**
- Arrow keys, Space, scroll/swipe/touch. Nav dots on right edge.
- Slide transitions: clean fade in/out only. All animations apply freely within each slide.

**Inline editing (every deck):**
- Hotzone top-left + `E` key. JS-based hover with 400ms grace period.

---

## Phase 4: Save

Save to `output/slides/[deck-name].html` (kebab-case).
**Do NOT open yet** — run Visual QA first.

---

## Phase 5: Visual QA (REQUIRED — do not skip)

### Step 1 — Render

```bash
python3 skills/html-slides-advanced/render_slides.py \
  --html output/slides/<deck>.html \
  --out  output/slides/qa/
```

### Step 2 — Subagent inspection

Spawn a subagent with image paths + one-line expected note per slide:

```
Visually inspect these slide images. Assume there are issues — find them.
For each slide, list problems (even minor):
- Overlapping elements
- Text overflow or cut off at edges
- Images cropped or only partially visible
- Low-contrast text or icons
- Washed-out or faded images
- Mid-animation / half-faded captures
- Footers or labels colliding with content
- Uneven gaps (< 0.3") or insufficient margins (< 0.5")
- Columns not aligned
- Leftover placeholder text
- Copy density: bullets wrapping 3+ lines, more than 6 bullets per slide
- Font too small: body below ~14px rendered, captions below ~12px rendered
- Descender clipping: letters g, j, p, q, y with tails visibly cut at the bottom. Caused by line-height below 1.1 or overflow:hidden on a text container. Flag any letter tails that are sliced.
- Stat values showing zero: a stat grid where all numbers display as "0" means count-up JS did not fire — always flag.
- Content cut off at slide edges: any card, grid item, text block, or image partially outside the visible slide area.
Report ALL issues with the slide number. Clean slides: say so explicitly.

1. <path>/slide-01.png (Expected: <description>)
2. ...
```

### Step 3 — Fix and re-render

Fix every real issue. Re-render affected slides. Re-inspect. One fix can create another.

---

## Phase 6: Delivery

1. Clean up `output/slides/qa/`.
2. Open: `open output/slides/<deck>.html`
3. Tell user: location + QA summary, navigation (arrow keys / space / swipe), inline editing (hover top-left or press `E`), colors via `:root` CSS variables.
4. The deck is complete and ready to use in any browser.

---

## Supporting Files

| File | Purpose | When |
|------|---------|------|
| `TYPOGRAPHY.md` | Type scale, 24px floor, font loading, bug fixes | Phase 3 (first) |
| `FORMATS.md` | HTML + CSS for all 12 layouts + JS controller | Phase 3 |
| `STYLES.md` | All design system variables — 3 core + 12 presets | Phase 3 |
| `ANIMATION-TOOLKIT.md` | All animation CSS/JS, philosophy, per-format cheat sheet | Phase 3 |
| `viewport-base.css` | Fixed-stage CSS — paste into every deck | Phase 3 |
| `html-template.md` | HTML architecture, inline editing, image pipeline, code quality | Phase 3 |
| `bold-template-pack/selection-index.json` | Metadata for 34 bold template design systems | Phase 3 (if bold template chosen) |
| `bold-template-pack/templates/*/design.md` | Full design system for chosen bold template | Phase 3 (if bold template chosen) |
| `render_slides.py` | Headless Playwright renderer for QA | Phase 5 |
| `style-picker.html` | Visual swatch reference for all 49 design systems — share with user at Q5 | Phase 1 (Q5) |
| `memory.md` | Append-only QA and session log — read before editing, write after each session | Always |
