"""
URL configuration for weather_project.
"""
from django.contrib import admin
from django. urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),  # Include weather app URLs
]