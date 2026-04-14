weather_data = {
    "chennai": {"temp": 32, "humidity": 70, "condition": "Sunny", "wind": 12},
    "mumbai": {"temp": 30, "humidity": 80, "condition": "Cloudy", "wind": 10},
    "delhi": {"temp": 35, "humidity": 60, "condition": "Hot", "wind": 8},
    "bangalore": {"temp": 28, "humidity": 65, "condition": "Rainy", "wind": 9}
}

def get_weather(city):
    city = city.lower()
    
    if city in weather_data:
        data = weather_data[city]
        
        print("\n------ Weather Report ------")
        print(f"City: {city.title()}")
        print(f"Temperature: {data['temp']} °C")
        print(f"Humidity: {data['humidity']} %")
        print(f"Condition: {data['condition']}")
        print(f"Wind Speed: {data['wind']} km/h")
    else:
        print("\nCity not found in database!")

city_name = input("Enter city name: ")
get_weather(city_name)
