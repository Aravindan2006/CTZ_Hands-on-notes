# Hands-On 3 — JavaScript ES6+ & DOM Manipulation

Brings the Student Portal to life with modern ES6+ JavaScript and
direct DOM manipulation — no frameworks yet.

## Files

- `index.html` — page shell with an empty `.course-grid`, search input, sort button
- `data.js` — 5 course objects exported as an ES module
- `app.js` — ES6+ syntax practice, dynamic rendering, search/sort/event delegation
- `styles.css` — styling for the toolbar and course grid

## Run

Open `index.html` directly in your browser (uses `<script type="module">`,
which works from `file://` in most browsers, or serve with any static
file server if your browser restricts module loading from disk).

Open the browser console to see the ES6+ syntax practice output
(Task 1: destructuring, `map`, `filter`, `reduce` results).

## What's demonstrated

- **ES6+ syntax:** `const`/destructuring, arrow functions, template
  literals, `Array.map/filter/reduce`
- **DOM manipulation:** `querySelector`, `createElement`,
  `DocumentFragment` batching, `appendChild`
- **Events:** `input` event for live search, `click` for sort,
  **event delegation** on the grid container using
  `event.target.closest('.course-card')` instead of one listener per card
