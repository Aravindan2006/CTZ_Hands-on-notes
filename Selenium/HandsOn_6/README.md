# HandsOn 6 — pytest + Selenium

Wires the earlier scripts into pytest: shared fixtures, parametrized tests, an HTML
report, and a screenshot-on-failure hook.

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
pytest -v                    # everything (11 tests, including 3 parametrized + 1 intentional failure)
pytest Task_42.py Task_43.py -v
python Task_47.py            # generates report.html
```

Test files are named `Task_N.py` instead of `test_*.py` (matches the exercise's file
naming), so `pytest.ini` extends discovery to pick them up.

`Task_46.py` fails on purpose — it's there to prove the failure-screenshot hook in
`conftest.py` actually works. Check `screenshots/` after running it.
