import re
from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_flask.html",
        name=name,
        date=datetime.now()
    )