# Student Portal — Accessibility & Cross-Browser Edition (Hands-On 9)

A plain HTML5/CSS3/JavaScript Student Portal, audited and fixed
against WCAG 2.1 AA, with documented cross-browser compatibility
testing. No build step or framework — open directly in a browser or
serve with the included static server.

## What's included

- **Semantic HTML5** structure: `<header>`, `<nav>`, `<main>`,
  `<section>`, `<article>`, `<footer>`, correct heading hierarchy.
- **ARIA:** `aria-label` on nav, `aria-current="page"` on the active
  link, `aria-expanded`/`aria-controls` on the mobile nav toggle,
  `role="status" aria-live="polite"` on the search results count and
  form status messages.
- **Keyboard navigation:** every interactive element (nav toggle,
  course cards, buttons, form fields) is reachable and operable via
  keyboard; course cards respond to <kbd>Enter</kbd>/<kbd>Space</kbd>.
- **Visible focus indicator:** a custom, high-contrast
  `:focus-visible` outline on every focusable element — no
  `outline: none` without a replacement.
- **WCAG AA colour contrast:** all text/background pairs verified at
  ≥ 4.5:1 (documented before/after values in `styles.css` and
  `docs/Accessibility_Audit.md`).
- **Responsive, mobile-first layout:** Flexbox header/hero, CSS Grid
  course cards with `auto-fit`/`minmax()`, fluid typography via
  `clamp()`.
- **Feature detection & polyfill notes** instead of browser sniffing.
- Full accessibility audit (before/after Lighthouse scores) and
  cross-browser compatibility documentation in `docs/`.

## Folder structure

```
Frontend_Handson_09_Accessibility/
├── package.json
├── README.md
├── index.html
├── styles.css
├── app.js
├── data.js
├── docs/
│   ├── Accessibility_Audit.md
│   └── Browser_Compatibility.md
└── screenshots/
    └── README.md
```

## Installation

No dependencies are required to simply open the page. To use the
optional local static server:

```bash
cd Frontend_Handson_09_Accessibility
npm install
```

## Run

**Option A — open directly:**
Open `index.html` in your browser (double-click, or "Open File").

**Option B — local static server (recommended, avoids ES module CORS
issues in some browsers when opened via `file://`):**

```bash
npm start
```

Then open http://localhost:5500.

## Testing this project

1. **Lighthouse:** Chrome DevTools → Lighthouse → Accessibility →
   Generate report. Expect a 100/100 score (see
   `docs/Accessibility_Audit.md` for the before/after comparison).
2. **axe DevTools:** install the browser extension, run a scan, and
   confirm zero violations.
3. **Keyboard-only pass:** unplug your mouse (or just don't touch it)
   and Tab through the entire page — every control should be reachable
   and show a visible focus ring.
4. **Cross-browser:** open in Chrome, Firefox, and Safari/Edge and
   compare against `docs/Browser_Compatibility.md`.

## Sample data & API integration

- `data.js` exports 5 sample course objects used to render the course
  grid.
- The Notifications section fetches live data from JSONPlaceholder
  (`/posts?_limit=3`) with a loading state, friendly error message, and
  a Retry button — demonstrating the same async-fetch pattern from
  Hands-On 4, now with accessible loading/error states (`aria-live`
  regions, no console-only error reporting).
