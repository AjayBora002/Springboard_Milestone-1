from typing import Dict, List, Union, Any
from pathlib import Path
import requests
import os
from dotenv import load_dotenv

# Load API Key from .env (Look in project root)
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
API_KEY: Union[str, None] = os.getenv("OPENWEATHER_API_KEY")

BASE_URL: str = "https://api.openweathermap.org/data/2.5/weather"

def get_live_weather(city_name: str) -> Dict[str, Any]:
    """
    Fetches real-time weather metrics for a given city from OpenWeatherMap.

    Args:
        city_name (str): The name of the city (e.g., 'London' or 'Mumbai, IN').

    Returns:
        Dict[str, Any]: A dictionary containing weather data or an error message.
    """
    if not API_KEY or API_KEY == "your_api_key_here":
        return {"error": "API Key not configured. Please add your key to a .env file."}
    
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric" # Celsius
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].capitalize(),
            "wind_speed": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"]
        }
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {"error": f"City '{city_name}' not found."}
        return {"error": f"Weather API returned an error: {response.status_code}"}
    except requests.exceptions.Timeout:
        return {"error": "Connection timed out. Please try again later."}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

def get_forecast(city_name: str) -> Union[List[Dict[str, Any]], Dict[str, str]]:
    """
    Fetches a 5-day weather forecast (3-hour intervals) for a given city.

    Args:
        city_name (str): The name of the city.

    Returns:
        Union[List[Dict[str, Any]], Dict[str, str]]: List of daily summaries or error dict.
    """
    FORECAST_URL: str = "https://api.openweathermap.org/data/2.5/forecast"
    
    if not API_KEY or API_KEY == "your_api_key_here":
        return {"error": "API Key not configured."}
    
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    
    try:
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Simplify forecast data - take the mid-day forecast for each of the 5 days
        forecasts = []
        # The API returns 8 points per day (every 3 hours)
        for item in data["list"][::8]: 
            forecasts.append({
                "date": item["dt_txt"].split(" ")[0],
                "temp": item["main"]["temp"],
                "description": item["weather"][0]["description"].capitalize(),
                "icon": item["weather"][0]["icon"]
            })
        return forecasts
    except Exception as e:
        return {"error": f"Forecast fetch failed: {str(e)}"}
