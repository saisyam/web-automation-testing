from splinter import Browser

url = "https://google.com"

browser = Browser('chrome', headless=True)
browser.visit(url)
assert browser.title == "Google"
browser.quit()