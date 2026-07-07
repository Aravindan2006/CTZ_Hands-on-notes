# Module 2 — Frontend Development

Digital Nurture 5.0 · Python Full Stack Engineer Track
**Scenario:** Student Portal Web Application

Complete solutions for Hands-On Exercises 1–10, each in its own
self-contained folder, per the submission guidelines in the exercise
book. All ten build on the same running scenario — a Student Portal
where students browse courses, manage their profile, and track
enrollments — starting from plain HTML/CSS/JS and progressively
migrating into React, Angular, Vue, accessibility hardening, and
advanced state management.

## Folder map

| Folder | Hands-On | Topic | Tech |
|---|---|---|---|
| `handson_01/` | 1 | Semantic HTML5 & CSS3 fundamentals | HTML/CSS |
| `handson_02/` | 2 | Flexbox, Grid & responsive design | HTML/CSS/JS |
| `handson_03/` | 3 | JavaScript ES6+ & DOM manipulation | HTML/CSS/JS |
| `handson_04/` | 4 | Async JS, Fetch API & Axios intro | HTML/CSS/JS |
| `handson_05/` | 5 | React fundamentals (components, props, hooks) | React (Vite) |
| `handson_06/` | 6 | React Router, Context API, Redux Toolkit intro | React (Vite) |
| `handson_07/` | 7 | Angular — components, services, DI, routing, forms | Angular |
| `handson_08/` | 8 | Vue 3 — Composition API, Vue Router, Pinia | Vue 3 (Vite) |
| `handson_09/` | 9 | Accessibility (WCAG 2.1) & cross-browser compatibility | HTML/CSS/JS |
| `handson_10/` | 10 | Centralised API layer & advanced state management | React (Vite) |

Every folder is self-contained with its own README, and — where a
build step applies — its own `package.json`.

## How to run each one

**Hands-On 1–4 (plain HTML/CSS/JS, no build step):**
Open `index.html` directly in a browser, or serve locally to avoid
ES-module CORS restrictions on some browsers:

```bash
cd handson_0X
npx serve .
```

**Hands-On 5, 6, 8, 10 (Vite-based projects):**

```bash
cd handson_0X
npm install
npm run dev
```

**Hands-On 7 (Angular CLI project):**

```bash
cd handson_07
npm install
npm start        # or: ng serve
```

**Hands-On 9 (accessibility project, has an optional static server):**

```bash
cd handson_09
npm install
npm start
```

See each folder's own `README.md` for exact ports, feature notes, and
testing instructions.

## Progression at a glance

1–2 lay down the semantic HTML/CSS skeleton and make it responsive.
3–4 bring it to life with vanilla JavaScript — DOM rendering, search,
sort, and real API calls via Fetch/Axios. 5–6 rebuild the same portal
in React, adding component architecture, hooks, routing, and two
generations of shared state (Context, then Redux Toolkit). 7 and 8
rebuild it again in Angular and Vue, to compare how each framework's
own idioms (services + DI + RxJS vs. Composition API + Pinia) solve
the same problems. 9 goes back over the plain HTML/CSS/JS version and
hardens it for accessibility and cross-browser support. 10 finishes
with a production-style centralised API layer (Axios interceptors) and
advanced Redux Toolkit patterns (`createAsyncThunk`, selectors, an
error boundary), plus a written comparison of state management across
all three frameworks.
