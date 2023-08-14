from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import requests
import json


def get_picture_url(query):

    url = f"https://api.pexels.com/v1/search?query={query}"
    headers = {"Authorization": PEXELS_API_KEY}

    response = requests.get(url, headers=headers)
    pic = json.loads(response.content)

    return pic["photos"][0]["src"]["original"]


def get_weather_data(q):

    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={q}&appid={OPEN_WEATHER_API_KEY}"

    response = requests.get(geo_url)
    coord = json.loads(response.content)[0]
    coord_lat = coord["lat"]
    coord_lon = coord["lon"]

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={coord_lat}&lon={coord_lon}&appid={OPEN_WEATHER_API_KEY}"

    weather_response = requests.get(weather_url)
    weather = json.loads(weather_response.content)

    weather_dict = {
        "temp": weather["main"]["temp"],
        "description": weather["weather"][0]["description"],
    }
    return weather_dict
