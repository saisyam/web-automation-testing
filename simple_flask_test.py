from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.errorhandler(404)
def page_not_found(e):
    return 'Oops! 404', 404

from splinter import Browser

browser = Browser("flask", app=app)
browser.visit("http://localhost:5000")
assert "Hello, World!" == browser.html

browser.visit("http://localhost:5000/users")
assert "Oops! 404" == browser.html