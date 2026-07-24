# Task 59 — Why POM Matters

If the Submit button's ID changed from `submit` to `btn-submit` in a flat script where
`driver.find_element(By.ID, "submit")` is copy-pasted into every test, every one of
those tests breaks and each copy has to be found and fixed by hand.

With POM the locator exists in exactly one place — `SimpleFormPage.SUBMIT_BUTTON`.
Tests call `page.click_submit()`, not the locator directly, so fixing the ID means
changing one line in `pages/simple_form_page.py` and every test that uses it is fixed
automatically.
