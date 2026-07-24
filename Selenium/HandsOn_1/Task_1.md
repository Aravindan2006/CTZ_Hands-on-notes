# Task 1 — Test Cases per Testing Level

For the Course Management API, one concrete test case per level:

**Unit Testing** — Test `validate_course_code(code: str) -> bool` in isolation, no DB/network.
Call `validate_course_code("CS-101")` → expect `True`; call `validate_course_code("")` → expect `False`.

**Integration Testing** — Test the API endpoint + database together.
Call `POST /api/courses/` with a valid payload, then query the database directly to confirm a row
was inserted into `courses` with the matching `course_code`, `title`, and `credits`.

**System Testing** — Test the full end-to-end flow, API request to database response.
Against the fully running stack: `POST /api/courses/` to create a course, `GET /api/courses/{id}`
to retrieve it, `PUT` to update credits, then `GET` again to confirm the update persisted.

**User Acceptance Testing (UAT)** — Test from the perspective of an actual college admin.
As an admin, log in to the portal, create course "Data Structures" (`CS-201`, 4 credits), and
confirm it now shows up in the course listing students browse for enrollment.
