import requests
import json
import sys

API_KEY = '9a7c69538f7815b3d2e9e50a97d3a2e2'
city = input("Enter a city: ")

def get_weather_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors

        weather_data = response.json()
        return weather_data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    except (KeyError, json.JSONDecodeError):
        print("Failed to parse weather data.")
        sys.exit(1)

def display_weather_forecast(city, weather_data):
    main_info = weather_data['weather'][0]['main']
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']

    print(f"Weather forecast for {city}:")
    print(f"Condition: {main_info} ({description})")
    print(f"Temperature: {temperature}K")
    print(f"Humidity: {humidity}%")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a city name as an argument.")
        sys.exit(1)

    city_name = ' '.join(sys.argv[1:])  # Join command-line arguments

    weather_data = get_weather_forecast(city_name)
    display_weather_forecast(city_name, weather_data)
