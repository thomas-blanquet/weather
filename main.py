import requests
from lxml import html

def get_elem_div(div, elem):
    return [d.text_content() for d in div
            if elem in d.text_content().split(":")[0]][0].replace('\t', '').replace('\n', '').split(":")[1]

def get_location():
    geo_url = "https://geoiptool.com/"
    response = requests.get(geo_url)
    txt = response.text
    doc = html.fromstring(txt)
    div = doc.cssselect("div")
    country = get_elem_div(div, "Country")
    region = get_elem_div(div, "Region")
    city = get_elem_div(div, "City")
    return country, region, city

print(get_location())



