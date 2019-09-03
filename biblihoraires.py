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


    def clean_hours(hours_raw):
        if hours_raw == "fermée":
            cleaned_hours = False
        else:
            hours_raw = hours_raw.replace("h", "")
            cleaned_hours = hours_raw.split(" à ")

        if len(cleaned_hours) == 2:
            cleaned_hours = cleaned_hours[0] + "h -> " + cleaned_hours[1] + "h"

        return cleaned_hours

    for library in libraries_links:
        html = urllib.request.urlopen(url_libraries + library).read()
        soup = bs(html, "lxml")
        table = soup.table
        days = table.find_all("th")
        hours = table.find_all("td")
        library_name = soup.h1.text
        info_raw = soup.caption.string
        address = soup.find("div", class_="bib_adresse").string
        print(info_raw)

# TODO: test if the holidays is present on the site, otherwise empty string for holidays
        lib = {
            'name': library_name,
            'day': days[current_day].string,
            'hours': hours[current_day].string,
            'info': info_raw,
            'address': address,
            'maps' : "https://www.google.fr/maps/place/" + address
        }
        libraries.append(lib)

    return libraries
    # This prints all days in all libraries
    #    for i in range(len(days)):
    #        print(days[i].string + " : " + hours[i].string)
