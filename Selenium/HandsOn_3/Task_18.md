# Task 18 — Automate or Manual Decisions

| # | Test Case | Decision | Justification |
|---|---|---|---|
| a | Regression test for all CRUD endpoints after every code change | Automate | Repetitive, runs on every change, objectively verifiable — ideal automation candidate. |
| b | Exploratory testing of a new search feature | Manual | Exploratory testing relies on human intuition and ad-hoc investigation; there's no fixed script to automate. |
| c | Performance test: 100 concurrent users calling GET /api/courses/ | Automate | Needs a load-generation tool (e.g. Locust/JMeter) to simulate concurrency reliably and repeatedly — manual execution is impractical. |
| d | UI test for the login form | Automate | Stable, repetitive UI flow with clear pass/fail criteria — a strong Selenium candidate, though lower priority than API tests. |
| e | Verify the API documentation (Swagger) is accurate | Manual | Requires human judgment to compare written descriptions against intended behavior; not easily scriptable. |
| f | Smoke test: verify the API is reachable after deployment | Automate | Simple, fast, run after every deployment — perfect for a CI/CD pipeline health check. |
