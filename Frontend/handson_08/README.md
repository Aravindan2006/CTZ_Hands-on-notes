# Student Portal — Vue 3 (Hands-On 8)

A Vue 3 implementation of the Student Portal using the Composition
API, Vue Router, and Pinia for state management.

## Features

- **Composition API:** `<script setup>` single-file components,
  `ref`/`reactive`/`computed` throughout
- **Components:** `Header.vue`, `CourseCard.vue`
- **Views:** `HomeView`, `CoursesView`, `CourseDetailView`, `ProfileView`
- **Reactive search:** `computed()` filters the course list live as
  you type, without extra re-renders when unrelated state changes
- **Vue Router:** 4 routes (`/`, `/courses`, `/courses/:id`,
  `/profile`), `RouterLink` navigation, `useRoute`/`useRouter` for
  param access and programmatic navigation, plus a `beforeEach`
  navigation guard that logs every route change
- **Pinia store (`stores/enrollment.js`):** `enrolledCourses` state,
  `totalCredits` computed getter, `enroll`/`unenroll` actions, an
  async `fetchAndEnroll` action, and a `$reset()` helper
- **`storeToRefs`** used in `ProfileView` to destructure store state
  without losing reactivity
- Responsive, accessible UI with keyboard-operable course cards and a
  live-announced search results count

## Folder structure

```
Frontend_Handson_08_Vue/
├── package.json
├── vite.config.js
├── index.html
├── README.md
├── screenshots/
└── src/
    ├── main.js
    ├── App.vue
    ├── style.css
    ├── data/courses.js
    ├── router/index.js
    ├── stores/enrollment.js
    ├── components/
    │   ├── Header.vue
    │   └── CourseCard.vue
    └── views/
        ├── HomeView.vue
        ├── CoursesView.vue
        ├── CourseDetailView.vue
        └── ProfileView.vue
```

## Installation

```bash
cd Frontend_Handson_08_Vue
npm install
```

## Run

```bash
npm run dev
```

Open http://localhost:5174.

## Build

```bash
npm run build
npm run preview
```

## Notes

- Enrolling a course from either `CoursesView` or `CourseDetailView`
  immediately updates the header's enrolled count and the profile
  page's list — all through the shared Pinia store, no prop drilling.
- Open Vue DevTools' Pinia tab while testing to watch `enroll` /
  `unenroll` actions and state updates in real time.
