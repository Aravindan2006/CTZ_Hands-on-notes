# HandsOn 5 — Locators & Explicit Waits

Practising all the locator strategies and swapping hardcoded sleeps for explicit waits.

## Setup
Same deps as Hands-On 4: `pip install selenium webdriver-manager`

## Run
```bash
python Task_32.py   # ID/name/class/tag/xpath, all on one element
python Task_33.py   # CSS selectors
python Task_34.py   # xpath text() / contains()
python Task_35.py   # locator ranking (just prints notes)
python Task_36.py   # WebDriverWait + visibility
python Task_37.py   # sleep(3) vs explicit wait, timed
python Task_38.py   # clickable vs visible
python Task_39.py   # fluent-style wait
```

`Task_37.py` is the only file in this project that uses `time.sleep()` — it's there on
purpose, to compare it against an explicit wait.
