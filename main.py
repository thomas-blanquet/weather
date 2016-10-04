import os
import weather

api_key = os.environ['OWM_KEY']
weather = weather.Weather(api_key)



