# Student Portal — API Integration & Advanced State Management (Hands-On 10)

React implementation of the Student Portal focused on a centralised
Axios API layer and Redux Toolkit's `createAsyncThunk` pattern for
async state management, plus a global error boundary.

## Features

- **Centralised API layer** (`src/api/`):
  - `apiClient.js` — single Axios instance (`baseURL`, `timeout`,
    default headers)
  - Request interceptor attaches a mock `Authorization` header to
    every outgoing request and logs the call
  - Response interceptor unwraps `response.data` and converts errors
    into a standardised `{ message, statusCode }` shape, so components
    never see raw HTTP status codes
  - `courseApi.js` — `getAllCourses()`, `getCourseById(id)`,
    `enrollStudent(studentId, courseId)`, all built on `apiClient`
- **Redux Toolkit:**
  - `coursesSlice.js` — `createAsyncThunk('courses/fetchAll', ...)`
    with `pending`/`fulfilled`/`rejected` handled in `extraReducers`
  - `enrollmentSlice.js` — synchronous `enroll`/`unenroll` reducers
  - Selectors (`selectCourses`, `selectCoursesLoading`,
    `selectCoursesError`, `selectEnrolledCourses`, ...) — components
    only ever read state through these functions
- **Error Boundary:** a class-based `ErrorBoundary` component wraps
  the whole app (and the routed page content) and renders a friendly
  fallback UI plus a "Try again" reset button if a render error occurs
- **Reusable components:** `Header`, `CourseCard`, `LoadingSpinner`
- **Routing:** React Router v6 (`/`, `/courses/:courseId`, `/profile`)
- **Responsive, accessible UI:** keyboard-operable course cards,
  `aria-live` search result count, focus-visible outlines, inline form
  validation

## Folder structure

```
Frontend_Handson_10_API_State_Management/
├── package.json
├── vite.config.js
├── index.html
├── README.md
├── screenshots/
└── src/
    ├── main.jsx
    ├── App.jsx
    ├── api/
    │   ├── apiClient.js
    │   └── courseApi.js
    ├── store/
    │   ├── store.js
    │   ├── coursesSlice.js
    │   └── enrollmentSlice.js
    ├── components/
    │   ├── Header.jsx
    │   ├── CourseCard.jsx
    │   ├── LoadingSpinner.jsx
    │   └── ErrorBoundary.jsx
    ├── pages/
    │   ├── CoursesPage.jsx
    │   ├── CourseDetailPage.jsx
    │   └── ProfilePage.jsx
    ├── data/courses.js
    └── styles/index.css
```

## Installation

```bash
cd Frontend_Handson_10_API_State_Management
npm install
```

## Run

```bash
npm run dev
```

Open http://localhost:5175.

## Build

```bash
npm run build
npm run preview
```

## Testing the error/loading states

- **Loading:** the spinner shows briefly on first load of `/` while
  `fetchAllCourses` is `pending`.
- **Error + retry:** temporarily change `apiClient`'s `baseURL` in
  `src/api/apiClient.js` to an invalid host, reload, and confirm the
  error banner and Retry button appear; clicking Retry re-dispatches
  the thunk.
- **Error boundary:** throw an error inside any page component
  temporarily (e.g. `throw new Error('test')` at the top of
  `CoursesPage`) to confirm the fallback UI renders instead of a blank
  page.

## Framework comparison — state management (Hands-On 10, Task 3, Step 151)

| | React + Redux Toolkit | Angular + NgRx | Vue + Pinia |
|---|---|---|---|
| **Core pattern** | Actions → reducers (via `createSlice`) → store → `useSelector`/`useDispatch` | Actions → reducers → store → Effects (side effects) → Selectors → `async` pipe / `select()` | Reactive store object → direct property access/actions, no explicit action objects required |
| **Boilerplate** | Low with RTK (`createSlice`, `createAsyncThunk` remove most manual action-type/reducer boilerplate) | Higher — explicit Actions, Reducers, Effects, and Selectors are usually separate files per feature | Lowest — a Pinia store is just a function returning reactive state + actions, no separate action/reducer layer |
| **Async handling** | `createAsyncThunk` + `extraReducers` (pending/fulfilled/rejected) | NgRx Effects (separate, RxJS-based side-effect layer, keeping reducers pure) | Plain `async` actions inside the store — no separate effects layer needed |
| **Learning curve** | Moderate — need to understand actions, reducers, thunks, and the Provider/hooks integration | Steepest — requires solid RxJS knowledge on top of Redux-style concepts (Actions/Reducers/Effects/Selectors) | Gentlest — closely mirrors plain Vue reactivity (`ref`/`computed`) that developers already use locally |
| **Built-in tooling** | Redux DevTools (time-travel debugging, action log/diff) | Redux DevTools works via `@ngrx/store-devtools`; strong RxJS/Angular DevTools integration | Vue DevTools has a first-class Pinia tab showing state and actions live |
| **Type safety** | Good with TypeScript + RTK's typed hooks | Excellent — NgRx is built TypeScript-first and leans on Angular's DI typing | Good — Pinia's Composition API style is described as more TypeScript-friendly than the Options API style |

**Summary:** all three follow the same conceptual shape — a single
source of truth, pure state transitions, and a dedicated place for
side effects (thunks/effects/async actions) — but Redux Toolkit and
Pinia both trade some of Redux's original ceremony for less
boilerplate, while NgRx keeps the strict Actions/Reducers/Effects
separation that scales well on large Angular codebases at the cost of
a steeper learning curve.

## Notes

- JSONPlaceholder doesn't model "courses", so `courseApi.js` maps its
  `/posts` response onto local sample course fields (name, code,
  credits, grade) — this still exercises a genuine HTTP round trip
  through the centralised Axios client and its interceptors while
  keeping realistic-looking course data in the UI.
