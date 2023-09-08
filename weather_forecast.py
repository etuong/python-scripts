# Script to get a city's weather

import requests


def get_weather_data(json_data, city):
    description_of_weather = json_data['weather'][0]['description']
    weather_type = json_data['weather'][0]['description']
    temperature = json_data['main']['temp']
    wind_speed = json_data['wind']['speed']

    return "The weather in {} is currently {} with a temperature of {} degrees and wind speeds reaching {} km/ph".format(city, weather_type, temperature, wind_speed)


def main():
    api_key = 'a10fd8a212e47edf8d946f26fb4cdef8&q='
    api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=' + api_key
    city = input("City Name : ")
    units_format = "&units=metric"
    final_url = api_address + city + units_format
    json_data = requests.get(final_url).json()
    weather_details = get_weather_data(json_data, city)
    print(weather_details)


main()
