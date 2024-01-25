# weather_app/models.py
# weather_app/models.py
from django.db import models

class Weather(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()