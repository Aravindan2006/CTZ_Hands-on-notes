# Hands-On 2 — CSS Flexbox, Grid & Responsive Design

Extends Hands-On 1 with a Flexbox header/hero/stats-bar layout, a CSS
Grid course-card layout, and mobile-first responsive breakpoints.

## Files

- `index.html` — adds a stats bar and 5 course cards wrapped in `.course-grid`
- `styles.css` — Flexbox nav/hero/stats-bar, CSS Grid course layout,
  mobile-first `min-width` media queries at 768px and 1024px
- `app.js` — mobile nav toggle (hamburger button)

## Run

Open `index.html` directly in your browser.

## What's demonstrated

- **Flexbox:** header (`justify-content: space-between`), hero
  (column direction, centred), stats bar (equal spacing via `flex: 1`)
- **CSS Grid:** `.course-grid` — 1 column (mobile) → 2 columns (≥768px)
  → 3 columns (≥1024px); an alternate `.auto-fit` variant using
  `repeat(auto-fit, minmax(280px, 1fr))` needs no media queries at all
- **Mobile-first media queries:** base styles are single-column with no
  media query; `min-width` queries add complexity for larger screens
- **Fluid typography:** `clamp(1.5rem, 4vw, 2.5rem)` on headings
- **Viewport units:** hero `min-height: 40vh`

## Testing responsiveness

Open DevTools (F12) → device toolbar, and test at 375px (mobile),
768px (tablet), and 1280px (desktop). The nav collapses into a
hamburger toggle below 768px and expands to a full inline nav above it.
