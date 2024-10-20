import requests
import time

# Define the list of cities to monitor
cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

# Function to fetch weather data using Open-Meteo API
def fetch_weather_data(city):
    # Set the Open-Meteo API URL with latitude and longitude for the city
    city_coordinates = {
        "Delhi": (28.6139, 77.2090),
        "Mumbai": (19.0760, 72.8777),
        "Chennai": (13.0827, 80.2707),
        "Bangalore": (12.9716, 77.5946),
        "Kolkata": (22.5726, 88.3639),
        "Hyderabad": (17.3850, 78.4867),
    }

    lat, lon = city_coordinates[city]
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,weathercode"

    try:
        response = requests.get(weather_url)
        response.raise_for_status()  # Raise an error for bad responses
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data for {city}: {e}")
        return None

def display_weather(weather_data):
    for city, data in weather_data.items():
        if data:
            temperature = data['hourly']['temperature_2m'][0]  # Current temperature
            weather_code = data['hourly']['weathercode'][0]  # Current weather code
            weather_state = "Clear" if weather_code == 0 else "Cloudy"  # Simplified weather state
            print(f"Weather in {city}: {weather_state}, Temperature: {temperature:.2f}°C")

def main():
    print("Weather monitoring system is running...")
    
    while True:
        weather_data = {}
        
        for city in cities:
            print(f"Fetching weather data for {city}...")
            city_weather = fetch_weather_data(city)
            weather_data[city] = city_weather
        
        display_weather(weather_data)
        
        print("\nWaiting for 30 seconds before the next update...\n")
        time.sleep(30)  # Wait for 30 seconds before the next update

if __name__ == "__main__":
    main()
