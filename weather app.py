import requests

# Replace with your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n------ Weather Report ------")
    print("City:", city_name)
    print("Temperature:", temperature, "°C")
    print("Weather:", weather.title())
    print("Humidity:", humidity, "%")
    print("Wind Speed:", wind_speed, "m/s")

else:
    print("City not found or invalid API key!")
