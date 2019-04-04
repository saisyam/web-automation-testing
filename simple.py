from splinter import Browser

url = "https://saisyam.com"
browser = Browser()
browser.visit(url)
assert browser.title == "Saisyam – Personal Blog"
browser.quit()

