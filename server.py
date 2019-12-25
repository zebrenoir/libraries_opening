#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
import biblihoraires
from data import get_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hours")
def generate_hours():

    libraries = biblihoraires.get_hours()
    return render_template("hours.html", libraries=libraries)


@app.route("/alexa")
def alexa():
    data = get_data()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

