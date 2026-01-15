"""
Views for the weather app.
This file handles the logic for fetching weather data and rendering templates.
"""
from django.shortcuts import render
from django.conf import settings
import requests
from django.contrib import messages
from datetime import datetime


def index(request):
    """
    Main view for the weather app.
    Fetches weather data from OpenWeather API and displays it.
    Supports both city name search and geolocation (lat/lon).
    """
    
    # Initialize context with default values
    context = {
        'weather_data': None,
        'city':  None,
        'error': None
    }
    
    # Check if user submitted a search (city or geolocation)
    if request.method == 'POST': 
        city = request.POST.get('city', '').strip()
        lat = request.POST.get('lat', '').strip()
        lon = request.POST.get('lon', '').strip()
        
        # OpenWeather API configuration
        api_key = settings.OPENWEATHER_API_KEY
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # Build parameters based on input type
        if lat and lon:
            # Geolocation-based search
            params = {
                'lat': lat,
                'lon': lon,
                'appid': api_key,
                'units': 'metric'
            }
        elif city:
            # City name search
            params = {
                'q': city,
                'appid': api_key,
                'units': 'metric'
            }
        else:
            context['error'] = "Please enter a city name or allow location access."
            return render(request, 'weather/index.html', context)
        
        try:
            # Make API request
            response = requests.get(base_url, params=params, timeout=10)
            
            # Check if request was successful
            if response.status_code == 200:
                data = response.json()
                
                # Extract relevant weather information
                weather_data = {
                    'city':  data['name'],
                    'country': data['sys']['country'],
                    'temperature': round(data['main']['temp']),
                    'feels_like': round(data['main']['feels_like']),
                    'description': data['weather'][0]['description'].title(),
                    'icon': data['weather'][0]['icon'],
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'wind_speed': round(data['wind']['speed'] * 3.6, 1),
                    'visibility': round(data.get('visibility', 0) / 1000, 1),
                    'temp_min': round(data['main']['temp_min']),
                    'temp_max': round(data['main']['temp_max']),
                }
                
                context['weather_data'] = weather_data
                context['city'] = data['name']

                # Fetch 5-Day Forecast (use lat/lon from response for accuracy)
                forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
                forecast_params = {
                    'lat': data['coord']['lat'],
                    'lon': data['coord']['lon'],
                    'appid': api_key,
                    'units': 'metric'
                }
                forecast_response = requests.get(forecast_url, params=forecast_params, timeout=10)
                
                if forecast_response.status_code == 200:
                    forecast_raw = forecast_response.json()
                    forecast_data = []
                    
                    for item in forecast_raw['list']:
                        if '12:00:00' in item['dt_txt']:
                            date_obj = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')
                            forecast_data.append({
                                'date': date_obj.strftime('%a, %d %b'), 
                                'temperature': round(item['main']['temp']),
                                'description': item['weather'][0]['description'].title(),
                                'icon': item['weather'][0]['icon']
                            })
                            
                            if len(forecast_data) >= 5:
                                break
                    
                    context['forecast_data'] = forecast_data
                
            elif response.status_code == 404:
                context['error'] = f"Location not found. Please try again."
            else:
                context['error'] = "Unable to fetch weather data. Please try again later."
                
        except requests.exceptions.Timeout:
            context['error'] = "Request timed out. Please check your internet connection."
        except requests.exceptions.RequestException as e:
            context['error'] = "An error occurred while fetching weather data."
        except KeyError: 
            context['error'] = "Error processing weather data. Please try again."
    
    return render(request, 'weather/index.html', context)