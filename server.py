#!/usr/bin/env python3

from flask import Flask, render_template
import biblihoraires

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hours")
def generate_hours():

    libraries = biblihoraires.get_hours()
    return render_template("hours.html", libraries=libraries)


if __name__ == "__main__":
    app.run(debug=True)
