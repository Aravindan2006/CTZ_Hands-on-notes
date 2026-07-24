# Task 15 — Shift-Left Practices

Four Shift-Left practices applied to the Course Management API:

**(a) Reviewing requirements for testability** - Before development starts, QA reviews
the "create course" user story and flags that "course code must be valid" is untestable
as written, pushing the team to define exact validation rules (length, allowed
characters, uniqueness scope).

**(b) Writing test cases before code (TDD/BDD)** - QA and developers write
Given-When-Then scenarios for `POST /api/courses/` (happy path, duplicate code, missing
fields) before implementation begins, so the code is written to satisfy known,
agreed-upon behavior.

**(c) Static code analysis** - Tools like flake8/mypy/bandit run automatically on
every commit to the API codebase, catching type errors, unused imports, and basic
security issues before the code ever reaches a test environment.

**(d) API contract testing before integration** - The API's OpenAPI/Swagger schema is
validated against a contract test suite (e.g. using schemathesis) as soon as the
endpoint is scaffolded, catching schema mismatches before the frontend team starts
integrating against it.
