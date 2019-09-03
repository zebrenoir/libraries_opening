#!/usr/bin/env python3

import urllib
import datetime
from bs4 import BeautifulSoup as bs

"""
TODO: Need to get the opening info of the whole week,
    get everyday hours and put them in an object so I can use
    what I want (even if for now I only use the current day)
"""

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
        info_raw = soup.caption.string
        if info_raw == "Horaires d'ouverture":
            info_raw = "No info"
        print(info_raw)
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
            'info': info_raw
        }
        libraries.append(lib)

    return libraries
    # This prints all days in all libraries
    #    for i in range(len(days)):
    #        print(days[i].string + " : " + hours[i].string)
