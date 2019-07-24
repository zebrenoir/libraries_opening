import urllib
import requests
from bs4 import BeautifulSoup as bs

url_libraries = "https://www.bm-lyon.fr/16-bibliotheques-et-un-bibliobus/"
library_lyon1 = "bibliotheque-du-1er/"


lyon1_html = urllib.request.urlopen(url_libraries + library_lyon1).read()

"""
lyon2 = "voici une string je crois bien !!!!"
lyon2_array = lyon2.split(" ")
print(lyon2_array)

# lyon1_html_array = lyon1_html.split('printemps')

lyon_1_pretty = BeautifulSoup(lyon1_html, html.parser)

"""

soup = bs(lyon1_html, "lxml")
hours_table = soup.table
str(hours_table)
print(type(hours_table))
# hours_table_list = hours_table.split("<tr>")
