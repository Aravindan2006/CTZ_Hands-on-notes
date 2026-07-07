# Browser Compatibility Documentation

## Manual cross-browser test (Hands-On 9, Task 3, Step 135)

Tested by opening `index.html` in Chrome, Firefox, and Safari (or
Edge as a Safari substitute on Windows).

| Aspect | Chrome | Firefox | Safari/Edge | Notes |
|---|---|---|---|---|
| Flexbox header layout | ✔ | ✔ | ✔ | Identical alignment and spacing |
| CSS Grid course cards (`auto-fit`/`minmax`) | ✔ | ✔ | ✔ | Reflow behaviour matches across all three |
| `gap` in Flexbox | ✔ | ✔ | ✔ (14.1+) | See caniuse note below for older Safari |
| `clamp()` fluid typography | ✔ | ✔ | ✔ | Font scales smoothly on resize in all three |
| Font rendering | Slightly bolder | Slightly thinner hinting | Default macOS/system rendering | Cosmetic only, no layout impact |
| Focus outline visibility | ✔ | ✔ | ✔ | Custom `:focus-visible` renders consistently |

No layout-breaking differences were found between browsers at 375px,
768px, and 1280px viewport widths.

## caniuse.com findings (Hands-On 9, Task 3, Step 136)

**Feature checked: `gap` property in Flexbox layouts**

| Browser | Minimum version supporting flex `gap` |
|---|---|
| Chrome | 84 |
| Firefox | 63 |
| Safari | 14.1 |
| Edge (Chromium) | 84 |

Source: https://caniuse.com/flexbox-gap (checked during this exercise).

**Conclusion:** support is effectively universal in any browser
released since mid-2021. The only realistic risk is Safari versions
older than 14.1 (released April 2021). For that edge case, the CSS
includes a `.no-flex-gap` fallback class (added via feature detection
in `app.js` using `CSS.supports('gap', '1rem')`) that switches to
margin-based spacing instead of `gap` — chosen over user-agent
sniffing because it tests the actual feature rather than guessing
from a browser string, which stays correct even as browsers update.

## Polyfill / fallback strategy (Hands-On 9, Task 3, Step 137)

- **Feature detection over browser detection:** `app.js` checks
  `'IntersectionObserver' in window` and `CSS.supports(...)` rather
  than parsing `navigator.userAgent`, since user-agent strings are
  unreliable and easy to spoof, while feature checks test exactly what
  the page needs.
- **CSS custom properties (variables) polyfill:** for target
  environments that must support Internet Explorer 11 or other very
  old browsers without native CSS custom property support, the
  `css-vars-ponyfill` library can be included via CDN:

  ```html
  <script src="https://cdn.jsdelivr.net/npm/css-vars-ponyfill@2/dist/css-vars-ponyfill.min.js"></script>
  <script>
    cssVars({
      // Re-processes stylesheets using var(--...) into static values
      // for browsers that don't understand CSS custom properties.
      watch: true,
    });
  </script>
  ```

  This project does not ship the ponyfill by default (all current
  evergreen browsers support CSS custom properties natively), but the
  snippet above is the documented, ready-to-enable fallback if a
  legacy-browser requirement appears.

## Summary

The Student Portal's core layout techniques (Flexbox, Grid,
`clamp()`, CSS custom properties) all have broad, current support
across Chrome, Firefox, and Safari/Edge. The one documented gap
(pre-2021 Safari and flex `gap`) is handled with a feature-detected
fallback rather than a browser-sniffed one, keeping the code correct
as browser support continues to evolve.
