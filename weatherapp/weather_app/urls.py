# weather_app/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('weather/', index, name='weather'),
]