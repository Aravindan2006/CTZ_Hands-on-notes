# Task 2 — Functional vs Non-Functional Classification

| Test Case | Classification | Reason |
|---|---|---|
| Unit test on `validate_course_code` | Functional | Checks *what* the function does |
| Integration test: POST persists to DB | Functional | Checks *what* the system does |
| System test: full CRUD cycle | Functional | Checks *what* the flow does |
| UAT: create-course-to-listing flow | Functional | Checks the feature works for the user |

**Non-functional example:** Performance — `POST /api/courses/` must respond within 300ms at the
95th percentile under 50 concurrent requests/second. This tests **how well** the system performs
rather than what it does, so it is non-functional.
