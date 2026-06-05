# Slide Styles Reference

The **Brand** style is the default — use it unless the user asks for another. Every style is a complete skin over the same 12 format templates. All formats use only the shared CSS token contract — never hardcoded colors.

**For style inspiration and additional palettes:** https://coolors.co/palettes

**Format contract** — every style must define these tokens:
`--bg-primary` `--text-primary` `--text-secondary` `--accent` `--accent-dim` `--on-accent` `--surface` `--border` `--font-title` `--font-body`

**All styles must support all 12 formats.** When adding or changing a format, verify it renders correctly under Brand, Dark (Midnight Sun), and Light (Minimalist Serenity).

---

## Style Selection Rules

- **Brand** = default. Use it unless the user explicitly says Dark, Light, or names another style.
- If user says "you pick" → use Brand.
- For style previews: generate a single-slide HTML preview per style in `output/slide-previews/`, open them, ask which they prefer, then continue.
- For custom styles: start from https://coolors.co/palettes, derive tokens, document the palette source URL.

---

## #1 · Brand (Default)

Warm "paper" content slides, near-black "ink" title/closing slides, one sharp red accent. Editorial and premium, not corporate. Crimson Pro + Manrope.

**Font import:**
```html
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
```

**CSS Variables:**
```css
:root {
  /* Palette */
  --red:   #D30B00;
  --ink:   #100202;
  --paper: #FBEFD9;

  /* Format contract — content slides */
  --bg-primary:     var(--paper);
  --text-primary:   var(--ink);
  --text-secondary: rgba(16, 2, 2, 0.60);
  --accent:         var(--red);
  --accent-dim:     rgba(211, 11, 0, 0.10);
  --border:         rgba(16, 2, 2, 0.14);
  --surface:        #ffffff;
  --on-accent:      #ffffff;

  --font-title: 'Crimson Pro', Georgia, serif;
  --font-body:  'Manrope', -apple-system, Arial, sans-serif;
}

/* Dark slides: cover + closing */
.slide--dark {
  --bg-primary:     #100202;
  --text-primary:   #FBEFD9;
  --text-secondary: rgba(251, 239, 217, 0.55);
  --border:         rgba(251, 239, 217, 0.14);
  --surface:        rgba(255, 255, 255, 0.07);
  --accent-dim:     rgba(211, 11, 0, 0.20);
}
```

**Signature elements:**
- Paper `#FBEFD9` on ~65% of slides. Never use white as the main slide bg.
- Spark mark (4-point star SVG) on cover and closing only.
- One italic red word per headline — carries voice and emphasis.
- Crimson Pro for all titles, headers, large numbers.
- Manrope for body text, labels, UI chrome.
- `--red` only for: spark, one accent word, active agenda item, CTA, chart fill, NOW marker. Never decorative.

**Required shadow overrides (use --red, not generic blue):**
```css
.agenda-item.active     { box-shadow: 0 14px 36px rgba(211,11,0,.14); }
.tl-marker              { box-shadow: 0 12px 30px rgba(211,11,0,.22); }
.tl-step.now .tl-marker { box-shadow: 0 12px 30px rgba(211,11,0,.22), 0 0 0 4px rgba(211,11,0,.14); }
.portrait-card          { background: linear-gradient(145deg,rgba(211,11,0,.06),rgba(211,11,0,.16)); }
```

---

## #2 · Dark — "Midnight Sun Fun"

Source: https://coolors.co/palettes — Midnight Sun Fun
Palette: `#000000` · `#14213D` · `#FCA311`

Pure black with deep navy depth and warm amber accent. Bold, contemporary, high contrast. Great for tech talks, product launches, developer audiences.

**Font import:**
```html
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;1,9..40,400&display=swap" rel="stylesheet">
```

**CSS Variables:**
```css
:root {
  /* Palette — Midnight Sun Fun */
  --midnight-black: #000000;
  --midnight-navy:  #14213D;
  --midnight-amber: #FCA311;

  /* Format contract */
  --bg-primary:     #000000;
  --text-primary:   #F5F0E8;
  --text-secondary: rgba(245, 240, 232, 0.55);
  --accent:         #FCA311;
  --accent-dim:     rgba(252, 163, 17, 0.12);
  --border:         rgba(245, 240, 232, 0.12);
  --surface:        #14213D;
  --on-accent:      #000000;

  --font-title: 'Archivo Black', -apple-system, Arial, sans-serif;
  --font-body:  'DM Sans', -apple-system, Arial, sans-serif;
}

/* Dark slides: cover + closing — navy bg for depth */
.slide--dark {
  --bg-primary:  #14213D;
  --surface:     rgba(252, 163, 17, 0.06);
  --border:      rgba(252, 163, 17, 0.20);
  --accent-dim:  rgba(252, 163, 17, 0.16);
}
```

**Signature elements:**
- Pure black `#000000` on content slides; deep navy `#14213D` on cover/closing.
- Amber `#FCA311` accent — spark, ONE highlight word, CTA, stat numbers, active states.
- Archivo Black 400 for all display text (bold, geometric, strong).
- DM Sans for body.
- Navy `#14213D` used as card/surface color on dark slides — creates depth layers.
- Chart bars: amber tint ramp (`#FCA311` full → `rgba(252,163,17,.65)` → `rgba(252,163,17,.30)`).
- Code card: same `#1d1d1f` dark; amber replaces red on cursor and prompt.

**Shadow overrides:**
```css
.agenda-item.active     { box-shadow: 0 14px 36px rgba(252,163,17,.14); border-color: var(--accent); }
.tl-marker              { box-shadow: 0 12px 30px rgba(252,163,17,.28); background: var(--accent); color: var(--on-accent); }
.tl-step.now .tl-marker { box-shadow: 0 12px 30px rgba(252,163,17,.28), 0 0 0 4px rgba(252,163,17,.16); }
.portrait-card          { background: linear-gradient(145deg,rgba(252,163,17,.06),rgba(252,163,17,.18)); border-color: rgba(252,163,17,.25); }
.pulse { animation: pulse-midnight 2.2s ease-in-out infinite; }
@keyframes pulse-midnight {
  0%,100% { box-shadow: 0 12px 30px rgba(252,163,17,.28), 0 0 0 0 rgba(252,163,17,0); }
  50%     { box-shadow: 0 12px 30px rgba(252,163,17,.28), 0 0 0 14px rgba(252,163,17,.12); }
}
```

---

## #3 · Light — "Minimalist Serenity"

Source: https://coolors.co/palettes — Minimalist Serenity
Palette: `#273043` · `#9197AE` · `#EFF6EE`

Cool slate with soft sage and muted silver. Calm, refined, trustworthy. Best for executive presentations, investor decks, healthcare, finance, strategy reviews.

**Font import:**
```html
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

**CSS Variables:**
```css
:root {
  /* Palette — Minimalist Serenity */
  --serenity-dark:   #273043;
  --serenity-silver: #9197AE;
  --serenity-sage:   #EFF6EE;

  /* Format contract */
  --bg-primary:     #EFF6EE;
  --text-primary:   #273043;
  --text-secondary: #9197AE;
  --accent:         #273043;
  --accent-dim:     rgba(39, 48, 67, 0.08);
  --border:         rgba(145, 151, 174, 0.30);
  --surface:        #FFFFFF;
  --on-accent:      #EFF6EE;

  --font-title: 'Plus Jakarta Sans', -apple-system, Arial, sans-serif;
  --font-body:  'Plus Jakarta Sans', -apple-system, Arial, sans-serif;
}

/* Dark slides: cover + closing — deep slate bg */
.slide--dark {
  --bg-primary:     #273043;
  --text-primary:   #EFF6EE;
  --text-secondary: rgba(239, 246, 238, 0.60);
  --border:         rgba(145, 151, 174, 0.25);
  --surface:        rgba(145, 151, 174, 0.12);
  --accent:         #EFF6EE;
  --accent-dim:     rgba(239, 246, 238, 0.10);
  --on-accent:      #273043;
}
```

**Signature elements:**
- Sage `#EFF6EE` on content slides — not stark white, a breath of outdoor calm.
- Deep slate `#273043` as accent on light slides; sage `#EFF6EE` as accent on dark slides.
- Silver `#9197AE` for secondary text, borders, dividers — the palette's mid-tone workhorse.
- Plus Jakarta Sans across the board — 800 for display, 400–600 for body. Refined but not fussy.
- No decorative glow effects — clean borders and soft shadows only.
- Chart bars: slate tint ramp (`#273043` full → `rgba(39,48,67,.60)` → `rgba(39,48,67,.25)`).
- Code card: same `#1d1d1f` dark; silver `#9197AE` for comments, sage for prompts.
- Stat numbers: slate `#273043` (not a bright accent — this style is restrained).

**Shadow overrides:**
```css
.agenda-item.active     { box-shadow: 0 14px 36px rgba(39,48,67,.12); border-color: var(--accent); }
.tl-marker              { box-shadow: 0 12px 30px rgba(39,48,67,.20); background: var(--accent); color: var(--on-accent); }
.tl-step.now .tl-marker { box-shadow: 0 12px 30px rgba(39,48,67,.20), 0 0 0 4px rgba(39,48,67,.12); }
.portrait-card          { background: linear-gradient(145deg,rgba(39,48,67,.05),rgba(39,48,67,.14)); border-color: rgba(145,151,174,.30); }
.bento-card:hover       { box-shadow: 0 8px 32px rgba(39,48,67,.10); }
.pulse { animation: pulse-serenity 2.2s ease-in-out infinite; }
@keyframes pulse-serenity {
  0%,100% { box-shadow: 0 12px 30px rgba(39,48,67,.20), 0 0 0 0 rgba(39,48,67,0); }
  50%     { box-shadow: 0 12px 30px rgba(39,48,67,.20), 0 0 0 14px rgba(39,48,67,.10); }
}
```

---

## Additional Style Presets

These presets are available for creative, expressive decks. They can be selected directly during Phase 1 (Q5), or suggested when the user asks for something beyond the three core styles.

Generate a deck that honors each preset's design DNA — fonts, palette, decorative vocabulary, spacing rhythm — while using the 12 canonical format structures as content scaffolding.

### Bold Signal
Dark gradient, colored card focal point, large section numbers. Archivo Black + Space Grotesk.
Palette: `#1a1a1a` bg, `#FF5722` card, `#ffffff` text.

### Electric Studio
Split panel white/blue. Strong quote typography as hero. Manrope 800 throughout.
Palette: `#0a0a0a` dark, `#4361ee` accent, `#ffffff` light.

### Creative Voltage
Electric blue + neon yellow, halftone textures. Archivo Black + Space Mono.
Palette: `#0066ff` primary, `#1a1a2e` dark, `#d4ff00` neon.

### Dark Botanical
Centered content, abstract soft gradient circles, warm accent tones. Cormorant + IBM Plex Sans.
Palette: `#0f0f0f` bg, `#d4a574` warm, `#e8b4b8` pink.

### Notebook Tabs
Cream paper card on dark outer. Colorful editorial tabs on right edge. Bodoni Moda + DM Sans.
Palette: `#f8f6f1` page, `#2d2d2d` outer, multi-color tabs.

### Vintage Editorial
Cream bg, abstract geometric shapes, confident personality. Fraunces + Work Sans.
Palette: `#f5f3ee` cream, `#1a1a1a` ink, `#e8d4c0` warm.

### Terminal Green
Developer hacker aesthetic. JetBrains Mono only. Scan lines, blinking cursor.
Palette: `#0d1117` GitHub dark, `#39d353` terminal green.

### Swiss Modern
Bauhaus-inspired. Visible grid, asymmetric layouts. Archivo 800 + Nunito.
Palette: White, black, `#ff3300` red.

---

## Cross-Style Rules (All Styles)

```css
/* Code card always dark — overrides any style */
.code-slide .code-card { background: #1d1d1f !important; }

/* Stat numbers always in accent color */
.stat-number { color: var(--accent); }

/* Italic accent word */
.accent-word { color: var(--accent); font-style: italic; }

/* Spark mark uses accent fill */
.spark path { fill: var(--accent); }
```

---

## Style × Format Compatibility

Every cell must render correctly before delivering a deck.

| Format        | Brand | Dark | Light |
|--------------|-------|------|-------|
| Cover         | ✓ | ✓ | ✓ |
| Agenda        | ✓ | ✓ | ✓ |
| Two-column    | ✓ | ✓ | ✓ |
| Stat grid     | ✓ | ✓ | ✓ |
| Feature bento | ✓ | ✓ | ✓ |
| Comparison    | ✓ | ✓ | ✓ |
| Steps         | ✓ | ✓ | ✓ |
| Roadmap       | ✓ | ✓ | ✓ |
| Chart         | ✓ | ✓ | ✓ |
| Code block    | ✓ | ✓ | ✓ |
| Quote         | ✓ | ✓ | ✓ |
| Closing       | ✓ | ✓ | ✓ |

---

## Style Presets — Full Specifications

The 12 curated presets below are available for use directly (no bold-template-pack needed). Use them in Phase 2 previews as Option 1 (safe) or Option 3 (wildcard), or when the user names one explicitly.

**Abstract shapes only — no illustrations.**

### Dark Themes

**#4 · Bold Signal** — Confident, bold, modern, high-impact
- Layout: Colored card on dark gradient. Large section numbers top-left, navigation top-right, title bottom-left.
- Fonts: `Archivo Black` (900) display, `Space Grotesk` (400/500) body
- Colors: `--bg-primary: #1a1a1a; --card-bg: #FF5722; --text-primary: #fff; --text-on-card: #1a1a1a;`
- Signature: Bold colored focal card, large section numbers (01, 02), grid-based layout

**#5 · Electric Studio** — Bold, clean, professional, high contrast
- Layout: Split panel — white top, blue bottom. Brand marks in corners.
- Fonts: `Manrope` (800) display, `Manrope` (400/500) body
- Colors: `--bg-dark: #0a0a0a; --bg-white: #fff; --accent-blue: #4361ee; --text-dark: #0a0a0a; --text-light: #fff;`
- Signature: Two-panel vertical split, accent bar on panel edge, quote typography as hero

**#6 · Creative Voltage** — Bold, creative, energetic, retro-modern
- Layout: Split panels — electric blue left, dark right. Script accents.
- Fonts: `Archivo Black` (400), `Space Mono` (400/700)
- Colors: `--bg-primary: #0066ff; --bg-dark: #1a1a2e; --accent-neon: #d4ff00; --text-light: #fff;`
- Signature: Electric blue + neon yellow, halftone textures, neon badges/callouts

**#7 · Dark Botanical** — Elegant, sophisticated, artistic, premium
- Layout: Centered content on dark. Abstract soft shapes in corner.
- Fonts: `Cormorant` (400/600) display, `IBM Plex Sans` (300/400) body
- Colors: `--bg-primary: #0f0f0f; --text-primary: #e8e4df; --accent-warm: #d4a574; --accent-pink: #e8b4b8;`
- Signature: Abstract soft gradient circles (blurred, overlapping), thin vertical accent lines, italic signature typography

### Light Themes

**#8 · Notebook Tabs** — Editorial, organized, elegant, tactile
- Layout: Cream paper card on dark background. Colorful tabs on right edge.
- Fonts: `Bodoni Moda` (400/700) display, `DM Sans` (400/500) body
- Colors: `--bg-outer: #2d2d2d; --bg-page: #f8f6f1; --tab-1: #98d4bb; --tab-2: #c7b8ea; --tab-3: #f4b8c5;`
- Signature: Paper container with shadow, colorful section tabs on right (vertical text), binder holes on left

**#9 · Pastel Geometry** — Friendly, organized, modern, approachable
- Layout: White card on pastel background. Vertical pills on right edge.
- Fonts: `Plus Jakarta Sans` (700/800) display, `Plus Jakarta Sans` (400/500) body
- Colors: `--bg-primary: #c8d9e6; --card-bg: #faf9f7; --pill-pink: #f0b4d4; --pill-mint: #a8d4c4;`
- Signature: Rounded card with soft shadow, vertical pills varying heights on right edge

**#10 · Split Pastel** — Playful, modern, friendly, creative
- Layout: Two-color vertical split (peach left, lavender right).
- Fonts: `Outfit` (700/800) display, `Outfit` (400/500) body
- Colors: `--bg-peach: #f5e6dc; --bg-lavender: #e4dff0; --badge-mint: #c8f0d8; --badge-yellow: #f0f0c8;`
- Signature: Split background colors, playful badge pills with icons, grid pattern overlay on right panel

**#11 · Vintage Editorial** — Witty, confident, editorial, personality-driven
- Layout: Centered content on cream. Abstract geometric shapes as accent.
- Fonts: `Fraunces` (700/900) display, `Work Sans` (400/500) body
- Colors: `--bg-cream: #f5f3ee; --text-primary: #1a1a1a; --accent-warm: #e8d4c0;`
- Signature: Abstract geometric shapes (circle outline + line + dot), bold bordered CTA boxes

### Specialty Themes

**#12 · Neon Cyber** — Futuristic, techy, confident
- Fonts: `Clash Display` + `Satoshi` (Fontshare)
- Colors: Deep navy `#0a0f1c`, cyan `#00ffcc`, magenta `#ff00aa`
- Signature: Particle backgrounds, neon glow, grid patterns

**#13 · Terminal Green** — Developer-focused, hacker aesthetic
- Fonts: `JetBrains Mono` (monospace only)
- Colors: GitHub dark `#0d1117`, terminal green `#39d353`
- Signature: Scan lines, blinking cursor, code syntax styling

**#14 · Swiss Modern** — Clean, precise, Bauhaus-inspired
- Fonts: `Archivo` (800) + `Nunito` (400)
- Colors: Pure white, pure black, red `#ff3300`
- Signature: Visible grid, asymmetric layouts, geometric shapes

**#15 · Paper & Ink** — Editorial, literary, thoughtful
- Fonts: `Cormorant Garamond` + `Source Serif 4`
- Colors: Warm cream `#faf9f7`, charcoal `#1a1a1a`, crimson `#c41e3a`
- Signature: Drop caps, pull quotes, elegant horizontal rules

---

## DO NOT USE (Generic AI Patterns)

**Fonts:** Inter, Roboto, Arial, system fonts as display type
**Colors:** `#6366f1` (generic indigo), purple gradients on white
**Layouts:** Everything centered, generic hero sections, identical card grids
**Decorations:** Realistic illustrations, gratuitous glassmorphism, drop shadows without purpose

---

## Font Pairing Quick Reference

| Preset | Display Font | Body Font | Source |
|--------|-------------|-----------|--------|
| Brand | Crimson Pro | Manrope | Google |
| Dark-Midnight | Archivo Black | DM Sans | Google |
| Light-Serenity | Plus Jakarta Sans | Plus Jakarta Sans | Google |
| Bold Signal | Archivo Black | Space Grotesk | Google |
| Electric Studio | Manrope | Manrope | Google |
| Creative Voltage | Archivo Black | Space Mono | Google |
| Dark Botanical | Cormorant | IBM Plex Sans | Google |
| Notebook Tabs | Bodoni Moda | DM Sans | Google |
| Pastel Geometry | Plus Jakarta Sans | Plus Jakarta Sans | Google |
| Split Pastel | Outfit | Outfit | Google |
| Vintage Editorial | Fraunces | Work Sans | Google |
| Neon Cyber | Clash Display | Satoshi | Fontshare |
| Terminal Green | JetBrains Mono | JetBrains Mono | JetBrains |
| Swiss Modern | Archivo | Nunito | Google |
| Paper & Ink | Cormorant Garamond | Source Serif 4 | Google |
