# Task 21 — Comparing the 5 Automation Framework Types

**Linear (Record & Playback)**
Scripts are recorded step-by-step exactly as a user performs them, with no reuse or
abstraction. *Advantage:* very fast to create initially, no coding skill needed.
*Disadvantage:* extremely brittle — any UI change breaks every recorded script, and
there is heavy duplication across scripts. *Use for:* a one-off smoke check of the
Course Management login page during a demo.

**Modular**
The application is broken into independent modules (e.g. login, create-course,
search-course), each with its own reusable test script that other tests can call.
*Advantage:* reduces duplication versus Linear. *Disadvantage:* still requires
programming knowledge and doesn't handle large data variations well. *Use for:* reusing
a `login()` module across dozens of Course Management UI tests.

**Data-Driven**
Test logic is separated from test data, which lives in external files (CSV/Excel/JSON);
the same script runs once per data row. *Advantage:* easily test many input
combinations without duplicating scripts. *Disadvantage:* the framework itself requires
more upfront engineering effort to build. *Use for:* validating course creation with 50
different valid/invalid course-code formats.

**Keyword-Driven**
Test steps are represented as keywords (e.g. "ClickButton", "EnterText") in a table/sheet,
interpreted by a driver engine; non-programmers can write tests. *Advantage:* usable by
manual testers with no coding background. *Disadvantage:* significant framework
development effort to build the keyword engine, and debugging is harder. *Use for:*
letting manual QA testers on the Course Management team add new test scenarios without
writing Python.

**Hybrid**
Combines elements of Modular, Data-Driven, and (optionally) Keyword-Driven approaches to
get reusability, data parameterization, and sometimes accessibility for non-coders.
*Advantage:* most flexible and realistic for production use. *Disadvantage:* most
complex framework to design and maintain. *Use for:* the full Course Management
Selenium+pytest suite in Hands-On 6/7, which reuses Page Objects (Modular),
parametrizes tests with pytest (Data-Driven), and could add a keyword layer later.
