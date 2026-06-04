# Typography Reference

Font sizing rules for the 1920×1080 fixed stage. All sizes are authored at stage resolution.
The stage scales uniformly to the viewport — a 28px body on a 1920-wide stage renders as
~14px on a 960px screen (0.5× scale). **Never go below the minimums below.**

---

## Why Font Sizes Break

The most common cause of tiny text in frontend-slides output was mixing two things:
- `clamp()` inside the slide stage (correct only for non-slide UI like progress bars/dots)
- Authoring text at viewport-relative sizes (`vw`, `vh`, `%`) instead of fixed stage px

Inside the 1920×1080 stage, **all sizes must be fixed px** authored for the design canvas.
The stage-scale transform handles the shrink. `clamp()` and `vw` inside the stage create
a second, compounding shrink that produces illegibly small text.

---

## Type Scale — 1920×1080 Stage

**The 12pt rendered floor:** At the most common presentation screen width (1280px), the stage
scales to ×0.625. A stage element must be at least **19px** to render at 12pt (≈16px) at that
scale. At 1440px (×0.75 scale), the floor is **16px stage** to hit 12pt. Use **24px as the
universal stage minimum** — this guarantees ≥12pt at every screen from 1280px up.
**No element on any slide may render below 12pt. This is an absolute, non-negotiable floor.**

| Role | Min stage px | Recommended px | Max px | Min rendered pt (1280px) |
|------|-------------|----------------|--------|--------------------------|
| **Cover / closing title** | 80 | 96–112 | 140 | ~50pt ✓ |
| **Section / slide title (h2)** | 52 | 64–72 | 96 | ~33pt ✓ |
| **Sub-heading (h3)** | 40 | 44–52 | 64 | ~25pt ✓ |
| **Eyebrow / label** | 24 | 26–28 | 36 | ~15pt ✓ |
| **Body / paragraph** | 26 | 28–32 | 40 | ~16pt ✓ |
| **Bullets / list items** | 24 | 26–30 | 36 | ~15pt ✓ |
| **Captions / footnotes** | 24 | 24–26 | 30 | ~15pt ✓ — raised from 18; 18px = ~11pt, below floor |
| **Stat numbers** | 80 | 100–120 | 160 | ~50pt ✓ |
| **Stat suffix (M, %, ×)** | 36 | 42–48 | 64 | ~23pt ✓ |
| **Stat label** | 24 | 26–28 | 32 | ~15pt ✓ |
| **Stat note / sub-label** | 24 | 24–26 | 28 | ~15pt ✓ — floor |
| **Code body** | 24 | 24–26 | 30 | ~15pt ✓ — raised from 18 |
| **Agenda numbers** | 40 | 48–56 | 72 | ~25pt ✓ |
| **Quote text** | 40 | 48–56 | 80 | ~25pt ✓ |
| **Timeline label** | 24 | 24–26 | 30 | ~15pt ✓ — raised from 20 |
| **Chart axis / legend** | 24 | 24–26 | 28 | ~15pt ✓ — raised from 14; set via Chart.js `font.size` |
| **Nav dots / progress** | — | 8–10px dot | — | Outside stage; `clamp()` OK here |

**Key change from prior versions:** Captions, code, timeline labels, and chart labels previously
allowed 14–18px stage sizes. At 1280px scale those rendered at 9–11pt — below the 12pt floor.
All are now floored at 24px stage minimum.

---

## CSS Variables — Set Once, Use Everywhere

Add to `:root` in every deck:

```css
:root {
  /* Type scale — all in stage px, no clamp() inside the stage */
  /* Universal floor: 24px stage → ≥12pt at 1280px (×0.625 scale) */
  --text-cover:    104px;  /* adjust per style, min 80 */
  --text-h2:        68px;  /* adjust per style, min 52 */
  --text-h3:        48px;  /* adjust per style, min 40 */
  --text-eyebrow:   26px;  /* min 24 — raised from 18 */
  --text-body:      28px;  /* min 26 */
  --text-bullet:    26px;  /* min 24 */
  --text-caption:   24px;  /* hard floor — never below — raised from 18 */
  --text-stat:     112px;  /* min 80 */
  --text-stat-sfx:  44px;  /* min 36 */
  --text-stat-lbl:  26px;  /* min 24 */
  --text-code:      24px;  /* min 24 — raised from 18 */
  --text-quote:     52px;  /* min 40 */
  --text-agenda-n:  52px;  /* min 40 */
  --text-tl-label:  24px;  /* min 24 — raised from 20 */

  /* Line heights */
  --lh-display: 1.05;
  --lh-title:   1.10;
  --lh-body:    1.55;
  --lh-code:    1.70;
  --lh-tight:   1.25;

  /* Letter spacing */
  --ls-display:  -0.03em;
  --ls-title:    -0.02em;
  --ls-eyebrow:   0.12em;
  --ls-body:      0;
}
```

---

## Per-Format Type Settings

### Cover / Closing
```css
.cover-title, .closing-title {
  font-family: var(--font-title);
  font-size: var(--text-cover);    /* 96–112px */
  font-weight: 500;
  line-height: var(--lh-display);
  letter-spacing: var(--ls-display);
}
.cover-sub, .closing-sub {
  font-size: var(--text-body);     /* 28–32px */
  color: var(--text-secondary);
}
```

### Slide Titles (all other formats)
```css
.slide-title {
  font-family: var(--font-title);
  font-size: var(--text-h2);       /* 64–72px */
  font-weight: 500;
  line-height: var(--lh-title);
  letter-spacing: var(--ls-title);
}
.slide-sub {
  font-size: var(--text-body);     /* 26–28px */
  color: var(--text-secondary);
  line-height: var(--lh-body);
}
```

### Body / Bullets
```css
.body-text  { font-size: var(--text-body);   line-height: var(--lh-body); }
.bullet-list li { font-size: var(--text-bullet); line-height: 1.5; }
.caption    { font-size: var(--text-caption); color: var(--text-secondary); }
```

### Stat Grid
```css
.stat-number { font-size: var(--text-stat); line-height: 1.0; }
.stat-label  { font-size: 28px;  font-weight: 600; } /* never below 24 */
.stat-note   { font-size: 20px;  color: var(--text-secondary); } /* never below 18 */
```

### Code Block
```css
.code-body {
  font-size: var(--text-code);    /* 20–22px */
  line-height: var(--lh-code);
  font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
}
```

### Chart
```javascript
// Chart.js — set font sizes explicitly, never leave as defaults
Chart.defaults.font.size = 16;      // axis labels — min 14
Chart.defaults.font.family = 'var(--font-body)';

// In dataset options:
plugins: {
  legend: { labels: { font: { size: 16 } } },   // min 14
  tooltip: { bodyFont: { size: 16 }, titleFont: { size: 16 } }
}
```

---

## Hard Floors — Absolute Minimums

**12pt is the absolute rendered floor.** At 1280px viewport (×0.625 stage scale),
24px stage = 15px rendered = ~11pt. Therefore **24px is the universal stage minimum**
that guarantees ≥12pt at all screens from 1280px and wider.

| Element | Hard floor (stage px) | Renders as at 1280px | If violated |
|---------|----------------------|----------------------|-------------|
| Any body / bullet text | 24px | ~15pt ✓ | Increase font or reduce copy |
| Any caption / footnote / label | 24px | ~15pt ✓ | Increase font or remove |
| Any eyebrow | 24px | ~15pt ✓ | Increase font |
| Code text | 24px | ~15pt ✓ | Increase font |
| Timeline / roadmap labels | 24px | ~15pt ✓ | Increase font |
| Chart axis labels / legend | 24px | ~15pt ✓ | Set explicitly in Chart.js options |
| Stat sub-label / note | 24px | ~15pt ✓ | Increase font |
| Stat number | 80px | ~50pt ✓ | Never shrink — cut copy instead |
| Slide title (h2) | 52px | ~33pt ✓ | Split to shorter title + subtitle |
| Cover / closing title | 80px | ~50pt ✓ | Never shrink — shorten the title |

**If content overflows at these minimum sizes → split into two slides. Never compromise the floor.**

---

## Descender Safety Rules

Descenders are the tails on letters like **g, j, p, q, y**. They extend below the text baseline. Three CSS properties working together cause them to be clipped:

**Root causes and fixes:**

| Cause | Symptom | Fix |
|-------|---------|-----|
| `line-height: 1` or lower | Tails on g/j/p/q/y sliced off | Minimum `line-height: 1.15` for display text, `1.55` for body |
| `overflow: hidden` on text container | Hard crop at container bottom | Add `overflow: visible` to text elements and their parents |
| Fixed `height` with no padding | Letters touch the container floor | Use `min-height` not `height`; add `padding-bottom: 0.15em` to text containers |
| Tight `padding-bottom: 0` | No breathing room below baseline | Add `padding-bottom: 0.12em–0.18em` on all large display text |

**Required minimums — apply to every display text element:**

```css
/* ✓ Correct — all large text */
.cover-title, .closing-title {
  line-height: 1.15;        /* never below 1.1 for display */
  padding-bottom: 0.14em;   /* descender clearance */
  overflow: visible;         /* never hidden on text elements */
}

/* ✓ Correct — stat numbers */
.stat-number {
  line-height: 1.2;          /* never below 1.15 for large numerals */
  padding-bottom: 0.18em;    /* numerals have deep descenders in many fonts */
  overflow: visible;
}

/* ✓ Correct — body and bullets */
.body-text, .bullet-list li {
  line-height: 1.55;         /* standard — well above descender floor */
  /* no special padding needed at body size */
}

/* ✗ Wrong — clips descenders */
.stat-number {
  line-height: 1;            /* NEVER — will clip g, j, p, q, y tails */
  height: 140px;             /* NEVER fixed height on text containers */
  overflow: hidden;          /* NEVER on elements containing text */
}
```

**Stat grid specific rule:** stat number containers must use `overflow: visible` on both the number element AND its parent cell. Flexbox cells with `align-items: stretch` can create implicit height constraints that clip even with correct `line-height`.

**First-slide count-up rule:** If the first slide is initialized with `animate = false` (to skip entrance animations on load), count-up JS must be triggered separately with a small delay (300–500ms) after the controller initializes. Otherwise all stat values display as "0".

```javascript
// Always do this when slide 1 has count-up stats:
document.addEventListener('DOMContentLoaded', () => {
  window.presentation = new SlidePresentation();
  setTimeout(() => { window.presentation.triggerCountUps(0); }, 400);
});
```

---

## Common Font Sizing Bugs & Fixes

| Bug | Cause | Fix |
|-----|-------|-----|
| Text renders below 12pt | Stage size below 24px floor | Raise all sub-24px stage sizes to 24px minimum |
| Body text < 10pt on screen | `clamp()` inside stage AND stage scale compound | Remove `clamp()` inside stage; use fixed px |
| All text illegibly tiny | Font sizes in `vw` or `%` inside stage | Convert all to fixed px at 1920×1080 |
| Title overflows slide | Font too large for headline length | Use `var(--text-h2)` for long titles, `--text-cover` only for ≤3-word covers |
| Stat number clips bottom | Descenders clipped by overflow: hidden | Add `padding-bottom: 0.15em` to stat container; check `overflow: visible` |
| Caption illegible at small screens | Caption below 24px stage floor | Minimum 24px stage; was previously 18px — update legacy decks |
| Code text cramped | Default browser monospace size used | Set explicitly to 24px minimum in `.code-body` |
| Chart labels tiny | Chart.js defaults to 12px internal | Set `Chart.defaults.font.size = 24` and per-dataset `font: { size: 24 }` |
| Bullet text wraps badly | Font too large for bullet count | Reduce bullets first; never reduce below 24px |
| Timeline labels invisible | Set below 24px floor | `var(--text-tl-label)` = 24px minimum |

---

## Font Loading

Always load from Google Fonts or Fontshare — never system fonts for display.

```html
<!-- Google Fonts (two-step for performance) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,500;1,400;1,500&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">

<!-- Fontshare (for Clash Display, Satoshi, etc.) -->
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=clash-display@400,600,700&f[]=satoshi@400,500&display=swap">
```

**Always include `display=swap`** — prevents invisible text during font load.
**Never use `@import` inside `<style>`** — blocks render. Use `<link>` in `<head>` only.

---

## Read This File In

`TYPOGRAPHY.md` is a required pre-generation reference alongside `FORMATS.md`, `STYLES.md`, and `ANIMATION-TOOLKIT.md`. Add it to the Phase 4 reading list in `SKILL.md`.
