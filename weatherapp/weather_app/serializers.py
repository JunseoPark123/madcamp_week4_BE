# weather_app/serializers.py
from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    current_weather = serializers.ListField(child=serializers.DictField())
    daily_forecasts = serializers.ListField(child=serializers.DictField())
    sunrise_sunset = serializers.DictField()