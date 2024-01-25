import datetime
import requests
from .date_korean_encoder import date_korean_encoder
from .weather_korean_encoder import weather_korean_encoder

def fetch_daily_weather(city_data, daily_weather_url, daily_weather_url_sub, app_id):

    latitude = city_data["latitude"]
    longitude = city_data["longitude"]
    timezone = city_data["timezone"]

    daily_weather_response = requests.get(daily_weather_url.format(latitude, longitude, timezone)).json()
    print('daily_weather_response',daily_weather_response)

    daily_weather_response_sub = requests.get(daily_weather_url_sub.format(latitude, longitude, app_id)).json()
    print('daily_weather_response_sub',daily_weather_response_sub)

    daily_forecasts = []
    for index in range(len(daily_weather_response["daily"]["time"])):
        try:
            date = daily_weather_response["daily"]["time"][index]
            daily_data = {
                "temperature_2m_max": daily_weather_response["daily"]["temperature_2m_max"][index],
                "temperature_2m_min": daily_weather_response["daily"]["temperature_2m_min"][index],
                "apparent_temperature_max": daily_weather_response["daily"]["apparent_temperature_max"][index],
                "apparent_temperature_min": daily_weather_response["daily"]["apparent_temperature_min"][index],
                "precipitation_sum": daily_weather_response["daily"]["precipitation_sum"][index],
                "rain_sum": daily_weather_response["daily"]["rain_sum"][index],
                "showers_sum": daily_weather_response["daily"]["showers_sum"][index],
                "snowfall_sum": daily_weather_response["daily"]["snowfall_sum"][index],
                "precipitation_hours": daily_weather_response["daily"]["precipitation_hours"][index],
                "wind_speed_10m_max": daily_weather_response["daily"]["wind_speed_10m_max"][index],
                "wind_gusts_10m_max": daily_weather_response["daily"]["wind_gusts_10m_max"][index],
                "wind_direction_10m_dominant": daily_weather_response["daily"]["wind_direction_10m_dominant"][index],
                "weather_id": daily_weather_response_sub["daily"][index]["weather"][0]["id"],
                "weather_main": daily_weather_response_sub["daily"][index]["weather"][0]["main"],
                "weather_description": daily_weather_response_sub["daily"][index]["weather"][0]["description"],
                "weather_icon": daily_weather_response_sub["daily"][index]["weather"][0]["icon"],
                "moon_phase": daily_weather_response_sub["daily"][index]["moon_phase"],
                "clouds": daily_weather_response_sub["daily"][index]["clouds"],
            }

            date_str = datetime.datetime.fromisoformat(date).strftime("%Y-%m-%d").split('-')
            year = int(date_str[0])
            month = int(date_str[1])
            day = int(date_str[2])

            daily_forecasts.append({
                "date": datetime.datetime.fromisoformat(date).strftime("%Y-%m-%d"),
                "day": datetime.datetime.fromisoformat(date).strftime("%A"),
                **daily_data,
                "date_korean": date_korean_encoder(year, month, day),
                "weather_korean": weather_korean_encoder(daily_data["weather_id"], daily_data["rain_sum"], daily_data["showers_sum"], month),
            })

        except KeyError as e:
            print(f"Error in processing daily forecast data: {e}")


    return daily_forecasts