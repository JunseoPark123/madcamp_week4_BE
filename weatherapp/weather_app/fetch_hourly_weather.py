import datetime
import requests
from .date_korean_encoder import date_korean_encoder
from .weather_korean_encoder import weather_korean_encoder

def fetch_hourly_weather(city_data, hourly_weather_url, hourly_weather_url_sub, app_id):

    latitude = city_data["latitude"]
    longitude = city_data["longitude"]
    timezone = city_data["timezone"]

    hourly_weather_response = requests.get(hourly_weather_url.format(latitude, longitude, timezone)).json()
    print('hourly_weather_response',hourly_weather_response)

    hourly_weather_response_sub = requests.get(hourly_weather_url_sub.format(latitude, longitude, app_id)).json()
    print('hourly_weather_response_sub',hourly_weather_response_sub)

    hourly_weather_response_sub = hourly_weather_response_sub["hourly"][:24]

    hourly_forecasts = []
    for index in range(len(hourly_weather_response["hourly"]["time"])):
        try:
            date_time = hourly_weather_response["hourly"]["time"][index]
            hourly_data = {
                "temperature_2m": hourly_weather_response["hourly"]["temperature_2m"][index],
                "relative_humidity_2m": hourly_weather_response["hourly"]["relative_humidity_2m"][index],
                "dew_point_2m": hourly_weather_response["hourly"]["dew_point_2m"][index],
                "apparent_temperature": hourly_weather_response["hourly"]["apparent_temperature"][index],
                "precipitation": hourly_weather_response["hourly"]["precipitation"][index],
                "rain": hourly_weather_response["hourly"]["rain"][index],
                "showers": hourly_weather_response["hourly"]["showers"][index],
                "snowfall": hourly_weather_response["hourly"]["snowfall"][index],
                "snow_depth": hourly_weather_response["hourly"]["snow_depth"][index],
                "cloud_cover_total": hourly_weather_response["hourly"]["cloud_cover"][index],
                "cloud_cover_low": hourly_weather_response["hourly"]["cloud_cover_low"][index],
                "cloud_cover_mid": hourly_weather_response["hourly"]["cloud_cover_mid"][index],
                "cloud_cover_high": hourly_weather_response["hourly"]["cloud_cover_high"][index],
                "weather_id": hourly_weather_response_sub[index]["weather"][0]["id"],
                "weather_main": hourly_weather_response_sub[index]["weather"][0]["main"],
                "weather_description": hourly_weather_response_sub[index]["weather"][0]["description"],
                "weather_icon": hourly_weather_response_sub[index]["weather"][0]["icon"],
                "visibility": hourly_weather_response_sub[index]["visibility"],
            }

            date_str = datetime.datetime.fromisoformat(date_time).strftime("%Y-%m-%d").split('-')
            year = int(date_str[0])
            month = int(date_str[1])
            day = int(date_str[2])

            hourly_forecasts.append({
                "date": datetime.datetime.fromisoformat(date_time).strftime("%Y-%m-%d"),
                "time": datetime.datetime.fromisoformat(date_time).strftime("%H:%M"),
                **hourly_data,
                "date_korean": date_korean_encoder(year, month, day),
                "weather_korean": weather_korean_encoder(hourly_data["weather_id"], hourly_data["rain"], hourly_data["showers"], month),
            })

        except KeyError as e:
            print(f"Error in processing hourly forecast data: {e}")


    return hourly_forecasts