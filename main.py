import requests
import os
import weather
from lxml import html

api_key = os.environ['OWM_KEY']

weather = weather.Weather(api_key)



