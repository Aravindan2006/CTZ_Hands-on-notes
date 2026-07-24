# Task 3 — Black-Box vs White-Box Testing

- **Black-Box Testing:** Tests the software without knowledge of internal code — only inputs and
  expected outputs matter. Example: sending `POST /api/courses/` and checking the HTTP status and
  response body without reading the route handler's source.
- **White-Box Testing:** Tests with full knowledge of internal code structure — branches, loops,
  logic paths. Example: writing a unit test that specifically exercises the `else` branch inside
  `validate_course_code` to hit a code-coverage target.
- **Who performs which:** QA testers typically perform black-box testing (validating behavior
  against requirements without needing the implementation). Developers typically perform
  white-box testing (unit tests, branch coverage) since they own and understand the internals.
