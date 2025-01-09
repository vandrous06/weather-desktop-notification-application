import requests
from plyer import notification
import time

# Function to get weather data
def get_weather_data(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

# Function to send desktop notification
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification duration in seconds
    )

# Main function to fetch and display weather updates
def weather_updates(city, api_key, interval=3600):
    while True:
        weather_data = get_weather_data(city, api_key)
        if weather_data:
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            city_name = weather_data['name']
            weather_message = f"Temperature: {temp}°C\nDescription: {description}"
            send_notification(f"Weather Update: {city_name}", weather_message)
        time.sleep(interval)  # Wait for the specified interval before next update

# Set your parameters here
CITY = "Gulu"
API_KEY = "6857a64d61cfda0a6309007130580e97"
INTERVAL = 120  # 1 hour interval in seconds

# Run the weather update notifications
weather_updates(CITY, API_KEY, INTERVAL)

