
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    """Basic home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
