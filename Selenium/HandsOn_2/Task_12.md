# Task 12 — Early QA Engagement Points

Two places (beyond the formal testing phases) where QA should engage during the Course
Management API project:

1. **Requirements Review (left side of the V-Model):** QA reviews the requirements
   documents alongside business analysts to catch ambiguous, untestable, or conflicting
   requirements before any code is written - e.g. clarifying whether `course_code` must
   be globally unique or unique-per-department before development starts.

2. **Architecture/Design Review:** QA participates in design walkthroughs for the API
   architecture to flag testability concerns early - e.g. requesting that the database
   layer expose a way to seed/reset test data, or that error responses follow a
   consistent, machine-checkable JSON schema, both of which make later automation far
   easier.
