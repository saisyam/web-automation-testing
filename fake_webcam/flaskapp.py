from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('webcam.html')

if __name__ == '__main__':
    app.run(debug=True)
