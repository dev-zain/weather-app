"""
Views for the weather app.
This file handles the logic for fetching weather data and rendering templates.
"""
from django.shortcuts import render
from django.conf import settings
import requests
from django.contrib import messages


def index(request):
    """
    Main view for the weather app.
    Fetches weather data from OpenWeather API and displays it.
    """
    
    # Initialize context with default values
    context = {
        'weather_data': None,
        'city':  None,
        'error': None
    }
    
    # Check if user submitted a city search
    if request.method == 'POST': 
        city = request.POST. get('city', '').strip()
        
        if city:
            # OpenWeather API configuration
            api_key = settings. OPENWEATHER_API_KEY
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            
            # Parameters for the API request
            params = {
                'q': city,
                'appid': api_key,
                'units': 'metric'  # Use metric units (Celsius)
            }
            
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
                        'description': data['weather'][0]['description']. title(),
                        'icon': data['weather'][0]['icon'],
                        'humidity': data['main']['humidity'],
                        'pressure': data['main']['pressure'],
                        'wind_speed': round(data['wind']['speed'] * 3.6, 1),  # Convert m/s to km/h
                        'visibility': round(data. get('visibility', 0) / 1000, 1),  # Convert to km
                        'temp_min': round(data['main']['temp_min']),
                        'temp_max': round(data['main']['temp_max']),
                    }
                    
                    context['weather_data'] = weather_data
                    context['city'] = city
                    
                elif response.status_code == 404:
                    context['error'] = f"City '{city}' not found.  Please try again."
                else:
                    context['error'] = "Unable to fetch weather data. Please try again later."
                    
            except requests.exceptions. Timeout:
                context['error'] = "Request timed out. Please check your internet connection."
            except requests.exceptions.RequestException as e:
                context['error'] = "An error occurred while fetching weather data."
            except KeyError: 
                context['error'] = "Error processing weather data. Please try again."
        else:
            context['error'] = "Please enter a city name."
    
    return render(request, 'weather/index.html', context)