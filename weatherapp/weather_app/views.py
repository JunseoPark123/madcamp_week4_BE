# weather_app/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .fetch_current_weather import fetch_current_weather
from .fetch_daily_weather import fetch_daily_weather
from .fetch_sunrise_sunset import fetch_sunrise_sunset
from .fetch_hourly_weather import fetch_hourly_weather

@api_view(['POST'])
def index(request):
    app_id = "cac9d514830b2b60066bcd3acb51fd7e"

    current_weather_url = "https://api.open-meteo.com/v1/dwd-icon?latitude={}&longitude={}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m&timezone={}"
    current_weather_url_sub = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly,daily&appid={}&units=metric"
    daily_weather_url = "https://api.open-meteo.com/v1/dwd-icon?latitude={}&longitude={}&daily=weather_code,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,precipitation_probability_max,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant&timezone={}"
    daily_weather_url_sub = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly&appid={}&units=metric"
    hourly_weather_url = "https://api.open-meteo.com/v1/dwd-icon?latitude={}&longitude={}&hourly=temperature_2m,relative_humidity_2m,dew_point_2m,apparent_temperature,precipitation_probability,precipitation,rain,showers,snowfall,snow_depth,weather_code,cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high&forecast_days=1&timezone={}"
    hourly_weather_url_sub = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,daily&appid={}&units=metric"
    sunrise_sunset_url = "https://api.sunrisesunset.io/json?lat={}&lng={}"
    sunrise_sunset_url_sub = "https://api.sunrise-sunset.org/json?lat={}&lng={}&date=today&tzid={}"
    timezone = "Asia/Seoul"

    try:
        data = request.data
        latitude = round(float(data.get("latitude")), 2)
        longitude = round(float(data.get("longitude")), 2)
    except (KeyError, ValueError):
        return Response({"error_message": "Invalid latitude or longitude."}, status=400)

    city_data = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
    }
    current_forecasts = fetch_current_weather(city_data, current_weather_url, current_weather_url_sub, app_id)
    daily_forecasts = fetch_daily_weather(city_data, daily_weather_url, daily_weather_url_sub, app_id)
    hourly_forecasts = fetch_hourly_weather(city_data, hourly_weather_url, hourly_weather_url_sub, app_id)
    sunrise_sunset_data = fetch_sunrise_sunset(city_data, sunrise_sunset_url, sunrise_sunset_url_sub)

    context = {
        "current_weather": current_forecasts,  # 현재 날씨
        "daily_forecasts": daily_forecasts,  # 일일 날씨 (7일)
        "hourly_forecasts": hourly_forecasts,  # 시간별 날씨 (24시간)
        "sunrise_sunset": sunrise_sunset_data,  # 일출 일몰  # 날씨 한글화 데이터
    }

    return Response(context)
