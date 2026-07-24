"""
Task 35 - locator ranking, most to least preferred:

1. ID           - unique, fast, readable
2. CSS selector - fast, flexible, readable
3. Name         - fine on forms, not always unique
4. XPath (relative, e.g. by attribute or text) - more powerful than CSS but a bit slower
5. Class/Tag name - usually matches more than one element, brittle on its own
6. XPath (absolute, /html/body/div[3]/...) - breaks with any markup change, avoid this
"""

if __name__ == "__main__":
    print(__doc__)
