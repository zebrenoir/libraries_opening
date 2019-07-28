# import requests
# import urllib
# from bs4 import BeautifulSoup

string = "Déménagement"

for stringo in string:
    if(stringo == "é"):
        string_array = string.split("é")

print(string_array)
