import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
APP_ID = os.getenv("APP_ID")

class OpenWeatherError(Exception):
    """Custom exception for OpenWeather API errors."""
    pass

def get_weather(city: str, appid: str | None = APP_ID) -> requests.Response:
    """
    Fetch weather data for a given city from OpenWeather API.
    Args:
        city (str): Name of the city.
        appid (str, optional): API key.
    Returns:
        requests.Response: The HTTP response object.
    Raises:
        OpenWeatherError: If the API call fails.
    """
    
    params = {}
    if city:
        params = {"q": city}
    if appid:
        params["appid"] = appid
    response = requests.get(BASE_URL, params=params)
    # if response.status_code != 200:
    #     raise OpenWeatherError(f"Error fetching weather data: {response.status_code}")

    return response
