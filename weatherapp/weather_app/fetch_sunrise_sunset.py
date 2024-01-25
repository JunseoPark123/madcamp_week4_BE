from datetime import datetime, timedelta
import requests
import locale
from astral import LocationInfo
from astral.sun import golden_hour
from astral.sun import blue_hour
from astral.sun import SunDirection

def fetch_sunrise_sunset(city_data, sunrise_sunset_url, sunrise_sunset_url_sub):

    latitude = city_data["latitude"]
    longitude = city_data["longitude"]
    timezone = city_data["timezone"]
    
    sunrise_sunset_response = requests.get(sunrise_sunset_url.format(latitude, longitude)).json()
    print('sunrise_sunset_response',sunrise_sunset_response)

    sunrise_sunset_response_sub = requests.get(sunrise_sunset_url_sub.format(latitude, longitude, timezone)).json()
    print('sunrise_sunset_response_sub',sunrise_sunset_response_sub)


    sunrise_sunset_forecasts = []
    sunrise_sunset_data = sunrise_sunset_response["results"]
    sunrise_sunset_data_sub = sunrise_sunset_response_sub["results"]

    city = LocationInfo(name="Seoul", region="Korea", timezone=timezone, latitude=latitude, longitude=longitude)
    print('city',city)

    gh_m = golden_hour(city.observer, datetime.now().date())
    bh_m = blue_hour(city.observer, datetime.now().date())

    gh_d = golden_hour(city.observer, datetime.now().date(), SunDirection.SETTING)
    bh_d = blue_hour(city.observer, datetime.now().date(), SunDirection.SETTING)

    gh_m_start = (gh_m[0] + timedelta(hours = 9)).strftime("%H:%M:%S")
    gh_m_end = (gh_m[1] + timedelta(hours = 9)).strftime("%H:%M:%S")
    bh_m_start = (bh_m[0] + timedelta(hours = 9)).strftime("%H:%M:%S")
    bh_m_end = (bh_m[1] + timedelta(hours = 9)).strftime("%H:%M:%S")

    gh_d_start = (gh_d[0] + timedelta(hours = 9)).strftime("%H:%M:%S")
    gh_d_end = (gh_d[1] + timedelta(hours = 9)).strftime("%H:%M:%S")
    bh_d_start = (bh_d[0] + timedelta(hours = 9)).strftime("%H:%M:%S")
    bh_d_end = (bh_d[1] + timedelta(hours = 9)).strftime("%H:%M:%S")

    print("Golden hour start: " + gh_m_start)
    print("Golden hour end: " + gh_m_end)
    print("Blue hour start: " + bh_m_start)
    print("Blue hour end: " + bh_m_end)

    print("Golden hour start: " + gh_d_start)
    print("Golden hour end: " + gh_d_end)
    print("Blue hour start: " + bh_d_start)
    print("Blue hour end: " + bh_d_end)

    try:
        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')

        sunrise_sunset_forecasts.append({
            "sunrise": datetime.strptime(sunrise_sunset_data.get("sunrise", ""), "%I:%M:%S %p").strftime("%H:%M:%S"),
            "sunset": datetime.strptime(sunrise_sunset_data.get("sunset", ""), "%I:%M:%S %p").strftime("%H:%M:%S"),
            "dawn": datetime.strptime(sunrise_sunset_data.get("dawn", ""), "%I:%M:%S %p").strftime("%H:%M:%S"),
            "dusk": datetime.strptime(sunrise_sunset_data.get("dusk", ""), "%I:%M:%S %p").strftime("%H:%M:%S"),
            "golden_hour": datetime.strptime(sunrise_sunset_data.get("golden_hour", ""), "%I:%M:%S %p").strftime("%H:%M:%S"),
            "civil_twilight_begin": datetime.strptime(sunrise_sunset_data_sub.get("civil_twilight_begin", ""), "%I:%M:%S %p").strftime("%H:%M:%S"),
            "civil_twilight_end": datetime.strptime(sunrise_sunset_data_sub.get("civil_twilight_end", ""), "%I:%M:%S %p").strftime("%H:%M:%S"),
            "nautical_twilight_begin": datetime.strptime(sunrise_sunset_data_sub.get("nautical_twilight_begin", ""), "%I:%M:%S %p").strftime("%H:%M:%S"),
            "nautical_twilight_end": datetime.strptime(sunrise_sunset_data_sub.get("nautical_twilight_end", ""), "%I:%M:%S %p").strftime("%H:%M:%S"),
            "astronomical_twilight_begin": datetime.strptime(sunrise_sunset_data_sub.get("astronomical_twilight_begin", ""), "%I:%M:%S %p").strftime("%H:%M:%S"),
            "astronomical_twilight_end": datetime.strptime(sunrise_sunset_data_sub.get("astronomical_twilight_end", ""), "%I:%M:%S %p").strftime("%H:%M:%S"),
            "golden_hour_morning_start": gh_m_start,
            "golden_hour_morning_end": gh_m_end,
            "golden_hour_evening_start": gh_d_start,
            "golden_hour_evening_end": gh_d_end,
            "blue_hour_morning_start": bh_m_start,
            "blue_hour_morning_end": bh_m_end,
            "blue_hour_evening_start": bh_d_start,
            "blue_hour_evening_end": bh_d_end,
        })
    except KeyError as e:
        print(f"Error in processing sunrise sunset data: {e}")


    return sunrise_sunset_forecasts
'''
sun_color = "#FFFFFF"
if weather_id / 100 == 2:
    return sun_color = "#6B6B6B"
elif weather_id / 100 == 3:
    return sun_color = "#5C6E70"
elif weather_id / 100 == 5:
    return sun_color = "#3D85C6"
elif weather_id / 100 == 6:
    return sun_color = "#D9D9D9"
elif weather_id / 100 == 7:
    return sun_color = "#B66D05"
elif weather_id == 800:
    return sun_color = "#FFD966"
else:
    return sun_color = "#CFE2F3"

'''