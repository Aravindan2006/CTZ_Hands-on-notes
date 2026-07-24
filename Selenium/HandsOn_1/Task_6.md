# Task 6 — Severity / Priority Classification

| Bug | Severity | Priority | Justification |
|---|---|---|---|
| (a) POST /api/courses/ returns 500 for all requests | Critical | P1 | Core create functionality is completely broken for every user - the API is unusable for its primary write operation. |
| (b) Course names >150 chars silently truncated, no error | Medium | P3 | Data is corrupted but the system doesn't crash, and most course names are well under 150 characters, so real-world impact is limited. |
| (c) Typo in Swagger /docs description | Low | P4 | Purely cosmetic documentation issue with zero functional impact. |
| (d) Intermittent 401 on first login attempt with correct credentials | High | P2 | Doesn't break the system outright, but authentication reliability is core to the product; intermittent bugs erode user trust and are hard to diagnose later, so it deserves prompt attention. |
