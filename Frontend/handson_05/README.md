# Hands-On 5 — React Fundamentals

Student Portal rebuilt as a React (Vite) app: JSX, functional
components, props, `useState`, `useEffect`, conditional rendering, and
lists.

## What's covered

- **Components:** `Header`, `Footer`, `CourseCard`, `StudentProfile`
- **Props:** `Header` receives `siteName` and `enrolledCount`;
  `CourseCard` receives course fields plus an `onEnroll` handler
- **`useState`:** course list, search term, enrolled courses (lifted up
  to `App`), loading/error state
- **Lists:** `courses.map(...)` renders a `CourseCard` per course, each
  with a stable `key={course.id}` (never an array index)
- **`useEffect`:** fetches 5 posts from JSONPlaceholder on mount
  (empty dependency array `[]`, so it behaves like
  `componentDidMount`), plus a second effect that logs whenever the
  `courses` array changes (dependency array `[courses]`)
- **Conditional rendering:** loading message, error banner, and the
  course grid are shown/hidden based on state

## Install & run

```bash
cd handson_05
npm install
npm run dev
```

Open http://localhost:5173.

## Notes

- If the network request fails, an error message is shown in the UI
  (not just logged) — see `App.jsx`'s `catch` block.
- `StudentProfile` keeps its own local `useState` for `name`, `email`,
  and `semester`, bound to inputs via `onChange` handlers.
