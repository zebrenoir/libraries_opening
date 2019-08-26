#!/usr/bin/env python3

import urllib
import datetime
from bs4 import BeautifulSoup as bs


def get_hours():

    url_libraries = "https://www.bm-lyon.fr/16-bibliotheques-et-un-bibliobus/"
    libraries_links = ["bibliotheque-du-1er/", "bibliotheque-du-2e/", "bibliotheque-du-4e-croix-rousse/",
                       "bibliotheque-du-5e-saint-jean/", "bibliotheque-du-7e-jean-mace/", "mediatheque-de-vaise/"]

    current_day = datetime.datetime.today().weekday()

    libraries = []

    for library in libraries_links:
        html = urllib.request.urlopen(url_libraries + library).read()
        soup = bs(html, "lxml")
        table = soup.table
        days = table.find_all("th")
        hours = table.find_all("td")
        library_name = soup.h1.text
        holidays_raw = soup.caption.string
        """
        if holidays_raw == "Horaires d'ouverture":
            holidays = "No holidays"
        else:
            holidays = holidays_raw.split("FERMETURE ")[1]
        
        print("\n" + library_name + "\n")
        """
# TODO: test if the holidays is present on the site, otherwise empty string for holidays
        lib = {
            'name': library_name,
            'day': days[current_day].string,
            'hours': hours[current_day].string,
#            'holidays': holidays
        }
        libraries.append(lib)

    return libraries
    # This prints all days in all libraries
    #    for i in range(len(days)):
    #        print(days[i].string + " : " + hours[i].string)
