# app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Python Application Running"

app.run(host="1.0.0.", port=5000)
