# HandsOn 7 — Page Object Model

Refactors the earlier tests to use Page Objects instead of calling `driver.find_element`
directly in the test files.

## Structure
```
pages/    BasePage + one page class per demo page
tests/    the actual pytest tests, using the page classes
utils/    config constants + a driver factory
```
`Task_50.py`–`Task_58.py` are the individual exercise steps; they mostly just run or
demonstrate what's in `pages/` and `tests/`.

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
pytest tests/ -v --html=report.html --self-contained-html
```
or
```bash
python Task_58.py
```
