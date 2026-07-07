# Hands-On 1 — HTML5 Semantic Structure & CSS3 Foundations

The structural skeleton of the Student Portal, built with semantic
HTML5 and styled with CSS3 fundamentals (box model, typography,
basic layout). No frameworks, no build step.

## Files

- `index.html` — semantic page structure (`header`, `nav`, `main`,
  `section`, `article`, `footer`)
- `styles.css` — CSS reset, box-sizing, header/nav/hero styling,
  course card styling

## Run

Open `index.html` directly in your browser — no server or install
required.

## What's demonstrated

- Proper HTML5 doctype, `lang`, charset, viewport meta, descriptive title
- `<header>`, `<nav>`, `<main>` (used once), two `<section>`s, `<footer>`
- `<article>` used for self-contained course cards (more semantically
  correct than `<div>`)
- CSS reset with `box-sizing: border-box`
- Flexbox header (`justify-content: space-between`)
- Button `:hover` state
- `.course-card` styling: padding, border, border-radius, box-shadow

## Validation

Validate at https://validator.w3.org/ — this page is written to pass
with zero errors.
