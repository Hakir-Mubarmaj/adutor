import requests
import json
import geocoder
import datetime

def get_location():
    try:
        location = geocoder.ip('me')
        return location
    except Exception as e:
        print(f"Error getting location: {str(e)}")
        return None

def calculate_daily_max_min_temperature(hourly_temperature):
    # Calculate the maximum and minimum temperatures for the day
    max_temp = max(hourly_temperature)
    min_temp = min(hourly_temperature)
    return max_temp, min_temp

def get_temp(location):
    if location is None:
        return "Unable to determine location. Please check your internet connection."

    base_url = "https://api.open-meteo.com/v1/forecast"
    lat, lon = location.latlng
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
    }

    try:
        response = requests.get(base_url, params=params)
        data = json.loads(response.text)

        if 'hourly' in data:
            hourly_temperature = data['hourly']['temperature_2m']

            # Calculate daily max and min temperature
            max_temp, min_temp = calculate_daily_max_min_temperature(hourly_temperature)

            weather_message = "Weather Update\n"
            weather_message += f"Today's Max Temperature: {max_temp}°C\n"
            weather_message += f"Today's Min Temperature: {min_temp}°C\n"
            return weather_message
        else:
            return "Today's Max Temperature: Not Available\nToday's Min Temperature: Not Available"

    except Exception as e:
        return f"Today's Max Temperature: An error occurred: {str(e)}\n"

def calculate_daily_rain_probability(hourly_rain):
    # Calculate the daily rain probability by summing up the hourly values
    return sum(hourly_rain) / len(hourly_rain)

def get_rain(location):
    if location is None:
        return "Unable to determine location. Please check your internet connection."

    base_url = "https://api.open-meteo.com/v1/forecast"
    lat, lon = location.latlng
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "precipitation_probability",
    }

    try:
        response = requests.get(base_url, params=params)
        data = json.loads(response.text)

        if 'hourly' in data:
            hourly_rain = data['hourly']['precipitation_probability']
            daily_rain_probability = round(calculate_daily_rain_probability(hourly_rain),2)

            weather_message = f"Today's Rain Probability: {daily_rain_probability}%\n"
            return weather_message
        else:
            return "Today's Rain Probability: Not Available\n"

    except Exception as e:
        return f"Today's Rain Probability: An error occurred: {str(e)}\n"
    

def calculate_daily_average_humidity(hourly_humidity):
    # Calculate the daily average humidity by averaging the hourly values
    if hourly_humidity:
        return sum(hourly_humidity) / len(hourly_humidity)
    else:
        return 0  # If there is no hourly data, assume 0% humidity

def get_humidity(location):
    if location is None:
        return "Unable to determine location. Please check your internet connection."

    base_url = "https://api.open-meteo.com/v1/forecast"
    lat, lon = location.latlng
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "humidity_2m",
    }

    try:
        response = requests.get(base_url, params=params)
        data = json.loads(response.text)

        if 'hourly' in data:
            hourly_humidity = data['hourly']['humidity_2m']
            daily_average_humidity = calculate_daily_average_humidity(hourly_humidity)

            weather_message = f"Today's Average Humidity: {daily_average_humidity}%"
            return weather_message
        else:
            return "Today's Average Humidity: Not available"

    except Exception as e:
        return f"Today's Average Humidity: An error occurred: {str(e)}"

location = get_location()
if location is not None:
    weather_info = get_temp(location)
    weather_info += get_rain(location)
    weather_info += get_humidity(location)