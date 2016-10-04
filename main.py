import requests
import os
from lxml import html

api_key = os.environ['OWM_KEY']

def get_elem_div(div, elem):
    return [d.text_content() for d in div
            if elem in d.text_content().split(":")[0]][0].replace('\t', '').replace('\n', '').split(":")[1]

def get_location():
    geo_url = "https://geoiptool.com/"
    response = requests.get(geo_url)
    txt = response.text
    doc = html.fromstring(txt)
    div = doc.cssselect("div")
    country = get_elem_div(div, "Country Code").split(" ")[0]
    city = get_elem_div(div, "City")
    return country, city

country, city = get_location()
url_weather = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country + "&APPID=" + api_key
response = requests.get(url_weather)
print(response)



