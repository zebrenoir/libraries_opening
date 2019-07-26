import urllib
import requests
from bs4 import BeautifulSoup as bs

url_libraries = "https://www.bm-lyon.fr/16-bibliotheques-et-un-bibliobus/"
libraries_links = ["bibliotheque-du-1er/", "bibliotheque-du-2e/", "bibliotheque-du-4e-croix-rousse/",
                   "bibliotheque-du-5e-saint-jean/", "bibliotheque-du-7e-jean-mace/", "mediatheque-de-vaise/"]

for library in libraries_links:
    html = urllib.request.urlopen(url_libraries + library).read()
    soup = bs(html, "lxml")
    table = soup.table
    days = table.find_all("th")
    hours = table.find_all("td")

    library_name = soup.h1.text
    print("\n" + library_name + "\n")

    for i in range(len(libraries_links)):
        print(days[i].string + " : " + hours[i].string)

print("\n")

"""
Add a way to show the current day opening hours in all libraries
first by manual input, then by sytem datetime check

Check the holiday closing dates and show if a library is closed for holidays
Otherwise the hours will be wrong.
"""
