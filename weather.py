import requests


API_KEY = "465be5f35e14d8a60e58144123d5e4d0"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather is : ", weather)
    print("Temperature : ", temperature, "celsius")
else:
    print("An error occured.")    
