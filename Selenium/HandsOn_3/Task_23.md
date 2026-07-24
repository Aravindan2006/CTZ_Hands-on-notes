# Task 23 — Hybrid Framework Folder Structure

```
Course_Management_Frontend_Tests/
├── config/
│   └── config.py            # base_url, browser, timeout settings
├── test_data/
│   ├── login_data.csv       # 50 username/password combinations
│   └── course_data.json     # course-creation payload variations
├── pages/
│   ├── base_page.py         # shared driver/wait utilities
│   ├── login_page.py        # LoginPage Page Object
│   └── course_page.py       # CoursePage Page Object
├── utils/
│   ├── driver_factory.py    # WebDriver creation (Chrome/headless)
│   └── helpers.py           # generic assertion/screenshot helpers
├── tests/
│   ├── test_login.py        # data-driven login tests (uses login_data.csv)
│   └── test_course_crud.py  # course create/edit/delete tests
├── keywords/                # optional keyword-driven layer for non-coders
│   └── keyword_map.py       # maps keyword strings to Page Object calls
├── reports/
│   └── report.html          # pytest-html output
├── conftest.py               # pytest fixtures (driver setup/teardown)
├── requirements.txt
└── README.md
```

- `test_data/` and `config/` give the Data-Driven parameterization.
- `pages/` gives the Modular reusability (Page Object Model).
- `utils/` centralizes cross-cutting concerns (driver setup, helpers) to avoid duplicate
  code.
- `keywords/` is the optional bridge for non-technical contributors.
