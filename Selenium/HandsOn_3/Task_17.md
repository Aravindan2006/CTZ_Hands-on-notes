# Task 17 — Automation Decision Criteria

Five criteria for deciding whether a test case should be automated, applied to:
*"Test that POST /api/courses/ returns 201 with the correct course data when valid input
is provided."*

1. **Repeatability** — Will this test run many times (every build/regression cycle)?
   Yes: this happy-path create test runs on every CI build, so automating pays off fast.
2. **Stability of the feature** — Is the feature's UI/API contract stable? Yes: the
   `POST /api/courses/` contract is unlikely to change frequently once released, making
   an automated test low-maintenance.
3. **Business criticality/risk** — Is this a core, high-risk flow? Yes: course creation
   is a core write operation; a regression here directly breaks the product.
4. **Data-driven nature** — Can it easily be parameterized with different inputs? Yes:
   valid payloads, boundary values, and invalid payloads can all be run through the same
   automated test with different data.
5. **Objectively verifiable outcome** — Can pass/fail be determined programmatically
   without human judgment? Yes: HTTP status code and JSON body equality checks are fully
   deterministic and scriptable.

All five criteria point to **automate** for this test case.
