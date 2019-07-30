from flask import Flask, render_template
import jinja2
import urllib
import requests
import datetime
import lxml
from bs4 import BeautifulSoup as bs

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hours")
def generate_hours():
    url_libraries = "https://www.bm-lyon.fr/16-bibliotheques-et-un-bibliobus/"
    libraries_links = ["bibliotheque-du-1er/", "bibliotheque-du-2e/", "bibliotheque-du-4e-croix-rousse/",
                       "bibliotheque-du-5e-saint-jean/", "bibliotheque-du-7e-jean-mace/", "mediatheque-de-vaise/"]

    current_day = datetime.datetime.today().weekday()
    results = ""

    for library in libraries_links:
        html = urllib.request.urlopen(url_libraries + library).read()
        soup = bs(html, "lxml")
        table = soup.table
        days = table.find_all("th")
        hours = table.find_all("td")

        library_name = soup.h1.text
        print("\n" + library_name + "\n")

        # This prints all days in all libraries
        #    for i in range(len(days)):
        #        print(days[i].string + " : " + hours[i].string)

        results += (library_name + " : \n" + days[current_day].string + " : " + hours[current_day].string + "\n")

    return results


if __name__ == "__main__":
    app.run(debug=True)
