# Task 22 — Framework Recommendation

**Scenario:** Test login with 50 different user/password combinations, reuse login steps
across 20 test cases, and support both technical and non-technical team members writing
tests.

**Recommendation: Hybrid framework (Modular + Data-Driven, with a lightweight
Keyword-Driven layer for non-technical contributors).**

- **Modular** covers "reuse login steps across 20 test cases": a `LoginPage` class (Page
  Object) with a `login(username, password)` method is written once and called from all
  20 test cases.
- **Data-Driven** covers "50 different user/password combinations": the 50 combinations
  live in a CSV/JSON file or a `pytest.mark.parametrize` data set, and the same
  `test_login` function runs once per row — no duplicated test code.
- **Keyword-Driven (lightweight)** covers "non-technical team members": a thin layer on
  top (e.g. a spreadsheet mapping keywords like `ENTER_USERNAME`, `CLICK_LOGIN` to
  underlying Page Object methods) lets non-coders add new login scenarios without
  touching Python.

A pure Modular framework alone wouldn't handle 50 data combinations cleanly, and a pure
Data-Driven framework alone wouldn't give non-technical members an easy entry point —
Hybrid is the only option that satisfies all three requirements simultaneously.
