import requests

q = input("Enter municipality name: ")
app_id = "596992968244cc2ae6bbceae22cdade1"
weather_request = f"https://api.openweathermap.org/data/2.5/weather?q={q}&units=metric&appid={app_id}"
try:
    weather_response = requests.get(weather_request)
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        print(f"Weather: {description}")
        print(f"Temperature: {temperature} Celsius")

except requests.exceptions.RequestException as e:
    print("Something wrong with weather request")

### Version 2
"""
import requests
import json

city_name = input("Enter municipality name: ")
coords_request = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={app_id}"
try:
    response = requests.get(coords_request)
    if response.status_code == 200:
        data = response.json()
        if data:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
        else:
            print("Location not found")
except requests.exceptions.RequestException as e:
    print("Something went wrong")

if lat and lon:
    weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={app_id}"
    try:
        weather_response = requests.get(weather_request)
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            print(f"Weather: {description}")
            print(f"Temperature: {temperature} Celsius")

    except requests.exceptions.RequestException as e:
        print("Something wrong with weather request")
"""