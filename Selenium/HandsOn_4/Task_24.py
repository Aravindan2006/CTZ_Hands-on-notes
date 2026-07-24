"""
Task 24 - quick notes on Selenium's architecture.

WebDriver: talks to the browser directly (via the W3C WebDriver protocol / the
browser's driver binary like chromedriver). This is what we use for automation.

Selenium Grid: runs tests in parallel across multiple machines/browsers. Useful once
your suite gets big enough that running everything sequentially is too slow.

Selenium IDE: browser extension for record-and-playback. Good for quickly prototyping
a flow or for people who don't want to write code, but not something you'd build a real
suite on top of.
"""

if __name__ == "__main__":
    print("WebDriver -> drives the browser")
    print("Grid -> parallel/cross-browser execution")
    print("IDE -> record & playback")
