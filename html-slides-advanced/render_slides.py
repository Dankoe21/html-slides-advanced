#!/usr/bin/env python3
"""
render_slides.py — Visual QA renderer for html-slides-advanced
-------------------------------------------------------------
Captures each slide in an HTML presentation as a PNG image.
Uses Playwright (headless Chromium) so fonts, CSS variables,
and Chart.js all render exactly as they appear in the browser.

Usage:
    python3 render_slides.py --html output/slides/my-deck.html
    python3 render_slides.py --html output/slides/my-deck.html --out output/slides/qa/
    python3 render_slides.py --html output/slides/my-deck.html --width 1920 --height 1080

Output:
    Prints one absolute image path per line (for subagent inspection).
    Images saved to --out directory as slide-01.png, slide-02.png, ...

Requirements:
    pip install playwright
    playwright install chromium
"""

import argparse
import os
import sys
import time
from pathlib import Path


def install_playwright():
    """Auto-install playwright if missing."""
    try:
        import playwright  # noqa: F401
    except ImportError:
        print("[render_slides] Installing playwright...", file=sys.stderr)
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "--quiet"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium", "--quiet"])
        print("[render_slides] playwright installed.", file=sys.stderr)


def render_slides(html_path: str, out_dir: str, width: int = 1920, height: int = 1080) -> list[str]:
    """
    Render each slide in an HTML presentation to PNG.

    Strategy:
    1. Inject a small JS snippet that:
       a. Removes scroll-snap so Playwright can control slide visibility.
       b. Forces all animations to their final state (sets .visible on every slide,
          removes transitions temporarily, then re-hides all but the target slide).
       c. Exposes window.__totalSlides and window.__goToSlide(n).
    2. Navigate to each slide by index, screenshot the viewport.
    3. Save PNGs to out_dir/slide-NN.png.

    Returns a list of absolute PNG paths (one per slide), printed to stdout.
    """
    install_playwright()

    from playwright.sync_api import sync_playwright  # noqa: E402

    html_path = Path(html_path).resolve()
    if not html_path.exists():
        print(f"[render_slides] ERROR: file not found: {html_path}", file=sys.stderr)
        sys.exit(1)

    out_path = Path(out_dir).resolve()
    out_path.mkdir(parents=True, exist_ok=True)

    # Injection script — runs in the page context after load
    INJECT_JS = """
    (() => {
      // 1. Freeze all transitions so screenshots capture final state
      const style = document.createElement('style');
      style.id = '__qa_freeze';
      style.textContent = `
        *, *::before, *::after {
          animation-duration:        0.001ms !important;
          animation-delay:           0ms     !important;
          transition-duration:       0.001ms !important;
          transition-delay:          0ms     !important;
        }
        /* Force draw-line SVGs to their end state */
        .draw-line { stroke-dashoffset: 0 !important; }
        /* Force stat counters to show target value (handled by data-target below) */
      `;
      document.head.appendChild(style);

      // 2. Trigger all count-up values to their target immediately
      document.querySelectorAll('.stat-val[data-target]').forEach(el => {
        el.textContent = el.dataset.target + (el.dataset.suffix || '');
      });

      // 3. Remove scroll-snap from html element
      document.documentElement.style.scrollSnapType = 'none';
      document.body.style.overflow = 'hidden';

      // 4. Expose slide control helpers
      const slides = Array.from(document.querySelectorAll('.slide'));
      window.__totalSlides = slides.length;

      window.__goToSlide = function(index) {
        slides.forEach((s, i) => {
          const active = i === index;
          s.classList.toggle('active',  active);
          s.classList.toggle('visible', active);
          // Force visible state on all child .reveal elements so nothing is hidden
          if (active) {
            s.querySelectorAll('.reveal, .from-left, .from-right, .from-scale, .from-blur, .fade-only').forEach(el => {
              el.style.opacity   = '1';
              el.style.transform = 'none';
              el.style.filter    = 'none';
            });
            // Also trigger chart rendering if present
            if (window.presentation && window.presentation.triggerCountUps) {
              window.presentation.triggerCountUps(index);
            }
          }
        });
        return slides[index] ? slides[index].className : 'not-found';
      };

      // 5. Disable the QA freeze after initial load so Chart.js can render
      //    (Chart.js uses requestAnimationFrame — remove freeze after 200ms)
      setTimeout(() => {
        const el = document.getElementById('__qa_freeze');
        if (el) el.remove();
      }, 250);

    })();
    """

    saved_paths = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
        )

        page = browser.new_page(viewport={"width": width, "height": height})

        # Load the HTML file via file:// URL so relative paths and local fonts work
        url = html_path.as_uri()
        print(f"[render_slides] Loading: {url}", file=sys.stderr)
        page.goto(url, wait_until="networkidle", timeout=30_000)

        # Give fonts and Chart.js a moment to render
        page.wait_for_timeout(800)

        # Inject control helpers
        page.evaluate(INJECT_JS)
        page.wait_for_timeout(300)  # wait for freeze timeout to clear

        total = page.evaluate("window.__totalSlides || 0")
        if total == 0:
            print("[render_slides] ERROR: no .slide elements found in the document.", file=sys.stderr)
            print("[render_slides] Ensure slides use class='slide'.", file=sys.stderr)
            browser.close()
            sys.exit(1)

        print(f"[render_slides] Found {total} slides. Rendering...", file=sys.stderr)

        for i in range(total):
            # Navigate to the slide
            page.evaluate(f"window.__goToSlide({i})")
            # Wait for Chart.js animation or any deferred render
            page.wait_for_timeout(400)

            # Screenshot the full viewport
            slide_num = str(i + 1).zfill(2)
            out_file = out_path / f"slide-{slide_num}.png"
            page.screenshot(path=str(out_file), full_page=False)

            abs_path = str(out_file.resolve())
            saved_paths.append(abs_path)
            print(abs_path)  # stdout: one path per line (for subagent)
            print(f"[render_slides]   slide-{slide_num}.png ✓", file=sys.stderr)

        browser.close()

    print(f"\n[render_slides] Done. {len(saved_paths)} slides saved to: {out_path}", file=sys.stderr)
    return saved_paths


def main():
    parser = argparse.ArgumentParser(
        description="Render HTML slide deck to PNG images for Visual QA."
    )
    parser.add_argument(
        "--html", required=True,
        help="Path to the HTML presentation file."
    )
    parser.add_argument(
        "--out", default=None,
        help="Output directory for PNG images. Defaults to <html_dir>/qa/."
    )
    parser.add_argument(
        "--width", type=int, default=1920,
        help="Viewport width in pixels (default: 1920)."
    )
    parser.add_argument(
        "--height", type=int, default=1080,
        help="Viewport height in pixels (default: 1080)."
    )

    args = parser.parse_args()

    html_path = Path(args.html)
    if args.out:
        out_dir = args.out
    else:
        out_dir = html_path.parent / "qa"

    render_slides(
        html_path=str(html_path),
        out_dir=str(out_dir),
        width=args.width,
        height=args.height,
    )


if __name__ == "__main__":
    main()
