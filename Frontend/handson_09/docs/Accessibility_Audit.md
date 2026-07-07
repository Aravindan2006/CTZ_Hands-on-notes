# Accessibility Audit — Student Portal

## Baseline (Hands-On 1–3 version)

**Lighthouse Accessibility score: 71 / 100**

| # | Issue | Tool | Severity |
|---|---|---|---|
| 1 | `<img>` elements missing `alt` attributes | Lighthouse | Serious |
| 2 | Search input has no associated `<label>` | Lighthouse, axe | Serious |
| 3 | Heading order skips a level (`h1` → `h3`) | Lighthouse | Moderate |
| 4 | Mobile nav toggle is a non-interactive `<span>` | axe | Serious |
| 5 | Course cards are `<div>`s with `onclick`, not keyboard-operable | axe | Critical |
| 6 | Body text contrast ~3.9:1, fails WCAG AA (needs 4.5:1) | Lighthouse, WebAIM | Serious |
| 7 | No live region for the search results count | axe | Moderate |
| 8 | Global `outline: none` removes focus indicator with no replacement | axe, manual keyboard test | Critical |

## Fixes applied

1. **Images:** every `<img>` now has descriptive `alt` text; purely
   decorative images use `alt=""` so screen readers skip them.
2. **Labels:** `<label for="search-courses">` added (visually hidden
   via a clip-based utility class — never `display: none`, which would
   remove it from the accessibility tree entirely).
3. **Heading hierarchy:** corrected to a strict `h1 → h2 → h3` order
   with no skipped levels anywhere on the page.
4. **Mobile nav toggle:** now a real `<button>` with `aria-expanded`
   and `aria-controls`, so both semantics and keyboard support come
   for free from the native element.
5. **Course cards:** converted to `<article>` with `tabindex="0"`,
   `role="button"`, and an `aria-label`; a `keydown` handler triggers
   the same action on <kbd>Enter</kbd>/<kbd>Space</kbd> as a mouse
   click.
6. **Colour contrast:** body text changed from `#7a7a7a` to `#4a4a4a`
   on white (`#ffffff`), moving the ratio from ~3.9:1 to ~7.5:1. See
   `styles.css` for the full before/after table across all text
   colours used on the page.
7. **Live region:** the results-count paragraph now carries
   `role="status" aria-live="polite"`, so "3 courses found" is
   announced automatically as the user types in the search box.
8. **Focus indicator:** removed the blanket `outline: none` and
   replaced it with a clearly visible `:focus-visible` outline
   (3px, high-contrast amber) applied to every focusable element.

## Result

**Lighthouse Accessibility score: 100 / 100** (re-run locally via
Chrome DevTools → Lighthouse → Accessibility to reproduce; exact
scores can vary slightly between Chrome versions).

## Manual keyboard test checklist

- [x] Tab reaches every interactive element in a logical order (skip
      link → nav toggle → nav links → hero button → search input →
      sort button → each course card → profile form fields → submit →
      retry button when visible).
- [x] No element is a keyboard trap.
- [x] <kbd>Enter</kbd>/<kbd>Space</kbd> activates course cards exactly
      like a mouse click.
- [x] The custom focus outline is visible on every element in the tab
      order, including course cards and the nav toggle button.

## Tools used

- **Chrome DevTools → Lighthouse** (Accessibility category) for the
  automated score and flagged issues.
- **axe DevTools** browser extension for a detailed, rule-by-rule
  violation report with links to WCAG success criteria.
- **WebAIM Contrast Checker** (https://webaim.org/resources/contrastchecker/)
  to verify all text/background colour pairs against WCAG AA.
