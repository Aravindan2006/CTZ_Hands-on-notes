# Task 5 — Defect Lifecycle Diagram

```
   New -> Assigned -> Open -> Fixed -> Retest -> Verified -> Closed
                        |                 |
                        |                 v
                        |             Reopened -> Open (loop back)
                        |
                        +--> Rejected   (not a valid defect / cannot reproduce)
                        +--> Deferred   (valid, but scheduled for a later release)
```

- **New:** QA logs the defect for the first time.
- **Assigned:** A lead assigns it to a developer.
- **Open:** Developer analyzes the root cause and starts fixing.
- **Fixed:** Developer applies and checks in a code fix.
- **Retest:** QA re-executes the original failing test against the fix.
- **Verified:** QA confirms the fix resolves the issue with no regressions.
- **Closed:** Defect is formally closed once verified in the target build.
- **Rejected path:** Duplicate, not reproducible, or working-as-designed reports move here
  instead of Open.
- **Deferred path:** Valid but low-priority defects are scheduled for a future release instead
  of being fixed now.
- **Reopened:** If Retest fails, the defect returns to Open rather than proceeding to Verified.
