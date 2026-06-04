# Animation Toolkit

**Single source of truth for all animations in html-slides-advanced.**
This replaces `animation-patterns.md` from frontend-slides. All patterns from both sources are unified here.

Include the CSS blocks in every deck's `<style>`. The `SlidePresentation` controller triggers slide-entry animations by adding `.visible` to the active slide.

---

## 1. CSS Custom Properties

Add to `:root` in every deck:

```css
:root {
  /* Easing curves */
  --ease-out-expo:  cubic-bezier(0.16, 1, 0.3, 1);
  --ease-out-cubic: cubic-bezier(0.33, 1, 0.68, 1);
  --ease-spring:    cubic-bezier(0.34, 1.56, 0.64, 1);

  /* Duration scale */
  --dur-fast:   0.35s;
  --dur-normal: 0.55s;
  --dur-slow:   0.80s;
}
```

---

## 2. Entrance Animations

Apply to elements that should animate in when their slide becomes active.
The parent `.slide` must have `.visible` to trigger.

```css
/* ── Fade + Slide Up — most versatile, default choice ── */
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition:
    opacity   var(--dur-normal) var(--ease-out-expo),
    transform var(--dur-normal) var(--ease-out-expo);
}
.slide.visible .reveal { opacity: 1; transform: none; }

/* ── Directional variants — add alongside .reveal ── */
.from-left  { transform: translateX(-40px); }
.from-right { transform: translateX( 40px); }
.from-scale { transform: scale(0.88) translateY(12px); }
.from-blur  { filter: blur(10px); opacity: 0; }

.slide.visible .from-left  { transform: none; }
.slide.visible .from-right { transform: none; }
.slide.visible .from-scale { transform: none; }
.slide.visible .from-blur  { filter: none; opacity: 1; }

/* ── Fade only — use on full-bleed image slides ── */
.fade-only {
  opacity: 0;
  transition: opacity var(--dur-slow) ease;
}
.slide.visible .fade-only { opacity: 1; }
```

### Stagger — cascade child reveals sequentially

Wrap siblings in `.stagger` to offset each child's entrance:

```css
.stagger .reveal:nth-child(1)  { transition-delay: 0.05s; }
.stagger .reveal:nth-child(2)  { transition-delay: 0.15s; }
.stagger .reveal:nth-child(3)  { transition-delay: 0.25s; }
.stagger .reveal:nth-child(4)  { transition-delay: 0.35s; }
.stagger .reveal:nth-child(5)  { transition-delay: 0.45s; }
.stagger .reveal:nth-child(6)  { transition-delay: 0.55s; }
.stagger .reveal:nth-child(7)  { transition-delay: 0.65s; }
.stagger .reveal:nth-child(8)  { transition-delay: 0.75s; }
```

---

## 3. Looping Ambient Animations

These run continuously after slide entry. Always wrap in `@media (prefers-reduced-motion: no-preference)`.

```css
/* ── Float — gentle up/down drift (portrait cards, decorative discs) ── */
.float { animation: float-anim 4s ease-in-out infinite; }
@keyframes float-anim {
  0%, 100% { transform: translateY(0); }
  50%       { transform: translateY(-10px); }
}

/* ── Pulse — breathing glow ring (NOW marker, active agenda item) ── */
/* Use style-specific color via --accent in the keyframe below */
.pulse { animation: pulse-ring 2.2s ease-in-out infinite; }
@keyframes pulse-ring {
  0%, 100% { box-shadow: 0 8px 24px rgba(var(--pulse-rgb, 211,11,0),.25), 0 0 0 0  rgba(var(--pulse-rgb, 211,11,0),0); }
  50%       { box-shadow: 0 8px 24px rgba(var(--pulse-rgb, 211,11,0),.25), 0 0 0 14px rgba(var(--pulse-rgb, 211,11,0),.12); }
}
/* Override --pulse-rgb per style:
   Brand:          211,11,0
   Dark-Midnight:  252,163,17
   Light-Serenity: 39,48,67    */

/* ── Blink — cursor (code block) ── */
.blink { animation: blink-anim 1.2s step-end infinite; }
@keyframes blink-anim {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0; }
}

/* ── Glow breathe — icon/mark ambient glow ── */
.glow-anim { animation: glow-breathe 3s ease-in-out infinite; }
@keyframes glow-breathe {
  0%, 100% { filter: drop-shadow(0 0 8px  rgba(var(--pulse-rgb, 211,11,0),.30)); }
  50%       { filter: drop-shadow(0 0 20px rgba(var(--pulse-rgb, 211,11,0),.60)); }
}
```

---

## 4. Draw & Write Animations

For SVG paths, lines, and decorative accents.

```css
/* ── Draw-line — SVG path draws itself left-to-right ── */
/* JS sets strokeDasharray = path length, strokeDashoffset = length */
/* .slide.visible then transitions dashoffset to 0 */
.draw-line {
  stroke-dashoffset: 1000; /* overwritten by JS with actual getTotalLength() */
  transition: stroke-dashoffset 0.9s var(--ease-out-expo) 0.25s;
}
.slide.visible .draw-line { stroke-dashoffset: 0; }

/* ── Self-write — decorative accent line grows from left ── */
.self-write {
  stroke-dasharray: 1 0;
  stroke-dashoffset: 0;
  stroke-width: 2;
  transition: stroke-dasharray 1.2s var(--ease-out-expo) 0.4s;
}
.slide.visible .self-write { stroke-dasharray: 200 0; }
```

**JS init (run once in SlidePresentation constructor):**

```javascript
document.querySelectorAll('.draw-line').forEach(el => {
  let len;
  try { len = el.getTotalLength(); } catch { len = 300; }
  el.style.strokeDasharray  = len;
  el.style.strokeDashoffset = len;
  // CSS transition fires when parent slide gets .visible
});
```

---

## 5. Luminescence Glow Sweep

A top-to-bottom light shimmer that fires once on slide entry. Used on the **Code Block** card and the **Quote** card. Adds a premium "screen wipe" feel to dark or richly styled containers.

```css
/* Place on the container element — not a child */
.lum-glow { position: relative; overflow: hidden; }
.lum-glow::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(255, 255, 255, 0.07) 40%,
    rgba(255, 255, 255, 0.13) 50%,
    rgba(255, 255, 255, 0.07) 60%,
    transparent 100%
  );
  transform: translateY(-110%);
  pointer-events: none;
  border-radius: inherit;
}

/* Fires once when the parent slide becomes active */
.slide.visible .lum-glow::after {
  animation: lum-sweep 1.1s cubic-bezier(0.16, 1, 0.3, 1) 0.6s forwards;
}
@keyframes lum-sweep {
  from { transform: translateY(-110%); }
  to   { transform: translateY(110%); }
}
```

**Timing:** delay of 0.6s on Code Block card (fires after the card slides in from right). Delay of 0.5s on Quote blockquote, 0.7s on Quote portrait card.

**Works on any dark or richly colored container** — the light band is subtle enough to avoid looking garish on light surfaces, but most effective on dark cards. Can also be applied to stat cells, feature bento cards, or roadmap markers for additional emphasis.

**Reduced motion:** the `lum-sweep` animation is gated by `prefers-reduced-motion: reduce` via the global reset — no extra code needed.

---

## 6. Scan & Sweep

```css
/* ── Scan — vertical light sweep over code card or image ── */
.scan-wrap { position: relative; overflow: hidden; }
.scan {
  position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(
    to bottom,
    transparent,
    rgba(var(--pulse-rgb, 211,11,0), 0.06),
    transparent
  );
  animation: scan-anim 3.5s ease-in-out infinite;
}
@keyframes scan-anim {
  0%   { transform: translateY(-100%); opacity: 0; }
  15%  { opacity: 1; }
  85%  { opacity: 1; }
  100% { transform: translateY(100%); opacity: 0; }
}
```

---

## 7. Background Effects

Apply to `.slide-inner` or a `::before` pseudo-element for atmospheric depth.

```css
/* ── Gradient mesh — layered radial gradients ── */
/* Adapt color stops to match the chosen style */
.gradient-bg {
  background:
    radial-gradient(ellipse at 20% 80%, rgba(252,163,17,.18) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 20%, rgba(252,163,17,.10) 0%, transparent 50%),
    var(--bg-primary);
}

/* ── Grid pattern — structural lines for techy/developer styles ── */
.grid-bg {
  background-image:
    linear-gradient(rgba(255,255,255,.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.03) 1px, transparent 1px);
  background-size: 60px 60px;
}

/* ── Noise texture — grain overlay for editorial/vintage styles ── */
/* Use inline SVG data URI for the noise pattern */
.noise-bg::before {
  content: '';
  position: absolute; inset: 0;
  background-image: url("data:image/svg+xml,...");
  opacity: 0.04;
  pointer-events: none;
}
```

---

## 8. Interactive Effects

```javascript
/* ── 3D Tilt on hover — depth for cards and bento panels ── */
class TiltEffect {
  constructor(element, intensity = 8) {
    element.style.transformStyle = 'preserve-3d';
    element.style.perspective = '1000px';
    element.addEventListener('mousemove', (e) => {
      const rect = element.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width  - 0.5;
      const y = (e.clientY - rect.top)  / rect.height - 0.5;
      element.style.transform = `rotateY(${x * intensity}deg) rotateX(${-y * intensity}deg)`;
    });
    element.addEventListener('mouseleave', () => {
      element.style.transform = 'rotateY(0) rotateX(0)';
      element.style.transition = 'transform 0.4s var(--ease-out-expo)';
    });
    element.addEventListener('mousemove', () => {
      element.style.transition = 'none';
    });
  }
}
// Apply: document.querySelectorAll('.bento-card').forEach(el => new TiltEffect(el));
```

---

## 9. Count-Up (Stat Grid)

Handled by `SlidePresentation.triggerCountUps()`. Reference:

```javascript
// Reads data-target (number) and data-suffix (string) from .stat-val elements.
// Animates 0 → target over 1400ms with ease-out-cubic. Fires once per slide.
// HTML: <span class="stat-val" data-target="900" data-suffix="M">0</span>
```

---

## 10. Reduced Motion

Always include. Gates all motion:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration:        0.01ms !important;
    animation-iteration-count: 1      !important;
    transition-duration:       0.1ms  !important;
  }
  .draw-line, .self-write { stroke-dashoffset: 0 !important; }
}
```

---

## 11. Effect-to-Feeling Guide

Match animation character to the chosen style's mood. Same classes, different tuning.

| Feeling | Animation approach | Recommended classes |
|---------|-------------------|---------------------|
| **Dramatic / Cinematic** | Slow fades (0.9–1.3s), large scale (0.88→1), blur-in | `.reveal.from-blur`, `.fade-only`, `.float` |
| **Techy / Futuristic** | Neon glow, scan sweep, cursor blink, grid reveals | `.scan`, `.blink`, `.glow-anim`, `.draw-line` |
| **Bold / Confident** | Fast snappy (0.4s), scale-in cards, draw-line connectors | `.reveal.from-scale`, `.draw-line`, `.stagger` |
| **Playful / Friendly** | Spring bounce, float bobbing, pop-in cards | `.float`, `.reveal.from-scale`, `.stagger` |
| **Professional / Corporate** | Subtle fast (300–450ms), clean stagger | `.reveal`, `.stagger`, `.fade-only` |
| **Calm / Minimal** | Very slow (700ms+), gentle fades only | `.reveal` (slowed), `.fade-only` |
| **Editorial / Magazine** | Staggered text reveals, draw-line accents | `.stagger`, `.draw-line`, `.self-write` |

### Style × Animation Character

| Style | Easing | Duration | Stagger gap | Ambient loops |
|-------|--------|----------|-------------|---------------|
| Brand | `ease-out-expo` | 550ms | 100ms | float (slow), pulse-red |
| Dark-Midnight | `ease-out-expo` | 500ms | 90ms | pulse-amber, glow-anim |
| Light-Serenity | `ease-out-cubic` | 600ms | 120ms | none — too restrained |
| Bold Signal | `ease-spring` | 400ms | 60ms | none |
| Dark Botanical | `ease-out-expo` | 800ms | 150ms | float (very slow) |
| Terminal Green | linear | 200ms | 40ms | scan, blink |
| Creative Voltage | `ease-spring` | 380ms | 55ms | glow-anim |
| Neon Cyber | `ease-out-expo` | 450ms | 70ms | scan, glow-anim |
| Notebook Tabs | `ease-out-cubic` | 600ms | 130ms | none |
| Vintage Editorial | `ease-out-expo` | 650ms | 130ms | none |
| Swiss Modern | `ease-out-cubic` | 350ms | 50ms | none |
| Paper & Ink | `ease-out-expo` | 700ms | 150ms | float (very subtle) |

---

## 12. Per-Format Animation Cheat Sheet

| Format | Element | Class(es) | Notes |
|--------|---------|-----------|-------|
| **Cover** | Spark mark | `.reveal.from-scale` | First, delay 0 |
| **Cover** | Title | `.reveal` | Delay 0.15s |
| **Cover** | Subtitle | `.reveal` | Delay 0.30s |
| **Agenda** | Item list | `.stagger` on wrapper | `.from-left` variant |
| **Agenda** | Active item | `.pulse` | Looping glow ring |
| **Two-column** | Left content | `.stagger` | Fade + up |
| **Two-column** | Right visual | `.reveal.from-right` | Slides from right |
| **Stat grid** | Title + sub | `.reveal` | |
| **Stat grid** | Each cell | `.stagger` | Count-up JS fires after |
| **Stat grid** | Numbers | `countUp()` JS | data-target, data-suffix |
| **Feature bento** | Each card | `.stagger.from-scale` | Cards pop in |
| **Comparison** | Header row | `.reveal` | |
| **Comparison** | Data rows | `.stagger.from-left` | Row by row |
| **Steps** | Each node | `.stagger` | |
| **Steps** | Arrow SVGs | `.draw-line` | Lines draw between nodes |
| **Roadmap** | Title + sub | `.reveal` | |
| **Roadmap** | Timeline line | `.draw-line` | Draws left → right |
| **Roadmap** | Milestones | `.stagger` | |
| **Roadmap** | NOW marker | `.pulse` | Looping glow |
| **Chart** | Container | `.reveal` | Chart.js animates bars |
| **Code block** | Left text | `.stagger` | |
| **Code block** | Code card | `.reveal.from-right` → `.lum-glow` sweep | Card enters from right, then glow sweeps top→bottom (delay 0.6s) |
| **Code block** | Cursor | `.blink` | Loop |
| **Code block** | Scan overlay | `.scan` | Optional |
| **Quote** | Quote mark | `.reveal.from-scale` | |
| **Quote** | Quote text | `.reveal` → `.lum-glow` sweep | Fades up, glow sweeps top→bottom (delay 0.5s) |
| **Quote** | Attribution | `.reveal` | |
| **Quote** | Portrait card | `.reveal.from-right` → `.lum-glow` + `.float` | Entry + sweep (delay 0.7s), then float loop |
| **Closing** | Spark | `.reveal.from-scale` | Mirror of Cover |
| **Closing** | Title | `.reveal` | |
| **Closing** | CTA button | `.reveal` | |

---

## 13. Animation Philosophy & Level Selection

**Core rule: animations should improve the slide, never just decorate it.**
Selection is based on topic, design system, audience, and slide content — not a fixed tier list.
No animation is categorically excluded if it genuinely serves the slide.

### Q6 Level (starting temperature, not a ceiling)

| Level | What it means |
|-------|--------------|
| **Subtle** | Quick, unobtrusive entrances. Ambient loops only where they add clear meaning (e.g. pulse on an active milestone). Nothing distracts from content. |
| **Moderate** | Confident entrances with directional variants. Draw-line on connectors and timelines. One or two ambient loops per slide where they reinforce the message. |
| **Rich** | Full toolkit. Every format gets its best animation. Looping effects, interactive hover depth, atmospheric background motion, particle systems where the design system calls for it. |

### Slide transition (one fixed rule)
Every slide change uses a clean fade — switching `visibility` and `opacity` only. No push, flip, or wipe between slides. This keeps performance solid and lets within-slide animations carry all the motion energy. All 19 animation tools apply freely within each slide; this rule only governs the moment of switching from one slide to the next.

### Within-slide animation — flexible, context-driven
Apply whichever animations make each specific slide better. Match to:
- **Topic** — technical content pairs with scan/draw-line; milestone content pairs with pulse; stats pair with count-up
- **Design system** — dark systems welcome glow and scan; editorial systems suit draw-line and self-write; minimal systems prefer subtle fades
- **Audience** — executive audiences prefer restraint; creative/developer audiences welcome rich motion
- **Slide content** — process steps need draw-line connectors; stat grids need count-up; code blocks need blink cursor; quote cards suit float

If a richer animation would genuinely improve a deck's most important slide, use it — and apply it with intention. The level is a guide, not a hard ceiling.

### Skip an animation only when:
- It adds motion without adding meaning to the slide
- It delays the audience from reading the content
- It conflicts with the design system's mood

---

## 14. CSS Gotchas

**Never negate CSS functions directly:**
```css
/* WRONG — browser silently ignores */
margin-left: -clamp(20px, 3vw, 40px);

/* CORRECT */
margin-left: calc(-1 * clamp(20px, 3vw, 40px));
```

**`transform` + `filter` stacking context:**
Don't combine `filter: blur()` entrance with `transform` on the same element — use one or the other.

**`will-change` — sparingly only:**
```css
.tl-marker.pulse { will-change: box-shadow; }
.code-cursor      { will-change: opacity; }
```

**Troubleshooting:**

| Problem | Fix |
|---------|-----|
| Fonts not loading | Check Fontshare/Google Fonts URL; name matches in CSS |
| Animations not triggering | Verify `.visible` is being added; check JS controller |
| All slides visible at once | Never use `display:none/block` for switching — use `visibility`+`opacity` from viewport-base.css |
| Draw-line not animating | Check `getTotalLength()` ran; confirm `.slide.visible .draw-line { stroke-dashoffset: 0 }` |
| Count-up fires twice | `_countUpDone` Set must track by slide index, not by element |
| Slide text overflows | Cut copy. Split. Never shrink font below minimums. |
| CSS negation bug | `-clamp()` silently ignored. Use `calc(-1 * clamp(...))` |
| Scroll snap broken | Ensure `scroll-snap-type: y mandatory` on html; each slide needs `scroll-snap-align: start` |
| Mobile issues | Disable heavy effects at 768px; reduce particle count; test touch events |
| Performance | `will-change` sparingly; prefer `transform`/`opacity`; throttle scroll handlers |
