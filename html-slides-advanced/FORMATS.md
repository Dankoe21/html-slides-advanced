# Layout Formats Reference

All 12 canonical slide formats. Every format uses only CSS tokens from the format contract — never hardcoded colors. Every deck's `<style>` block must include `viewport-base.css` contents + `STYLES.md` variables + `ANIMATION-TOOLKIT.md` classes before any format-specific CSS.

**Format contract tokens** (all 4 styles define these):
`--bg-primary` `--text-primary` `--text-secondary` `--accent` `--accent-dim` `--border` `--surface` `--on-accent` `--font-title` `--font-body`

---

## Shared Layout Wrapper

Every slide uses this outer structure:

```html
<section class="slide [format-class]" data-slide="N">
  <!-- format-specific inner content -->
</section>
```

Dark slides (cover + closing): add `slide--dark` class.

### Slide Base CSS (beyond viewport-base.css)

```css
.slide-inner {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  padding: 72px 96px;
  background: var(--bg-primary);
  font-family: var(--font-body);
  color: var(--text-primary);
}

.slide-eyebrow {
  font-size: 18px;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--text-secondary);
  margin-bottom: 16px;
}

.slide-title {
  font-family: var(--font-title);
  font-size: 64px;
  font-weight: 500;
  line-height: 1.1;
  letter-spacing: -.02em;
  color: var(--text-primary);
  margin-bottom: 20px;
}

.slide-sub {
  font-size: 26px;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 48px;
}

.accent-word {
  color: var(--accent);
  font-style: italic;
}

/* Spark mark — constant brand mark on cover + closing */
.spark {
  width: 48px;
  height: 48px;
  margin-bottom: 40px;
}
```

---

## Format 1: Cover / Title

**When to use:** First slide of every deck. Near-black "ink" background. Spark mark top-left, centered title block.

```html
<section class="slide slide--dark cover-slide" data-slide="1">
  <div class="slide-inner cover-inner">
    <svg class="spark reveal from-scale" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- Spark: 4-pointed star shape in accent red -->
      <path d="M24 4 L26.5 21.5 L44 24 L26.5 26.5 L24 44 L21.5 26.5 L4 24 L21.5 21.5 Z"
            fill="var(--accent)"/>
    </svg>
    <h1 class="cover-title reveal">
      A presentation title <em class="accent-word">in your voice</em>
    </h1>
    <p class="cover-sub reveal">A short subtitle. Follows the title.</p>
  </div>
</section>
```

```css
.cover-inner {
  justify-content: center;
  padding: 120px 160px;
}

.cover-title {
  font-family: var(--font-title);
  font-size: 96px;
  font-weight: 500;
  line-height: 1.05;
  letter-spacing: -.03em;
  color: var(--text-primary);
  max-width: 1200px;
  margin-bottom: 32px;
}

.cover-sub {
  font-size: 28px;
  color: var(--text-secondary);
  max-width: 800px;
}
```

**Animation:** Spark scales in (`.from-scale`), title fades up (`.reveal`), sub fades up delayed.

---

## Format 2: Agenda

**When to use:** Roadmap of 3–4 sections at the top of a deck. Current item filled red, rest outlined.

```html
<section class="slide agenda-slide" data-slide="2">
  <div class="slide-inner">
    <p class="slide-eyebrow reveal">Agenda</p>
    <div class="agenda-list stagger">
      <div class="agenda-item active reveal">
        <div class="agenda-num">01</div>
        <div class="agenda-body">
          <strong>First section</strong>
          <span>One-line description of this section.</span>
        </div>
      </div>
      <div class="agenda-item reveal">
        <div class="agenda-num">02</div>
        <div class="agenda-body">
          <strong>Second section</strong>
          <span>One-line description of this section.</span>
        </div>
      </div>
      <div class="agenda-item reveal">
        <div class="agenda-num">03</div>
        <div class="agenda-body">
          <strong>Third section</strong>
          <span>One-line description of this section.</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

```css
.agenda-list { display: flex; flex-direction: column; gap: 32px; max-width: 900px; }

.agenda-item {
  display: flex; align-items: flex-start; gap: 40px;
  padding: 28px 36px;
  border: 1.5px solid var(--border);
  border-radius: 12px;
}

.agenda-item.active {
  border-color: var(--accent);
  background: var(--accent-dim);
}

.agenda-num {
  font-family: var(--font-title);
  font-size: 48px;
  font-weight: 500;
  color: var(--text-secondary);
  line-height: 1;
  min-width: 64px;
}

.agenda-item.active .agenda-num { color: var(--accent); }

.agenda-body { display: flex; flex-direction: column; gap: 6px; }
.agenda-body strong { font-size: 26px; font-weight: 600; color: var(--text-primary); }
.agenda-body span { font-size: 20px; color: var(--text-secondary); }
```

**Animation:** Items stagger in from-left. Active item pulses subtly on loop.

---

## Format 3: Two-Column

**When to use:** Pair a tight point with a real visual — mock, screenshot, chart, or animated illustration.

```html
<section class="slide two-col-slide" data-slide="3">
  <div class="slide-inner two-col-inner">
    <div class="two-col-left">
      <h2 class="slide-title reveal">Two-column layout</h2>
      <p class="slide-sub reveal">
        Pair a tight sentence with a real visual. Use this when you want a screenshot,
        mock, or chart to do the heavy lifting alongside one clear point.
      </p>
      <ul class="check-list stagger">
        <li class="reveal">✓ Works with screenshots, mocks, or SVGs</li>
        <li class="reveal">✓ Auto-balances on every viewport</li>
      </ul>
    </div>
    <div class="two-col-right reveal from-right">
      <!-- Place mock, screenshot, chart, or animated SVG illustration here -->
      <figure class="mock-frame">
        <div class="mock-titlebar">
          <span class="mock-dot red"></span>
          <span class="mock-dot"></span>
          <span class="mock-dot"></span>
        </div>
        <div class="mock-body">
          <!-- inline SVG illustration or img tag -->
        </div>
      </figure>
    </div>
  </div>
</section>
```

```css
.two-col-inner { flex-direction: row; align-items: center; gap: 80px; }
.two-col-left { flex: 1; }
.two-col-right { flex: 1; display: flex; align-items: center; justify-content: center; }

.check-list { list-style: none; display: flex; flex-direction: column; gap: 16px; }
.check-list li { font-size: 24px; color: var(--text-secondary); }
.check-list li::first-letter { color: var(--accent); font-weight: 700; }

.mock-frame {
  width: 100%; max-width: 680px;
  background: var(--surface);
  border-radius: 12px;
  box-shadow: 0 24px 60px rgba(0,0,0,.10);
  overflow: hidden;
}
.mock-titlebar {
  display: flex; gap: 8px; padding: 16px 20px;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
}
.mock-dot {
  width: 12px; height: 12px; border-radius: 50%;
  background: var(--border);
}
.mock-dot.red { background: var(--accent); }
.mock-body { padding: 28px; min-height: 320px; }
```

**Animation:** Left content stagger-reveals. Right mock slides in from-right.

---

## Format 4: Stat Grid

**When to use:** KPIs and big numbers. Each stat counts up from 0 on slide entry.

```html
<section class="slide stat-slide" data-slide="4">
  <div class="slide-inner">
    <h2 class="slide-title reveal">Stat grid</h2>
    <p class="slide-sub reveal">Use this for KPIs and big numbers. Each stat counts up from zero when the slide appears.</p>
    <div class="stat-grid stagger">
      <div class="stat-cell reveal">
        <div class="stat-number">
          <span class="stat-val" data-target="900" data-suffix="M">0</span>
        </div>
        <div class="stat-label">Monthly users</div>
        <div class="stat-note">Placeholder metric</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-cell reveal">
        <div class="stat-number">
          <span class="stat-val" data-target="3" data-suffix="×">0</span>
        </div>
        <div class="stat-label">Faster</div>
        <div class="stat-note">Placeholder metric</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-cell reveal">
        <div class="stat-number">
          <span class="stat-val" data-target="40" data-suffix="%">0</span>
        </div>
        <div class="stat-label">Lower cost</div>
        <div class="stat-note">Placeholder metric</div>
      </div>
    </div>
  </div>
</section>
```

```css
.stat-grid { display: flex; align-items: stretch; gap: 0; margin-top: 40px; flex: 1; }
.stat-cell { flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 0 60px; }
.stat-divider { width: 1px; background: var(--border); flex-shrink: 0; }

.stat-number {
  font-family: var(--font-title);
  font-size: 120px;
  font-weight: 500;
  line-height: 1;
  color: var(--accent);
  letter-spacing: -.04em;
  margin-bottom: 16px;
}

.stat-label { font-size: 28px; font-weight: 600; color: var(--text-primary); margin-bottom: 8px; }
.stat-note { font-size: 20px; color: var(--text-secondary); }
```

**Animation:** Title + sub fade up. Cells stagger in. Numbers count up from 0 (JS `data-target`).
See `countUp()` in ANIMATION-TOOLKIT.md.

---

## Format 5: Feature Bento

**When to use:** Showcase 4–6 features in a bento/card grid. Each card has a hand-built SVG icon — no emoji.

```html
<section class="slide bento-slide" data-slide="5">
  <div class="slide-inner">
    <h2 class="slide-title reveal">Feature bento</h2>
    <div class="bento-grid stagger">
      <div class="bento-card reveal">
        <div class="bento-icon">
          <!-- Inline SVG icon, drawn with var(--accent) or var(--text-secondary) -->
          <svg viewBox="0 0 40 40" fill="none">
            <rect x="4" y="8" width="32" height="4" rx="2" fill="var(--accent)"/>
            <rect x="4" y="18" width="24" height="4" rx="2" fill="var(--text-secondary)"/>
            <rect x="4" y="28" width="28" height="4" rx="2" fill="var(--text-secondary)"/>
          </svg>
        </div>
        <div class="bento-label">Feature name</div>
        <div class="bento-desc">Brief one-line description.</div>
      </div>
      <!-- Repeat for each feature (4–6 cards) -->
    </div>
  </div>
</section>
```

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 32px;
  flex: 1;
}

.bento-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 36px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  transition: box-shadow 0.3s ease;
}

.bento-card:hover { box-shadow: 0 8px 32px rgba(0,0,0,.08); }

.bento-icon { width: 40px; height: 40px; }
.bento-label { font-size: 22px; font-weight: 600; color: var(--text-primary); }
.bento-desc { font-size: 18px; color: var(--text-secondary); line-height: 1.5; }
```

**Animation:** Cards stagger in with fade+scale from `from-scale` variant.

---

## Format 6: Comparison

**When to use:** Side-by-side table contrasting two options. Left column = feature, center = us (accent-tinted), right = them.

```html
<section class="slide comparison-slide" data-slide="6">
  <div class="slide-inner">
    <h2 class="slide-title reveal">Comparison</h2>
    <p class="slide-sub reveal">Use this when you need to contrast two options or show tradeoffs side by side.</p>
    <div class="comp-table reveal">
      <div class="comp-header">
        <div class="comp-col-feature"></div>
        <div class="comp-col-us">Us</div>
        <div class="comp-col-them">Them</div>
      </div>
      <div class="comp-row">
        <div class="comp-feature">Built in one prompt</div>
        <div class="comp-us">✓</div>
        <div class="comp-them">✗</div>
      </div>
      <div class="comp-row">
        <div class="comp-feature">Single shareable HTML file</div>
        <div class="comp-us">✓</div>
        <div class="comp-them">✗</div>
      </div>
      <!-- Add rows as needed -->
    </div>
  </div>
</section>
```

```css
.comp-table { width: 100%; border-collapse: collapse; flex: 1; }

.comp-header, .comp-row {
  display: grid;
  grid-template-columns: 1fr 240px 240px;
  border-bottom: 1px solid var(--border);
}

.comp-header { font-size: 20px; font-weight: 600; padding-bottom: 16px; }
.comp-col-us { background: var(--accent-dim); color: var(--accent); text-align: center; padding: 16px; font-weight: 700; }
.comp-col-them { text-align: center; padding: 16px; color: var(--text-secondary); }

.comp-row { align-items: center; }
.comp-feature { padding: 20px 0; font-size: 22px; color: var(--text-primary); }
.comp-us { background: var(--accent-dim); text-align: center; padding: 20px 16px; color: var(--accent); font-size: 22px; font-weight: 700; }
.comp-them { text-align: center; padding: 20px 16px; color: var(--text-secondary); font-size: 22px; }
```

**Animation:** Header and rows cascade in with stagger from-left.

---

## Format 7: Process / Steps

**When to use:** 3–4 steps connected by animated dashed arrows. Icons are hand-built SVG circles with inline drawings.

```html
<section class="slide steps-slide" data-slide="7">
  <div class="slide-inner">
    <h2 class="slide-title reveal">Steps</h2>
    <p class="slide-sub reveal">Use this for a multi-stage process or workflow — three to four steps connected by arrows.</p>
    <div class="steps-row stagger">
      <div class="step-node reveal">
        <div class="step-disc">
          <!-- Inline SVG icon -->
          <svg viewBox="0 0 48 48" fill="none">
            <rect x="10" y="14" width="28" height="3" rx="1.5" fill="var(--text-primary)"/>
            <rect x="10" y="22" width="20" height="3" rx="1.5" fill="var(--accent)"/>
            <rect x="10" y="30" width="24" height="3" rx="1.5" fill="var(--text-secondary)"/>
          </svg>
        </div>
        <div class="step-label">Step one</div>
        <div class="step-desc">Brief description of this step.</div>
      </div>
      <div class="step-arrow">
        <svg class="draw-line" viewBox="0 0 80 20" fill="none" width="120">
          <line x1="0" y1="10" x2="68" y2="10" stroke="var(--accent)" stroke-width="2" stroke-dasharray="6 4"/>
          <path d="M64 5 L80 10 L64 15" fill="none" stroke="var(--accent)" stroke-width="2"/>
        </svg>
      </div>
      <div class="step-node reveal">
        <!-- Step 2 -->
      </div>
      <div class="step-arrow"><!-- arrow SVG --></div>
      <div class="step-node reveal">
        <!-- Step 3 -->
      </div>
    </div>
  </div>
</section>
```

```css
.steps-row {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  gap: 0;
  margin-top: 48px;
  flex: 1;
}

.step-node {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  width: 260px;
  gap: 20px;
}

.step-disc {
  width: 120px; height: 120px;
  border-radius: 50%;
  background: var(--surface);
  border: 1.5px solid var(--border);
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 8px 32px rgba(0,0,0,.06);
}

.step-disc svg { width: 48px; height: 48px; }
.step-label { font-size: 28px; font-weight: 600; color: var(--text-primary); }
.step-desc { font-size: 18px; color: var(--text-secondary); line-height: 1.5; }

.step-arrow {
  display: flex; align-items: center;
  padding-top: 50px; /* aligns with center of disc */
  flex-shrink: 0;
}
```

**Animation:** Nodes stagger-reveal left to right. Dashed arrow draws itself with `.draw-line` class on the SVG line element.

---

## Format 8: Roadmap / Timeline

**When to use:** Milestone cards across quarters or sprints — past, present, next. Horizontal line connects filled dots. Current milestone pulsing.

```html
<section class="slide roadmap-slide" data-slide="8">
  <div class="slide-inner">
    <h2 class="slide-title reveal">Roadmap</h2>
    <p class="slide-sub reveal">Use this to walk through milestones across quarters or sprints — past, present, and next.</p>
    <div class="tl-track reveal">
      <div class="tl-line"></div>
      <div class="tl-items stagger">
        <div class="tl-step done reveal">
          <div class="tl-marker">Q1</div>
          <div class="tl-body">
            <div class="tl-head">First milestone</div>
            <div class="tl-desc">Placeholder description for the past quarter.</div>
          </div>
        </div>
        <div class="tl-step done reveal">
          <div class="tl-marker">Q2</div>
          <div class="tl-body">
            <div class="tl-head">Second milestone</div>
            <div class="tl-desc">Placeholder description for what landed.</div>
          </div>
        </div>
        <div class="tl-step now reveal">
          <div class="tl-label-now">NOW</div>
          <div class="tl-marker pulse">Q3</div>
          <div class="tl-body">
            <div class="tl-head">Current focus</div>
            <div class="tl-desc">Placeholder for the in-flight quarter.</div>
          </div>
        </div>
        <div class="tl-step next reveal">
          <div class="tl-label-next">NEXT</div>
          <div class="tl-marker outline">Q4</div>
          <div class="tl-body">
            <div class="tl-head">Coming up</div>
            <div class="tl-desc">Placeholder for the next bet.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

```css
.tl-track { position: relative; margin-top: 48px; flex: 1; display: flex; flex-direction: column; justify-content: center; }

.tl-line {
  position: absolute;
  top: 60px; /* center of markers */
  left: 60px;
  right: 60px;
  height: 2px;
  background: var(--border);
}

.tl-items { display: flex; justify-content: space-between; position: relative; z-index: 1; }

.tl-step { display: flex; flex-direction: column; align-items: center; text-align: center; flex: 1; gap: 16px; }

.tl-marker {
  width: 80px; height: 80px;
  border-radius: 50%;
  background: var(--accent);
  color: var(--on-accent);
  font-family: var(--font-title);
  font-size: 24px;
  font-weight: 600;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 8px 24px rgba(211,11,0,.25);
}

.tl-marker.outline {
  background: transparent;
  border: 2px solid var(--border);
  color: var(--text-secondary);
  box-shadow: none;
}

.tl-marker.pulse { animation: tl-pulse 2s ease-in-out infinite; }
@keyframes tl-pulse {
  0%, 100% { box-shadow: 0 8px 24px rgba(211,11,0,.25), 0 0 0 0 rgba(211,11,0,.0); }
  50%       { box-shadow: 0 8px 24px rgba(211,11,0,.25), 0 0 0 12px rgba(211,11,0,.10); }
}

.tl-label-now, .tl-label-next {
  font-size: 14px; font-weight: 700; letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--accent);
  height: 20px;
}
.tl-label-next { color: var(--text-secondary); }

.tl-head { font-size: 24px; font-weight: 600; color: var(--text-primary); margin-bottom: 8px; }
.tl-desc { font-size: 18px; color: var(--text-secondary); line-height: 1.5; max-width: 200px; }
```

**Animation:** Slide title + sub fade up. Timeline line draws left-to-right (`.draw-line` on `.tl-line`). Milestone nodes stagger in. Current marker pulses on loop.

---

## Format 9: Chart

**When to use:** Quantitative substance. Chart.js renders stacked bars (P0), donut/pie (P1), line, or grouped bar. Monochrome tint ramp on `--accent`. Hover tooltips. Never rainbow.

```html
<section class="slide chart-slide" data-slide="9">
  <div class="slide-inner">
    <h2 class="slide-title reveal">Chart</h2>
    <p class="slide-sub reveal">Use this when the deck needs quantitative substance. Charts render with Chart.js and inherit the deck's accent color.</p>
    <div class="chart-wrap reveal">
      <canvas id="slide-chart"></canvas>
    </div>
  </div>
</section>
```

```css
.chart-wrap {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 40px 48px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.chart-wrap canvas { max-height: 480px; }
```

**JS — Chart initialization (add inside SlidePresentation or DOMContentLoaded):**

```javascript
function initChart() {
  const ctx = document.getElementById('slide-chart');
  if (!ctx) return;

  // Monochrome tint ramp — derive from accent using opacity
  const accent = getComputedStyle(document.documentElement)
    .getPropertyValue('--accent').trim() || '#D30B00';

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'],
      datasets: [
        { label: 'Product',     data: [14, 20, 28, 34, 42], backgroundColor: accent },
        { label: 'Marketing',   data: [6,  10, 12, 18, 22], backgroundColor: accent + 'CC' },
        { label: 'Engineering', data: [4,  5,  5,  6,  8],  backgroundColor: accent + '55' },
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: { position: 'top', labels: { font: { family: 'Manrope', size: 14 } } },
        tooltip: { mode: 'index', intersect: false }
      },
      scales: {
        x: { stacked: true, grid: { display: false } },
        y: { stacked: true, beginAtZero: true }
      },
      animation: { duration: 1200, easing: 'easeOutQuart' }
    }
  });
}
```

Load Chart.js from CDN in `<head>`:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.3/dist/chart.umd.min.js"></script>
```

**Animation:** Chart bars grow up from baseline on first render (Chart.js built-in animation). Container fades in on slide entry.

---

## Format 10: Code Block

**When to use:** Technical walkthroughs where the snippet is the visual. Two-column: left = context text, right = dark editor card with syntax-highlighted code and blinking cursor.

```html
<section class="slide code-slide" data-slide="10">
  <div class="slide-inner two-col-inner">
    <div class="two-col-left">
      <h2 class="slide-title reveal">Code block</h2>
      <p class="slide-sub reveal">Use this for tutorials and technical walkthroughs where the snippet is the visual.</p>
    </div>
    <div class="two-col-right reveal from-right">
      <div class="code-card scan-wrap lum-glow">
        <div class="code-head">
          <span class="code-dot red"></span>
          <span class="code-dot yellow"></span>
          <span class="code-dot green"></span>
        </div>
        <pre class="code-body"><code><span class="code-comment">// in Claude Code:</span>
<span class="code-prompt">&gt;</span> <span class="code-cmd">/slides</span>

<span class="code-comment">// topic?</span>
<span class="code-prompt">&gt;</span> Q4 strategy review

<span class="code-comment">// template?</span>
<span class="code-prompt">&gt;</span> default

<span class="code-tick">✓</span> 8 slides generated
<span class="code-tick">✓</span> Visual QA passed
<span class="code-tick">—</span> output/slides/q4-review.html<span class="code-cursor">█</span></code></pre>
      </div>
    </div>
  </div>
</section>
```

```css
.code-card {
  background: #1d1d1f;
  border-radius: 12px;
  box-shadow: 0 24px 60px rgba(0,0,0,.28);
  overflow: hidden;
  width: 100%;
  max-width: 660px;
}

.code-head {
  display: flex; gap: 8px; padding: 16px 20px;
  background: #2a2a2e;
}

.code-dot {
  width: 12px; height: 12px; border-radius: 50%;
  background: #444;
}
.code-dot.red    { background: #ff5f56; }
.code-dot.yellow { background: #ffbd2e; }
.code-dot.green  { background: #27c93f; }

.code-body {
  padding: 28px;
  font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
  font-size: 18px;
  line-height: 1.7;
  color: #e8e8ea;
  overflow: hidden;
  margin: 0;
}

.code-comment { color: rgba(255,255,255,.40); }
.code-prompt  { color: var(--accent); }
.code-cmd     { color: #5ba8f5; }
.code-tick    { color: #27c93f; }
.code-cursor  {
  color: var(--accent);
  animation: blink 1.2s step-end infinite;
}
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
```

**Animation:** Left text fades up. Code card slides in from right (`from-right`). On entry, a luminescence glow sweeps from top to bottom across the card (`.lum-glow` class triggers `.lum-sweep` pseudo-element animation, delayed 0.6s after the card appears). Cursor blinks on loop (`.blink`).

```css
/* Luminescence glow sweep — used on Code Block and Quote formats */
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
/* Trigger: fires once when slide becomes visible */
.slide.visible .lum-glow::after {
  animation: lum-sweep 1.1s cubic-bezier(0.16, 1, 0.3, 1) 0.6s forwards;
}
@keyframes lum-sweep {
  from { transform: translateY(-110%); }
  to   { transform: translateY(110%); }
}
```

---

## Format 11: Quote

**When to use:** Anchor with a powerful testimonial or pull-quote. Two-column: left = large serif quote text, right = dark portrait/logo card.

```html
<section class="slide quote-slide slide--dark" data-slide="11">
  <div class="slide-inner two-col-inner" style="gap: 100px;">
    <div class="two-col-left">
      <div class="quote-mark reveal" aria-hidden="true">❝</div>
      <blockquote class="quote-text reveal lum-glow">
        Use this to anchor your message with a powerful
        <em class="accent-word">testimonial</em> or pull-quote.
      </blockquote>
      <cite class="quote-attr reveal">Speaker Name · Role or context</cite>
    </div>
    <div class="two-col-right reveal from-right">
      <div class="portrait-card lum-glow">
        <div class="quote-icon">❝</div>
      </div>
    </div>
  </div>
</section>
```

```css
.quote-mark {
  font-family: var(--font-title);
  font-size: 80px;
  color: var(--accent);
  line-height: 1;
  margin-bottom: -16px;
}

.quote-text {
  font-family: var(--font-title);
  font-size: 52px;
  font-weight: 500;
  line-height: 1.25;
  color: var(--text-primary);
  margin-bottom: 32px;
  font-style: normal;
}

.quote-attr {
  font-size: 20px;
  color: var(--text-secondary);
  font-style: normal;
  letter-spacing: .04em;
}

.portrait-card {
  width: 320px; height: 320px;
  border-radius: 16px;
  background: linear-gradient(145deg, rgba(211,11,0,.08), rgba(211,11,0,.20));
  border: 1px solid rgba(211,11,0,.25);
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 24px 80px rgba(0,0,0,.18);
}

.quote-icon {
  font-size: 96px;
  color: rgba(255,255,255,.15);
  font-family: var(--font-title);
  line-height: 1;
}
```

**Animation:** Quote mark scales in (`.from-scale`). Quote text fades up with a luminescence glow sweeping top-to-bottom on entry (`.lum-glow` on the blockquote, delayed 0.5s). Attribution fades up. Portrait card slides in from right and receives its own luminescence sweep (`.lum-glow` on `.portrait-card`, delayed 0.7s), then floats gently on loop (`.float`).

---

## Format 12: Closing / CTA

**When to use:** Final slide. Near-black background. Spark mark, big closing line, one clear next action.

```html
<section class="slide slide--dark closing-slide" data-slide="12">
  <div class="slide-inner closing-inner">
    <svg class="spark reveal from-scale" viewBox="0 0 48 48" fill="none">
      <path d="M24 4 L26.5 21.5 L44 24 L26.5 26.5 L24 44 L21.5 26.5 L4 24 L21.5 21.5 Z"
            fill="var(--accent)"/>
    </svg>
    <h1 class="closing-title reveal">
      Thanks for <em class="accent-word">listening</em>
    </h1>
    <p class="closing-sub reveal">A short closing line or CTA</p>
    <a class="closing-cta reveal" href="#">Get started →</a>
  </div>
</section>
```

```css
.closing-inner { justify-content: center; padding: 120px 160px; }

.closing-title {
  font-family: var(--font-title);
  font-size: 96px;
  font-weight: 500;
  line-height: 1.05;
  letter-spacing: -.03em;
  color: var(--text-primary);
  margin-bottom: 28px;
}

.closing-sub {
  font-size: 30px;
  color: var(--text-secondary);
  margin-bottom: 56px;
}

.closing-cta {
  display: inline-block;
  padding: 20px 48px;
  background: var(--accent);
  color: var(--on-accent);
  font-family: var(--font-body);
  font-size: 22px;
  font-weight: 600;
  border-radius: 8px;
  text-decoration: none;
  letter-spacing: .02em;
  transition: opacity .2s;
}
.closing-cta:hover { opacity: .88; }
```

**Animation:** Identical to Cover. Spark scales in, title fades up, CTA button fades in last.

---

## Slide Presentation Controller

Include this complete JS in every deck:

```javascript
class SlidePresentation {
  constructor() {
    this.slides      = Array.from(document.querySelectorAll('.slide'));
    this.current     = 0;
    this.stage       = document.getElementById('deckStage');
    this.navDots     = document.getElementById('navDots');
    this.total       = this.slides.length;

    this.setupStageScale();
    this.setupKeyboard();
    this.setupTouch();
    this.setupWheel();
    this.buildNav();
    this.showSlide(0, false);
    this.initCountUps();
    this.initDrawLines();
    this.initChart && this.initChart();
  }

  setupStageScale() {
    const scale = () => {
      const f = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
      const x = (window.innerWidth  - 1920 * f) / 2;
      const y = (window.innerHeight - 1080 * f) / 2;
      this.stage.style.transform = `translate(${x}px,${y}px) scale(${f})`;
    };
    scale();
    window.addEventListener('resize', scale);
  }

  setupKeyboard() {
    document.addEventListener('keydown', e => {
      if (e.target.getAttribute('contenteditable')) return;
      if (['ArrowRight','ArrowDown','Space',' '].includes(e.key)) { e.preventDefault(); this.next(); }
      if (['ArrowLeft','ArrowUp'].includes(e.key)) { e.preventDefault(); this.prev(); }
    });
  }

  setupTouch() {
    let sx = 0, sy = 0;
    document.addEventListener('touchstart', e => { sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, { passive: true });
    document.addEventListener('touchend', e => {
      const dx = sx - e.changedTouches[0].clientX;
      const dy = sy - e.changedTouches[0].clientY;
      if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) dx > 0 ? this.next() : this.prev();
    });
  }

  setupWheel() {
    let last = 0;
    document.addEventListener('wheel', e => {
      if (Date.now() - last < 800) return;
      last = Date.now();
      e.deltaY > 0 ? this.next() : this.prev();
    }, { passive: true });
  }

  buildNav() {
    if (!this.navDots) return;
    this.navDots.innerHTML = '';
    this.slides.forEach((_, i) => {
      const d = document.createElement('button');
      d.className = 'nav-dot';
      d.setAttribute('aria-label', `Slide ${i + 1}`);
      d.addEventListener('click', () => this.showSlide(i));
      this.navDots.appendChild(d);
    });
  }

  showSlide(index, animate = true) {
    const prev = this.current;
    this.current = Math.max(0, Math.min(index, this.total - 1));

    this.slides.forEach((s, i) => {
      s.classList.toggle('active',  i === this.current);
      s.classList.toggle('visible', i === this.current);
    });


    // Nav dots
    if (this.navDots) {
      Array.from(this.navDots.children).forEach((d, i) => {
        d.classList.toggle('active', i === this.current);
      });
    }

    // Trigger count-ups on new slide
    if (animate) this.triggerCountUps(this.current);
  }

  next() { this.showSlide(this.current + 1); }
  prev() { this.showSlide(this.current - 1); }

  /* ── Count-up animation ── */
  initCountUps() {
    this._countUpDone = new Set();
  }

  triggerCountUps(slideIndex) {
    const slide = this.slides[slideIndex];
    if (!slide || this._countUpDone.has(slideIndex)) return;
    const vals = slide.querySelectorAll('.stat-val[data-target]');
    if (!vals.length) return;
    this._countUpDone.add(slideIndex);

    vals.forEach(el => {
      const target = parseFloat(el.dataset.target);
      const suffix = el.dataset.suffix || '';
      const duration = 1400;
      const start = performance.now();

      const tick = (now) => {
        const t = Math.min((now - start) / duration, 1);
        const ease = 1 - Math.pow(1 - t, 3); // ease-out-cubic
        const val = Math.round(ease * target);
        el.textContent = val + suffix;
        if (t < 1) requestAnimationFrame(tick);
        else el.textContent = target + suffix;
      };
      requestAnimationFrame(tick);
    });
  }

  /* ── Draw-line animation ── */
  initDrawLines() {
    document.querySelectorAll('.draw-line').forEach(el => {
      const len = el.getTotalLength ? el.getTotalLength() : 200;
      el.style.strokeDasharray  = len;
      el.style.strokeDashoffset = len;
      el.style.transition = 'stroke-dashoffset 0.9s cubic-bezier(0.16,1,0.3,1) 0.3s';
    });
  }

  triggerDrawLines(slideIndex) {
    const slide = this.slides[slideIndex];
    if (!slide) return;
    slide.querySelectorAll('.draw-line').forEach(el => {
      el.style.strokeDashoffset = '0';
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.presentation = new SlidePresentation();
});
```

### Progress Bar + Nav Dots HTML (outside `.deck-stage`)

```html


<!-- Nav dots -->
<nav id="navDots" style="
  position: fixed; right: 20px; top: 50%;
  transform: translateY(-50%);
  display: flex; flex-direction: column; gap: 10px;
  z-index: 9999;
"></nav>

<style>
.nav-dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  background: rgba(16,2,2,.20);
  border: none; cursor: pointer; padding: 0;
  transition: background .25s, transform .25s;
}
.nav-dot.active {
  background: var(--accent, #D30B00);
  transform: scale(1.35);
}
</style>
```

---

## Inline Editing

Include by default. Reveals on hover over top-left corner or pressing `E`.

```html
<div class="edit-hotzone"></div>
<button class="edit-toggle" id="editToggle" title="Edit mode (E)">✏️</button>
```

```css
.edit-hotzone {
  position: fixed; top: 0; left: 0;
  width: 80px; height: 80px;
  z-index: 10000; cursor: pointer;
}
.edit-toggle {
  position: fixed; top: 16px; left: 16px;
  opacity: 0; pointer-events: none;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 8px; padding: 8px 12px;
  font-size: 18px; cursor: pointer;
  transition: opacity .3s ease;
  z-index: 10001;
}
.edit-toggle.show, .edit-toggle.active { opacity: 1; pointer-events: auto; }
```

```javascript
const hotzone   = document.querySelector('.edit-hotzone');
const editBtn   = document.getElementById('editToggle');
let editActive  = false;
let hideTimer   = null;

function toggleEdit() {
  editActive = !editActive;
  editBtn.classList.toggle('active', editActive);
  document.querySelectorAll('.slide.active [data-editable], .slide.active h1, .slide.active h2, .slide.active p, .slide.active li')
    .forEach(el => el.setAttribute('contenteditable', editActive ? 'true' : 'false'));
}

hotzone.addEventListener('mouseenter', () => { clearTimeout(hideTimer); editBtn.classList.add('show'); });
hotzone.addEventListener('mouseleave', () => { hideTimer = setTimeout(() => { if (!editActive) editBtn.classList.remove('show'); }, 400); });
editBtn.addEventListener('mouseenter', () => clearTimeout(hideTimer));
editBtn.addEventListener('mouseleave', () => { hideTimer = setTimeout(() => { if (!editActive) editBtn.classList.remove('show'); }, 400); });
editBtn.addEventListener('click',      () => toggleEdit());
hotzone.addEventListener('click',      () => toggleEdit());
document.addEventListener('keydown', e => {
  if ((e.key === 'e' || e.key === 'E') && !e.target.getAttribute('contenteditable')) toggleEdit();
});
```
