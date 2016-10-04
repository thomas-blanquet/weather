import requests
import json


class Location:
    def __init__(self):
        _response = requests.get("http://ip-api.com/json").text
        locate = json.loads(_response)
        self.city = locate["city"]
        self.region = locate["region"]
        self.region_name = locate["regionName"]
        self.country = locate["country"]
        self.country_code = locate["countryCode"]
        self.lat = locate["lat"]
        self.long = locate["lon"]


class Weather:

    def __init__(self, api_key):
        self.location = Location()
        api_url = "http://api.openweathermap.org/data/2.5/weather?q=" + self.location.city + ","\
                  + self.location.country_code + "&APPID=" + api_key
        response = requests.get(api_url)
        self.weather = None
