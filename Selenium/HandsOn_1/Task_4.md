# Task 4 — Formal Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|---|
| TC-COURSE-001 | Create a course with valid data | API and DB are running; no course `CS-301` exists | 1. `POST /api/courses/` with `{"course_code":"CS-301","title":"Algorithms","credits":4}` 2. Read response | `201 Created`; body has the created course with generated `id`; row exists in DB | | |
| TC-COURSE-002 | Reject duplicate course code | Course `CS-301` already exists | 1. `POST /api/courses/` with `{"course_code":"CS-301","title":"Algorithms II","credits":3}` 2. Read response | `409 Conflict`; error mentions duplicate code; no new row inserted | | |
| TC-COURSE-003 | Reject missing required field | API is running | 1. `POST /api/courses/` with `{"title":"Algorithms"}` (no `course_code`) 2. Read response | `422 Unprocessable Entity`; error identifies `course_code` as required; no row inserted | | |
