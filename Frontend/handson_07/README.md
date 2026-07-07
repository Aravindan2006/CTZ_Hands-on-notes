# Student Portal — Angular (Hands-On 7)

An Angular implementation of the Student Portal: components, services
with dependency injection, HttpClient + RxJS, routing, and Reactive
Forms with validation.

## Features

- **Components:** `Header`, `CourseList`, `CourseCard`, `CourseDetail`,
  `StudentProfile`, `LoadingSpinner`
- **Data binding:** interpolation, `[property]` binding, `[(ngModel)]`
  two-way binding (search box), event binding (`(click)`, `(keydown)`)
- **Services & DI:** `CourseService` (singleton, `providedIn: 'root'`)
  wraps `HttpClient` calls so components never talk to HTTP directly
- **RxJS:** `map`, `tap`, `catchError` operators in `CourseService`
- **Routing:** `/` (course list), `/courses/:id` (detail),
  `/profile` (reactive form), with `routerLink` navigation and
  programmatic `router.navigate()` after enrolling
- **Reactive Forms:** `FormGroup`/`FormControl` with `Validators`
  (required, email, min/max) and inline error messages
- **Responsive, accessible UI:** keyboard-navigable course cards,
  `aria-live` search result count, focus-visible outlines

## Folder structure

```
Frontend_Handson_07_Angular/
├── package.json
├── angular.json
├── tsconfig*.json
├── README.md
├── screenshots/
└── src/
    ├── index.html
    ├── main.ts
    ├── styles.css
    ├── assets/data/courses.json
    └── app/
        ├── app.module.ts
        ├── app-routing.module.ts
        ├── app.component.{ts,html,css}
        ├── models/course.model.ts
        ├── services/course.service.ts
        └── components/
            ├── header/
            ├── course-list/
            ├── course-card/
            ├── course-detail/
            ├── student-profile/
            └── loading-spinner/
```

## Installation

```bash
cd Frontend_Handson_07_Angular
npm install
```

## Run

```bash
npm start
# or: ng serve
```

Open http://localhost:4200.

## Build

```bash
npm run build
```

## Notes

- Course data is fetched from JSONPlaceholder (`/posts?_limit=5`) and
  enriched with local sample course fields (name, code, credits,
  grade) in `CourseService`, demonstrating a real HTTP round trip via
  `HttpClient` + RxJS while keeping realistic course data in the UI.
- If the network request fails, `CourseService` falls back to local
  sample data via `catchError`, so the UI never breaks even offline.
