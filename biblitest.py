import urllib
import requests
import datetime
from bs4 import BeautifulSoup as bs
def generate_hours():
    url_libraries = "https://www.bm-lyon.fr/16-bibliotheques-et-un-bibliobus/"
    libraries_links = ["bibliotheque-du-1er/", "bibliotheque-du-2e/", "bibliotheque-du-4e-croix-rousse/",
                       "bibliotheque-du-5e-saint-jean/", "bibliotheque-du-7e-jean-mace/", "mediatheque-de-vaise/"]

    current_day = datetime.datetime.today().weekday()

    """
    input_day = input("Pour quel jour de la semaine souhaitez-vous voir les horaires ?\n"
                      "(en minuscules en français sans espaces)\n")
    
    if input_day:
        if input_day == "lundi":
            input_day = 0
        elif input_day == "mardi":
            input_day = 1
        elif input_day == "mercredi":
            input_day = 2
        elif input_day == "jeudi":
            input_day = 3
        elif input_day == "vendredi":
            input_day = 4
        elif input_day == "samedi":
            input_day = 5
        elif input_day == "dimanche":
            input_day = 6
        else:
            print("Oh boy, I'm afraid this is not working between us :'(")
            raise SystemExit(0)
    else:
        print("Oh come on you lazy cow!")
        raise SystemExit(0)
    
    # lundi = 0
    # mardi = 1
    # mercredi = 2
    # jeudi = 3
    # vendredi = 4
    # samedi = 5
    # dimanche = 6
    """

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

        print(days[current_day].string + " : " + hours[current_day].string)

    print("\n")

    """
    Add a way to show either the current day opening hours in all libraries
    either all days in all libraries
    first by manual input, then by sytem datetime check
    
    Check the holiday closing dates and show if a library is closed for holidays
    Otherwise the hours will be wrong.
    """

generate_hours()
