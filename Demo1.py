import requests

API_KEYS = "0fa08aa3c9a3f2d5b50214b533a8e308";
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?&appid=0fa08aa3c9a3f2d5b50214b533a8e308&units=metric";


def get_weather(city):
    params = {
        "q" : city,
        "apiid" : API_KEYS,
        "units" : "metric"
    }

    response = requests.get(BASE_URL,params=params)
    data = response.json()


    if response.status_code == 200:
        print(f"n/ weather in {data['name']},{data['sys']['country']}:")
        print(f"Temperature : {data ['main']['temp']}°C")
        print(f" Condition : {data['weather'][0]['description'].capitalize()}")
        print(f" Humidity : {data['main']['humidity']}%" )
        print(f"Wind ")
        print(f"Wind Speed : {data['wind']['speed']}m/s\n")
    else:
        print(f"Errore : {data.get('message','unable to open fetch weather app')}")


if __name__ == '__main__':
    city = input("Enter city name :")
    get_weather(city)