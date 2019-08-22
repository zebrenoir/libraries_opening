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
    results = ""
    for library in libraries:
        # results += "{name}<br/> {day} : {hours} <br/> VACANCES {holidays}<br/>".format(name=library["name"],
        #          day=library["day"], hours=library["hours"], holidays=library["holidays"])
        # results += "{name}<br/> {day} : {hours} <br/> VACANCES {holidays}<br/>".format(**library)
        results += f"{library['name']}<br/> {library['day']} : {library['hours']} <br/> VACANCES {library['holidays']}<br/>"
    # return render_template("hours.html", libraries)
    trial = "Biblifoliiiiiiiiiiiii'z!!!!"
    return render_template("hours.html", libraries=libraries)


if __name__ == "__main__":
    app.run(debug=True)
