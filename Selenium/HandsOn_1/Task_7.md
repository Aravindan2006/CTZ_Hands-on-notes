# Task 7 — Defect Report for Bug (a)

| Field | Value |
|---|---|
| Defect ID | DEF-1042 |
| Title | POST /api/courses/ returns 500 Internal Server Error for all requests |
| Environment | Staging, Ubuntu 22.04, Python 3.11, PostgreSQL 15 |
| Build Version | v1.4.2-rc3 |
| Severity | Critical |
| Priority | P1 |
| Steps to Reproduce | 1. Start the API server on build v1.4.2-rc3. 2. Send POST /api/courses/ with a valid JSON payload, e.g. {"course_code":"CS-101","title":"Intro","credits":3}. 3. Observe the response. |
| Expected Result | 201 Created with the newly created course object in the response body. |
| Actual Result | 500 Internal Server Error with a generic error message; server logs show an unhandled IntegrityError from the ORM layer. |
| Attachments | screenshot of 500 error |
