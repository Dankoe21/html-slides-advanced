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

**Q5 — Design system:** Choose your visual style.

**Core Styles** — polished, ready to use:

| | Name | Look & Feel | Colors |
|--|------|-------------|--------|
| 🟥⬛🟫 | **#1 · Brand** *(default)* | Warm editorial. Cream paper, near-black ink, sharp red accent. Serif headlines, clean sans body. | `#FBEFD9` · `#100202` · `#D30B00` |
| 🟧🟦⬛ | **#2 · Dark** | Bold and contemporary. Pure black with deep navy surfaces and warm amber accent. Geometric type. | `#000000` · `#14213D` · `#FCA311` |
| 🟩🩶⬜ | **#3 · Light** | Calm and minimalist. Soft sage background, slate text, silver midtones. Refined sans-serif. | `#EFF6EE` · `#273043` · `#9197AE` |

**Additional Style Presets** — more creative and expressive options:

| | Name | Look & Feel |
|--|------|-------------|
| ⬛🟥🟫 | **#4 · Bold Signal** | Dark gradient, bold colored card, large section numbers. High-impact. |
| ⬛🟦⬜ | **#5 · Electric Studio** | Split white/dark panel. Strong quote typography as hero. |
| 🟦⬛🟡 | **#6 · Creative Voltage** | Electric blue, neon yellow, halftone textures. Energized. |
| ⬛🟤🌸 | **#7 · Dark Botanical** | Deep dark with soft gradient circles. Elegant and artistic. |
| 🟫📄🎨 | **#8 · Notebook Tabs** | Cream paper card with colorful section tabs on right edge. |
| 🩶⬜🌸 | **#9 · Pastel Geometry** | White card on pastel, vertical pills. Friendly and organized. |
| 🍑🪻🌿 | **#10 · Split Pastel** | Two-color split background. Playful badges and grid accents. |
| 🟫⬜📐 | **#11 · Vintage Editorial** | Cream, geometric shapes, confident personality. Witty. |
| 🌐🟦💜 | **#12 · Neon Cyber** | Deep navy, cyan, magenta. Futuristic and techy. |
| ⬛🟩💻 | **#13 · Terminal Green** | GitHub dark, terminal green, monospace only. Developer. |
| ⬜⬛🟥 | **#14 · Swiss Modern** | White, black, red. Bauhaus-inspired, precise grid. |
| 🟫⬜🔴 | **#15 · Paper & Ink** | Warm cream, Cormorant Garamond, crimson. Literary. |
| ⬛🟡📰 | **#17 · Biennale Yellow** | Solar yellow editorial. Dutch poster energy. |
| ⬛🟠📋 | **#21 · Broadside** | Newspaper editorial on dark. Fire orange accent. |
| ⬛💜🌙 | **#38 · Pink Script — After Hours** | Nocturnal and moody. Script accents. |
| ⬛🟡🎬 | **#48 · Studio** | Electric yellow on pure black. High voltage creative. |
| 🌑🟤📚 | **#49 · Vellum** | Navy canvas, Cormorant serifs. Scholarly and advisory. |
| 🎮🟦💫 | **#16 · 8-Bit Orbit** | Pixel neon arcade aesthetic. Retro-tech. |
| 🟡🔵📐 | **#35 · Neo-Grid Bold** | Confident, punchy, grid-structured. |
| 🌸⬜🎭 | **#27 · Daisy Days** | Cheerful, playful, light and warm. |
| 🟩🟫📖 | **#28 · Editorial Forest** | Quiet editorial, sage tones, mixed scheme. |
| 🟤🟫🌿 | **#30 · Emerald Editorial** | Warm editorial, considered, medium formality. |
| 🌿🟢📋 | **#31 · Grove** | Organic and considered. |
| 🟫🟠🏺 | **#47 · Stencil & Tablet** | Bone paper, stencil headlines, earthy. |
| 🌸🎌🌈 | **#43 · Sakura Chroma** | Vintage Japanese cassette aesthetic. |
| 📝💛🗂 | **#44 · Scatterbrain** | Post-it notes, handwriting, workshop feel. |
| 🌿💚💛 | **#39 · Playful** | Warm, rounded, approachable. |
| ⚓🟦🟡 | **#45 · Signal** | Navy and gold, institutional, board-level trust. |
| 🌸📖🍋 | **#46 · Soft Editorial** | Cormorant Garamond, sage, blush, lemon. Literary. |
| 🟧⬜🎭 | **#22 · Capsule** | Pill-shaped cards, warm bone, pastel pop. |
| 🟦⬜📊 | **#24 · Cobalt Grid** | Design research, editorial, structured. |
| 🟧⬛🌊 | **#25 · Coral** | Bold warm, mixed scheme, confident. |
| ❤️🟥🗣 | **#36 · People's Platform (Block & Bold)** | Activist, bold block type, loud. |
| 📌🟫🗺 | **#37 · Pin & Paper** | Crafted, handmade, pinboard aesthetic. |
| 🟪🟦🟥 | **#18 · BlockFrame** | Neobrutalist, pastel neon, chunky borders. |
| 🟫⬜🔲 | **#32 · Long Table** | Warm, intimate, medium formality. |
| 🌏🟤🟢 | **#33 · Mat** | Warm-modern, considered. |
| ⬛📖🔤 | **#34 · Monochrome** | Restrained, literary, black/white only. |
| 🟫🎸🟡 | **#41 · Retro Windows** | Nostalgic, retro OS aesthetic. |
| 📰🟤✂️ | **#42 · Retro Zine** | Crafted, lo-fi, cut-and-paste energy. |

Options: Type the name, or `Brand` for default.

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
