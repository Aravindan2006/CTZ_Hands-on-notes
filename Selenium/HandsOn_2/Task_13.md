# Task 13 — Problems Caused by Waterfall's Late Testing

Three problems caused by testing only after development is complete, for the Course
Management API:

1. **Expensive late fixes:** A requirements misunderstanding (e.g. course codes should
   allow letters and numbers, not just numbers) is found only during system testing,
   requiring a costly redesign of validation logic and database constraints instead of a
   cheap requirements-review fix.
2. **Compressed test schedule:** If development runs late, the fixed release date eats
   into the testing window, forcing QA to reduce test coverage under time pressure and
   ship with more risk.
3. **Delayed feedback to developers:** Developers who wrote the `POST /api/courses/`
   endpoint weeks earlier have moved on to other modules by the time defects surface,
   making root-cause analysis slower and context-switching costly.
