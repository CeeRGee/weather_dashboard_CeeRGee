# weather.py

import requests
from config import API_KEY, BASE_URL, DEFAULT_CITY

def fetch_weather_data(city=DEFAULT_CITY):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=imperial"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
