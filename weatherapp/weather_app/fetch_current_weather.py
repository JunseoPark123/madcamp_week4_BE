import datetime
import requests
from korean_lunar_calendar import KoreanLunarCalendar
from .date_korean_encoder import date_korean_encoder
from .weather_korean_encoder import weather_korean_encoder

def fetch_current_weather(city_data, current_weather_url, current_weather_url_sub, app_id):

    latitude = city_data["latitude"]
    longitude = city_data["longitude"]
    timezone = city_data["timezone"]

    current_weather_response = requests.get(current_weather_url.format(latitude, longitude, timezone)).json()
    print('current_weather_response', current_weather_response)

    current_weather_response_sub = requests.get(current_weather_url_sub.format(latitude, longitude, app_id)).json()
    print('current_weather_response_sub', current_weather_response_sub)

    calendar = KoreanLunarCalendar()
    
    current_forecasts = []
    
    current_data = current_weather_response["current"]
    date_time_str = current_data.get("time", "")

    current_data_sub = current_weather_response_sub["current"]

    date_time_str = current_data.get("time", "")
    datetime_obj = datetime.datetime.fromisoformat(date_time_str)

    year = datetime_obj.year
    month = datetime_obj.month
    day = datetime_obj.day

    calendar.setSolarDate(year, month, day)

    current_forecasts.append({
        "date": datetime_obj.strftime("%Y-%m-%d"),
        "lunar_date": calendar.LunarIsoFormat(),
        "time": datetime_obj.strftime("%H:%M"),
        "temperature": current_data.get("temperature_2m", 0),
        "apparent_temperature": current_data.get("apparent_temperature", 0),
        "percipitation": current_data.get("precipitation", 0),
        "rain": current_data.get("rain", 0),
        "showers": current_data.get("showers", 0),
        "snowfall": current_data.get("snowfall", 0),
        "cloud_cover": current_data.get("cloud_cover", 0),
        "wind_speed": current_data.get("wind_speed_10m", 0),
        "wind_direction": current_data.get("wind_direction_10m", 0),
        "humidity": current_data.get("relative_humidity_2m", 0),
        "visibility": current_data_sub.get("visibility", 0),
        "weather_id": current_data_sub.get("weather")[0].get("id", 0),
        "weather_main": current_data_sub.get("weather")[0].get("main", ""),
        "weather_description": current_data_sub.get("weather")[0].get("description", ""),
        "weather_icon": current_data_sub.get("weather")[0].get("icon", ""),
        "date_korean": date_korean_encoder(year, month, day),
        "weather_korean": weather_korean_encoder(current_data_sub.get("weather")[0].get("id", 0), current_data.get("rain", 0), current_data.get("showers", 0), month),
        "is_day": current_data_sub.get("is_day", 0),
    })

    
    return current_forecasts