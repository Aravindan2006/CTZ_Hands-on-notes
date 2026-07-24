# Task 20 — Flaky Tests

**Definition:** A flaky test is one that produces inconsistent results (sometimes pass,
sometimes fail) against the same code, with no actual change in the system under test —
the failure is caused by test infrastructure issues rather than a real defect.

**Example:** A Selenium test that clicks "Submit" and immediately asserts a success
message is visible, without waiting for the page's AJAX call to finish. On a fast machine
it passes; on a slower/loaded CI runner the assertion runs before the message renders,
so the test fails intermittently.

**Three strategies to prevent/fix flaky tests:**
1. **Use explicit waits (`WebDriverWait` + `ExpectedConditions`)** instead of fixed
   `time.sleep()` calls, so the test waits exactly as long as needed and no longer.
2. **Isolate test data and state** — give every test its own fresh browser session and
   test data (e.g. a unique course code per test run) so tests don't interfere with each
   other or depend on execution order.
3. **Retry with root-cause investigation, not blind retries** — a single automatic retry
   can mask transient CI issues, but every flaky failure should be logged and
   investigated (e.g. via captured screenshots/logs on failure) so genuine flakiness gets
   fixed rather than permanently hidden behind retries.
