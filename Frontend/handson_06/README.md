# Hands-On 6 — React Routing & State Management

Extends the Hands-On 5 Student Portal with multi-page navigation
(React Router v6), a Context API example, and a Redux Toolkit
refactor of the enrollment state.

## What's covered

- **Task 1 — React Router:** `BrowserRouter` in `main.jsx`, routes for
  `/`, `/courses`, `/courses/:courseId`, `/profile` in `App.jsx`,
  `<Link>`/`<NavLink>` navigation in `Header.jsx`, `useParams()` in
  `CourseDetailPage`, and `useNavigate()` to redirect to `/profile`
  after enrolling.
- **Task 2 — Context API:** `src/context/EnrollmentContext.jsx`
  demonstrates `createContext` + a Provider holding `enrolledCourses`
  state, with `enroll`/`unenroll` functions exposed via
  `useEnrollment()`. **Note:** the running app uses the Task 3 Redux
  store instead of this Provider — the file is kept to show the
  Context pattern the exercise asks for, and as the "before" state
  that Task 3 explicitly refactors away from.
- **Task 3 — Redux Toolkit:** `src/store/store.js` +
  `src/store/enrollmentSlice.js` (`createSlice` with `enroll`/`unenroll`
  reducers and selectors). `Header`, `CourseDetailPage`, and
  `ProfilePage` all read/write this shared store via
  `useSelector`/`useDispatch` — enrolling on `CourseDetailPage`
  immediately updates the count in `Header` and the list in
  `ProfilePage`, with no props passed between them.

## Folder structure

```
handson_06/
├── package.json
├── vite.config.js
├── index.html
├── README.md
└── src/
    ├── main.jsx
    ├── App.jsx
    ├── styles.css
    ├── data/courses.js
    ├── context/EnrollmentContext.jsx   (Task 2 reference implementation)
    ├── store/
    │   ├── store.js
    │   └── enrollmentSlice.js          (Task 3 — used by the running app)
    ├── components/
    │   ├── Header.jsx
    │   └── CourseCard.jsx
    └── pages/
        ├── HomePage.jsx
        ├── CoursesPage.jsx
        ├── CourseDetailPage.jsx
        └── ProfilePage.jsx
```

## Install & run

```bash
cd handson_06
npm install
npm run dev
```

Open http://localhost:5173.

## Try it

1. Go to **Courses**, click a course card → navigates to
   `/courses/:id`.
2. Click **Enroll** on the detail page → dispatches the Redux `enroll`
   action and redirects to `/profile`.
3. Open Redux DevTools (browser extension) and watch the `enroll`/
   `unenroll` actions and state diff as you enroll/remove courses.
